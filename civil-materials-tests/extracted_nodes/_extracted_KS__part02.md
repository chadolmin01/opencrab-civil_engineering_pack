# Extracted graph — KS__part02.jsonl

_source jsonl: KS__part02.jsonl_

## Nodes

## Node — Qualification / `Qualification:ks_d_3503_grade_ss410_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KS D 3503
- properties:
  - `name_ko`: SS410 등급
  - `grade`: SS410
  - `fy_min_mpa`: 410
  - `fu_range_mpa`: 540 ~ 680
  - `standard_no`: KS D 3503

## Node — Qualification / `Qualification:ks_d_3503_grade_ss450_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KS D 3503
- properties:
  - `name_ko`: SS450 등급
  - `grade`: SS450
  - `fy_min_mpa`: 450
  - `fu_range_mpa`: 590 ~ 740
  - `standard_no`: KS D 3503

## Node — Qualification / `Qualification:ks_d_3503_grade_ss550_01`
- space: `concept`
- node_type: `Qualification`
- source_article: KS D 3503
- properties:
  - `name_ko`: SS550 등급
  - `grade`: SS550
  - `fy_min_mpa`: 550
  - `fu_range_mpa`: 690 ~ 830
  - `standard_no`: KS D 3503

## Node — Specification / `Specification:ks_d_3503_yield_thickness_ss275_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS D 3503
- properties:
  - `name_ko`: SS275 두께별 항복강도
  - `standard_no`: KS D 3503
  - `fy_t_le_16mm`: 275
  - `fy_t_16_to_40mm`: 265
  - `fy_t_40_to_100mm`: 245
  - `fy_t_over_100mm`: 235

## Node — Specification / `Specification:ks_d_3503_elongation_ss275_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS D 3503
- properties:
  - `name_ko`: SS275 연신율 (KS B 0801 5호 기준)
  - `standard_no`: KS D 3503
  - `elongation_t_le_5mm_pct`: 21
  - `elongation_t_5_to_16mm_pct`: 23
  - `elongation_t_over_16mm_pct`: 24

## Node — Specification / `Specification:ks_d_3503_chem_ss275_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS D 3503
- properties:
  - `name_ko`: SS275 화학 성분
  - `standard_no`: KS D 3503
  - `C_max_pct_t_le_50mm`: 0.24
  - `P_max_pct`: 0.05
  - `S_max_pct`: 0.05

## Node — Specification / `Specification:ks_d_3503_bend_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS D 3503
- properties:
  - `name_ko`: 굽힘 시험 (SS235·SS275)
  - `standard_no`: KS D 3503
  - `angle_deg`: 180
  - `inner_diameter`: 1.5t

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:ks_d_3503_decision_grade_01`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: KS D 3503
- properties:
  - `name_ko`: 강재 종류·강도 검수
  - `criterion_source`: KS D 3503

## Node — DecisionOutcome / `DecisionOutcome:ks_d_3503_outcome_pass_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KS D 3503
- properties:
  - `name_ko`: 강재 적합
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:ks_d_3503_outcome_fail_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KS D 3503
- properties:
  - `name_ko`: 강재 부적합 — 반품
  - `result`: fail

## Node — Specification / `Specification:ks_b_0801_main_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0801
- properties:
  - `name_ko`: KS B 0801 금속재료 인장 시험편
  - `standard_no`: KS B 0801

## Node — Specification / `Specification:ks_b_0801_prop_gauge_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0801
- properties:
  - `name_ko`: 비례 시험편 게이지 길이
  - `standard_no`: KS B 0801
  - `Lo_formula`: 5.65 √Ao
  - `Lo_round_section`: 5d
  - `Lo_long_formula`: 11.3 √Ao
  - `Lo_long_round`: 10d

## Node — Specification / `Specification:ks_b_0801_round_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0801
- properties:
  - `name_ko`: 원형 시험편 표준 치수
  - `standard_no`: KS B 0801
  - `d_list_mm`: [14, 12.5, 10, 8, 6, 5, 4, 3, 2.5]
  - `Lc_range`: Lo + d ~ Lo + 2d
  - `grip_D_min_ratio`: 1.4 × d
  - `shoulder_R_min_ratio`: >= d

## Node — Specification / `Specification:ks_b_0801_plate_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0801
- properties:
  - `name_ko`: 판상 시험편 (1A·1B호)
  - `standard_no`: KS B 0801
  - `type_1A_b_mm`: 25
  - `type_1A_Lo_mm`: 50
  - `type_1B_b_mm`: 12.5
  - `type_1B_Lo_mm`: 25
  - `Lc_formula`: Lo + 2b
  - `shoulder_R_min_mm`: 20

## Node — Specification / `Specification:ks_b_0801_14_rebar_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0801
- properties:
  - `name_ko`: 14호 시험편 (이형철근)
  - `standard_no`: KS B 0801
  - `Lo`: 호칭 지름 5배 (5d)
  - `Lc_min`: 5.5d
  - `area_used`: 호칭 단면적

## Node — Specification / `Specification:ks_b_0801_finish_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0801
- properties:
  - `name_ko`: 표면 가공·정밀도
  - `standard_no`: KS B 0801
  - `Ra_max_um`: 3.2
  - `parallelism_max_mm`: 0.05
  - `no_notch`: True

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:ks_b_0801_decision_specimen_01`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: KS B 0801
- properties:
  - `name_ko`: 인장 시험편 적합성 확인
  - `criterion_source`: KS B 0801

## Node — DecisionOutcome / `DecisionOutcome:ks_b_0801_outcome_pass_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KS B 0801
- properties:
  - `name_ko`: 시험편 적합
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:ks_b_0801_outcome_fail_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KS B 0801
- properties:
  - `name_ko`: 시험편 부적합 — 재가공
  - `result`: fail
  - `action`: 재가공

## Node — Specification / `Specification:ks_b_0802_main_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0802
- properties:
  - `name_ko`: KS B 0802 금속재료 인장 시험 방법
  - `standard_no`: KS B 0802

## Node — Specification / `Specification:ks_b_0802_temperature_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0802
- properties:
  - `name_ko`: 시험 온도
  - `standard_no`: KS B 0802
  - `standard_range_c`: 10 ~ 35
  - `precision_range_c`: 23 ± 5

## Node — Specification / `Specification:ks_b_0802_rate_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0802
- properties:
  - `name_ko`: 변형/응력 속도
  - `standard_no`: KS B 0802
  - `elastic_stress_rate_mpa_per_s`: 6 ~ 60
  - `elastic_strain_rate_per_s`: 0.00025 ~ 0.0025
  - `yield_strain_rate_max_per_s`: 0.0025
  - `post_yield_strain_rate_max_per_s`: 0.008

## Node — Specification / `Specification:ks_b_0802_ys_method_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0802
- properties:
  - `name_ko`: 항복강도 결정 방법
  - `standard_no`: KS B 0802
  - `primary`: 상부/하부 항복점 ReH/ReL
  - `offset_method`: Rp0.2 (영구 변형 0.2 %)
  - `alt_total_extension`: Rt0.5

## Node — Specification / `Specification:ks_b_0802_ts_method_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0802
- properties:
  - `name_ko`: 인장강도 결정
  - `standard_no`: KS B 0802
  - `formula`: Rm = F_max / Ao
  - `unit`: MPa
  - `rounding`: 1 MPa

## Node — Specification / `Specification:ks_b_0802_el_ra_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0802
- properties:
  - `name_ko`: 연신율 및 단면수축률
  - `standard_no`: KS B 0802
  - `EL_formula`: (Lu - Lo) / Lo × 100
  - `RA_formula`: (Ao - Au) / Ao × 100
  - `break_position_rule`: 표점 중앙에서 1/3 이내
  - `outside_gauge_rule`: 표점 외 파단 시 강도값만 유효

## Node — Specification / `Specification:ks_b_0802_precision_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0802
- properties:
  - `name_ko`: 측정 정밀도
  - `standard_no`: KS B 0802
  - `diameter_mm`: 0.01
  - `plate_thickness_mm`: 0.02
  - `gauge_length_pct`: 0.5
  - `load_max_pct`: 0.5
  - `machine_class_recommend`: 등급 1

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:ks_b_0802_decision_test_01`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: KS B 0802
- properties:
  - `name_ko`: 인장 시험 적합 판정
  - `criterion_source`: KS B 0802

## Node — DecisionOutcome / `DecisionOutcome:ks_b_0802_outcome_valid_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KS B 0802
- properties:
  - `name_ko`: 시험 유효
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:ks_b_0802_outcome_invalid_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KS B 0802
- properties:
  - `name_ko`: 시험 무효
  - `result`: fail
  - `action`: 재시험 (그립부 파단 또는 표점 외 파단)

## Node — Specification / `Specification:ks_b_0896_main_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0896
- properties:
  - `name_ko`: KS B 0896 강용접부 초음파 탐상
  - `standard_no`: KS B 0896
  - `scope_thickness_mm`: 6 ~ 200

## Node — Specification / `Specification:ks_b_0896_probe_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0896
- properties:
  - `name_ko`: 탐촉자 사양
  - `standard_no`: KS B 0896
  - `angle_deg_list`: [35, 45, 60, 70]
  - `frequency_mhz_list`: [2, 5]
  - `transducer_size_mm_list`: ["10×10", "14×14"]

## Node — Specification / `Specification:ks_b_0896_stb_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0896
- properties:
  - `name_ko`: 표준 시험편
  - `standard_no`: KS B 0896
  - `STB_A1_ref`: KS B 0831 — DAC 작성
  - `STB_A2_ref`: 굴절각·입사점
  - `RB_4_ref`: DAC 보조

## Node — Specification / `Specification:ks_b_0896_dac_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0896
- properties:
  - `name_ko`: 감도 조정 (DAC L/M/H 선)
  - `standard_no`: KS B 0896
  - `L_line_db`: 0
  - `M_line_db`: 6
  - `H_line_db`: 12

## Node — Specification / `Specification:ks_b_0896_class_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0896
- properties:
  - `name_ko`: 결함 등급 분류 한계 (두께 18 mm 이하 예시)
  - `standard_no`: KS B 0896
  - `class_1`: 영역 II, 길이 ≤ t/3
  - `class_2`: 영역 II, 길이 ≤ t/2 또는 영역 III, 길이 ≤ t/3
  - `class_3`: 영역 II, 길이 ≤ 2t/3 또는 영역 III, 길이 ≤ t/2 또는 영역 IV, 길이 ≤ t/3
  - `class_4`: 그 외 (불합격)

## Node — Specification / `Specification:ks_b_0896_accept_01`
- space: `resource`
- node_type: `Specification`
- source_article: KS B 0896
- properties:
  - `name_ko`: 합격 판정 (1차 응력 부재)
  - `standard_no`: KS B 0896
  - `pass`: 1류·2류
  - `repair`: 3류 보수 후 재검
  - `reject`: 4류 불합격

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:ks_b_0896_decision_ut_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KS B 0896
- properties:
  - `name_ko`: 강용접부 UT 검사 판정
  - `criterion_source`: KS B 0896
  - `decision_type`: 비파괴 검사 결과 등급 판정

## Node — DecisionOutcome / `DecisionOutcome:ks_b_0896_outcome_pass_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KS B 0896
- properties:
  - `name_ko`: 용접부 합격 (1·2류)
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:ks_b_0896_outcome_repair_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KS B 0896
- properties:
  - `name_ko`: 용접부 보수 후 재검 (3류)
  - `result`: rework

## Node — DecisionOutcome / `DecisionOutcome:ks_b_0896_outcome_reject_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KS B 0896
- properties:
  - `name_ko`: 용접부 불합격 (4류)
  - `result`: fail
  - `action`: 용접부 제거·재시공

## Node — SiteEngineer / `SiteEngineer:ks_b_0896_ut_inspector_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KS B 0896
- properties:
  - `name_ko`: 비파괴검사 기술자 (UT 레벨 2 이상)
  - `duties`: ["KS B 0896 UT 수행", "결함 등급 판정", "기록 작성"]

## Edges

## Edge — `grants_authority_for`
- from: `Qualification:ks_qual_supervisor_01` (concept)
- to: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- source_article: KS D 3503

## Edge — `performs`
- from: `Supervisor:ks_supervisor_01` (subject)
- to: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- source_article: KS D 3503

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Specification:ks_d_3503_yield_thickness_ss275_01` (resource)
- source_article: KS D 3503

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Specification:ks_d_3503_elongation_ss275_01` (resource)
- source_article: KS D 3503

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Specification:ks_d_3503_chem_ss275_01` (resource)
- source_article: KS D 3503

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Specification:ks_d_3503_bend_01` (resource)
- source_article: KS D 3503

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Specification:ks_d_3503_main_01` (resource)
- source_article: KS D 3503

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Qualification:ks_d_3503_grade_ss235_01` (concept)
- source_article: KS D 3503

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Qualification:ks_d_3503_grade_ss275_01` (concept)
- source_article: KS D 3503

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Qualification:ks_d_3503_grade_ss315_01` (concept)
- source_article: KS D 3503

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Qualification:ks_d_3503_grade_ss410_01` (concept)
- source_article: KS D 3503

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Qualification:ks_d_3503_grade_ss450_01` (concept)
- source_article: KS D 3503

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `Qualification:ks_d_3503_grade_ss550_01` (concept)
- source_article: KS D 3503

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `StructuralComponent:ks_component_steel_01` (concept)
- source_article: KS D 3503

## Edge — `targets_work_type`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `WorkType:ks_worktype_steel_struct_01` (concept)
- source_article: KS D 3503

## Edge — `yields`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `DecisionOutcome:ks_d_3503_outcome_pass_01` (outcome)
- source_article: KS D 3503

## Edge — `yields`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `DecisionOutcome:ks_d_3503_outcome_fail_01` (outcome)
- source_article: KS D 3503

## Edge — `grants_authority_for`
- from: `Qualification:ks_qual_supervisor_01` (concept)
- to: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- source_article: KS B 0801

## Edge — `performs`
- from: `Supervisor:ks_supervisor_01` (subject)
- to: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- source_article: KS B 0801

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `Specification:ks_b_0801_prop_gauge_01` (resource)
- source_article: KS B 0801

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `Specification:ks_b_0801_round_01` (resource)
- source_article: KS B 0801

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `Specification:ks_b_0801_plate_01` (resource)
- source_article: KS B 0801

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `Specification:ks_b_0801_14_rebar_01` (resource)
- source_article: KS B 0801

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `Specification:ks_b_0801_finish_01` (resource)
- source_article: KS B 0801

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `StructuralComponent:ks_component_steel_01` (concept)
- source_article: KS B 0801

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `StructuralComponent:ks_component_rebar_01` (concept)
- source_article: KS B 0801

## Edge — `targets_work_type`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `WorkType:ks_worktype_steel_struct_01` (concept)
- source_article: KS B 0801

## Edge — `yields`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `DecisionOutcome:ks_b_0801_outcome_pass_01` (outcome)
- source_article: KS B 0801

## Edge — `yields`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `DecisionOutcome:ks_b_0801_outcome_fail_01` (outcome)
- source_article: KS B 0801

## Edge — `grants_authority_for`
- from: `Qualification:ks_qual_supervisor_01` (concept)
- to: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- source_article: KS B 0802

## Edge — `performs`
- from: `Supervisor:ks_supervisor_01` (subject)
- to: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- source_article: KS B 0802

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `Specification:ks_b_0802_temperature_01` (resource)
- source_article: KS B 0802

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `Specification:ks_b_0802_rate_01` (resource)
- source_article: KS B 0802

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `Specification:ks_b_0802_ys_method_01` (resource)
- source_article: KS B 0802

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `Specification:ks_b_0802_ts_method_01` (resource)
- source_article: KS B 0802

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `Specification:ks_b_0802_el_ra_01` (resource)
- source_article: KS B 0802

## Edge — `based_on`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `Specification:ks_b_0802_precision_01` (resource)
- source_article: KS B 0802

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `StructuralComponent:ks_component_steel_01` (concept)
- source_article: KS B 0802

## Edge — `targets_component`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `StructuralComponent:ks_component_rebar_01` (concept)
- source_article: KS B 0802

## Edge — `targets_work_type`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `WorkType:ks_worktype_steel_struct_01` (concept)
- source_article: KS B 0802

## Edge — `yields`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `DecisionOutcome:ks_b_0802_outcome_valid_01` (outcome)
- source_article: KS B 0802

## Edge — `yields`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `DecisionOutcome:ks_b_0802_outcome_invalid_01` (outcome)
- source_article: KS B 0802

## Edge — `precedes`
- from: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- to: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- source_article: KS B 0801 / KS B 0802

## Edge — `depends_on`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `MaterialReceiptDecision:ks_b_0801_decision_specimen_01` (decision)
- source_article: KS B 0801 / KS B 0802

## Edge — `precedes`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `MaterialReceiptDecision:ks_d_3504_decision_grade_01` (decision)
- source_article: KS B 0802 / KS D 3504

## Edge — `depends_on`
- from: `MaterialReceiptDecision:ks_d_3504_decision_grade_01` (decision)
- to: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- source_article: KS B 0802 / KS D 3504

## Edge — `precedes`
- from: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- to: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- source_article: KS B 0802 / KS D 3503

## Edge — `depends_on`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `MaterialReceiptDecision:ks_b_0802_decision_test_01` (decision)
- source_article: KS B 0802 / KS D 3503

## Edge — `grants_authority_for`
- from: `Qualification:ks_qual_ndt_ut_level2_01` (concept)
- to: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- source_article: KS B 0896

## Edge — `qualified_as`
- from: `SiteEngineer:ks_b_0896_ut_inspector_01` (subject)
- to: `Qualification:ks_qual_ndt_ut_level2_01` (concept)
- source_article: KS B 0896

## Edge — `performs`
- from: `SiteEngineer:ks_b_0896_ut_inspector_01` (subject)
- to: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- source_article: KS B 0896

## Edge — `based_on`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `Specification:ks_b_0896_probe_01` (resource)
- source_article: KS B 0896

## Edge — `based_on`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `Specification:ks_b_0896_stb_01` (resource)
- source_article: KS B 0896

## Edge — `based_on`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `Specification:ks_b_0896_dac_01` (resource)
- source_article: KS B 0896

## Edge — `based_on`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `Specification:ks_b_0896_class_01` (resource)
- source_article: KS B 0896

## Edge — `based_on`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `Specification:ks_b_0896_accept_01` (resource)
- source_article: KS B 0896

## Edge — `based_on`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `Specification:ks_b_0896_main_01` (resource)
- source_article: KS B 0896

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `StructuralComponent:ks_component_weld_01` (concept)
- source_article: KS B 0896

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `WorkType:ks_worktype_weld_ut_01` (concept)
- source_article: KS B 0896

## Edge — `yields`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `DecisionOutcome:ks_b_0896_outcome_pass_01` (outcome)
- source_article: KS B 0896

## Edge — `yields`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `DecisionOutcome:ks_b_0896_outcome_repair_01` (outcome)
- source_article: KS B 0896

## Edge — `yields`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `DecisionOutcome:ks_b_0896_outcome_reject_01` (outcome)
- source_article: KS B 0896

## Edge — `precedes`
- from: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- to: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- source_article: KS D 3503 / KS B 0896

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:ks_b_0896_decision_ut_01` (decision)
- to: `MaterialReceiptDecision:ks_d_3503_decision_grade_01` (decision)
- source_article: KS D 3503 / KS B 0896
