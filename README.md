# civil_engineering — OpenCRAB ontology pack (multi-version)

Korean civil-engineering qualified-actor decision ontology — split into ingest-sized sub-versions to fit OpenCRAB SaaS document limits per ingest run.

## How to ingest

In OpenCRAB GitHub ingest UI:
- URL: `https://github.com/chadolmin01/opencrab-civil_engineering_pack`
- Branch: `main`
- Path: choose one of `v1.0`, `v1.1`, `v1.2`, `v1.3`, `v1.4` per ingest run

Ingest in order: **v1.0 → v1.1 → v1.2 → v1.3 → v1.4**. Each ingest adds to the same workspace.

## Versions

| Version | Contents | Files |
|---|---|---|
| `v1.0/` | Schema only (26 types + manifest) | ~28 |
| `v1.1/` | Laws + directives + forms (Korean primary sources) | ~23 |
| `v1.2/` | KDS design standards (markdown corpus) | ~75 |
| `v1.3/` | KCS construction specs + KS material/test standards | ~30 |
| `v1.4/` | Pre-extracted seed graph (jsonl) | ~44 |

## Schema

- 5 spaces: subject, concept, resource, **decision** (new), outcome
- 26 node types with faceted classification axes (material/property/phase/scope/environment)
- 10 new META_EDGES relations (qualified_as, performs, based_on, depends_on, precedes, yields, etc.)

## Version 1.0.0
