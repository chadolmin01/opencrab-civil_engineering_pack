# civil_engineering — v1.4 — pre-extracted seed graph

Pre-extracted node/edge jsonl from public Korean civil-engineering corpus:
- `extracted/laws/` — 7 jsonl
- `extracted/directives/` — 5 jsonl (some split into parts to stay under 200 records)
- `extracted/forms/` — 11 jsonl
- `extracted/standards/` — KCS · KDS · KS · KCS first-pass extraction

Each record carries source_article references and grammar-validated (space, node_type) / (from_space, to_space, relation) per the manifest in v1.0.

This is bonus seed data — the OpenCRAB extractor in v1.1–v1.3 ingest passes generates its own graph from raw markdown, but v1.4 provides a verified baseline.
