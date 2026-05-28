"""Build KCS.jsonl — Korean Construction Specification 5 codes:
KCS 14 20 (콘크리트), 14 31 (강구조), 21 50 (거푸집·동바리),
11 30 (연약지반), 21 60 (비계·가시설).

Grammar-strict (manifest v1.0.0): SPACES + META_EDGES only.
"""
import json
import os

OUT = r"C:\temp\opencrab-civil_engineering_pack\extracted\standards\kcs\KCS.jsonl"

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


def edge(from_space, from_id, relation, to_space, to_id, source_article,
         props=None):
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
# Shared subjects, qualifications, orgs (re-usable across all KCS codes)
# =========================================================================
node("subject", "Org", "kcsc_kcs_root_01",
     {"name_ko": "국가건설기준센터(KCSC)",
      "role": "KCS 표준시방서 관리·운영"},
     "KCS general")
node("subject", "Org", "kcs_ordering_agency_01",
     {"name_ko": "발주자",
      "role": "단계 승인·재시공 최종 권한"},
     "KCS general")

node("subject", "SiteEngineer", "kcs_site_engineer_01",
     {"name_ko": "시공자(현장기술자)",
      "duties": ["시공계획서 작성", "배합·재료 시험",
                 "검측 요청", "시공기록 작성"]},
     "KCS general")
node("subject", "Supervisor", "kcs_supervisor_01",
     {"name_ko": "감리원",
      "duties": ["자재 검수", "시공 검측", "단계 승인 결재",
                 "기록 검토"]},
     "KCS general")
node("subject", "ChiefSupervisor", "kcs_chief_supervisor_01",
     {"name_ko": "책임감리원",
      "duties": ["단계 승인 최종 결재", "재시공 협의",
                 "비파괴·강도 판정 결재"]},
     "KCS general")
node("subject", "SafetyManager", "kcs_safety_manager_01",
     {"name_ko": "안전관리자",
      "duties": ["작업 중지 권한", "안전시설 점검",
                 "재해 예방 조치"]},
     "KCS general")

node("concept", "Qualification", "kcs_qual_site_engineer_01",
     {"name_ko": "현장기술자(건설기술인)",
      "reference_law": "건설기술 진흥법 시행령 제55조"},
     "KCS general")
node("concept", "Qualification", "kcs_qual_supervisor_01",
     {"name_ko": "감리원 자격",
      "reference_law": "건설기술 진흥법 시행령 제55조"},
     "KCS general")
node("concept", "Qualification", "kcs_qual_chief_supervisor_01",
     {"name_ko": "책임감리원 자격",
      "reference_law": "건설기술 진흥법 시행령 제55조"},
     "KCS general")
node("concept", "Qualification", "kcs_qual_safety_manager_01",
     {"name_ko": "안전관리자 자격",
      "reference_law": "산업안전보건법 시행령 별표 4"},
     "KCS general")
node("concept", "Qualification", "kcs_qual_ndt_ut_lvl2_01",
     {"name_ko": "비파괴검사 UT 레벨 2 이상",
      "reference_standard": "KS B ISO 9712"},
     "KS B ISO 9712")
node("concept", "Qualification", "kcs_qual_welder_01",
     {"name_ko": "용접기능자(승인시험 합격)",
      "reference_standard": "KS B ISO 9606"},
     "KCS 14 31 20")
node("concept", "Qualification", "kcs_qual_soil_geo_01",
     {"name_ko": "토질·지반 기술자(토질및기초기술사 등)",
      "reference_law": "국가기술자격법(토질및기초기술사)"},
     "KCS 11 30")

edge("subject", "SiteEngineer:kcs_site_engineer_01", "qualified_as",
     "concept", "Qualification:kcs_qual_site_engineer_01", "KCS general")
edge("subject", "Supervisor:kcs_supervisor_01", "qualified_as",
     "concept", "Qualification:kcs_qual_supervisor_01", "KCS general")
edge("subject", "ChiefSupervisor:kcs_chief_supervisor_01", "qualified_as",
     "concept", "Qualification:kcs_qual_chief_supervisor_01", "KCS general")
edge("subject", "SafetyManager:kcs_safety_manager_01", "qualified_as",
     "concept", "Qualification:kcs_qual_safety_manager_01", "KCS general")


# =========================================================================
# Shared cross-code resources (logs/reports/checklists/work permits)
# =========================================================================
node("resource", "ConstructionLog", "log_kcs_construction_01",
     {"name_ko": "시공 일지",
      "purpose": "타설·양생·시공 일별 기록"}, "KCS general")
node("resource", "SupervisionLog", "log_kcs_supervision_01",
     {"name_ko": "감리 일지",
      "purpose": "검측 및 단계 승인 기록"}, "KCS general")
node("resource", "Checklist", "checklist_kcs_pre_pour_01",
     {"name_ko": "콘크리트 타설 전 체크리스트",
      "scope": "거푸집·철근·기상·배합 확인"}, "KCS 14 20 10")
node("resource", "Checklist", "checklist_kcs_form_strip_01",
     {"name_ko": "거푸집·동바리 해체 체크리스트",
      "scope": "강도·양생기간·부재 점검"}, "KCS 21 50 10")
node("resource", "Checklist", "checklist_kcs_weld_pre_01",
     {"name_ko": "용접 전 체크리스트",
      "scope": "기상·예열·자재·자격 확인"}, "KCS 14 31 20")
node("resource", "Checklist", "checklist_kcs_scaffold_daily_01",
     {"name_ko": "비계 일상 점검 체크리스트",
      "scope": "기둥·연결부·발판·풍속"}, "KCS 21 60 05")
node("resource", "TestReport", "test_kcs_strength_report_01",
     {"name_ko": "콘크리트 압축강도 시험성적서",
      "test_method": "KS F 2405"}, "KCS 14 20 10")
node("resource", "TestReport", "test_kcs_ut_report_01",
     {"name_ko": "용접부 UT 시험성적서",
      "test_method": "KS B 0896"}, "KCS 14 31 20")
node("resource", "TestReport", "test_kcs_torque_report_01",
     {"name_ko": "고장력볼트 토크·축력 시험성적서"},
     "KCS 14 31 25")
node("resource", "TestReport", "test_kcs_monitoring_report_01",
     {"name_ko": "연약지반 계측 보고서 (침하·간극수압·경사)"},
     "KCS 11 30 30")
node("resource", "WorkPermit", "permit_kcs_pour_01",
     {"name_ko": "콘크리트 타설 작업허가서"},
     "KCS 14 20 10")
node("resource", "WorkPermit", "permit_kcs_weld_01",
     {"name_ko": "강구조 용접 작업허가서"},
     "KCS 14 31 20")
node("resource", "WorkPermit", "permit_kcs_scaffold_01",
     {"name_ko": "비계 작업 허가서 (기상 조건 확인)"},
     "KCS 21 60 05")
node("resource", "SafetyInspectionReport",
     "safety_kcs_scaffold_report_01",
     {"name_ko": "비계 안전 점검 보고서"},
     "KCS 21 60 05")
node("resource", "SafetyInspectionReport",
     "safety_kcs_formwork_report_01",
     {"name_ko": "거푸집·동바리 안전 점검 보고서"},
     "KCS 21 50 15")


# =========================================================================
# KCS 14 20 — 콘크리트공사
# =========================================================================
S = "KCS 14 20"
# WorkType / Component anchors
node("concept", "WorkType", "kcs_14_20_worktype_concrete_01",
     {"name_ko": "콘크리트공사",
      "scope": "타설·양생·다짐·해체·시험"}, S)
node("concept", "WorkType", "kcs_14_20_worktype_winter_01",
     {"name_ko": "한중콘크리트공사",
      "applies_when": "일평균 기온 4℃ 이하"}, "KCS 14 20 11")
node("concept", "WorkType", "kcs_14_20_worktype_hot_01",
     {"name_ko": "서중콘크리트공사",
      "applies_when": "일평균 기온 25℃ 초과"}, "KCS 14 20 12")
node("concept", "WorkType", "kcs_14_20_worktype_mass_01",
     {"name_ko": "매스콘크리트공사",
      "applies_when": "수화열 관리 필요 부재(통상 두께 0.8m 이상)"},
     "KCS 14 20 13")
node("concept", "WorkType", "kcs_14_20_worktype_watertight_01",
     {"name_ko": "수밀콘크리트공사"}, "KCS 14 20 40")
node("concept", "StructuralComponent", "kcs_14_20_component_slab_01",
     {"name_ko": "콘크리트 슬래브·보"}, S)
node("concept", "StructuralComponent", "kcs_14_20_component_column_01",
     {"name_ko": "콘크리트 기둥·벽체"}, S)
node("concept", "StructuralComponent", "kcs_14_20_component_cantilever_01",
     {"name_ko": "콘크리트 캔틸레버 부재"},
     "KCS 14 20 10 / KCS 21 50 10")
edge("concept", "WorkType:kcs_14_20_worktype_mass_01", "subclass_of",
     "concept", "WorkType:kcs_14_20_worktype_concrete_01",
     "KCS 14 20 13")
edge("concept", "WorkType:kcs_14_20_worktype_watertight_01",
     "subclass_of", "concept",
     "WorkType:kcs_14_20_worktype_concrete_01", "KCS 14 20 40")
edge("concept", "WorkType:kcs_14_20_worktype_winter_01",
     "subclass_of", "concept",
     "WorkType:kcs_14_20_worktype_concrete_01", "KCS 14 20 11")
edge("concept", "WorkType:kcs_14_20_worktype_hot_01",
     "subclass_of", "concept",
     "WorkType:kcs_14_20_worktype_concrete_01", "KCS 14 20 12")

# Specification anchors — KCS 14 20 sub-clauses
node("resource", "Specification", "spec_kcs_14_20_main_01",
     {"name_ko": "KCS 14 20 콘크리트공사 표준시방서",
      "standard_no": "KCS 14 20 00",
      "issuer": "국가건설기준센터",
      "latest_notice": "국토교통부고시 제2024-879호 (2024-12-30)"},
     "KCS 14 20 00")
node("resource", "Specification", "spec_kcs_14_20_mix_wb_01",
     {"name_ko": "물-결합재비(W/B) 한계",
      "standard_no": "KCS 14 20 10",
      "EX0_max_wb": 0.60,
      "EX1_max_wb": 0.55,
      "EX2_max_wb": 0.50,
      "EX3_EX4_max_wb": 0.45,
      "unit_water_max_kg_per_m3": 185},
     "KCS 14 20 10")
node("resource", "Specification", "spec_kcs_14_20_slump_air_01",
     {"name_ko": "슬럼프·공기량·염화물 한계",
      "standard_no": "KCS 14 20 10",
      "slump_tolerance_mm": "±25 (80~180mm 호칭)",
      "air_normal_pct": "4.5±1.5",
      "air_lightweight_pct": "5.0±1.5",
      "chloride_max_kg_per_m3": 0.30,
      "test_methods": ["KS F 2402", "KS F 2421", "KS F 2515"]},
     "KCS 14 20 10")
node("resource", "Specification", "spec_kcs_14_20_transport_time_01",
     {"name_ko": "운반·타설 시간 한계 (KS F 4009)",
      "standard_no": "KCS 14 20 10",
      "limit_below_25C_hours": 1.5,
      "limit_above_25C_hours": 1.0,
      "cold_joint_below_25C_hours": 2.5,
      "cold_joint_above_25C_hours": 2.0,
      "reference_standard": "KS F 4009"},
     "KCS 14 20 10")
node("resource", "Specification", "spec_kcs_14_20_placement_01",
     {"name_ko": "타설·다짐 한계",
      "standard_no": "KCS 14 20 10",
      "free_fall_max_m": 1.5,
      "vibrator_spacing_max_cm": 50,
      "vibrator_dwell_sec": "5~15",
      "pump_vertical_max_m": 100,
      "pump_horizontal_max_m": 300},
     "KCS 14 20 10")
node("resource", "Specification", "spec_kcs_14_20_rain_exception_01",
     {"name_ko": "우천 시 타설 예외·중지 기준",
      "standard_no": "KCS 14 20 10",
      "rule": "강우 시 타설 금지 원칙, 시트·천막 양생 보호 시 한정 시공",
      "stop_condition": ["호우주의보 발효",
                         "표면 빗물 고임·워싱아웃 우려",
                         "강풍주의보 발효"]},
     "KCS 14 20 10")
node("resource", "Specification", "spec_kcs_14_20_cold_01",
     {"name_ko": "한중콘크리트 시공 한계",
      "standard_no": "KCS 14 20 11",
      "trigger_temp_C": "일평균 4 이하 또는 24h 내 0 예상",
      "placement_temp_range_C": "5 ~ 20",
      "curing_surface_min_C": 5,
      "initial_frost_strength_MPa": 5,
      "insulated_curing_days_min": 5,
      "heated_curing_days_min": 3,
      "heating_mandatory_below_C": -3,
      "heated_mandatory_below_C": -10},
     "KCS 14 20 11")
node("resource", "Specification", "spec_kcs_14_20_hot_01",
     {"name_ko": "서중콘크리트 시공 한계",
      "standard_no": "KCS 14 20 12",
      "trigger_temp_C": "일평균 25 초과 또는 최고 30 초과",
      "placement_temp_max_C": 35,
      "transport_max_hours": 1.0,
      "wet_curing_days_min": 5},
     "KCS 14 20 12")
node("resource", "Specification", "spec_kcs_14_20_curing_general_01",
     {"name_ko": "일반 습윤양생 기간",
      "standard_no": "KCS 14 20 10",
      "T15_days_min": 5,
      "T10to15_days_min": 7,
      "T5to10_days_min": 9,
      "curing_temp_min_C": 5,
      "no_impact_hours_min": 24},
     "KCS 14 20 10")
node("resource", "Specification", "spec_kcs_14_20_strip_form_01",
     {"name_ko": "거푸집·동바리 해체 강도 기준",
      "standard_no": "KCS 14 20 10",
      "side_form_min_MPa": 5,
      "simply_supported_min_fck_pct": 50,
      "continuous_min_fck_pct": 100,
      "cantilever_min_fck_pct": 100,
      "test_method": "KS F 2405"},
     "KCS 14 20 10")
node("resource", "Specification", "spec_kcs_14_20_strength_judge_01",
     {"name_ko": "압축강도 합격 판정",
      "standard_no": "KCS 14 20 10",
      "single_min_pct": 85,
      "three_avg_min_pct": 100,
      "frequency": "150㎥/회 (KS F 4009)"},
     "KCS 14 20 10")
node("resource", "Specification", "spec_kcs_14_20_unit_cement_01",
     {"name_ko": "최소 단위시멘트량",
      "standard_no": "KCS 14 20 10",
      "min_kg_per_m3_range": "270 ~ 330",
      "depends_on": "노출등급(EX0~EX4)"},
     "KCS 14 20 10")
node("resource", "Specification", "spec_kcs_14_20_aggregate_01",
     {"name_ko": "굵은골재 최대치수 한계",
      "standard_no": "KCS 14 20 10",
      "slab_beam_max_mm": 25,
      "general_max_mm": 40},
     "KCS 14 20 10")
# Wire new specs to existing decisions
edge("decision",
     "StageApprovalDecision:decision_kcs_14_20_mix_approval_01",
     "based_on", "resource",
     "Specification:spec_kcs_14_20_unit_cement_01", "KCS 14 20 10")
edge("decision",
     "MaterialReceiptDecision:decision_kcs_14_20_material_01",
     "based_on", "resource",
     "Specification:spec_kcs_14_20_aggregate_01", "KCS 14 20 10")

# Decisions — KCS 14 20
node("decision", "MaterialReceiptDecision",
     "decision_kcs_14_20_material_01",
     {"name_ko": "콘크리트 자재 검수 결정",
      "criterion_source": "KCS 14 20 10 자재 검수"}, S)
node("decision", "StageApprovalDecision",
     "decision_kcs_14_20_mix_approval_01",
     {"name_ko": "콘크리트 배합·시공계획서 승인",
      "criterion_source": "KCS 14 20 10",
      "checks": ["W/B비", "단위수량", "슬럼프", "공기량"]}, S)
node("decision", "WorkPermitDecision",
     "decision_kcs_14_20_pour_permit_01",
     {"name_ko": "콘크리트 타설 작업허가",
      "criterion_source": "KCS 14 20 10",
      "preconditions": ["거푸집 검측 완료",
                        "철근 배근 검측 완료",
                        "기상 적합 (강우 없음·기온 적합)"]}, S)
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_14_20_pour_inspection_01",
     {"name_ko": "타설 검측 (다짐·이어치기·자유낙하)",
      "criterion_source": "KCS 14 20 10"}, S)
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_14_20_winter_inspection_01",
     {"name_ko": "한중콘크리트 양생 검측",
      "criterion_source": "KCS 14 20 11",
      "checks": ["콘크리트 온도", "양생 시설", "초기 동해 방지"]},
     "KCS 14 20 11")
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_14_20_hot_inspection_01",
     {"name_ko": "서중콘크리트 양생 검측",
      "criterion_source": "KCS 14 20 12",
      "checks": ["콘크리트 온도", "습윤양생", "차광"]},
     "KCS 14 20 12")
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_14_20_strength_test_01",
     {"name_ko": "압축강도 시험 판정",
      "criterion_source": "KCS 14 20 10"},
     "KCS 14 20 10")
node("decision", "StageApprovalDecision",
     "decision_kcs_14_20_form_strip_approval_01",
     {"name_ko": "거푸집·동바리 해체 승인",
      "criterion_source": "KCS 14 20 10 + KCS 21 50 10"},
     "KCS 14 20 10")

# Outcomes
node("outcome", "DecisionOutcome", "outcome_kcs_14_20_pass_01",
     {"name_ko": "합격·승인", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_14_20_rework_01",
     {"name_ko": "재시공·보강", "result": "rework"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_14_20_stop_01",
     {"name_ko": "작업 중지(우천·강풍·기온)",
      "result": "work_stop"}, S)

# Authority grants
edge("concept", "Qualification:kcs_qual_supervisor_01",
     "grants_authority_for", "decision",
     "MaterialReceiptDecision:decision_kcs_14_20_material_01", S)
edge("concept", "Qualification:kcs_qual_chief_supervisor_01",
     "grants_authority_for", "decision",
     "StageApprovalDecision:decision_kcs_14_20_mix_approval_01", S)
edge("concept", "Qualification:kcs_qual_chief_supervisor_01",
     "grants_authority_for", "decision",
     "WorkPermitDecision:decision_kcs_14_20_pour_permit_01", S)
edge("concept", "Qualification:kcs_qual_supervisor_01",
     "grants_authority_for", "decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01",
     S)
edge("concept", "Qualification:kcs_qual_supervisor_01",
     "grants_authority_for", "decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01",
     "KCS 14 20 11")
edge("concept", "Qualification:kcs_qual_supervisor_01",
     "grants_authority_for", "decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01",
     "KCS 14 20 12")
edge("concept", "Qualification:kcs_qual_chief_supervisor_01",
     "grants_authority_for", "decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01",
     "KCS 14 20 10")
edge("concept", "Qualification:kcs_qual_chief_supervisor_01",
     "grants_authority_for", "decision",
     "StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01",
     "KCS 14 20 10")

# Performs (subject -> decision)
edge("subject", "Supervisor:kcs_supervisor_01", "performs",
     "decision",
     "MaterialReceiptDecision:decision_kcs_14_20_material_01", S)
edge("subject", "ChiefSupervisor:kcs_chief_supervisor_01", "performs",
     "decision",
     "StageApprovalDecision:decision_kcs_14_20_mix_approval_01", S)
edge("subject", "ChiefSupervisor:kcs_chief_supervisor_01", "performs",
     "decision",
     "WorkPermitDecision:decision_kcs_14_20_pour_permit_01", S)
edge("subject", "Supervisor:kcs_supervisor_01", "performs",
     "decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01",
     S)
edge("subject", "Supervisor:kcs_supervisor_01", "performs",
     "decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01",
     "KCS 14 20 11")
edge("subject", "Supervisor:kcs_supervisor_01", "performs",
     "decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01",
     "KCS 14 20 12")
edge("subject", "ChiefSupervisor:kcs_chief_supervisor_01", "performs",
     "decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01",
     "KCS 14 20 10")
edge("subject", "ChiefSupervisor:kcs_chief_supervisor_01", "performs",
     "decision",
     "StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01",
     "KCS 14 20 10")

# Decisions based_on specifications
KCS1420_SPECS = [
    "spec_kcs_14_20_main_01", "spec_kcs_14_20_mix_wb_01",
    "spec_kcs_14_20_slump_air_01", "spec_kcs_14_20_transport_time_01",
    "spec_kcs_14_20_placement_01", "spec_kcs_14_20_rain_exception_01",
    "spec_kcs_14_20_cold_01", "spec_kcs_14_20_hot_01",
    "spec_kcs_14_20_curing_general_01", "spec_kcs_14_20_strip_form_01",
    "spec_kcs_14_20_strength_judge_01",
]
KCS1420_BASED = {
    "MaterialReceiptDecision:decision_kcs_14_20_material_01":
        ["spec_kcs_14_20_main_01", "spec_kcs_14_20_slump_air_01"],
    "StageApprovalDecision:decision_kcs_14_20_mix_approval_01":
        ["spec_kcs_14_20_mix_wb_01", "spec_kcs_14_20_slump_air_01"],
    "WorkPermitDecision:decision_kcs_14_20_pour_permit_01":
        ["spec_kcs_14_20_transport_time_01",
         "spec_kcs_14_20_rain_exception_01"],
    "ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01":
        ["spec_kcs_14_20_placement_01", "spec_kcs_14_20_transport_time_01"],
    "ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01":
        ["spec_kcs_14_20_cold_01", "spec_kcs_14_20_curing_general_01"],
    "ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01":
        ["spec_kcs_14_20_hot_01", "spec_kcs_14_20_curing_general_01"],
    "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01":
        ["spec_kcs_14_20_strength_judge_01"],
    "StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01":
        ["spec_kcs_14_20_strip_form_01"],
}
for d_id, specs in KCS1420_BASED.items():
    for sp in specs:
        edge("decision", d_id, "based_on", "resource",
             f"Specification:{sp}", S)

# Decisions targeting work types / components
for d_id in [
    "ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01",
    "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01",
    "WorkPermitDecision:decision_kcs_14_20_pour_permit_01",
    "StageApprovalDecision:decision_kcs_14_20_mix_approval_01",
]:
    edge("decision", d_id, "targets_work_type", "concept",
         "WorkType:kcs_14_20_worktype_concrete_01", S)

edge("decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01",
     "targets_work_type", "concept",
     "WorkType:kcs_14_20_worktype_winter_01", "KCS 14 20 11")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01",
     "targets_work_type", "concept",
     "WorkType:kcs_14_20_worktype_hot_01", "KCS 14 20 12")
edge("decision",
     "StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_14_20_component_slab_01", "KCS 14 20 10")
edge("decision",
     "StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_14_20_component_column_01", "KCS 14 20 10")
edge("decision",
     "StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_14_20_component_cantilever_01",
     "KCS 14 20 10")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_14_20_component_slab_01", "KCS 14 20 10")

# Yields outcomes
for d_id in [
    "MaterialReceiptDecision:decision_kcs_14_20_material_01",
    "StageApprovalDecision:decision_kcs_14_20_mix_approval_01",
    "WorkPermitDecision:decision_kcs_14_20_pour_permit_01",
    "ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01",
    "ConstructionInspectionDecision:decision_kcs_14_20_winter_inspection_01",
    "ConstructionInspectionDecision:decision_kcs_14_20_hot_inspection_01",
    "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01",
    "StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01",
]:
    edge("decision", d_id, "yields", "outcome",
         "DecisionOutcome:outcome_kcs_14_20_pass_01", S)
    edge("decision", d_id, "yields", "outcome",
         "DecisionOutcome:outcome_kcs_14_20_rework_01", S)

edge("decision",
     "WorkPermitDecision:decision_kcs_14_20_pour_permit_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_14_20_stop_01",
     "KCS 14 20 10 rain exception")

# Decision dependencies (precedes / depends_on) — construction sequence
SEQ_1420 = [
    ("MaterialReceiptDecision:decision_kcs_14_20_material_01",
     "StageApprovalDecision:decision_kcs_14_20_mix_approval_01"),
    ("StageApprovalDecision:decision_kcs_14_20_mix_approval_01",
     "WorkPermitDecision:decision_kcs_14_20_pour_permit_01"),
    ("WorkPermitDecision:decision_kcs_14_20_pour_permit_01",
     "ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01"),
    ("ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01",
     "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01"),
    ("ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01",
     "StageApprovalDecision:decision_kcs_14_20_form_strip_approval_01"),
]
for a, b in SEQ_1420:
    edge("decision", a, "precedes", "decision", b, S)
    edge("decision", b, "depends_on", "decision", a, S)


# =========================================================================
# KCS 14 31 — 강구조공사 (결합법·시공한계·UT·풍속)
# =========================================================================
S = "KCS 14 31"
node("concept", "WorkType", "kcs_14_31_worktype_steel_01",
     {"name_ko": "강구조공사",
      "scope": "공장제작·현장설치·용접·볼트접합·도장"}, S)
node("concept", "WorkType", "kcs_14_31_worktype_weld_01",
     {"name_ko": "강구조 용접 (결합법)",
      "scope": "맞대기·필릿·부분침투"}, "KCS 14 31 20")
node("concept", "WorkType", "kcs_14_31_worktype_hsb_01",
     {"name_ko": "고장력볼트 접합 (결합법)",
      "scope": "마찰·인장·지압 접합"}, "KCS 14 31 25")
node("concept", "WorkType", "kcs_14_31_worktype_paint_01",
     {"name_ko": "강구조 도장",
      "scope": "표면처리·도막두께"}, "KCS 14 31 40")
node("concept", "StructuralComponent", "kcs_14_31_component_beam_01",
     {"name_ko": "강재 보·기둥"}, S)
node("concept", "StructuralComponent", "kcs_14_31_component_weld_01",
     {"name_ko": "용접부 (맞대기 그루브)"}, "KCS 14 31 20")
node("concept", "StructuralComponent", "kcs_14_31_component_bolt_01",
     {"name_ko": "고장력볼트 접합부"}, "KCS 14 31 25")
edge("concept", "WorkType:kcs_14_31_worktype_weld_01", "subclass_of",
     "concept", "WorkType:kcs_14_31_worktype_steel_01", "KCS 14 31 20")
edge("concept", "WorkType:kcs_14_31_worktype_hsb_01", "subclass_of",
     "concept", "WorkType:kcs_14_31_worktype_steel_01", "KCS 14 31 25")
edge("concept", "WorkType:kcs_14_31_worktype_paint_01", "subclass_of",
     "concept", "WorkType:kcs_14_31_worktype_steel_01", "KCS 14 31 40")

# Specifications
node("resource", "Specification", "spec_kcs_14_31_main_01",
     {"name_ko": "KCS 14 31 강구조공사 표준시방서",
      "standard_no": "KCS 14 31 00",
      "latest_notice": "국토교통부고시 제2024-224호"}, S)
node("resource", "Specification", "spec_kcs_14_31_precision_01",
     {"name_ko": "강구조 정밀도(시공 한계)",
      "standard_no": "KCS 14 31 05",
      "length_tol_mm": "±2 ~ ±3",
      "vert_tol_max_mm": 35,
      "vert_tol_ratio": "±H/1000",
      "horiz_tol_ratio": "±L/1000",
      "twist_tol_ratio": "±L/700",
      "bolt_hole_offset_mm": "±1"},
     "KCS 14 31 05")
node("resource", "Specification", "spec_kcs_14_31_weld_env_01",
     {"name_ko": "용접 시공 환경 한계",
      "standard_no": "KCS 14 31 20",
      "ambient_temp_min_C": -5,
      "preheat_required_below_C": 5,
      "wind_gas_shield_max_m_per_s": 2,
      "wind_stop_all_m_per_s": 10,
      "humidity_stop_pct": 80,
      "rain_snow_rule": "차폐 불가 시 작업 중지"},
     "KCS 14 31 20")
node("resource", "Specification", "spec_kcs_14_31_preheat_01",
     {"name_ko": "예열 온도",
      "standard_no": "KCS 14 31 20",
      "SM355_t25_min_C": 50,
      "SM355_t25_50_min_C": 80,
      "SM490_t50_min_C": 100,
      "HSA800_min_C": 100,
      "additional_below_0C_C": 25,
      "measure_point_mm_from_weld": 75},
     "KCS 14 31 20")
node("resource", "Specification", "spec_kcs_14_31_ut_01",
     {"name_ko": "용접부 UT 검사 기준",
      "standard_no": "KCS 14 31 20",
      "qualification": "KS B ISO 9712 Level 2",
      "method_standard": "KS B 0896",
      "delay_after_weld_hours": "8 ~ 48",
      "lot_size": "300 용접/로트",
      "sample_per_lot": 30,
      "accept_initial_max_defects": 1,
      "rework_range": "2~3",
      "rework_60_pass_max": 4},
     "KCS 14 31 20")
node("resource", "Specification", "spec_kcs_14_31_rework_limit_01",
     {"name_ko": "용접 재시공 한계",
      "standard_no": "KCS 14 31 20",
      "normal_steel_max_redo": 3,
      "high_strength_steel_max_redo": 2,
      "action_if_exceed": "부재 교체 협의"},
     "KCS 14 31 20")
node("resource", "Specification", "spec_kcs_14_31_hsb_01",
     {"name_ko": "고장력볼트 시공",
      "standard_no": "KCS 14 31 25",
      "grades": ["F8T", "F10T", "F13T", "S10T"],
      "primary_tighten_pct": 60,
      "final_tighten_pct": 100,
      "final_tolerance_pct": 10,
      "nut_rotation_deg_options": [60, 90, 120],
      "rain_snow_rule": "마찰면 노출 금지, 미처리 시 본 조임 금지"},
     "KCS 14 31 25")
node("resource", "Specification", "spec_kcs_14_31_hsb_inspect_01",
     {"name_ko": "고장력볼트 검사",
      "standard_no": "KCS 14 31 25",
      "sample_pct_per_group": 10,
      "min_sample_count": 10,
      "marking_check": "본 조임 후 마킹 어긋남으로 확인",
      "reuse": "불합격 볼트 재사용 금지"},
     "KCS 14 31 25")
node("resource", "Specification", "spec_kcs_14_31_paint_01",
     {"name_ko": "도장 환경 한계",
      "standard_no": "KCS 14 31 40",
      "surface_prep": "SSPC-SP10 / Sa2.5",
      "steel_temp_range_C": "5 ~ 50",
      "dew_point_margin_C": 3,
      "humidity_max_pct": 85,
      "wind_spray_stop_m_per_s": 8,
      "DFT_um_range": "200 ~ 320"},
     "KCS 14 31 40")

# Decisions — KCS 14 31
node("decision", "MaterialReceiptDecision",
     "decision_kcs_14_31_material_01",
     {"name_ko": "강재·볼트·용접재 검수 결정",
      "criterion_source": "KCS 14 31 05"}, S)
node("decision", "StageApprovalDecision",
     "decision_kcs_14_31_plan_approval_01",
     {"name_ko": "강구조 시공계획서 승인",
      "criterion_source": "KCS 14 31 05"}, S)
node("decision", "WorkPermitDecision",
     "decision_kcs_14_31_weld_permit_01",
     {"name_ko": "용접 작업허가 (기상·예열 확인)",
      "criterion_source": "KCS 14 31 20",
      "stop_triggers": ["기온 -5℃ 이하",
                        "풍속 10m/s 초과",
                        "강우·강설"]}, "KCS 14 31 20")
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_14_31_weld_visual_01",
     {"name_ko": "용접 외관 검사·정밀도 검측",
      "criterion_source": "KCS 14 31 05·20"}, S)
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_14_31_ut_01",
     {"name_ko": "용접부 UT 검사 판정",
      "criterion_source": "KCS 14 31 20 / KS B 0896"},
     "KCS 14 31 20")
node("decision", "WorkPermitDecision",
     "decision_kcs_14_31_hsb_permit_01",
     {"name_ko": "고장력볼트 본 조임 작업허가",
      "criterion_source": "KCS 14 31 25",
      "preconditions": ["마찰면 처리 완료",
                        "1차 조임·마킹 완료",
                        "강우·강설 없음"]},
     "KCS 14 31 25")
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_14_31_hsb_inspect_01",
     {"name_ko": "고장력볼트 토크·마킹 검사",
      "criterion_source": "KCS 14 31 25"},
     "KCS 14 31 25")
node("decision", "WorkPermitDecision",
     "decision_kcs_14_31_paint_permit_01",
     {"name_ko": "도장 작업허가 (온도·습도·풍속)",
      "criterion_source": "KCS 14 31 40"},
     "KCS 14 31 40")
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_14_31_paint_inspect_01",
     {"name_ko": "도장 외관·도막두께 검사",
      "criterion_source": "KCS 14 31 40"},
     "KCS 14 31 40")

# Outcomes
node("outcome", "DecisionOutcome", "outcome_kcs_14_31_pass_01",
     {"name_ko": "용접·볼트·도장 합격", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_14_31_rework_01",
     {"name_ko": "용접 재용접·볼트 재시공·도장 보수",
      "result": "rework"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_14_31_reject_01",
     {"name_ko": "용접부 불합격(부재 교체·재제작)",
      "result": "reject"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_14_31_stop_01",
     {"name_ko": "작업 중지(풍속·강우·기온)",
      "result": "work_stop"}, S)

# Authority + performs (UT inspector separately)
node("subject", "SiteEngineer", "kcs_14_31_ut_inspector_01",
     {"name_ko": "비파괴검사 기술자 (UT Lv.2 이상)",
      "duties": ["KS B 0896 UT 수행", "결함 등급 판정"]},
     "KCS 14 31 20")
edge("subject", "SiteEngineer:kcs_14_31_ut_inspector_01", "qualified_as",
     "concept", "Qualification:kcs_qual_ndt_ut_lvl2_01", "KCS 14 31 20")

node("subject", "SiteEngineer", "kcs_14_31_welder_01",
     {"name_ko": "용접기능자(승인시험 합격자)",
      "duties": ["승인된 절차서로 용접 수행"]}, "KCS 14 31 20")
edge("subject", "SiteEngineer:kcs_14_31_welder_01", "qualified_as",
     "concept", "Qualification:kcs_qual_welder_01", "KCS 14 31 20")

KCS1431_AUTH = {
    "MaterialReceiptDecision:decision_kcs_14_31_material_01":
        ("Qualification:kcs_qual_supervisor_01",
         "Supervisor:kcs_supervisor_01"),
    "StageApprovalDecision:decision_kcs_14_31_plan_approval_01":
        ("Qualification:kcs_qual_chief_supervisor_01",
         "ChiefSupervisor:kcs_chief_supervisor_01"),
    "WorkPermitDecision:decision_kcs_14_31_weld_permit_01":
        ("Qualification:kcs_qual_chief_supervisor_01",
         "ChiefSupervisor:kcs_chief_supervisor_01"),
    "ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01":
        ("Qualification:kcs_qual_supervisor_01",
         "Supervisor:kcs_supervisor_01"),
    "ConstructionInspectionDecision:decision_kcs_14_31_ut_01":
        ("Qualification:kcs_qual_ndt_ut_lvl2_01",
         "SiteEngineer:kcs_14_31_ut_inspector_01"),
    "WorkPermitDecision:decision_kcs_14_31_hsb_permit_01":
        ("Qualification:kcs_qual_chief_supervisor_01",
         "ChiefSupervisor:kcs_chief_supervisor_01"),
    "ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01":
        ("Qualification:kcs_qual_supervisor_01",
         "Supervisor:kcs_supervisor_01"),
    "WorkPermitDecision:decision_kcs_14_31_paint_permit_01":
        ("Qualification:kcs_qual_chief_supervisor_01",
         "ChiefSupervisor:kcs_chief_supervisor_01"),
    "ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01":
        ("Qualification:kcs_qual_supervisor_01",
         "Supervisor:kcs_supervisor_01"),
}
for d_id, (q, subj) in KCS1431_AUTH.items():
    edge("concept", q, "grants_authority_for", "decision", d_id, S)
    subj_space = "subject"
    edge(subj_space, subj, "performs", "decision", d_id, S)

KCS1431_BASED = {
    "MaterialReceiptDecision:decision_kcs_14_31_material_01":
        ["spec_kcs_14_31_main_01"],
    "StageApprovalDecision:decision_kcs_14_31_plan_approval_01":
        ["spec_kcs_14_31_main_01", "spec_kcs_14_31_precision_01"],
    "WorkPermitDecision:decision_kcs_14_31_weld_permit_01":
        ["spec_kcs_14_31_weld_env_01", "spec_kcs_14_31_preheat_01"],
    "ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01":
        ["spec_kcs_14_31_precision_01"],
    "ConstructionInspectionDecision:decision_kcs_14_31_ut_01":
        ["spec_kcs_14_31_ut_01", "spec_kcs_14_31_rework_limit_01"],
    "WorkPermitDecision:decision_kcs_14_31_hsb_permit_01":
        ["spec_kcs_14_31_hsb_01"],
    "ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01":
        ["spec_kcs_14_31_hsb_inspect_01", "spec_kcs_14_31_hsb_01"],
    "WorkPermitDecision:decision_kcs_14_31_paint_permit_01":
        ["spec_kcs_14_31_paint_01"],
    "ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01":
        ["spec_kcs_14_31_paint_01"],
}
for d_id, specs in KCS1431_BASED.items():
    for sp in specs:
        edge("decision", d_id, "based_on", "resource",
             f"Specification:{sp}", S)

# Targets
for d_id in [
    "WorkPermitDecision:decision_kcs_14_31_weld_permit_01",
    "ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01",
    "ConstructionInspectionDecision:decision_kcs_14_31_ut_01",
]:
    edge("decision", d_id, "targets_work_type", "concept",
         "WorkType:kcs_14_31_worktype_weld_01", "KCS 14 31 20")
    edge("decision", d_id, "targets_component", "concept",
         "StructuralComponent:kcs_14_31_component_weld_01", "KCS 14 31 20")

for d_id in [
    "WorkPermitDecision:decision_kcs_14_31_hsb_permit_01",
    "ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01",
]:
    edge("decision", d_id, "targets_work_type", "concept",
         "WorkType:kcs_14_31_worktype_hsb_01", "KCS 14 31 25")
    edge("decision", d_id, "targets_component", "concept",
         "StructuralComponent:kcs_14_31_component_bolt_01", "KCS 14 31 25")

for d_id in [
    "WorkPermitDecision:decision_kcs_14_31_paint_permit_01",
    "ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01",
]:
    edge("decision", d_id, "targets_work_type", "concept",
         "WorkType:kcs_14_31_worktype_paint_01", "KCS 14 31 40")
    edge("decision", d_id, "targets_component", "concept",
         "StructuralComponent:kcs_14_31_component_beam_01", "KCS 14 31 40")

edge("decision",
     "MaterialReceiptDecision:decision_kcs_14_31_material_01",
     "targets_work_type", "concept",
     "WorkType:kcs_14_31_worktype_steel_01", S)
edge("decision",
     "StageApprovalDecision:decision_kcs_14_31_plan_approval_01",
     "targets_work_type", "concept",
     "WorkType:kcs_14_31_worktype_steel_01", S)

# Yields outcomes
for d_id in KCS1431_AUTH:
    edge("decision", d_id, "yields", "outcome",
         "DecisionOutcome:outcome_kcs_14_31_pass_01", S)
    edge("decision", d_id, "yields", "outcome",
         "DecisionOutcome:outcome_kcs_14_31_rework_01", S)

edge("decision",
     "ConstructionInspectionDecision:decision_kcs_14_31_ut_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_14_31_reject_01", "KCS 14 31 20")
edge("decision",
     "WorkPermitDecision:decision_kcs_14_31_weld_permit_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_14_31_stop_01", "KCS 14 31 20")
edge("decision",
     "WorkPermitDecision:decision_kcs_14_31_paint_permit_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_14_31_stop_01", "KCS 14 31 40")

# Decision sequence
SEQ_1431 = [
    ("MaterialReceiptDecision:decision_kcs_14_31_material_01",
     "StageApprovalDecision:decision_kcs_14_31_plan_approval_01"),
    ("StageApprovalDecision:decision_kcs_14_31_plan_approval_01",
     "WorkPermitDecision:decision_kcs_14_31_weld_permit_01"),
    ("WorkPermitDecision:decision_kcs_14_31_weld_permit_01",
     "ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01"),
    ("ConstructionInspectionDecision:decision_kcs_14_31_weld_visual_01",
     "ConstructionInspectionDecision:decision_kcs_14_31_ut_01"),
    ("ConstructionInspectionDecision:decision_kcs_14_31_ut_01",
     "WorkPermitDecision:decision_kcs_14_31_hsb_permit_01"),
    ("WorkPermitDecision:decision_kcs_14_31_hsb_permit_01",
     "ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01"),
    ("ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01",
     "WorkPermitDecision:decision_kcs_14_31_paint_permit_01"),
    ("WorkPermitDecision:decision_kcs_14_31_paint_permit_01",
     "ConstructionInspectionDecision:decision_kcs_14_31_paint_inspect_01"),
]
for a, b in SEQ_1431:
    edge("decision", a, "precedes", "decision", b, S)
    edge("decision", b, "depends_on", "decision", a, S)


# =========================================================================
# KCS 21 50 — 거푸집·동바리 (해체 시기·하중·재시공)
# =========================================================================
S = "KCS 21 50"
node("concept", "WorkType", "kcs_21_50_worktype_formwork_01",
     {"name_ko": "거푸집·동바리 공사",
      "scope": "조립·점검·해체"}, S)
node("concept", "StructuralComponent", "kcs_21_50_component_form_01",
     {"name_ko": "거푸집(측벽·기둥·슬래브 밑면)"}, S)
node("concept", "StructuralComponent", "kcs_21_50_component_shore_01",
     {"name_ko": "동바리(파이프 서포트·시스템 동바리)"}, S)

node("resource", "Specification", "spec_kcs_21_50_main_01",
     {"name_ko": "KCS 21 50 거푸집 및 동바리 표준시방서",
      "standard_no": "KCS 21 50 00"}, S)
node("resource", "Specification", "spec_kcs_21_50_load_vert_01",
     {"name_ko": "연직 하중 (자중+작업하중+측압)",
      "standard_no": "KCS 21 50 05",
      "work_load_kN_per_m2": 1.5,
      "slab_thick_extra_above_m": 0.5,
      "pump_impact_pct_of_pressure": 50},
     "KCS 21 50 05")
node("resource", "Specification", "spec_kcs_21_50_pressure_01",
     {"name_ko": "콘크리트 측압 한계",
      "standard_no": "KCS 21 50 05",
      "max_pressure_kN_per_m2": 100,
      "formula": "P = w·H (수정식: R, T 보정)"},
     "KCS 21 50 05")
node("resource", "Specification", "spec_kcs_21_50_load_horiz_01",
     {"name_ko": "수평 하중·풍하중",
      "standard_no": "KCS 21 50 05",
      "horiz_load_min_pct_of_vert": 2,
      "horiz_load_min_kN_per_m": 1.5,
      "wind_load_reference": "KDS 41 12 00"},
     "KCS 21 50 05")
node("resource", "Specification", "spec_kcs_21_50_shore_safety_01",
     {"name_ko": "동바리 강도·좌굴 한계",
      "standard_no": "KCS 21 50 15",
      "safety_factor_min": 2.5,
      "pipe_shore_max_height_m": 3.5,
      "horizontal_brace_spacing_m": 2.0,
      "lateral_deflection_max": "H/200"},
     "KCS 21 50 15")
node("resource", "Specification", "spec_kcs_21_50_strip_strength_01",
     {"name_ko": "해체 시기 — 강도 기준",
      "standard_no": "KCS 21 50 10 / KCS 14 20 10",
      "side_form_min_MPa": 5,
      "simply_supported_min_fck_pct": 50,
      "simply_supported_min_MPa": 14,
      "continuous_min_fck_pct": 100,
      "cantilever_min_fck_pct": 100},
     "KCS 21 50 10")
node("resource", "Specification", "spec_kcs_21_50_strip_curing_01",
     {"name_ko": "해체 시기 — 양생 기간 환산 (보통포틀랜드시멘트)",
      "standard_no": "KCS 21 50 10",
      "T20_side_days": "1~2",
      "T20_simply_days": 8,
      "T20_continuous_days": 21,
      "T10_20_side_days": "2~3",
      "T10_20_simply_days": 14,
      "T10_20_continuous_days": 28,
      "T5_10_side_days": "3~4",
      "T5_10_simply_days": 20,
      "T5_10_continuous_days": 35},
     "KCS 21 50 10")
node("resource", "Specification", "spec_kcs_21_50_reuse_01",
     {"name_ko": "재사용 한도",
      "standard_no": "KCS 21 50 10",
      "timber_reuse_max": 7,
      "plywood_coated_reuse_max": 10,
      "steel_form_reuse_max": 100,
      "shore_pipe_max_strain_pct": 0.5},
     "KCS 21 50 10")
node("resource", "Specification", "spec_kcs_21_50_weather_stop_01",
     {"name_ko": "거푸집·동바리 시공 중 작업 중지 기상 한계",
      "standard_no": "KCS 21 50 05",
      "wind_stop_m_per_s": 10,
      "rain_stop": "작업발판 미끄럼 우려 시 중지",
      "snow_ice_stop": "결빙·적설 시 중지",
      "visibility_stop_m_below": 100},
     "KCS 21 50 05")
node("resource", "Specification", "spec_kcs_21_50_settle_check_01",
     {"name_ko": "동바리 침하·변형 한계",
      "standard_no": "KCS 21 50 15",
      "settlement_alarm_mm": 5,
      "inspection_after_wind_m_per_s": 10},
     "KCS 21 50 15")

# Decisions
node("decision", "StageApprovalDecision",
     "decision_kcs_21_50_form_plan_approval_01",
     {"name_ko": "거푸집·동바리 시공계획 승인",
      "criterion_source": "KCS 21 50 05 + 산안기준 제331조"}, S)
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_21_50_assembly_inspect_01",
     {"name_ko": "거푸집·동바리 조립 검측 (타설 전)",
      "criterion_source": "KCS 21 50 05·15"}, S)
node("decision", "SafetyInspectionDecision",
     "decision_kcs_21_50_safety_inspect_01",
     {"name_ko": "거푸집·동바리 안전 점검 (강풍·강진·강우 후)",
      "criterion_source": "KCS 21 50 05·15"}, S)
node("decision", "StageApprovalDecision",
     "decision_kcs_21_50_strip_approval_01",
     {"name_ko": "거푸집·동바리 해체 승인 (강도·양생 확인)",
      "criterion_source": "KCS 21 50 10 / KCS 14 20 10"},
     "KCS 21 50 10")
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_21_50_post_strip_inspect_01",
     {"name_ko": "해체 직후 부재 검측 (침하·균열·처짐)",
      "criterion_source": "KCS 21 50 10"},
     "KCS 21 50 10")

node("outcome", "DecisionOutcome", "outcome_kcs_21_50_pass_01",
     {"name_ko": "거푸집·동바리 합격", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_21_50_rework_01",
     {"name_ko": "재조립·보강", "result": "rework"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_21_50_stop_01",
     {"name_ko": "작업 중지(풍속·강진·강우)",
      "result": "work_stop"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_21_50_redo_pour_01",
     {"name_ko": "재타설·부재 보강 (해체 후 침하·균열)",
      "result": "rework"}, "KCS 21 50 10")

KCS2150_AUTH = {
    "StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01":
        ("Qualification:kcs_qual_chief_supervisor_01",
         "ChiefSupervisor:kcs_chief_supervisor_01"),
    "ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01":
        ("Qualification:kcs_qual_supervisor_01",
         "Supervisor:kcs_supervisor_01"),
    "SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01":
        ("Qualification:kcs_qual_safety_manager_01",
         "SafetyManager:kcs_safety_manager_01"),
    "StageApprovalDecision:decision_kcs_21_50_strip_approval_01":
        ("Qualification:kcs_qual_chief_supervisor_01",
         "ChiefSupervisor:kcs_chief_supervisor_01"),
    "ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01":
        ("Qualification:kcs_qual_supervisor_01",
         "Supervisor:kcs_supervisor_01"),
}
for d_id, (q, subj) in KCS2150_AUTH.items():
    edge("concept", q, "grants_authority_for", "decision", d_id, S)
    edge("subject", subj, "performs", "decision", d_id, S)

KCS2150_BASED = {
    "StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01":
        ["spec_kcs_21_50_main_01", "spec_kcs_21_50_load_vert_01",
         "spec_kcs_21_50_pressure_01", "spec_kcs_21_50_load_horiz_01",
         "spec_kcs_21_50_shore_safety_01"],
    "ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01":
        ["spec_kcs_21_50_shore_safety_01", "spec_kcs_21_50_settle_check_01"],
    "SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01":
        ["spec_kcs_21_50_weather_stop_01",
         "spec_kcs_21_50_settle_check_01"],
    "StageApprovalDecision:decision_kcs_21_50_strip_approval_01":
        ["spec_kcs_21_50_strip_strength_01",
         "spec_kcs_21_50_strip_curing_01",
         "spec_kcs_21_50_reuse_01"],
    "ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01":
        ["spec_kcs_21_50_strip_strength_01"],
}
for d_id, specs in KCS2150_BASED.items():
    for sp in specs:
        edge("decision", d_id, "based_on", "resource",
             f"Specification:{sp}", S)

for d_id in KCS2150_AUTH:
    edge("decision", d_id, "targets_work_type", "concept",
         "WorkType:kcs_21_50_worktype_formwork_01", S)

edge("decision",
     "ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_21_50_component_form_01", S)
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_21_50_component_shore_01", S)
edge("decision",
     "StageApprovalDecision:decision_kcs_21_50_strip_approval_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_21_50_component_form_01",
     "KCS 21 50 10")
edge("decision",
     "StageApprovalDecision:decision_kcs_21_50_strip_approval_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_21_50_component_shore_01",
     "KCS 21 50 10")

for d_id in KCS2150_AUTH:
    edge("decision", d_id, "yields", "outcome",
         "DecisionOutcome:outcome_kcs_21_50_pass_01", S)
    edge("decision", d_id, "yields", "outcome",
         "DecisionOutcome:outcome_kcs_21_50_rework_01", S)
edge("decision",
     "SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_21_50_stop_01", S)
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_21_50_redo_pour_01", "KCS 21 50 10")

SEQ_2150 = [
    ("StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01",
     "ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01"),
    ("ConstructionInspectionDecision:decision_kcs_21_50_assembly_inspect_01",
     "StageApprovalDecision:decision_kcs_21_50_strip_approval_01"),
    ("StageApprovalDecision:decision_kcs_21_50_strip_approval_01",
     "ConstructionInspectionDecision:decision_kcs_21_50_post_strip_inspect_01"),
]
for a, b in SEQ_2150:
    edge("decision", a, "precedes", "decision", b, S)
    edge("decision", b, "depends_on", "decision", a, S)

# Cross-code link: KCS 21 50 strip approval depends on KCS 14 20 strength test
edge("decision",
     "StageApprovalDecision:decision_kcs_21_50_strip_approval_01",
     "depends_on", "decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01",
     "KCS 21 50 10 / KCS 14 20 10")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01",
     "precedes", "decision",
     "StageApprovalDecision:decision_kcs_21_50_strip_approval_01",
     "KCS 21 50 10 / KCS 14 20 10")

# Cross-code: KCS 21 50 form plan approval precedes KCS 14 20 pour permit
edge("decision",
     "StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01",
     "precedes", "decision",
     "WorkPermitDecision:decision_kcs_14_20_pour_permit_01",
     "KCS 21 50 / KCS 14 20")
edge("decision",
     "WorkPermitDecision:decision_kcs_14_20_pour_permit_01",
     "depends_on", "decision",
     "StageApprovalDecision:decision_kcs_21_50_form_plan_approval_01",
     "KCS 21 50 / KCS 14 20")


# =========================================================================
# KCS 11 30 — 연약지반 (압밀·계측·한계)
# =========================================================================
S = "KCS 11 30"
node("concept", "WorkType", "kcs_11_30_worktype_softground_01",
     {"name_ko": "연약지반 처리·압밀공사",
      "scope": "압밀·치환·고결·다짐"}, S)
node("concept", "WorkType", "kcs_11_30_worktype_pbd_01",
     {"name_ko": "연직배수공법(PBD/SD)"}, "KCS 11 30 10")
node("concept", "Facility", "kcs_11_30_facility_embankment_01",
     {"name_ko": "성토부(연약지반)",
      "scope": "도로·철도 노반·교대 접속부"}, S)
node("concept", "StructuralComponent", "kcs_11_30_component_pbd_01",
     {"name_ko": "PBD(Plastic Board Drain)"},
     "KCS 11 30 10")
edge("concept", "WorkType:kcs_11_30_worktype_pbd_01", "subclass_of",
     "concept", "WorkType:kcs_11_30_worktype_softground_01",
     "KCS 11 30 10")

node("resource", "Specification", "spec_kcs_11_30_main_01",
     {"name_ko": "KCS 11 30 연약지반 표준시방서",
      "standard_no": "KCS 11 30 00"}, S)
node("resource", "Specification", "spec_kcs_11_30_settle_limit_01",
     {"name_ko": "잔류침하 허용 한계",
      "standard_no": "KCS 11 30 05",
      "road_general_max_cm": 30,
      "bridge_abutment_max_cm": 10,
      "rail_high_speed_max_cm": 3,
      "rail_general_max_cm": 10},
     "KCS 11 30 05")
node("resource", "Specification", "spec_kcs_11_30_construction_limit_01",
     {"name_ko": "시공 중 침하·변형 한계",
      "standard_no": "KCS 11 30 05",
      "daily_settle_stop_cm_per_day": 1.0,
      "daily_lateral_max_cm_per_day": 0.5},
     "KCS 11 30 05")
node("resource", "Specification", "spec_kcs_11_30_consolidation_judge_01",
     {"name_ko": "압밀 완료 판정",
      "standard_no": "KCS 11 30 05",
      "structure_U_pct_min": 90,
      "bridge_abutment_U_pct_min": 95,
      "methods": ["Hyperbolic", "Asaoka"],
      "hyperbolic_valid_above_pct": 60},
     "KCS 11 30 05")
node("resource", "Specification", "spec_kcs_11_30_pbd_01",
     {"name_ko": "PBD 사양·간격",
      "standard_no": "KCS 11 30 10",
      "pbd_width_min_mm": 100,
      "discharge_min_cm3_per_s": 100,
      "depth_overlap_m": 1,
      "spacing_min_m": 1.0,
      "spacing_max_m": 1.5,
      "depth_practical_max_m": 30},
     "KCS 11 30 10")
node("resource", "Specification", "spec_kcs_11_30_stability_01",
     {"name_ko": "성토 사면 안정 안전율",
      "standard_no": "KCS 11 30 05",
      "construction_min_FS": 1.2,
      "permanent_min_FS": 1.5,
      "seismic_min_FS": 1.0,
      "stage_lift_height_m": "1.5~2.0",
      "next_stage_U_pct_min": 70},
     "KCS 11 30 05")
node("resource", "Specification", "spec_kcs_11_30_monitor_freq_01",
     {"name_ko": "계측 빈도",
      "standard_no": "KCS 11 30 30",
      "construction_freq": "1일 1회 (성토 1m마다)",
      "early_post_freq": "주 2~3회 (성토 완료 후 6개월)",
      "late_post_freq": "월 1~2회",
      "items": ["침하판", "층별 침하계", "간극수압계",
                "지중 경사계", "토압계"]},
     "KCS 11 30 30")
node("resource", "Specification", "spec_kcs_11_30_alarm_01",
     {"name_ko": "3단계 계측 관리 기준",
      "standard_no": "KCS 11 30 30",
      "yellow_pct_of_predict": 70,
      "yellow_daily_cm": 1.0,
      "orange_pct_of_predict": 85,
      "orange_daily_cm": 1.5,
      "red_pct_of_predict": 100,
      "red_daily_cm": 2.0,
      "action_on_red": "성토 중지·전문가 검토"},
     "KCS 11 30 30")
node("resource", "Specification", "spec_kcs_11_30_replace_01",
     {"name_ko": "치환공법 적용 한계",
      "standard_no": "KCS 11 30 15",
      "soft_layer_max_m": 5},
     "KCS 11 30 15")
node("resource", "Specification", "spec_kcs_11_30_dmm_01",
     {"name_ko": "심층혼합처리 (DMM) 설계강도",
      "standard_no": "KCS 11 30 20",
      "design_strength_28d_MPa_min": 1.0},
     "KCS 11 30 20")
node("resource", "Specification", "spec_kcs_11_30_compaction_01",
     {"name_ko": "다짐공법 (SCP·진동다짐) 검측 기준",
      "standard_no": "KCS 11 30 25",
      "relative_density_min_pct": 70,
      "applicable_soil": "사질토",
      "verification": "N치 증가량 측정"},
     "KCS 11 30 25")
node("resource", "Specification", "spec_kcs_11_30_sand_drain_01",
     {"name_ko": "샌드드레인(SD) 사양",
      "standard_no": "KCS 11 30 10",
      "diameter_mm": 400,
      "spacing_m_range": "2.0 ~ 3.0"},
     "KCS 11 30 10")
edge("decision",
     "StageApprovalDecision:decision_kcs_11_30_plan_approval_01",
     "based_on", "resource",
     "Specification:spec_kcs_11_30_dmm_01", "KCS 11 30 20")
edge("decision",
     "StageApprovalDecision:decision_kcs_11_30_plan_approval_01",
     "based_on", "resource",
     "Specification:spec_kcs_11_30_replace_01", "KCS 11 30 15")
edge("decision",
     "StageApprovalDecision:decision_kcs_11_30_plan_approval_01",
     "based_on", "resource",
     "Specification:spec_kcs_11_30_compaction_01", "KCS 11 30 25")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01",
     "based_on", "resource",
     "Specification:spec_kcs_11_30_sand_drain_01", "KCS 11 30 10")

node("decision", "StageApprovalDecision",
     "decision_kcs_11_30_plan_approval_01",
     {"name_ko": "연약지반 처리 시공계획 승인",
      "criterion_source": "KCS 11 30 05"}, S)
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_11_30_pbd_inspect_01",
     {"name_ko": "PBD 시공 검측 (간격·깊이·통수능)",
      "criterion_source": "KCS 11 30 10"},
     "KCS 11 30 10")
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_11_30_monitor_inspect_01",
     {"name_ko": "계측 결과 검측·관리 단계 판정",
      "criterion_source": "KCS 11 30 30"},
     "KCS 11 30 30")
node("decision", "StageApprovalDecision",
     "decision_kcs_11_30_consolidation_approval_01",
     {"name_ko": "압밀 완료 판정·다음 공정 승인",
      "criterion_source": "KCS 11 30 05"},
     "KCS 11 30 05")
node("decision", "SafetyInspectionDecision",
     "decision_kcs_11_30_safety_stop_01",
     {"name_ko": "성토 중지 결정 (1일 침하 한계 초과)",
      "criterion_source": "KCS 11 30 30"},
     "KCS 11 30 30")

node("outcome", "DecisionOutcome", "outcome_kcs_11_30_pass_01",
     {"name_ko": "압밀 완료·다음 공정 진행", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_11_30_wait_01",
     {"name_ko": "압밀 대기·추가 계측",
      "result": "hold"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_11_30_stop_01",
     {"name_ko": "성토 중지(관리 기준 초과)",
      "result": "work_stop"}, S)

KCS1130_AUTH = {
    "StageApprovalDecision:decision_kcs_11_30_plan_approval_01":
        ("Qualification:kcs_qual_chief_supervisor_01",
         "ChiefSupervisor:kcs_chief_supervisor_01"),
    "ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01":
        ("Qualification:kcs_qual_supervisor_01",
         "Supervisor:kcs_supervisor_01"),
    "ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01":
        ("Qualification:kcs_qual_supervisor_01",
         "Supervisor:kcs_supervisor_01"),
    "StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01":
        ("Qualification:kcs_qual_chief_supervisor_01",
         "ChiefSupervisor:kcs_chief_supervisor_01"),
    "SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01":
        ("Qualification:kcs_qual_safety_manager_01",
         "SafetyManager:kcs_safety_manager_01"),
}
for d_id, (q, subj) in KCS1130_AUTH.items():
    edge("concept", q, "grants_authority_for", "decision", d_id, S)
    edge("subject", subj, "performs", "decision", d_id, S)

# Soil/Geo expert role (subject)
node("subject", "SiteEngineer", "kcs_11_30_geo_engineer_01",
     {"name_ko": "토질·지반 기술자",
      "duties": ["압밀 예측", "안정해석", "계측 해석"]}, S)
edge("subject", "SiteEngineer:kcs_11_30_geo_engineer_01", "qualified_as",
     "concept", "Qualification:kcs_qual_soil_geo_01", S)
edge("subject", "SiteEngineer:kcs_11_30_geo_engineer_01", "performs",
     "decision",
     "ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01",
     S)
edge("concept", "Qualification:kcs_qual_soil_geo_01",
     "grants_authority_for", "decision",
     "ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01",
     S)

KCS1130_BASED = {
    "StageApprovalDecision:decision_kcs_11_30_plan_approval_01":
        ["spec_kcs_11_30_main_01", "spec_kcs_11_30_settle_limit_01",
         "spec_kcs_11_30_stability_01"],
    "ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01":
        ["spec_kcs_11_30_pbd_01"],
    "ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01":
        ["spec_kcs_11_30_monitor_freq_01", "spec_kcs_11_30_alarm_01",
         "spec_kcs_11_30_construction_limit_01"],
    "StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01":
        ["spec_kcs_11_30_consolidation_judge_01",
         "spec_kcs_11_30_settle_limit_01"],
    "SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01":
        ["spec_kcs_11_30_construction_limit_01",
         "spec_kcs_11_30_alarm_01"],
}
for d_id, specs in KCS1130_BASED.items():
    for sp in specs:
        edge("decision", d_id, "based_on", "resource",
             f"Specification:{sp}", S)

for d_id in KCS1130_AUTH:
    edge("decision", d_id, "targets_work_type", "concept",
         "WorkType:kcs_11_30_worktype_softground_01", S)
    edge("decision", d_id, "targets_facility", "concept",
         "Facility:kcs_11_30_facility_embankment_01", S)

edge("decision",
     "ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_11_30_component_pbd_01", "KCS 11 30 10")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01",
     "targets_work_type", "concept",
     "WorkType:kcs_11_30_worktype_pbd_01", "KCS 11 30 10")

for d_id in KCS1130_AUTH:
    edge("decision", d_id, "yields", "outcome",
         "DecisionOutcome:outcome_kcs_11_30_pass_01", S)
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_11_30_wait_01", "KCS 11 30 30")
edge("decision",
     "SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_11_30_stop_01", "KCS 11 30 30")
edge("decision",
     "StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_11_30_wait_01", "KCS 11 30 05")

SEQ_1130 = [
    ("StageApprovalDecision:decision_kcs_11_30_plan_approval_01",
     "ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01"),
    ("ConstructionInspectionDecision:decision_kcs_11_30_pbd_inspect_01",
     "ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01"),
    ("ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01",
     "StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01"),
    ("ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01",
     "SafetyInspectionDecision:decision_kcs_11_30_safety_stop_01"),
]
for a, b in SEQ_1130:
    edge("decision", a, "precedes", "decision", b, S)
    edge("decision", b, "depends_on", "decision", a, S)


# =========================================================================
# KCS 21 60 — 비계·가시설 (풍속·강우·작업중지·점검)
# =========================================================================
S = "KCS 21 60"
node("concept", "WorkType", "kcs_21_60_worktype_scaffold_01",
     {"name_ko": "비계·가시설 공사",
      "scope": "강관·시스템·달비계·작업발판"}, S)
node("concept", "Facility", "kcs_21_60_facility_scaffold_01",
     {"name_ko": "비계 구조물",
      "lifecycle": "가설(시공 중)"}, S)
node("concept", "StructuralComponent", "kcs_21_60_component_pipe_01",
     {"name_ko": "강관 비계(48.6mm/2.4t)"}, "KCS 21 60 10")
node("concept", "StructuralComponent", "kcs_21_60_component_platform_01",
     {"name_ko": "작업발판·발끝막이판"},
     "KCS 21 60 25")

node("resource", "Specification", "spec_kcs_21_60_main_01",
     {"name_ko": "KCS 21 60 비계 표준시방서",
      "standard_no": "KCS 21 60 00"}, S)
node("resource", "Specification", "spec_kcs_21_60_load_01",
     {"name_ko": "비계 작업하중·안전율",
      "standard_no": "KCS 21 60 05",
      "work_load_kN_per_m2": 2.5,
      "material_load_kN_per_m2": 4.0,
      "pipe_safety_factor_min": 4.0,
      "wire_safety_factor_min": 10.0},
     "KCS 21 60 05")
node("resource", "Specification", "spec_kcs_21_60_pipe_assembly_01",
     {"name_ko": "강관 비계 조립 한계",
      "standard_no": "KCS 21 60 10",
      "post_spacing_band_max_m": 1.85,
      "post_spacing_joist_max_m": 1.5,
      "band_height_max_m": 1.5,
      "first_band_height_max_m": 2.0,
      "wall_tie_vertical_max_m": 5,
      "wall_tie_horizontal_max_m": 5},
     "KCS 21 60 10")
node("resource", "Specification", "spec_kcs_21_60_platform_01",
     {"name_ko": "작업발판·안전난간 한계",
      "standard_no": "KCS 21 60 25",
      "platform_width_min_cm": 40,
      "platform_gap_max_cm": 3,
      "platform_to_wall_max_cm": 30,
      "toe_board_min_cm": 10,
      "guardrail_top_cm": "90~120",
      "guardrail_mid_cm": "45~60",
      "guardrail_force_kgf": 100,
      "fall_net_mesh_max_cm": 10},
     "KCS 21 60 25")
node("resource", "Specification", "spec_kcs_21_60_wind_stop_01",
     {"name_ko": "풍속 작업 중지 기준",
      "standard_no": "KCS 21 60 05 + 산안기준",
      "assembly_stop_m_per_s": 10,
      "all_work_stop_m_per_s": 15,
      "warning_average_m_per_s": 14,
      "warning_gust_m_per_s": 20,
      "post_event_inspect_above_m_per_s": 10},
     "KCS 21 60 05")
node("resource", "Specification", "spec_kcs_21_60_rain_snow_stop_01",
     {"name_ko": "강우·강설 작업 중지 기준",
      "standard_no": "KCS 21 60 05 + 산안기준",
      "rain_stop_mm_per_h": 1,
      "rain_daily_stop_mm": 25,
      "snow_stop_cm_per_h": 1,
      "snow_accum_stop_cm": 10,
      "icing_rule": "결빙·미끄럼 시 즉시 중지"},
     "KCS 21 60 05")
node("resource", "Specification", "spec_kcs_21_60_visibility_stop_01",
     {"name_ko": "야간·시야 작업 한계",
      "standard_no": "KCS 21 60 05 + 산안기준",
      "visibility_stop_m_below": 100,
      "night_lux_min": 75,
      "seismic_intensity_stop_min": 5},
     "KCS 21 60 05")
node("resource", "Specification", "spec_kcs_21_60_inspection_freq_01",
     {"name_ko": "비계 점검 주기",
      "standard_no": "KCS 21 60 05",
      "daily_before_work": "매일 작업 시작 전",
      "weekly": "주 1회 정기 (감리자 입회)",
      "post_wind_threshold_m_per_s": 10,
      "post_rain_24h_threshold_mm": 50,
      "post_seismic_threshold": "진도 4 이상",
      "long_idle_reuse_days_min": 30},
     "KCS 21 60 05")
node("resource", "Specification", "spec_kcs_21_60_mobile_scaffold_01",
     {"name_ko": "달비계·이동비계·말비계 한계",
      "standard_no": "KCS 21 60 20·25",
      "mobile_height_base_ratio_max": 4,
      "mobile_during_move_rule": "이동·승강 중 사용 금지",
      "ladder_scaffold_max_height_m": 2},
     "KCS 21 60 20")
node("resource", "Specification", "spec_kcs_21_60_falling_net_01",
     {"name_ko": "낙하물방지망 설치 기준",
      "standard_no": "KCS 21 60 05",
      "first_height_max_m": 10,
      "vertical_interval_max_m": 10,
      "extrusion_min_m": 2},
     "KCS 21 60 05")
node("resource", "Specification", "spec_kcs_21_60_system_brace_01",
     {"name_ko": "벽이음·버팀·가새 한계",
      "standard_no": "KCS 21 60 10",
      "wall_tie_vertical_max_m": 5,
      "wall_tie_horizontal_max_m": 5,
      "diagonal_angle_deg": 45},
     "KCS 21 60 10")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01",
     "based_on", "resource",
     "Specification:spec_kcs_21_60_falling_net_01", "KCS 21 60 05")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01",
     "based_on", "resource",
     "Specification:spec_kcs_21_60_system_brace_01", "KCS 21 60 10")

# Decisions
node("decision", "StageApprovalDecision",
     "decision_kcs_21_60_plan_approval_01",
     {"name_ko": "비계·가시설 시공계획 승인",
      "criterion_source": "KCS 21 60 05"}, S)
node("decision", "ConstructionInspectionDecision",
     "decision_kcs_21_60_assembly_inspect_01",
     {"name_ko": "비계 조립 검측 (간격·벽이음·안전난간)",
      "criterion_source": "KCS 21 60 10·25"}, S)
node("decision", "SafetyInspectionDecision",
     "decision_kcs_21_60_daily_inspect_01",
     {"name_ko": "비계 일상 점검 (매일 작업 전)",
      "criterion_source": "KCS 21 60 05"}, S)
node("decision", "SafetyInspectionDecision",
     "decision_kcs_21_60_post_event_inspect_01",
     {"name_ko": "강풍·강우·지진 후 임시 점검",
      "criterion_source": "KCS 21 60 05"}, S)
node("decision", "WorkPermitDecision",
     "decision_kcs_21_60_work_permit_01",
     {"name_ko": "비계 작업 허가 (풍속·강우·시야)",
      "criterion_source": "KCS 21 60 05 + 산안기준",
      "stop_triggers": ["풍속 10m/s 이상",
                        "강우 1mm/h 이상",
                        "강설 1cm/h 이상 또는 적설 10cm",
                        "가시거리 100m 이하",
                        "진도 5 이상"]}, S)

node("outcome", "DecisionOutcome", "outcome_kcs_21_60_pass_01",
     {"name_ko": "비계 합격·작업 허가", "result": "pass"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_21_60_rework_01",
     {"name_ko": "비계 재조립·보강", "result": "rework"}, S)
node("outcome", "DecisionOutcome", "outcome_kcs_21_60_stop_01",
     {"name_ko": "비계 작업 중지(풍속·강우·시야·지진)",
      "result": "work_stop"}, S)

KCS2160_AUTH = {
    "StageApprovalDecision:decision_kcs_21_60_plan_approval_01":
        ("Qualification:kcs_qual_chief_supervisor_01",
         "ChiefSupervisor:kcs_chief_supervisor_01"),
    "ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01":
        ("Qualification:kcs_qual_supervisor_01",
         "Supervisor:kcs_supervisor_01"),
    "SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01":
        ("Qualification:kcs_qual_safety_manager_01",
         "SafetyManager:kcs_safety_manager_01"),
    "SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01":
        ("Qualification:kcs_qual_safety_manager_01",
         "SafetyManager:kcs_safety_manager_01"),
    "WorkPermitDecision:decision_kcs_21_60_work_permit_01":
        ("Qualification:kcs_qual_safety_manager_01",
         "SafetyManager:kcs_safety_manager_01"),
}
for d_id, (q, subj) in KCS2160_AUTH.items():
    edge("concept", q, "grants_authority_for", "decision", d_id, S)
    edge("subject", subj, "performs", "decision", d_id, S)

KCS2160_BASED = {
    "StageApprovalDecision:decision_kcs_21_60_plan_approval_01":
        ["spec_kcs_21_60_main_01", "spec_kcs_21_60_load_01",
         "spec_kcs_21_60_pipe_assembly_01",
         "spec_kcs_21_60_mobile_scaffold_01"],
    "ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01":
        ["spec_kcs_21_60_pipe_assembly_01",
         "spec_kcs_21_60_platform_01",
         "spec_kcs_21_60_inspection_freq_01"],
    "SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01":
        ["spec_kcs_21_60_inspection_freq_01"],
    "SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01":
        ["spec_kcs_21_60_inspection_freq_01",
         "spec_kcs_21_60_wind_stop_01",
         "spec_kcs_21_60_rain_snow_stop_01"],
    "WorkPermitDecision:decision_kcs_21_60_work_permit_01":
        ["spec_kcs_21_60_wind_stop_01",
         "spec_kcs_21_60_rain_snow_stop_01",
         "spec_kcs_21_60_visibility_stop_01"],
}
for d_id, specs in KCS2160_BASED.items():
    for sp in specs:
        edge("decision", d_id, "based_on", "resource",
             f"Specification:{sp}", S)

for d_id in KCS2160_AUTH:
    edge("decision", d_id, "targets_work_type", "concept",
         "WorkType:kcs_21_60_worktype_scaffold_01", S)
    edge("decision", d_id, "targets_facility", "concept",
         "Facility:kcs_21_60_facility_scaffold_01", S)

edge("decision",
     "ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_21_60_component_pipe_01", "KCS 21 60 10")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01",
     "targets_component", "concept",
     "StructuralComponent:kcs_21_60_component_platform_01",
     "KCS 21 60 25")

for d_id in KCS2160_AUTH:
    edge("decision", d_id, "yields", "outcome",
         "DecisionOutcome:outcome_kcs_21_60_pass_01", S)
    edge("decision", d_id, "yields", "outcome",
         "DecisionOutcome:outcome_kcs_21_60_rework_01", S)
edge("decision",
     "WorkPermitDecision:decision_kcs_21_60_work_permit_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_21_60_stop_01", S)
edge("decision",
     "SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_21_60_stop_01", S)
edge("decision",
     "SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01",
     "yields", "outcome",
     "DecisionOutcome:outcome_kcs_21_60_stop_01", S)

SEQ_2160 = [
    ("StageApprovalDecision:decision_kcs_21_60_plan_approval_01",
     "ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01"),
    ("ConstructionInspectionDecision:decision_kcs_21_60_assembly_inspect_01",
     "SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01"),
    ("SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01",
     "WorkPermitDecision:decision_kcs_21_60_work_permit_01"),
    ("SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01",
     "WorkPermitDecision:decision_kcs_21_60_work_permit_01"),
]
for a, b in SEQ_2160:
    edge("decision", a, "precedes", "decision", b, S)
    edge("decision", b, "depends_on", "decision", a, S)


# =========================================================================
# Shared resources -> decision based_on wiring
# =========================================================================
# KCS 14 20: pour permit references checklist + work permit
edge("decision",
     "WorkPermitDecision:decision_kcs_14_20_pour_permit_01",
     "based_on", "resource",
     "Checklist:checklist_kcs_pre_pour_01", "KCS 14 20 10")
edge("decision",
     "WorkPermitDecision:decision_kcs_14_20_pour_permit_01",
     "based_on", "resource",
     "WorkPermit:permit_kcs_pour_01", "KCS 14 20 10")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_pour_inspection_01",
     "based_on", "resource",
     "ConstructionLog:log_kcs_construction_01", "KCS 14 20 10")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_14_20_strength_test_01",
     "based_on", "resource",
     "TestReport:test_kcs_strength_report_01", "KCS 14 20 10")

# KCS 21 50: strip approval references checklist + log
edge("decision",
     "StageApprovalDecision:decision_kcs_21_50_strip_approval_01",
     "based_on", "resource",
     "Checklist:checklist_kcs_form_strip_01", "KCS 21 50 10")
edge("decision",
     "StageApprovalDecision:decision_kcs_21_50_strip_approval_01",
     "based_on", "resource",
     "SupervisionLog:log_kcs_supervision_01", "KCS 21 50 10")
edge("decision",
     "SafetyInspectionDecision:decision_kcs_21_50_safety_inspect_01",
     "based_on", "resource",
     "SafetyInspectionReport:safety_kcs_formwork_report_01",
     "KCS 21 50 15")

# KCS 14 31: weld permit + UT
edge("decision",
     "WorkPermitDecision:decision_kcs_14_31_weld_permit_01",
     "based_on", "resource",
     "Checklist:checklist_kcs_weld_pre_01", "KCS 14 31 20")
edge("decision",
     "WorkPermitDecision:decision_kcs_14_31_weld_permit_01",
     "based_on", "resource",
     "WorkPermit:permit_kcs_weld_01", "KCS 14 31 20")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_14_31_ut_01",
     "based_on", "resource",
     "TestReport:test_kcs_ut_report_01", "KCS 14 31 20")
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_14_31_hsb_inspect_01",
     "based_on", "resource",
     "TestReport:test_kcs_torque_report_01", "KCS 14 31 25")

# KCS 11 30: monitoring report
edge("decision",
     "ConstructionInspectionDecision:decision_kcs_11_30_monitor_inspect_01",
     "based_on", "resource",
     "TestReport:test_kcs_monitoring_report_01", "KCS 11 30 30")
edge("decision",
     "StageApprovalDecision:decision_kcs_11_30_consolidation_approval_01",
     "based_on", "resource",
     "TestReport:test_kcs_monitoring_report_01", "KCS 11 30 30")

# KCS 21 60: daily/post-event/work permit
edge("decision",
     "SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01",
     "based_on", "resource",
     "Checklist:checklist_kcs_scaffold_daily_01", "KCS 21 60 05")
edge("decision",
     "SafetyInspectionDecision:decision_kcs_21_60_daily_inspect_01",
     "based_on", "resource",
     "SafetyInspectionReport:safety_kcs_scaffold_report_01",
     "KCS 21 60 05")
edge("decision",
     "SafetyInspectionDecision:decision_kcs_21_60_post_event_inspect_01",
     "based_on", "resource",
     "SafetyInspectionReport:safety_kcs_scaffold_report_01",
     "KCS 21 60 05")
edge("decision",
     "WorkPermitDecision:decision_kcs_21_60_work_permit_01",
     "based_on", "resource",
     "WorkPermit:permit_kcs_scaffold_01", "KCS 21 60 05")


# =========================================================================
# Write
# =========================================================================
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

# =========================================================================
# Validate against manifest
# =========================================================================
from collections import Counter
SPACES = {
    "subject": {"User", "Team", "Org", "Agent", "Supervisor",
                "ChiefSupervisor", "SiteEngineer", "SafetyManager",
                "ChiefSafetyInspector", "ChiefPrecisionDiagnoser"},
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
    "decision": {"MaterialReceiptDecision",
                 "ConstructionInspectionDecision",
                 "WorkPermitDecision", "StageApprovalDecision",
                 "SafetyInspectionDecision",
                 "PrecisionDiagnosisDecision"},
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
            errors.append(
                f"BAD (space, type): ({sp}, {nt}) for {r['node_id']}")
        nodes_by_id[r["node_id"]] = sp
        type_counter[f"{sp}/{nt}"] += 1

for r in records:
    if r["kind"] == "edge":
        fs, ts = r["from_space"], r["to_space"]
        rel = r["relation"]
        if rel not in META.get((fs, ts), set()):
            errors.append(
                f"BAD edge ({fs}, {ts}, {rel}) "
                f"{r['from_id']} -> {r['to_id']}"
            )
        if r["from_id"] not in nodes_by_id:
            errors.append(f"ORPHAN from: {r['from_id']}")
        if r["to_id"] not in nodes_by_id:
            errors.append(f"ORPHAN to: {r['to_id']}")
        relation_counter[rel] += 1

n_nodes = sum(1 for r in records if r["kind"] == "node")
n_edges = sum(1 for r in records if r["kind"] == "edge")

print(f"OUT={OUT}")
print(f"records={len(records)} nodes={n_nodes} "
      f"edges={n_edges} errors={len(errors)}")
if errors:
    for e in errors[:50]:
        print("  ERR:", e)
print("\nTypes (space/type → count):")
for k, v in sorted(type_counter.items()):
    print(f"  {k}: {v}")
print("\nRelations:")
for k, v in sorted(relation_counter.items()):
    print(f"  {k}: {v}")
print(f"\nFile size: {os.path.getsize(OUT)} bytes")
