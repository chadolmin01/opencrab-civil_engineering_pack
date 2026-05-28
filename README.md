# civil_engineering

Korean civil-engineering qualified-actor decision ontology — a **schema layer** for OpenCRAB.

## What this pack is

This pack defines the *shape* of qualified-actor decision-making in Korean civil engineering. It is a schema layer that other users install so that their own ingested data (site logs, inspection reports, permit forms) automatically maps to a consistent graph structure.

It is **not** primarily a content dump. The bundled `extracted/` graph is sample/seed data — when you install the pack and ingest your own corpus, the OpenCRAB LLM extractor uses this schema to classify your nodes and edges automatically.

## Schema

- **5 spaces**: subject, concept, resource, **decision** (new), outcome
- **26 node types** (see `types/` for each schema)
- **10 new META_EDGES relations**: `qualified_as`, `grants_authority_for`, `performs`, `targets_component`, `targets_facility`, `targets_work_type`, `based_on`, `depends_on`, `precedes`, `yields`

### Faceted classification

Each type schema declares **orthogonal facet axes** beyond the type itself. The OpenCRAB extractor fills these axes at ingest time to enable cross-domain node matching:

| Facet | Examples |
|---|---|
| `topic_material` | concrete · steel · rebar · aggregate · cement · soil · rock · asphalt · timber · composite · mixed |
| `topic_property` | strength · slump · fatigue · durability · stability · safety · dimension · tolerance · settlement · vibration · thermal · corrosion · fire |
| `topic_phase` | planning · design · material_acceptance · construction · inspection · approval · commissioning · maintenance · diagnosis · demolition |
| `topic_scope` | material · specimen · joint · member · assembly · structure · facility · site · project |
| `topic_environment` | normal · cold_weather · hot_weather · rainy · windy · snowy · seismic · underwater · underground · marine |

Per Ranganathan-style faceted classification (Hogan et al. 2021, Pan et al. 2024): a type alone is not enough for cross-domain matching. Two entities with different types (e.g. a Specification and a MaterialReceiptDecision) but the same facets (`material=concrete, property=strength, phase=material_acceptance`) are matched as semantically aligned.

### Node-type → applicable facet axes

Not all facets apply to every type. Each `types/<Name>.yaml` declares the relevant axes:

| Type group | Applicable facets |
|---|---|
| subject (Supervisor / ChiefSupervisor / SiteEngineer / SafetyManager / ChiefSafetyInspector / ChiefPrecisionDiagnoser) | phase, scope (SafetyManager also environment) |
| concept (Qualification, StructuralComponent, WorkType, Facility) | varies |
| resource (Specification, Drawing, Checklist, TestReport, WorkPermit, ConstructionLog, SupervisionLog, MaterialReceiptReport, SafetyInspectionReport) | up to all 5 (Specification has all 5) |
| decision (six ~Decision types) | up to all 5 (varies per decision phase) |
| outcome (DecisionOutcome) | phase, scope |

## Bundled seed (`extracted/`)

A starter graph extracted from public Korean construction-engineering sources, demonstrating that the schema instantiates with real data:

- Source coverage:
  - **laws** — 건설기술 진흥법 · 시설물 안전 및 유지관리에 관한 특별법 · 산업안전보건법(건설 관련)
  - **directives** — CM 업무지침 · 건설기술인 등급 인정 기준 · 감리업무 수행지침서 · 주택건설공사 감리업무 세부기준 · KOSHA 안전작업허가지침 P-94
  - **forms** — 검측 체크리스트(6공종) · 작업허가서 · 자재검수일보 · 시공일지 · 안전점검 보고서
  - **standards/kds** — KDS 11 (지반), KDS 14 20 (콘크리트구조), KDS 14 30/31 (강구조 설계+시공)
  - **standards/ks** — KS F 4009/2403/2405/2402/2526, KS D 3504/3503, KS B 0801/0802/0896
  - **standards/kcs** — KCS 14 20 (콘크리트공사), KCS 14 31 (강구조공사), KCS 21 50 (거푸집·동바리), KCS 11 30 (연약지반), KCS 21 60 (비계·가시설)
- Coverage axes:
  - Design criteria (φ values, fy/fck limits, anchor lengths, retaining-wall safety factors)
  - Material standards (SD400 fy, SS275 graded, slump tolerance, specimen dimensions, UT acceptance)
  - Construction practice (cold-joint time, weather exceptions, form/shore removal, curing, weld preheat, scaffold wind-stop)

This is sample/seed data. Production usage: install the pack, then ingest your own corpus.

## Layout

```
opencrab_ingest/             ← SaaS canonical ingest dir (chunked raw text)
  chunks.jsonl                 132 sources / 1,108 text chunks
  manifest.json                source-level metadata (sha256, bytes, chars)
  manifest.csv                 same, CSV form
civil_engineering.yaml       — pack manifest (26 types, 5 spaces)
types/                       — 26 type schemas with facet axes
extracted/                   — bundled pre-extracted seed graph (optional)
  laws/         7 jsonl
  directives/  ~8 jsonl
  forms/       11 jsonl
  standards/
    KCS_*.jsonl (4)            first-pass KCS/KDS clauses
    ks/         ~2 jsonl       KS material/test standards
    kcs/        ~3 jsonl       KCS construction specifications
    kds/        ~6 jsonl       KDS design standards (concrete/steel/geotech)
```

The `opencrab_ingest/` directory is the SaaS-canonical entry point: raw text chunks the OpenCRAB LLM extractor can directly run its 6-stage pipeline on. The `extracted/` directory holds pre-extracted node/edge seeds that the extractor may augment or override.

## Intended use

1. Install this pack into an OpenCRAB workspace.
2. Ingest your own corpus (site logs, permits, reports, drawings).
3. The OpenCRAB LLM extractor uses the type schemas + facet axes to classify nodes and emit edges.
4. Query the resulting graph either directly (Cypher-style traversal) or via an LLM with the graph as the retrieval source.

## Version

`1.0.0`
