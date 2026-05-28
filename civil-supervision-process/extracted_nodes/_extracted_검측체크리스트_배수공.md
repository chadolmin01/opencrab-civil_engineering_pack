# Extracted graph — 검측체크리스트_배수공.jsonl

_source jsonl: 검측체크리스트_배수공.jsonl_

## Nodes

## Node — Checklist / `Checklist:checklist_drainage_01`
- space: `resource`
- node_type: `Checklist`
- source_article: 검측 체크리스트 — 배수공 표준 머리행
- properties:
  - `name_ko`: 검측 체크리스트 — 배수공 (맹암거·측구·집수정·U형 배수로)
  - `form_code`: 한국도로공사/철도공단/LH 배수공 검측표
  - `issuer`: 한국도로공사 / 국가철도공단 / LH
  - `sections`: ["일반정보", "일반 검측", "맹암거", "측구/집수정", "시험성과", "종합판정", "서명란"]
  - `sub_works`: ["측구", "맹암거", "종배수", "횡배수", "집수정", "U형 배수"]
  - `key_items`: ["굴착 깊이 ±30mm", "종단경사 최소 0.3% 이상", "기초 다짐도 ≥ 90%", "유공관 KS M 3408", "부직포 200 g/㎡", "측구 콘크리트 fck ≥ 24 MPa", "이음부 지수재 처리", "뒷채움 다짐도 ≥ 90%"]

## Node — WorkType / `WorkType:drainage`
- space: `concept`
- node_type: `WorkType`
- source_article: 검측 체크리스트 — 배수공 공종
- properties:
  - `name_ko`: 배수공
  - `applicable_standards`: ["KS M 3408", "KS D 3504"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_drainage_site_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 배수공 서명란 시공자
- properties:
  - `name_ko`: 배수공 시공자 자체검측
  - `stage`: site_self_inspection

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_drainage_supervisor_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 배수공 서명란 감리원
- properties:
  - `name_ko`: 배수공 감리원 검측
  - `stage`: supervisor_inspection

## Node — DecisionOutcome / `DecisionOutcome:checklist_drainage_outcome_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 검측 체크리스트 — 배수공 종합판정
- properties:
  - `name_ko`: 종합 검측 결과
  - `status`: pass
  - `status_options`: ["pass", "conditional_pass", "fail"]

## Node — SiteEngineer / `SiteEngineer:checklist_drainage_site_engineer_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 검측 체크리스트 — 배수공 서명란
- properties:
  - `name_ko`: 시공자 (시공기술자/현장대리인)

## Node — Supervisor / `Supervisor:checklist_drainage_supervisor_subj_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: 검측 체크리스트 — 배수공 서명란
- properties:
  - `name_ko`: 감리원 (건설사업관리기술자)

## Node — ChiefSupervisor / `ChiefSupervisor:checklist_drainage_chief_subj_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 검측 체크리스트 — 배수공 서명란
- properties:
  - `name_ko`: 책임감리원

## Edges

## Edge — `performs`
- from: `SiteEngineer:checklist_drainage_site_engineer_01` (subject)
- to: `ConstructionInspectionDecision:checklist_drainage_site_01` (decision)
- source_article: 검측 체크리스트 — 배수공 서명란 시공자

## Edge — `performs`
- from: `Supervisor:checklist_drainage_supervisor_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_drainage_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 배수공 서명란 감리원

## Edge — `performs`
- from: `ChiefSupervisor:checklist_drainage_chief_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_drainage_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 배수공 서명란 책임감리원

## Edge — `based_on`
- from: `ConstructionInspectionDecision:checklist_drainage_supervisor_01` (decision)
- to: `Checklist:checklist_drainage_01` (resource)
- source_article: 검측 체크리스트 — 배수공 검측 항목

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:checklist_drainage_supervisor_01` (decision)
- to: `WorkType:drainage` (concept)
- source_article: 검측 체크리스트 — 배수공 공종

## Edge — `yields`
- from: `ConstructionInspectionDecision:checklist_drainage_supervisor_01` (decision)
- to: `DecisionOutcome:checklist_drainage_outcome_01` (outcome)
- source_article: 검측 체크리스트 — 배수공 종합판정

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:checklist_drainage_supervisor_01` (decision)
- to: `ConstructionInspectionDecision:checklist_drainage_site_01` (decision)
- source_article: 검측 체크리스트 — 배수공 감리원 검측은 시공자 자체점검 후
