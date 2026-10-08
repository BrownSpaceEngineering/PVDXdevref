"""Ingest and search the PVDX datasheets.

  uv run main.py ingest [--no-embed] [--index-only]
  uv run main.py search "WHO_AM_I register" [-k 8] [--part 9-axis]
"""
import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "original"
OUT = ROOT / "markdown"
MANIFEST = OUT / ".manifest.json"
DB = ROOT / "index" / "index.sqlite"
MODEL = "BAAI/bge-small-en-v1.5"
MAX_CHARS = 3000  # about 800 tokens
TEXT_EXT = {".md", ".txt", ".c", ".h"}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _convert_range(args):
    pdf, pages = args
    import onnxruntime as ort

    # The layout model builds its sessions with default options, which use every core per
    # session. With one worker per core that thrashes, so cap each session at one thread.
    class OneThread(ort.InferenceSession):
        def __init__(self, path, sess_options=None, *a, **k):
            so = sess_options or ort.SessionOptions()
            so.intra_op_num_threads = so.inter_op_num_threads = 1
            super().__init__(path, sess_options=so, *a, **k)

    ort.InferenceSession = OneThread
    import pymupdf4llm

    out = pymupdf4llm.to_markdown(pdf, pages=pages, page_chunks=True, show_progress=False)
    return [p["text"] for p in out]


def convert(pdf):
    """PDF -> list of (page number, markdown). Pages are split across CPU cores.
    Swap this function to change converter."""
    import pymupdf
    from concurrent.futures import ProcessPoolExecutor, as_completed

    with pymupdf.open(pdf) as doc:
        n = len(doc)
    workers = min(os.cpu_count() or 1, max(1, n // 10))
    step = -(-n // (workers * 4))  # about 4 slices per worker keeps them evenly loaded
    jobs = [(str(pdf), list(range(i, min(i + step, n)))) for i in range(0, n, step)]
    print(f"  {n} pages, {workers} workers, {len(jobs)} slices", flush=True)
    results, done = {}, 0
    with ProcessPoolExecutor(workers) as pool:
        futures = {pool.submit(_convert_range, j): k for k, j in enumerate(jobs)}
        for f in as_completed(futures):
            k = futures[f]
            results[k] = f.result()
            done += len(results[k])
            print(f"  converted {done}/{n} pages", flush=True)
    texts = [t for k in sorted(results) for t in results[k]]
    # PDF text can hold lone surrogates, which utf-8 cannot encode
    return [(i + 1, t.encode("utf-8", "replace").decode("utf-8")) for i, t in enumerate(texts)]


def chunk(pages):
    """Yield (page, heading path, text). Split on headings, then on paragraphs."""
    heading = ""
    for page, text in pages:
        buf = []

        def flush():
            body = "\n".join(buf).strip()
            buf.clear()
            while body:
                if len(body) <= MAX_CHARS:
                    cut = len(body)
                else:
                    cut = body.rfind("\n\n", 0, MAX_CHARS)
                    cut = cut if cut > 0 else MAX_CHARS
                yield page, heading, body[:cut].strip()
                body = body[cut:].strip()

        for line in text.splitlines():
            m = re.match(r"#{1,6}\s+(.*)", line)
            if m:
                yield from flush()
                heading = m.group(1).strip("* ")
            buf.append(line)
        yield from flush()


def sources():
    """Map each input file to its markdown output path."""
    for f in sorted(SRC.rglob("*")):
        if not f.is_file():
            continue
        ext = f.suffix.lower()
        if ext == ".pdf":
            yield f, OUT / f.relative_to(SRC).with_suffix(".md")
        elif ext in TEXT_EXT:
            yield f, OUT / f.relative_to(SRC)
        elif ext == ".docx" and f.with_suffix(".pdf").exists():
            continue
        else:
            print(f"skip (unsupported): {f.relative_to(ROOT)}")


def connect():
    DB.parent.mkdir(exist_ok=True)
    db = sqlite3.connect(DB)
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS indexed(path TEXT PRIMARY KEY, hash TEXT, embedded INT);
        CREATE TABLE IF NOT EXISTS chunks(
            id INTEGER PRIMARY KEY, path TEXT, part TEXT, page INT,
            heading TEXT, text TEXT, emb BLOB);
        CREATE VIRTUAL TABLE IF NOT EXISTS fts USING fts5(
            heading, text, content='chunks', content_rowid='id');
        """
    )
    return db


class Embedder:
    """Same model on every backend, so vectors from a GPU machine work on a CPU machine."""

    def __init__(self):
        mode = os.environ.get("PVDX_EMBED", "auto")  # auto | gpu | cpu
        self.st = None
        if mode in ("auto", "gpu"):
            try:
                import torch
                from sentence_transformers import SentenceTransformer

                if torch.cuda.is_available():
                    self.st = SentenceTransformer(MODEL, device="cuda")
                    self.st.half()
                    print(f"embedding on GPU: {torch.cuda.get_device_name(0)}")
            except ImportError:
                pass
            if mode == "gpu" and self.st is None:
                sys.exit("PVDX_EMBED=gpu but no usable CUDA GPU: uv sync --extra gpu")
        if self.st is None:
            from fastembed import TextEmbedding

            self.fe = TextEmbedding(MODEL)

    def embed(self, texts, batch=64):
        """Yield one float32 vector per text, printing progress."""
        for i in range(0, len(texts), batch):
            part = texts[i : i + batch]
            if self.st is not None:
                vecs = self.st.encode(part, batch_size=batch, normalize_embeddings=True)
            else:
                vecs = list(self.fe.embed(part, batch_size=batch))
            yield from vecs
            print(f"  embedded {min(i + batch, len(texts))}/{len(texts)}", flush=True)


def embedder():
    try:
        return Embedder()
    except ImportError:
        return None


def load_manifest():
    return json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}


def convert_all():
    """original/ -> markdown/. Skips files whose hash is in the committed manifest."""
    manifest, seen, n = load_manifest(), set(), 0
    for src, md in sources():
        rel = str(src.relative_to(ROOT))
        seen.add(rel)
        h = sha(src)
        if manifest.get(rel) == h and md.exists():
            continue
        print(f"convert: {rel}")
        md.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() == ".pdf":
            pages = convert(src)
            md.write_text(
                f"# {src.stem}\n\n*Source: `{rel}` ({len(pages)} pages)*\n\n"
                + "\n\n".join(f"<!-- page {p} -->\n\n{t}" for p, t in pages)
            )
        else:
            md.write_text(src.read_text(errors="replace"))
        manifest[rel] = h
        MANIFEST.write_text(json.dumps(manifest, indent=1, sort_keys=True))
        n += 1
    for gone in set(manifest) - seen:
        manifest.pop(gone)
    MANIFEST.write_text(json.dumps(manifest, indent=1, sort_keys=True))
    return n


def split_pages(text):
    parts = re.split(r"<!-- page (\d+) -->", text)
    if len(parts) == 1:
        return [(1, text)]
    return [(int(p), t) for p, t in zip(parts[1::2], parts[2::2])]


def remove(db, path):
    db.execute(
        "INSERT INTO fts(fts, rowid, heading, text) SELECT 'delete', id, heading, text FROM chunks WHERE path=?",
        (path,),
    )
    db.execute("DELETE FROM chunks WHERE path=?", (path,))
    db.execute("DELETE FROM indexed WHERE path=?", (path,))


def index_all(embed):
    """markdown/ -> index. Needs no PDFs and, with embed=False, no model."""
    import numpy as np

    db = connect()
    done = {p: (h, e) for p, h, e in db.execute("SELECT path, hash, embedded FROM indexed")}
    model = embedder() if embed else None
    if embed and model is None:
        print("fastembed not installed: building keyword index only (uv sync --extra embed or --extra gpu to add vectors)")
    seen, n = set(), 0
    for md in sorted(OUT.rglob("*")):
        if not md.is_file() or md.suffix not in {".md", *TEXT_EXT} or md.name == "INDEX.md":
            continue
        path = str(md.relative_to(ROOT))
        seen.add(path)
        h = sha(md)
        if path in done and done[path][0] == h and (done[path][1] or model is None):
            continue
        print(f"index: {path}")
        rows = list(chunk(split_pages(md.read_text(errors="replace"))))
        old = {t: e for t, e in db.execute("SELECT text, emb FROM chunks WHERE path=? AND emb IS NOT NULL", (path,))}
        remove(db, path)
        embs = [old.get(t) for _, _, t in rows]
        todo = [i for i, e in enumerate(embs) if e is None]
        if model and todo:
            texts = [f"{rows[i][1]}\n{rows[i][2]}" for i in todo]
            for i, e in zip(todo, model.embed(texts)):
                embs[i] = np.asarray(e, np.float32).tobytes()
        part = md.relative_to(OUT).parts[0]
        for (page, hd, t), e in zip(rows, embs):
            cur = db.execute(
                "INSERT INTO chunks(path, part, page, heading, text, emb) VALUES(?,?,?,?,?,?)",
                (path, part, page, hd, t, e),
            )
            db.execute("INSERT INTO fts(rowid, heading, text) VALUES(?,?,?)", (cur.lastrowid, hd, t))
        db.execute("INSERT INTO indexed VALUES(?,?,?)", (path, h, int(model is not None)))
        db.commit()
        n += 1
    for gone in set(done) - seen:
        remove(db, gone)
    db.commit()
    total = db.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    print(f"index: {n} files indexed, {total} chunks")


def ingest(embed=True, convert_pdfs=True):
    if convert_pdfs:
        print(f"convert: {convert_all()} files converted")
    index_all(embed)
    write_index()


def write_index():
    lines = [
        "# PVDX Datasheet Index",
        "",
        "Generated by `uv run main.py ingest`. Do not edit by hand.",
        "Search with `uv run main.py search \"<query>\"`. Page markers look like `<!-- page N -->`.",
        "",
    ]
    for part in sorted(p for p in OUT.iterdir() if p.is_dir()):
        lines += [f"## {part.name}", ""]
        for f in sorted(part.rglob("*.md")):
            lines.append(f"- `{f.relative_to(OUT)}`")
        lines.append("")
    (OUT / "INDEX.md").write_text("\n".join(lines))


def search(query, k=8, part=None):
    db = connect()
    rows = db.execute(
        "SELECT id, path, part, page, heading, text, emb FROM chunks"
        + (" WHERE part=?" if part else ""),
        (part,) if part else (),
    ).fetchall()
    if not rows:
        sys.exit("index is empty: run `uv run main.py ingest --no-embed`")
    byid = {r[0]: r for r in rows}
    rankings = []
    # keyword ranking (BM25): always available
    words = re.findall(r"[A-Za-z0-9_]+", query)
    if words:
        match = " OR ".join(f'"{w}"' for w in words)
        rankings.append([r[0] for r in db.execute(
            "SELECT rowid FROM fts WHERE fts MATCH ? ORDER BY bm25(fts) LIMIT 100", (match,))
            if r[0] in byid])
    # vector ranking (cosine): only if vectors exist and fastembed is installed
    withvec = [r for r in rows if r[6] is not None]
    model = embedder() if withvec else None
    if model:
        import numpy as np

        q = np.asarray(next(iter(model.embed([query]))), np.float32)
        mat = np.stack([np.frombuffer(r[6], np.float32) for r in withvec])
        sims = mat @ q / (np.linalg.norm(mat, axis=1) * np.linalg.norm(q) + 1e-9)
        rankings.append([withvec[i][0] for i in np.argsort(-sims)[:100]])
    else:
        print("(keyword search only: no vectors, or no embedding package installed)\n", file=sys.stderr)
    # reciprocal rank fusion
    score = {}
    for ranking in rankings:
        for rank, i in enumerate(ranking):
            score[i] = score.get(i, 0) + 1 / (60 + rank)
    for i in sorted(score, key=score.get, reverse=True)[:k]:
        _, path, prt, page, hd, text, _ = byid[i]
        print(f"## {path} (page {page}) [{prt}] {hd}\n\n{text}\n\n---\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("ingest", help="convert original/ to markdown/ and build the index")
    g.add_argument("--no-embed", action="store_true", help="keyword index only, no model")
    g.add_argument("--index-only", action="store_true", help="skip PDF conversion; index markdown/ as is")
    s = sub.add_parser("search", help="search the index")
    s.add_argument("query")
    s.add_argument("-k", type=int, default=8)
    s.add_argument("--part", help="limit to one folder in original/")
    a = ap.parse_args()
    if a.cmd == "ingest":
        ingest(embed=not a.no_embed, convert_pdfs=not a.index_only)
    else:
        search(a.query, a.k, a.part)


if __name__ == "__main__":
    main()
