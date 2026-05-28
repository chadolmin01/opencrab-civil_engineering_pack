# civil_engineering

Korean civil-engineering qualified-actor decision ontology — a **schema layer** for OpenCRAB.

## What this is

This pack defines the *shape* of qualified-actor decision-making in Korean civil engineering:
- **Who** makes the decision (subject space: 6 actor types)
- **What** is being decided (concept space: qualifications, components, work types, facilities)
- **Which document** grounds the decision (resource space: drawings, specs, checklists, permits, reports, logs)
- **Which decision act** is performed (decision space: 6 decision types — material receipt, construction inspection, work permit, stage approval, safety inspection, precision diagnosis)
- **Which outcome** results (outcome space)

It is **not** a content dump. It is the schema other users install so their own ingested data (site logs, inspection reports, permit forms) automatically maps to a consistent graph structure.

## Schema

- **5 spaces**: subject, concept, resource, **decision** (new), outcome
- **26 node types** with rich property definitions in `types/`
- **10 new META_EDGES relations**: `qualified_as`, `grants_authority_for`, `performs`, `targets_component`, `targets_facility`, `targets_work_type`, `based_on`, `depends_on`, `precedes`, `yields`

## Bundled seed (`extracted/`)

A starter graph extracted from public Korean construction-engineering sources, demonstrating that the schema instantiates with real data:

- **1,308 nodes / 1,549 edges** — 0 grammar violations, 0 orphan edges
- All 26 types and all 10 new relations are exercised at least once.

This is sample/seed data, not the product. When you install the pack and ingest your own corpus, your nodes replace or extend the seed.

Source coverage in seed:
- 건설기술 진흥법 / 시설물 안전 및 유지관리에 관한 특별법 / 산업안전보건법 (건설 관련 조항)
- 건설사업관리 업무지침, 건설기술인 등급 인정 기준, 감리업무 수행지침서, 주택건설공사 감리업무 세부기준
- KOSHA P-94 안전작업허가지침
- KDS 14 20, KDS 14 30, KCS 10 10, KCS 14 20, KCS 14 31 (selected key clauses with quantitative specs)
- Standard forms: inspection checklists (6 work types), work permits, material receipt reports, construction logs, safety inspection reports

## Layout

```
civil_engineering.yaml       — pack manifest
types/                       — 26 type schemas (the schema layer itself)
extracted/
  laws/                      — 7 jsonl
  directives/                — 5 jsonl
  forms/                     — 11 jsonl
  standards/                 — 4 jsonl (KDS/KCS quantitative criteria)
```

## Intended use

Install this pack, then:
1. Ingest your own site corpus (logs, permits, reports). Nodes are typed automatically.
2. Run graph traversal queries: which decisions precede this approval? whose qualification authorizes this permit? what does this report ground?
3. Use as a retrieval source for an LLM (GraphRAG): the LLM answers with verifiable `source_article` citations from the graph, not from its training memory.

## Version

`1.0.0`
