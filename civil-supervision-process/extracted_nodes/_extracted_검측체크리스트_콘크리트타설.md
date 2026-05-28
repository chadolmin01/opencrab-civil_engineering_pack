# Extracted graph — 검측체크리스트_콘크리트타설.jsonl

_source jsonl: 검측체크리스트_콘크리트타설.jsonl_

## Nodes

## Node — Checklist / `Checklist:checklist_concrete_01`
- space: `resource`
- node_type: `Checklist`
- source_article: 검측 체크리스트 — 콘크리트 타설 표준 머리행
- properties:
  - `name_ko`: 검측 체크리스트 — 콘크리트 타설(타설 전·중·후)
  - `form_code`: MOLIT/LH 콘크리트 타설 검측표
  - `issuer`: 국토교통부 / LH
  - `sections`: ["일반정보", "타설 전", "타설 중", "타설 후", "시험성과", "종합판정", "서명란"]
  - `key_items`: ["거푸집 청소/박리제", "철근 배근 (피복/이음)", "레미콘 배합표/운반시간 90분 이내", "슬럼프 ±25mm", "공기량 ±1.5%", "염화물 0.30 kg/m³ 이하", "공시체 채취 150㎥/1회", "양생 일수 보통 5일/조강 3일"]

## Node — WorkType / `WorkType:concrete`
- space: `concept`
- node_type: `WorkType`
- source_article: 검측 체크리스트 — 콘크리트 타설 공종
- properties:
  - `name_ko`: 콘크리트공사 (타설)
  - `applicable_standards`: ["KS F 4009", "KDS 14 20 50"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_concrete_site_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 콘크리트 타설 서명란 시공자
- properties:
  - `name_ko`: 콘크리트공사 (타설) 시공자 자체검측
  - `stage`: site_self_inspection

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_concrete_supervisor_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 콘크리트 타설 서명란 감리원
- properties:
  - `name_ko`: 콘크리트공사 (타설) 감리원 검측
  - `stage`: supervisor_inspection

## Node — DecisionOutcome / `DecisionOutcome:checklist_concrete_outcome_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 검측 체크리스트 — 콘크리트 타설 종합판정
- properties:
  - `name_ko`: 종합 검측 결과
  - `status`: pass
  - `status_options`: ["pass", "conditional_pass", "fail"]

## Node — SiteEngineer / `SiteEngineer:checklist_concrete_site_engineer_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 검측 체크리스트 — 콘크리트 타설 서명란
- properties:
  - `name_ko`: 시공자 (시공기술자/현장대리인)

## Node — Supervisor / `Supervisor:checklist_concrete_supervisor_subj_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: 검측 체크리스트 — 콘크리트 타설 서명란
- properties:
  - `name_ko`: 감리원 (건설사업관리기술자)

## Node — ChiefSupervisor / `ChiefSupervisor:checklist_concrete_chief_subj_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 검측 체크리스트 — 콘크리트 타설 서명란
- properties:
  - `name_ko`: 책임감리원

## Edges

## Edge — `performs`
- from: `SiteEngineer:checklist_concrete_site_engineer_01` (subject)
- to: `ConstructionInspectionDecision:checklist_concrete_site_01` (decision)
- source_article: 검측 체크리스트 — 콘크리트 타설 서명란 시공자

## Edge — `performs`
- from: `Supervisor:checklist_concrete_supervisor_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_concrete_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 콘크리트 타설 서명란 감리원

## Edge — `performs`
- from: `ChiefSupervisor:checklist_concrete_chief_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_concrete_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 콘크리트 타설 서명란 책임감리원

## Edge — `based_on`
- from: `ConstructionInspectionDecision:checklist_concrete_supervisor_01` (decision)
- to: `Checklist:checklist_concrete_01` (resource)
- source_article: 검측 체크리스트 — 콘크리트 타설 검측 항목

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:checklist_concrete_supervisor_01` (decision)
- to: `WorkType:concrete` (concept)
- source_article: 검측 체크리스트 — 콘크리트 타설 공종

## Edge — `yields`
- from: `ConstructionInspectionDecision:checklist_concrete_supervisor_01` (decision)
- to: `DecisionOutcome:checklist_concrete_outcome_01` (outcome)
- source_article: 검측 체크리스트 — 콘크리트 타설 종합판정

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:checklist_concrete_supervisor_01` (decision)
- to: `ConstructionInspectionDecision:checklist_concrete_site_01` (decision)
- source_article: 검측 체크리스트 — 콘크리트 타설 감리원 검측은 시공자 자체점검 후
