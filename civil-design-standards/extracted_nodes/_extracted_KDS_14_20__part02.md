# Extracted graph — KDS_14_20__part02.jsonl

_source jsonl: KDS_14_20__part02.jsonl_

## Nodes

## Node — Specification / `Specification:kds14_20_72_min_vert_rebar_other`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 72 §4.5.2
- properties:
  - `name`: 벽체 수직철근비 — 기타
  - `key_value`: ρ ≥ 0.0015 (D16 초과 또는 fy<400MPa)
  - `min_ratio`: 0.0015

## Node — Specification / `Specification:kds14_20_72_min_horiz_rebar`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 72 §4.5.2
- properties:
  - `name`: 벽체 수평철근비
  - `key_value`: 이형철근 ρ ≥ 0.0020 (fy ≥ 400 MPa)
  - `min_ratio`: 0.002

## Node — Specification / `Specification:kds14_20_72_rebar_spacing`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 72 §4.5.2
- properties:
  - `name`: 벽체 철근 간격 — 수직·수평
  - `key_value`: 간격 ≤ 벽두께의 3배 또한 ≤ 450 mm
  - `max_spacing_mm`: 450
  - `max_factor`: 3

## Node — Specification / `Specification:kds14_20_74_retaining_min_cover`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 74 §4
- properties:
  - `name`: 옹벽 최소 피복두께
  - `key_value`: 흙에 접하는 부재 ≥ 75 mm
  - `min_cover_mm`: 75

## Node — Specification / `Specification:kds14_20_74_retaining_safety`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 74 §4
- properties:
  - `name`: 옹벽 안정 안전율
  - `key_value`: 활동 ≥ 1.5, 전도 ≥ 2.0, 지지력 ≥ 3.0
  - `sliding`: 1.5
  - `overturning`: 2.0
  - `bearing`: 3.0

## Node — Specification / `Specification:kds14_20_74_tank_crack_width`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 74 §4
- properties:
  - `name`: 수조 균열폭 제한
  - `key_value`: 수밀 구조 균열폭 ≤ 0.2 mm
  - `max_crack_mm`: 0.2

## Node — Specification / `Specification:kds14_20_74_culvert_min_cover`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 74 §4
- properties:
  - `name`: 암거 최소 토피
  - `key_value`: ≥ 600 mm

## Node — Specification / `Specification:kds14_20_80_min_fck`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.1.4
- properties:
  - `name`: 특수모멘트골조 콘크리트 fck
  - `key_value`: fck ≥ 21 MPa, 경량콘크리트 ≤ 35 MPa
  - `fck_min_mpa`: 21
  - `lightweight_max_mpa`: 35

## Node — Specification / `Specification:kds14_20_80_rebar_fy`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.1.5
- properties:
  - `name`: 내진 주철근 항복강도
  - `key_value`: fy ≤ 600 MPa (주철근), 전단철근 선부재 ≤ 500 MPa, 벽체 ≤ 600 MPa
  - `fy_main_max_mpa`: 600
  - `fy_shear_member_max_mpa`: 500
  - `fy_shear_wall_max_mpa`: 600

## Node — Specification / `Specification:kds14_20_80_rebar_overstrength`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.1.5
- properties:
  - `name`: 주철근 실제 항복 초과 한도
  - `key_value`: 실제 항복강도가 공칭의 120 MPa 이상 초과 금지, 인장/항복비 ≥ 1.25
  - `yield_overshoot_mpa`: 120
  - `min_tensile_to_yield_ratio`: 1.25

## Node — Specification / `Specification:kds14_20_80_smf_beam_width`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.4.1
- properties:
  - `name`: 특수모멘트골조 보 폭
  - `key_value`: 폭 ≥ 250 mm, 폭/깊이 ≥ 0.3, 순경간 ≥ 4d
  - `min_width_mm`: 250
  - `min_width_depth_ratio`: 0.3
  - `min_clear_span_factor`: 4

## Node — Specification / `Specification:kds14_20_80_smf_axial_min_dim`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.5.1
- properties:
  - `name`: 특수모멘트골조 기둥 최소 치수
  - `key_value`: 최소 단면치수 ≥ 300 mm, 짧은변/긴변 ≥ 0.4
  - `min_dim_mm`: 300
  - `min_aspect_ratio`: 0.4

## Node — Specification / `Specification:kds14_20_80_smf_rebar_ratio`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.4.2
- properties:
  - `name`: 특수모멘트골조 휨철근비
  - `key_value`: ρ ≤ 0.025, ρ ≥ 1.4·bw·d/fy
  - `max_ratio`: 0.025

## Node — Specification / `Specification:kds14_20_80_smf_hoop_spacing`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.4.3
- properties:
  - `name`: 특수모멘트골조 후프철근 간격
  - `key_value`: ≤ d/4, 8db(축), 24db(후프), 300 mm 중 최소
  - `max_factor_d`: d/4
  - `max_factor_axial_db`: 8
  - `max_factor_hoop_db`: 24
  - `max_mm`: 300

## Node — Specification / `Specification:kds14_20_80_smf_lo_length`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.5.4
- properties:
  - `name`: 특수모멘트골조 기둥 lo 길이
  - `key_value`: lo ≥ max(순경간/6, 최대치수, 450 mm)
  - `min_mm`: 450
  - `min_factor_clear_span`: 1/6

## Node — Specification / `Specification:kds14_20_80_imf_beam_hoop`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.3.4
- properties:
  - `name`: 중간모멘트골조 보 후프
  - `key_value`: 양단 2d 구간 후프, 첫 후프 50 mm 이내, 간격 ≤ d/4·8db·24db·300mm 최소
  - `min_first_distance_mm`: 50
  - `max_mm`: 300

## Node — Specification / `Specification:kds14_20_80_special_wall_min`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 80 §4.7
- properties:
  - `name`: 특수구조벽 최소 두께·철근
  - `key_value`: 벽체 두께 ≥ 200 mm 일반, ρv·ρh ≥ 0.0025
  - `min_thickness_mm`: 200
  - `min_ratio`: 0.0025

## Node — Specification / `Specification:kds14_20_90_load_factor_reduction`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 90 §4.2.5(2)
- properties:
  - `name`: 안전성 평가 — 하중계수 감소
  - `key_value`: 정밀 현장조사 시 D·L 하중계수 5% 감소 가능
  - `reduction_pct`: 5

## Node — Specification / `Specification:kds14_20_90_phi_eval_tension`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 90 §4.2.4
- properties:
  - `name`: 평가 강도감소계수 — 인장지배
  - `key_value`: φ ≤ 1.0
  - `phi`: 1.0

## Node — Specification / `Specification:kds14_20_90_phi_eval_compress_spiral`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 90 §4.2.4
- properties:
  - `name`: 평가 강도감소계수 — 나선철근 압축지배
  - `key_value`: φ ≤ 0.85
  - `phi`: 0.85

## Node — Specification / `Specification:kds14_20_90_phi_eval_shear`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 90 §4.2.4
- properties:
  - `name`: 평가 강도감소계수 — 전단·비틀림
  - `key_value`: φ ≤ 0.80
  - `phi`: 0.8

## Node — Specification / `Specification:kds14_20_90_load_test_age`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 90 §4.4
- properties:
  - `name`: 재하시험 가능 재령
  - `key_value`: 설계강도 도달 후 시험 (일반적으로 재령 56일 이상 권장)
  - `min_age_days`: 56

## Node — Specification / `Specification:kds14_20_90_core_compression`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 90 §4.1(3)
- properties:
  - `name`: 콘크리트 코어 압축강도 시험
  - `key_value`: KS F 2422에 따른 코어 채취·시험으로 평가입력값 산정
  - `test_standard`: KS F 2422

## Node — Specification / `Specification:kds14_20_90_eval_eq`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 90 §부록
- properties:
  - `name`: 평가식 — 내하율
  - `key_value`: F = (φA·Rn − γA·D) / (γA·(L+I))

## Node — TestReport / `TestReport:kds14_20_90_core_compression`
- space: `resource`
- node_type: `TestReport`
- source_article: KDS 14 20 90 §4.1(3)
- properties:
  - `name`: 콘크리트 코어 압축강도 시험성적서
  - `test_standard`: KS F 2422
  - `scope`: 기존 콘크리트구조물 평가입력값 산정

## Edges

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- to: `Specification:kds14_20_01_design_method` (resource)
- source_article: KDS 14 20 01 §4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- to: `Specification:kds14_20_01_min_structural_fck` (resource)
- source_article: KDS 14 20 01 §4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- to: `Specification:kds14_20_01_min_lightweight_fck` (resource)
- source_article: KDS 14 20 01 §4

## Edge — `based_on`
- from: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- to: `Specification:kds14_20_01_design_method` (resource)
- source_article: KDS 14 20 10 §4.2.4

## Edge — `based_on`
- from: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- to: `Specification:kds14_20_01_min_structural_fck` (resource)
- source_article: KDS 14 20 10 §4.2.4

## Edge — `based_on`
- from: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- to: `Specification:kds14_20_01_min_lightweight_fck` (resource)
- source_article: KDS 14 20 10 §4.2.4

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- to: `Specification:kds14_20_01_design_method` (resource)
- source_article: KDS 14 20 50 §4.2

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- to: `Specification:kds14_20_01_min_structural_fck` (resource)
- source_article: KDS 14 20 50 §4.2

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- to: `Specification:kds14_20_01_min_lightweight_fck` (resource)
- source_article: KDS 14 20 50 §4.2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_cover_check` (decision)
- to: `Specification:kds14_20_01_design_method` (resource)
- source_article: KDS 14 20 50 §4.3

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_cover_check` (decision)
- to: `Specification:kds14_20_01_min_structural_fck` (resource)
- source_article: KDS 14 20 50 §4.3

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_cover_check` (decision)
- to: `Specification:kds14_20_01_min_lightweight_fck` (resource)
- source_article: KDS 14 20 50 §4.3

## Edge — `based_on`
- from: `PrecisionDiagnosisDecision:kds14_20_existing_safety_eval` (decision)
- to: `Specification:kds14_20_01_design_method` (resource)
- source_article: KDS 14 20 90 §4

## Edge — `based_on`
- from: `PrecisionDiagnosisDecision:kds14_20_existing_safety_eval` (decision)
- to: `Specification:kds14_20_01_min_structural_fck` (resource)
- source_article: KDS 14 20 90 §4

## Edge — `based_on`
- from: `PrecisionDiagnosisDecision:kds14_20_existing_safety_eval` (decision)
- to: `Specification:kds14_20_01_min_lightweight_fck` (resource)
- source_article: KDS 14 20 90 §4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_seismic_detail` (decision)
- to: `Specification:kds14_20_01_design_method` (resource)
- source_article: KDS 14 20 80 §4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_seismic_detail` (decision)
- to: `Specification:kds14_20_01_min_structural_fck` (resource)
- source_article: KDS 14 20 80 §4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_seismic_detail` (decision)
- to: `Specification:kds14_20_01_min_lightweight_fck` (resource)
- source_article: KDS 14 20 80 §4

## Edge — `performs`
- from: `ChiefSupervisor:kds14_20_chief_structural` (subject)
- to: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- source_article: KDS 14 20 01 §4

## Edge — `performs`
- from: `ChiefSupervisor:kds14_20_chief_structural` (subject)
- to: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- source_article: KDS 14 20 10 §4.2.4

## Edge — `performs`
- from: `ChiefSupervisor:kds14_20_chief_structural` (subject)
- to: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- source_article: KDS 14 20 50 §4.2

## Edge — `performs`
- from: `ChiefSupervisor:kds14_20_chief_structural` (subject)
- to: `ConstructionInspectionDecision:kds14_20_cover_check` (decision)
- source_article: KDS 14 20 50 §4.3

## Edge — `performs`
- from: `ChiefSupervisor:kds14_20_chief_structural` (subject)
- to: `PrecisionDiagnosisDecision:kds14_20_existing_safety_eval` (decision)
- source_article: KDS 14 20 90 §4

## Edge — `performs`
- from: `ChiefSupervisor:kds14_20_chief_structural` (subject)
- to: `ConstructionInspectionDecision:kds14_20_seismic_detail` (decision)
- source_article: KDS 14 20 80 §4

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- to: `StructuralComponent:kds14_20_beam` (concept)
- source_article: KDS 14 20 01 §4

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- to: `WorkType:kds14_20_rc_design` (concept)
- source_article: KDS 14 20 01 §4

## Edge — `yields`
- from: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- to: `DecisionOutcome:kds14_20_pass` (outcome)
- source_article: KDS 14 20 01 §4

## Edge — `targets_component`
- from: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- to: `StructuralComponent:kds14_20_beam` (concept)
- source_article: KDS 14 20 10 §4.2.4

## Edge — `targets_work_type`
- from: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- to: `WorkType:kds14_20_rc_design` (concept)
- source_article: KDS 14 20 10 §4.2.4

## Edge — `yields`
- from: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- to: `DecisionOutcome:kds14_20_pass` (outcome)
- source_article: KDS 14 20 10 §4.2.4

## Edge — `targets_component`
- from: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- to: `StructuralComponent:kds14_20_beam` (concept)
- source_article: KDS 14 20 50 §4.2

## Edge — `targets_work_type`
- from: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- to: `WorkType:kds14_20_rc_design` (concept)
- source_article: KDS 14 20 50 §4.2

## Edge — `yields`
- from: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- to: `DecisionOutcome:kds14_20_pass` (outcome)
- source_article: KDS 14 20 50 §4.2

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:kds14_20_cover_check` (decision)
- to: `StructuralComponent:kds14_20_beam` (concept)
- source_article: KDS 14 20 50 §4.3

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:kds14_20_cover_check` (decision)
- to: `WorkType:kds14_20_rc_design` (concept)
- source_article: KDS 14 20 50 §4.3

## Edge — `yields`
- from: `ConstructionInspectionDecision:kds14_20_cover_check` (decision)
- to: `DecisionOutcome:kds14_20_pass` (outcome)
- source_article: KDS 14 20 50 §4.3

## Edge — `targets_component`
- from: `PrecisionDiagnosisDecision:kds14_20_existing_safety_eval` (decision)
- to: `StructuralComponent:kds14_20_beam` (concept)
- source_article: KDS 14 20 90 §4

## Edge — `targets_work_type`
- from: `PrecisionDiagnosisDecision:kds14_20_existing_safety_eval` (decision)
- to: `WorkType:kds14_20_rc_design` (concept)
- source_article: KDS 14 20 90 §4

## Edge — `yields`
- from: `PrecisionDiagnosisDecision:kds14_20_existing_safety_eval` (decision)
- to: `DecisionOutcome:kds14_20_pass` (outcome)
- source_article: KDS 14 20 90 §4

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:kds14_20_seismic_detail` (decision)
- to: `StructuralComponent:kds14_20_beam` (concept)
- source_article: KDS 14 20 80 §4

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:kds14_20_seismic_detail` (decision)
- to: `WorkType:kds14_20_rc_design` (concept)
- source_article: KDS 14 20 80 §4

## Edge — `yields`
- from: `ConstructionInspectionDecision:kds14_20_seismic_detail` (decision)
- to: `DecisionOutcome:kds14_20_pass` (outcome)
- source_article: KDS 14 20 80 §4

## Edge — `qualified_as`
- from: `SiteEngineer:kds14_20_concrete_constructor` (subject)
- to: `Qualification:kds14_20_responsible_structural_engineer` (concept)
- source_article: _none_

## Edge — `can_view`
- from: `SiteEngineer:kds14_20_concrete_constructor` (subject)
- to: `TestReport:kds14_20_90_core_compression` (resource)
- source_article: _none_

## Edge — `qualified_as`
- from: `Supervisor:kds14_20_concrete_supervisor` (subject)
- to: `Qualification:kds14_20_responsible_structural_engineer` (concept)
- source_article: _none_

## Edge — `can_view`
- from: `Supervisor:kds14_20_concrete_supervisor` (subject)
- to: `TestReport:kds14_20_90_core_compression` (resource)
- source_article: _none_

## Edge — `qualified_as`
- from: `ChiefSupervisor:kds14_20_chief_structural` (subject)
- to: `Qualification:kds14_20_responsible_structural_engineer` (concept)
- source_article: _none_

## Edge — `can_view`
- from: `ChiefSupervisor:kds14_20_chief_structural` (subject)
- to: `TestReport:kds14_20_90_core_compression` (resource)
- source_article: _none_

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_responsible_structural_engineer` (concept)
- to: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- source_article: _none_

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_responsible_structural_engineer` (concept)
- to: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- source_article: _none_

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_responsible_structural_engineer` (concept)
- to: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- source_article: _none_

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_concrete_designer` (concept)
- to: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- source_article: _none_

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_concrete_designer` (concept)
- to: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- source_article: _none_

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_concrete_designer` (concept)
- to: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- source_article: _none_

## Edge — `precedes`
- from: `ConstructionInspectionDecision:kds14_20_strength_compliance` (decision)
- to: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- source_article: _none_

## Edge — `precedes`
- from: `MaterialReceiptDecision:kds14_20_rebar_yield` (decision)
- to: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- source_article: _none_

## Edge — `precedes`
- from: `StageApprovalDecision:kds14_20_rebar_placement` (decision)
- to: `ConstructionInspectionDecision:kds14_20_cover_check` (decision)
- source_article: _none_

## Edge — `precedes`
- from: `ConstructionInspectionDecision:kds14_20_cover_check` (decision)
- to: `PrecisionDiagnosisDecision:kds14_20_existing_safety_eval` (decision)
- source_article: _none_

## Edge — `precedes`
- from: `PrecisionDiagnosisDecision:kds14_20_existing_safety_eval` (decision)
- to: `ConstructionInspectionDecision:kds14_20_seismic_detail` (decision)
- source_article: _none_
