# Extracted graph — 검측체크리스트_철근.jsonl

_source jsonl: 검측체크리스트_철근.jsonl_

## Nodes

## Node — Checklist / `Checklist:checklist_rebar_01`
- space: `resource`
- node_type: `Checklist`
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 표준 머리행
- properties:
  - `name_ko`: 검측 체크리스트 — 철근공사 (배근 검측)
  - `form_code`: MOLIT/LH 철근배근 검측표
  - `issuer`: 국토교통부 / LH
  - `sections`: ["일반정보", "자재 검수", "배근 검측", "시험성과", "종합판정", "서명란"]
  - `rebar_grades`: ["SD400", "SD500", "SD600"]
  - `key_items`: ["철근 KS 마크 KS D 3504", "철근 간격 ±20mm", "피복두께 기초 80/기둥·보 40/슬래브 20mm", "정착길이 40db 등", "이음 50% 이상 동일위치 금지", "스페이서 1㎡당 4개 이상"]

## Node — WorkType / `WorkType:rebar`
- space: `concept`
- node_type: `WorkType`
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 공종
- properties:
  - `name_ko`: 철근콘크리트공사 (배근)
  - `applicable_standards`: ["KS D 3504", "KDS 14 20 50", "KDS 14 20 52", "KS D 0244"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_rebar_site_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 서명란 시공자
- properties:
  - `name_ko`: 철근콘크리트공사 (배근) 시공자 자체검측
  - `stage`: site_self_inspection

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_rebar_supervisor_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 서명란 감리원
- properties:
  - `name_ko`: 철근콘크리트공사 (배근) 감리원 검측
  - `stage`: supervisor_inspection

## Node — DecisionOutcome / `DecisionOutcome:checklist_rebar_outcome_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 종합판정
- properties:
  - `name_ko`: 종합 검측 결과
  - `status`: pass
  - `status_options`: ["pass", "conditional_pass", "fail"]

## Node — SiteEngineer / `SiteEngineer:checklist_rebar_site_engineer_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 서명란
- properties:
  - `name_ko`: 시공자 (시공기술자/현장대리인)

## Node — Supervisor / `Supervisor:checklist_rebar_supervisor_subj_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 서명란
- properties:
  - `name_ko`: 감리원 (건설사업관리기술자)

## Node — ChiefSupervisor / `ChiefSupervisor:checklist_rebar_chief_subj_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 서명란
- properties:
  - `name_ko`: 책임감리원

## Edges

## Edge — `performs`
- from: `SiteEngineer:checklist_rebar_site_engineer_01` (subject)
- to: `ConstructionInspectionDecision:checklist_rebar_site_01` (decision)
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 서명란 시공자

## Edge — `performs`
- from: `Supervisor:checklist_rebar_supervisor_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_rebar_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 서명란 감리원

## Edge — `performs`
- from: `ChiefSupervisor:checklist_rebar_chief_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_rebar_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 서명란 책임감리원

## Edge — `based_on`
- from: `ConstructionInspectionDecision:checklist_rebar_supervisor_01` (decision)
- to: `Checklist:checklist_rebar_01` (resource)
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 검측 항목

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:checklist_rebar_supervisor_01` (decision)
- to: `WorkType:rebar` (concept)
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 공종

## Edge — `yields`
- from: `ConstructionInspectionDecision:checklist_rebar_supervisor_01` (decision)
- to: `DecisionOutcome:checklist_rebar_outcome_01` (outcome)
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 종합판정

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:checklist_rebar_supervisor_01` (decision)
- to: `ConstructionInspectionDecision:checklist_rebar_site_01` (decision)
- source_article: 검측 체크리스트 — 철근공사 (배근 검측) 감리원 검측은 시공자 자체점검 후
