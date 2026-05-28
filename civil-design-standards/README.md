# civil-design-standards

**Lifecycle phase**: `DESIGN`

**Role in workflow chain**: KDS 설계기준 (토목 한정)

## Contents

- `sources/` — raw markdown (source-of-truth documents)
- `extracted_nodes/` — grammar-validated node/edge records converted from the seed graph (jsonl→md)

## Boundary rule

Inclusion criterion: documents and extracted records that belong to the `DESIGN` lifecycle phase of Korean civil-engineering qualified-actor decision-making. Cross-phase documents (e.g. statutes spanning design+construction) are routed to the pack representing their primary lifecycle anchor; downstream packs reference them via Workflow chain.
