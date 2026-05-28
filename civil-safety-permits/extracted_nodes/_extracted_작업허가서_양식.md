# Extracted graph — 작업허가서_양식.jsonl

_source jsonl: 작업허가서_양식.jsonl_

## Nodes

## Node — WorkPermit / `WorkPermit:form_workpermit_01`
- space: `resource`
- node_type: `WorkPermit`
- source_article: 안전작업허가서 표준양식
- properties:
  - `issuer`: KOSHA / 고용노동부
  - `source`: KOSHA Guide P-94-2021, KOSHA Guide Z-5-2022, KIOST 체크리스트
  - `legal_basis`: 산업안전보건법 제38조 (안전조치), 산업안전보건기준규칙
  - `language`: ko
  - `form_count`: 8
  - `name`: 안전작업허가서 (Safety Work Permit) 표준양식

## Node — WorkPermitDecision / `WorkPermitDecision:form_workpermit_01`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 안전작업허가서 — 종합 결정
- properties:
  - `decision_type`: work_permit
  - `permit_number_format`: WP-YYYY-NNNN
  - `valid_within_hours`: 24
  - `requires_pre_job_safety_meeting`: True
  - `requires_risk_assessment`: True
  - `covers_work_types`: ["hot-work", "confined-space", "working-at-height", "excavation", "electrical-isolation", "radiation", "heavy-equipment", "general"]
  - `name`: 위험공종 작업허가 결정

## Node — WorkType / `WorkType:general`
- space: `concept`
- node_type: `WorkType`
- source_article: 양식 1 — 일반작업허가서
- properties:
  - `slug`: general
  - `ko`: 일반작업
  - `scope`: 모든 작업의 공통 베이스
  - `name`: 일반작업 (General Work)

## Node — WorkType / `WorkType:hot-work`
- space: `concept`
- node_type: `WorkType`
- source_article: 양식 2 — 화기작업허가서
- properties:
  - `slug`: hot-work
  - `ko`: 화기작업
  - `scope`: 용접·용단·가열·연삭
  - `key_controls`: ["가연물 11m 격리", "LEL<10%", "O2 18-23.5%", "화기감시자", "잔불 30분-2시간 감시"]
  - `name`: 화기작업 (Hot Work)

## Node — WorkType / `WorkType:confined-space`
- space: `concept`
- node_type: `WorkType`
- source_article: 양식 3 — 밀폐공간 작업허가서
- properties:
  - `slug`: confined-space
  - `ko`: 밀폐공간 작업
  - `scope`: 산소결핍/유해가스 위험
  - `key_controls`: ["가스측정 30분 이내", "O2 18-23.5%", "LEL<10%", "CO<30ppm", "H2S<10ppm", "외부감시인 상시", "송기마스크"]
  - `name`: 밀폐공간 작업 (Confined Space)

## Node — WorkType / `WorkType:working-at-height`
- space: `concept`
- node_type: `WorkType`
- source_article: 양식 4 — 고소작업 허가서
- properties:
  - `slug`: working-at-height
  - `ko`: 고소작업
  - `scope`: 2m 이상 추락위험
  - `key_controls`: ["안전대 부착설비", "추락방호망", "작업발판 폭 40cm 이상", "풍속 10m/s 초과 시 중지"]
  - `name`: 고소작업 (Working at Height)

## Node — WorkType / `WorkType:excavation`
- space: `concept`
- node_type: `WorkType`
- source_article: 양식 5 — 굴착작업 허가서
- properties:
  - `slug`: excavation
  - `ko`: 굴착작업
  - `scope`: 2m 이상 지반 굴착
  - `key_controls`: ["지하매설물 조사", "흙막이 지보공(>1.5m)", "비탈면 1:1.0 이상", "산소·유해가스 측정"]
  - `name`: 굴착작업 (Excavation)

## Node — WorkType / `WorkType:electrical-isolation`
- space: `concept`
- node_type: `WorkType`
- source_article: 작업허가의 종류 — 정전작업
- properties:
  - `slug`: electrical-isolation
  - `ko`: 정전작업
  - `scope`: 활선/정전 전기작업
  - `key_controls`: ["LOTO 절차", "전기작업지휘자", "검전기 확인", "접지 단락"]
  - `name`: 정전작업 (Electrical Isolation)

## Node — WorkType / `WorkType:radiation`
- space: `concept`
- node_type: `WorkType`
- source_article: 작업허가의 종류 — 방사선작업
- properties:
  - `slug`: radiation
  - `ko`: 방사선 작업
  - `scope`: 비파괴검사 등
  - `key_controls`: ["방사선안전관리자", "구역설정", "피폭관리", "경보장치"]
  - `name`: 방사선 작업 (Radiation Work)

## Node — WorkType / `WorkType:heavy-equipment`
- space: `concept`
- node_type: `WorkType`
- source_article: 작업허가의 종류 — 중장비작업
- properties:
  - `slug`: heavy-equipment
  - `ko`: 중장비 작업
  - `scope`: 크레인·항타기 등
  - `key_controls`: ["조종사 자격", "신호수", "작업반경 출입통제", "아웃트리거"]
  - `name`: 중장비 작업 (Heavy Equipment)

## Node — SiteEngineer / `SiteEngineer:form_workpermit_permit_authority`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 작업허가서 [7. 서명란] 허가권자
- properties:
  - `role`: permit_authority
  - `ko`: 허가권자
  - `is_org`: False
  - `appointment_basis`: 사업주 위임
  - `name`: 허가권자 (현장소장)

## Node — SafetyManager / `SafetyManager:form_workpermit_safety_manager`
- space: `subject`
- node_type: `SafetyManager`
- source_article: 작업허가서 [7. 서명란] 안전관리자
- properties:
  - `role`: safety_manager
  - `ko`: 안전관리자
  - `qualification_examples`: ["산업안전기사", "산업안전지도사"]
  - `appointment_basis`: 산업안전보건법 선임
  - `name`: 안전관리자

## Node — ChiefSupervisor / `ChiefSupervisor:form_workpermit_chief_supervisor`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 작업허가서 [7. 서명란] 입회자
- properties:
  - `role`: witness
  - `ko`: 책임감리원
  - `applies_to`: 공공공사
  - `name`: 책임감리원 (입회자)

## Node — SiteEngineer / `SiteEngineer:form_workpermit_fire_watcher`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 양식 2 — 화기작업허가서 추가 서명
- properties:
  - `role`: fire_watcher
  - `ko`: 화기감시자
  - `qualification`: 화기감시자 교육 이수
  - `applies_to_work_type`: hot-work
  - `name`: 화기감시자

## Node — SiteEngineer / `SiteEngineer:form_workpermit_gas_tester`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 양식 2/3 — 화기·밀폐공간 가스측정자
- properties:
  - `role`: gas_tester
  - `ko`: 가스측정 담당자
  - `qualification`: 산업위생관리기사 또는 측정담당자
  - `applies_to_work_types`: ["hot-work", "confined-space"]
  - `name`: 가스측정 담당자

## Node — DecisionOutcome / `DecisionOutcome:form_workpermit_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 작업허가서 종합 결정 결과
- properties:
  - `status_enum`: ["approved", "conditional_approval", "rejected"]
  - `validity`: 단일 작업일 또는 24시간 이내
  - `ko`: 허가/조건부허가/불허가
  - `name`: 작업허가 결정 결과
