"""Build KS.jsonl from verified KS standard quantitative criteria.

Grammar-strict (manifest v1.0.0):
- SPACES: subject/resource/concept/decision/outcome only used here
- META_EDGES used:
  subject->concept: qualified_as
  subject->decision: performs
  concept->decision: grants_authority_for
  decision->resource: based_on
  decision->concept: targets_component / targets_facility / targets_work_type
  decision->outcome: yields
  decision->decision: depends_on / precedes
  concept->concept: subclass_of
"""
import json
import os

OUT = r"C:\temp\opencrab-civil_engineering_pack\extracted\standards\ks\KS.jsonl"

records = []


def node(space, ntype, nid, props, source_article):
    records.append({
        "kind": "node",
        "space": space,
        "node_type": ntype,
        "node_id": f"{ntype}:{nid}",
        "properties": props,
        "source_article": source_article,
    })


def edge(from_space, from_id, relation, to_space, to_id, source_article, props=None):
    records.append({
        "kind": "edge",
        "from_space": from_space,
        "from_id": from_id,
        "relation": relation,
        "to_space": to_space,
        "to_id": to_id,
        "properties": props or {},
        "source_article": source_article,
    })


# =========================================================================
# Shared subject / qualification concepts (re-usable across KS standards)
# =========================================================================
node("subject", "SiteEngineer", "ks_site_engineer_01",
     {"name_ko": "현장 시공자(시험 의뢰자)",
      "duties": ["KS 시험 의뢰", "공시체 채취 입회", "시험성적서 수령"]},
     "KS general")
node("subject", "Supervisor", "ks_supervisor_01",
     {"name_ko": "감리원(자재 검수 담당)",
      "duties": ["KS 적합 자재 확인", "시험성적서 검토", "검수 결정"]},
     "KS general")
node("subject", "ChiefSupervisor", "ks_chief_supervisor_01",
     {"name_ko": "책임감리원",
      "duties": ["자재 최종 승인", "불합격 자재 반출 지시", "감리보고서 결재"]},
     "KS general")

node("concept", "Qualification", "ks_qual_site_engineer_01",
     {"name_ko": "현장기술자", "scope": "KS 시험 의뢰 및 입회"},
     "KS general")
node("concept", "Qualification", "ks_qual_supervisor_01",
     {"name_ko": "감리원 자격",
      "scope": "KS F·KS D 기반 자재 검수 결정",
      "reference_law": "건설기술 진흥법 시행령 제55조"},
     "KS general")
node("concept", "Qualification", "ks_qual_chief_supervisor_01",
     {"name_ko": "책임감리원 자격",
      "scope": "KS 기반 자재 최종 승인"},
     "KS general")
node("concept", "Qualification", "ks_qual_ndt_ut_level2_01",
     {"name_ko": "비파괴검사기술자 UT 레벨 2 이상",
      "scope": "KS B 0896 강용접부 초음파 탐상",
      "reference_standard": "KS A 0035"},
     "KS B 0896")

edge("subject", "SiteEngineer:ks_site_engineer_01", "qualified_as",
     "concept", "Qualification:ks_qual_site_engineer_01", "KS general")
edge("subject", "Supervisor:ks_supervisor_01", "qualified_as",
     "concept", "Qualification:ks_qual_supervisor_01", "KS general")
edge("subject", "ChiefSupervisor:ks_chief_supervisor_01", "qualified_as",
     "concept", "Qualification:ks_qual_chief_supervisor_01", "KS general")

# Shared structural / work-type concept anchors
node("concept", "WorkType", "ks_worktype_concrete_01",
     {"name_ko": "콘크리트 공사 (자재·시험)"}, "KS F 4009/2402/2403/2405/2526")
node("concept", "WorkType", "ks_worktype_rebar_01",
     {"name_ko": "철근 공사 (자재·시험)"}, "KS D 3504")
node("concept", "WorkType", "ks_worktype_steel_struct_01",
     {"name_ko": "강구조 공사 (자재·시험)"}, "KS D 3503")
node("concept", "WorkType", "ks_worktype_weld_ut_01",
     {"name_ko": "강용접부 초음파 탐상"}, "KS B 0896")
node("concept", "StructuralComponent", "ks_component_concrete_01",
     {"name_ko": "콘크리트 부재"}, "KS F 4009")
node("concept", "StructuralComponent", "ks_component_rebar_01",
     {"name_ko": "철근(이형철근·원형철근)"}, "KS D 3504")
node("concept", "StructuralComponent", "ks_component_steel_01",
     {"name_ko": "압연 강재(강판·형강·평강)"}, "KS D 3503")
node("concept", "StructuralComponent", "ks_component_weld_01",
     {"name_ko": "맞대기 용접부"}, "KS B 0896")


# =========================================================================
# KS F 4009 — 레디믹스트 콘크리트
# =========================================================================
S = "KS F 4009"
# Specification anchor + sub-clauses
node("resource", "Specification", "ks_f_4009_main_01",
     {"name_ko": "KS F 4009 레디믹스트 콘크리트",
      "standard_no": "KS F 4009",
      "scope": "레미콘 종류·품질·시험·검사·운반·인도"},
     S)
node("resource", "Specification", "ks_f_4009_strength_01",
     {"name_ko": "압축강도 합격 판정",
      "standard_no": "KS F 4009",
      "criterion": "재령 28일 압축강도 ≥ 호칭강도",
      "rule_under_35MPa": "1회 시험치 ≥ 호칭강도 - 3.5 MPa",
      "rule_over_35MPa": "1회 시험치 ≥ 호칭강도 × 0.9",
      "test_age_days": 28},
     S)
node("resource", "Specification", "ks_f_4009_slump_tol_01",
     {"name_ko": "슬럼프 허용차",
      "standard_no": "KS F 4009",
      "tolerance_slump_25mm": "±10 mm",
      "tolerance_slump_50_65mm": "±15 mm",
      "tolerance_slump_80mm_plus": "±25 mm",
      "tolerance_slump_flow_500_600_700": "±100 mm"},
     S)
node("resource", "Specification", "ks_f_4009_air_01",
     {"name_ko": "공기량 허용차",
      "standard_no": "KS F 4009",
      "normal_concrete": "4.5 ± 1.5 %",
      "lightweight_concrete": "5.0 ± 1.5 %",
      "pavement_concrete": "4.5 ± 1.5 %",
      "high_strength_concrete": "3.5 ± 1.5 %"},
     S)
node("resource", "Specification", "ks_f_4009_chloride_01",
     {"name_ko": "염화물 함유량 한도",
      "standard_no": "KS F 4009",
      "limit_default_kg_per_m3": 0.30,
      "limit_with_approval_kg_per_m3": 0.60,
      "ion": "Cl-"},
     S)
node("resource", "Specification", "ks_f_4009_transport_01",
     {"name_ko": "운반 시간 한도",
      "standard_no": "KS F 4009",
      "limit_under_25C_hours": 1.5,
      "limit_over_25C_hours": 1.0},
     S)

# Decisions
node("decision", "MaterialReceiptDecision", "ks_f_4009_decision_strength_01",
     {"name_ko": "레미콘 압축강도 합격 판정",
      "criterion_source": "KS F 4009",
      "test_age_days": 28,
      "decision_basis": "공시체 압축강도 시험 결과"},
     S)
node("decision", "MaterialReceiptDecision", "ks_f_4009_decision_slump_01",
     {"name_ko": "레미콘 슬럼프 검수",
      "criterion_source": "KS F 4009",
      "field_test": True},
     S)
node("decision", "MaterialReceiptDecision", "ks_f_4009_decision_air_01",
     {"name_ko": "레미콘 공기량 검수",
      "criterion_source": "KS F 4009"},
     S)
node("decision", "MaterialReceiptDecision", "ks_f_4009_decision_chloride_01",
     {"name_ko": "레미콘 염화물 검수",
      "criterion_source": "KS F 4009"},
     S)

# Outcomes
node("outcome", "DecisionOutcome", "ks_f_4009_outcome_strength_pass_01",
     {"name_ko": "압축강도 합격", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_f_4009_outcome_strength_fail_01",
     {"name_ko": "압축강도 불합격", "result": "fail",
      "action": "추가 공시체 시험 또는 구조물 재하시험·코어 채취"}, S)
node("outcome", "DecisionOutcome", "ks_f_4009_outcome_slump_pass_01",
     {"name_ko": "슬럼프 적합", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_f_4009_outcome_slump_fail_01",
     {"name_ko": "슬럼프 부적합", "result": "fail", "action": "타설 거부·반품"}, S)
node("outcome", "DecisionOutcome", "ks_f_4009_outcome_air_pass_01",
     {"name_ko": "공기량 적합", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_f_4009_outcome_chloride_fail_01",
     {"name_ko": "염화물 초과 — 반품", "result": "fail",
      "action": "0.30 kg/m³ 초과(승인 0.60 kg/m³ 초과 시) 반품"}, S)

# TestReport resources
node("resource", "TestReport", "ks_f_4009_report_slump_01",
     {"name_ko": "슬럼프 시험 성적서", "linked_method": "KS F 2402"}, S)
node("resource", "TestReport", "ks_f_4009_report_strength_01",
     {"name_ko": "압축강도 시험 성적서", "linked_method": "KS F 2405"}, S)

# Edges — KS F 4009
# qualification grants authority
edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_f_4009_decision_strength_01", S)
edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_f_4009_decision_slump_01", S)
edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_f_4009_decision_air_01", S)
edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_f_4009_decision_chloride_01", S)

# subject performs
for d in ["ks_f_4009_decision_strength_01", "ks_f_4009_decision_slump_01",
          "ks_f_4009_decision_air_01", "ks_f_4009_decision_chloride_01"]:
    edge("subject", "Supervisor:ks_supervisor_01", "performs",
         "decision", f"MaterialReceiptDecision:{d}", S)

# decision based_on Specification
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_strength_01",
     "based_on", "resource", "Specification:ks_f_4009_strength_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_slump_01",
     "based_on", "resource", "Specification:ks_f_4009_slump_tol_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_air_01",
     "based_on", "resource", "Specification:ks_f_4009_air_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_chloride_01",
     "based_on", "resource", "Specification:ks_f_4009_chloride_01", S)
# also based_on TestReport
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_slump_01",
     "based_on", "resource", "TestReport:ks_f_4009_report_slump_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_strength_01",
     "based_on", "resource", "TestReport:ks_f_4009_report_strength_01", S)

# decision targets_component / work_type
for d in ["ks_f_4009_decision_strength_01", "ks_f_4009_decision_slump_01",
          "ks_f_4009_decision_air_01", "ks_f_4009_decision_chloride_01"]:
    edge("decision", f"MaterialReceiptDecision:{d}", "targets_component",
         "concept", "StructuralComponent:ks_component_concrete_01", S)
    edge("decision", f"MaterialReceiptDecision:{d}", "targets_work_type",
         "concept", "WorkType:ks_worktype_concrete_01", S)

# decision yields outcome
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_strength_01",
     "yields", "outcome", "DecisionOutcome:ks_f_4009_outcome_strength_pass_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_strength_01",
     "yields", "outcome", "DecisionOutcome:ks_f_4009_outcome_strength_fail_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_slump_01",
     "yields", "outcome", "DecisionOutcome:ks_f_4009_outcome_slump_pass_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_slump_01",
     "yields", "outcome", "DecisionOutcome:ks_f_4009_outcome_slump_fail_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_air_01",
     "yields", "outcome", "DecisionOutcome:ks_f_4009_outcome_air_pass_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_chloride_01",
     "yields", "outcome", "DecisionOutcome:ks_f_4009_outcome_chloride_fail_01", S)

# sub-specifications subclass_of main
for sub in ["ks_f_4009_strength_01", "ks_f_4009_slump_tol_01",
            "ks_f_4009_air_01", "ks_f_4009_chloride_01",
            "ks_f_4009_transport_01"]:
    # concept->concept rel allowed; here both resources, so skip subclass_of
    pass


# =========================================================================
# KS F 2403 — 공시체 제작
# =========================================================================
S = "KS F 2403"
node("resource", "Specification", "ks_f_2403_main_01",
     {"name_ko": "KS F 2403 콘크리트 공시체 제작 방법",
      "standard_no": "KS F 2403",
      "scope": "강도 시험용 공시체 제작·양생"},
     S)
node("resource", "Specification", "ks_f_2403_size_cyl_01",
     {"name_ko": "원주형 공시체 표준 치수",
      "standard_no": "KS F 2403",
      "size_standard_mm": "φ150 × 300",
      "size_alt_mm": "φ100 × 200",
      "ratio_d_to_h": "1:2",
      "min_diameter_vs_max_agg": "3배 이상"},
     S)
node("resource", "Specification", "ks_f_2403_size_prism_01",
     {"name_ko": "각주형 공시체 (휨) 표준 치수",
      "standard_no": "KS F 2403",
      "size_mm": "150 × 150 × 530",
      "span_mm": 450},
     S)
node("resource", "Specification", "ks_f_2403_curing_01",
     {"name_ko": "표준 양생 조건",
      "standard_no": "KS F 2403",
      "temperature_c": "20 ± 2",
      "relative_humidity_pct": "≥ 95",
      "demold_hours_range": "16 ~ 72"},
     S)
node("resource", "Specification", "ks_f_2403_compaction_01",
     {"name_ko": "다짐 방법",
      "standard_no": "KS F 2403",
      "rod_diameter_mm": 16,
      "layers": 3,
      "strokes_phi150": 25,
      "strokes_phi100": 15,
      "vibration_required_slump_below_mm": 50},
     S)

# decision: 공시체 적합성
node("decision", "MaterialReceiptDecision", "ks_f_2403_decision_specimen_01",
     {"name_ko": "공시체 제작 적합성 확인",
      "criterion_source": "KS F 2403"},
     S)
node("outcome", "DecisionOutcome", "ks_f_2403_outcome_pass_01",
     {"name_ko": "공시체 적합", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_f_2403_outcome_fail_01",
     {"name_ko": "공시체 부적합 — 재채취",
      "result": "fail", "action": "공시체 재제작"}, S)

edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01", S)
edge("subject", "Supervisor:ks_supervisor_01", "performs",
     "decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01",
     "based_on", "resource", "Specification:ks_f_2403_size_cyl_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01",
     "based_on", "resource", "Specification:ks_f_2403_curing_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01",
     "based_on", "resource", "Specification:ks_f_2403_compaction_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_concrete_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01",
     "targets_work_type", "concept",
     "WorkType:ks_worktype_concrete_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01",
     "yields", "outcome", "DecisionOutcome:ks_f_2403_outcome_pass_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01",
     "yields", "outcome", "DecisionOutcome:ks_f_2403_outcome_fail_01", S)


# =========================================================================
# KS F 2405 — 압축강도 시험
# =========================================================================
S = "KS F 2405"
node("resource", "Specification", "ks_f_2405_main_01",
     {"name_ko": "KS F 2405 콘크리트 압축강도 시험 방법",
      "standard_no": "KS F 2405"},
     S)
node("resource", "Specification", "ks_f_2405_loading_01",
     {"name_ko": "재하 속도",
      "standard_no": "KS F 2405",
      "loading_rate_mpa_per_s": "0.6 ± 0.4",
      "range_mpa_per_s": "0.2 ~ 1.0"},
     S)
node("resource", "Specification", "ks_f_2405_age_01",
     {"name_ko": "시험 재령",
      "standard_no": "KS F 2405",
      "standard_age_days": 28,
      "early_age_days_list": [3, 7],
      "long_age_days_list": [56, 91]},
     S)
node("resource", "Specification", "ks_f_2405_hd_correction_01",
     {"name_ko": "h/d 비 보정계수",
      "standard_no": "KS F 2405",
      "hd_2_0": 1.00,
      "hd_1_75": 0.98,
      "hd_1_50": 0.96,
      "hd_1_25": 0.93,
      "hd_1_00": 0.87},
     S)
node("resource", "Specification", "ks_f_2405_precision_01",
     {"name_ko": "정밀도 기준",
      "standard_no": "KS F 2405",
      "machine_accuracy_pct": 1.0,
      "platen_flatness_mm": 0.02,
      "specimen_end_flatness_mm": 0.05,
      "specimen_axis_squareness_deg": 0.5,
      "outlier_rule_pct": 15},
     S)

node("decision", "MaterialReceiptDecision", "ks_f_2405_decision_strength_test_01",
     {"name_ko": "압축강도 시험 적합 판정",
      "criterion_source": "KS F 2405"},
     S)
node("outcome", "DecisionOutcome", "ks_f_2405_outcome_valid_01",
     {"name_ko": "시험 유효", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_f_2405_outcome_invalid_01",
     {"name_ko": "시험 무효", "result": "fail",
      "action": "재시험 또는 이상치 제외"}, S)

edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01", S)
edge("subject", "Supervisor:ks_supervisor_01", "performs",
     "decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "based_on", "resource", "Specification:ks_f_2405_loading_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "based_on", "resource", "Specification:ks_f_2405_age_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "based_on", "resource", "Specification:ks_f_2405_hd_correction_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "based_on", "resource", "Specification:ks_f_2405_precision_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_concrete_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "targets_work_type", "concept",
     "WorkType:ks_worktype_concrete_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "yields", "outcome", "DecisionOutcome:ks_f_2405_outcome_valid_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "yields", "outcome", "DecisionOutcome:ks_f_2405_outcome_invalid_01", S)

# 2403 공시체 적합 -> 2405 압축강도 시험 (precedes)
edge("decision", "MaterialReceiptDecision:ks_f_2403_decision_specimen_01",
     "precedes", "decision",
     "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "KS F 2403 / KS F 2405")
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "depends_on", "decision",
     "MaterialReceiptDecision:ks_f_2403_decision_specimen_01",
     "KS F 2403 / KS F 2405")
# 2405 압축강도 -> 4009 합격 판정
edge("decision", "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "precedes", "decision",
     "MaterialReceiptDecision:ks_f_4009_decision_strength_01",
     "KS F 2405 / KS F 4009")
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_strength_01",
     "depends_on", "decision",
     "MaterialReceiptDecision:ks_f_2405_decision_strength_test_01",
     "KS F 2405 / KS F 4009")


# =========================================================================
# KS F 2402 — 슬럼프 시험
# =========================================================================
S = "KS F 2402"
node("resource", "Specification", "ks_f_2402_main_01",
     {"name_ko": "KS F 2402 슬럼프 시험 방법",
      "standard_no": "KS F 2402"}, S)
node("resource", "Specification", "ks_f_2402_cone_01",
     {"name_ko": "슬럼프 콘 치수",
      "standard_no": "KS F 2402",
      "top_diameter_mm": 100,
      "bottom_diameter_mm": 200,
      "height_mm": 300,
      "thickness_min_mm": 1.5},
     S)
node("resource", "Specification", "ks_f_2402_rod_01",
     {"name_ko": "다짐봉 규격",
      "standard_no": "KS F 2402",
      "diameter_mm": 16,
      "length_mm": 600,
      "tip": "반구형"},
     S)
node("resource", "Specification", "ks_f_2402_procedure_01",
     {"name_ko": "다짐 절차",
      "standard_no": "KS F 2402",
      "layers": 3,
      "strokes_per_layer": 25,
      "cone_lift_time_sec": "2 ~ 5",
      "test_window_min": 5,
      "reading_unit_mm": 5},
     S)

node("decision", "MaterialReceiptDecision", "ks_f_2402_decision_slump_test_01",
     {"name_ko": "슬럼프 시험 적합 판정",
      "criterion_source": "KS F 2402"}, S)
node("outcome", "DecisionOutcome", "ks_f_2402_outcome_valid_01",
     {"name_ko": "시험 유효", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_f_2402_outcome_invalid_01",
     {"name_ko": "전단 파괴 — 재시험", "result": "fail"}, S)

edge("concept", "Qualification:ks_qual_site_engineer_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01", S)
edge("subject", "SiteEngineer:ks_site_engineer_01", "performs",
     "decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01",
     "based_on", "resource", "Specification:ks_f_2402_cone_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01",
     "based_on", "resource", "Specification:ks_f_2402_procedure_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01",
     "based_on", "resource", "Specification:ks_f_2402_rod_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_concrete_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01",
     "targets_work_type", "concept",
     "WorkType:ks_worktype_concrete_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01",
     "yields", "outcome", "DecisionOutcome:ks_f_2402_outcome_valid_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01",
     "yields", "outcome", "DecisionOutcome:ks_f_2402_outcome_invalid_01", S)
# 2402 슬럼프 시험 -> 4009 슬럼프 판정 (precedes)
edge("decision", "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01",
     "precedes", "decision",
     "MaterialReceiptDecision:ks_f_4009_decision_slump_01",
     "KS F 2402 / KS F 4009")
edge("decision", "MaterialReceiptDecision:ks_f_4009_decision_slump_01",
     "depends_on", "decision",
     "MaterialReceiptDecision:ks_f_2402_decision_slump_test_01",
     "KS F 2402 / KS F 4009")


# =========================================================================
# KS F 2526 — 콘크리트용 골재
# =========================================================================
S = "KS F 2526"
node("resource", "Specification", "ks_f_2526_main_01",
     {"name_ko": "KS F 2526 콘크리트용 골재",
      "standard_no": "KS F 2526"}, S)
node("resource", "Specification", "ks_f_2526_fine_quality_01",
     {"name_ko": "잔골재 품질 기준",
      "standard_no": "KS F 2526",
      "abs_dry_density_min_g_cm3": 2.5,
      "absorption_max_pct": 3.0,
      "soundness_Na2SO4_max_pct": 10,
      "pass_0_08mm_max_pct_concrete": 3.0,
      "pass_0_08mm_max_pct_mortar": 5.0,
      "clay_lumps_max_pct": 1.0,
      "chloride_NaCl_max_pct": 0.04,
      "fineness_modulus_range": "2.3 ~ 3.1"},
     S)
node("resource", "Specification", "ks_f_2526_coarse_quality_01",
     {"name_ko": "굵은 골재 품질 기준",
      "standard_no": "KS F 2526",
      "abs_dry_density_min_g_cm3": 2.5,
      "absorption_max_pct": 3.0,
      "soundness_Na2SO4_max_pct": 12,
      "abrasion_LA_max_pct_general": 40,
      "abrasion_LA_max_pct_pavement": 25,
      "pass_0_08mm_max_pct": 1.0,
      "clay_lumps_max_pct": 0.25,
      "soft_particles_max_pct": 5.0},
     S)
node("resource", "Specification", "ks_f_2526_coarse_gradation_25_01",
     {"name_ko": "굵은 골재 표준 입도 (최대치수 25 mm)",
      "standard_no": "KS F 2526",
      "pass_25mm_pct_range": "90 ~ 100",
      "pass_19mm_pct_range": "20 ~ 55",
      "pass_10mm_pct_range": "0 ~ 10",
      "pass_5mm_pct_range": "0 ~ 5"},
     S)
node("resource", "Specification", "ks_f_2526_max_size_01",
     {"name_ko": "굵은 골재 최대치수 제한",
      "standard_no": "KS F 2526",
      "rule_member_min_dim": "부재 최소치수의 1/5 이하",
      "rule_rebar_spacing": "철근 최소간격의 3/4 이하",
      "rule_slab_thickness": "슬래브 두께의 1/3 이하"},
     S)
node("resource", "Specification", "ks_f_2526_asr_01",
     {"name_ko": "알칼리-실리카 반응성 평가",
      "standard_no": "KS F 2526",
      "chem_method_ref": "KS F 2545",
      "mortar_bar_method_ref": "KS F 2546",
      "required_result": "무해(innocuous)"},
     S)

node("decision", "MaterialReceiptDecision", "ks_f_2526_decision_fine_agg_01",
     {"name_ko": "잔골재 검수 판정",
      "criterion_source": "KS F 2526"}, S)
node("decision", "MaterialReceiptDecision", "ks_f_2526_decision_coarse_agg_01",
     {"name_ko": "굵은 골재 검수 판정",
      "criterion_source": "KS F 2526"}, S)
node("outcome", "DecisionOutcome", "ks_f_2526_outcome_pass_01",
     {"name_ko": "골재 적합", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_f_2526_outcome_fail_01",
     {"name_ko": "골재 부적합 — 반입 거절",
      "result": "fail", "action": "반품 또는 사용 금지"}, S)

edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_f_2526_decision_fine_agg_01", S)
edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_f_2526_decision_coarse_agg_01", S)
edge("subject", "Supervisor:ks_supervisor_01", "performs",
     "decision", "MaterialReceiptDecision:ks_f_2526_decision_fine_agg_01", S)
edge("subject", "Supervisor:ks_supervisor_01", "performs",
     "decision", "MaterialReceiptDecision:ks_f_2526_decision_coarse_agg_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2526_decision_fine_agg_01",
     "based_on", "resource", "Specification:ks_f_2526_fine_quality_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2526_decision_coarse_agg_01",
     "based_on", "resource", "Specification:ks_f_2526_coarse_quality_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2526_decision_coarse_agg_01",
     "based_on", "resource", "Specification:ks_f_2526_coarse_gradation_25_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2526_decision_coarse_agg_01",
     "based_on", "resource", "Specification:ks_f_2526_max_size_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2526_decision_fine_agg_01",
     "based_on", "resource", "Specification:ks_f_2526_asr_01", S)
edge("decision", "MaterialReceiptDecision:ks_f_2526_decision_coarse_agg_01",
     "based_on", "resource", "Specification:ks_f_2526_asr_01", S)

for d in ["ks_f_2526_decision_fine_agg_01", "ks_f_2526_decision_coarse_agg_01"]:
    edge("decision", f"MaterialReceiptDecision:{d}", "targets_component",
         "concept", "StructuralComponent:ks_component_concrete_01", S)
    edge("decision", f"MaterialReceiptDecision:{d}", "targets_work_type",
         "concept", "WorkType:ks_worktype_concrete_01", S)
    edge("decision", f"MaterialReceiptDecision:{d}", "yields",
         "outcome", "DecisionOutcome:ks_f_2526_outcome_pass_01", S)
    edge("decision", f"MaterialReceiptDecision:{d}", "yields",
         "outcome", "DecisionOutcome:ks_f_2526_outcome_fail_01", S)

# 골재 검수 -> 레미콘 검수 (precedes)
edge("decision", "MaterialReceiptDecision:ks_f_2526_decision_fine_agg_01",
     "precedes", "decision",
     "MaterialReceiptDecision:ks_f_4009_decision_strength_01",
     "KS F 2526 / KS F 4009")
edge("decision", "MaterialReceiptDecision:ks_f_2526_decision_coarse_agg_01",
     "precedes", "decision",
     "MaterialReceiptDecision:ks_f_4009_decision_strength_01",
     "KS F 2526 / KS F 4009")


# =========================================================================
# KS D 3504 — 철근콘크리트용 봉강
# =========================================================================
S = "KS D 3504"
node("resource", "Specification", "ks_d_3504_main_01",
     {"name_ko": "KS D 3504 철근콘크리트용 봉강",
      "standard_no": "KS D 3504"}, S)

# Grades — as Qualification concept (material grade)
grades = [
    ("sd300", "SD300", 300, 440, 16, "일반용"),
    ("sd400", "SD400", 400, 560, 16, "일반용"),
    ("sd500", "SD500", 500, 620, 12, "일반용"),
    ("sd600", "SD600", 600, 710, 10, "고강도"),
]
for gid, name, fy, fu, el, usage in grades:
    node("concept", "Qualification", f"ks_d_3504_grade_{gid}_01",
         {"name_ko": f"{name} 등급",
          "grade": name,
          "fy_min_mpa": fy,
          "fu_min_mpa": fu,
          "elongation_min_pct": el,
          "usage": usage,
          "standard_no": "KS D 3504"},
         S)

# Weldable & seismic variants
node("concept", "Qualification", "ks_d_3504_grade_sd400w_01",
     {"name_ko": "SD400W (용접용)",
      "grade": "SD400W",
      "fy_range_mpa": "400 ~ 520",
      "fu_min_mpa": 560,
      "ceq_max_pct": 0.50,
      "standard_no": "KS D 3504"}, S)
node("concept", "Qualification", "ks_d_3504_grade_sd500w_01",
     {"name_ko": "SD500W (용접용)",
      "grade": "SD500W",
      "fy_range_mpa": "500 ~ 620",
      "fu_min_mpa": 620,
      "ceq_max_pct": 0.50,
      "standard_no": "KS D 3504"}, S)
node("concept", "Qualification", "ks_d_3504_grade_sd400s_01",
     {"name_ko": "SD400S (내진용)",
      "grade": "SD400S",
      "yield_ratio_max": 1.25,
      "fy_overshoot_max_mpa": 130,
      "standard_no": "KS D 3504"}, S)
node("concept", "Qualification", "ks_d_3504_grade_sd500s_01",
     {"name_ko": "SD500S (내진용)",
      "grade": "SD500S",
      "yield_ratio_max": 1.25,
      "fy_overshoot_max_mpa": 130,
      "standard_no": "KS D 3504"}, S)
node("concept", "Qualification", "ks_d_3504_grade_sd600s_01",
     {"name_ko": "SD600S (내진용)",
      "grade": "SD600S",
      "yield_ratio_max": 1.25,
      "fy_overshoot_max_mpa": 130,
      "standard_no": "KS D 3504"}, S)

# subclass_of (concept->concept) — seismic grades inherit from base
edge("concept", "Qualification:ks_d_3504_grade_sd400s_01", "subclass_of",
     "concept", "Qualification:ks_d_3504_grade_sd400_01", S)
edge("concept", "Qualification:ks_d_3504_grade_sd500s_01", "subclass_of",
     "concept", "Qualification:ks_d_3504_grade_sd500_01", S)
edge("concept", "Qualification:ks_d_3504_grade_sd600s_01", "subclass_of",
     "concept", "Qualification:ks_d_3504_grade_sd600_01", S)
edge("concept", "Qualification:ks_d_3504_grade_sd400w_01", "subclass_of",
     "concept", "Qualification:ks_d_3504_grade_sd400_01", S)
edge("concept", "Qualification:ks_d_3504_grade_sd500w_01", "subclass_of",
     "concept", "Qualification:ks_d_3504_grade_sd500_01", S)

# Diameter spec (single resource with table)
node("resource", "Specification", "ks_d_3504_diameters_01",
     {"name_ko": "이형철근 호칭 지름 및 단위 질량",
      "standard_no": "KS D 3504",
      "table": [
          {"name": "D10", "d_mm": 9.53, "area_mm2": 71.33, "mass_kg_per_m": 0.560},
          {"name": "D13", "d_mm": 12.7, "area_mm2": 126.7, "mass_kg_per_m": 0.995},
          {"name": "D16", "d_mm": 15.9, "area_mm2": 198.6, "mass_kg_per_m": 1.56},
          {"name": "D19", "d_mm": 19.1, "area_mm2": 286.5, "mass_kg_per_m": 2.25},
          {"name": "D22", "d_mm": 22.2, "area_mm2": 387.1, "mass_kg_per_m": 3.04},
          {"name": "D25", "d_mm": 25.4, "area_mm2": 506.7, "mass_kg_per_m": 3.98},
          {"name": "D29", "d_mm": 28.6, "area_mm2": 642.4, "mass_kg_per_m": 5.04},
          {"name": "D32", "d_mm": 31.8, "area_mm2": 794.2, "mass_kg_per_m": 6.23},
          {"name": "D35", "d_mm": 34.9, "area_mm2": 956.6, "mass_kg_per_m": 7.51},
          {"name": "D38", "d_mm": 38.1, "area_mm2": 1140, "mass_kg_per_m": 8.95},
          {"name": "D41", "d_mm": 41.3, "area_mm2": 1340, "mass_kg_per_m": 10.5},
          {"name": "D51", "d_mm": 50.8, "area_mm2": 2027, "mass_kg_per_m": 15.9},
      ]},
     S)

node("resource", "Specification", "ks_d_3504_chem_01",
     {"name_ko": "화학 성분 한도 (SD400 일반)",
      "standard_no": "KS D 3504",
      "C_max_pct": 0.30,
      "P_max_pct": 0.040,
      "S_max_pct": 0.040,
      "Ceq_max_pct_general": 0.55,
      "Ceq_max_pct_weldable": 0.50},
     S)

node("resource", "Specification", "ks_d_3504_bend_01",
     {"name_ko": "굽힘 시험 기준",
      "standard_no": "KS D 3504",
      "angle_deg": 180,
      "inner_diameter_d16_sd300_400": "3d",
      "inner_diameter_d16_sd500": "4d",
      "inner_diameter_d19_sd300_400": "4d",
      "inner_diameter_d19_sd500": "5d",
      "inner_diameter_d19_sd600": "6d"},
     S)

# Decision
node("decision", "MaterialReceiptDecision", "ks_d_3504_decision_grade_01",
     {"name_ko": "철근 종류·강도 검수",
      "criterion_source": "KS D 3504"}, S)
node("decision", "MaterialReceiptDecision", "ks_d_3504_decision_bend_01",
     {"name_ko": "철근 굽힘 시험 판정",
      "criterion_source": "KS D 3504"}, S)
node("outcome", "DecisionOutcome", "ks_d_3504_outcome_pass_01",
     {"name_ko": "철근 적합", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_d_3504_outcome_fail_01",
     {"name_ko": "철근 부적합 — 반품", "result": "fail"}, S)

edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01", S)
edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_d_3504_decision_bend_01", S)
edge("subject", "Supervisor:ks_supervisor_01", "performs",
     "decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01", S)
edge("subject", "Supervisor:ks_supervisor_01", "performs",
     "decision", "MaterialReceiptDecision:ks_d_3504_decision_bend_01", S)

# decision based_on each grade specification + diameters/chem/bend
for gid, name, fy, fu, el, usage in grades:
    edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
         "based_on", "resource", "Specification:ks_d_3504_main_01", S)
# Grade decisions target the rebar component grade concept (targets_component)
for gid, _, _, _, _, _ in grades:
    edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
         "targets_component", "concept",
         f"Qualification:ks_d_3504_grade_{gid}_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
     "based_on", "resource", "Specification:ks_d_3504_diameters_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
     "based_on", "resource", "Specification:ks_d_3504_chem_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_bend_01",
     "based_on", "resource", "Specification:ks_d_3504_bend_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_rebar_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
     "targets_work_type", "concept",
     "WorkType:ks_worktype_rebar_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_bend_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_rebar_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_bend_01",
     "targets_work_type", "concept",
     "WorkType:ks_worktype_rebar_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
     "yields", "outcome", "DecisionOutcome:ks_d_3504_outcome_pass_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
     "yields", "outcome", "DecisionOutcome:ks_d_3504_outcome_fail_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_bend_01",
     "yields", "outcome", "DecisionOutcome:ks_d_3504_outcome_pass_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_bend_01",
     "yields", "outcome", "DecisionOutcome:ks_d_3504_outcome_fail_01", S)


# =========================================================================
# KS D 3503 — 일반 구조용 압연 강재
# =========================================================================
S = "KS D 3503"
node("resource", "Specification", "ks_d_3503_main_01",
     {"name_ko": "KS D 3503 일반 구조용 압연 강재",
      "standard_no": "KS D 3503"}, S)

ss_grades = [
    ("ss235", "SS235", 235, "330 ~ 450"),
    ("ss275", "SS275", 275, "410 ~ 550"),
    ("ss315", "SS315", 315, "490 ~ 630"),
    ("ss410", "SS410", 410, "540 ~ 680"),
    ("ss450", "SS450", 450, "590 ~ 740"),
    ("ss550", "SS550", 550, "690 ~ 830"),
]
for gid, name, fy, fu_range in ss_grades:
    node("concept", "Qualification", f"ks_d_3503_grade_{gid}_01",
         {"name_ko": f"{name} 등급",
          "grade": name,
          "fy_min_mpa": fy,
          "fu_range_mpa": fu_range,
          "standard_no": "KS D 3503"},
         S)

# thickness-dependent yield (SS275 example)
node("resource", "Specification", "ks_d_3503_yield_thickness_ss275_01",
     {"name_ko": "SS275 두께별 항복강도",
      "standard_no": "KS D 3503",
      "fy_t_le_16mm": 275,
      "fy_t_16_to_40mm": 265,
      "fy_t_40_to_100mm": 245,
      "fy_t_over_100mm": 235},
     S)
node("resource", "Specification", "ks_d_3503_elongation_ss275_01",
     {"name_ko": "SS275 연신율 (KS B 0801 5호 기준)",
      "standard_no": "KS D 3503",
      "elongation_t_le_5mm_pct": 21,
      "elongation_t_5_to_16mm_pct": 23,
      "elongation_t_over_16mm_pct": 24},
     S)
node("resource", "Specification", "ks_d_3503_chem_ss275_01",
     {"name_ko": "SS275 화학 성분",
      "standard_no": "KS D 3503",
      "C_max_pct_t_le_50mm": 0.24,
      "P_max_pct": 0.050,
      "S_max_pct": 0.050},
     S)
node("resource", "Specification", "ks_d_3503_bend_01",
     {"name_ko": "굽힘 시험 (SS235·SS275)",
      "standard_no": "KS D 3503",
      "angle_deg": 180,
      "inner_diameter": "1.5t"},
     S)

node("decision", "MaterialReceiptDecision", "ks_d_3503_decision_grade_01",
     {"name_ko": "강재 종류·강도 검수",
      "criterion_source": "KS D 3503"}, S)
node("outcome", "DecisionOutcome", "ks_d_3503_outcome_pass_01",
     {"name_ko": "강재 적합", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_d_3503_outcome_fail_01",
     {"name_ko": "강재 부적합 — 반품", "result": "fail"}, S)

edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01", S)
edge("subject", "Supervisor:ks_supervisor_01", "performs",
     "decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "based_on", "resource", "Specification:ks_d_3503_yield_thickness_ss275_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "based_on", "resource", "Specification:ks_d_3503_elongation_ss275_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "based_on", "resource", "Specification:ks_d_3503_chem_ss275_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "based_on", "resource", "Specification:ks_d_3503_bend_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "based_on", "resource", "Specification:ks_d_3503_main_01", S)
for gid, _, _, _ in ss_grades:
    edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
         "targets_component", "concept",
         f"Qualification:ks_d_3503_grade_{gid}_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_steel_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "targets_work_type", "concept",
     "WorkType:ks_worktype_steel_struct_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "yields", "outcome", "DecisionOutcome:ks_d_3503_outcome_pass_01", S)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "yields", "outcome", "DecisionOutcome:ks_d_3503_outcome_fail_01", S)


# =========================================================================
# KS B 0801 — 인장 시험편
# =========================================================================
S = "KS B 0801"
node("resource", "Specification", "ks_b_0801_main_01",
     {"name_ko": "KS B 0801 금속재료 인장 시험편",
      "standard_no": "KS B 0801"}, S)
node("resource", "Specification", "ks_b_0801_prop_gauge_01",
     {"name_ko": "비례 시험편 게이지 길이",
      "standard_no": "KS B 0801",
      "Lo_formula": "5.65 √Ao",
      "Lo_round_section": "5d",
      "Lo_long_formula": "11.3 √Ao",
      "Lo_long_round": "10d"},
     S)
node("resource", "Specification", "ks_b_0801_round_01",
     {"name_ko": "원형 시험편 표준 치수",
      "standard_no": "KS B 0801",
      "d_list_mm": [14, 12.5, 10, 8, 6, 5, 4, 3, 2.5],
      "Lc_range": "Lo + d ~ Lo + 2d",
      "grip_D_min_ratio": "1.4 × d",
      "shoulder_R_min_ratio": ">= d"},
     S)
node("resource", "Specification", "ks_b_0801_plate_01",
     {"name_ko": "판상 시험편 (1A·1B호)",
      "standard_no": "KS B 0801",
      "type_1A_b_mm": 25, "type_1A_Lo_mm": 50,
      "type_1B_b_mm": 12.5, "type_1B_Lo_mm": 25,
      "Lc_formula": "Lo + 2b",
      "shoulder_R_min_mm": 20},
     S)
node("resource", "Specification", "ks_b_0801_14_rebar_01",
     {"name_ko": "14호 시험편 (이형철근)",
      "standard_no": "KS B 0801",
      "Lo": "호칭 지름 5배 (5d)",
      "Lc_min": "5.5d",
      "area_used": "호칭 단면적"},
     S)
node("resource", "Specification", "ks_b_0801_finish_01",
     {"name_ko": "표면 가공·정밀도",
      "standard_no": "KS B 0801",
      "Ra_max_um": 3.2,
      "parallelism_max_mm": 0.05,
      "no_notch": True},
     S)

node("decision", "MaterialReceiptDecision", "ks_b_0801_decision_specimen_01",
     {"name_ko": "인장 시험편 적합성 확인",
      "criterion_source": "KS B 0801"}, S)
node("outcome", "DecisionOutcome", "ks_b_0801_outcome_pass_01",
     {"name_ko": "시험편 적합", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_b_0801_outcome_fail_01",
     {"name_ko": "시험편 부적합 — 재가공",
      "result": "fail", "action": "재가공"}, S)

edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_b_0801_decision_specimen_01", S)
edge("subject", "Supervisor:ks_supervisor_01", "performs",
     "decision", "MaterialReceiptDecision:ks_b_0801_decision_specimen_01", S)
for spec in ["ks_b_0801_prop_gauge_01", "ks_b_0801_round_01",
             "ks_b_0801_plate_01", "ks_b_0801_14_rebar_01",
             "ks_b_0801_finish_01"]:
    edge("decision", "MaterialReceiptDecision:ks_b_0801_decision_specimen_01",
         "based_on", "resource", f"Specification:{spec}", S)
edge("decision", "MaterialReceiptDecision:ks_b_0801_decision_specimen_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_steel_01", S)
edge("decision", "MaterialReceiptDecision:ks_b_0801_decision_specimen_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_rebar_01", S)
edge("decision", "MaterialReceiptDecision:ks_b_0801_decision_specimen_01",
     "targets_work_type", "concept",
     "WorkType:ks_worktype_steel_struct_01", S)
edge("decision", "MaterialReceiptDecision:ks_b_0801_decision_specimen_01",
     "yields", "outcome", "DecisionOutcome:ks_b_0801_outcome_pass_01", S)
edge("decision", "MaterialReceiptDecision:ks_b_0801_decision_specimen_01",
     "yields", "outcome", "DecisionOutcome:ks_b_0801_outcome_fail_01", S)


# =========================================================================
# KS B 0802 — 인장 시험 방법
# =========================================================================
S = "KS B 0802"
node("resource", "Specification", "ks_b_0802_main_01",
     {"name_ko": "KS B 0802 금속재료 인장 시험 방법",
      "standard_no": "KS B 0802"}, S)
node("resource", "Specification", "ks_b_0802_temperature_01",
     {"name_ko": "시험 온도",
      "standard_no": "KS B 0802",
      "standard_range_c": "10 ~ 35",
      "precision_range_c": "23 ± 5"},
     S)
node("resource", "Specification", "ks_b_0802_rate_01",
     {"name_ko": "변형/응력 속도",
      "standard_no": "KS B 0802",
      "elastic_stress_rate_mpa_per_s": "6 ~ 60",
      "elastic_strain_rate_per_s": "0.00025 ~ 0.0025",
      "yield_strain_rate_max_per_s": 0.0025,
      "post_yield_strain_rate_max_per_s": 0.008},
     S)
node("resource", "Specification", "ks_b_0802_ys_method_01",
     {"name_ko": "항복강도 결정 방법",
      "standard_no": "KS B 0802",
      "primary": "상부/하부 항복점 ReH/ReL",
      "offset_method": "Rp0.2 (영구 변형 0.2 %)",
      "alt_total_extension": "Rt0.5"},
     S)
node("resource", "Specification", "ks_b_0802_ts_method_01",
     {"name_ko": "인장강도 결정",
      "standard_no": "KS B 0802",
      "formula": "Rm = F_max / Ao",
      "unit": "MPa",
      "rounding": "1 MPa"},
     S)
node("resource", "Specification", "ks_b_0802_el_ra_01",
     {"name_ko": "연신율 및 단면수축률",
      "standard_no": "KS B 0802",
      "EL_formula": "(Lu - Lo) / Lo × 100",
      "RA_formula": "(Ao - Au) / Ao × 100",
      "break_position_rule": "표점 중앙에서 1/3 이내",
      "outside_gauge_rule": "표점 외 파단 시 강도값만 유효"},
     S)
node("resource", "Specification", "ks_b_0802_precision_01",
     {"name_ko": "측정 정밀도",
      "standard_no": "KS B 0802",
      "diameter_mm": 0.01,
      "plate_thickness_mm": 0.02,
      "gauge_length_pct": 0.5,
      "load_max_pct": 0.5,
      "machine_class_recommend": "등급 1"},
     S)

node("decision", "MaterialReceiptDecision", "ks_b_0802_decision_test_01",
     {"name_ko": "인장 시험 적합 판정",
      "criterion_source": "KS B 0802"}, S)
node("outcome", "DecisionOutcome", "ks_b_0802_outcome_valid_01",
     {"name_ko": "시험 유효", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_b_0802_outcome_invalid_01",
     {"name_ko": "시험 무효", "result": "fail",
      "action": "재시험 (그립부 파단 또는 표점 외 파단)"}, S)

edge("concept", "Qualification:ks_qual_supervisor_01", "grants_authority_for",
     "decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01", S)
edge("subject", "Supervisor:ks_supervisor_01", "performs",
     "decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01", S)
for spec in ["ks_b_0802_temperature_01", "ks_b_0802_rate_01",
             "ks_b_0802_ys_method_01", "ks_b_0802_ts_method_01",
             "ks_b_0802_el_ra_01", "ks_b_0802_precision_01"]:
    edge("decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01",
         "based_on", "resource", f"Specification:{spec}", S)
edge("decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_steel_01", S)
edge("decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_rebar_01", S)
edge("decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "targets_work_type", "concept",
     "WorkType:ks_worktype_steel_struct_01", S)
edge("decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "yields", "outcome", "DecisionOutcome:ks_b_0802_outcome_valid_01", S)
edge("decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "yields", "outcome", "DecisionOutcome:ks_b_0802_outcome_invalid_01", S)

# KS B 0801 (시험편) precedes KS B 0802 (시험)
edge("decision", "MaterialReceiptDecision:ks_b_0801_decision_specimen_01",
     "precedes", "decision",
     "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "KS B 0801 / KS B 0802")
edge("decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "depends_on", "decision",
     "MaterialReceiptDecision:ks_b_0801_decision_specimen_01",
     "KS B 0801 / KS B 0802")
# 0802 시험 -> 3504 철근 등급 검수
edge("decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "precedes", "decision",
     "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
     "KS B 0802 / KS D 3504")
edge("decision", "MaterialReceiptDecision:ks_d_3504_decision_grade_01",
     "depends_on", "decision",
     "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "KS B 0802 / KS D 3504")
# 0802 시험 -> 3503 강재 등급 검수
edge("decision", "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "precedes", "decision",
     "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "KS B 0802 / KS D 3503")
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "depends_on", "decision",
     "MaterialReceiptDecision:ks_b_0802_decision_test_01",
     "KS B 0802 / KS D 3503")


# =========================================================================
# KS B 0896 — 강용접부 UT
# =========================================================================
S = "KS B 0896"
node("resource", "Specification", "ks_b_0896_main_01",
     {"name_ko": "KS B 0896 강용접부 초음파 탐상",
      "standard_no": "KS B 0896",
      "scope_thickness_mm": "6 ~ 200"}, S)
node("resource", "Specification", "ks_b_0896_probe_01",
     {"name_ko": "탐촉자 사양",
      "standard_no": "KS B 0896",
      "angle_deg_list": [35, 45, 60, 70],
      "frequency_mhz_list": [2, 5],
      "transducer_size_mm_list": ["10×10", "14×14"]},
     S)
node("resource", "Specification", "ks_b_0896_stb_01",
     {"name_ko": "표준 시험편",
      "standard_no": "KS B 0896",
      "STB_A1_ref": "KS B 0831 — DAC 작성",
      "STB_A2_ref": "굴절각·입사점",
      "RB_4_ref": "DAC 보조"},
     S)
node("resource", "Specification", "ks_b_0896_dac_01",
     {"name_ko": "감도 조정 (DAC L/M/H 선)",
      "standard_no": "KS B 0896",
      "L_line_db": 0,
      "M_line_db": 6,
      "H_line_db": 12},
     S)
node("resource", "Specification", "ks_b_0896_class_01",
     {"name_ko": "결함 등급 분류 한계 (두께 18 mm 이하 예시)",
      "standard_no": "KS B 0896",
      "class_1": "영역 II, 길이 ≤ t/3",
      "class_2": "영역 II, 길이 ≤ t/2 또는 영역 III, 길이 ≤ t/3",
      "class_3": "영역 II, 길이 ≤ 2t/3 또는 영역 III, 길이 ≤ t/2 또는 영역 IV, 길이 ≤ t/3",
      "class_4": "그 외 (불합격)"},
     S)
node("resource", "Specification", "ks_b_0896_accept_01",
     {"name_ko": "합격 판정 (1차 응력 부재)",
      "standard_no": "KS B 0896",
      "pass": "1류·2류",
      "repair": "3류 보수 후 재검",
      "reject": "4류 불합격"},
     S)

node("decision", "ConstructionInspectionDecision",
     "ks_b_0896_decision_ut_01",
     {"name_ko": "강용접부 UT 검사 판정",
      "criterion_source": "KS B 0896",
      "decision_type": "비파괴 검사 결과 등급 판정"},
     S)
node("outcome", "DecisionOutcome", "ks_b_0896_outcome_pass_01",
     {"name_ko": "용접부 합격 (1·2류)", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "ks_b_0896_outcome_repair_01",
     {"name_ko": "용접부 보수 후 재검 (3류)", "result": "rework"}, S)
node("outcome", "DecisionOutcome", "ks_b_0896_outcome_reject_01",
     {"name_ko": "용접부 불합격 (4류)", "result": "fail",
      "action": "용접부 제거·재시공"}, S)

edge("concept", "Qualification:ks_qual_ndt_ut_level2_01", "grants_authority_for",
     "decision", "ConstructionInspectionDecision:ks_b_0896_decision_ut_01", S)
# Site engineer holds UT level 2 qualification (typical role binding)
node("subject", "SiteEngineer", "ks_b_0896_ut_inspector_01",
     {"name_ko": "비파괴검사 기술자 (UT 레벨 2 이상)",
      "duties": ["KS B 0896 UT 수행", "결함 등급 판정", "기록 작성"]},
     S)
edge("subject", "SiteEngineer:ks_b_0896_ut_inspector_01", "qualified_as",
     "concept", "Qualification:ks_qual_ndt_ut_level2_01", S)
edge("subject", "SiteEngineer:ks_b_0896_ut_inspector_01", "performs",
     "decision", "ConstructionInspectionDecision:ks_b_0896_decision_ut_01", S)

for spec in ["ks_b_0896_probe_01", "ks_b_0896_stb_01", "ks_b_0896_dac_01",
             "ks_b_0896_class_01", "ks_b_0896_accept_01", "ks_b_0896_main_01"]:
    edge("decision",
         "ConstructionInspectionDecision:ks_b_0896_decision_ut_01",
         "based_on", "resource", f"Specification:{spec}", S)
edge("decision", "ConstructionInspectionDecision:ks_b_0896_decision_ut_01",
     "targets_component", "concept",
     "StructuralComponent:ks_component_weld_01", S)
edge("decision", "ConstructionInspectionDecision:ks_b_0896_decision_ut_01",
     "targets_work_type", "concept",
     "WorkType:ks_worktype_weld_ut_01", S)
edge("decision", "ConstructionInspectionDecision:ks_b_0896_decision_ut_01",
     "yields", "outcome", "DecisionOutcome:ks_b_0896_outcome_pass_01", S)
edge("decision", "ConstructionInspectionDecision:ks_b_0896_decision_ut_01",
     "yields", "outcome", "DecisionOutcome:ks_b_0896_outcome_repair_01", S)
edge("decision", "ConstructionInspectionDecision:ks_b_0896_decision_ut_01",
     "yields", "outcome", "DecisionOutcome:ks_b_0896_outcome_reject_01", S)

# 3503 강재 합격이 UT 선행 (강재 적합 후 용접부 검사)
edge("decision", "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "precedes", "decision",
     "ConstructionInspectionDecision:ks_b_0896_decision_ut_01",
     "KS D 3503 / KS B 0896")
edge("decision", "ConstructionInspectionDecision:ks_b_0896_decision_ut_01",
     "depends_on", "decision",
     "MaterialReceiptDecision:ks_d_3503_decision_grade_01",
     "KS D 3503 / KS B 0896")


# =========================================================================
# Write
# =========================================================================
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

# Validate against manifest
from collections import Counter
SPACES = {
    "subject": {"User", "Team", "Org", "Agent", "Supervisor", "ChiefSupervisor",
                "SiteEngineer", "SafetyManager", "ChiefSafetyInspector",
                "ChiefPrecisionDiagnoser"},
    "resource": {"Project", "Document", "File", "Dataset", "Tool", "API",
                 "CrawlRun", "Drawing", "Specification", "Checklist",
                 "TestReport", "WorkPermit", "ConstructionLog",
                 "SupervisionLog", "MaterialReceiptReport",
                 "SafetyInspectionReport"},
    "evidence": {"TextUnit", "LogEntry", "Evidence"},
    "concept": {"Entity", "Concept", "Topic", "Class", "Qualification",
                "StructuralComponent", "WorkType", "Facility"},
    "claim": {"Claim", "Covariate", "CollectionCompleteness"},
    "community": {"Community", "CommunityReport"},
    "decision": {"MaterialReceiptDecision", "ConstructionInspectionDecision",
                 "WorkPermitDecision", "StageApprovalDecision",
                 "SafetyInspectionDecision", "PrecisionDiagnosisDecision"},
    "outcome": {"Outcome", "KPI", "Risk", "DecisionOutcome"},
    "lever": {"Lever"},
    "policy": {"Policy", "Sensitivity", "ApprovalRule"},
}
META = {
    ("subject", "resource"): {"owns", "member_of", "manages", "can_view",
                              "can_edit", "can_execute", "can_approve"},
    ("resource", "evidence"): {"contains", "derived_from", "logged_as"},
    ("evidence", "concept"): {"mentions", "describes", "exemplifies"},
    ("evidence", "claim"): {"supports", "contradicts", "timestamps"},
    ("concept", "concept"): {"related_to", "subclass_of", "part_of",
                             "influences", "depends_on"},
    ("concept", "outcome"): {"contributes_to", "constrains",
                             "predicts", "degrades"},
    ("lever", "outcome"): {"raises", "lowers", "stabilizes", "optimizes"},
    ("lever", "concept"): {"affects"},
    ("community", "concept"): {"clusters", "summarizes"},
    ("policy", "resource"): {"protects", "classifies", "restricts"},
    ("policy", "subject"): {"permits", "denies", "requires_approval"},
    ("subject", "concept"): {"qualified_as"},
    ("concept", "decision"): {"grants_authority_for"},
    ("subject", "decision"): {"performs"},
    ("decision", "concept"): {"targets_component", "targets_facility",
                              "targets_work_type"},
    ("decision", "resource"): {"based_on"},
    ("decision", "decision"): {"depends_on", "precedes"},
    ("decision", "outcome"): {"yields"},
}

errors = []
nodes_by_id = {}
type_counter = Counter()
relation_counter = Counter()

for r in records:
    if r["kind"] == "node":
        nt = r["node_type"]
        sp = r["space"]
        if nt not in SPACES.get(sp, set()):
            errors.append(f"BAD (space, type): ({sp}, {nt}) for {r['node_id']}")
        nodes_by_id[r["node_id"]] = sp
        type_counter[f"{sp}/{nt}"] += 1

for r in records:
    if r["kind"] == "edge":
        fs, ts = r["from_space"], r["to_space"]
        rel = r["relation"]
        if rel not in META.get((fs, ts), set()):
            errors.append(
                f"BAD edge ({fs}, {ts}, {rel}) {r['from_id']} -> {r['to_id']}"
            )
        if r["from_id"] not in nodes_by_id:
            errors.append(f"ORPHAN from: {r['from_id']}")
        if r["to_id"] not in nodes_by_id:
            errors.append(f"ORPHAN to: {r['to_id']}")
        relation_counter[rel] += 1

n_nodes = sum(1 for r in records if r["kind"] == "node")
n_edges = sum(1 for r in records if r["kind"] == "edge")

print(f"OUT={OUT}")
print(f"records={len(records)} nodes={n_nodes} edges={n_edges} errors={len(errors)}")
if errors:
    for e in errors[:50]:
        print("  ERR:", e)
print("\nTypes:")
for k, v in sorted(type_counter.items()):
    print(f"  {k}: {v}")
print("\nRelations:")
for k, v in sorted(relation_counter.items()):
    print(f"  {k}: {v}")
print(f"\nFile size: {os.path.getsize(OUT)} bytes")
