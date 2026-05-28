# Extracted graph — KDS_14_20.jsonl

_source jsonl: KDS_14_20.jsonl_

## Nodes

## Node — Org / `Org:kcsc-kds1420`
- space: `subject`
- node_type: `Org`
- source_article: KDS 14 20 sec1
- properties:
  - `name_ko`: 국가건설기준센터
  - `role`: KDS 14 20 설계기준 관리

## Node — Org / `Org:ordering-agency-kds1420`
- space: `subject`
- node_type: `Org`
- source_article: KDS 14 20 sec7
- properties:
  - `name_ko`: 발주자(인허가권자)
  - `scope`: 강도설계법 외 설계방법 적용 시 승인 권한, 설계기준 변경 승인

## Node — SiteEngineer / `SiteEngineer:kds14_20_sec7_responsible-design-engineer`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KDS 14 20 sec7-1
- properties:
  - `name_ko`: 책임구조기술자
  - `duties`: ["구조설계 도면·계산서·시방서 작성", "설계기준 변경 검토", "강도설계법 외 설계방법 적용 검토"]
  - `source_standard`: KDS 14 20 01

## Node — SiteEngineer / `SiteEngineer:kds14_20_sec7-2_construction`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KDS 14 20 sec7-2
- properties:
  - `name_ko`: 시공자
  - `duties`: ["설계기준에 따라 시공", "설계기준 준수"]
  - `source_standard`: KDS 14 20 01

## Node — Supervisor / `Supervisor:kds14_20_sec7-2_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: KDS 14 20 sec7-2
- properties:
  - `name_ko`: 감리자
  - `duties`: ["시공자가 설계기준 준수 여부 검측"]
  - `source_standard`: KDS 14 20 01

## Node — Qualification / `Qualification:kds14_20_responsible-design-engineer`
- space: `concept`
- node_type: `Qualification`
- source_article: KDS 14 20 sec7-1
- properties:
  - `name_ko`: 책임구조기술자 자격
  - `scope`: 콘크리트구조 설계 도면·계산서·시방서 작성 및 검토
  - `source_standard`: KDS 14 20 01

## Node — Qualification / `Qualification:kds14_20_supervisor`
- space: `concept`
- node_type: `Qualification`
- source_article: KDS 14 20 sec7-2
- properties:
  - `name_ko`: 콘크리트구조 감리자 자격
  - `scope`: 설계기준 준수 검측
  - `source_standard`: KDS 14 20 01

## Node — WorkType / `WorkType:kds14_20_concrete-design`
- space: `concept`
- node_type: `WorkType`
- source_article: KDS 14 20 sec2
- properties:
  - `name_ko`: 콘크리트구조 설계
  - `scope`: 철근콘크리트·프리스트레스트콘크리트 설계
  - `source_standard`: KDS 14 20 01

## Node — StructuralComponent / `StructuralComponent:kds14_20_rc-member`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KDS 14 20 sec2
- properties:
  - `name_ko`: 철근콘크리트 부재
  - `source_standard`: KDS 14 20 01

## Node — StructuralComponent / `StructuralComponent:kds14_20_pc-member`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KDS 14 20 sec2
- properties:
  - `name_ko`: 프리스트레스트콘크리트 부재
  - `source_standard`: KDS 14 20 01

## Node — StructuralComponent / `StructuralComponent:kds14_20_tension-section`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KDS 14 20 sec4-1
- properties:
  - `name_ko`: 인장지배단면
  - `source_standard`: KDS 14 20 10 4.1

## Node — StructuralComponent / `StructuralComponent:kds14_20_compression-section`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KDS 14 20 sec4-1
- properties:
  - `name_ko`: 압축지배단면
  - `source_standard`: KDS 14 20 10 4.1

## Node — Specification / `Specification:kds14_20_01`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec1
- properties:
  - `name_ko`: KDS 14 20 01 콘크리트구조 설계 일반사항
  - `code`: KDS 14 20 01
  - `legal_basis`: 건설기술 진흥법 제44조, 시행령 제65조
  - `notice`: 국토교통부고시 제2024-879호 (2024-12-30)

## Node — Specification / `Specification:kds14_20_10`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec4
- properties:
  - `name_ko`: KDS 14 20 10 해석과 설계 - 하중 및 강도감소계수
  - `code`: KDS 14 20 10

## Node — Specification / `Specification:kds14_20_nominal-strength`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec3-1
- properties:
  - `name_ko`: 호칭강도 정의
  - `requirement`: 레디믹스트 콘크리트 주문 시 강도 표시값, 단위 MPa, 통상 18·21·24·27·30·35·40 MPa
  - `unit`: MPa
  - `typical_values`: [18, 21, 24, 27, 30, 35, 40]
  - `source_standard`: KDS 14 20 01 3.1

## Node — Specification / `Specification:kds14_20_fck`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec3-2
- properties:
  - `name_ko`: 설계기준압축강도 fck
  - `requirement`: 구조 부재 설계 시 기준이 되는 콘크리트 압축강도, 호칭강도와 동등 또는 그 이상으로 결정
  - `symbol`: fck
  - `unit`: MPa
  - `general_range_MPa`: 21-40
  - `high_strength_MPa`: [50, 60, 70, 80]
  - `source_standard`: KDS 14 20 01 3.2

## Node — Specification / `Specification:kds14_20_fy`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec3-3
- properties:
  - `name_ko`: 설계기준항복강도 fy
  - `requirement`: 철근 설계 기준 항복강도; SD400=400 MPa, SD500=500 MPa, SD600=600 MPa, 휨 설계용 철근 fy ≤ 600 MPa
  - `symbol`: fy
  - `unit`: MPa
  - `SD400_MPa`: 400
  - `SD500_MPa`: 500
  - `SD600_MPa`: 600
  - `flexural_max_MPa`: 600
  - `source_standard`: KDS 14 20 01 3.3 / 6.2

## Node — Specification / `Specification:kds14_20_phi-tension`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec4-1
- properties:
  - `name_ko`: 강도감소계수 φ - 인장지배단면
  - `symbol`: φ
  - `value`: 0.85
  - `scope`: 휨모멘트 또는 휨모멘트+축력
  - `source_standard`: KDS 14 20 10 4.1

## Node — Specification / `Specification:kds14_20_phi-compression-spiral`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec4-1
- properties:
  - `name_ko`: 강도감소계수 φ - 압축지배단면(나선철근)
  - `symbol`: φ
  - `value`: 0.7
  - `source_standard`: KDS 14 20 10 4.1

## Node — Specification / `Specification:kds14_20_phi-compression-other`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec4-1
- properties:
  - `name_ko`: 강도감소계수 φ - 압축지배단면(그 외)
  - `symbol`: φ
  - `value`: 0.65
  - `source_standard`: KDS 14 20 10 4.1

## Node — Specification / `Specification:kds14_20_phi-transition`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec4-1
- properties:
  - `name_ko`: 강도감소계수 φ - 변화구간단면
  - `symbol`: φ
  - `range`: 0.65-0.85
  - `method`: 보간
  - `source_standard`: KDS 14 20 10 4.1

## Node — Specification / `Specification:kds14_20_phi-shear-torsion`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec4-2
- properties:
  - `name_ko`: 강도감소계수 φ - 전단력·비틀림
  - `symbol`: φ
  - `value`: 0.75
  - `source_standard`: KDS 14 20 10 4.2

## Node — Specification / `Specification:kds14_20_phi-bearing`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec4-3
- properties:
  - `name_ko`: 강도감소계수 φ - 콘크리트 지압
  - `symbol`: φ
  - `value`: 0.65
  - `exclusion`: 포스트텐션 정착부 제외
  - `source_standard`: KDS 14 20 10 4.3

## Node — Specification / `Specification:kds14_20_phi-plain`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec4-4
- properties:
  - `name_ko`: 강도감소계수 φ - 무근콘크리트
  - `symbol`: φ
  - `value`: 0.55
  - `scope`: 휨모멘트·압축력·전단력·지압력
  - `source_standard`: KDS 14 20 10 4.4

## Node — Specification / `Specification:kds14_20_load-combination`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec5
- properties:
  - `name_ko`: 하중계수 조합
  - `combinations`: ["U = 1.4D", "U = 1.2D + 1.6L + 0.5(Lr 또는 S 또는 R)", "U = 1.2D + 1.6(Lr 또는 S 또는 R) + (1.0L 또는 0.5W)"]
  - `symbols`: {"D": "고정하중", "L": "활하중", "W": "풍하중", "E": "지진하중", "S": "적설하중", "Lr": "지붕활하중", "R": "빗물하중"}
  - `source_standard`: KDS 14 20 10 5

## Node — Specification / `Specification:kds14_20_ec`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec6-3
- properties:
  - `name_ko`: 콘크리트 탄성계수 Ec
  - `formula`: Ec = 8500 × ∛fcm (MPa)
  - `fcm_def`: fck + 4 (fck ≤ 40 MPa); fck + Δf (fck > 40 MPa)
  - `unit`: MPa
  - `source_standard`: KDS 14 20 10 6.3

## Node — Specification / `Specification:kds14_20_design-method`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec2
- properties:
  - `name_ko`: 설계법 기준
  - `requirement`: 강도설계법 적용을 원칙으로 함; 외 설계방법 적용 시 책임구조기술자 검토 및 발주자(인허가권자) 승인 필요
  - `default_method`: 강도설계법
  - `source_standard`: KDS 14 20 01 2

## Node — Drawing / `Drawing:kds14_20_structural-drawing`
- space: `resource`
- node_type: `Drawing`
- source_article: KDS 14 20 sec7-1
- properties:
  - `name_ko`: 구조설계 도면
  - `author`: 책임구조기술자
  - `source_standard`: KDS 14 20 01 7.1

## Node — Specification / `Specification:kds14_20_calculation`
- space: `resource`
- node_type: `Specification`
- source_article: KDS 14 20 sec7-1
- properties:
  - `name_ko`: 구조계산서
  - `author`: 책임구조기술자
  - `source_standard`: KDS 14 20 01 7.1

## Node — StageApprovalDecision / `StageApprovalDecision:kds14_20_sec7-1_design-review`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KDS 14 20 sec7-1
- properties:
  - `name_ko`: 구조설계 검토·승인
  - `description`: 책임구조기술자가 작성한 구조설계 도면·계산서·시방서를 발주자(또는 인허가권자)가 검토·승인
  - `source_standard`: KDS 14 20 01 7.1

## Node — StageApprovalDecision / `StageApprovalDecision:kds14_20_alt-method`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KDS 14 20 sec2
- properties:
  - `name_ko`: 강도설계법 외 설계방법 승인
  - `description`: 강도설계법 외 설계방법 적용 시 책임구조기술자 검토 및 발주자(인허가권자) 승인
  - `source_standard`: KDS 14 20 01 2

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:kds14_20_sec7-2_compliance`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KDS 14 20 sec7-2
- properties:
  - `name_ko`: 설계기준 준수 검측
  - `description`: 감리자가 시공 단계에서 시공자가 설계기준(KDS 14 20)을 준수하는지 검측
  - `source_standard`: KDS 14 20 01 7.2

## Node — StageApprovalDecision / `StageApprovalDecision:kds14_20_design-change`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KDS 14 20 sec7-2
- properties:
  - `name_ko`: 설계기준 변경 승인
  - `description`: 설계기준 변경 사항은 책임구조기술자 검토 후 발주자 승인
  - `source_standard`: KDS 14 20 01 7.2

## Node — DecisionOutcome / `DecisionOutcome:kds14_20_design-approved`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KDS 14 20 sec7-1
- properties:
  - `name_ko`: 구조설계 승인
  - `result`: approved

## Node — DecisionOutcome / `DecisionOutcome:kds14_20_compliance-pass`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KDS 14 20 sec7-2
- properties:
  - `name_ko`: 설계기준 준수 합격
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:kds14_20_compliance-fail`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KDS 14 20 sec7-2
- properties:
  - `name_ko`: 설계기준 미준수
  - `result`: fail
  - `next_action`: 시정 후 재검측

## Edges

## Edge — `qualified_as`
- from: `SiteEngineer:kds14_20_sec7_responsible-design-engineer` (subject)
- to: `Qualification:kds14_20_responsible-design-engineer` (concept)
- source_article: KDS 14 20 sec7-1

## Edge — `qualified_as`
- from: `Supervisor:kds14_20_sec7-2_01` (subject)
- to: `Qualification:kds14_20_supervisor` (concept)
- source_article: KDS 14 20 sec7-2

## Edge — `part_of`
- from: `StructuralComponent:kds14_20_tension-section` (concept)
- to: `StructuralComponent:kds14_20_rc-member` (concept)
- source_article: KDS 14 20 sec4-1

## Edge — `part_of`
- from: `StructuralComponent:kds14_20_compression-section` (concept)
- to: `StructuralComponent:kds14_20_rc-member` (concept)
- source_article: KDS 14 20 sec4-1

## Edge — `subclass_of`
- from: `StructuralComponent:kds14_20_pc-member` (concept)
- to: `StructuralComponent:kds14_20_rc-member` (concept)
- source_article: KDS 14 20 sec2

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_responsible-design-engineer` (concept)
- to: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- source_article: KDS 14 20 sec7-1

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_responsible-design-engineer` (concept)
- to: `StageApprovalDecision:kds14_20_alt-method` (decision)
- source_article: KDS 14 20 sec2

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_responsible-design-engineer` (concept)
- to: `StageApprovalDecision:kds14_20_design-change` (decision)
- source_article: KDS 14 20 sec7-2

## Edge — `grants_authority_for`
- from: `Qualification:kds14_20_supervisor` (concept)
- to: `ConstructionInspectionDecision:kds14_20_sec7-2_compliance` (decision)
- source_article: KDS 14 20 sec7-2

## Edge — `performs`
- from: `SiteEngineer:kds14_20_sec7_responsible-design-engineer` (subject)
- to: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- source_article: KDS 14 20 sec7-1

## Edge — `performs`
- from: `Supervisor:kds14_20_sec7-2_01` (subject)
- to: `ConstructionInspectionDecision:kds14_20_sec7-2_compliance` (decision)
- source_article: KDS 14 20 sec7-2

## Edge — `targets_work_type`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `WorkType:kds14_20_concrete-design` (concept)
- source_article: KDS 14 20 sec2

## Edge — `targets_work_type`
- from: `StageApprovalDecision:kds14_20_alt-method` (decision)
- to: `WorkType:kds14_20_concrete-design` (concept)
- source_article: KDS 14 20 sec2

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:kds14_20_sec7-2_compliance` (decision)
- to: `StructuralComponent:kds14_20_rc-member` (concept)
- source_article: KDS 14 20 sec7-2

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:kds14_20_sec7-2_compliance` (decision)
- to: `StructuralComponent:kds14_20_pc-member` (concept)
- source_article: KDS 14 20 sec7-2

## Edge — `targets_work_type`
- from: `StageApprovalDecision:kds14_20_design-change` (decision)
- to: `WorkType:kds14_20_concrete-design` (concept)
- source_article: KDS 14 20 sec7-2

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_01` (resource)
- source_article: KDS 14 20 sec1

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_10` (resource)
- source_article: KDS 14 20 sec4

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_fck` (resource)
- source_article: KDS 14 20 sec3-2

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_fy` (resource)
- source_article: KDS 14 20 sec3-3

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_phi-tension` (resource)
- source_article: KDS 14 20 sec4-1

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_phi-compression-spiral` (resource)
- source_article: KDS 14 20 sec4-1

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_phi-compression-other` (resource)
- source_article: KDS 14 20 sec4-1

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_phi-transition` (resource)
- source_article: KDS 14 20 sec4-1

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_phi-shear-torsion` (resource)
- source_article: KDS 14 20 sec4-2

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_phi-bearing` (resource)
- source_article: KDS 14 20 sec4-3

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_phi-plain` (resource)
- source_article: KDS 14 20 sec4-4

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_load-combination` (resource)
- source_article: KDS 14 20 sec5

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_ec` (resource)
- source_article: KDS 14 20 sec6-3

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_nominal-strength` (resource)
- source_article: KDS 14 20 sec3-1

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Drawing:kds14_20_structural-drawing` (resource)
- source_article: KDS 14 20 sec7-1

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `Specification:kds14_20_calculation` (resource)
- source_article: KDS 14 20 sec7-1

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_alt-method` (decision)
- to: `Specification:kds14_20_design-method` (resource)
- source_article: KDS 14 20 sec2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_sec7-2_compliance` (decision)
- to: `Specification:kds14_20_01` (resource)
- source_article: KDS 14 20 sec7-2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kds14_20_sec7-2_compliance` (decision)
- to: `Drawing:kds14_20_structural-drawing` (resource)
- source_article: KDS 14 20 sec7-2

## Edge — `based_on`
- from: `StageApprovalDecision:kds14_20_design-change` (decision)
- to: `Specification:kds14_20_01` (resource)
- source_article: KDS 14 20 sec7-2

## Edge — `precedes`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `ConstructionInspectionDecision:kds14_20_sec7-2_compliance` (decision)
- source_article: KDS 14 20 sec7-2

## Edge — `depends_on`
- from: `StageApprovalDecision:kds14_20_alt-method` (decision)
- to: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- source_article: KDS 14 20 sec2

## Edge — `depends_on`
- from: `StageApprovalDecision:kds14_20_design-change` (decision)
- to: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- source_article: KDS 14 20 sec7-2

## Edge — `yields`
- from: `StageApprovalDecision:kds14_20_sec7-1_design-review` (decision)
- to: `DecisionOutcome:kds14_20_design-approved` (outcome)
- source_article: KDS 14 20 sec7-1

## Edge — `yields`
- from: `ConstructionInspectionDecision:kds14_20_sec7-2_compliance` (decision)
- to: `DecisionOutcome:kds14_20_compliance-pass` (outcome)
- source_article: KDS 14 20 sec7-2

## Edge — `yields`
- from: `ConstructionInspectionDecision:kds14_20_sec7-2_compliance` (decision)
- to: `DecisionOutcome:kds14_20_compliance-fail` (outcome)
- source_article: KDS 14 20 sec7-2
