# civil-facility-diagnosis

**Lifecycle phase**: `DIAGNOSIS`

**Role in workflow chain**: 시특법 + 안전점검 보고서 + 정밀진단

## Contents

- `sources/` — raw markdown (source-of-truth documents)
- `extracted_nodes/` — grammar-validated node/edge records converted from the seed graph (jsonl→md)

## Boundary rule

Inclusion criterion: documents and extracted records that belong to the `DIAGNOSIS` lifecycle phase of Korean civil-engineering qualified-actor decision-making. Cross-phase documents (e.g. statutes spanning design+construction) are routed to the pack representing their primary lifecycle anchor; downstream packs reference them via Workflow chain.
