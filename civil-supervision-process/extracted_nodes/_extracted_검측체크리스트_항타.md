# Extracted graph — 검측체크리스트_항타.jsonl

_source jsonl: 검측체크리스트_항타.jsonl_

## Nodes

## Node — Checklist / `Checklist:checklist_pile_driving_01`
- space: `resource`
- node_type: `Checklist`
- source_article: 검측 체크리스트 — 항타공사 표준 머리행
- properties:
  - `name_ko`: 검측 체크리스트 — 항타공사 (PHC/강관파일/시험항타)
  - `form_code`: LH/한국도로공사 항타 검측표
  - `issuer`: LH / 한국도로공사 / KOSHA
  - `sections`: ["일반정보", "시험항타", "본항타", "두부정리", "시험성과", "종합판정", "서명란"]
  - `pile_types`: ["PHC파일", "강관파일", "SCP", "SIP", "DRA", "RCD"]
  - `key_items`: ["수직도 1/100 (해상 1/50)", "위치 편심 100mm 이내", "최종 관입량 10~20mm/10타", "PDA 안전율 2.0~3.0", "Set-up 24시간 후 재시험", "컷오프 ±20mm", "소음 65dB 이하 (주거지)"]

## Node — WorkType / `WorkType:pile-driving`
- space: `concept`
- node_type: `WorkType`
- source_article: 검측 체크리스트 — 항타공사 공종
- properties:
  - `name_ko`: 항타공사 (기초공사)
  - `applicable_standards`: ["KS F 4306", "KS F 4602", "소음진동관리법", "KOSHA Guide"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_pile_driving_site_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 항타공사 서명란 시공자
- properties:
  - `name_ko`: 항타공사 (기초공사) 시공자 자체검측
  - `stage`: site_self_inspection

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_pile_driving_supervisor_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 항타공사 서명란 감리원
- properties:
  - `name_ko`: 항타공사 (기초공사) 감리원 검측
  - `stage`: supervisor_inspection

## Node — DecisionOutcome / `DecisionOutcome:checklist_pile_driving_outcome_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 검측 체크리스트 — 항타공사 종합판정
- properties:
  - `name_ko`: 종합 검측 결과
  - `status`: pass
  - `status_options`: ["pass", "conditional_pass", "fail"]

## Node — SiteEngineer / `SiteEngineer:checklist_pile_driving_site_engineer_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 검측 체크리스트 — 항타공사 서명란
- properties:
  - `name_ko`: 시공자 (시공기술자/현장대리인)

## Node — Supervisor / `Supervisor:checklist_pile_driving_supervisor_subj_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: 검측 체크리스트 — 항타공사 서명란
- properties:
  - `name_ko`: 감리원 (건설사업관리기술자)

## Node — ChiefSupervisor / `ChiefSupervisor:checklist_pile_driving_chief_subj_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 검측 체크리스트 — 항타공사 서명란
- properties:
  - `name_ko`: 책임감리원

## Edges

## Edge — `performs`
- from: `SiteEngineer:checklist_pile_driving_site_engineer_01` (subject)
- to: `ConstructionInspectionDecision:checklist_pile_driving_site_01` (decision)
- source_article: 검측 체크리스트 — 항타공사 서명란 시공자

## Edge — `performs`
- from: `Supervisor:checklist_pile_driving_supervisor_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_pile_driving_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 항타공사 서명란 감리원

## Edge — `performs`
- from: `ChiefSupervisor:checklist_pile_driving_chief_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_pile_driving_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 항타공사 서명란 책임감리원

## Edge — `based_on`
- from: `ConstructionInspectionDecision:checklist_pile_driving_supervisor_01` (decision)
- to: `Checklist:checklist_pile_driving_01` (resource)
- source_article: 검측 체크리스트 — 항타공사 검측 항목

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:checklist_pile_driving_supervisor_01` (decision)
- to: `WorkType:pile-driving` (concept)
- source_article: 검측 체크리스트 — 항타공사 공종

## Edge — `yields`
- from: `ConstructionInspectionDecision:checklist_pile_driving_supervisor_01` (decision)
- to: `DecisionOutcome:checklist_pile_driving_outcome_01` (outcome)
- source_article: 검측 체크리스트 — 항타공사 종합판정

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:checklist_pile_driving_supervisor_01` (decision)
- to: `ConstructionInspectionDecision:checklist_pile_driving_site_01` (decision)
- source_article: 검측 체크리스트 — 항타공사 감리원 검측은 시공자 자체점검 후
