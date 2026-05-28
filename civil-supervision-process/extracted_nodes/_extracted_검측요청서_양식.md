# Extracted graph — 검측요청서_양식.jsonl

_source jsonl: 검측요청서_양식.jsonl_

## Nodes

## Node — Checklist / `Checklist:inspection_request_form_molit6`
- space: `resource`
- node_type: `Checklist`
- source_article: 검측요청서 (MOLIT 별지 제6호) 표제부/검측대상
- properties:
  - `name_ko`: 검측요청·결과 통보서
  - `form_code`: MOLIT 별지 제6호
  - `issuer`: 국토교통부
  - `purpose`: 시공자 자체점검 후 책임감리원에게 검측 요청 시 제출
  - `fields_header`: ["문서번호", "수신", "발신", "작성일자", "공사명", "발주처"]
  - `fields_target`: ["위치 및 공종", "세부공종", "검측부위", "공사량", "검측요구일시", "검측 항목"]

## Node — WorkType / `WorkType:construction-general`
- space: `concept`
- node_type: `WorkType`
- source_article: 검측요청서 (MOLIT 별지 제6호) 검측 대상
- properties:
  - `name_ko`: 공사 일반 (검측 대상 공종)
  - `scope`: 검측요청서가 가리키는 모든 공종 (콘크리트/철근/거푸집/항타/토공/배수공 등)

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:request_form_site_self_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측요청서 (MOLIT 별지 제6호) 절차 1~3
- properties:
  - `name_ko`: 시공자 담당기술자 자체점검
  - `stage`: site_self_inspection
  - `preceded_by`: 현장시공 완료
  - `deliverable`: 검측요청서 제출

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:request_form_supervisor_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: 검측요청서 (MOLIT 별지 제6호) 절차 4~5
- properties:
  - `name_ko`: 책임감리원 검측 수행
  - `stage`: supervisor_inspection
  - `method_options`: ["육안", "측정", "시험", "입회"]

## Node — DecisionOutcome / `DecisionOutcome:request_form_outcome_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 검측요청서 (MOLIT 별지 제6호) 절차 5
- properties:
  - `name_ko`: 검측 결과 통보 (적합/부적합)
  - `status`: pass
  - `status_options`: ["pass", "fail"]
  - `fail_action`: 부적합 시정지시서 통보 → 재시공/보완

## Node — SiteEngineer / `SiteEngineer:request_form_site_engineer_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 검측요청서 (MOLIT 별지 제6호) 서명란
- properties:
  - `name_ko`: 시공자 현장대리인
  - `role`: 발신/자체점검 책임자

## Node — Supervisor / `Supervisor:request_form_supervisor_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: 검측요청서 (MOLIT 별지 제6호) 서명란
- properties:
  - `name_ko`: 감리원 (검측자)
  - `role`: 건설사업관리기술자

## Node — ChiefSupervisor / `ChiefSupervisor:request_form_chief_supervisor_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 검측요청서 (MOLIT 별지 제6호) 서명란
- properties:
  - `name_ko`: 책임감리원
  - `qualification`: 건설사업관리기술자(특급) + 책임감리원 교육

## Edges

## Edge — `performs`
- from: `SiteEngineer:request_form_site_engineer_01` (subject)
- to: `ConstructionInspectionDecision:request_form_site_self_01` (decision)
- source_article: 검측요청서 (MOLIT 별지 제6호) 절차 2

## Edge — `performs`
- from: `Supervisor:request_form_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:request_form_supervisor_01` (decision)
- source_article: 검측요청서 (MOLIT 별지 제6호) 절차 4

## Edge — `performs`
- from: `ChiefSupervisor:request_form_chief_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:request_form_supervisor_01` (decision)
- source_article: 검측요청서 (MOLIT 별지 제6호) 서명란

## Edge — `based_on`
- from: `ConstructionInspectionDecision:request_form_site_self_01` (decision)
- to: `Checklist:inspection_request_form_molit6` (resource)
- source_article: 검측요청서 (MOLIT 별지 제6호) 첨부

## Edge — `based_on`
- from: `ConstructionInspectionDecision:request_form_supervisor_01` (decision)
- to: `Checklist:inspection_request_form_molit6` (resource)
- source_article: 검측요청서 (MOLIT 별지 제6호) 절차 4

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:request_form_supervisor_01` (decision)
- to: `WorkType:construction-general` (concept)
- source_article: 검측요청서 (MOLIT 별지 제6호) 검측 대상

## Edge — `yields`
- from: `ConstructionInspectionDecision:request_form_supervisor_01` (decision)
- to: `DecisionOutcome:request_form_outcome_01` (outcome)
- source_article: 검측요청서 (MOLIT 별지 제6호) 절차 5

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:request_form_supervisor_01` (decision)
- to: `ConstructionInspectionDecision:request_form_site_self_01` (decision)
- source_article: 검측요청서 (MOLIT 별지 제6호) 절차 2 → 4
