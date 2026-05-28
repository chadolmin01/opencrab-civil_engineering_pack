# civil-supervision-schema

Schema layer for the civil_engineering ontology pack family.

- `civil_engineering.yaml` — pack manifest (26 types, 5 spaces)
- `types/*.yaml` — 26 type schemas with facet axes (material/property/phase/scope/environment)

**Workflow role**: install as the first step of any OpenCRAB Workflow chain. Downstream packs (laws, design, construction, materials, safety, diagnosis) reuse these types and relations.
