# Extracted graph — KCS__part02.jsonl

_source jsonl: KCS__part02.jsonl_

## Nodes

## Node — WorkType / `WorkType:kcs_21_50_worktype_formwork_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 21 50
- properties:
  - `name_ko`: 거푸집·동바리 공사
  - `scope`: 조립·점검·해체

## Node — StructuralComponent / `StructuralComponent:kcs_21_50_component_form_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 21 50
- properties:
  - `name_ko`: 거푸집(측벽·기둥·슬래브 밑면)

## Node — StructuralComponent / `StructuralComponent:kcs_21_50_component_shore_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 21 50
- properties:
  - `name_ko`: 동바리(파이프 서포트·시스템 동바리)

## Node — Specification / `Specification:spec_kcs_21_50_main_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50
- properties:
  - `name_ko`: KCS 21 50 거푸집 및 동바리 표준시방서
  - `standard_no`: KCS 21 50 00

## Node — Specification / `Specification:spec_kcs_21_50_load_vert_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50 05
- properties:
  - `name_ko`: 연직 하중 (자중+작업하중+측압)
  - `standard_no`: KCS 21 50 05
  - `work_load_kN_per_m2`: 1.5
  - `slab_thick_extra_above_m`: 0.5
  - `pump_impact_pct_of_pressure`: 50

## Node — Specification / `Specification:spec_kcs_21_50_pressure_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50 05
- properties:
  - `name_ko`: 콘크리트 측압 한계
  - `standard_no`: KCS 21 50 05
  - `max_pressure_kN_per_m2`: 100
  - `formula`: P = w·H (수정식: R, T 보정)

## Node — Specification / `Specification:spec_kcs_21_50_load_horiz_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50 05
- properties:
  - `name_ko`: 수평 하중·풍하중
  - `standard_no`: KCS 21 50 05
  - `horiz_load_min_pct_of_vert`: 2
  - `horiz_load_min_kN_per_m`: 1.5
  - `wind_load_reference`: KDS 41 12 00

## Node — Specification / `Specification:spec_kcs_21_50_shore_safety_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50 15
- properties:
  - `name_ko`: 동바리 강도·좌굴 한계
  - `standard_no`: KCS 21 50 15
  - `safety_factor_min`: 2.5
  - `pipe_shore_max_height_m`: 3.5
  - `horizontal_brace_spacing_m`: 2.0
  - `lateral_deflection_max`: H/200

## Node — Specification / `Specification:spec_kcs_21_50_strip_strength_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50 10
- properties:
  - `name_ko`: 해체 시기 — 강도 기준
  - `standard_no`: KCS 21 50 10 / KCS 14 20 10
  - `side_form_min_MPa`: 5
  - `simply_supported_min_fck_pct`: 50
  - `simply_supported_min_MPa`: 14
  - `continuous_min_fck_pct`: 100
  - `cantilever_min_fck_pct`: 100

## Node — Specification / `Specification:spec_kcs_21_50_strip_curing_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50 10
- properties:
  - `name_ko`: 해체 시기 — 양생 기간 환산 (보통포틀랜드시멘트)
  - `standard_no`: KCS 21 50 10
  - `T20_side_days`: 1~2
  - `T20_simply_days`: 8
  - `T20_continuous_days`: 21
  - `T10_20_side_days`: 2~3
  - `T10_20_simply_days`: 14
  - `T10_20_continuous_days`: 28
  - `T5_10_side_days`: 3~4
  - `T5_10_simply_days`: 20
  - `T5_10_continuous_days`: 35

## Node — Specification / `Specification:spec_kcs_21_50_reuse_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50 10
- properties:
  - `name_ko`: 재사용 한도
  - `standard_no`: KCS 21 50 10
  - `timber_reuse_max`: 7
  - `plywood_coated_reuse_max`: 10
  - `steel_form_reuse_max`: 100
  - `shore_pipe_max_strain_pct`: 0.5

## Node — Specification / `Specification:spec_kcs_21_50_weather_stop_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50 05
- properties:
  - `name_ko`: 거푸집·동바리 시공 중 작업 중지 기상 한계
  - `standard_no`: KCS 21 50 05
  - `wind_stop_m_per_s`: 10
  - `rain_stop`: 작업발판 미끄럼 우려 시 중지
  - `snow_ice_stop`: 결빙·적설 시 중지
  - `visibility_stop_m_below`: 100

## Node — Specification / `Specification:spec_kcs_21_50_settle_check_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 50 15
- properties:
  - `name_ko`: 동바리 침하·변형 한계
  - `standard_no`: KCS 21 50 15
  - `settlement_alarm_mm`: 5
  - `inspection_after_wind_m_per_s`: 10

## Node — StageApprovalDecision / `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 21 50
- properties:
  - `name_ko`: 거푸집·동바리 시공계획 승인
  - `criterion_source`: KCS 21 50 05 + 산안기준 제331조

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 21 50
- properties:
  - `name_ko`: 거푸집·동바리 조립 검측 (타설 전)
  - `criterion_source`: KCS 21 50 05·15

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: KCS 21 50
- properties:
  - `name_ko`: 거푸집·동바리 안전 점검 (강풍·강진·강우 후)
  - `criterion_source`: KCS 21 50 05·15

## Node — StageApprovalDecision / `StageApprovalDecision:decision_kcs_21_50_strip_approval_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 21 50 10
- properties:
  - `name_ko`: 거푸집·동바리 해체 승인 (강도·양생 확인)
  - `criterion_source`: KCS 21 50 10 / KCS 14 20 10

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 21 50 10
- properties:
  - `name_ko`: 해체 직후 부재 검측 (침하·균열·처짐)
  - `criterion_source`: KCS 21 50 10

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_21_50_pass_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 21 50
- properties:
  - `name_ko`: 거푸집·동바리 합격
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_21_50_rework_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 21 50
- properties:
  - `name_ko`: 재조립·보강
  - `result`: rework

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_21_50_stop_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 21 50
- properties:
  - `name_ko`: 작업 중지(풍속·강진·강우)
  - `result`: work_stop

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_21_50_redo_pour_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 21 50 10
- properties:
  - `name_ko`: 재타설·부재 보강 (해체 후 침하·균열)
  - `result`: rework

## Node — WorkType / `WorkType:kcs_11_30_worktype_softground_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 11 30
- properties:
  - `name_ko`: 연약지반 처리·압밀공사
  - `scope`: 압밀·치환·고결·다짐

## Node — WorkType / `WorkType:kcs_11_30_worktype_pbd_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 11 30 10
- properties:
  - `name_ko`: 연직배수공법(PBD/SD)

## Node — Facility / `Facility:kcs_11_30_facility_embankment_01`
- space: `concept`
- node_type: `Facility`
- source_article: KCS 11 30
- properties:
  - `name_ko`: 성토부(연약지반)
  - `scope`: 도로·철도 노반·교대 접속부

## Node — StructuralComponent / `StructuralComponent:kcs_11_30_component_pbd_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 11 30 10
- properties:
  - `name_ko`: PBD(Plastic Board Drain)

## Node — Specification / `Specification:spec_kcs_11_30_main_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30
- properties:
  - `name_ko`: KCS 11 30 연약지반 표준시방서
  - `standard_no`: KCS 11 30 00

## Node — Specification / `Specification:spec_kcs_11_30_settle_limit_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 05
- properties:
  - `name_ko`: 잔류침하 허용 한계
  - `standard_no`: KCS 11 30 05
  - `road_general_max_cm`: 30
  - `bridge_abutment_max_cm`: 10
  - `rail_high_speed_max_cm`: 3
  - `rail_general_max_cm`: 10

## Node — Specification / `Specification:spec_kcs_11_30_construction_limit_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 05
- properties:
  - `name_ko`: 시공 중 침하·변형 한계
  - `standard_no`: KCS 11 30 05
  - `daily_settle_stop_cm_per_day`: 1.0
  - `daily_lateral_max_cm_per_day`: 0.5

## Node — Specification / `Specification:spec_kcs_11_30_consolidation_judge_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 05
- properties:
  - `name_ko`: 압밀 완료 판정
  - `standard_no`: KCS 11 30 05
  - `structure_U_pct_min`: 90
  - `bridge_abutment_U_pct_min`: 95
  - `methods`: ["Hyperbolic", "Asaoka"]
  - `hyperbolic_valid_above_pct`: 60

## Node — Specification / `Specification:spec_kcs_11_30_pbd_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 10
- properties:
  - `name_ko`: PBD 사양·간격
  - `standard_no`: KCS 11 30 10
  - `pbd_width_min_mm`: 100
  - `discharge_min_cm3_per_s`: 100
  - `depth_overlap_m`: 1
  - `spacing_min_m`: 1.0
  - `spacing_max_m`: 1.5
  - `depth_practical_max_m`: 30

## Node — Specification / `Specification:spec_kcs_11_30_stability_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 05
- properties:
  - `name_ko`: 성토 사면 안정 안전율
  - `standard_no`: KCS 11 30 05
  - `construction_min_FS`: 1.2
  - `permanent_min_FS`: 1.5
  - `seismic_min_FS`: 1.0
  - `stage_lift_height_m`: 1.5~2.0
  - `next_stage_U_pct_min`: 70

## Node — Specification / `Specification:spec_kcs_11_30_monitor_freq_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 30
- properties:
  - `name_ko`: 계측 빈도
  - `standard_no`: KCS 11 30 30
  - `construction_freq`: 1일 1회 (성토 1m마다)
  - `early_post_freq`: 주 2~3회 (성토 완료 후 6개월)
  - `late_post_freq`: 월 1~2회
  - `items`: ["침하판", "층별 침하계", "간극수압계", "지중 경사계", "토압계"]

## Node — Specification / `Specification:spec_kcs_11_30_alarm_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 30
- properties:
  - `name_ko`: 3단계 계측 관리 기준
  - `standard_no`: KCS 11 30 30
  - `yellow_pct_of_predict`: 70
  - `yellow_daily_cm`: 1.0
  - `orange_pct_of_predict`: 85
  - `orange_daily_cm`: 1.5
  - `red_pct_of_predict`: 100
  - `red_daily_cm`: 2.0
  - `action_on_red`: 성토 중지·전문가 검토

## Node — Specification / `Specification:spec_kcs_11_30_replace_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 15
- properties:
  - `name_ko`: 치환공법 적용 한계
  - `standard_no`: KCS 11 30 15
  - `soft_layer_max_m`: 5

## Node — Specification / `Specification:spec_kcs_11_30_dmm_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 20
- properties:
  - `name_ko`: 심층혼합처리 (DMM) 설계강도
  - `standard_no`: KCS 11 30 20
  - `design_strength_28d_MPa_min`: 1.0

## Node — Specification / `Specification:spec_kcs_11_30_compaction_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 25
- properties:
  - `name_ko`: 다짐공법 (SCP·진동다짐) 검측 기준
  - `standard_no`: KCS 11 30 25
  - `relative_density_min_pct`: 70
  - `applicable_soil`: 사질토
  - `verification`: N치 증가량 측정

## Node — Specification / `Specification:spec_kcs_11_30_sand_drain_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 11 30 10
- properties:
  - `name_ko`: 샌드드레인(SD) 사양
  - `standard_no`: KCS 11 30 10
  - `diameter_mm`: 400
  - `spacing_m_range`: 2.0 ~ 3.0

## Node — StageApprovalDecision / `StageApprovalDecision:decision_kcs_11_30_plan_approval_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 11 30
- properties:
  - `name_ko`: 연약지반 처리 시공계획 승인
  - `criterion_source`: KCS 11 30 05

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 11 30 10
- properties:
  - `name_ko`: PBD 시공 검측 (간격·깊이·통수능)
  - `criterion_source`: KCS 11 30 10

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 11 30 30
- properties:
  - `name_ko`: 계측 결과 검측·관리 단계 판정
  - `criterion_source`: KCS 11 30 30

## Node — StageApprovalDecision / `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 11 30 05
- properties:
  - `name_ko`: 압밀 완료 판정·다음 공정 승인
  - `criterion_source`: KCS 11 30 05

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: KCS 11 30 30
- properties:
  - `name_ko`: 성토 중지 결정 (1일 침하 한계 초과)
  - `criterion_source`: KCS 11 30 30

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_11_30_pass_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 11 30
- properties:
  - `name_ko`: 압밀 완료·다음 공정 진행
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_11_30_wait_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 11 30
- properties:
  - `name_ko`: 압밀 대기·추가 계측
  - `result`: hold

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_11_30_stop_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 11 30
- properties:
  - `name_ko`: 성토 중지(관리 기준 초과)
  - `result`: work_stop

## Node — SiteEngineer / `SiteEngineer:kcs_11_30_geo_engineer_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS 11 30
- properties:
  - `name_ko`: 토질·지반 기술자
  - `duties`: ["압밀 예측", "안정해석", "계측 해석"]

## Edges

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- to: `Specification:spec_kcs_14_31_hsb_inspect_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- to: `Specification:spec_kcs_14_31_hsb_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- to: `Specification:spec_kcs_14_31_paint_01` (resource)
- source_article: KCS 14 31

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01` (decision)
- to: `Specification:spec_kcs_14_31_paint_01` (resource)
- source_article: KCS 14 31

## Edge — `targets_work_type`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `WorkType:kcs_14_31_worktype_weld_01` (concept)
- source_article: KCS 14 31 20

## Edge — `targets_component`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `StructuralComponent:kcs_14_31_component_weld_01` (concept)
- source_article: KCS 14 31 20

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- to: `WorkType:kcs_14_31_worktype_weld_01` (concept)
- source_article: KCS 14 31 20

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- to: `StructuralComponent:kcs_14_31_component_weld_01` (concept)
- source_article: KCS 14 31 20

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `WorkType:kcs_14_31_worktype_weld_01` (concept)
- source_article: KCS 14 31 20

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `StructuralComponent:kcs_14_31_component_weld_01` (concept)
- source_article: KCS 14 31 20

## Edge — `targets_work_type`
- from: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- to: `WorkType:kcs_14_31_worktype_hsb_01` (concept)
- source_article: KCS 14 31 25

## Edge — `targets_component`
- from: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- to: `StructuralComponent:kcs_14_31_component_bolt_01` (concept)
- source_article: KCS 14 31 25

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- to: `WorkType:kcs_14_31_worktype_hsb_01` (concept)
- source_article: KCS 14 31 25

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- to: `StructuralComponent:kcs_14_31_component_bolt_01` (concept)
- source_article: KCS 14 31 25

## Edge — `targets_work_type`
- from: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- to: `WorkType:kcs_14_31_worktype_paint_01` (concept)
- source_article: KCS 14 31 40

## Edge — `targets_component`
- from: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- to: `StructuralComponent:kcs_14_31_component_beam_01` (concept)
- source_article: KCS 14 31 40

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01` (decision)
- to: `WorkType:kcs_14_31_worktype_paint_01` (concept)
- source_article: KCS 14 31 40

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01` (decision)
- to: `StructuralComponent:kcs_14_31_component_beam_01` (concept)
- source_article: KCS 14 31 40

## Edge — `targets_work_type`
- from: `MaterialReceiptDecision:decision_kcs_14_31_material_01` (decision)
- to: `WorkType:kcs_14_31_worktype_steel_01` (concept)
- source_article: KCS 14 31

## Edge — `targets_work_type`
- from: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- to: `WorkType:kcs_14_31_worktype_steel_01` (concept)
- source_article: KCS 14 31

## Edge — `yields`
- from: `MaterialReceiptDecision:decision_kcs_14_31_material_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_pass_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `MaterialReceiptDecision:decision_kcs_14_31_material_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_rework_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_pass_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_rework_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_pass_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_rework_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_pass_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_rework_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_pass_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_rework_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_pass_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_rework_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_pass_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_rework_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_pass_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_rework_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_pass_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_rework_01` (outcome)
- source_article: KCS 14 31

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_reject_01` (outcome)
- source_article: KCS 14 31 20

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_stop_01` (outcome)
- source_article: KCS 14 31 20

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_14_31_stop_01` (outcome)
- source_article: KCS 14 31 40

## Edge — `precedes`
- from: `MaterialReceiptDecision:decision_kcs_14_31_material_01` (decision)
- to: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- source_article: KCS 14 31

## Edge — `depends_on`
- from: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- to: `MaterialReceiptDecision:decision_kcs_14_31_material_01` (decision)
- source_article: KCS 14 31

## Edge — `precedes`
- from: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- to: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `depends_on`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `StageApprovalDecision:decision_kcs_14_31_plan_approval_01` (decision)
- source_article: KCS 14 31

## Edge — `precedes`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- source_article: KCS 14 31

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- to: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- source_article: KCS 14 31

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01` (decision)
- source_article: KCS 14 31

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `depends_on`
- from: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- source_article: KCS 14 31

## Edge — `precedes`
- from: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- source_article: KCS 14 31

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- to: `WorkPermitDecision:decision_kcs_14_31_hsb_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- to: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `depends_on`
- from: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- source_article: KCS 14 31

## Edge — `precedes`
- from: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01` (decision)
- source_article: KCS 14 31

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01` (decision)
- to: `WorkPermitDecision:decision_kcs_14_31_paint_permit_01` (decision)
- source_article: KCS 14 31

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- source_article: KCS 21 50

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- source_article: KCS 21 50

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- source_article: KCS 21 50

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- source_article: KCS 21 50

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_safety_manager_01` (concept)
- to: `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01` (decision)
- source_article: KCS 21 50

## Edge — `performs`
- from: `SafetyManager:kcs_safety_manager_01` (subject)
- to: `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01` (decision)
- source_article: KCS 21 50

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- source_article: KCS 21 50

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- source_article: KCS 21 50

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01` (decision)
- source_article: KCS 21 50

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01` (decision)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `Specification:spec_kcs_21_50_main_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `Specification:spec_kcs_21_50_load_vert_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `Specification:spec_kcs_21_50_pressure_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `Specification:spec_kcs_21_50_load_horiz_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `Specification:spec_kcs_21_50_shore_safety_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- to: `Specification:spec_kcs_21_50_shore_safety_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- to: `Specification:spec_kcs_21_50_settle_check_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01` (decision)
- to: `Specification:spec_kcs_21_50_weather_stop_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01` (decision)
- to: `Specification:spec_kcs_21_50_settle_check_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `Specification:spec_kcs_21_50_strip_strength_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `Specification:spec_kcs_21_50_strip_curing_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `Specification:spec_kcs_21_50_reuse_01` (resource)
- source_article: KCS 21 50

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01` (decision)
- to: `Specification:spec_kcs_21_50_strip_strength_01` (resource)
- source_article: KCS 21 50

## Edge — `targets_work_type`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `WorkType:kcs_21_50_worktype_formwork_01` (concept)
- source_article: KCS 21 50

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- to: `WorkType:kcs_21_50_worktype_formwork_01` (concept)
- source_article: KCS 21 50

## Edge — `targets_work_type`
- from: `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01` (decision)
- to: `WorkType:kcs_21_50_worktype_formwork_01` (concept)
- source_article: KCS 21 50

## Edge — `targets_work_type`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `WorkType:kcs_21_50_worktype_formwork_01` (concept)
- source_article: KCS 21 50

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01` (decision)
- to: `WorkType:kcs_21_50_worktype_formwork_01` (concept)
- source_article: KCS 21 50

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- to: `StructuralComponent:kcs_21_50_component_form_01` (concept)
- source_article: KCS 21 50

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- to: `StructuralComponent:kcs_21_50_component_shore_01` (concept)
- source_article: KCS 21 50

## Edge — `targets_component`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `StructuralComponent:kcs_21_50_component_form_01` (concept)
- source_article: KCS 21 50 10

## Edge — `targets_component`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `StructuralComponent:kcs_21_50_component_shore_01` (concept)
- source_article: KCS 21 50 10

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_pass_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_rework_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_pass_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_rework_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_pass_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_rework_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_pass_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_rework_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_pass_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_rework_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_stop_01` (outcome)
- source_article: KCS 21 50

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_50_redo_pour_01` (outcome)
- source_article: KCS 21 50 10

## Edge — `precedes`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- source_article: KCS 21 50

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- to: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- source_article: KCS 21 50

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- to: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- source_article: KCS 21 50

## Edge — `depends_on`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01` (decision)
- source_article: KCS 21 50

## Edge — `precedes`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01` (decision)
- source_article: KCS 21 50

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01` (decision)
- to: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- source_article: KCS 21 50

## Edge — `depends_on`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- source_article: KCS 21 50 10 / KCS 14 20 10

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- to: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- source_article: KCS 21 50 10 / KCS 14 20 10

## Edge — `precedes`
- from: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- to: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- source_article: KCS 21 50 / KCS 14 20

## Edge — `depends_on`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01` (decision)
- source_article: KCS 21 50 / KCS 14 20

## Edge — `subclass_of`
- from: `WorkType:kcs_11_30_worktype_pbd_01` (concept)
- to: `WorkType:kcs_11_30_worktype_softground_01` (concept)
- source_article: KCS 11 30 10

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `Specification:spec_kcs_11_30_dmm_01` (resource)
- source_article: KCS 11 30 20

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `Specification:spec_kcs_11_30_replace_01` (resource)
- source_article: KCS 11 30 15

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `Specification:spec_kcs_11_30_compaction_01` (resource)
- source_article: KCS 11 30 25

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- to: `Specification:spec_kcs_11_30_sand_drain_01` (resource)
- source_article: KCS 11 30 10

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- source_article: KCS 11 30

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- source_article: KCS 11 30

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- source_article: KCS 11 30

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- source_article: KCS 11 30

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_safety_manager_01` (concept)
- to: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- source_article: KCS 11 30

## Edge — `performs`
- from: `SafetyManager:kcs_safety_manager_01` (subject)
- to: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- source_article: KCS 11 30

## Edge — `qualified_as`
- from: `SiteEngineer:kcs_11_30_geo_engineer_01` (subject)
- to: `Qualification:kcs_qual_soil_geo_01` (concept)
- source_article: KCS 11 30

## Edge — `performs`
- from: `SiteEngineer:kcs_11_30_geo_engineer_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_soil_geo_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `Specification:spec_kcs_11_30_main_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `Specification:spec_kcs_11_30_settle_limit_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `Specification:spec_kcs_11_30_stability_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- to: `Specification:spec_kcs_11_30_pbd_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `Specification:spec_kcs_11_30_monitor_freq_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `Specification:spec_kcs_11_30_alarm_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `Specification:spec_kcs_11_30_construction_limit_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- to: `Specification:spec_kcs_11_30_consolidation_judge_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- to: `Specification:spec_kcs_11_30_settle_limit_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- to: `Specification:spec_kcs_11_30_construction_limit_01` (resource)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- to: `Specification:spec_kcs_11_30_alarm_01` (resource)
- source_article: KCS 11 30

## Edge — `targets_work_type`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `WorkType:kcs_11_30_worktype_softground_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_facility`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `Facility:kcs_11_30_facility_embankment_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- to: `WorkType:kcs_11_30_worktype_softground_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_facility`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- to: `Facility:kcs_11_30_facility_embankment_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `WorkType:kcs_11_30_worktype_softground_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_facility`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `Facility:kcs_11_30_facility_embankment_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_work_type`
- from: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- to: `WorkType:kcs_11_30_worktype_softground_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_facility`
- from: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- to: `Facility:kcs_11_30_facility_embankment_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_work_type`
- from: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- to: `WorkType:kcs_11_30_worktype_softground_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- to: `Facility:kcs_11_30_facility_embankment_01` (concept)
- source_article: KCS 11 30

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- to: `StructuralComponent:kcs_11_30_component_pbd_01` (concept)
- source_article: KCS 11 30 10

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- to: `WorkType:kcs_11_30_worktype_pbd_01` (concept)
- source_article: KCS 11 30 10

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_11_30_pass_01` (outcome)
- source_article: KCS 11 30
