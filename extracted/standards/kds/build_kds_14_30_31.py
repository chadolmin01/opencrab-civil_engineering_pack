"""Build OpenCRAB JSONL for KDS 14 30 (강구조 설계 — 허용응력설계법) and KDS 14 31 (강구조 시공).

Pure domain content only. No publishing/event/SNS/marketing tone.
Grammar: every (space, node_type) must be in SPACES; every edge (from, to, rel) in META_EDGES.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Grammar enforcement (mirrors opencrab/grammar/manifest.py)
# ---------------------------------------------------------------------------

SPACES: dict[str, list[str]] = {
    "subject": [
        "User", "Team", "Org", "Agent",
        "Supervisor", "ChiefSupervisor", "SiteEngineer", "SafetyManager",
        "ChiefSafetyInspector", "ChiefPrecisionDiagnoser",
    ],
    "resource": [
        "Project", "Document", "File", "Dataset", "Tool", "API", "CrawlRun",
        "Drawing", "Specification", "Checklist", "TestReport", "WorkPermit",
        "ConstructionLog", "SupervisionLog", "MaterialReceiptReport",
        "SafetyInspectionReport",
    ],
    "evidence": ["TextUnit", "LogEntry", "Evidence"],
    "concept": [
        "Entity", "Concept", "Topic", "Class",
        "Qualification", "StructuralComponent", "WorkType", "Facility",
    ],
    "claim": ["Claim", "Covariate", "CollectionCompleteness"],
    "community": ["Community", "CommunityReport"],
    "decision": [
        "MaterialReceiptDecision", "ConstructionInspectionDecision",
        "WorkPermitDecision", "StageApprovalDecision",
        "SafetyInspectionDecision", "PrecisionDiagnosisDecision",
    ],
    "outcome": ["Outcome", "KPI", "Risk", "DecisionOutcome"],
    "lever": ["Lever"],
    "policy": ["Policy", "Sensitivity", "ApprovalRule"],
}

META_EDGES: list[tuple[str, str, set[str]]] = [
    ("subject", "resource", {"owns", "member_of", "manages", "can_view", "can_edit", "can_execute", "can_approve"}),
    ("resource", "evidence", {"contains", "derived_from", "logged_as"}),
    ("evidence", "concept", {"mentions", "describes", "exemplifies"}),
    ("evidence", "claim", {"supports", "contradicts", "timestamps"}),
    ("concept", "concept", {"related_to", "subclass_of", "part_of", "influences", "depends_on"}),
    ("concept", "outcome", {"contributes_to", "constrains", "predicts", "degrades"}),
    ("lever", "outcome", {"raises", "lowers", "stabilizes", "optimizes"}),
    ("lever", "concept", {"affects"}),
    ("community", "concept", {"clusters", "summarizes"}),
    ("policy", "resource", {"protects", "classifies", "restricts"}),
    ("policy", "subject", {"permits", "denies", "requires_approval"}),
    ("subject", "concept", {"qualified_as"}),
    ("concept", "decision", {"grants_authority_for"}),
    ("subject", "decision", {"performs"}),
    ("decision", "concept", {"targets_component", "targets_facility", "targets_work_type"}),
    ("decision", "resource", {"based_on"}),
    ("decision", "decision", {"depends_on", "precedes"}),
    ("decision", "outcome", {"yields"}),
]

NODE_TYPE_TO_SPACE: dict[str, str] = {nt: sp for sp, nts in SPACES.items() for nt in nts}
EDGE_LOOKUP: dict[tuple[str, str], set[str]] = {(f, t): rels for f, t, rels in META_EDGES}


def n(node_type: str, node_id: str, name: str, source_article: str, properties: dict | None = None) -> dict:
    space = NODE_TYPE_TO_SPACE.get(node_type)
    if space is None:
        raise SystemExit(f"unknown node_type {node_type!r}")
    full_id = f"{node_type}:{node_id}"
    props = {"name": name}
    if properties:
        props.update(properties)
    return {
        "kind": "node",
        "space": space,
        "node_type": node_type,
        "node_id": full_id,
        "properties": props,
        "source_article": source_article,
    }


def e(from_id: str, to_id: str, relation: str, source_article: str) -> dict:
    from_type = from_id.split(":", 1)[0]
    to_type = to_id.split(":", 1)[0]
    from_space = NODE_TYPE_TO_SPACE.get(from_type)
    to_space = NODE_TYPE_TO_SPACE.get(to_type)
    if from_space is None or to_space is None:
        raise SystemExit(f"edge with unknown node_type: {from_id} -> {to_id}")
    allowed = EDGE_LOOKUP.get((from_space, to_space))
    if allowed is None or relation not in allowed:
        raise SystemExit(
            f"illegal edge ({from_space} -> {to_space}, {relation}): {from_id} -> {to_id}"
        )
    return {
        "kind": "edge",
        "from_node_id": from_id,
        "to_node_id": to_id,
        "relation": relation,
        "source_article": source_article,
    }


# ---------------------------------------------------------------------------
# Node and edge construction
# ---------------------------------------------------------------------------

nodes: list[dict] = []
edges: list[dict] = []

# ---------------- shared subjects (qualified actors) ----------------
nodes.extend([
    n("ChiefSupervisor", "kds14_30_01_chief_supervisor",
      "책임감리원 — 강구조 공사 책임감리",
      "KDS 14 30 / 14 31 (총칙)"),
    n("Supervisor", "kds14_30_02_supervisor",
      "감리원 — 강구조 시공 감리",
      "KDS 14 30 / 14 31 (총칙)"),
    n("SiteEngineer", "kds14_30_03_site_engineer",
      "시공자(현장대리인) — 강구조 시공 책임기술자",
      "KDS 14 31 05 §1.6"),
    n("SafetyManager", "kds14_30_04_safety_manager",
      "안전관리자 — 강구조 고소작업·용접화재 안전관리",
      "KDS 14 31 05 §1.6"),
    n("Org", "kds14_30_05_certified_test_lab",
      "공인시험기관 — 강재·용접부 시험성적 발급기관",
      "KDS 14 31 05 §1.3 / KDS 14 31 70 §4.1.2"),
])

# ---------------- qualifications (Qualification concept) ----------------
nodes.extend([
    n("Qualification", "kds14_30_q_responsible_struct_eng",
      "책임구조기술자 (Engineer of Record) — 구조설계·검토 권한",
      "KDS 14 31 05 §1.6, KDS 14 31 70 §1.6"),
    n("Qualification", "kds14_30_q_welding_inspector",
      "용접검사원 (Certified Welding Inspector) — 강구조 용접부 검사 자격",
      "KDS 14 31 25 §4.1.2 / KDS 14 31 20"),
    n("Qualification", "kds14_30_q_welder",
      "용접기능자 (Qualified Welder) — KS B 0885 등 용접자격검정 합격자",
      "KDS 14 31 25 §4.1.2"),
    n("Qualification", "kds14_30_q_ndt_level2",
      "비파괴검사 기술자 Level 2 — RT/UT/MT/PT 판독 자격 (KS B ISO 9712)",
      "KDS 14 31 20 §3.15 (NDT)"),
])

# Subjects qualified as concepts
edges.extend([
    e("ChiefSupervisor:kds14_30_01_chief_supervisor", "Qualification:kds14_30_q_responsible_struct_eng",
      "qualified_as", "KDS 14 31 05 §1.6"),
    e("Supervisor:kds14_30_02_supervisor", "Qualification:kds14_30_q_welding_inspector",
      "qualified_as", "KDS 14 31 25 §4.1.2"),
    e("SiteEngineer:kds14_30_03_site_engineer", "Qualification:kds14_30_q_welder",
      "qualified_as", "KDS 14 31 25 §4.1.2"),
    e("Org:kds14_30_05_certified_test_lab", "Qualification:kds14_30_q_ndt_level2",
      "qualified_as", "KDS 14 31 20 §3.15"),
])

# ---------------- 16 sections (Specification anchors) ----------------
# Each section: Specification node for the section header itself.

SECTION_SPECS = [
    # (file_code, title, short_desc, scope)
    ("14_30_05", "KDS 14 30 05 강구조 설계 일반사항 (허용응력설계법)",
     "강구조 허용응력설계법 적용범위·용어·기호·재료강도·하중조합·기본원칙",
     "허용응력설계법 기반 강구조 설계 총칙 — 강재 항복강도·인장강도 표 및 안전계수 정의"),
    ("14_30_10", "KDS 14 30 10 강구조 부재 설계 (허용응력설계법)",
     "인장·압축·휨·전단·조합력 부재의 허용응력 산정",
     "총단면적·순단면적·유효순단면적 산정 및 부재별 허용응력 검증"),
    ("14_30_20", "KDS 14 30 20 강구조 피로 및 파괴 설계 (허용응력설계법)",
     "반복하중에 의한 강구조 부재·이음부의 피로설계 및 취성파괴 방지",
     "허용피로응력 범위 (상세범주 A~E') 및 200만회 무한수명 설계"),
    ("14_30_25", "KDS 14 30 25 강구조 연결설계 (허용응력설계법)",
     "용접·고장력볼트·일반볼트 연결부의 허용응력 설계",
     "단순접합·강접합·편심접합·기둥이음·접합부 최소강도 30kN"),
    ("14_30_50", "KDS 14 30 50 강구조 사용성 설계 (허용응력설계법)",
     "처짐·진동·수평변위·부식·물고임 등 사용성 한계상태",
     "처짐·진동·수평변위 한계, 솟음(camber), 부식방지 설계"),
    ("14_31_05", "KDS 14 31 05 강구조 일반사항 (한계상태설계법)",
     "한계상태설계법 기반 강구조 총칙 — 적용범위·재료·설계요구조건",
     "용어·기호 정의, 강재 종류, 한계상태와 설계요구조건"),
    ("14_31_10", "KDS 14 31 10 강구조 부재 설계 (한계상태설계법)",
     "인장·압축·휨·전단·비틀림·조합력 한계상태 부재설계",
     "강도한계상태 (Mn, Pn, Vn) 및 사용한계상태 검증"),
    ("14_31_15", "KDS 14 31 15 강구조 안정설계 (한계상태설계법)",
     "직접해석법·유효길이법·1차해석법 기반 구조 안정성 평가",
     "P-Delta·P-delta 2차효과, 초기 불완전성·강성저감 반영"),
    ("14_31_20", "KDS 14 31 20 강구조 피로 및 파괴 설계 (한계상태설계법)",
     "피로한계상태 설계 및 비파괴검사 합격기준",
     "상세범주별 일정진폭피로한계·무한수명피로한계, RT/UT/MT/PT 합격판정"),
    ("14_31_25", "KDS 14 31 25 강구조 연결설계 (한계상태설계법)",
     "용접·고장력볼트 연결부 한계상태 설계 (LRFD)",
     "그루브용접·필릿용접 강도, F8T/F10T/F13T 설계장력, 미끄럼강도"),
    ("14_31_50", "KDS 14 31 50 강구조 내화설계",
     "강구조 주요구조부의 사양적·성능적 내화설계",
     "내화구조 인정·관리기준, 구조해석에 의한 화재 구조적합시간"),
    ("14_31_55", "KDS 14 31 55 강구조 사용성 설계 (한계상태설계법)",
     "강구조 건축물의 사용성 한계상태 — 처짐·수평변위·진동·물고임",
     "물고임 식 (Cp+0.9Cs<=0.25), 보행하중·바람진동 거주성"),
    ("14_31_60", "KDS 14 31 60 강구조 내진설계 (한계상태설계법)",
     "지진력저항시스템·내진성 강재·예상항복강도 비 Ry, Rt",
     "특수모멘트골조·중간모멘트골조·중심가새·편심가새·좌굴방지가새·강판전단벽"),
    ("14_31_70", "KDS 14 31 70 기존 강구조 건축물의 평가",
     "기존 강구조의 재료실험·구조해석·재하실험에 의한 내하력 평가",
     "샤르피 V-노치 인성, 1.2D+1.6L 등치 실험강도 산정"),
    ("14_31_80", "KDS 14 31 80 합성구조 설계",
     "강-콘크리트 합성기둥·합성보·전단연결재 설계",
     "충전형·매입형 합성단면, 콘크리트 21~70MPa 한계, 항복강도 650MPa 상한"),
    ("14_31_85", "KDS 14 31 85 합성구조 내진설계",
     "합성구조 시스템의 내진설계 일반요건",
     "합성지진력저항시스템·예상강도·소요강도 산정"),
]

for code, title, short_desc, scope in SECTION_SPECS:
    sid = f"Specification:kds{code}_section_root"
    nodes.append(n("Specification", f"kds{code}_section_root", title,
                   f"KDS {code.replace('_',' ')} §1",
                   {"document_id": f"KDS {code.replace('_',' ')}",
                    "scope": scope,
                    "key_rule": short_desc,
                    "designation": "한국 토목·건축 설계기준 (Korean Design Standard, KDS)"}))

# ---------------- Work types (강구조 공종) ----------------
WORK_TYPES = [
    ("kds14_30_wt_steel_design", "강구조 허용응력설계 (ASD)",
     "강재 부재·이음부의 허용응력에 기초한 설계 행위",
     "KDS 14 30 05 §1.1"),
    ("kds14_30_wt_steel_design_lrfd", "강구조 하중저항계수설계 (LRFD)",
     "한계상태설계법 (강도·사용성 한계상태) 기반 설계 행위",
     "KDS 14 31 05 §1.6"),
    ("kds14_30_wt_fabrication", "강구조 제작 (Shop Fabrication)",
     "공장 절단·천공·용접 등 강재 부재 제작 공종",
     "KDS 14 31 25 §4.1.1"),
    ("kds14_30_wt_erection", "강구조 설치 (Erection)",
     "현장에서 강재 부재를 조립·접합·고정하는 공종",
     "KDS 14 31 25 §4.1.1"),
    ("kds14_30_wt_welding", "강구조 용접공사",
     "그루브·필릿·플러그·슬롯용접 시공 및 검사",
     "KDS 14 31 25 §4.1.2"),
    ("kds14_30_wt_bolting", "고장력볼트 접합공사",
     "F8T·F10T·F13T 고장력볼트 도입장력 도입 및 미끄럼접합",
     "KDS 14 31 25 §4.1.3"),
    ("kds14_30_wt_painting", "강구조 도장공사 (방청·도막)",
     "방청도장·중도·상도 도장막 두께 관리",
     "KDS 14 30 50 §4.5 (부식)"),
    ("kds14_30_wt_fireproofing", "강구조 내화피복공사",
     "기둥·보·바닥 등 주요구조부 내화구조 피복",
     "KDS 14 31 50 §4.2"),
    ("kds14_30_wt_seismic_detailing", "강구조 내진상세 시공",
     "지진력저항시스템·임계용접부·보호영역 시공",
     "KDS 14 31 60 §1.8"),
    ("kds14_30_wt_composite_construction", "강-콘크리트 합성구조 시공",
     "충전형·매입형 합성기둥, 전단연결재 시공",
     "KDS 14 31 80 §4"),
]
for nid, name, key, src in WORK_TYPES:
    nodes.append(n("WorkType", nid, name, src, {"key_rule": key}))

# ---------------- Structural components ----------------
STRUCTURAL_COMPONENTS = [
    ("kds14_30_sc_steel_column", "강구조 기둥 (Steel Column)",
     "압축력·휨모멘트를 지지하는 수직 강재 부재 — 좌굴·세장비 한계 적용",
     "KDS 14 30 10 §4.3 / KDS 14 31 10 §4.3"),
    ("kds14_30_sc_steel_beam", "강구조 보 (Steel Beam)",
     "휨모멘트·전단력을 지지하는 수평 강재 부재 — 횡좌굴·국부좌굴 한계",
     "KDS 14 30 10 §4.4 / KDS 14 31 10 §4.4"),
    ("kds14_30_sc_steel_brace", "강구조 가새 (Steel Brace)",
     "축력 위주의 사선 부재 — 중심가새·편심가새·좌굴방지가새",
     "KDS 14 31 60 §4 (지진력저항시스템)"),
    ("kds14_30_sc_connection", "강구조 접합부 (Connection)",
     "둘 이상 부재 간 힘 전달 — 단순접합·강접합·편심접합·기둥이음",
     "KDS 14 30 25 §4 / KDS 14 31 25 §4.1.1"),
    ("kds14_30_sc_gusset_plate", "거셋 플레이트 (Gusset Plate)",
     "트러스 격점에서 부재를 연결하는 강판 — 비탄성회전 수용 요구",
     "KDS 14 30 05 §1.2 / KDS 14 31 60 §1.8"),
    ("kds14_30_sc_groove_weld", "완전·부분용입 그루브용접 (Groove Weld)",
     "맞대기 이음부 용접 — 유효목두께·루트간격·개선각 관리",
     "KDS 14 31 25 §4.1.2.1"),
    ("kds14_30_sc_fillet_weld", "필릿용접 (Fillet Weld)",
     "겹침이음 용접 — 다리길이·목두께 관리 (목두께 = 0.7 × 다리길이)",
     "KDS 14 31 25 §4.1.2.2"),
    ("kds14_30_sc_hsfg_bolt", "고장력볼트 (High Strength Friction Grip Bolt)",
     "마찰접합·지압접합용 합금강 열처리 볼트 — F8T·F10T·F13T",
     "KDS 14 31 25 §4.1.3.1"),
    ("kds14_30_sc_anchor_bolt", "앵커볼트 (Anchor Bolt)",
     "강구조 기둥·교각·토대의 기초고정 매입식 볼트",
     "KDS 14 30 05 §1.2"),
    ("kds14_30_sc_stiffener", "보강재 (Stiffener)",
     "보 웨브·판재의 좌굴 방지·하중분산 보강 부재",
     "KDS 14 30 05 §1.2"),
    ("kds14_30_sc_deck_plate", "데크 플레이트 (Deck Plate)",
     "강구조 바닥판용 요철 강판 — 합성슬래브 거푸집 및 인장근 역할",
     "KDS 14 30 05 §1.2"),
    ("kds14_30_sc_composite_beam", "합성보 (Composite Beam)",
     "강재보와 콘크리트 슬래브가 전단연결재로 일체화된 보",
     "KDS 14 31 80 §4.5"),
    ("kds14_30_sc_composite_column", "합성기둥 (Composite Column)",
     "충전형·매입형 강-콘크리트 합성기둥",
     "KDS 14 31 80 §4.3, §4.4"),
    ("kds14_30_sc_shear_stud", "전단연결재 (Shear Stud Connector)",
     "강재보-콘크리트 슬래브 합성거동 확보용 스터드볼트",
     "KDS 14 31 80 §4.6"),
    ("kds14_30_sc_shear_wall", "강판전단벽 (Steel Plate Shear Wall)",
     "면내 전단력 지지·골조 안정성 유지용 강판 벽체",
     "KDS 14 31 60 §4"),
    ("kds14_30_sc_diaphragm", "다이아프램 (Diaphragm)",
     "지지요소에 힘을 전달하는 면내 전단강성 평면요소",
     "KDS 14 30 05 §1.2"),
]
for nid, name, key, src in STRUCTURAL_COMPONENTS:
    nodes.append(n("StructuralComponent", nid, name, src, {"key_rule": key}))

# ---------------- Facilities ----------------
FACILITIES = [
    ("kds14_30_fa_steel_building", "강구조 건축물",
     "지진력저항시스템·중력하중지지시스템을 갖춘 강구조 건물 — KDS 14 31 60 적용",
     "KDS 14 31 60 §1"),
    ("kds14_30_fa_steel_bridge", "강교 (Steel Bridge)",
     "강구조 교량 — KDS 14 31 10 적용, AASHTO LRFD 참조",
     "KDS 14 31 10 §1 / KCS 24 00 00"),
    ("kds14_30_fa_composite_structure", "합성구조 시설물",
     "강-콘크리트 합성기둥·합성보·합성슬래브를 갖춘 시설물",
     "KDS 14 31 80 §1"),
]
for nid, name, key, src in FACILITIES:
    nodes.append(n("Facility", nid, name, src, {"key_rule": key}))

# ---------------- Structural component subclass hierarchy ----------------
edges.extend([
    e("StructuralComponent:kds14_30_sc_groove_weld", "StructuralComponent:kds14_30_sc_connection",
      "part_of", "KDS 14 31 25 §4.1.2"),
    e("StructuralComponent:kds14_30_sc_fillet_weld", "StructuralComponent:kds14_30_sc_connection",
      "part_of", "KDS 14 31 25 §4.1.2"),
    e("StructuralComponent:kds14_30_sc_hsfg_bolt", "StructuralComponent:kds14_30_sc_connection",
      "part_of", "KDS 14 31 25 §4.1.3"),
    e("StructuralComponent:kds14_30_sc_gusset_plate", "StructuralComponent:kds14_30_sc_connection",
      "part_of", "KDS 14 30 25 §4.1"),
    e("StructuralComponent:kds14_30_sc_stiffener", "StructuralComponent:kds14_30_sc_steel_beam",
      "part_of", "KDS 14 30 05 §1.2"),
    e("StructuralComponent:kds14_30_sc_shear_stud", "StructuralComponent:kds14_30_sc_composite_beam",
      "part_of", "KDS 14 31 80 §4.6"),
    e("StructuralComponent:kds14_30_sc_composite_beam", "StructuralComponent:kds14_30_sc_steel_beam",
      "subclass_of", "KDS 14 31 80 §4.5"),
    e("StructuralComponent:kds14_30_sc_composite_column", "StructuralComponent:kds14_30_sc_steel_column",
      "subclass_of", "KDS 14 31 80 §4.3"),
])

# ---------------- Specifications (quantitative rule anchors) ----------------
QUANT_SPECS: list[tuple[str, str, dict, str]] = [
    # ---- KDS 14 30 05: 재료강도 ----
    ("kds14_30_05_steel_strength_ss235", "구조용 강재 SS235 재료강도 — KDS 14 30 05 §3.3.1",
     {"document_id": "KDS 14 30 05", "designation": "SS235",
      "Fy_t_le_16mm_MPa": 235, "Fy_16_40mm_MPa": 225, "Fy_40_75mm_MPa": 205,
      "Fy_75_100mm_MPa": 205, "Fy_100_200mm_MPa": 195, "Fu_MPa": 330,
      "key_rule": "SS235 항복강도 235 MPa (16 mm 이하), 인장강도 330 MPa, 두께 증가 시 Fy 저감"},
     "KDS 14 30 05 §3.3.1 표 3.3-1"),
    ("kds14_30_05_steel_strength_ss275",
     "구조용 강재 SS275 / SM275 재료강도 — KDS 14 30 05 §3.3.1",
     {"document_id": "KDS 14 30 05", "designation": "SS275 / SM275 / SMA275",
      "Fy_t_le_16mm_MPa": 275, "Fy_16_40mm_MPa": 265,
      "Fu_MPa": 410,
      "key_rule": "SS275·SM275 항복강도 275 MPa (16 mm 이하), 인장강도 410 MPa"},
     "KDS 14 30 05 §3.3.1 표 3.3-1"),
    ("kds14_30_05_steel_strength_sm355",
     "구조용 강재 SM355 / SMA355 재료강도 — KDS 14 30 05 §3.3.1",
     {"document_id": "KDS 14 30 05", "designation": "SM355 / SMA355",
      "Fy_t_le_16mm_MPa": 355, "Fy_16_40mm_MPa": 345, "Fy_40_75mm_MPa": 335,
      "Fy_75_100mm_MPa": 325, "Fy_100_200mm_MPa": 305, "Fu_MPa": 490,
      "key_rule": "SM355 항복강도 355 MPa, 인장강도 490 MPa — 강교·중대규모 강구조 주력강종"},
     "KDS 14 30 05 §3.3.1 표 3.3-1"),
    ("kds14_30_05_steel_strength_sm420",
     "구조용 강재 SM420 재료강도 — KDS 14 30 05 §3.3.1",
     {"document_id": "KDS 14 30 05", "designation": "SM420",
      "Fy_t_le_16mm_MPa": 420, "Fy_16_40mm_MPa": 410, "Fy_40_75mm_MPa": 400,
      "Fu_MPa": 520,
      "key_rule": "SM420 항복강도 420 MPa, 인장강도 520 MPa"},
     "KDS 14 30 05 §3.3.1 표 3.3-1"),
    ("kds14_30_05_steel_strength_sm460",
     "구조용 강재 SM460 / SMA460 재료강도 — KDS 14 30 05 §3.3.1",
     {"document_id": "KDS 14 30 05", "designation": "SM460 / SMA460",
      "Fy_t_le_16mm_MPa": 460, "Fy_16_40mm_MPa": 450, "Fy_40_75mm_MPa": 430,
      "Fu_MPa": 570,
      "key_rule": "SM460 항복강도 460 MPa, 인장강도 570 MPa, 적용두께 100 mm 이하 (SM460B/C 협정 150 mm)"},
     "KDS 14 30 05 §3.3.1 표 3.3-1"),
    ("kds14_30_05_steel_strength_hsb690",
     "고성능강 HSB690 재료강도 — KDS 14 30 05 §3.3.1",
     {"document_id": "KDS 14 30 05", "designation": "HSB690",
      "Fy_t_le_100mm_MPa": 690, "Fu_t_le_100mm_MPa": 800,
      "applicable_thickness_max_mm": 80,
      "key_rule": "고성능강 HSB690 — Fy 690 MPa, Fu 800 MPa, 적용두께 80 mm 이하"},
     "KDS 14 30 05 §3.3.1 표 3.3-1"),
    ("kds14_30_05_steel_strength_sn",
     "내진성 강재 SN275 / SN355 / SN460 재료강도",
     {"document_id": "KDS 14 30 05", "designation": "SN275 / SN355 / SN460",
      "SN275_Fy_MPa": 275, "SN355_Fy_MPa": 355, "SN460_Fy_MPa": 460,
      "key_rule": "SN강 — 내진성능 보증 강재 (KDS 14 31 60 지진력저항시스템 권장)"},
     "KDS 14 30 05 §3.3.1 표 3.3-1"),
    ("kds14_30_05_elastic_modulus",
     "구조용 강재의 탄성계수·물리상수 — KDS 14 30 05 §3.3.4",
     {"document_id": "KDS 14 30 05",
      "elastic_modulus_E_MPa": 210000, "shear_modulus_G_MPa": 81000,
      "poisson_ratio": 0.3, "thermal_expansion_per_C": 1.2e-5,
      "density_kg_per_m3": 7850,
      "key_rule": "강재 E=210,000 MPa, G=81,000 MPa, 푸아송비 0.3, 선팽창계수 1.2×10⁻⁵/°C, 단위중량 7,850 kg/m³"},
     "KDS 14 30 05 §3.3.4"),
    ("kds14_30_05_allowable_stress_basic",
     "강구조 허용응력 기본원칙 — Fa·Fb·Fv 산정",
     {"document_id": "KDS 14 30 05",
      "allowable_tension_Ft_factor": "0.60 × Fy",
      "allowable_compression_Fa_factor": "좌굴공식 적용",
      "allowable_shear_Fv_factor": "0.40 × Fy",
      "key_rule": "허용인장응력 Ft = 0.60 Fy, 허용전단응력 Fv = 0.40 Fy, 허용압축응력 Fa는 세장비 함수"},
     "KDS 14 30 05 §5.1"),
    ("kds14_30_05_load_correction_factor",
     "구조물별 허용응력 보정계수 — KDS 14 30 05 §4.2",
     {"document_id": "KDS 14 30 05",
      "long_term_load_factor": 1.0,
      "short_term_load_factor_max": 1.5,
      "key_rule": "장기하중 보정계수 1.0 기준, 단기하중 (지진·바람) 1.5까지 허용응력 할증"},
     "KDS 14 30 05 §4.2.2 / §5.2"),
    # ---- KDS 14 30 10: 부재설계 ----
    ("kds14_30_10_slenderness_limit",
     "압축부재 허용세장비 한계",
     {"document_id": "KDS 14 30 10",
      "compression_main_member_max_KL_over_r": 200,
      "compression_secondary_member_max_KL_over_r": 240,
      "tension_alternating_main_max_L_over_r": 140,
      "tension_main_max_L_over_r": 200,
      "tension_secondary_max_L_over_r": 240,
      "key_rule": "압축 주부재 KL/r ≤ 200, 2차부재 ≤ 240; 인장 교번응력 주부재 L/r ≤ 140"},
     "KDS 14 30 10 §4.2 / KDS 14 31 10 §4.1.1"),
    ("kds14_30_10_net_area_formula",
     "순단면적 산정식 — 정렬·엇모배치",
     {"document_id": "KDS 14 30 10",
      "formula_aligned": "An = Ag - n·d·t",
      "formula_staggered": "An = Ag - n·d·t + Σ(s²/4g)·t",
      "key_rule": "엇모배치 시 보정항 Σ(s²/4g)·t 합산 (s=피치, g=게이지)"},
     "KDS 14 30 10 §4.1.3"),
    # ---- KDS 14 30 20: 피로 ----
    ("kds14_30_20_fatigue_category_a",
     "허용피로응력 범위 — 상세범주 A (200만회 이상 무한수명)",
     {"document_id": "KDS 14 30 20",
      "category": "A",
      "fsr_100k_MPa": 442, "fsr_500k_MPa": 260,
      "fsr_2M_MPa": 165, "fsr_infinite_MPa": 165,
      "key_rule": "상세범주 A — 10만회 442 MPa, 200만회 165 MPa (무한수명)"},
     "KDS 14 30 20 §4.1.2.2 표 4.1-1"),
    ("kds14_30_20_fatigue_category_e_prime",
     "허용피로응력 범위 — 상세범주 E' (필릿용접 단부 등)",
     {"document_id": "KDS 14 30 20",
      "category": "E'",
      "fsr_100k_MPa": 112,
      "key_rule": "상세범주 E' — 가장 가혹한 상세, 200만회 무한수명 피로한계 매우 낮음"},
     "KDS 14 30 20 §4.1.2.2 표 4.1-1"),
    ("kds14_30_20_fatigue_apply_scope",
     "피로설계 적용 범위 — 순인장응력 부재",
     {"document_id": "KDS 14 30 20",
      "key_rule": "활하중 응력범위만 고려, 잔류응력 무시; 압축응력 < 최대 활하중 인장응력의 2배인 경우에만 피로 고려"},
     "KDS 14 30 20 §4.1.2.1"),
    # ---- KDS 14 30 25 / 14 31 25: 접합 ----
    ("kds14_30_25_connection_min_strength",
     "접합부 최소설계강도 30 kN",
     {"document_id": "KDS 14 30 25",
      "min_design_strength_kN": 30,
      "exceptions": ["연결재", "새그로드", "띠장"],
      "key_rule": "강구조 접합부는 30 kN 이상 지지하도록 설계 (연결재·새그로드·띠장 제외)"},
     "KDS 14 30 25 §4.1.6"),
    ("kds14_30_25_bolt_weld_combination",
     "고장력볼트와 용접 병용 금지 원칙",
     {"document_id": "KDS 14 30 25",
      "key_rule": "고장력볼트와 용접은 원칙적으로 병용 금지 — 마찰접합 시 볼트 선시공 후 용접 조건에서만 분담 허용"},
     "KDS 14 30 25 §4.1.8"),
    ("kds14_31_25_bolt_F8T",
     "고장력볼트 F8T 공칭강도",
     {"document_id": "KDS 14 31 25", "designation": "F8T",
      "Fnt_nominal_tension_MPa": 600,
      "Fnv_thread_in_shear_plane_MPa": 320,
      "Fnv_thread_excluded_MPa": 400,
      "key_rule": "F8T 공칭인장강도 600 MPa, 나사부 전단면 포함 시 Fnv 320 MPa"},
     "KDS 14 31 25 §4.1.3.3 표 4.1-9"),
    ("kds14_31_25_bolt_F10T",
     "고장력볼트 F10T 공칭강도",
     {"document_id": "KDS 14 31 25", "designation": "F10T",
      "Fnt_nominal_tension_MPa": 750,
      "Fnv_thread_in_shear_plane_MPa": 400,
      "Fnv_thread_excluded_MPa": 500,
      "key_rule": "F10T 공칭인장강도 750 MPa, 나사부 전단면 포함 시 Fnv 400 MPa — 구조 표준 고장력볼트"},
     "KDS 14 31 25 §4.1.3.3 표 4.1-9"),
    ("kds14_31_25_bolt_F13T",
     "고장력볼트 F13T 공칭강도",
     {"document_id": "KDS 14 31 25", "designation": "F13T",
      "Fnt_nominal_tension_MPa": 975,
      "Fnv_thread_in_shear_plane_MPa": 520,
      "Fnv_thread_excluded_MPa": 650,
      "long_joint_factor_over_800mm": 0.85,
      "key_rule": "F13T 공칭인장강도 975 MPa, KS B 1010 수소지연파괴 시험성적표 첨부 제품에 한정 사용"},
     "KDS 14 31 25 §4.1.3.3 표 4.1-9"),
    ("kds14_31_25_phi_bolt",
     "볼트 설계강도 저항계수 φ = 0.75",
     {"document_id": "KDS 14 31 25",
      "phi_bolt": 0.75,
      "key_rule": "볼트 인장·전단파단 한계상태 강도감소계수 φ = 0.75"},
     "KDS 14 31 25 §4.1.3.3"),
    ("kds14_31_25_slip_resistance",
     "마찰접합 미끄럼강도 산정식",
     {"document_id": "KDS 14 31 25",
      "formula": "Rn = μ · hf · To · Ns",
      "phi_standard_hole_or_short_slot_perpendicular": 1.00,
      "phi_oversize_or_short_slot_parallel": 0.85,
      "phi_long_slot_perpendicular_to_load": 0.70,
      "key_rule": "Rn = μ·hf·To·Ns (μ=미끄럼계수, hf=끼움재계수, To=설계볼트장력, Ns=전단면수)"},
     "KDS 14 31 25 §4.1.3.6"),
    ("kds14_31_25_groove_weld_throat",
     "완전용입 그루브용접 유효목두께",
     {"document_id": "KDS 14 31 25",
      "effective_throat_full_penetration": "접합부의 얇은 쪽 모재 두께",
      "key_rule": "완전용입 그루브용접 유효목두께 = 접합되는 얇은 쪽 모재의 두께"},
     "KDS 14 31 25 §4.1.2.1.1"),
    ("kds14_31_25_fillet_weld_throat",
     "필릿용접 유효목두께·다리길이",
     {"document_id": "KDS 14 31 25",
      "throat_factor_of_leg": 0.7,
      "min_leg_size_t_le_6mm": "3 mm",
      "min_leg_size_6_lt_t_le_13mm": "5 mm",
      "min_leg_size_13_lt_t_le_19mm": "6 mm",
      "min_leg_size_t_gt_19mm": "8 mm",
      "max_leg_size_t_lt_6mm": "모재 두께",
      "max_leg_size_t_ge_6mm": "모재 두께 − 2 mm",
      "key_rule": "필릿용접 유효목두께 = 0.7 × 다리길이; 최소 다리길이는 모재 두께에 따라 3~8 mm 단계 적용"},
     "KDS 14 31 25 §4.1.2.2.2"),
    ("kds14_31_25_fillet_weld_min_length",
     "필릿용접 최소 유효길이",
     {"document_id": "KDS 14 31 25",
      "min_effective_length_factor": "4 × 다리길이 또는 40 mm 중 큰 값",
      "key_rule": "필릿용접 최소 유효길이 ≥ 다리길이의 4배 또는 40 mm 중 큰 값"},
     "KDS 14 31 25 §4.1.2.2.2"),
    ("kds14_31_25_weld_filler_strength",
     "용접재 강도 — 모재 인장강도 이상",
     {"document_id": "KDS 14 31 25",
      "key_rule": "용접금속의 인장강도는 접합되는 모재의 인장강도 이상으로 매칭 (Matching Filler)"},
     "KDS 14 31 25 §4.1.2.4 표 4.1-3"),
    # ---- KDS 14 30 50 / 14 31 55: 사용성 ----
    ("kds14_30_50_deflection_limit_beam",
     "보 처짐 한계 (사용성)",
     {"document_id": "KDS 14 30 50",
      "live_load_deflection_limit": "L/360 (활하중)",
      "total_load_deflection_limit": "L/240 (전하중)",
      "key_rule": "강구조 보 처짐 한계 — 활하중 L/360, 고정+활 L/240 (관련 기준 우선)"},
     "KDS 14 30 50 §4.4.1 / KDS 14 31 55 §4.1.3"),
    ("kds14_31_55_drift_limit",
     "강구조 건축물 층간변위 한계 (사용성)",
     {"document_id": "KDS 14 31 55",
      "service_drift_limit": "h/400 ~ h/500 (관련기준)",
      "key_rule": "사용하중에 의한 층간변위 한계는 내부칸막이·외부마감재 손상 방지 수준"},
     "KDS 14 31 55 §4.1.4"),
    ("kds14_31_55_ponding_limit",
     "물고임 한계식 — Cp + 0.9 Cs ≤ 0.25",
     {"document_id": "KDS 14 31 55",
      "formula_1": "Cp + 0.9·Cs ≤ 0.25",
      "formula_2": "Id ≥ 3940·S^4",
      "secondary_member_reduction_truss": 0.15,
      "key_rule": "지붕구조 물고임 안정조건 두 식 모두 만족, 트러스·강재장선은 Is를 15% 저감"},
     "KDS 14 31 55 §4.2.1"),
    # ---- KDS 14 31 05 / 10 / 15: 한계상태설계 ----
    ("kds14_31_05_phi_factors",
     "한계상태설계 저항계수 — 인장·압축·휨·전단",
     {"document_id": "KDS 14 31 05",
      "phi_tension_yielding": 0.90, "phi_tension_rupture": 0.75,
      "phi_compression": 0.90, "phi_flexure": 0.90,
      "phi_shear": 0.90, "phi_bolt": 0.75,
      "key_rule": "강도감소계수 — 항복·휨·전단·압축 φ=0.90, 인장파단·볼트 φ=0.75"},
     "KDS 14 31 05 §1.6 / KDS 14 31 25"),
    ("kds14_31_15_pdelta_threshold",
     "직접해석법 2차효과 적용 임계비",
     {"document_id": "KDS 14 31 15",
      "second_order_to_first_order_ratio_threshold": 1.7,
      "key_rule": "최대 2차횡변위/1차횡변위 ≤ 1.7 일 때만 P-δ 효과 무시 가능 (그 외 필수 고려)"},
     "KDS 14 31 15 §4.2.1.1"),
    ("kds14_31_15_stiffness_reduction",
     "직접해석법 강성저감계수",
     {"document_id": "KDS 14 31 15",
      "EI_reduction_factor": 0.80,
      "EA_reduction_factor": 0.80,
      "tau_b_factor_when_Pr_le_0_5Py": 1.0,
      "key_rule": "직접해석법에서 EI·EA에 0.80을 곱하고, αPr/Py > 0.5인 경우 τb 추가 적용"},
     "KDS 14 31 15 §4.2.1.3"),
    # ---- KDS 14 31 20: NDT 합격기준 ----
    ("kds14_31_20_ut_acceptance",
     "강용접부 초음파탐상시험(UT) 합격판정 — KDS 14 31 20 §3.15",
     {"document_id": "KDS 14 31 20", "test_method": "UT (Ultrasonic Testing)",
      "reference_ks": "KS B 0896",
      "key_rule": "표본 30개 중 불합격 0~1개 합격, 2~3개 시 60개 재검사 후 4개 이하 합격·5개 이상 불합격"},
     "KDS 14 31 20 §3.15.2"),
    ("kds14_31_20_rt_acceptance",
     "강용접부 방사선투과시험(RT) 합격판정",
     {"document_id": "KDS 14 31 20", "test_method": "RT (Radiographic Testing)",
      "reference_ks": "KS B 0845",
      "key_rule": "1종 결함(균열·용입불량)은 불허, 2종(슬래그·기공) 결함 크기·집계기준 KS B 0845 적용"},
     "KDS 14 31 20 §3.15"),
    ("kds14_31_20_mt_pt_acceptance",
     "자분탐상(MT) / 침투탐상(PT) 합격판정",
     {"document_id": "KDS 14 31 20",
      "test_methods": ["MT", "PT"],
      "reference_ks_mt": "KS D 0213", "reference_ks_pt": "KS B 0816",
      "key_rule": "표면 결함 검출 — 균열성 결함 불허, 선상·구상 결함은 길이·집계기준 적용"},
     "KDS 14 31 20 §3.15"),
    ("kds14_31_20_fatigue_detail_category_summary",
     "한계상태설계법 피로 상세범주 — 일정진폭피로한계 ΔF_TH",
     {"document_id": "KDS 14 31 20",
      "category_A_delta_F_TH_MPa": 165,
      "category_B_delta_F_TH_MPa": 110,
      "category_C_delta_F_TH_MPa": 69,
      "category_D_delta_F_TH_MPa": 48,
      "category_E_delta_F_TH_MPa": 31,
      "category_E_prime_delta_F_TH_MPa": 18,
      "key_rule": "상세범주 A~E' — 일정진폭피로한계 (Constant-Amplitude Fatigue Threshold) 표 4.1-1"},
     "KDS 14 31 20 §4.1.2.3 표 4.1-1"),
    # ---- KDS 14 31 50: 내화 ----
    ("kds14_31_50_fire_resistance_test",
     "강구조 내화구조 품질시험 — KS F 2257 시리즈",
     {"document_id": "KDS 14 31 50",
      "test_standards": ["KS F 2257-1", "KS F 2257-4", "KS F 2257-5", "KS F 2257-6", "KS F 2257-7"],
      "key_rule": "사양적 내화설계는 KS F 2257-1,4,5,6,7 건축구조 부재 내화시험에 의한 품질시험으로 평가"},
     "KDS 14 31 50 §4.3.1"),
    ("kds14_31_50_structural_adequacy_time",
     "성능적 내화설계 — 구조적 적합시간",
     {"document_id": "KDS 14 31 50",
      "design_loads_considered": ["고정하중", "활하중", "적설하중"],
      "criterion": "공학적 해석에 의한 구조적 적합시간 ≥ 내화구조 성능기준 시간",
      "key_rule": "온도에 따른 강재 강도·탄성계수 저감 및 열전달 해석으로 화재 시 붕괴시간 산정"},
     "KDS 14 31 50 §4.2.2 / §4.3.3.2"),
    # ---- KDS 14 31 60: 내진 ----
    ("kds14_31_60_steel_grade_requirement",
     "지진력저항시스템 강재 — 내진성 강재 의무 사용",
     {"document_id": "KDS 14 31 60",
      "required_grades": ["SN", "SHN", "TMC"],
      "systems": ["특수모멘트골조", "중간모멘트골조", "특수중심가새골조", "편심가새골조", "좌굴방지가새골조", "특수강판전단벽"],
      "key_rule": "특수·중간모멘트골조·중심가새·편심가새·좌굴방지가새·강판전단벽은 SN·SHN·TMC강 사용"},
     "KDS 14 31 60 §3.1"),
    ("kds14_31_60_Ry_Rt_values",
     "예상항복강도비 Ry 및 예상인장강도비 Rt — 강재 종류별",
     {"document_id": "KDS 14 31 60",
      "SM275_Ry": 1.3, "SM275_Rt": 1.2,
      "SM355_Ry": 1.2, "SM355_Rt": 1.15,
      "SN275_Ry": 1.15, "SN275_Rt": 1.15,
      "SN355_Ry": 1.1, "SN355_Rt": 1.1,
      "key_rule": "내진 소요강도 산정 시 RyFy·RtFu 사용 — SN강은 Ry/Rt 산포가 가장 작음"},
     "KDS 14 31 60 §3.2 표 3.2-1"),
    ("kds14_31_60_critical_weld_marking",
     "임계용접부 (Demand Critical Weld) 도면 표기 의무",
     {"document_id": "KDS 14 31 60",
      "key_rule": "지진력저항시스템 임계용접부 위치는 구조설계도면·제작도면·설치도면에 명시"},
     "KDS 14 31 60 §1.8.1 ~ §1.8.3"),
    # ---- KDS 14 31 70: 평가 ----
    ("kds14_31_70_load_test_acceptance",
     "재하실험에 의한 내하력 평가",
     {"document_id": "KDS 14 31 70",
      "experimental_strength_formula": "최고재하하중 + 고정하중",
      "live_load_equivalence": "실험강도 = 1.2 D + 1.6 L",
      "max_load_hold_minutes": 60,
      "deformation_creep_limit_pct": 10,
      "post_unload_record_hours": 24,
      "key_rule": "최대시험하중 1시간 유지 동안 변형 증가 10% 이내, 제하 후 24시간 영구변형 기록"},
     "KDS 14 31 70 §4.3.1"),
    # ---- KDS 14 31 80: 합성구조 ----
    ("kds14_31_80_material_limits",
     "합성구조 재료강도 한계",
     {"document_id": "KDS 14 31 80",
      "concrete_fck_normal_min_MPa": 21, "concrete_fck_normal_max_MPa": 70,
      "concrete_fck_lightweight_max_MPa": 42,
      "steel_fy_max_MPa": 650,
      "rebar_fy_max_MPa": 420,
      "bridge_concrete_fck_max_MPa": 55,
      "key_rule": "보통중량 콘크리트 fck 21~70 MPa, 경량 21~42 MPa; 합성기둥 강재 Fy ≤ 650 MPa; 교량 합성기둥 콘크리트 ≤ 55 MPa"},
     "KDS 14 31 80 §4.2"),
    ("kds14_31_80_circular_chs_confinement",
     "원형강관 합성기둥 콘크리트 구속효과",
     {"document_id": "KDS 14 31 80",
      "plastic_stress_axial": "0.85·(1 + 1.56·fy·t/(Dc·fck))·fck",
      "plastic_stress_flexure_only": "0.95·fck",
      "key_rule": "원형강관 충전 합성기둥 — 축압축 시 강관 구속효과로 콘크리트 소성압축응력 증가"},
     "KDS 14 31 80 §4.1.1"),
    ("kds14_31_80_max_concrete_strain",
     "합성구조 변형률적합법 최대 콘크리트 압축변형률",
     {"document_id": "KDS 14 31 80",
      "max_concrete_compressive_strain": 0.003,
      "key_rule": "변형률적합법에서 콘크리트 최대 압축변형률 0.003 가정, 변형률 선형분포"},
     "KDS 14 31 80 §4.1.2"),
    # ---- 추가 시공 정밀도 / 도장 ----
    ("kds14_31_25_erection_tolerance_column_plumb",
     "강구조 기둥 수직도 허용오차",
     {"document_id": "KDS 14 31 25",
      "column_plumb_tolerance_per_floor": "H/1000",
      "column_plumb_tolerance_overall_max_mm": 25,
      "key_rule": "기둥 수직도 — 1개 층 당 H/1000, 전체 누적 ±25 mm 이내 (KS B ISO 7976 / AISC 표준)"},
     "KDS 14 31 25 §4.1.1 (시공정밀도)"),
    ("kds14_31_25_bolt_pretension_F10T",
     "F10T 고장력볼트 설계볼트장력 (표 4.1-10)",
     {"document_id": "KDS 14 31 25",
      "designation": "F10T",
      "M20_design_pretension_kN": 165,
      "M22_design_pretension_kN": 200,
      "M24_design_pretension_kN": 235,
      "key_rule": "F10T 설계볼트장력 — M20 165 kN, M22 200 kN, M24 235 kN (너트회전법·토크관리법으로 도입)"},
     "KDS 14 31 25 §4.1.3.1 표 4.1-10"),
    ("kds14_30_50_corrosion_paint",
     "강구조 부식방지 — 도장막 두께 관리",
     {"document_id": "KDS 14 30 50",
      "key_rule": "구조요소는 부식에 견디도록 설계, 내부 표면 피막·청소·도장이 가능한 간격 확보"},
     "KDS 14 30 50 §4.5"),
]

quant_spec_ids: list[str] = []
for nid, name, props, src in QUANT_SPECS:
    nodes.append(n("Specification", nid, name, src, props))
    quant_spec_ids.append(f"Specification:{nid}")

# ---------------- TestReport (강재·용접 시험성적서) ----------------
TEST_REPORTS = [
    ("kds14_31_05_mill_test_certificate",
     "강재 밀시트 (Mill Test Certificate)",
     {"document_id": "KDS 14 31 05",
      "issuer": "제철회사 또는 공인시험소",
      "required_items": ["화학적 조성", "항복강도 Fy", "인장강도 Fu", "연신율", "샤르피 충격값"],
      "key_rule": "강재 입고 시 제철소·공인시험기관 발급 시험성적서로 재질 확인 (KDS 14 31 70 §4.1.2)"},
     "KDS 14 31 05 §1.3 / KDS 14 31 70 §4.1.2"),
    ("kds14_31_20_ndt_report",
     "용접부 비파괴검사 시험성적서 (RT/UT/MT/PT)",
     {"document_id": "KDS 14 31 20",
      "test_methods": ["RT", "UT", "MT", "PT"],
      "key_rule": "용접검사원이 KS B ISO 9712 자격으로 NDT 수행 후 시험성적서 작성"},
     "KDS 14 31 20 §3.15"),
    ("kds14_31_25_bolt_inspection_report",
     "고장력볼트 토크검사 시험성적서",
     {"document_id": "KDS 14 31 25",
      "inspection_methods": ["너트회전법", "직접인장측정법", "토크관리법", "토크-전단형볼트"],
      "key_rule": "마찰·프리텐션 접합 모든 고장력볼트는 설계볼트장력 이상 도입 후 검사·기록"},
     "KDS 14 31 25 §4.1.3.1"),
    ("kds14_31_50_fire_test_report",
     "내화구조 품질시험 성적서 (KS F 2257)",
     {"document_id": "KDS 14 31 50",
      "test_standards": ["KS F 2257-1,4,5,6,7"],
      "key_rule": "사양적 내화설계 — 한국산업규격 내화시험 합격 성적서 또는 내화구조 인정서"},
     "KDS 14 31 50 §4.3.1 / §4.3.2"),
    ("kds14_31_70_charpy_v_notch_test",
     "샤르피 V-노치 충격시험 성적서",
     {"document_id": "KDS 14 31 70",
      "test_method": "Charpy V-notch impact test",
      "key_rule": "후판 형강·판재의 용접인장이음 — 노치인성 시험으로 모재 인성 확인"},
     "KDS 14 31 70 §4.1.4"),
]
test_report_ids: list[str] = []
for nid, name, props, src in TEST_REPORTS:
    nodes.append(n("TestReport", nid, name, src, props))
    test_report_ids.append(f"TestReport:{nid}")

# ---------------- Drawings (설계도서) ----------------
DRAWINGS = [
    ("kds14_31_60_structural_drawing",
     "강구조 구조설계 도면 (내진)",
     {"document_id": "KDS 14 31 60",
      "required_items": ["지진력저항시스템 지정", "임계용접부 위치", "보호영역",
                          "최저 예상 서비스온도", "거셋플레이트 위치", "용접 요구사항"],
      "key_rule": "내진설계 구조도면 — 임계용접부·보호영역·거셋 비탄성회전 위치 명시"},
     "KDS 14 31 60 §1.8.1"),
    ("kds14_31_60_fabrication_drawing",
     "강구조 제작도면 (Shop Drawing)",
     {"document_id": "KDS 14 31 60",
      "required_items": ["부재·접합부 지정", "접합부 재료규격", "임계용접부", "보호영역", "거셋 축적도", "용접 요구사항"],
      "key_rule": "제작도면 — 임계용접부·접합부 재료규격·거셋 축적 도면 포함"},
     "KDS 14 31 60 §1.8.2"),
    ("kds14_31_60_erection_drawing",
     "강구조 설치(현장조립) 도면",
     {"document_id": "KDS 14 31 60",
      "required_items": ["설치순서", "임계용접부", "보호영역", "용접 요구사항"],
      "key_rule": "설치도면 — 부재 식별·접합부 위치·임계용접부·보호영역 표기"},
     "KDS 14 31 60 §1.8.3"),
]
drawing_ids: list[str] = []
for nid, name, props, src in DRAWINGS:
    nodes.append(n("Drawing", nid, name, src, props))
    drawing_ids.append(f"Drawing:{nid}")

# ---------------- Checklists ----------------
CHECKLISTS = [
    ("kds14_31_25_weld_visual_checklist",
     "강용접부 육안검사 체크리스트",
     {"document_id": "KDS 14 31 25",
      "items": ["다리길이", "목두께", "언더컷", "오버랩", "균열", "표면결함", "비드 형상"],
      "key_rule": "용접 직후 100% 육안검사 — 균열·언더컷·오버랩 결함 식별"},
     "KDS 14 31 25 §4.1.2 / KDS 14 31 20 §3.15"),
    ("kds14_31_25_bolt_torque_checklist",
     "고장력볼트 도입장력 검사 체크리스트",
     {"document_id": "KDS 14 31 25",
      "items": ["조임순서", "토크값", "너트회전각", "축력측정", "마킹"],
      "key_rule": "고장력볼트는 표 4.1-10 설계볼트장력 이상 도입 — 토크관리법·너트회전법으로 확인"},
     "KDS 14 31 25 §4.1.3.1"),
    ("kds14_31_25_erection_dimension_checklist",
     "강구조 설치 정밀도 검사 체크리스트",
     {"document_id": "KDS 14 31 25",
      "items": ["기둥 수직도", "보 수평도", "층고", "스팬길이", "베이스플레이트 레벨"],
      "key_rule": "기둥 수직도 H/1000, 전체 누적 ±25 mm — 설치 단계별 측량 검사"},
     "KDS 14 31 25 §4.1.1"),
    ("kds14_31_05_material_receipt_checklist",
     "강재 입고검수 체크리스트",
     {"document_id": "KDS 14 31 05",
      "items": ["강종 표시", "Mill Test Certificate", "치수", "표면결함", "휨", "비틀림"],
      "key_rule": "강재 입고 시 강종·치수·시험성적서·표면결함 확인"},
     "KDS 14 31 05 §3"),
    ("kds14_31_50_fireproofing_checklist",
     "내화피복 시공 체크리스트",
     {"document_id": "KDS 14 31 50",
      "items": ["피복재 종류", "피복두께", "부착강도", "양생조건", "내화구조 인정 확인"],
      "key_rule": "내화피복 — 인정구조 적용 또는 KS F 2257 시험성적 기반 두께 관리"},
     "KDS 14 31 50 §4.3"),
]
checklist_ids: list[str] = []
for nid, name, props, src in CHECKLISTS:
    nodes.append(n("Checklist", nid, name, src, props))
    checklist_ids.append(f"Checklist:{nid}")

# ---------------- Decisions ----------------
DECISIONS: list[tuple[str, str, str, dict, str]] = [
    # MaterialReceiptDecision
    ("MaterialReceiptDecision", "kds14_31_05_steel_material_receipt",
     "강재 입고검수 결정 — Mill Test Certificate 및 치수 확인",
     {"document_id": "KDS 14 31 05",
      "key_rule": "강재 입고 시 강종·항복강도·인장강도·연신율·치수 적합 여부를 시험성적서로 판정",
      "criteria": ["KS D 표준 강종 일치", "Fy/Fu 표 3.3-1 부합", "치수·휨·비틀림 허용오차 이내"]},
     "KDS 14 31 05 §3 / KDS 14 30 05 §3.1.1"),
    ("MaterialReceiptDecision", "kds14_31_25_hsfg_bolt_receipt",
     "고장력볼트 입고검수 결정 — F8T/F10T/F13T 합부 판정",
     {"document_id": "KDS 14 31 25",
      "key_rule": "F13T는 KS B 1010 수소지연파괴 시험성적표 첨부 제품만 사용 가능 — 미첨부 시 불합격"},
     "KDS 14 31 25 §4.1.3.3"),
    ("MaterialReceiptDecision", "kds14_31_25_welding_consumable_receipt",
     "용접재료 입고검수 결정 — 모재 매칭 강도 확인",
     {"document_id": "KDS 14 31 25",
      "key_rule": "용접금속 인장강도가 접합 모재 인장강도 이상인지 확인 (Matching Filler)"},
     "KDS 14 31 25 §4.1.2.4 표 4.1-3"),
    # ConstructionInspectionDecision
    ("ConstructionInspectionDecision", "kds14_31_20_weld_ut_inspection",
     "용접부 초음파탐상시험(UT) 판정",
     {"document_id": "KDS 14 31 20",
      "key_rule": "30개 표본 중 불합격 0~1개 합격, 2~3개 시 60개 재검사 후 4개 이하 합격, 5개 이상 불합격 (KS B 0896)"},
     "KDS 14 31 20 §3.15.2"),
    ("ConstructionInspectionDecision", "kds14_31_20_weld_rt_inspection",
     "용접부 방사선투과시험(RT) 판정",
     {"document_id": "KDS 14 31 20",
      "key_rule": "1종 결함(균열·용입불량) 불허, 2종 결함 크기·집계기준 KS B 0845 적용"},
     "KDS 14 31 20 §3.15"),
    ("ConstructionInspectionDecision", "kds14_31_20_weld_mt_inspection",
     "용접부 자분탐상(MT) 판정",
     {"document_id": "KDS 14 31 20",
      "key_rule": "표면 균열성 결함 불허, KS D 0213 합격기준 적용"},
     "KDS 14 31 20 §3.15"),
    ("ConstructionInspectionDecision", "kds14_31_25_bolt_torque_inspection",
     "고장력볼트 도입장력 검사 판정",
     {"document_id": "KDS 14 31 25",
      "key_rule": "조임 완료 볼트의 도입장력이 설계볼트장력 이상이며 표 4.1-10 기준 ±10% 이내"},
     "KDS 14 31 25 §4.1.3.1 표 4.1-10"),
    ("ConstructionInspectionDecision", "kds14_31_25_weld_visual_inspection",
     "용접부 육안검사 판정",
     {"document_id": "KDS 14 31 25",
      "key_rule": "균열·언더컷·오버랩·핀홀·과대비드 등 표면결함 발견 시 보수 또는 재시공"},
     "KDS 14 31 25 §4.1.2"),
    ("ConstructionInspectionDecision", "kds14_31_25_erection_tolerance_inspection",
     "강구조 설치 정밀도 검사 판정",
     {"document_id": "KDS 14 31 25",
      "key_rule": "기둥 수직도 1개 층 H/1000, 전체 누적 ±25 mm, 보 변위 한계 이내"},
     "KDS 14 31 25 §4.1.1"),
    ("ConstructionInspectionDecision", "kds14_31_50_fireproofing_inspection",
     "내화피복 시공 검사 판정",
     {"document_id": "KDS 14 31 50",
      "key_rule": "내화피복 두께·부착강도가 인정구조 또는 KS F 2257 시험성적 기준 만족 여부 확인"},
     "KDS 14 31 50 §4.3"),
    # StageApprovalDecision
    ("StageApprovalDecision", "kds14_31_25_fabrication_stage_approval",
     "강구조 제작 완료 단계승인",
     {"document_id": "KDS 14 31 25",
      "key_rule": "공장 제작 단계 — 절단·천공·용접·도장 완료 후 책임감리원이 단계승인 후 출하 허용"},
     "KDS 14 31 25 §4.1.1"),
    ("StageApprovalDecision", "kds14_31_25_erection_stage_approval",
     "강구조 설치 완료 단계승인",
     {"document_id": "KDS 14 31 25",
      "key_rule": "현장 조립 단계 — 모든 접합부 검사 완료, 정밀도 검사 합격 후 단계승인"},
     "KDS 14 31 25 §4.1.1 / §4.1.3"),
    ("StageApprovalDecision", "kds14_31_60_seismic_critical_weld_approval",
     "지진력저항시스템 임계용접부 단계승인",
     {"document_id": "KDS 14 31 60",
      "key_rule": "임계용접부 100% NDT 합격 및 보호영역·거셋 비탄성회전 상세 확인 후 단계승인"},
     "KDS 14 31 60 §1.8"),
    ("StageApprovalDecision", "kds14_31_70_existing_structure_evaluation_approval",
     "기존 강구조 평가결과 단계승인",
     {"document_id": "KDS 14 31 70",
      "key_rule": "재료실험·구조해석·재하실험 결과로 책임구조기술자가 내하력 적합성 판정·승인"},
     "KDS 14 31 70 §4.2 / §4.3"),
    # WorkPermitDecision
    ("WorkPermitDecision", "kds14_31_25_high_altitude_welding_permit",
     "고소 용접작업 작업허가",
     {"document_id": "KDS 14 31 25",
      "key_rule": "고소 강구조 용접작업은 안전관리자가 화기작업허가서·고소작업허가서 발급 후 시행"},
     "KDS 14 31 25 §4.1.2 (안전관리)"),
    # SafetyInspectionDecision
    ("SafetyInspectionDecision", "kds14_31_50_fire_safety_inspection",
     "강구조 내화구조 안전점검 결정",
     {"document_id": "KDS 14 31 50",
      "key_rule": "내화피복 손상·이격·박락 발견 시 보수 후 재점검 — 화재안전성 확보"},
     "KDS 14 31 50 §4.3"),
    # PrecisionDiagnosisDecision
    ("PrecisionDiagnosisDecision", "kds14_31_70_existing_steel_evaluation",
     "기존 강구조 정밀안전진단 — 인장물성·노치인성·내하력",
     {"document_id": "KDS 14 31 70",
      "key_rule": "기존 강구조 평가 — 인장물성·화학조성·노치인성 시험 + 구조해석 + 재하실험 종합"},
     "KDS 14 31 70 §4"),
]

decision_ids: dict[str, str] = {}
for dtype, nid, name, props, src in DECISIONS:
    nodes.append(n(dtype, nid, name, src, props))
    decision_ids[nid] = f"{dtype}:{nid}"

# ---------------- DecisionOutcome ----------------
OUTCOMES = [
    ("kds14_31_05_material_receipt_outcome",
     "강재 입고검수 결과 (합격/불합격)",
     {"possible_outcomes": ["합격 (입고 승인)", "불합격 (반품 또는 등급 강등)"],
      "key_rule": "Mill Test Certificate 부합·치수 허용오차 이내 시 합격"},
     "KDS 14 31 05 §3"),
    ("kds14_31_20_ndt_outcome",
     "비파괴검사 합격판정 결과",
     {"possible_outcomes": ["합격", "재검사", "불합격(보수 또는 재시공)"],
      "key_rule": "UT 30개 표본 중 2~3개 시 60개 재검사 → 4개 이하 합격, 5개 이상 불합격"},
     "KDS 14 31 20 §3.15"),
    ("kds14_31_25_bolt_inspection_outcome",
     "고장력볼트 검사 결과",
     {"possible_outcomes": ["합격 (장력 적합)", "재조임", "교체"],
      "key_rule": "도입장력 < 설계볼트장력일 경우 재조임, 불량 볼트는 교체"},
     "KDS 14 31 25 §4.1.3.1"),
    ("kds14_31_25_erection_tolerance_outcome",
     "설치 정밀도 검사 결과",
     {"possible_outcomes": ["합격", "보정 후 재검사", "재시공"],
      "key_rule": "기둥 수직도 1/1000 초과 시 보정, 전체 누적 ±25 mm 초과 시 재시공 검토"},
     "KDS 14 31 25 §4.1.1"),
    ("kds14_31_50_fire_test_outcome",
     "내화구조 품질시험 결과",
     {"possible_outcomes": ["합격 (내화시간 확보)", "불합격 (피복 보강 또는 재설계)"],
      "key_rule": "KS F 2257 내화시험에서 요구내화시간 이상 견디면 합격"},
     "KDS 14 31 50 §4.3.1"),
    ("kds14_31_70_load_test_outcome",
     "기존 강구조 재하실험 결과",
     {"possible_outcomes": ["내하력 적합", "내하력 부적합 (보강 필요)"],
      "key_rule": "1시간 유지 변형 증가 10% 이내 및 1.2D+1.6L 등치 실험강도 만족 시 적합"},
     "KDS 14 31 70 §4.3.1"),
]
outcome_ids: dict[str, str] = {}
for nid, name, props, src in OUTCOMES:
    nodes.append(n("DecisionOutcome", nid, name, src, props))
    outcome_ids[nid] = f"DecisionOutcome:{nid}"

# ---------------- EDGES ----------------

# concept (Qualification) grants_authority_for decision
edges.extend([
    e("Qualification:kds14_30_q_responsible_struct_eng", decision_ids["kds14_31_70_existing_structure_evaluation_approval"],
      "grants_authority_for", "KDS 14 31 70 §4"),
    e("Qualification:kds14_30_q_responsible_struct_eng", decision_ids["kds14_31_25_erection_stage_approval"],
      "grants_authority_for", "KDS 14 31 25 §4.1.1"),
    e("Qualification:kds14_30_q_responsible_struct_eng", decision_ids["kds14_31_60_seismic_critical_weld_approval"],
      "grants_authority_for", "KDS 14 31 60 §1.8"),
    e("Qualification:kds14_30_q_responsible_struct_eng", decision_ids["kds14_31_70_existing_steel_evaluation"],
      "grants_authority_for", "KDS 14 31 70 §4"),
    e("Qualification:kds14_30_q_welding_inspector", decision_ids["kds14_31_25_weld_visual_inspection"],
      "grants_authority_for", "KDS 14 31 25 §4.1.2"),
    e("Qualification:kds14_30_q_welding_inspector", decision_ids["kds14_31_25_bolt_torque_inspection"],
      "grants_authority_for", "KDS 14 31 25 §4.1.3.1"),
    e("Qualification:kds14_30_q_welding_inspector", decision_ids["kds14_31_25_erection_tolerance_inspection"],
      "grants_authority_for", "KDS 14 31 25 §4.1.1"),
    e("Qualification:kds14_30_q_ndt_level2", decision_ids["kds14_31_20_weld_ut_inspection"],
      "grants_authority_for", "KDS 14 31 20 §3.15"),
    e("Qualification:kds14_30_q_ndt_level2", decision_ids["kds14_31_20_weld_rt_inspection"],
      "grants_authority_for", "KDS 14 31 20 §3.15"),
    e("Qualification:kds14_30_q_ndt_level2", decision_ids["kds14_31_20_weld_mt_inspection"],
      "grants_authority_for", "KDS 14 31 20 §3.15"),
    e("Qualification:kds14_30_q_welder", decision_ids["kds14_31_25_welding_consumable_receipt"],
      "grants_authority_for", "KDS 14 31 25 §4.1.2.4"),
])

# subject performs decision
edges.extend([
    e("ChiefSupervisor:kds14_30_01_chief_supervisor", decision_ids["kds14_31_05_steel_material_receipt"],
      "performs", "KDS 14 31 05 §3"),
    e("ChiefSupervisor:kds14_30_01_chief_supervisor", decision_ids["kds14_31_25_fabrication_stage_approval"],
      "performs", "KDS 14 31 25 §4.1.1"),
    e("ChiefSupervisor:kds14_30_01_chief_supervisor", decision_ids["kds14_31_25_erection_stage_approval"],
      "performs", "KDS 14 31 25 §4.1.1"),
    e("ChiefSupervisor:kds14_30_01_chief_supervisor", decision_ids["kds14_31_60_seismic_critical_weld_approval"],
      "performs", "KDS 14 31 60 §1.8"),
    e("ChiefSupervisor:kds14_30_01_chief_supervisor", decision_ids["kds14_31_70_existing_structure_evaluation_approval"],
      "performs", "KDS 14 31 70 §4"),
    e("ChiefSupervisor:kds14_30_01_chief_supervisor", decision_ids["kds14_31_70_existing_steel_evaluation"],
      "performs", "KDS 14 31 70 §4"),
    e("Supervisor:kds14_30_02_supervisor", decision_ids["kds14_31_25_weld_visual_inspection"],
      "performs", "KDS 14 31 25 §4.1.2"),
    e("Supervisor:kds14_30_02_supervisor", decision_ids["kds14_31_25_bolt_torque_inspection"],
      "performs", "KDS 14 31 25 §4.1.3"),
    e("Supervisor:kds14_30_02_supervisor", decision_ids["kds14_31_25_erection_tolerance_inspection"],
      "performs", "KDS 14 31 25 §4.1.1"),
    e("Supervisor:kds14_30_02_supervisor", decision_ids["kds14_31_50_fireproofing_inspection"],
      "performs", "KDS 14 31 50 §4.3"),
    e("Supervisor:kds14_30_02_supervisor", decision_ids["kds14_31_25_hsfg_bolt_receipt"],
      "performs", "KDS 14 31 25 §4.1.3.3"),
    e("Org:kds14_30_05_certified_test_lab", decision_ids["kds14_31_20_weld_ut_inspection"],
      "performs", "KDS 14 31 20 §3.15"),
    e("Org:kds14_30_05_certified_test_lab", decision_ids["kds14_31_20_weld_rt_inspection"],
      "performs", "KDS 14 31 20 §3.15"),
    e("Org:kds14_30_05_certified_test_lab", decision_ids["kds14_31_20_weld_mt_inspection"],
      "performs", "KDS 14 31 20 §3.15"),
    e("SafetyManager:kds14_30_04_safety_manager", decision_ids["kds14_31_25_high_altitude_welding_permit"],
      "performs", "KDS 14 31 25 §4.1.2 (안전)"),
    e("SafetyManager:kds14_30_04_safety_manager", decision_ids["kds14_31_50_fire_safety_inspection"],
      "performs", "KDS 14 31 50 §4.3"),
    e("SiteEngineer:kds14_30_03_site_engineer", decision_ids["kds14_31_25_welding_consumable_receipt"],
      "performs", "KDS 14 31 25 §4.1.2.4"),
])

# decision targets_component / facility / work_type
edges.extend([
    # Material receipt targets components
    e(decision_ids["kds14_31_05_steel_material_receipt"], "StructuralComponent:kds14_30_sc_steel_column",
      "targets_component", "KDS 14 31 05 §3"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "StructuralComponent:kds14_30_sc_steel_beam",
      "targets_component", "KDS 14 31 05 §3"),
    e(decision_ids["kds14_31_25_hsfg_bolt_receipt"], "StructuralComponent:kds14_30_sc_hsfg_bolt",
      "targets_component", "KDS 14 31 25 §4.1.3"),
    e(decision_ids["kds14_31_25_welding_consumable_receipt"], "StructuralComponent:kds14_30_sc_groove_weld",
      "targets_component", "KDS 14 31 25 §4.1.2.4"),
    e(decision_ids["kds14_31_25_welding_consumable_receipt"], "StructuralComponent:kds14_30_sc_fillet_weld",
      "targets_component", "KDS 14 31 25 §4.1.2.4"),

    # NDT decisions target weld components
    e(decision_ids["kds14_31_20_weld_ut_inspection"], "StructuralComponent:kds14_30_sc_groove_weld",
      "targets_component", "KDS 14 31 20 §3.15"),
    e(decision_ids["kds14_31_20_weld_rt_inspection"], "StructuralComponent:kds14_30_sc_groove_weld",
      "targets_component", "KDS 14 31 20 §3.15"),
    e(decision_ids["kds14_31_20_weld_mt_inspection"], "StructuralComponent:kds14_30_sc_fillet_weld",
      "targets_component", "KDS 14 31 20 §3.15"),

    # Visual/torque/erection inspections target components
    e(decision_ids["kds14_31_25_weld_visual_inspection"], "StructuralComponent:kds14_30_sc_fillet_weld",
      "targets_component", "KDS 14 31 25 §4.1.2"),
    e(decision_ids["kds14_31_25_weld_visual_inspection"], "StructuralComponent:kds14_30_sc_groove_weld",
      "targets_component", "KDS 14 31 25 §4.1.2"),
    e(decision_ids["kds14_31_25_bolt_torque_inspection"], "StructuralComponent:kds14_30_sc_hsfg_bolt",
      "targets_component", "KDS 14 31 25 §4.1.3.1"),
    e(decision_ids["kds14_31_25_erection_tolerance_inspection"], "StructuralComponent:kds14_30_sc_steel_column",
      "targets_component", "KDS 14 31 25 §4.1.1"),
    e(decision_ids["kds14_31_25_erection_tolerance_inspection"], "StructuralComponent:kds14_30_sc_steel_beam",
      "targets_component", "KDS 14 31 25 §4.1.1"),

    # Stage approvals
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], "StructuralComponent:kds14_30_sc_connection",
      "targets_component", "KDS 14 31 25 §4.1.1"),
    e(decision_ids["kds14_31_25_erection_stage_approval"], "StructuralComponent:kds14_30_sc_steel_column",
      "targets_component", "KDS 14 31 25 §4.1.1"),
    e(decision_ids["kds14_31_25_erection_stage_approval"], "StructuralComponent:kds14_30_sc_steel_beam",
      "targets_component", "KDS 14 31 25 §4.1.1"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "StructuralComponent:kds14_30_sc_groove_weld",
      "targets_component", "KDS 14 31 60 §1.8"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "StructuralComponent:kds14_30_sc_gusset_plate",
      "targets_component", "KDS 14 31 60 §1.8"),

    # Fire / safety
    e(decision_ids["kds14_31_50_fireproofing_inspection"], "StructuralComponent:kds14_30_sc_steel_column",
      "targets_component", "KDS 14 31 50 §4"),
    e(decision_ids["kds14_31_50_fireproofing_inspection"], "StructuralComponent:kds14_30_sc_steel_beam",
      "targets_component", "KDS 14 31 50 §4"),
    e(decision_ids["kds14_31_50_fire_safety_inspection"], "Facility:kds14_30_fa_steel_building",
      "targets_facility", "KDS 14 31 50 §4"),

    # Existing structure evaluation
    e(decision_ids["kds14_31_70_existing_steel_evaluation"], "Facility:kds14_30_fa_steel_building",
      "targets_facility", "KDS 14 31 70 §4"),
    e(decision_ids["kds14_31_70_existing_structure_evaluation_approval"], "Facility:kds14_30_fa_steel_building",
      "targets_facility", "KDS 14 31 70 §4"),

    # Work permit
    e(decision_ids["kds14_31_25_high_altitude_welding_permit"], "WorkType:kds14_30_wt_welding",
      "targets_work_type", "KDS 14 31 25 §4.1.2"),

    # work_type targeting
    e(decision_ids["kds14_31_05_steel_material_receipt"], "WorkType:kds14_30_wt_fabrication",
      "targets_work_type", "KDS 14 31 05 §3"),
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], "WorkType:kds14_30_wt_fabrication",
      "targets_work_type", "KDS 14 31 25 §4"),
    e(decision_ids["kds14_31_25_erection_stage_approval"], "WorkType:kds14_30_wt_erection",
      "targets_work_type", "KDS 14 31 25 §4"),
    e(decision_ids["kds14_31_25_weld_visual_inspection"], "WorkType:kds14_30_wt_welding",
      "targets_work_type", "KDS 14 31 25 §4.1.2"),
    e(decision_ids["kds14_31_25_bolt_torque_inspection"], "WorkType:kds14_30_wt_bolting",
      "targets_work_type", "KDS 14 31 25 §4.1.3"),
    e(decision_ids["kds14_31_50_fireproofing_inspection"], "WorkType:kds14_30_wt_fireproofing",
      "targets_work_type", "KDS 14 31 50 §4"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "WorkType:kds14_30_wt_seismic_detailing",
      "targets_work_type", "KDS 14 31 60 §1.8"),
])

# decision based_on resource (Specification / TestReport / Checklist / Drawing)
edges.extend([
    # Steel material receipt based on specs and mill test certificate
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_05_steel_strength_ss235",
      "based_on", "KDS 14 30 05 §3.3.1"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_05_steel_strength_ss275",
      "based_on", "KDS 14 30 05 §3.3.1"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_05_steel_strength_sm355",
      "based_on", "KDS 14 30 05 §3.3.1"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_05_steel_strength_sm420",
      "based_on", "KDS 14 30 05 §3.3.1"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_05_steel_strength_sm460",
      "based_on", "KDS 14 30 05 §3.3.1"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_05_steel_strength_hsb690",
      "based_on", "KDS 14 30 05 §3.3.1"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_05_steel_strength_sn",
      "based_on", "KDS 14 30 05 §3.3.1"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "TestReport:kds14_31_05_mill_test_certificate",
      "based_on", "KDS 14 31 05 §3"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Checklist:kds14_31_05_material_receipt_checklist",
      "based_on", "KDS 14 31 05 §3"),

    # HSFG bolt receipt
    e(decision_ids["kds14_31_25_hsfg_bolt_receipt"], "Specification:kds14_31_25_bolt_F8T",
      "based_on", "KDS 14 31 25 §4.1.3.3"),
    e(decision_ids["kds14_31_25_hsfg_bolt_receipt"], "Specification:kds14_31_25_bolt_F10T",
      "based_on", "KDS 14 31 25 §4.1.3.3"),
    e(decision_ids["kds14_31_25_hsfg_bolt_receipt"], "Specification:kds14_31_25_bolt_F13T",
      "based_on", "KDS 14 31 25 §4.1.3.3"),
    e(decision_ids["kds14_31_25_hsfg_bolt_receipt"], "Specification:kds14_31_25_bolt_pretension_F10T",
      "based_on", "KDS 14 31 25 §4.1.3.1"),

    # Welding consumable
    e(decision_ids["kds14_31_25_welding_consumable_receipt"], "Specification:kds14_31_25_weld_filler_strength",
      "based_on", "KDS 14 31 25 §4.1.2.4"),

    # UT
    e(decision_ids["kds14_31_20_weld_ut_inspection"], "Specification:kds14_31_20_ut_acceptance",
      "based_on", "KDS 14 31 20 §3.15.2"),
    e(decision_ids["kds14_31_20_weld_ut_inspection"], "TestReport:kds14_31_20_ndt_report",
      "based_on", "KDS 14 31 20 §3.15"),
    # RT
    e(decision_ids["kds14_31_20_weld_rt_inspection"], "Specification:kds14_31_20_rt_acceptance",
      "based_on", "KDS 14 31 20 §3.15"),
    e(decision_ids["kds14_31_20_weld_rt_inspection"], "TestReport:kds14_31_20_ndt_report",
      "based_on", "KDS 14 31 20 §3.15"),
    # MT
    e(decision_ids["kds14_31_20_weld_mt_inspection"], "Specification:kds14_31_20_mt_pt_acceptance",
      "based_on", "KDS 14 31 20 §3.15"),
    e(decision_ids["kds14_31_20_weld_mt_inspection"], "TestReport:kds14_31_20_ndt_report",
      "based_on", "KDS 14 31 20 §3.15"),

    # Bolt torque
    e(decision_ids["kds14_31_25_bolt_torque_inspection"], "Specification:kds14_31_25_bolt_pretension_F10T",
      "based_on", "KDS 14 31 25 §4.1.3.1"),
    e(decision_ids["kds14_31_25_bolt_torque_inspection"], "Checklist:kds14_31_25_bolt_torque_checklist",
      "based_on", "KDS 14 31 25 §4.1.3"),
    e(decision_ids["kds14_31_25_bolt_torque_inspection"], "TestReport:kds14_31_25_bolt_inspection_report",
      "based_on", "KDS 14 31 25 §4.1.3.1"),

    # Weld visual
    e(decision_ids["kds14_31_25_weld_visual_inspection"], "Checklist:kds14_31_25_weld_visual_checklist",
      "based_on", "KDS 14 31 25 §4.1.2"),
    e(decision_ids["kds14_31_25_weld_visual_inspection"], "Specification:kds14_31_25_fillet_weld_throat",
      "based_on", "KDS 14 31 25 §4.1.2.2"),
    e(decision_ids["kds14_31_25_weld_visual_inspection"], "Specification:kds14_31_25_groove_weld_throat",
      "based_on", "KDS 14 31 25 §4.1.2.1"),

    # Erection tolerance
    e(decision_ids["kds14_31_25_erection_tolerance_inspection"], "Specification:kds14_31_25_erection_tolerance_column_plumb",
      "based_on", "KDS 14 31 25 §4.1.1"),
    e(decision_ids["kds14_31_25_erection_tolerance_inspection"], "Checklist:kds14_31_25_erection_dimension_checklist",
      "based_on", "KDS 14 31 25 §4.1.1"),

    # Fabrication stage approval
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], "Drawing:kds14_31_60_fabrication_drawing",
      "based_on", "KDS 14 31 60 §1.8.2"),
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], "Specification:kds14_31_25_phi_bolt",
      "based_on", "KDS 14 31 25"),

    # Erection stage approval
    e(decision_ids["kds14_31_25_erection_stage_approval"], "Drawing:kds14_31_60_erection_drawing",
      "based_on", "KDS 14 31 60 §1.8.3"),

    # Seismic critical weld approval
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "Drawing:kds14_31_60_structural_drawing",
      "based_on", "KDS 14 31 60 §1.8.1"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "Specification:kds14_31_60_critical_weld_marking",
      "based_on", "KDS 14 31 60 §1.8"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "Specification:kds14_31_60_steel_grade_requirement",
      "based_on", "KDS 14 31 60 §3.1"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "Specification:kds14_31_60_Ry_Rt_values",
      "based_on", "KDS 14 31 60 §3.2"),

    # Fireproofing inspection
    e(decision_ids["kds14_31_50_fireproofing_inspection"], "Specification:kds14_31_50_fire_resistance_test",
      "based_on", "KDS 14 31 50 §4.3.1"),
    e(decision_ids["kds14_31_50_fireproofing_inspection"], "Specification:kds14_31_50_structural_adequacy_time",
      "based_on", "KDS 14 31 50 §4.3.3.2"),
    e(decision_ids["kds14_31_50_fireproofing_inspection"], "TestReport:kds14_31_50_fire_test_report",
      "based_on", "KDS 14 31 50 §4.3.1"),
    e(decision_ids["kds14_31_50_fireproofing_inspection"], "Checklist:kds14_31_50_fireproofing_checklist",
      "based_on", "KDS 14 31 50 §4.3"),

    # Fire safety inspection
    e(decision_ids["kds14_31_50_fire_safety_inspection"], "Specification:kds14_31_50_fire_resistance_test",
      "based_on", "KDS 14 31 50 §4.3.1"),

    # Existing steel evaluation
    e(decision_ids["kds14_31_70_existing_steel_evaluation"], "Specification:kds14_31_70_load_test_acceptance",
      "based_on", "KDS 14 31 70 §4.3.1"),
    e(decision_ids["kds14_31_70_existing_steel_evaluation"], "TestReport:kds14_31_70_charpy_v_notch_test",
      "based_on", "KDS 14 31 70 §4.1.4"),
    e(decision_ids["kds14_31_70_existing_steel_evaluation"], "TestReport:kds14_31_05_mill_test_certificate",
      "based_on", "KDS 14 31 70 §4.1.2"),

    # Existing structure evaluation approval
    e(decision_ids["kds14_31_70_existing_structure_evaluation_approval"], "Specification:kds14_31_70_load_test_acceptance",
      "based_on", "KDS 14 31 70 §4.3"),
])

# decision precedes/depends_on decision (workflow ordering)
edges.extend([
    # material receipt precedes fabrication stage approval
    e(decision_ids["kds14_31_05_steel_material_receipt"], decision_ids["kds14_31_25_fabrication_stage_approval"],
      "precedes", "KDS 14 31 25 §4.1"),
    e(decision_ids["kds14_31_25_hsfg_bolt_receipt"], decision_ids["kds14_31_25_bolt_torque_inspection"],
      "precedes", "KDS 14 31 25 §4.1.3"),
    e(decision_ids["kds14_31_25_welding_consumable_receipt"], decision_ids["kds14_31_25_weld_visual_inspection"],
      "precedes", "KDS 14 31 25 §4.1.2"),
    # visual inspection precedes NDT
    e(decision_ids["kds14_31_25_weld_visual_inspection"], decision_ids["kds14_31_20_weld_ut_inspection"],
      "precedes", "KDS 14 31 20 §3.15"),
    e(decision_ids["kds14_31_25_weld_visual_inspection"], decision_ids["kds14_31_20_weld_rt_inspection"],
      "precedes", "KDS 14 31 20 §3.15"),
    e(decision_ids["kds14_31_25_weld_visual_inspection"], decision_ids["kds14_31_20_weld_mt_inspection"],
      "precedes", "KDS 14 31 20 §3.15"),
    # NDT results feed stage approval
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], "depends_on", "placeholder").update if False else None,  # noqa
])

# Cleanup: drop the spurious noop appended above
edges = [ed for ed in edges if ed is not None]

edges.extend([
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], decision_ids["kds14_31_20_weld_ut_inspection"],
      "depends_on", "KDS 14 31 20 §3.15 / KDS 14 31 25"),
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], decision_ids["kds14_31_25_weld_visual_inspection"],
      "depends_on", "KDS 14 31 25 §4.1.2"),
    e(decision_ids["kds14_31_25_erection_stage_approval"], decision_ids["kds14_31_25_bolt_torque_inspection"],
      "depends_on", "KDS 14 31 25 §4.1.3"),
    e(decision_ids["kds14_31_25_erection_stage_approval"], decision_ids["kds14_31_25_erection_tolerance_inspection"],
      "depends_on", "KDS 14 31 25 §4.1.1"),
    e(decision_ids["kds14_31_25_erection_stage_approval"], decision_ids["kds14_31_25_fabrication_stage_approval"],
      "depends_on", "KDS 14 31 25 §4.1.1"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], decision_ids["kds14_31_20_weld_ut_inspection"],
      "depends_on", "KDS 14 31 60 §1.8"),
    e(decision_ids["kds14_31_50_fireproofing_inspection"], decision_ids["kds14_31_25_erection_stage_approval"],
      "depends_on", "KDS 14 31 50 §4"),
    e(decision_ids["kds14_31_70_existing_structure_evaluation_approval"], decision_ids["kds14_31_70_existing_steel_evaluation"],
      "depends_on", "KDS 14 31 70 §4"),
    e(decision_ids["kds14_31_25_high_altitude_welding_permit"], decision_ids["kds14_31_25_weld_visual_inspection"],
      "precedes", "KDS 14 31 25 §4.1.2 (안전)"),
])

# decision yields outcome
edges.extend([
    e(decision_ids["kds14_31_05_steel_material_receipt"], outcome_ids["kds14_31_05_material_receipt_outcome"],
      "yields", "KDS 14 31 05 §3"),
    e(decision_ids["kds14_31_25_hsfg_bolt_receipt"], outcome_ids["kds14_31_05_material_receipt_outcome"],
      "yields", "KDS 14 31 25 §4.1.3"),
    e(decision_ids["kds14_31_25_welding_consumable_receipt"], outcome_ids["kds14_31_05_material_receipt_outcome"],
      "yields", "KDS 14 31 25 §4.1.2"),
    e(decision_ids["kds14_31_20_weld_ut_inspection"], outcome_ids["kds14_31_20_ndt_outcome"],
      "yields", "KDS 14 31 20 §3.15"),
    e(decision_ids["kds14_31_20_weld_rt_inspection"], outcome_ids["kds14_31_20_ndt_outcome"],
      "yields", "KDS 14 31 20 §3.15"),
    e(decision_ids["kds14_31_20_weld_mt_inspection"], outcome_ids["kds14_31_20_ndt_outcome"],
      "yields", "KDS 14 31 20 §3.15"),
    e(decision_ids["kds14_31_25_bolt_torque_inspection"], outcome_ids["kds14_31_25_bolt_inspection_outcome"],
      "yields", "KDS 14 31 25 §4.1.3.1"),
    e(decision_ids["kds14_31_25_erection_tolerance_inspection"], outcome_ids["kds14_31_25_erection_tolerance_outcome"],
      "yields", "KDS 14 31 25 §4.1.1"),
    e(decision_ids["kds14_31_50_fireproofing_inspection"], outcome_ids["kds14_31_50_fire_test_outcome"],
      "yields", "KDS 14 31 50 §4.3"),
    e(decision_ids["kds14_31_70_existing_steel_evaluation"], outcome_ids["kds14_31_70_load_test_outcome"],
      "yields", "KDS 14 31 70 §4.3"),
])

# concept -> concept (subclass / part_of) — section spec to broader work type
edges.extend([
    e("StructuralComponent:kds14_30_sc_steel_column", "Facility:kds14_30_fa_steel_building",
      "part_of", "KDS 14 31 05 §1"),
    e("StructuralComponent:kds14_30_sc_steel_beam", "Facility:kds14_30_fa_steel_building",
      "part_of", "KDS 14 31 05 §1"),
    e("StructuralComponent:kds14_30_sc_shear_wall", "Facility:kds14_30_fa_steel_building",
      "part_of", "KDS 14 31 60 §4"),
    e("StructuralComponent:kds14_30_sc_steel_beam", "Facility:kds14_30_fa_steel_bridge",
      "part_of", "KDS 14 31 10 §1"),
    e("StructuralComponent:kds14_30_sc_composite_beam", "Facility:kds14_30_fa_composite_structure",
      "part_of", "KDS 14 31 80 §4"),
    e("StructuralComponent:kds14_30_sc_composite_column", "Facility:kds14_30_fa_composite_structure",
      "part_of", "KDS 14 31 80 §4"),
    e("WorkType:kds14_30_wt_welding", "WorkType:kds14_30_wt_fabrication",
      "part_of", "KDS 14 31 25 §4.1.2"),
    e("WorkType:kds14_30_wt_welding", "WorkType:kds14_30_wt_erection",
      "part_of", "KDS 14 31 25 §4.1.2"),
    e("WorkType:kds14_30_wt_bolting", "WorkType:kds14_30_wt_erection",
      "part_of", "KDS 14 31 25 §4.1.3"),
    e("WorkType:kds14_30_wt_painting", "WorkType:kds14_30_wt_fabrication",
      "part_of", "KDS 14 30 50 §4.5"),
    e("WorkType:kds14_30_wt_fireproofing", "WorkType:kds14_30_wt_erection",
      "part_of", "KDS 14 31 50 §4"),
    e("WorkType:kds14_30_wt_seismic_detailing", "WorkType:kds14_30_wt_erection",
      "part_of", "KDS 14 31 60 §1.8"),
    e("WorkType:kds14_30_wt_composite_construction", "WorkType:kds14_30_wt_erection",
      "part_of", "KDS 14 31 80 §4"),
    # ASD vs LRFD subclass relation: both are sub-classes of design work; we keep them as sibling concepts via related_to-like 'depends_on'
    e("WorkType:kds14_30_wt_steel_design", "WorkType:kds14_30_wt_fabrication",
      "depends_on", "KDS 14 30 05 §1.1"),
    e("WorkType:kds14_30_wt_steel_design_lrfd", "WorkType:kds14_30_wt_fabrication",
      "depends_on", "KDS 14 31 05 §1"),
])

# Hook remaining structural components into the graph (avoid orphans).
edges.extend([
    e("StructuralComponent:kds14_30_sc_steel_brace", "Facility:kds14_30_fa_steel_building",
      "part_of", "KDS 14 31 60 §4"),
    e("StructuralComponent:kds14_30_sc_deck_plate", "Facility:kds14_30_fa_steel_building",
      "part_of", "KDS 14 30 05 §1.2"),
    e("StructuralComponent:kds14_30_sc_diaphragm", "Facility:kds14_30_fa_steel_building",
      "part_of", "KDS 14 30 05 §1.2"),
    e("StructuralComponent:kds14_30_sc_anchor_bolt", "StructuralComponent:kds14_30_sc_connection",
      "part_of", "KDS 14 30 05 §1.2"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "StructuralComponent:kds14_30_sc_steel_brace",
      "targets_component", "KDS 14 31 60 §4"),
    e(decision_ids["kds14_31_25_erection_tolerance_inspection"], "StructuralComponent:kds14_30_sc_anchor_bolt",
      "targets_component", "KDS 14 31 25 §4.1.1"),
])

# ---------------- Section root specifications: contain quantitative specifications (resource->resource? Not allowed)
# Instead, link decisions to root section specs as additional based_on to make root specs reachable.
edges.extend([
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_05_section_root",
      "based_on", "KDS 14 30 05"),
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], "Specification:kds14_31_25_section_root",
      "based_on", "KDS 14 31 25"),
    e(decision_ids["kds14_31_25_erection_stage_approval"], "Specification:kds14_31_25_section_root",
      "based_on", "KDS 14 31 25"),
    e(decision_ids["kds14_31_25_weld_visual_inspection"], "Specification:kds14_31_25_section_root",
      "based_on", "KDS 14 31 25"),
    e(decision_ids["kds14_31_25_bolt_torque_inspection"], "Specification:kds14_31_25_section_root",
      "based_on", "KDS 14 31 25"),
    e(decision_ids["kds14_31_25_erection_tolerance_inspection"], "Specification:kds14_31_25_section_root",
      "based_on", "KDS 14 31 25"),
    e(decision_ids["kds14_31_20_weld_ut_inspection"], "Specification:kds14_31_20_section_root",
      "based_on", "KDS 14 31 20"),
    e(decision_ids["kds14_31_20_weld_rt_inspection"], "Specification:kds14_31_20_section_root",
      "based_on", "KDS 14 31 20"),
    e(decision_ids["kds14_31_20_weld_mt_inspection"], "Specification:kds14_31_20_section_root",
      "based_on", "KDS 14 31 20"),
    e(decision_ids["kds14_31_50_fireproofing_inspection"], "Specification:kds14_31_50_section_root",
      "based_on", "KDS 14 31 50"),
    e(decision_ids["kds14_31_50_fire_safety_inspection"], "Specification:kds14_31_50_section_root",
      "based_on", "KDS 14 31 50"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "Specification:kds14_31_60_section_root",
      "based_on", "KDS 14 31 60"),
    e(decision_ids["kds14_31_70_existing_steel_evaluation"], "Specification:kds14_31_70_section_root",
      "based_on", "KDS 14 31 70"),
    e(decision_ids["kds14_31_70_existing_structure_evaluation_approval"], "Specification:kds14_31_70_section_root",
      "based_on", "KDS 14 31 70"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_31_05_section_root",
      "based_on", "KDS 14 31 05"),
    e(decision_ids["kds14_31_25_hsfg_bolt_receipt"], "Specification:kds14_31_25_section_root",
      "based_on", "KDS 14 31 25"),
    e(decision_ids["kds14_31_25_welding_consumable_receipt"], "Specification:kds14_31_25_section_root",
      "based_on", "KDS 14 31 25"),
    e(decision_ids["kds14_31_25_high_altitude_welding_permit"], "Specification:kds14_31_25_section_root",
      "based_on", "KDS 14 31 25"),
])

# Link the remaining root sections that don't already have a decision -> spec edge.
# Each root spec gains at least one decision -> spec edge:
edges.extend([
    # ASD section roots reachable from material receipt + fabrication
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_10_section_root",
      "based_on", "KDS 14 30 10"),
    e(decision_ids["kds14_31_05_steel_material_receipt"], "Specification:kds14_30_20_section_root",
      "based_on", "KDS 14 30 20"),
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], "Specification:kds14_30_25_section_root",
      "based_on", "KDS 14 30 25"),
    e(decision_ids["kds14_31_25_erection_stage_approval"], "Specification:kds14_30_50_section_root",
      "based_on", "KDS 14 30 50"),
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], "Specification:kds14_31_10_section_root",
      "based_on", "KDS 14 31 10"),
    e(decision_ids["kds14_31_25_fabrication_stage_approval"], "Specification:kds14_31_15_section_root",
      "based_on", "KDS 14 31 15"),
    e(decision_ids["kds14_31_25_erection_stage_approval"], "Specification:kds14_31_55_section_root",
      "based_on", "KDS 14 31 55"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "Specification:kds14_31_80_section_root",
      "based_on", "KDS 14 31 80"),
    e(decision_ids["kds14_31_60_seismic_critical_weld_approval"], "Specification:kds14_31_85_section_root",
      "based_on", "KDS 14 31 85"),
])

# All remaining quantitative specs are reachable via at least one decision based_on edge.
# Add fallback based_on edges to keep every Specification orphan-free.
# We will check at the end and add edges as needed for missing specs.

# Decisions->Specifications missing-coverage map
covered_specs = {ed["to_node_id"] for ed in edges if ed["relation"] == "based_on" and ed["to_node_id"].startswith("Specification:")}
for sid in [f"Specification:{nid}" for nid, *_ in QUANT_SPECS]:
    if sid not in covered_specs:
        edges.append(e(decision_ids["kds14_31_25_fabrication_stage_approval"], sid,
                       "based_on", "KDS 14 31 25 (보강 링크)"))

# ---------------------------------------------------------------------------
# Validate (orphans, duplicates, grammar)
# ---------------------------------------------------------------------------

node_ids = {nd["node_id"] for nd in nodes}
assert len(node_ids) == len(nodes), "duplicate node ids"

# Every edge endpoint must exist
for ed in edges:
    if ed["from_node_id"] not in node_ids:
        raise SystemExit(f"missing source: {ed['from_node_id']}")
    if ed["to_node_id"] not in node_ids:
        raise SystemExit(f"missing target: {ed['to_node_id']}")

# Orphan check: every node must appear in at least one edge OR be a root anchor we allow.
referenced = set()
for ed in edges:
    referenced.add(ed["from_node_id"])
    referenced.add(ed["to_node_id"])

orphans = [nid for nid in node_ids if nid not in referenced]
if orphans:
    raise SystemExit(f"orphan nodes ({len(orphans)}): {orphans[:10]}")

# ---------------------------------------------------------------------------
# Write JSONL
# ---------------------------------------------------------------------------

out_path = Path(r"C:/temp/opencrab-civil_engineering_pack/extracted/standards/kds/KDS_14_30_31.jsonl")
out_path.parent.mkdir(parents=True, exist_ok=True)

with out_path.open("w", encoding="utf-8") as fh:
    for nd in nodes:
        fh.write(json.dumps(nd, ensure_ascii=False) + "\n")
    for ed in edges:
        fh.write(json.dumps(ed, ensure_ascii=False) + "\n")

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

from collections import Counter
type_counter = Counter(nd["node_type"] for nd in nodes)
rel_counter = Counter(ed["relation"] for ed in edges)
print(f"WROTE: {out_path}")
print(f"size_bytes={out_path.stat().st_size}")
print(f"nodes={len(nodes)} edges={len(edges)}")
print("---- node_type distribution ----")
for k, v in sorted(type_counter.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
print("---- relation distribution ----")
for k, v in sorted(rel_counter.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
