# Extracted graph — 시설물안전법_시행규칙.jsonl

_source jsonl: 시설물안전법_시행규칙.jsonl_

## Nodes

## Node — Qualification / `Qualification:safety-inspection-responsible`
- space: `concept`
- node_type: `Qualification`
- source_article: 제10조 ①②
- properties:
  - `name_ko`: 책임기술자
  - `scope`: 안전점검등 및 정밀안전진단·성능평가 책임기술자
  - `training_hours_initial_precision`: 70
  - `training_hours_refresh_precision`: 14
  - `training_hours_initial_regular`: 35
  - `training_hours_refresh_regular`: 7
  - `refresh_cycle_years`: 5

## Node — Qualification / `Qualification:precision-diagnosis-responsible`
- space: `concept`
- node_type: `Qualification`
- source_article: 제10조 ①②
- properties:
  - `name_ko`: 정밀안전진단 책임기술자
  - `training_hours_initial`: 70
  - `training_hours_refresh`: 14
  - `refresh_cycle_years`: 5

## Node — Qualification / `Qualification:participating-engineer`
- space: `concept`
- node_type: `Qualification`
- source_article: 제10조의2
- properties:
  - `name_ko`: 참여기술자
  - `registration_system`: 시설물통합정보관리체계

## Node — Qualification / `Qualification:safety-diagnosis-firm-engineer`
- space: `concept`
- node_type: `Qualification`
- source_article: 제25조 ①, 제26조
- properties:
  - `name_ko`: 안전진단전문기관 기술인력
  - `fields`: ["교량 및 터널", "수리시설", "항만", "건축", "종합"]
  - `basis`: 별표 6

## Node — Qualification / `Qualification:safety-inspection-firm-engineer`
- space: `concept`
- node_type: `Qualification`
- source_article: 제27조의3 ①, 제27조의5
- properties:
  - `name_ko`: 안전점검전문기관 기술인력
  - `fields`: ["토목", "건축"]
  - `basis`: 별표 8

## Node — Facility / `Facility:type-1-facility`
- space: `concept`
- node_type: `Facility`
- source_article: 제6조 ①
- properties:
  - `name_ko`: 제1종시설물

## Node — Facility / `Facility:type-2-facility`
- space: `concept`
- node_type: `Facility`
- source_article: 제6조 ①
- properties:
  - `name_ko`: 제2종시설물

## Node — Facility / `Facility:type-3-facility`
- space: `concept`
- node_type: `Facility`
- source_article: 제4조, 제5조
- properties:
  - `name_ko`: 제3종시설물

## Node — Facility / `Facility:small-scale-vulnerable`
- space: `concept`
- node_type: `Facility`
- source_article: 제16조 ①
- properties:
  - `name_ko`: 소규모 취약시설

## Node — Facility / `Facility:bridge-tunnel`
- space: `concept`
- node_type: `Facility`
- source_article: 제25조 ①
- properties:
  - `name_ko`: 교량 및 터널

## Node — Facility / `Facility:hydraulic-structure`
- space: `concept`
- node_type: `Facility`
- source_article: 제25조 ①
- properties:
  - `name_ko`: 수리시설

## Node — Facility / `Facility:harbor`
- space: `concept`
- node_type: `Facility`
- source_article: 제25조 ①
- properties:
  - `name_ko`: 항만

## Node — Facility / `Facility:building`
- space: `concept`
- node_type: `Facility`
- source_article: 제25조 ①
- properties:
  - `name_ko`: 건축

## Node — StructuralComponent / `StructuralComponent:bridge-bearing`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: 제7조 1호
- properties:
  - `name_ko`: 교량받침

## Node — StructuralComponent / `StructuralComponent:tunnel-lining`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: 제7조 2호
- properties:
  - `name_ko`: 터널의 복공 부위

## Node — StructuralComponent / `StructuralComponent:floodgate-door`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: 제7조 3호
- properties:
  - `name_ko`: 하천시설 수문의 문짝

## Node — StructuralComponent / `StructuralComponent:dam-body`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: 제7조 4호
- properties:
  - `name_ko`: 댐의 본체, 시공이음부 및 여수로

## Node — StructuralComponent / `StructuralComponent:prefab-joint`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: 제7조 5호
- properties:
  - `name_ko`: 조립식 건축물의 연결부위

## Node — StructuralComponent / `StructuralComponent:waterpipe-joint`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: 제7조 6호
- properties:
  - `name_ko`: 상수도 관로이음부

## Node — StructuralComponent / `StructuralComponent:harbor-gate-mooring`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: 제7조 7호
- properties:
  - `name_ko`: 항만시설 갑문 문짝 작동시설, 계류시설, 방파제, 파제제, 호안 구조체

## Node — SafetyInspectionReport / `SafetyInspectionReport:type3-designation-attachment`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: 제5조 ① 1호
- properties:
  - `name_ko`: 제3종시설물 지정신청용 점검결과 보고서
  - `context`: 제3종시설물 지정 신청 첨부서류

## Node — SafetyInspectionReport / `SafetyInspectionReport:type3-deregistration-attachment`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: 제5조 ② 1호
- properties:
  - `name_ko`: 제3종시설물 지정해제용 안전점검 결과보고서
  - `legal_basis`: 법 제17조제1항

## Node — SafetyInspectionReport / `SafetyInspectionReport:inspection-diagnosis-result`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: 제13조
- properties:
  - `name_ko`: 안전점검 및 정밀안전진단 결과보고서
  - `retention_years`: 10
  - `supporting_data_retention_years`: 5

## Node — SafetyInspectionReport / `SafetyInspectionReport:emergency-inspection-log`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: 제11조 ①②
- properties:
  - `name_ko`: 긴급안전점검 대장
  - `form`: 별지 제7호서식
  - `storage`: 전자적 처리

## Node — SafetyInspectionReport / `SafetyInspectionReport:small-vulnerable-result`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: 제16조 ③
- properties:
  - `name_ko`: 소규모 취약시설 안전점검 결과
  - `notify_within_days`: 30

## Node — SafetyInspectionReport / `SafetyInspectionReport:agency-performance-record`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: 제29조 ① 1호
- properties:
  - `name_ko`: 안전점검등 대행실적 결과보고서
  - `legal_basis`: 법 제13조제3항·제17조제1항
  - `submission_deadline_days`: 30

## Node — SafetyInspectionReport / `SafetyInspectionReport:state-inspection-log`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: 제34조 ①②
- properties:
  - `name_ko`: 실태점검 대장
  - `form`: 별지 제25호서식

## Node — Org / `Org:molit-minister`
- space: `subject`
- node_type: `Org`
- source_article: 제9조 ②
- properties:
  - `name_ko`: 국토교통부장관
  - `type`: central-government

## Node — Org / `Org:kalis`
- space: `subject`
- node_type: `Org`
- source_article: 제16조 ①②③
- properties:
  - `name_ko`: 국토안전관리원
  - `legal_basis`: 국토안전관리원법

## Node — Org / `Org:management-entity`
- space: `subject`
- node_type: `Org`
- source_article: 제3조 ①
- properties:
  - `name_ko`: 관리주체

## Node — Org / `Org:public-official-inspector`
- space: `subject`
- node_type: `Org`
- source_article: 제11조 ①
- properties:
  - `name_ko`: 긴급안전점검 공무원
  - `legal_basis`: 법 제13조제2항

## Node — Org / `Org:safety-diagnosis-firm`
- space: `subject`
- node_type: `Org`
- source_article: 제22조, 제24조
- properties:
  - `name_ko`: 안전진단전문기관
  - `legal_basis`: 법 제28조

## Node — Org / `Org:safety-inspection-firm`
- space: `subject`
- node_type: `Org`
- source_article: 제22조, 제27조의2
- properties:
  - `name_ko`: 안전점검전문기관
  - `legal_basis`: 법 제28조의2

## Node — ChiefSafetyInspector / `ChiefSafetyInspector:facility_safety_rule_art10_01`
- space: `subject`
- node_type: `ChiefSafetyInspector`
- source_article: 제10조 ①
- properties:
  - `name_ko`: 안전점검 책임기술자
  - `role`: 안전점검등 책임기술자
  - `education_required`: True

## Node — ChiefPrecisionDiagnoser / `ChiefPrecisionDiagnoser:facility_safety_rule_art10_01`
- space: `subject`
- node_type: `ChiefPrecisionDiagnoser`
- source_article: 제10조 ①
- properties:
  - `name_ko`: 정밀안전진단 책임기술자
  - `role`: 정밀안전진단·성능평가 책임기술자
  - `education_required`: True

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:facility_safety_rule_art11_01`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 제11조 ①
- properties:
  - `name_ko`: 긴급안전점검 실시
  - `legal_basis`: 법 제13조제2항
  - `record_form`: 별지 제7호서식

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:facility_safety_rule_art12_01`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 제12조 ①
- properties:
  - `name_ko`: 안전등급 지정 (제1·2종)
  - `trigger`: 정밀안전점검 또는 정밀안전진단 완료
  - `legal_basis`: 법 제16조제1항

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:facility_safety_rule_art12_02`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 제12조 ①
- properties:
  - `name_ko`: 안전등급 지정 (제3종)
  - `trigger`: 안전점검 또는 정밀안전진단 완료
  - `legal_basis`: 법 제16조제1항

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:facility_safety_rule_art12_03`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 제12조 ②
- properties:
  - `name_ko`: 안전등급 변경
  - `actor`: 국토교통부장관
  - `notify_deadline_days`: 15
  - `legal_basis`: 법 제16조제2항

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:facility_safety_rule_art16_01`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 제16조 ②③
- properties:
  - `name_ko`: 소규모 취약시설 안전점검 실시
  - `actor`: 국토안전관리원
  - `legal_basis`: 법 제19조제1항

## Node — PrecisionDiagnosisDecision / `PrecisionDiagnosisDecision:facility_safety_rule_art12_01`
- space: `decision`
- node_type: `PrecisionDiagnosisDecision`
- source_article: 제12조 ①
- properties:
  - `name_ko`: 정밀안전진단 실시
  - `scope`: 제1·2·3종시설물 안전등급 지정 사전 절차
  - `legal_basis`: 법 제16조제1항

## Node — DecisionOutcome / `DecisionOutcome:facility_safety_rule_art12_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 제12조 ①
- properties:
  - `name_ko`: 안전등급 (제1·2종)
  - `status`: approved
  - `grades_possible`: ["A", "B", "C", "D", "E"]

## Node — DecisionOutcome / `DecisionOutcome:facility_safety_rule_art12_02`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 제12조 ①
- properties:
  - `name_ko`: 안전등급 (제3종)
  - `status`: approved
  - `grades_possible`: ["A", "B", "C", "D", "E"]

## Node — DecisionOutcome / `DecisionOutcome:facility_safety_rule_art16_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 제16조 ③
- properties:
  - `name_ko`: 소규모 취약시설 안전점검 결과 및 안전조치 사항
  - `status`: approved

## Edges

## Edge — `subclass_of`
- from: `Facility:type-3-facility` (concept)
- to: `Facility:type-2-facility` (concept)
- source_article: 제5조 ①

## Edge — `subclass_of`
- from: `Qualification:precision-diagnosis-responsible` (concept)
- to: `Qualification:safety-inspection-responsible` (concept)
- source_article: 제10조

## Edge — `qualified_as`
- from: `ChiefSafetyInspector:facility_safety_rule_art10_01` (subject)
- to: `Qualification:safety-inspection-responsible` (concept)
- source_article: 제10조 ①

## Edge — `qualified_as`
- from: `ChiefPrecisionDiagnoser:facility_safety_rule_art10_01` (subject)
- to: `Qualification:precision-diagnosis-responsible` (concept)
- source_article: 제10조 ①

## Edge — `grants_authority_for`
- from: `Qualification:safety-inspection-responsible` (concept)
- to: `SafetyInspectionDecision:facility_safety_rule_art12_01` (decision)
- source_article: 제10조, 제12조

## Edge — `grants_authority_for`
- from: `Qualification:safety-inspection-responsible` (concept)
- to: `SafetyInspectionDecision:facility_safety_rule_art12_02` (decision)
- source_article: 제10조, 제12조

## Edge — `grants_authority_for`
- from: `Qualification:precision-diagnosis-responsible` (concept)
- to: `PrecisionDiagnosisDecision:facility_safety_rule_art12_01` (decision)
- source_article: 제10조, 제12조

## Edge — `performs`
- from: `Org:public-official-inspector` (subject)
- to: `SafetyInspectionDecision:facility_safety_rule_art11_01` (decision)
- source_article: 제11조 ①

## Edge — `performs`
- from: `Org:molit-minister` (subject)
- to: `SafetyInspectionDecision:facility_safety_rule_art12_03` (decision)
- source_article: 제12조 ②

## Edge — `performs`
- from: `Org:kalis` (subject)
- to: `SafetyInspectionDecision:facility_safety_rule_art16_01` (decision)
- source_article: 제16조 ②③

## Edge — `performs`
- from: `ChiefSafetyInspector:facility_safety_rule_art10_01` (subject)
- to: `SafetyInspectionDecision:facility_safety_rule_art12_01` (decision)
- source_article: 제10조, 제12조

## Edge — `performs`
- from: `ChiefSafetyInspector:facility_safety_rule_art10_01` (subject)
- to: `SafetyInspectionDecision:facility_safety_rule_art12_02` (decision)
- source_article: 제10조, 제12조

## Edge — `performs`
- from: `ChiefPrecisionDiagnoser:facility_safety_rule_art10_01` (subject)
- to: `PrecisionDiagnosisDecision:facility_safety_rule_art12_01` (decision)
- source_article: 제10조, 제12조

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_01` (decision)
- to: `Facility:type-1-facility` (concept)
- source_article: 제12조 ①

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_01` (decision)
- to: `Facility:type-2-facility` (concept)
- source_article: 제12조 ①

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_02` (decision)
- to: `Facility:type-3-facility` (concept)
- source_article: 제12조 ①

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:facility_safety_rule_art16_01` (decision)
- to: `Facility:small-scale-vulnerable` (concept)
- source_article: 제16조 ①②

## Edge — `targets_facility`
- from: `PrecisionDiagnosisDecision:facility_safety_rule_art12_01` (decision)
- to: `Facility:type-1-facility` (concept)
- source_article: 제12조 ①

## Edge — `targets_facility`
- from: `PrecisionDiagnosisDecision:facility_safety_rule_art12_01` (decision)
- to: `Facility:type-2-facility` (concept)
- source_article: 제12조 ①

## Edge — `targets_facility`
- from: `PrecisionDiagnosisDecision:facility_safety_rule_art12_01` (decision)
- to: `Facility:type-3-facility` (concept)
- source_article: 제12조 ①

## Edge — `based_on`
- from: `SafetyInspectionDecision:facility_safety_rule_art11_01` (decision)
- to: `SafetyInspectionReport:emergency-inspection-log` (resource)
- source_article: 제11조 ①

## Edge — `based_on`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_01` (decision)
- to: `SafetyInspectionReport:inspection-diagnosis-result` (resource)
- source_article: 제12조 ①, 제13조

## Edge — `based_on`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_02` (decision)
- to: `SafetyInspectionReport:inspection-diagnosis-result` (resource)
- source_article: 제12조 ①, 제13조

## Edge — `based_on`
- from: `PrecisionDiagnosisDecision:facility_safety_rule_art12_01` (decision)
- to: `SafetyInspectionReport:inspection-diagnosis-result` (resource)
- source_article: 제12조 ①, 제13조

## Edge — `based_on`
- from: `SafetyInspectionDecision:facility_safety_rule_art16_01` (decision)
- to: `SafetyInspectionReport:small-vulnerable-result` (resource)
- source_article: 제16조 ③

## Edge — `based_on`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_03` (decision)
- to: `SafetyInspectionReport:inspection-diagnosis-result` (resource)
- source_article: 제12조 ②

## Edge — `depends_on`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_01` (decision)
- to: `PrecisionDiagnosisDecision:facility_safety_rule_art12_01` (decision)
- source_article: 제12조 ①

## Edge — `depends_on`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_02` (decision)
- to: `PrecisionDiagnosisDecision:facility_safety_rule_art12_01` (decision)
- source_article: 제12조 ①

## Edge — `depends_on`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_03` (decision)
- to: `SafetyInspectionDecision:facility_safety_rule_art12_01` (decision)
- source_article: 제12조 ②

## Edge — `precedes`
- from: `PrecisionDiagnosisDecision:facility_safety_rule_art12_01` (decision)
- to: `SafetyInspectionDecision:facility_safety_rule_art12_01` (decision)
- source_article: 제12조 ①

## Edge — `yields`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_01` (decision)
- to: `DecisionOutcome:facility_safety_rule_art12_01` (outcome)
- source_article: 제12조 ①

## Edge — `yields`
- from: `SafetyInspectionDecision:facility_safety_rule_art12_02` (decision)
- to: `DecisionOutcome:facility_safety_rule_art12_02` (outcome)
- source_article: 제12조 ①

## Edge — `yields`
- from: `SafetyInspectionDecision:facility_safety_rule_art16_01` (decision)
- to: `DecisionOutcome:facility_safety_rule_art16_01` (outcome)
- source_article: 제16조 ③
