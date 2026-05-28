# civil-construction-specs

**Lifecycle phase**: `CONSTRUCTION`

**Role in workflow chain**: KCS 시공 표준

## Contents

- `sources/` — raw markdown (source-of-truth documents)
- `extracted_nodes/` — grammar-validated node/edge records converted from the seed graph (jsonl→md)

## Boundary rule

Inclusion criterion: documents and extracted records that belong to the `CONSTRUCTION` lifecycle phase of Korean civil-engineering qualified-actor decision-making. Cross-phase documents (e.g. statutes spanning design+construction) are routed to the pack representing their primary lifecycle anchor; downstream packs reference them via Workflow chain.
