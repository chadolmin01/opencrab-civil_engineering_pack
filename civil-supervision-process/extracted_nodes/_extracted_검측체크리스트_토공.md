# Extracted graph — 검측체크리스트_토공.jsonl

_source jsonl: 검측체크리스트_토공.jsonl_

## Nodes

## Node — Checklist / `Checklist:checklist_earthwork_01`
- space: `resource`
- node_type: `Checklist`
- source_article: 검측 체크리스트 — 토공사 표준 머리행
- properties:
  - `name_ko`: 검측 체크리스트 — 토공사 (절토·성토·다짐)
  - `form_code`: 한국도로공사/MOLIT/LH 토공 검측표
  - `issuer`: 한국도로공사 / 국토교통부 / LH
  - `sections`: ["일반정보", "절토 검측", "성토 검측", "다짐 시험 빈도", "시험성과", "종합판정", "서명란"]
  - `sub_works`: ["절토", "성토", "노상", "노체", "다짐", "사면보호"]
  - `key_items`: ["절토 표고 ±50mm (노체 ±30mm)", "성토 1층 두께 노체 ≤300mm/노상 ≤200mm", "함수비 OMC ±2~3%", "다짐도 노체 90%/노상 95%", "롤러 통과 8회 이상", "노상 K30 ≥ 100 MN/m³", "다짐시험 노체 4,000m³/회, 노상 1,000m²/회"]

## Node — WorkType / `WorkType:earthwork`
- space: `concept`
- node_type: `WorkType`
- source_article: 검측 체크리스트 — 토공사 공종
- properties:
  - `name_ko`: 토공사 (절토·성토·다짐)
  - `applicable_standards`: ["KS F 2310", "KS F 2311", "KS F 2312"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_earthwork_site_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 토공사 서명란 시공자
- properties:
  - `name_ko`: 토공사 (절토·성토·다짐) 시공자 자체검측
  - `stage`: site_self_inspection

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_earthwork_supervisor_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 토공사 서명란 감리원
- properties:
  - `name_ko`: 토공사 (절토·성토·다짐) 감리원 검측
  - `stage`: supervisor_inspection

## Node — DecisionOutcome / `DecisionOutcome:checklist_earthwork_outcome_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 검측 체크리스트 — 토공사 종합판정
- properties:
  - `name_ko`: 종합 검측 결과
  - `status`: pass
  - `status_options`: ["pass", "conditional_pass", "fail"]

## Node — SiteEngineer / `SiteEngineer:checklist_earthwork_site_engineer_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 검측 체크리스트 — 토공사 서명란
- properties:
  - `name_ko`: 시공자 (시공기술자/현장대리인)

## Node — Supervisor / `Supervisor:checklist_earthwork_supervisor_subj_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: 검측 체크리스트 — 토공사 서명란
- properties:
  - `name_ko`: 감리원 (건설사업관리기술자)

## Node — ChiefSupervisor / `ChiefSupervisor:checklist_earthwork_chief_subj_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 검측 체크리스트 — 토공사 서명란
- properties:
  - `name_ko`: 책임감리원

## Edges

## Edge — `performs`
- from: `SiteEngineer:checklist_earthwork_site_engineer_01` (subject)
- to: `ConstructionInspectionDecision:checklist_earthwork_site_01` (decision)
- source_article: 검측 체크리스트 — 토공사 서명란 시공자

## Edge — `performs`
- from: `Supervisor:checklist_earthwork_supervisor_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_earthwork_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 토공사 서명란 감리원

## Edge — `performs`
- from: `ChiefSupervisor:checklist_earthwork_chief_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_earthwork_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 토공사 서명란 책임감리원

## Edge — `based_on`
- from: `ConstructionInspectionDecision:checklist_earthwork_supervisor_01` (decision)
- to: `Checklist:checklist_earthwork_01` (resource)
- source_article: 검측 체크리스트 — 토공사 검측 항목

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:checklist_earthwork_supervisor_01` (decision)
- to: `WorkType:earthwork` (concept)
- source_article: 검측 체크리스트 — 토공사 공종

## Edge — `yields`
- from: `ConstructionInspectionDecision:checklist_earthwork_supervisor_01` (decision)
- to: `DecisionOutcome:checklist_earthwork_outcome_01` (outcome)
- source_article: 검측 체크리스트 — 토공사 종합판정

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:checklist_earthwork_supervisor_01` (decision)
- to: `ConstructionInspectionDecision:checklist_earthwork_site_01` (decision)
- source_article: 검측 체크리스트 — 토공사 감리원 검측은 시공자 자체점검 후
