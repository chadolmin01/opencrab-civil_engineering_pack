# Extracted graph — 안전작업허가지침__part01.jsonl

_source jsonl: 안전작업허가지침__part01.jsonl_

## Nodes

## Node — Org / `Org:kosha`
- space: `subject`
- node_type: `Org`
- source_article: 표지
- properties:
  - `name_ko`: 한국산업안전보건공단
  - `abbr`: KOSHA
  - `role`: guide_publisher

## Node — Org / `Org:business-owner`
- space: `subject`
- node_type: `Org`
- source_article: 1
- properties:
  - `name_ko`: 사업주
  - `role`: process_safety_report_submitter

## Node — Org / `Org:operation-dept`
- space: `subject`
- node_type: `Org`
- source_article: 4.2(1)
- properties:
  - `name_ko`: 운전부서
  - `role`: permit_issuer_dept

## Node — Org / `Org:operation-dept-head`
- space: `subject`
- node_type: `Org`
- source_article: 4.3(1)
- properties:
  - `name_ko`: 운전부서 책임자(운전부서장)
  - `role`: permit_approver

## Node — Org / `Org:safety-dept-head`
- space: `subject`
- node_type: `Org`
- source_article: 4.3(2)
- properties:
  - `name_ko`: 안전관리부서 책임자(안전부서장)
  - `role`: safety_equipment_provider

## Node — Org / `Org:maintenance-dept-head`
- space: `subject`
- node_type: `Org`
- source_article: 4.3(3)
- properties:
  - `name_ko`: 작업부서 책임자(정비부서장)
  - `role`: work_executor_head

## Node — SafetyManager / `SafetyManager:permit-issuer`
- space: `subject`
- node_type: `SafetyManager`
- source_article: 4.2(1), 4.4
- properties:
  - `name_ko`: 허가서 발급자
  - `role`: issues_work_permit
  - `duties`: ["현장확인", "허가서 기재", "위험성평가 결과 확인"]

## Node — SafetyManager / `SafetyManager:permit-approver`
- space: `subject`
- node_type: `SafetyManager`
- source_article: 4.4(4)
- properties:
  - `name_ko`: 허가서 승인자
  - `role`: approves_work_permit
  - `duties`: ["현장방문 확인", "승인 서명"]

## Node — SafetyManager / `SafetyManager:permit-confirmer`
- space: `subject`
- node_type: `SafetyManager`
- source_article: 4.2(2)
- properties:
  - `name_ko`: 확인자
  - `role`: supplementary_work_confirmation
  - `duties`: ["보충작업별 전문지식 보유", "사전 확인·점검", "서명"]

## Node — SafetyManager / `SafetyManager:witness`
- space: `subject`
- node_type: `SafetyManager`
- source_article: 4.3(4), 4.6(3)
- properties:
  - `name_ko`: 입회자
  - `role`: on_site_safety_witness
  - `duties`: ["작업중 안전요구사항 유지 확인", "재개시 안전상태 확인"]

## Node — SafetyManager / `SafetyManager:hot-work-witness`
- space: `subject`
- node_type: `SafetyManager`
- source_article: 6.1(3)아
- properties:
  - `name_ko`: 화기감시자(화기작업 입회자)
  - `role`: fire_watch
  - `duties`: ["작업전·작업도중 입회", "가스농도 및 분진농도 측정", "안전조치 확인"]

## Node — SafetyManager / `SafetyManager:gas-tester`
- space: `subject`
- node_type: `SafetyManager`
- source_article: 6.1(3)나②
- properties:
  - `name_ko`: 가스측정자
  - `role`: gas_concentration_measurement
  - `requirement`: 측정기기 및 작업현장에 대해 충분한 지식 보유

## Node — SafetyManager / `SafetyManager:confined-space-watcher`
- space: `subject`
- node_type: `SafetyManager`
- source_article: 6.3(1)바③④
- properties:
  - `name_ko`: 작업 감시인(밀폐공간)
  - `role`: confined_space_watcher
  - `duties`: ["밀폐공간 출입시 입회", "안전대·구명선 이상 유무 확인", "통신장비 휴대", "외부 안전대기조 2인1조 배치"]

## Node — SiteEngineer / `SiteEngineer:work-supervisor`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 4.4(1), 5.1
- properties:
  - `name_ko`: 현장 감독자
  - `role`: site_supervisor
  - `duties`: ["현장확인", "허가서 발급자와 동행"]

## Node — SiteEngineer / `SiteEngineer:work-applicant`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 4.2(1), 4.4
- properties:
  - `name_ko`: 작업담당자(신청인)
  - `role`: work_applicant

## Node — SiteEngineer / `SiteEngineer:electrical-officer`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 6.3(2)다②③
- properties:
  - `name_ko`: 전기담당자
  - `role`: electrical_isolation_officer
  - `duties`: ["주차단 스위치·기기 차단기·시험전원 차단", "운전원과 상호 연락", "잠금장치·차단표지 부착"]

## Node — SiteEngineer / `SiteEngineer:field-operator`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 6.3(2)다①
- properties:
  - `name_ko`: 현장 운전원
  - `role`: field_switch_operator
  - `duties`: ["현장 스위치 차단"]

## Node — SiteEngineer / `SiteEngineer:radiation-worker`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 6.3(4)다①
- properties:
  - `name_ko`: 방사선 작업자
  - `role`: qualified_radiation_worker
  - `requirement`: 자격 보유

## Node — SiteEngineer / `SiteEngineer:heavy-equipment-operator`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 6.3(6)다①
- properties:
  - `name_ko`: 중장비 운전자
  - `role`: designated_heavy_equipment_operator
  - `requirement`: 자격 보유 지정 운전자

## Node — SiteEngineer / `SiteEngineer:signal-guide`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 6.3(6)다②
- properties:
  - `name_ko`: 신호수(유도자)
  - `role`: signal_guide
  - `duties`: ["통신장비 휴대", "시야간섭 지역 배치"]

## Node — SiteEngineer / `SiteEngineer:operation-officer`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 6.3(1)다④
- properties:
  - `name_ko`: 운전책임자
  - `role`: operation_officer
  - `duties`: ["특별안전보건교육 실시", "MSDS 및 위험사항 교육"]

## Node — Qualification / `Qualification:gas-tester`
- space: `concept`
- node_type: `Qualification`
- source_article: 6.1(3)나②
- properties:
  - `name_ko`: 가스농도 측정 자격
  - `requirement`: 측정기기 및 작업현장에 대한 충분한 지식

## Node — Qualification / `Qualification:radiation-worker`
- space: `concept`
- node_type: `Qualification`
- source_article: 6.3(4)다①
- properties:
  - `name_ko`: 방사선 사용 자격
  - `scope`: 방사선 노출로부터 보호 안전수칙 숙지

## Node — Qualification / `Qualification:heavy-equipment-operator`
- space: `concept`
- node_type: `Qualification`
- source_article: 6.3(6)다①
- properties:
  - `name_ko`: 중장비 운전 자격
  - `scope`: 이동식 크레인 등 중장비 운전

## Node — Qualification / `Qualification:supplementary-work-expert`
- space: `concept`
- node_type: `Qualification`
- source_article: 4.2(2)
- properties:
  - `name_ko`: 보충작업별 전문지식
  - `scope`: 각 보충작업 사전 확인·점검 자격

## Node — Qualification / `Qualification:confined-space-program`
- space: `concept`
- node_type: `Qualification`
- source_article: 6.3(1)라②
- properties:
  - `name_ko`: 밀폐공간 보건작업 프로그램 이수
  - `scope`: 응급조치 등 안전보건 교육 및 훈련

## Node — WorkType / `WorkType:hot-work`
- space: `concept`
- node_type: `WorkType`
- source_article: 3(1)가, 4.1(1), 6.1
- properties:
  - `name_ko`: 화기작업
  - `definition`: 용접·용단·연마·드릴 등 화염 또는 스파크를 발생시키는 작업, 또는 가연성물질의 점화원이 될 수 있는 모든 기기를 사용하는 작업
  - `permit_form`: 화기작업 허가서

## Node — WorkType / `WorkType:general`
- space: `concept`
- node_type: `WorkType`
- source_article: 3(1)나, 4.1(2), 6.2
- properties:
  - `name_ko`: 일반위험작업
  - `definition`: 화염·스파크 발생 장비 외 유해·위험물 취급, 위험설비 해체 등 유해·위험 내재 작업
  - `permit_form`: 일반위험작업 허가서

## Node — WorkType / `WorkType:confined-space`
- space: `concept`
- node_type: `WorkType`
- source_article: 3(1)마, 4.1(3)가, 6.3(1)
- properties:
  - `name_ko`: 밀폐공간 출입작업
  - `definition`: 질식·중독·화재·폭발 등 위험 장소 출입작업
  - `permit_form`: 밀폐공간출입작업 허가서
  - `supplementary`: True

## Node — WorkType / `WorkType:electrical-isolation`
- space: `concept`
- node_type: `WorkType`
- source_article: 4.1(3)나, 6.3(2)
- properties:
  - `name_ko`: 정전작업
  - `definition`: 전기설비 점화원 또는 감전 위험 작업 시 전원차단
  - `permit_form`: 정전작업 허가서
  - `supplementary`: True

## Node — WorkType / `WorkType:excavation`
- space: `concept`
- node_type: `WorkType`
- source_article: 4.1(3)다, 6.3(3)
- properties:
  - `name_ko`: 굴착작업
  - `definition`: 깊이 30cm 이상 지반 굴착 및 지하매설 작업
  - `depth_threshold_cm`: 30
  - `permit_form`: 굴착작업 허가서
  - `supplementary`: True

## Node — WorkType / `WorkType:radiation`
- space: `concept`
- node_type: `WorkType`
- source_article: 4.1(3)라, 6.3(4)
- properties:
  - `name_ko`: 방사선사용작업
  - `definition`: 방사선을 사용한 기기 점검 또는 비파괴검사 작업
  - `permit_form`: 방사선사용작업 허가서
  - `supplementary`: True

## Node — WorkType / `WorkType:working-at-height`
- space: `concept`
- node_type: `WorkType`
- source_article: 4.1(3)마, 6.3(5)
- properties:
  - `name_ko`: 고소작업
  - `definition`: 2m 이상 높이에서 정비·점검·도장·보온 또는 위험물 상부에서 행하는 작업
  - `height_threshold_m`: 2
  - `permit_form`: 고소작업 허가서
  - `supplementary`: True

## Node — WorkType / `WorkType:heavy-equipment`
- space: `concept`
- node_type: `WorkType`
- source_article: 3(1)아, 4.1(3)바, 6.3(6)
- properties:
  - `name_ko`: 중장비사용작업
  - `definition`: 이동식 크레인 등 중장비를 사용해 중량물 매달기·수리·점검 작업
  - `permit_form`: 중장비사용작업 허가서
  - `supplementary`: True

## Node — WorkType / `WorkType:supplementary`
- space: `concept`
- node_type: `WorkType`
- source_article: 3(1)다, 4.1(3)
- properties:
  - `name_ko`: 보충적인 작업
  - `definition`: 화기작업 또는 일반위험작업 수행 중 보충적으로 병행되는 작업
  - `permit_form`: 보충작업허가

## Node — Facility / `Facility:hazardous-area`
- space: `concept`
- node_type: `Facility`
- source_article: 3(1)라
- properties:
  - `name_ko`: 위험지역
  - `definition`: 산업안전보건기준에 관한 규칙 제230조 폭발위험 장소 및 인근지역, 화재·폭발 우려 장소

## Node — Facility / `Facility:confined-space-vessel`
- space: `concept`
- node_type: `Facility`
- source_article: 3(1)마, 6.3(1)나
- properties:
  - `name_ko`: 밀폐공간(밀폐용기)
  - `definition`: 산업안전보건기준에 관한 규칙 제618조 제1호 장소, 가열로·건조기 내부 등

## Node — Facility / `Facility:general-area`
- space: `concept`
- node_type: `Facility`
- source_article: 3(1)바
- properties:
  - `name_ko`: 일반지역
  - `definition`: 일반행정 또는 정비부서 등 위험지역 이외의 지역

## Node — Facility / `Facility:process-equipment`
- space: `concept`
- node_type: `Facility`
- source_article: 6.2(3)나
- properties:
  - `name_ko`: 공정설비·부속설비
  - `definition`: 압력·온도·유해위험물질이 존재하는 공정설비 또는 부속설비

## Node — Facility / `Facility:electrical-equipment`
- space: `concept`
- node_type: `Facility`
- source_article: 6.3(2)가
- properties:
  - `name_ko`: 전기설비·전기구동기계
  - `definition`: 정전작업 대상 전기설비 및 전기구동기계

## Node — Facility / `Facility:underground-utility`
- space: `concept`
- node_type: `Facility`
- source_article: 6.3(3)나①
- properties:
  - `name_ko`: 지하매설물
  - `definition`: 배관·전력선·계장선·전화선·접지선 등 지하시설물

## Node — WorkPermit / `WorkPermit:integrated-hot-work-form1`
- space: `resource`
- node_type: `WorkPermit`
- source_article: 6.1(4), 별지 양식1
- properties:
  - `name_ko`: 화기작업 허가서 통합양식(별지 양식1)
  - `fields`: ["허가번호", "허가일자", "신청인", "허가기간", "장치번호", "장치명", "작업개요", "첨부서류", "안전조치 요구사항", "보충작업허가", "가스농도 측정", "작업완료", "안전조치 확인", "발급자/승인자 서명", "허가연장"]

## Node — WorkPermit / `WorkPermit:integrated-general-form2`
- space: `resource`
- node_type: `WorkPermit`
- source_article: 6.2(4), 별지 양식2
- properties:
  - `name_ko`: 일반위험작업 허가서 통합양식(별지 양식2)
  - `fields`: ["허가번호", "허가일자", "신청인", "허가기간", "장치번호", "장치명", "작업개요", "첨부서류", "안전조치 요구사항", "보충작업허가", "가스농도 측정", "작업완료", "안전조치 확인", "발급자/승인자 서명", "허가연장"]

## Node — WorkPermit / `WorkPermit:confined-space-entry`
- space: `resource`
- node_type: `WorkPermit`
- source_article: 6.3(1)가, 6.3(1)사
- properties:
  - `name_ko`: 밀폐공간출입작업 허가서
  - `issuance_basis`: 밀폐공간 출입을 위한 안전성 확보
  - `form_usage`: 양식1·양식2 통합양식 또는 별도 분리

## Node — WorkPermit / `WorkPermit:electrical-isolation`
- space: `resource`
- node_type: `WorkPermit`
- source_article: 6.3(2)가, 6.3(2)나, 6.3(2)라
- properties:
  - `name_ko`: 정전작업 허가서
  - `fields_required`: ["차단 스위치 식별", "차단 기기 번호와 이름"]
  - `form_usage`: 양식1·양식2 통합양식 또는 별도 분리

## Node — WorkPermit / `WorkPermit:excavation`
- space: `resource`
- node_type: `WorkPermit`
- source_article: 6.3(3)가, 6.3(3)나, 6.3(3)라
- properties:
  - `name_ko`: 굴착작업 허가서
  - `depth_threshold_cm`: 30
  - `attachment`: 굴착작업 도면(필요시)
  - `form_usage`: 양식1·양식2 통합양식 또는 별도 분리

## Node — WorkPermit / `WorkPermit:radiation-use`
- space: `resource`
- node_type: `WorkPermit`
- source_article: 6.3(4)가, 6.3(4)나, 6.3(4)라
- properties:
  - `name_ko`: 방사선사용작업 허가서
  - `attachment`: 방사선 방사위치 도면
  - `form_usage`: 양식1·양식2 통합양식 또는 별도 분리

## Node — WorkPermit / `WorkPermit:working-at-height`
- space: `resource`
- node_type: `WorkPermit`
- source_article: 6.3(5)가, 6.3(5)나, 6.3(5)라
- properties:
  - `name_ko`: 고소작업 허가서
  - `scope`: ["2m 이상 정비·점검", "2m 이상 도장·보온", "2m 이하 고열물·강산 등 위험물 상부 작업"]
  - `form_usage`: 양식1·양식2 통합양식 또는 별도 분리

## Node — WorkPermit / `WorkPermit:heavy-equipment-use`
- space: `resource`
- node_type: `WorkPermit`
- source_article: 6.3(6)가, 6.3(6)나, 6.3(6)라
- properties:
  - `name_ko`: 중장비사용작업 허가서
  - `scope`: ["기계류·장치류 설치·교체·정비", "반응기·흡수탑·탱크 충전물 교체·점검", "보온·단열·도장 케이지 작업", "제품 적재·이송"]
  - `form_usage`: 양식1·양식2 통합양식 또는 별도 분리

## Node — Checklist / `Checklist:pre-permit-inspection`
- space: `resource`
- node_type: `Checklist`
- source_article: 5.1
- properties:
  - `name_ko`: 작업허가 전 점검사항
  - `items_count`: 14
  - `items`: ["밀폐공간 여부", "정전 필요 여부", "굴착 병행 여부", "방사선사용 여부", "위험지역 회피 가능성", "인화성·독성 발생 가능성", "액체 열팽창 가능성", "내부포켓·드레인 잔류 가능성", "산소·유해가스 측정 및 강제환기", "초기 소화설비 배치", "출입 제한구역", "현장 입회자 필요 여부", "고소작업 예방대책", "중장비 작업 예방대책"]

## Node — Checklist / `Checklist:gas-concentration-measurement`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.3(1)마②③④⑤⑥
- properties:
  - `name_ko`: 가스농도 측정 체크리스트
  - `limits`: {"HC": "0%", "O2_min": "18%", "O2_max": "23.5%", "CO_max_ppm": 30, "CO2_max": "1.5%", "H2S_max_ppm": 10}
  - `frequency`: ["작업 전", "점심식사 후", "휴식 후", "농도 변화 의심 시"]
  - `points`: ["상", "중", "하"]

## Node — Checklist / `Checklist:hot-work-pre-safety`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.1(3)
- properties:
  - `name_ko`: 화기작업 사전 안전조치 체크리스트
  - `items`: ["작업구역 설정", "가스농도 측정 및 잔류물질 확인", "차량 출입제한", "밸브차단 표시판 부착", "위험물질 방출 및 처리", "환기", "비산불티차단막 설치", "화기작업 입회", "소화설비 비치"]

## Node — Checklist / `Checklist:general-risk-pre-safety`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.2(3)
- properties:
  - `name_ko`: 일반위험작업 사전 안전조치 체크리스트
  - `items`: ["작업구역 설정", "작업의 제한(압력방출·냉각·내용물 배출)", "밸브차단 표지 부착", "위험물질 방출 및 처리"]

## Node — Checklist / `Checklist:confined-space-entry`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.3(1)마
- properties:
  - `name_ko`: 밀폐공간출입 사전 안전보건조치
  - `items`: ["용기 세척과 치환", "측정대상가스(산소·CO2·CO·H2S·가연성·유해가스)", "산소농도 측정", "측정 빈도", "측정점(상·중·하)", "출입 허가제한", "통신장비 비치"]

## Node — Checklist / `Checklist:confined-space-rules`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.3(1)바
- properties:
  - `name_ko`: 밀폐공간 내 작업 수칙
  - `items`: ["송기마스크·사다리·섬유로우프 비치", "구명선 착용", "감시인 입회 및 외부 2인1조 대기", "안전대·구명선 확인 통신장비", "지속적 강제환기", "저전압방폭등 사용", "방폭형 공구 사용", "구출시 송기마스크 사용"]

## Node — Checklist / `Checklist:electrical-isolation-safety`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.3(2)다
- properties:
  - `name_ko`: 정전작업 안전조치
  - `items`: ["현장 스위치 차단(운전원)", "주차단기·기기차단기·시험전원 차단(전기담당자)", "상호 연락 차단 확인", "잠금장치·차단표지 부착", "열쇠 보관 및 표지 기재", "역순 통전 복구"]

## Node — Checklist / `Checklist:excavation-safety`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.3(3)다
- properties:
  - `name_ko`: 굴착작업 안전조치
  - `items`: ["지하매설물 인근 수동굴착", "굴착공사 안전작업지침 준용"]

## Node — Checklist / `Checklist:radiation-safety`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.3(4)다
- properties:
  - `name_ko`: 방사선 사용 안전조치
  - `items`: ["자격 작업자 수행", "출입제한 표지 게시", "방사선 위험표지 및 점멸등 설치", "작업 후 방사선 물질 즉시 수거"]

## Node — Checklist / `Checklist:working-at-height-safety`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.3(5)다
- properties:
  - `name_ko`: 고소작업 안전조치
  - `items`: ["비계·발판 견고 설치(작업발판설치 및 사용안전지침 준용)", "안전대 착용 및 부착설비 사용"]

## Node — Checklist / `Checklist:heavy-equipment-safety`
- space: `resource`
- node_type: `Checklist`
- source_article: 6.3(6)다
- properties:
  - `name_ko`: 중장비 작업 안전조치
  - `items`: ["자격 운전자 및 감독자 배치", "신호수(유도자) 배치", "연약지반·협소공간 작업 금지", "허용하중·붐 안전각도 유지", "차량운반구 적상·적하시 운전자 탑승 금지", "보조달기구 규정품 사용", "일상점검 실시", "관련부서와 사전 협의"]

## Node — Specification / `Specification:work-plan`
- space: `resource`
- node_type: `Specification`
- source_article: 5.1, 별지 양식1
- properties:
  - `name_ko`: 작업계획서
  - `purpose`: 허가서 첨부 신청서류

## Node — Specification / `Specification:pressure-vessel-open-procedure`
- space: `resource`
- node_type: `Specification`
- source_article: 5.2(3)가
- properties:
  - `name_ko`: 압력용기 및 배관개방 절차서

## Node — Specification / `Specification:content-disposal-procedure`
- space: `resource`
- node_type: `Specification`
- source_article: 5.2(3)나
- properties:
  - `name_ko`: 내용물 처리절차서

## Node — Specification / `Specification:risk-assessment`
- space: `resource`
- node_type: `Specification`
- source_article: 5.2(5)
- properties:
  - `name_ko`: 작업 전 위험성평가
  - `trigger`: 작업절차서 미비 또는 노후·상이 시

## Node — Drawing / `Drawing:electrical-single-line`
- space: `resource`
- node_type: `Drawing`
- source_article: 6.3(2)나①
- properties:
  - `name_ko`: 전기단선도
  - `purpose`: 차단 스위치 확인

## Node — Drawing / `Drawing:excavation-drawing`
- space: `resource`
- node_type: `Drawing`
- source_article: 6.3(3)나①③
- properties:
  - `name_ko`: 굴착작업 도면
  - `purpose`: 지하매설물 위치 검토

## Node — Drawing / `Drawing:radiation-emission-drawing`
- space: `resource`
- node_type: `Drawing`
- source_article: 6.3(4)나
- properties:
  - `name_ko`: 방사선 방사점 도면
  - `purpose`: 방사선 방사위치 표시 첨부

## Node — SafetyInspectionReport / `SafetyInspectionReport:gas-measurement-record`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: 별지 양식1, 별지 양식2, 4.5(2)
- properties:
  - `name_ko`: 가스농도 측정 기록
  - `fields`: ["물질명", "결과", "측정시간", "측정자/확인자"]
  - `retention_years`: 1

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec4_1`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 4.2(1)
- properties:
  - `name_ko`: 안전작업허가 발급 결정(일반)
  - `actor`: 운전부서 담당자
  - `trigger`: 신청자 서면 또는 전자문서 신청
  - `method`: 현장확인 후 발급

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec4_2`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 4.2(2)
- properties:
  - `name_ko`: 보충작업 확인·점검 결정
  - `actor`: 보충작업별 전문지식 보유 확인자
  - `scope`: 6.3 사항 사전 확인·점검 및 서명

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec4_3`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 4.2(3)
- properties:
  - `name_ko`: 허가서 승인(허가) 결정
  - `actor`: 운전부서 책임자 또는 상위 조직
  - `method`: 서면 확인 및 승인 서명
  - `delegation`: 소규모·저위험·시간외 사업장 내부규정에 따라 발급자에게 위임 가능

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec4_4`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 4.2(4)
- properties:
  - `name_ko`: 작업현장 입회 결정
  - `actor`: 운전부서 입회자
  - `trigger`: 작업의 위험정도·규모·복잡성에 따른 안전감독 필요

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec4_5`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 4.4(5), 4.6(1)
- properties:
  - `name_ko`: 허가서 연장 결정
  - `actor`: 허가서 발급자 또는 위임자
  - `trigger`: 근무 교대시간 이후까지 연장
  - `method`: 작업현장 재확인 후 서명

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec4_6`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 4.6(2)
- properties:
  - `name_ko`: 허가서 재발급 결정
  - `actor`: 허가서 발급자
  - `trigger`: 허가 익일 지속, 작업내용 변경, 안전요구 변경

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec5_1`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 5.1
- properties:
  - `name_ko`: 작업허가 전 점검 결정
  - `actor`: 허가서 발급자 + 현장 감독자/작업담당자
  - `method`: 신청서류·기술자료·도면·현장확인 종합
  - `review_by`: ["운전부서 책임자", "작업부서 책임자"]

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec5_2`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 5.2(5)라
- properties:
  - `name_ko`: 위험성평가 결과 반영 결정
  - `actor`: 허가서 발급자
  - `method`: 절차서 위험성평가 실시 및 반영 여부 확인

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec6_1`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 6.1(1)
- properties:
  - `name_ko`: 화기작업 허가 결정
  - `actor`: 허가서 발급자/승인자
  - `trigger`: 위험지역에서 화기작업 수행
  - `form`: 화기작업 허가서(별지 양식1)

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec6_2`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 6.2(1)
- properties:
  - `name_ko`: 일반위험작업 허가 결정
  - `actor`: 허가서 발급자/승인자
  - `trigger`: 화기작업 외 위험한 모든 작업
  - `form`: 일반위험작업 허가서(별지 양식2)

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec6_3`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 6.3(1)가
- properties:
  - `name_ko`: 밀폐공간출입작업 허가 결정
  - `actor`: 허가서 발급자 + 확인자
  - `trigger`: 밀폐공간 출입
  - `preconditions`: ["산소 18~23.5%", "CO2 <1.5%", "CO <30ppm", "H2S <10ppm"]
  - `form`: 밀폐공간출입작업 허가서

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec6_4`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 6.3(2)가
- properties:
  - `name_ko`: 정전작업 허가 결정
  - `actor`: 허가서 발급자 + 전기담당자
  - `trigger`: 전기설비 점화원 또는 감전 위험
  - `form`: 정전작업 허가서

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec6_5`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 6.3(3)가
- properties:
  - `name_ko`: 굴착작업 허가 결정
  - `actor`: 허가서 발급자 + 지하시설물 관장 부서
  - `trigger`: 30cm 이상 지반 굴착
  - `form`: 굴착작업 허가서

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec6_6`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 6.3(4)가
- properties:
  - `name_ko`: 방사선사용작업 허가 결정
  - `actor`: 허가서 발급자 + 자격 작업자
  - `trigger`: 방사선 사용 점검·비파괴검사
  - `form`: 방사선사용작업 허가서

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec6_7`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 6.3(5)가
- properties:
  - `name_ko`: 고소작업 허가 결정
  - `actor`: 허가서 발급자
  - `trigger`: 2m 이상 고소작업 또는 2m 이하 위험물 상부 작업
  - `form`: 고소작업 허가서

## Node — WorkPermitDecision / `WorkPermitDecision:safety_permit_guide_sec6_8`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: 6.3(6)가
- properties:
  - `name_ko`: 중장비사용작업 허가 결정
  - `actor`: 허가서 발급자 + 감독자
  - `trigger`: 중장비 사용 보수·청소·정비·촉매교환
  - `form`: 중장비사용작업 허가서

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:safety_permit_guide_sec6_9`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 6.1(3)나, 6.3(1)마
- properties:
  - `name_ko`: 가스농도 측정 안전점검 결정
  - `actor`: 가스측정자
  - `method`: 산소·인화성·독성가스 농도 측정 및 잔류물질 확인

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:safety_permit_guide_sec4_7`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: 4.6(3)
- properties:
  - `name_ko`: 작업 재개 안전상태 확인 결정
  - `actor`: 입회자 또는 현장 책임자
  - `trigger`: 식사 등 작업 일시중단 후 재개

## Node — DecisionOutcome / `DecisionOutcome:permit-approved`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 4.2(3), 4.4(4)
- properties:
  - `status`: approved
  - `name_ko`: 허가 승인

## Node — DecisionOutcome / `DecisionOutcome:permit-rejected`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 4.2(3)
- properties:
  - `status`: rejected
  - `name_ko`: 허가 거부

## Node — DecisionOutcome / `DecisionOutcome:permit-extended`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 4.4(5), 4.6(1)
- properties:
  - `status`: approved
  - `name_ko`: 허가 연장 승인

## Node — DecisionOutcome / `DecisionOutcome:permit-reissued`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 4.6(2)
- properties:
  - `status`: approved
  - `name_ko`: 재발급

## Node — DecisionOutcome / `DecisionOutcome:gas-pass`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 6.3(1)마⑥
- properties:
  - `status`: pass
  - `name_ko`: 가스농도 합격(출입허가)
  - `criteria`: O2 18~23.5%, CO2<1.5%, CO<30ppm, H2S<10ppm

## Node — DecisionOutcome / `DecisionOutcome:gas-fail`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 6.3(1)마⑥
- properties:
  - `status`: fail
  - `name_ko`: 가스농도 불합격(출입제한)

## Node — DecisionOutcome / `DecisionOutcome:conditional-pass`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 4.1(3), 6.1(2), 6.2(2)
- properties:
  - `status`: conditional_pass
  - `name_ko`: 조건부 허가(보충작업 병행)

## Edges

## Edge — `performs`
- from: `Org:kosha` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_1` (decision)
- source_article: 표지

## Edge — `performs`
- from: `Org:business-owner` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_1` (decision)
- source_article: 1

## Edge — `performs`
- from: `Org:operation-dept-head` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_3` (decision)
- source_article: 4.2(3), 4.3(1)

## Edge — `performs`
- from: `Org:safety-dept-head` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec5_1` (decision)
- source_article: 4.3(2)

## Edge — `performs`
- from: `Org:maintenance-dept-head` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec5_1` (decision)
- source_article: 4.3(3)

## Edge — `performs`
- from: `SafetyManager:permit-issuer` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_1` (decision)
- source_article: 4.2(1)

## Edge — `performs`
- from: `SafetyManager:permit-issuer` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_5` (decision)
- source_article: 4.4(5)

## Edge — `performs`
- from: `SafetyManager:permit-issuer` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_6` (decision)
- source_article: 4.6(2)

## Edge — `performs`
- from: `SafetyManager:permit-issuer` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec5_1` (decision)
- source_article: 5.1

## Edge — `performs`
- from: `SafetyManager:permit-issuer` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec5_2` (decision)
- source_article: 5.2(5)라

## Edge — `performs`
- from: `SafetyManager:permit-approver` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_3` (decision)
- source_article: 4.4(4)

## Edge — `performs`
- from: `SafetyManager:permit-confirmer` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_2` (decision)
- source_article: 4.2(2)

## Edge — `performs`
- from: `SafetyManager:witness` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_4` (decision)
- source_article: 4.2(4), 4.3(4)

## Edge — `performs`
- from: `SafetyManager:witness` (subject)
- to: `SafetyInspectionDecision:safety_permit_guide_sec4_7` (decision)
- source_article: 4.6(3)

## Edge — `performs`
- from: `SafetyManager:hot-work-witness` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- source_article: 6.1(3)아

## Edge — `performs`
- from: `SafetyManager:gas-tester` (subject)
- to: `SafetyInspectionDecision:safety_permit_guide_sec6_9` (decision)
- source_article: 6.1(3)나②

## Edge — `performs`
- from: `SafetyManager:confined-space-watcher` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- source_article: 6.3(1)바③

## Edge — `performs`
- from: `SiteEngineer:work-supervisor` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec5_1` (decision)
- source_article: 4.4(1), 5.1

## Edge — `performs`
- from: `SiteEngineer:work-applicant` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec4_1` (decision)
- source_article: 4.2(1)

## Edge — `performs`
- from: `SiteEngineer:electrical-officer` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec6_4` (decision)
- source_article: 6.3(2)다②③

## Edge — `performs`
- from: `SiteEngineer:field-operator` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec6_4` (decision)
- source_article: 6.3(2)다①

## Edge — `performs`
- from: `SiteEngineer:radiation-worker` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec6_6` (decision)
- source_article: 6.3(4)다①

## Edge — `performs`
- from: `SiteEngineer:heavy-equipment-operator` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec6_8` (decision)
- source_article: 6.3(6)다①

## Edge — `performs`
- from: `SiteEngineer:signal-guide` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec6_8` (decision)
- source_article: 6.3(6)다②

## Edge — `performs`
- from: `SiteEngineer:operation-officer` (subject)
- to: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- source_article: 6.3(1)다④

## Edge — `qualified_as`
- from: `SafetyManager:gas-tester` (subject)
- to: `Qualification:gas-tester` (concept)
- source_article: 6.1(3)나②

## Edge — `qualified_as`
- from: `SiteEngineer:radiation-worker` (subject)
- to: `Qualification:radiation-worker` (concept)
- source_article: 6.3(4)다①

## Edge — `qualified_as`
- from: `SiteEngineer:heavy-equipment-operator` (subject)
- to: `Qualification:heavy-equipment-operator` (concept)
- source_article: 6.3(6)다①

## Edge — `qualified_as`
- from: `SafetyManager:permit-confirmer` (subject)
- to: `Qualification:supplementary-work-expert` (concept)
- source_article: 4.2(2)

## Edge — `qualified_as`
- from: `SafetyManager:confined-space-watcher` (subject)
- to: `Qualification:confined-space-program` (concept)
- source_article: 6.3(1)라②

## Edge — `grants_authority_for`
- from: `Qualification:gas-tester` (concept)
- to: `SafetyInspectionDecision:safety_permit_guide_sec6_9` (decision)
- source_article: 6.1(3)나②

## Edge — `grants_authority_for`
- from: `Qualification:radiation-worker` (concept)
- to: `WorkPermitDecision:safety_permit_guide_sec6_6` (decision)
- source_article: 6.3(4)다①

## Edge — `grants_authority_for`
- from: `Qualification:heavy-equipment-operator` (concept)
- to: `WorkPermitDecision:safety_permit_guide_sec6_8` (decision)
- source_article: 6.3(6)다①

## Edge — `grants_authority_for`
- from: `Qualification:supplementary-work-expert` (concept)
- to: `WorkPermitDecision:safety_permit_guide_sec4_2` (decision)
- source_article: 4.2(2)

## Edge — `grants_authority_for`
- from: `Qualification:confined-space-program` (concept)
- to: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- source_article: 6.3(1)라

## Edge — `targets_work_type`
- from: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- to: `WorkType:hot-work` (concept)
- source_article: 6.1(1)

## Edge — `targets_work_type`
- from: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- to: `WorkType:general` (concept)
- source_article: 6.2(1)

## Edge — `targets_work_type`
- from: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- to: `WorkType:confined-space` (concept)
- source_article: 6.3(1)가

## Edge — `targets_work_type`
- from: `WorkPermitDecision:safety_permit_guide_sec6_4` (decision)
- to: `WorkType:electrical-isolation` (concept)
- source_article: 6.3(2)가

## Edge — `targets_work_type`
- from: `WorkPermitDecision:safety_permit_guide_sec6_5` (decision)
- to: `WorkType:excavation` (concept)
- source_article: 6.3(3)가

## Edge — `targets_work_type`
- from: `WorkPermitDecision:safety_permit_guide_sec6_6` (decision)
- to: `WorkType:radiation` (concept)
- source_article: 6.3(4)가

## Edge — `targets_work_type`
- from: `WorkPermitDecision:safety_permit_guide_sec6_7` (decision)
- to: `WorkType:working-at-height` (concept)
- source_article: 6.3(5)가

## Edge — `targets_work_type`
- from: `WorkPermitDecision:safety_permit_guide_sec6_8` (decision)
- to: `WorkType:heavy-equipment` (concept)
- source_article: 6.3(6)가

## Edge — `targets_facility`
- from: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- to: `Facility:hazardous-area` (concept)
- source_article: 6.1(1)

## Edge — `targets_facility`
- from: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- to: `Facility:confined-space-vessel` (concept)
- source_article: 6.3(1)나

## Edge — `targets_facility`
- from: `WorkPermitDecision:safety_permit_guide_sec6_4` (decision)
- to: `Facility:electrical-equipment` (concept)
- source_article: 6.3(2)가

## Edge — `targets_facility`
- from: `WorkPermitDecision:safety_permit_guide_sec6_5` (decision)
- to: `Facility:underground-utility` (concept)
- source_article: 6.3(3)나①

## Edge — `targets_facility`
- from: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- to: `Facility:process-equipment` (concept)
- source_article: 6.2(3)나

## Edge — `targets_work_type`
- from: `SafetyInspectionDecision:safety_permit_guide_sec6_9` (decision)
- to: `WorkType:hot-work` (concept)
- source_article: 6.1(3)나

## Edge — `targets_work_type`
- from: `SafetyInspectionDecision:safety_permit_guide_sec6_9` (decision)
- to: `WorkType:confined-space` (concept)
- source_article: 6.3(1)마

## Edge — `subclass_of`
- from: `WorkType:confined-space` (concept)
- to: `WorkType:supplementary` (concept)
- source_article: 4.1(3)가

## Edge — `subclass_of`
- from: `WorkType:electrical-isolation` (concept)
- to: `WorkType:supplementary` (concept)
- source_article: 4.1(3)나

## Edge — `subclass_of`
- from: `WorkType:excavation` (concept)
- to: `WorkType:supplementary` (concept)
- source_article: 4.1(3)다

## Edge — `subclass_of`
- from: `WorkType:radiation` (concept)
- to: `WorkType:supplementary` (concept)
- source_article: 4.1(3)라

## Edge — `subclass_of`
- from: `WorkType:working-at-height` (concept)
- to: `WorkType:supplementary` (concept)
- source_article: 4.1(3)마

## Edge — `subclass_of`
- from: `WorkType:heavy-equipment` (concept)
- to: `WorkType:supplementary` (concept)
- source_article: 4.1(3)바

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- to: `WorkPermit:integrated-hot-work-form1` (resource)
- source_article: 6.1(4)

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- to: `WorkPermit:integrated-general-form2` (resource)
- source_article: 6.2(4)

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- to: `WorkPermit:confined-space-entry` (resource)
- source_article: 6.3(1)가

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_4` (decision)
- to: `WorkPermit:electrical-isolation` (resource)
- source_article: 6.3(2)가

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_5` (decision)
- to: `WorkPermit:excavation` (resource)
- source_article: 6.3(3)가

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_6` (decision)
- to: `WorkPermit:radiation-use` (resource)
- source_article: 6.3(4)가

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_7` (decision)
- to: `WorkPermit:working-at-height` (resource)
- source_article: 6.3(5)가

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_8` (decision)
- to: `WorkPermit:heavy-equipment-use` (resource)
- source_article: 6.3(6)가

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec5_1` (decision)
- to: `Checklist:pre-permit-inspection` (resource)
- source_article: 5.1

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- to: `Checklist:hot-work-pre-safety` (resource)
- source_article: 6.1(3)

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- to: `Checklist:general-risk-pre-safety` (resource)
- source_article: 6.2(3)

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- to: `Checklist:confined-space-entry` (resource)
- source_article: 6.3(1)마

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- to: `Checklist:confined-space-rules` (resource)
- source_article: 6.3(1)바

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_4` (decision)
- to: `Checklist:electrical-isolation-safety` (resource)
- source_article: 6.3(2)다

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_5` (decision)
- to: `Checklist:excavation-safety` (resource)
- source_article: 6.3(3)다

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_6` (decision)
- to: `Checklist:radiation-safety` (resource)
- source_article: 6.3(4)다

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_7` (decision)
- to: `Checklist:working-at-height-safety` (resource)
- source_article: 6.3(5)다

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_8` (decision)
- to: `Checklist:heavy-equipment-safety` (resource)
- source_article: 6.3(6)다

## Edge — `based_on`
- from: `SafetyInspectionDecision:safety_permit_guide_sec6_9` (decision)
- to: `Checklist:gas-concentration-measurement` (resource)
- source_article: 6.1(3)나, 6.3(1)마

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec5_2` (decision)
- to: `Specification:risk-assessment` (resource)
- source_article: 5.2(5)

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec5_1` (decision)
- to: `Specification:work-plan` (resource)
- source_article: 5.1, 별지 양식1

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- to: `Specification:pressure-vessel-open-procedure` (resource)
- source_article: 5.2(3)가, 6.3(1)다⑥

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- to: `Specification:content-disposal-procedure` (resource)
- source_article: 5.2(3)나, 6.3(1)다②

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_4` (decision)
- to: `Drawing:electrical-single-line` (resource)
- source_article: 6.3(2)나①

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_5` (decision)
- to: `Drawing:excavation-drawing` (resource)
- source_article: 6.3(3)나③

## Edge — `based_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_6` (decision)
- to: `Drawing:radiation-emission-drawing` (resource)
- source_article: 6.3(4)나

## Edge — `based_on`
- from: `SafetyInspectionDecision:safety_permit_guide_sec6_9` (decision)
- to: `SafetyInspectionReport:gas-measurement-record` (resource)
- source_article: 별지 양식1, 별지 양식2

## Edge — `precedes`
- from: `WorkPermitDecision:safety_permit_guide_sec5_1` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec4_1` (decision)
- source_article: 5.1

## Edge — `precedes`
- from: `WorkPermitDecision:safety_permit_guide_sec5_2` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec4_1` (decision)
- source_article: 5.2(5)라

## Edge — `precedes`
- from: `WorkPermitDecision:safety_permit_guide_sec4_1` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec4_3` (decision)
- source_article: 4.2(1)→(3)

## Edge — `precedes`
- from: `WorkPermitDecision:safety_permit_guide_sec4_3` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec4_4` (decision)
- source_article: 4.2(3)→(4)

## Edge — `precedes`
- from: `WorkPermitDecision:safety_permit_guide_sec4_2` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec4_3` (decision)
- source_article: 4.2(2)→(3)

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- source_article: 6.1(2)가

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- source_article: 6.2(2)가

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_4` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- source_article: 6.1(2)나

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_4` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- source_article: 6.2(2)나

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_5` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- source_article: 6.1(2)다

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_5` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- source_article: 6.2(2)다

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_6` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- source_article: 6.1(2)라

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_6` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- source_article: 6.2(2)라

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_7` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- source_article: 6.1(2)마

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_7` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- source_article: 6.2(2)마

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_8` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- source_article: 6.1(2)바

## Edge — `depends_on`
- from: `WorkPermitDecision:safety_permit_guide_sec6_8` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_2` (decision)
- source_article: 6.2(2)바

## Edge — `precedes`
- from: `SafetyInspectionDecision:safety_permit_guide_sec6_9` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_3` (decision)
- source_article: 6.3(1)마⑥

## Edge — `precedes`
- from: `SafetyInspectionDecision:safety_permit_guide_sec6_9` (decision)
- to: `WorkPermitDecision:safety_permit_guide_sec6_1` (decision)
- source_article: 6.1(3)나

## Edge — `yields`
- from: `WorkPermitDecision:safety_permit_guide_sec4_3` (decision)
- to: `DecisionOutcome:permit-approved` (outcome)
- source_article: 4.2(3)

## Edge — `yields`
- from: `WorkPermitDecision:safety_permit_guide_sec4_3` (decision)
- to: `DecisionOutcome:permit-rejected` (outcome)
- source_article: 4.2(3)

## Edge — `yields`
- from: `WorkPermitDecision:safety_permit_guide_sec4_5` (decision)
- to: `DecisionOutcome:permit-extended` (outcome)
- source_article: 4.4(5), 4.6(1)

## Edge — `yields`
- from: `WorkPermitDecision:safety_permit_guide_sec4_6` (decision)
- to: `DecisionOutcome:permit-reissued` (outcome)
- source_article: 4.6(2)

## Edge — `yields`
- from: `SafetyInspectionDecision:safety_permit_guide_sec6_9` (decision)
- to: `DecisionOutcome:gas-pass` (outcome)
- source_article: 6.3(1)마⑥
