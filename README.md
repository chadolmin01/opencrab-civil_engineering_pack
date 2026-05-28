# civil_engineering

Korean civil-engineering qualified-actor decision ontology for OpenCRAB.

## Overview

This pack models how qualified actors in Korean civil engineering — site supervisors, chief supervisors, site engineers, safety managers, chief safety inspectors, and chief precision diagnosers — make regulated decisions about structural components, work types, and facilities.

The decisions covered include material receipt inspection, construction inspection, work permit issuance, stage approval, safety inspection, and precision diagnosis.

## Schema

- **5 spaces**: subject, concept, resource, **decision** (new), outcome
- **26 node types**
- **10 new META_EDGES relations**: `qualified_as`, `grants_authority_for`, `performs`, `targets_component`, `targets_facility`, `targets_work_type`, `based_on`, `depends_on`, `precedes`, `yields`

### Node types

**subject** (qualified actors, 6):
`Supervisor`, `ChiefSupervisor`, `SiteEngineer`, `SafetyManager`, `ChiefSafetyInspector`, `ChiefPrecisionDiagnoser`

**concept** (4):
`Qualification`, `StructuralComponent`, `WorkType`, `Facility`

**resource** (documents and forms, 9):
`Drawing`, `Specification`, `Checklist`, `TestReport`, `WorkPermit`, `ConstructionLog`, `SupervisionLog`, `MaterialReceiptReport`, `SafetyInspectionReport`

**decision** (regulated decision acts, 6):
`MaterialReceiptDecision`, `ConstructionInspectionDecision`, `WorkPermitDecision`, `StageApprovalDecision`, `SafetyInspectionDecision`, `PrecisionDiagnosisDecision`

**outcome** (1):
`DecisionOutcome`

## Bundled graph

The `extracted/` directory contains a pre-built graph:

- **1,150 nodes**
- **1,360 edges**
- 0 grammar violations, 0 orphan edges
- All 26 types and all 10 new relations are instantiated with real data.

Sources:
- 건설기술 진흥법 (Construction Technology Promotion Act) — 본문·시행령·시행규칙
- 시설물의 안전 및 유지관리에 관한 특별법 (Facility Safety Act) — 본문·시행령·시행규칙
- 산업안전보건법 (Occupational Safety and Health Act) — 건설 관련 조항
- 건설사업관리 업무지침, 건설기술인 등급 인정 기준, 감리업무 수행지침서, 주택건설공사 감리업무 세부기준 (MOLIT directives)
- KOSHA P-94 안전작업허가지침
- LH·한국도로공사·국토안전관리원 표준 양식 (검측 체크리스트 6공종, 작업허가서, 자재검수일보, 시공일지, 안전점검 보고서)

## Layout

```
civil_engineering.yaml       — pack manifest
types/                       — 26 type schemas
extracted/
  laws/                      — 7 jsonl
  directives/                — 5 jsonl
  forms/                     — 11 jsonl
```

## Version

`1.0.0`
