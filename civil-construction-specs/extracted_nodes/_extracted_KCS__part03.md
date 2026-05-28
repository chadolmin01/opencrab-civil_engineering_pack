# Extracted graph — KCS__part03.jsonl

_source jsonl: KCS__part03.jsonl_

## Nodes

## Node — WorkType / `WorkType:kcs_21_60_worktype_scaffold_01`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 비계·가시설 공사
  - `scope`: 강관·시스템·달비계·작업발판

## Node — Facility / `Facility:kcs_21_60_facility_scaffold_01`
- space: `concept`
- node_type: `Facility`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 비계 구조물
  - `lifecycle`: 가설(시공 중)

## Node — StructuralComponent / `StructuralComponent:kcs_21_60_component_pipe_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 21 60 10
- properties:
  - `name_ko`: 강관 비계(48.6mm/2.4t)

## Node — StructuralComponent / `StructuralComponent:kcs_21_60_component_platform_01`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 21 60 25
- properties:
  - `name_ko`: 작업발판·발끝막이판

## Node — Specification / `Specification:spec_kcs_21_60_main_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60
- properties:
  - `name_ko`: KCS 21 60 비계 표준시방서
  - `standard_no`: KCS 21 60 00

## Node — Specification / `Specification:spec_kcs_21_60_load_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 05
- properties:
  - `name_ko`: 비계 작업하중·안전율
  - `standard_no`: KCS 21 60 05
  - `work_load_kN_per_m2`: 2.5
  - `material_load_kN_per_m2`: 4.0
  - `pipe_safety_factor_min`: 4.0
  - `wire_safety_factor_min`: 10.0

## Node — Specification / `Specification:spec_kcs_21_60_pipe_assembly_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 10
- properties:
  - `name_ko`: 강관 비계 조립 한계
  - `standard_no`: KCS 21 60 10
  - `post_spacing_band_max_m`: 1.85
  - `post_spacing_joist_max_m`: 1.5
  - `band_height_max_m`: 1.5
  - `first_band_height_max_m`: 2.0
  - `wall_tie_vertical_max_m`: 5
  - `wall_tie_horizontal_max_m`: 5

## Node — Specification / `Specification:spec_kcs_21_60_platform_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 25
- properties:
  - `name_ko`: 작업발판·안전난간 한계
  - `standard_no`: KCS 21 60 25
  - `platform_width_min_cm`: 40
  - `platform_gap_max_cm`: 3
  - `platform_to_wall_max_cm`: 30
  - `toe_board_min_cm`: 10
  - `guardrail_top_cm`: 90~120
  - `guardrail_mid_cm`: 45~60
  - `guardrail_force_kgf`: 100
  - `fall_net_mesh_max_cm`: 10

## Node — Specification / `Specification:spec_kcs_21_60_wind_stop_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 05
- properties:
  - `name_ko`: 풍속 작업 중지 기준
  - `standard_no`: KCS 21 60 05 + 산안기준
  - `assembly_stop_m_per_s`: 10
  - `all_work_stop_m_per_s`: 15
  - `warning_average_m_per_s`: 14
  - `warning_gust_m_per_s`: 20
  - `post_event_inspect_above_m_per_s`: 10

## Node — Specification / `Specification:spec_kcs_21_60_rain_snow_stop_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 05
- properties:
  - `name_ko`: 강우·강설 작업 중지 기준
  - `standard_no`: KCS 21 60 05 + 산안기준
  - `rain_stop_mm_per_h`: 1
  - `rain_daily_stop_mm`: 25
  - `snow_stop_cm_per_h`: 1
  - `snow_accum_stop_cm`: 10
  - `icing_rule`: 결빙·미끄럼 시 즉시 중지

## Node — Specification / `Specification:spec_kcs_21_60_visibility_stop_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 05
- properties:
  - `name_ko`: 야간·시야 작업 한계
  - `standard_no`: KCS 21 60 05 + 산안기준
  - `visibility_stop_m_below`: 100
  - `night_lux_min`: 75
  - `seismic_intensity_stop_min`: 5

## Node — Specification / `Specification:spec_kcs_21_60_inspection_freq_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 05
- properties:
  - `name_ko`: 비계 점검 주기
  - `standard_no`: KCS 21 60 05
  - `daily_before_work`: 매일 작업 시작 전
  - `weekly`: 주 1회 정기 (감리자 입회)
  - `post_wind_threshold_m_per_s`: 10
  - `post_rain_24h_threshold_mm`: 50
  - `post_seismic_threshold`: 진도 4 이상
  - `long_idle_reuse_days_min`: 30

## Node — Specification / `Specification:spec_kcs_21_60_mobile_scaffold_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 20
- properties:
  - `name_ko`: 달비계·이동비계·말비계 한계
  - `standard_no`: KCS 21 60 20·25
  - `mobile_height_base_ratio_max`: 4
  - `mobile_during_move_rule`: 이동·승강 중 사용 금지
  - `ladder_scaffold_max_height_m`: 2

## Node — Specification / `Specification:spec_kcs_21_60_falling_net_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 05
- properties:
  - `name_ko`: 낙하물방지망 설치 기준
  - `standard_no`: KCS 21 60 05
  - `first_height_max_m`: 10
  - `vertical_interval_max_m`: 10
  - `extrusion_min_m`: 2

## Node — Specification / `Specification:spec_kcs_21_60_system_brace_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 21 60 10
- properties:
  - `name_ko`: 벽이음·버팀·가새 한계
  - `standard_no`: KCS 21 60 10
  - `wall_tie_vertical_max_m`: 5
  - `wall_tie_horizontal_max_m`: 5
  - `diagonal_angle_deg`: 45

## Node — StageApprovalDecision / `StageApprovalDecision:decision_kcs_21_60_plan_approval_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 비계·가시설 시공계획 승인
  - `criterion_source`: KCS 21 60 05

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 비계 조립 검측 (간격·벽이음·안전난간)
  - `criterion_source`: KCS 21 60 10·25

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 비계 일상 점검 (매일 작업 전)
  - `criterion_source`: KCS 21 60 05

## Node — SafetyInspectionDecision / `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01`
- space: `decision`
- node_type: `SafetyInspectionDecision`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 강풍·강우·지진 후 임시 점검
  - `criterion_source`: KCS 21 60 05

## Node — WorkPermitDecision / `WorkPermitDecision:decision_kcs_21_60_work_permit_01`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 비계 작업 허가 (풍속·강우·시야)
  - `criterion_source`: KCS 21 60 05 + 산안기준
  - `stop_triggers`: ["풍속 10m/s 이상", "강우 1mm/h 이상", "강설 1cm/h 이상 또는 적설 10cm", "가시거리 100m 이하", "진도 5 이상"]

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_21_60_pass_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 비계 합격·작업 허가
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_21_60_rework_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 비계 재조립·보강
  - `result`: rework

## Node — DecisionOutcome / `DecisionOutcome:outcome_kcs_21_60_stop_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 21 60
- properties:
  - `name_ko`: 비계 작업 중지(풍속·강우·시야·지진)
  - `result`: work_stop

## Edges

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_11_30_pass_01` (outcome)
- source_article: KCS 11 30

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_11_30_pass_01` (outcome)
- source_article: KCS 11 30

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_11_30_pass_01` (outcome)
- source_article: KCS 11 30

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- to: `DecisionOutcome:outcome_kcs_11_30_pass_01` (outcome)
- source_article: KCS 11 30

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_11_30_wait_01` (outcome)
- source_article: KCS 11 30 30

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- to: `DecisionOutcome:outcome_kcs_11_30_stop_01` (outcome)
- source_article: KCS 11 30 30

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_11_30_wait_01` (outcome)
- source_article: KCS 11 30 05

## Edge — `precedes`
- from: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- to: `StageApprovalDecision:decision_kcs_11_30_plan_approval_01` (decision)
- source_article: KCS 11 30

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- source_article: KCS 11 30

## Edge — `depends_on`
- from: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- source_article: KCS 11 30

## Edge — `depends_on`
- from: `SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- source_article: KCS 11 30

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `Specification:spec_kcs_21_60_falling_net_01` (resource)
- source_article: KCS 21 60 05

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `Specification:spec_kcs_21_60_system_brace_01` (resource)
- source_article: KCS 21 60 10

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_chief_supervisor_01` (concept)
- to: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- source_article: KCS 21 60

## Edge — `performs`
- from: `ChiefSupervisor:kcs_chief_supervisor_01` (subject)
- to: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- source_article: KCS 21 60

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_supervisor_01` (concept)
- to: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `performs`
- from: `Supervisor:kcs_supervisor_01` (subject)
- to: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_safety_manager_01` (concept)
- to: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `performs`
- from: `SafetyManager:kcs_safety_manager_01` (subject)
- to: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_safety_manager_01` (concept)
- to: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `performs`
- from: `SafetyManager:kcs_safety_manager_01` (subject)
- to: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `grants_authority_for`
- from: `Qualification:kcs_qual_safety_manager_01` (concept)
- to: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- source_article: KCS 21 60

## Edge — `performs`
- from: `SafetyManager:kcs_safety_manager_01` (subject)
- to: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- to: `Specification:spec_kcs_21_60_main_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- to: `Specification:spec_kcs_21_60_load_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- to: `Specification:spec_kcs_21_60_pipe_assembly_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- to: `Specification:spec_kcs_21_60_mobile_scaffold_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `Specification:spec_kcs_21_60_pipe_assembly_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `Specification:spec_kcs_21_60_platform_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `Specification:spec_kcs_21_60_inspection_freq_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `Specification:spec_kcs_21_60_inspection_freq_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `Specification:spec_kcs_21_60_inspection_freq_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `Specification:spec_kcs_21_60_wind_stop_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `Specification:spec_kcs_21_60_rain_snow_stop_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `Specification:spec_kcs_21_60_wind_stop_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `Specification:spec_kcs_21_60_rain_snow_stop_01` (resource)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `Specification:spec_kcs_21_60_visibility_stop_01` (resource)
- source_article: KCS 21 60

## Edge — `targets_work_type`
- from: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- to: `WorkType:kcs_21_60_worktype_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_facility`
- from: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- to: `Facility:kcs_21_60_facility_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `WorkType:kcs_21_60_worktype_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_facility`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `Facility:kcs_21_60_facility_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_work_type`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `WorkType:kcs_21_60_worktype_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `Facility:kcs_21_60_facility_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_work_type`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `WorkType:kcs_21_60_worktype_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `Facility:kcs_21_60_facility_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_work_type`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `WorkType:kcs_21_60_worktype_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_facility`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `Facility:kcs_21_60_facility_scaffold_01` (concept)
- source_article: KCS 21 60

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `StructuralComponent:kcs_21_60_component_pipe_01` (concept)
- source_article: KCS 21 60 10

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `StructuralComponent:kcs_21_60_component_platform_01` (concept)
- source_article: KCS 21 60 25

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_pass_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_rework_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_pass_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_rework_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_pass_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_rework_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_pass_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_rework_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_pass_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_rework_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_stop_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_stop_01` (outcome)
- source_article: KCS 21 60

## Edge — `yields`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `DecisionOutcome:outcome_kcs_21_60_stop_01` (outcome)
- source_article: KCS 21 60

## Edge — `precedes`
- from: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `StageApprovalDecision:decision_kcs_21_60_plan_approval_01` (decision)
- source_article: KCS 21 60

## Edge — `precedes`
- from: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- to: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `depends_on`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `precedes`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- source_article: KCS 21 60

## Edge — `depends_on`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `precedes`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- source_article: KCS 21 60

## Edge — `depends_on`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- source_article: KCS 21 60

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `Checklist:checklist_kcs_pre_pour_01` (resource)
- source_article: KCS 14 20 10

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_20_pour_permit_01` (decision)
- to: `WorkPermit:permit_kcs_pour_01` (resource)
- source_article: KCS 14 20 10

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01` (decision)
- to: `ConstructionLog:log_kcs_construction_01` (resource)
- source_article: KCS 14 20 10

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01` (decision)
- to: `TestReport:test_kcs_strength_report_01` (resource)
- source_article: KCS 14 20 10

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `Checklist:checklist_kcs_form_strip_01` (resource)
- source_article: KCS 21 50 10

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_21_50_strip_approval_01` (decision)
- to: `SupervisionLog:log_kcs_supervision_01` (resource)
- source_article: KCS 21 50 10

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01` (decision)
- to: `SafetyInspectionReport:safety_kcs_formwork_report_01` (resource)
- source_article: KCS 21 50 15

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `Checklist:checklist_kcs_weld_pre_01` (resource)
- source_article: KCS 14 31 20

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_14_31_weld_permit_01` (decision)
- to: `WorkPermit:permit_kcs_weld_01` (resource)
- source_article: KCS 14 31 20

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_ut_01` (decision)
- to: `TestReport:test_kcs_ut_report_01` (resource)
- source_article: KCS 14 31 20

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01` (decision)
- to: `TestReport:test_kcs_torque_report_01` (resource)
- source_article: KCS 14 31 25

## Edge — `based_on`
- from: `ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01` (decision)
- to: `TestReport:test_kcs_monitoring_report_01` (resource)
- source_article: KCS 11 30 30

## Edge — `based_on`
- from: `StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01` (decision)
- to: `TestReport:test_kcs_monitoring_report_01` (resource)
- source_article: KCS 11 30 30

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `Checklist:checklist_kcs_scaffold_daily_01` (resource)
- source_article: KCS 21 60 05

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01` (decision)
- to: `SafetyInspectionReport:safety_kcs_scaffold_report_01` (resource)
- source_article: KCS 21 60 05

## Edge — `based_on`
- from: `SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01` (decision)
- to: `SafetyInspectionReport:safety_kcs_scaffold_report_01` (resource)
- source_article: KCS 21 60 05

## Edge — `based_on`
- from: `WorkPermitDecision:decision_kcs_21_60_work_permit_01` (decision)
- to: `WorkPermit:permit_kcs_scaffold_01` (resource)
- source_article: KCS 21 60 05
