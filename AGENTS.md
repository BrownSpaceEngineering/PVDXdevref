# PVDX peripheral reference

This repo holds datasheets for the PVDX cubesat peripherals, converted to Markdown.

To answer a hardware question:

1. Run `uv run main.py search "<query>" [-k 8] [--part <folder>]`. If you know the exact register or pin name, put it in the query.
2. Read the file and page that the result cites. Page markers in the files look like `<!-- page N -->`.
3. Use `markdown/INDEX.md` to see which parts exist.

If you cannot run the embedding ingest/it is running too slow, just search via the markdown index.

Board schematics and layouts (KiCad) are in `boards/`. See `boards/README.md`. The `.kicad_sch` files are plain text, so you can grep them for nets, reference designators, and part values. Ingest does not index them.

Do not edit files in `markdown/` or `index/`. The command `uv run main.py ingest` generates them from `original/`.
