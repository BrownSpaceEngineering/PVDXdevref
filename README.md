# PVDX device reference

Datasheets for the PVDX cubesat peripherals w/ RAG

## Add a datasheet

1. Copy the PDF into `original/<peripheral>/`.
2. Run `uv run main.py ingest`.
3. Commit the new files in `original/` and `markdown/`.

The ingest step converts only new or changed files, so a second run is fast.

## GPU Acceleration

You can go super fast crazy mode by running on GPU if you have a CUDA-compatible NVIDIA gpu.
Run `uv run --extra gpu python -u main.py ingest`.

## Search

```
uv run main.py search "WHO_AM_I register" -k 5 --part 9-axis
```

## Layout

- `original/` source files provided by humans
- `markdown/` generated Markdown
- `index/` ingest-generated search index

## Note on Datasheet Availability

All datasheets are made available in `original/` to the public except for those pertaining
to the CUBECOM STX-G2/VESTALINK, which are provided to BSE by CUBECOM. If you need these,
please request them from Alex Khosrowshahi (spoonmilk) or Alicia Wu.

