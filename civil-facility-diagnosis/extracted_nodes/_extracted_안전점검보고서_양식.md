# Extracted graph — 안전점검보고서_양식.jsonl

_source jsonl: 안전점검보고서_양식.jsonl_

## Nodes

## Node — SafetyInspectionReport / `SafetyInspectionReport:form_safety_inspection_01`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: 건설현장 안전점검 보고서 표준양식
- properties:
  - `issuer`: KOSHA / 국토안전관리원 / 고용노동부
  - `source`: 건설기술 진흥법 시행령 제100조, KOSHA 자료, 대한산업안전협회
  - `language`: ko
  - `inspection_types`: ["self_daily", "self_weekly", "regular_quarterly", "precision"]
  - `inspection_areas`: ["추락", "낙하비래", "붕괴", "감전", "화재폭발", "건설기계장비", "보호구", "작업환경"]
  - `name`: 건설현장 안전점검 보고서 표준양식

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:form_safety_inspection_01`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 안전점검 종류 1 — 자체 일일점검
- properties:
  - `inspection_type`: self_daily
  - `frequency`: daily
  - `performer_role`: safety_manager
  - `scope`: 시공자 자율 일일 점검
  - `name`: 자체 일일 안전점검 결정

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:form_safety_inspection_02`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 안전점검 종류 1 — 자체 주간점검
- properties:
  - `inspection_type`: self_weekly
  - `frequency`: weekly
  - `performer_role`: safety_manager
  - `scope`: 시공자 자율 주간 점검
  - `name`: 자체 주간 안전점검 결정

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:form_safety_inspection_03`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 안전점검 종류 2 — 정기 안전점검
- properties:
  - `inspection_type`: regular_quarterly
  - `frequency`: quarterly
  - `performer_role`: construction_management_engineer
  - `legal_basis`: 건설기술 진흥법 시행령 제100조
  - `scope`: 건설사업관리기술자 정기점검
  - `name`: 정기 안전점검 결정 (분기별)

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:form_safety_inspection_04`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 안전점검 종류 3 — 정밀 안전점검
- properties:
  - `inspection_type`: precision
  - `frequency`: as_needed
  - `performer_role`: specialized_safety_diagnosis_agency
  - `scope`: 안전진단전문기관/국토안전관리원
  - `legal_basis`: 시설물안전법
  - `name`: 정밀 안전점검 결정

## Node — SafetyManager / `SafetyManager:form_safety_inspection_safety_manager`
- space: `subject`
- node_type: `SafetyManager`
- source_article: 안전점검 자격 매핑 — 자체점검
- properties:
  - `role`: self_inspector
  - `ko`: 안전관리자
  - `qualification`: ["산업안전기사", "산업안전지도사"]
  - `appointment_basis`: 산업안전보건법 선임
  - `name`: 안전관리자 (자체점검 수행자)

## Node — Supervisor / `Supervisor:form_safety_inspection_supervisor`
- space: `subject`
- node_type: `Supervisor`
- source_article: 안전점검 자격 매핑 — 정기점검
- properties:
  - `role`: regular_inspector
  - `ko`: 건설사업관리기술자
  - `qualification`: 건설사업관리기술자(감리원)
  - `name`: 건설사업관리기술자 (정기점검 수행자)

## Node — Org / `Org:form_safety_inspection_precision_agency`
- space: `subject`
- node_type: `Org`
- source_article: 안전점검 자격 매핑 — 정밀점검
- properties:
  - `role`: precision_inspection_agency
  - `ko`: 안전진단전문기관
  - `qualification_examples`: ["토목·건축 기술사", "시설안전기술사", "안전진단전문가"]
  - `institution_type`: specialized_agency
  - `name`: 안전진단전문기관 / 국토안전관리원

## Node — ChiefSupervisor / `ChiefSupervisor:form_safety_inspection_chief_supervisor`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 안전점검 보고서 [5] 서명란 및 자격 매핑 — 작업중지
- properties:
  - `role`: chief_supervisor_confirm
  - `ko`: 책임감리원
  - `authority`: 작업중지 명령권 보유
  - `name`: 책임감리원 (확인 및 작업중지 명령)

## Node — Facility / `Facility:construction_site_general`
- space: `concept`
- node_type: `Facility`
- source_article: 안전점검 보고서 [2] 점검 항목 — 일반 안전
- properties:
  - `ko`: 건설현장
  - `scope`: 교량·터널·옹벽·도로·철도 등 일반 건설현장
  - `inspection_zones`: ["추락구역", "굴착구역", "고소작업구역", "밀폐공간", "화기작업구역", "건설기계 작업반경"]
  - `name`: 건설현장 시설물 (일반)

## Node — DecisionOutcome / `DecisionOutcome:form_safety_inspection_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 안전점검 보고서 [4. 종합 평가]
- properties:
  - `grading`: ["A_우수", "B_양호", "C_보통", "D_미흡", "E_불량"]
  - `status_enum`: ["pass", "conditional_pass", "fail"]
  - `work_stop_order_possible`: True
  - `name`: 안전점검 종합 평가 결과
