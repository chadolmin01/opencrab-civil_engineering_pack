# civil-laws

**Lifecycle phase**: `DESIGN+`

**Role in workflow chain**: 법령 본문 (건진법·시특법·산안법)

## Contents

- `sources/` — raw markdown (source-of-truth documents)
- `extracted_nodes/` — grammar-validated node/edge records converted from the seed graph (jsonl→md)

## Boundary rule

Inclusion criterion: documents and extracted records that belong to the `DESIGN+` lifecycle phase of Korean civil-engineering qualified-actor decision-making. Cross-phase documents (e.g. statutes spanning design+construction) are routed to the pack representing their primary lifecycle anchor; downstream packs reference them via Workflow chain.
