# Extracted graph — KCS__part01.jsonl

_source jsonl: KCS__part01.jsonl_

## Nodes

## Node — Org / `Org:kcsc_kcs_root_01`
- space: `subject`
- node_type: `Org`
- source_article: KCS general
- properties:
  - `name_ko`: 국가건설기준센터(KCSC)
  - `role`: KCS 표준시방서 관리·운영

## Node — Org / `Org:kcs_ordering_agency_01`
- space: `subject`
- node_type: `Org`
- source_article: KCS general
- properties:
  - `name_ko`: 발주자
  - `role`: 단계 승인·재시공 최종 권한

## Node — SiteEngineer / `SiteEngineer:kcs_site_engineer_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS general
- properties:
  - `name_ko`: 시공자(현장기술자)
  - `duties`: ["시공계획서 작성", "배합·재료 시험", "검측 요청", "시공기록 작성"]

## Node — Supervisor / `Supervisor:kcs_supervisor_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: KCS general
- properties:
  - `name_ko`: 감리원
  - `duties`: ["자재 검수", "시공 검측", "단계 승인 결재", "기록 검토"]

## Node — ChiefSupervisor / `ChiefSupervisor:kcs_chief_supervisor_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: KCS general
- properties:
  - `name_ko`: 책임감리원
  - `duties`: ["단계 승인 최종 결재", "재시공 협의", "비파괴·강도 판정 결재"]

## Node — SafetyManager / `SafetyManager:kcs_safety_manager_01`
- space: `subject`
- node_type: `SafetyManager`
- source_article: KCS general
- properties:
  - `name_ko`: 안전관리자
  - `duties`: ["작업 중지 권한", "안전시설 점검", "재해 예방 조치"]

## Node — Qualification / `Qualification:kcs_qual_site_engineer_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS general
- properties:
  - `name_ko`: 현장기술자(건설기술인)
  - `reference_law`: 건설기술 진흥법 시행령 제55조

## Node — Qualification / `Qualification:kcs_qual_supervisor_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS general
- properties:
  - `name_ko`: 감리원 자격
  - `reference_law`: 건설기술 진흥법 시행령 제55조

## Node — Qualification / `Qualification:kcs_qual_chief_supervisor_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS general
- properties:
  - `name_ko`: 책임감리원 자격
  - `reference_law`: 건설기술 진흥법 시행령 제55조

## Node — Qualification / `Qualification:kcs_qual_safety_manager_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS general
- properties:
  - `name_ko`: 안전관리자 자격
  - `reference_law`: 산업안전보건법 시행령 별표 4

## Node — Qualification / `Qualification:kcs_qual_ndt_ut_lvl2_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KS B ISO 9712
- properties:
  - `name_ko`: 비파괴검사 UT 레벨 2 이상
  - `reference_standard`: KS B ISO 9712

## Node — Qualification / `Qualification:kcs_qual_welder_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접기능자(승인시험 합격)
  - `reference_standard`: KS B ISO 9606

## Node — Qualification / `Qualification:kcs_qual_soil_geo_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 11 30
- properties:
  - `name_ko`: 토질·지반 기술자(토질및기초기술사 등)
  - `reference_law`: 국가기술자격법(토질및기초기술사)

## Node — ConstructionLog / `ConstructionLog:log_kcs_construction_01`
- space: `resource`
- node_type: `ConstructionLog`
- source_article: KCS general
- properties:
  - `name_ko`: 시공 일지
  - `purpose`: 타설·양생·시공 일별 기록

## Node — SupervisionLog / `SupervisionLog:log_kcs_supervision_01`
- space: `resource`
- node_type: `SupervisionLog`
- source_article: KCS general
- properties:
  - `name_ko`: 감리 일지
  - `purpose`: 검측 및 단계 승인 기록

## Node — Checklist / `Checklist:checklist_kcs_pre_pour_01`
- space: `resource`
- node_type: `Checklist`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 콘크리트 타설 전 체크리스트
  - `scope`: 거푸집·철근·기상·배합 확인

## Node — Checklist / `Checklist:checklist_kcs_form_strip_01`
- space: `resource`
- node_type: `Checklist`
- source_article: KCS 21 50 10
- properties:
  - `name_ko`: 거푸집·동바리 해체 체크리스트
  - `scope`: 강도·양생기간·부재 점검

## Node — Checklist / `Checklist:checklist_kcs_weld_pre_01`
- space: `resource`
- node_type: `Checklist`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접 전 체크리스트
  - `scope`: 기상·예열·자재·자격 확인

## Node — Checklist / `Checklist:checklist_kcs_scaffold_daily_01`
- space: `resource`
- node_type: `Checklist`
- source_article: KCS 21 60 05
- properties:
  - `name_ko`: 비계 일상 점검 체크리스트
  - `scope`: 기둥·연결부·발판·풍속

## Node — TestReport / `TestReport:test_kcs_strength_report_01`
- space: `resource`
- node_type: `TestReport`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 콘크리트 압축강도 시험성적서
  - `test_method`: KS F 2405

## Node — TestReport / `TestReport:test_kcs_ut_report_01`
- space: `resource`
- node_type: `TestReport`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접부 UT 시험성적서
  - `test_method`: KS B 0896

## Node — TestReport / `TestReport:test_kcs_torque_report_01`
- space: `resource`
- node_type: `TestReport`
- source_article: KCS 14 31 25
- properties:
  - `name_ko`: 고장력볼트 토크·축력 시험성적서

## Node — TestReport / `TestReport:test_kcs_monitoring_report_01`
- space: `resource`
- node_type: `TestReport`
- source_article: KCS 11 30 30
- properties:
  - `name_ko`: 연약지반 계측 보고서 (침하·간극수압·경사)

## Node — WorkPermit / `WorkPermit:permit_kcs_pour_01`
- space: `resource`
- node_type: `WorkPermit`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 콘크리트 타설 작업허가서

## Node — WorkPermit / `WorkPermit:permit_kcs_weld_01`
- space: `resource`
- node_type: `WorkPermit`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 강구조 용접 작업허가서

## Node — WorkPermit / `WorkPermit:permit_kcs_scaffold_01`
- space: `resource`
- node_type: `WorkPermit`
- source_article: KCS 21 60 05
- properties:
  - `name_ko`: 비계 작업 허가서 (기상 조건 확인)

## Node — SafetyInspectionReport / `SafetyInspectionReport:safety_kcs_scaffold_report_01`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: KCS 21 60 05
- properties:
  - `name_ko`: 비계 안전 점검 보고서

## Node — SafetyInspectionReport / `SafetyInspectionReport:safety_kcs_formwork_report_01`
- space: `resource`
- node_type: `SafetyInspectionReport`
- source_article: KCS 21 50 15
- properties:
  - `name_ko`: 거푸집·동바리 안전 점검 보고서

## Node — WorkType / `WorkType:kcs_14_20_worktype_concrete_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 콘크리트공사
  - `scope`: 타설·양생·다짐·해체·시험

## Node — WorkType / `WorkType:kcs_14_20_worktype_winter_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20 11
- properties:
  - `name_ko`: 한중콘크리트공사
  - `applies_when`: 일평균 기온 4℃ 이하

## Node — WorkType / `WorkType:kcs_14_20_worktype_hot_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20 12
- properties:
  - `name_ko`: 서중콘크리트공사
  - `applies_when`: 일평균 기온 25℃ 초과

## Node — WorkType / `WorkType:kcs_14_20_worktype_mass_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20 13
- properties:
  - `name_ko`: 매스콘크리트공사
  - `applies_when`: 수화열 관리 필요 부재(통상 두께 0.8m 이상)

## Node — WorkType / `WorkType:kcs_14_20_worktype_watertight_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20 40
- properties:
  - `name_ko`: 수밀콘크리트공사

## Node — StructuralComponent / `StructuralComponent:kcs_14_20_component_slab_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 콘크리트 슬래브·보

## Node — StructuralComponent / `StructuralComponent:kcs_14_20_component_column_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 콘크리트 기둥·벽체

## Node — StructuralComponent / `StructuralComponent:kcs_14_20_component_cantilever_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 20 10 / KCS 21 50 10
- properties:
  - `name_ko`: 콘크리트 캔틸레버 부재

## Node — Specification / `Specification:spec_kcs_14_20_main_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 00
- properties:
  - `name_ko`: KCS 14 20 콘크리트공사 표준시방서
  - `standard_no`: KCS 14 20 00
  - `issuer`: 국가건설기준센터
  - `latest_notice`: 국토교통부고시 제2024-879호 (2024-12-30)

## Node — Specification / `Specification:spec_kcs_14_20_mix_wb_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 물-결합재비(W/B) 한계
  - `standard_no`: KCS 14 20 10
  - `EX0_max_wb`: 0.6
  - `EX1_max_wb`: 0.55
  - `EX2_max_wb`: 0.5
  - `EX3_EX4_max_wb`: 0.45
  - `unit_water_max_kg_per_m3`: 185

## Node — Specification / `Specification:spec_kcs_14_20_slump_air_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 슬럼프·공기량·염화물 한계
  - `standard_no`: KCS 14 20 10
  - `slump_tolerance_mm`: ±25 (80~180mm 호칭)
  - `air_normal_pct`: 4.5±1.5
  - `air_lightweight_pct`: 5.0±1.5
  - `chloride_max_kg_per_m3`: 0.3
  - `test_methods`: ["KS F 2402", "KS F 2421", "KS F 2515"]

## Node — Specification / `Specification:spec_kcs_14_20_transport_time_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 운반·타설 시간 한계 (KS F 4009)
  - `standard_no`: KCS 14 20 10
  - `limit_below_25C_hours`: 1.5
  - `limit_above_25C_hours`: 1.0
  - `cold_joint_below_25C_hours`: 2.5
  - `cold_joint_above_25C_hours`: 2.0
  - `reference_standard`: KS F 4009

## Node — Specification / `Specification:spec_kcs_14_20_placement_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 타설·다짐 한계
  - `standard_no`: KCS 14 20 10
  - `free_fall_max_m`: 1.5
  - `vibrator_spacing_max_cm`: 50
  - `vibrator_dwell_sec`: 5~15
  - `pump_vertical_max_m`: 100
  - `pump_horizontal_max_m`: 300

## Node — Specification / `Specification:spec_kcs_14_20_rain_exception_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 우천 시 타설 예외·중지 기준
  - `standard_no`: KCS 14 20 10
  - `rule`: 강우 시 타설 금지 원칙, 시트·천막 양생 보호 시 한정 시공
  - `stop_condition`: ["호우주의보 발효", "표면 빗물 고임·워싱아웃 우려", "강풍주의보 발효"]

## Node — Specification / `Specification:spec_kcs_14_20_cold_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 11
- properties:
  - `name_ko`: 한중콘크리트 시공 한계
  - `standard_no`: KCS 14 20 11
  - `trigger_temp_C`: 일평균 4 이하 또는 24h 내 0 예상
  - `placement_temp_range_C`: 5 ~ 20
  - `curing_surface_min_C`: 5
  - `initial_frost_strength_MPa`: 5
  - `insulated_curing_days_min`: 5
  - `heated_curing_days_min`: 3
  - `heating_mandatory_below_C`: -3
  - `heated_mandatory_below_C`: -10

## Node — Specification / `Specification:spec_kcs_14_20_hot_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 12
- properties:
  - `name_ko`: 서중콘크리트 시공 한계
  - `standard_no`: KCS 14 20 12
  - `trigger_temp_C`: 일평균 25 초과 또는 최고 30 초과
  - `placement_temp_max_C`: 35
  - `transport_max_hours`: 1.0
  - `wet_curing_days_min`: 5

## Node — Specification / `Specification:spec_kcs_14_20_curing_general_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 일반 습윤양생 기간
  - `standard_no`: KCS 14 20 10
  - `T15_days_min`: 5
  - `T10to15_days_min`: 7
  - `T5to10_days_min`: 9
  - `curing_temp_min_C`: 5
  - `no_impact_hours_min`: 24

## Node — Specification / `Specification:spec_kcs_14_20_strip_form_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 거푸집·동바리 해체 강도 기준
  - `standard_no`: KCS 14 20 10
  - `side_form_min_MPa`: 5
  - `simply_supported_min_fck_pct`: 50
  - `continuous_min_fck_pct`: 100
  - `cantilever_min_fck_pct`: 100
  - `test_method`: KS F 2405

## Node — Specification / `Specification:spec_kcs_14_20_strength_judge_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 압축강도 합격 판정
  - `standard_no`: KCS 14 20 10
  - `single_min_pct`: 85
  - `three_avg_min_pct`: 100
  - `frequency`: 150㎥/회 (KS F 4009)

## Node — Specification / `Specification:spec_kcs_14_20_unit_cement_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 최소 단위시멘트량
  - `standard_no`: KCS 14 20 10
  - `min_kg_per_m3_range`: 270 ~ 330
  - `depends_on`: 노출등급(EX0~EX4)

## Node — Specification / `Specification:spec_kcs_14_20_aggregate_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 굵은골재 최대치수 한계
  - `standard_no`: KCS 14 20 10
  - `slab_beam_max_mm`: 25
  - `general_max_mm`: 40

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:decision_kcs_14_20_material_01`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 콘크리트 자재 검수 결정
  - `criterion_source`: KCS 14 20 10 자재 검수

## Node — StageApprovalDecision / `StageApprovalDecision:decision_kcs_14_20_mix_approval_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 콘크리트 배합·시공계획서 승인
  - `criterion_source`: KCS 14 20 10
  - `checks`: ["W/B비", "단위수량", "슬럼프", "공기량"]

## Node — WorkPermitDecision / `WorkPermitDecision:decision_kcs_14_20_pour_permit_01`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 콘크리트 타설 작업허가
  - `criterion_source`: KCS 14 20 10
  - `preconditions`: ["거푸집 검측 완료", "철근 배근 검측 완료", "기상 적합 (강우 없음·기온 적합)"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 타설 검측 (다짐·이어치기·자유낙하)
  - `criterion_source`: KCS 14 20 10

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 20 11
- properties:
  - `name_ko`: 한중콘크리트 양생 검측
  - `criterion_source`: KCS 14 20 11
  - `checks`: ["콘크리트 온도", "양생 시설", "초기 동해 방지"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 20 12
- properties:
  - `name_ko`: 서중콘크리트 양생 검측
  - `criterion_source`: KCS 14 20 12
  - `checks`: ["콘크리트 온도", "습윤양생", "차광"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 압축강도 시험 판정
  - `criterion_source`: KCS 14 20 10

## Node — StageApprovalDecision / `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 14 20 10
- properties:
  - `name_ko`: 거푸집·동바리 해체 승인
  - `criterion_source`: KCS 14 20 10 + KCS 21 50 10

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_14_20_pass_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 합격·승인
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_14_20_rework_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 재시공·보강
  - `result`: rework

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_14_20_stop_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 20
- properties:
  - `name_ko`: 작업 중지(우천·강풍·기온)
  - `result`: work_stop

## Node — WorkType / `WorkType:kcs_14_31_worktype_steel_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 31
- properties:
  - `name_ko`: 강구조공사
  - `scope`: 공장제작·현장설치·용접·볼트접합·도장

## Node — WorkType / `WorkType:kcs_14_31_worktype_weld_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 강구조 용접 (결합법)
  - `scope`: 맞대기·필릿·부분침투

## Node — WorkType / `WorkType:kcs_14_31_worktype_hsb_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 31 25
- properties:
  - `name_ko`: 고장력볼트 접합 (결합법)
  - `scope`: 마찰·인장·지압 접합

## Node — WorkType / `WorkType:kcs_14_31_worktype_paint_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 31 40
- properties:
  - `name_ko`: 강구조 도장
  - `scope`: 표면처리·도막두께

## Node — StructuralComponent / `StructuralComponent:kcs_14_31_component_beam_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 31
- properties:
  - `name_ko`: 강재 보·기둥

## Node — StructuralComponent / `StructuralComponent:kcs_14_31_component_weld_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접부 (맞대기 그루브)

## Node — StructuralComponent / `StructuralComponent:kcs_14_31_component_bolt_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 31 25
- properties:
  - `name_ko`: 고장력볼트 접합부

## Node — Specification / `Specification:spec_kcs_14_31_main_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31
- properties:
  - `name_ko`: KCS 14 31 강구조공사 표준시방서
  - `standard_no`: KCS 14 31 00
  - `latest_notice`: 국토교통부고시 제2024-224호

## Node — Specification / `Specification:spec_kcs_14_31_precision_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 05
- properties:
  - `name_ko`: 강구조 정밀도(시공 한계)
  - `standard_no`: KCS 14 31 05
  - `length_tol_mm`: ±2 ~ ±3
  - `vert_tol_max_mm`: 35
  - `vert_tol_ratio`: ±H/1000
  - `horiz_tol_ratio`: ±L/1000
  - `twist_tol_ratio`: ±L/700
  - `bolt_hole_offset_mm`: ±1

## Node — Specification / `Specification:spec_kcs_14_31_weld_env_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접 시공 환경 한계
  - `standard_no`: KCS 14 31 20
  - `ambient_temp_min_C`: -5
  - `preheat_required_below_C`: 5
  - `wind_gas_shield_max_m_per_s`: 2
  - `wind_stop_all_m_per_s`: 10
  - `humidity_stop_pct`: 80
  - `rain_snow_rule`: 차폐 불가 시 작업 중지

## Node — Specification / `Specification:spec_kcs_14_31_preheat_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 예열 온도
  - `standard_no`: KCS 14 31 20
  - `SM355_t25_min_C`: 50
  - `SM355_t25_50_min_C`: 80
  - `SM490_t50_min_C`: 100
  - `HSA800_min_C`: 100
  - `additional_below_0C_C`: 25
  - `measure_point_mm_from_weld`: 75

## Node — Specification / `Specification:spec_kcs_14_31_ut_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접부 UT 검사 기준
  - `standard_no`: KCS 14 31 20
  - `qualification`: KS B ISO 9712 Level 2
  - `method_standard`: KS B 0896
  - `delay_after_weld_hours`: 8 ~ 48
  - `lot_size`: 300 용접/로트
  - `sample_per_lot`: 30
  - `accept_initial_max_defects`: 1
  - `rework_range`: 2~3
  - `rework_60_pass_max`: 4

## Node — Specification / `Specification:spec_kcs_14_31_rework_limit_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접 재시공 한계
  - `standard_no`: KCS 14 31 20
  - `normal_steel_max_redo`: 3
  - `high_strength_steel_max_redo`: 2
  - `action_if_exceed`: 부재 교체 협의

## Node — Specification / `Specification:spec_kcs_14_31_hsb_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 25
- properties:
  - `name_ko`: 고장력볼트 시공
  - `standard_no`: KCS 14 31 25
  - `grades`: ["F8T", "F10T", "F13T", "S10T"]
  - `primary_tighten_pct`: 60
  - `final_tighten_pct`: 100
  - `final_tolerance_pct`: 10
  - `nut_rotation_deg_options`: [60, 90, 120]
  - `rain_snow_rule`: 마찰면 노출 금지, 미처리 시 본 조임 금지

## Node — Specification / `Specification:spec_kcs_14_31_hsb_inspect_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 25
- properties:
  - `name_ko`: 고장력볼트 검사
  - `standard_no`: KCS 14 31 25
  - `sample_pct_per_group`: 10
  - `min_sample_count`: 10
  - `marking_check`: 본 조임 후 마킹 어긋남으로 확인
  - `reuse`: 불합격 볼트 재사용 금지

## Node — Specification / `Specification:spec_kcs_14_31_paint_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 40
- properties:
  - `name_ko`: 도장 환경 한계
  - `standard_no`: KCS 14 31 40
  - `surface_prep`: SSPC-SP10 / Sa2.5
  - `steel_temp_range_C`: 5 ~ 50
  - `dew_point_margin_C`: 3
  - `humidity_max_pct`: 85
  - `wind_spray_stop_m_per_s`: 8
  - `DFT_um_range`: 200 ~ 320

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:decision_kcs_14_31_material_01`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: KCS 14 31
- properties:
  - `name_ko`: 강재·볼트·용접재 검수 결정
  - `criterion_source`: KCS 14 31 05

## Node — StageApprovalDecision / `StageApprovalDecision:decision_kcs_14_31_plan_approval_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 14 31
- properties:
  - `name_ko`: 강구조 시공계획서 승인
  - `criterion_source`: KCS 14 31 05

## Node — WorkPermitDecision / `WorkPermitDecision:decision_kcs_14_31_weld_permit_01`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접 작업허가 (기상·예열 확인)
  - `criterion_source`: KCS 14 31 20
  - `stop_triggers`: ["기온 -5℃ 이하", "풍속 10m/s 초과", "강우·강설"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 31
- properties:
  - `name_ko`: 용접 외관 검사·정밀도 검측
  - `criterion_source`: KCS 14 31 05·20

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_14_31_ut_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접부 UT 검사 판정
  - `criterion_source`: KCS 14 31 20 / KS B 0896

## Node — WorkPermitDecision / `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: KCS 14 31 25
- properties:
  - `name_ko`: 고장력볼트 본 조임 작업허가
  - `criterion_source`: KCS 14 31 25
  - `preconditions`: ["마찰면 처리 완료", "1차 조임·마킹 완료", "강우·강설 없음"]

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 31 25
- properties:
  - `name_ko`: 고장력볼트 토크·마킹 검사
  - `criterion_source`: KCS 14 31 25

## Node — WorkPermitDecision / `WorkPermitDecision:decision_kcs_14_31_paint_permit_01`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: KCS 14 31 40
- properties:
  - `name_ko`: 도장 작업허가 (온도·습도·풍속)
  - `criterion_source`: KCS 14 31 40

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 31 40
- properties:
  - `name_ko`: 도장 외관·도막두께 검사
  - `criterion_source`: KCS 14 31 40

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_14_31_pass_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 31
- properties:
  - `name_ko`: 용접·볼트·도장 합격
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_14_31_rework_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 31
- properties:
  - `name_ko`: 용접 재용접·볼트 재시공·도장 보수
  - `result`: rework

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_14_31_reject_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 31
- properties:
  - `name_ko`: 용접부 불합격(부재 교체·재제작)
  - `result`: reject

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_14_31_stop_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 31
- properties:
  - `name_ko`: 작업 중지(풍속·강우·기온)
  - `result`: work_stop

## Node — SiteEngineer / `SiteEngineer:kcs_14_31_ut_inspector_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 비파괴검사 기술자 (UT Lv.2 이상)
  - `duties`: ["KS B 0896 UT 수행", "결함 등급 판정"]

## Node — SiteEngineer / `SiteEngineer:kcs_14_31_welder_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS 14 31 20
- properties:
  - `name_ko`: 용접기능자(승인시험 합격자)
  - `duties`: ["승인된 절차서로 용접 수행"]

## Edges

## Edge — `qualified_as`
- from: `SiteEngineer:kcs_site_engineer_01` (subject)
- to: `Qualification:kcs_qual_site_engineer_01` (concept)
- source_article: KCS general

## Edge — `qualified_as`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `Qualification:kcs_qual_supervisor_01` (concept)
- source_article: KCS general

## Edge — `qualified_as`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- source_article: KCS general

## Edge — `qualified_as`
- from: `SafetyManager:kcs_safety_manager_01` (subject)
- to: `Qualification:kcs_qual_safety_manager_01` (concept)
- source_article: KCS general

## Edge — `subclass_of`
- from: `WorkType:kcs_14_20_worktype_mass_01` (concept)
- to: `WorkType:kcs_14_20_worktype_concrete_01` (concept)
- source_article: KCS 14 20 13

## Edge — `subclass_of`
- from: `WorkType:kcs_14_20_worktype_watertight_01` (concept)
- to: `WorkType:kcs_14_20_worktype_concrete_01` (concept)
- source_article: KCS 14 20 40

## Edge — `subclass_of`
- from: `WorkType:kcs_14_20_worktype_winter_01` (concept)
- to: `WorkType:kcs_14_20_worktype_concrete_01` (concept)
- source_article: KCS 14 20 11

## Edge — `subclass_of`
- from: `WorkType:kcs_14_20_worktype_hot_01` (concept)
- to: `WorkType:kcs_14_20_worktype_concrete_01` (concept)
- source_article: KCS 14 20 12

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- to: `Specification:spec_kcs_14_20_unit_cement_01` (resource)
- source_article: KCS 14 20 10

## Edge — `based_on`
- from: `MaterialReceiptDecision:decision_kcs_14_20_material_01` (decision)
- to: `Specification:spec_kcs_14_20_aggregate_01` (resource)
- source_article: KCS 14 20 10

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `MaterialReceiptDecision:decision_kcs_14_20_material_01` (decision)
- source_article: KCS 14 20

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- source_article: KCS 14 20

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- source_article: KCS 14 20

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- source_article: KCS 14 20

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01` (decision)
- source_article: KCS 14 20 11

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01` (decision)
- source_article: KCS 14 20 12

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- source_article: KCS 14 20 10

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- source_article: KCS 14 20 10

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `MaterialReceiptDecision:decision_kcs_14_20_material_01` (decision)
- source_article: KCS 14 20

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- source_article: KCS 14 20

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- source_article: KCS 14 20

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- source_article: KCS 14 20

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01` (decision)
- source_article: KCS 14 20 11

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01` (decision)
- source_article: KCS 14 20 12

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- source_article: KCS 14 20 10

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- source_article: KCS 14 20 10

## Edge — `based_on`
- from: `MaterialReceiptDecision:decision_kcs_14_20_material_01` (decision)
- to: `Specification:spec_kcs_14_20_main_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `MaterialReceiptDecision:decision_kcs_14_20_material_01` (decision)
- to: `Specification:spec_kcs_14_20_slump_air_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- to: `Specification:spec_kcs_14_20_mix_wb_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- to: `Specification:spec_kcs_14_20_slump_air_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `Specification:spec_kcs_14_20_transport_time_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `Specification:spec_kcs_14_20_rain_exception_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- to: `Specification:spec_kcs_14_20_placement_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- to: `Specification:spec_kcs_14_20_transport_time_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01` (decision)
- to: `Specification:spec_kcs_14_20_cold_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01` (decision)
- to: `Specification:spec_kcs_14_20_curing_general_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01` (decision)
- to: `Specification:spec_kcs_14_20_hot_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01` (decision)
- to: `Specification:spec_kcs_14_20_curing_general_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- to: `Specification:spec_kcs_14_20_strength_judge_01` (resource)
- source_article: KCS 14 20

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- to: `Specification:spec_kcs_14_20_strip_form_01` (resource)
- source_article: KCS 14 20

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- to: `WorkType:kcs_14_20_worktype_concrete_01` (concept)
- source_article: KCS 14 20

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- to: `WorkType:kcs_14_20_worktype_concrete_01` (concept)
- source_article: KCS 14 20

## Edge — `targets_work_type`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `WorkType:kcs_14_20_worktype_concrete_01` (concept)
- source_article: KCS 14 20

## Edge — `targets_work_type`
- from: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- to: `WorkType:kcs_14_20_worktype_concrete_01` (concept)
- source_article: KCS 14 20

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01` (decision)
- to: `WorkType:kcs_14_20_worktype_winter_01` (concept)
- source_article: KCS 14 20 11

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01` (decision)
- to: `WorkType:kcs_14_20_worktype_hot_01` (concept)
- source_article: KCS 14 20 12

## Edge — `targets_component`
- from: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- to: `StructuralComponent:kcs_14_20_component_slab_01` (concept)
- source_article: KCS 14 20 10

## Edge — `targets_component`
- from: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- to: `StructuralComponent:kcs_14_20_component_column_01` (concept)
- source_article: KCS 14 20 10

## Edge — `targets_component`
- from: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- to: `StructuralComponent:kcs_14_20_component_cantilever_01` (concept)
- source_article: KCS 14 20 10

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- to: `StructuralComponent:kcs_14_20_component_slab_01` (concept)
- source_article: KCS 14 20 10

## Edge — `yields`
- from: `MaterialReceiptDecision:decision_kcs_14_20_material_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_pass_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `MaterialReceiptDecision:decision_kcs_14_20_material_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_rework_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_pass_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_rework_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_pass_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_rework_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_pass_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_rework_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_pass_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_rework_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_pass_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_rework_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_pass_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_rework_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_pass_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_rework_01` (outcome)
- source_article: KCS 14 20

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_20_stop_01` (outcome)
- source_article: KCS 14 20 10 rain exception

## Edge — `precedes`
- from: `MaterialReceiptDecision:decision_kcs_14_20_material_01` (decision)
- to: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- source_article: KCS 14 20

## Edge — `depends_on`
- from: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- to: `MaterialReceiptDecision:decision_kcs_14_20_material_01` (decision)
- source_article: KCS 14 20

## Edge — `precedes`
- from: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- to: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- source_article: KCS 14 20

## Edge — `depends_on`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `StageApprovalDecision:decision_kcs_14_20_mix_approval_01` (decision)
- source_article: KCS 14 20

## Edge — `precedes`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- source_article: KCS 14 20

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- to: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- source_article: KCS 14 20

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- source_article: KCS 14 20

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- source_article: KCS 14 20

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- to: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- source_article: KCS 14 20

## Edge — `depends_on`
- from: `StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- source_article: KCS 14 20

## Edge — `subclass_of`
- from: `WorkType:kcs_14_31_worktype_weld_01` (concept)
- to: `WorkType:kcs_14_31_worktype_steel_01` (concept)
- source_article: KCS 14 31 20

## Edge — `subclass_of`
- from: `WorkType:kcs_14_31_worktype_hsb_01` (concept)
- to: `WorkType:kcs_14_31_worktype_steel_01` (concept)
- source_article: KCS 14 31 25

## Edge — `subclass_of`
- from: `WorkType:kcs_14_31_worktype_paint_01` (concept)
- to: `WorkType:kcs_14_31_worktype_steel_01` (concept)
- source_article: KCS 14 31 40

## Edge — `qualified_as`
- from: `SiteEngineer:kcs_14_31_ut_inspector_01` (subject)
- to: `Qualification:kcs_qual_ndt_ut_lvl2_01` (concept)
- source_article: KCS 14 31 20

## Edge — `qualified_as`
- from: `SiteEngineer:kcs_14_31_welder_01` (subject)
- to: `Qualification:kcs_qual_welder_01` (concept)
- source_article: KCS 14 31 20

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `MaterialReceiptDecision:decision_kcs_14_31_material_01` (decision)
- source_article: KCS 14 31

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `MaterialReceiptDecision:decision_kcs_14_31_material_01` (decision)
- source_article: KCS 14 31

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- source_article: KCS 14 31

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- source_article: KCS 14 31

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- source_article: KCS 14 31

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- source_article: KCS 14 31

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_ndt_ut_lvl2_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- source_article: KCS 14 31

## Edge — `performs`
- from: `SiteEngineer:kcs_14_31_ut_inspector_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- source_article: KCS 14 31

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- source_article: KCS 14 31

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- source_article: KCS 14 31

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01` (decision)
- source_article: KCS 14 31

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01` (decision)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `MaterialReceiptDecision:decision_kcs_14_31_material_01` (decision)
- to: `Specification:spec_kcs_14_31_main_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- to: `Specification:spec_kcs_14_31_main_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- to: `Specification:spec_kcs_14_31_precision_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `Specification:spec_kcs_14_31_weld_env_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `Specification:spec_kcs_14_31_preheat_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- to: `Specification:spec_kcs_14_31_precision_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `Specification:spec_kcs_14_31_ut_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `Specification:spec_kcs_14_31_rework_limit_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- to: `Specification:spec_kcs_14_31_hsb_01` (resource)
- source_article: KCS 14 31
