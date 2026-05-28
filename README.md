# civil_engineering — OpenCRAB ontology pack (lifecycle-phase sub-packs)

Korean civil-engineering qualified-actor decision ontology, split along **construction lifecycle phase** to give each sub-pack a clear, non-overlapping boundary.

## Lifecycle phase axis (sub-pack layout)

| Phase | Sub-pack | Inclusion rule |
|---|---|---|
| SCHEMA       | `civil-supervision-schema/`   | 26 node types + 10 relations + 5 facet axes — installed first as grammar layer |
| DESIGN+      | `civil-laws/`                 | Korean primary statutes (건진법·시특법·산안법 본문 + 시행령·시행규칙) — cross-phase |
| DESIGN       | `civil-design-standards/`     | KDS design standards (concrete, steel, geotech, seismic, scaffolding — civil only, KDS 41 excluded) |
| MATERIAL     | `civil-materials-tests/`      | KS material + test standards (F·D·B) + 자재검수일보 |
| CONSTRUCTION | `civil-construction-specs/`   | KCS construction specifications (시공 표준) |
| CONSTRUCTION | `civil-supervision-process/`  | CM·감리·주택건설감리 지침 + 검측 체크리스트 + 시공일지 |
| SAFETY       | `civil-safety-permits/`       | KOSHA P-94 + 작업허가서 + 산안법 건설 발췌 |
| DIAGNOSIS    | `civil-facility-diagnosis/`   | 시특법 시설물 안전·유지관리 + 안전점검 보고서 + 정밀진단 |

Each sub-pack carries:
- `sources/` — raw markdown (laws, standards, directives, forms)
- `extracted_nodes/` — grammar-validated nodes/edges from the seed graph, converted to per-record markdown

## Workflow chain (example)

```
input: 시공 자료 (시공일지·검측·작업허가서 등)
  ↓ civil-supervision-schema    (그래머 layer)
  ↓ civil-supervision-process   (시공·감리 절차)
  ↓ civil-materials-tests       (자재 검수 요건)
  ↓ civil-construction-specs    (KCS 시공 기준)
  ↓ civil-design-standards      (KDS 설계 기준)
  ↓ civil-safety-permits        (안전·허가)
  ↓ civil-laws                  (법령 근거)
output: 결정 사슬 검증 리포트 (누락된 결정 + 위반 조항 + 책임 자격자)
```

`civil-facility-diagnosis` is a separate chain for maintenance / safety inspection workflows on existing facilities.

## Ingest

Set Path to one sub-pack folder per ingest run in OpenCRAB GitHub ingest UI. Each ingest produces an independent ontology pack in your workspace, ready to be wired into the Workflow agent.

## Schema highlights

- 5 spaces: subject, concept, resource, **decision** (new), outcome
- 26 node types with faceted classification axes (material/property/phase/scope/environment)
- 10 new META_EDGES relations (`qualified_as`, `performs`, `based_on`, `depends_on`, `precedes`, `yields`, `targets_*`, `grants_authority_for`, `subclass_of`)

## Version

`1.0.0`
