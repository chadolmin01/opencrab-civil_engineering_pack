# civil_engineering — OpenCRAB ontology pack (7 use-case sub-packs)

Korean civil-engineering qualified-actor decision ontology, split into seven semantic sub-packs designed to chain together inside an OpenCRAB Workflow.

## Sub-packs (each independently ingestable)

| Path | Role |
|---|---|
| [`civil-supervision-schema/`](./civil-supervision-schema) | Schema layer (26 types, 10 relations, 5 facet axes). Use first in any chain. |
| [`civil-laws/`](./civil-laws) | Korean primary laws (건진법) |
| [`civil-design-standards/`](./civil-design-standards) | KDS design standards (concrete/steel/geotech/seismic) |
| [`civil-construction-process/`](./civil-construction-process) | KCS construction specs + supervision directives + inspection forms |
| [`civil-materials-tests/`](./civil-materials-tests) | KS material + test standards + 자재검수일보 |
| [`civil-safety-permits/`](./civil-safety-permits) | 산안법 + KOSHA P-94 + 작업허가서 |
| [`civil-facility-diagnosis/`](./civil-facility-diagnosis) | 시특법 + 안전점검 보고서 |

## Workflow chain example — 시공 의사결정 검증

```
input: 시공일지 한 단락
  ↓ civil-supervision-schema  → 자격자·결정 type 분류
  ↓ civil-construction-process → 시공 단계 매칭
  ↓ civil-materials-tests      → 자재 검수 요건 확인
  ↓ civil-design-standards     → 설계 기준 매칭
  ↓ civil-safety-permits       → 안전·허가 위반 detect
  ↓ civil-laws                 → 법령 조항 인용
output: 검증 리포트 (누락된 결정 + 위반 조항 + 권장 조치 + 자격자 책임)
```

## Bundled `extracted/`

The repo root keeps an `extracted/` directory with pre-extracted node/edge jsonl for offline verification. Not part of any single sub-pack — provided as a verified seed graph aligned with the schema layer.

## Schema highlights

- 5 spaces: subject, concept, resource, **decision** (new), outcome
- 26 node types with faceted classification axes
- 10 new META_EDGES relations (`qualified_as`, `performs`, `based_on`, `depends_on`, `precedes`, `yields`, etc.)

## Ingest

In OpenCRAB GitHub ingest UI, set Path to one sub-pack folder per run. Each sub-pack creates its own ontology pack in your workspace, ready to be wired into a Workflow.

## Version

`1.0.0`
