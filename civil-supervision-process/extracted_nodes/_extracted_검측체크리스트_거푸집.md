# Extracted graph — 검측체크리스트_거푸집.jsonl

_source jsonl: 검측체크리스트_거푸집.jsonl_

## Nodes

## Node — Checklist / `Checklist:checklist_formwork_01`
- space: `resource`
- node_type: `Checklist`
- source_article: 검측 체크리스트 — 거푸집 설치공사 표준 머리행
- properties:
  - `name_ko`: 검측 체크리스트 — 거푸집 설치공사
  - `form_code`: MOLIT/LH 거푸집 검측표
  - `issuer`: 국토교통부 / LH / 한국건설기술인협회
  - `sections`: ["일반정보", "검측 항목 2.1~2.14", "시험성과/측정", "종합판정", "서명란"]
  - `form_types`: ["유로폼", "갱폼", "알루미늄폼", "시스템동바리", "합판거푸집", "슬립폼"]
  - `key_items`: ["거푸집 자재 손상 5% 미만", "수직도 1/500 이내, ≤25mm", "평면 위치 ±10mm", "단면 치수 ±5mm", "동바리 수평연결재 2m 이내", "긴결재 간격 600mm 이내", "안전난간 90~120cm"]

## Node — WorkType / `WorkType:formwork`
- space: `concept`
- node_type: `WorkType`
- source_article: 검측 체크리스트 — 거푸집 설치공사 공종
- properties:
  - `name_ko`: 거푸집 공사
  - `applicable_standards`: ["KDS 14 20 10", "산업안전보건기준규칙"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_formwork_site_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 거푸집 설치공사 서명란 시공자
- properties:
  - `name_ko`: 거푸집 공사 시공자 자체검측
  - `stage`: site_self_inspection

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:checklist_formwork_supervisor_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측 체크리스트 — 거푸집 설치공사 서명란 감리원
- properties:
  - `name_ko`: 거푸집 공사 감리원 검측
  - `stage`: supervisor_inspection

## Node — DecisionOutcome / `DecisionOutcome:checklist_formwork_outcome_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 검측 체크리스트 — 거푸집 설치공사 종합판정
- properties:
  - `name_ko`: 종합 검측 결과
  - `status`: pass
  - `status_options`: ["pass", "conditional_pass", "fail"]

## Node — SiteEngineer / `SiteEngineer:checklist_formwork_site_engineer_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 검측 체크리스트 — 거푸집 설치공사 서명란
- properties:
  - `name_ko`: 시공자 (시공기술자/현장대리인)

## Node — Supervisor / `Supervisor:checklist_formwork_supervisor_subj_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: 검측 체크리스트 — 거푸집 설치공사 서명란
- properties:
  - `name_ko`: 감리원 (건설사업관리기술자)

## Node — ChiefSupervisor / `ChiefSupervisor:checklist_formwork_chief_subj_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 검측 체크리스트 — 거푸집 설치공사 서명란
- properties:
  - `name_ko`: 책임감리원

## Edges

## Edge — `performs`
- from: `SiteEngineer:checklist_formwork_site_engineer_01` (subject)
- to: `ConstructionInspectionDecision:checklist_formwork_site_01` (decision)
- source_article: 검측 체크리스트 — 거푸집 설치공사 서명란 시공자

## Edge — `performs`
- from: `Supervisor:checklist_formwork_supervisor_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_formwork_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 거푸집 설치공사 서명란 감리원

## Edge — `performs`
- from: `ChiefSupervisor:checklist_formwork_chief_subj_01` (subject)
- to: `ConstructionInspectionDecision:checklist_formwork_supervisor_01` (decision)
- source_article: 검측 체크리스트 — 거푸집 설치공사 서명란 책임감리원

## Edge — `based_on`
- from: `ConstructionInspectionDecision:checklist_formwork_supervisor_01` (decision)
- to: `Checklist:checklist_formwork_01` (resource)
- source_article: 검측 체크리스트 — 거푸집 설치공사 검측 항목

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:checklist_formwork_supervisor_01` (decision)
- to: `WorkType:formwork` (concept)
- source_article: 검측 체크리스트 — 거푸집 설치공사 공종

## Edge — `yields`
- from: `ConstructionInspectionDecision:checklist_formwork_supervisor_01` (decision)
- to: `DecisionOutcome:checklist_formwork_outcome_01` (outcome)
- source_article: 검측 체크리스트 — 거푸집 설치공사 종합판정

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:checklist_formwork_supervisor_01` (decision)
- to: `ConstructionInspectionDecision:checklist_formwork_site_01` (decision)
- source_article: 검측 체크리스트 — 거푸집 설치공사 감리원 검측은 시공자 자체점검 후
