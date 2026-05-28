# Extracted graph — KCS_14_31.jsonl

_source jsonl: KCS_14_31.jsonl_

## Nodes

## Node — Org / `Org:kcsc-kcs1431`
- space: `subject`
- node_type: `Org`
- source_article: KCS 14 31 sec1
- properties:
  - `name_ko`: 국가건설기준센터
  - `role`: KCS 14 31 표준 관리

## Node — SiteEngineer / `SiteEngineer:kcs14_31_sec7_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS 14 31 sec7
- properties:
  - `name_ko`: 강구조 시공자
  - `duties`: ["밀시트·시험성적서 첨부", "시공계획서 작성·제출", "정밀도 관리", "용접·고장력볼트 시공"]
  - `source_standard`: KCS 14 31 05

## Node — Supervisor / `Supervisor:kcs14_31_sec7_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: KCS 14 31 sec7
- properties:
  - `name_ko`: 감리자(책임기술자)
  - `duties`: ["자재 검수", "용접 검측", "비파괴검사 결과 판정", "정밀도 검수", "시공 검측 및 승인"]
  - `source_standard`: KCS 14 31 05 / 20

## Node — ChiefSupervisor / `ChiefSupervisor:kcs14_31_sec7_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: KCS 14 31 sec7
- properties:
  - `name_ko`: 책임감리원
  - `scope`: 강구조공사 자재·용접·정밀도 종합 승인 총괄
  - `source_standard`: KCS 14 31 05

## Node — SiteEngineer / `SiteEngineer:kcs14_31_sec6-1_welder`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS 14 31 sec6-1
- properties:
  - `name_ko`: 용접기능자
  - `scope`: 수동·반자동 아크용접 종사자
  - `qualification`: 용접기술 승인시험 합격 유자격자
  - `source_standard`: KCS 14 31 20 3.2.3

## Node — SiteEngineer / `SiteEngineer:kcs14_31_sec6-2_ndt`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS 14 31 sec6-2
- properties:
  - `name_ko`: 비파괴검사자
  - `qualification`: KS B ISO 9712 레벨 2 이상 해당 종목 자격
  - `source_standard`: KCS 14 31 20 3.2.4

## Node — Qualification / `Qualification:kcs14_31_welder`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 14 31 sec6-1
- properties:
  - `name_ko`: 용접기능자 자격
  - `requirement`: 용접기술 승인시험 합격 유자격자
  - `source_standard`: KCS 14 31 20 3.2.3

## Node — Qualification / `Qualification:kcs14_31_ndt-inspector`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 14 31 sec6-2
- properties:
  - `name_ko`: 비파괴검사자 자격
  - `requirement`: KS B ISO 9712 레벨 2 이상
  - `ks_code`: KS B ISO 9712
  - `level`: ≥ 2
  - `source_standard`: KCS 14 31 20 3.2.4

## Node — Qualification / `Qualification:kcs14_31_supervisor`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 14 31 sec7
- properties:
  - `name_ko`: 강구조공사 감리자(책임기술자) 자격
  - `scope`: 자재 검수·용접 검측·정밀도 판정·비파괴검사 결과 판정
  - `source_standard`: KCS 14 31 05

## Node — Qualification / `Qualification:kcs14_31_chief-supervisor`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 14 31 sec7
- properties:
  - `name_ko`: 강구조공사 책임감리원 자격
  - `scope`: 강구조공사 종합 승인 총괄
  - `source_standard`: KCS 14 31 05

## Node — WorkType / `WorkType:kcs14_31_steel-work`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 31 sec2
- properties:
  - `name_ko`: 강구조공사
  - `scope`: 주요부재를 강재로 사용하는 강구조 건축물·공작물 공사
  - `source_standard`: KCS 14 31 05

## Node — WorkType / `WorkType:kcs14_31_welding`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 31 sec6
- properties:
  - `name_ko`: 용접 공사
  - `source_standard`: KCS 14 31 20

## Node — StructuralComponent / `StructuralComponent:kcs14_31_steel-member`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 31 sec3-2
- properties:
  - `name_ko`: 강재 부재
  - `source_standard`: KCS 14 31 05

## Node — StructuralComponent / `StructuralComponent:kcs14_31_hsfg-bolt`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 31 sec3-3
- properties:
  - `name_ko`: 고장력볼트
  - `ks_codes`: ["KS B 1010", "KS B 2819"]
  - `source_standard`: KCS 14 31 05 3.3

## Node — StructuralComponent / `StructuralComponent:kcs14_31_weld-joint`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 31 sec6
- properties:
  - `name_ko`: 용접부(그루브용접·필릿용접)
  - `source_standard`: KCS 14 31 20

## Node — Specification / `Specification:kcs14_31_05`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec1
- properties:
  - `name_ko`: KCS 14 31 05 강구조공사 일반사항
  - `code`: KCS 14 31 05
  - `notice`: 국토교통부고시 제2024-224호

## Node — Specification / `Specification:kcs14_31_20`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec6
- properties:
  - `name_ko`: KCS 14 31 20 강구조공사 용접
  - `code`: KCS 14 31 20

## Node — Specification / `Specification:kcs14_31_sec3-1_material`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec3-1
- properties:
  - `name_ko`: 자재 일반 검수 기준
  - `requirement`: KS 인증 공장 제조 자재만 사용, 강재는 규격증명서(밀시트) 원본 또는 증명인 부착 사본 제출, 용접재료·고장력볼트는 밀시트 및 시험성적서 첨부 필수
  - `source_standard`: KCS 14 31 05 3.1

## Node — Specification / `Specification:kcs14_31_sec3-2_steel`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec3-2
- properties:
  - `name_ko`: 강재 품질 기준
  - `requirement`: KS D 3503(일반구조용 압연강재), KS D 3515(용접구조용 압연강재), 강재 표면 KS 표시 확인
  - `ks_codes`: ["KS D 3503", "KS D 3515"]
  - `source_standard`: KCS 14 31 05 3.2

## Node — Specification / `Specification:kcs14_31_sec3-3_hsfg`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec3-3
- properties:
  - `name_ko`: 고장력볼트 검수 기준
  - `requirement`: KS B 1010(마찰접합용), KS B 2819(토크-전단형), 인장강도·항복강도 시험성적서 제출
  - `ks_codes`: ["KS B 1010", "KS B 2819"]
  - `source_standard`: KCS 14 31 05 3.3

## Node — Specification / `Specification:kcs14_31_sec5-1_tolerance`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec5-1
- properties:
  - `name_ko`: 허용차 구분 기준
  - `requirement`: 관리허용차(목표치, 95% 만족 원칙)와 한계허용차(합격/불합격 판정값) 구분
  - `mgmt_tolerance_pct`: 95
  - `source_standard`: KCS 14 31 05 5.1

## Node — Specification / `Specification:kcs14_31_sec5-2_root-gap`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec5-2
- properties:
  - `name_ko`: 루트간격 허용차
  - `requirement`: 수동용접 0~2.5mm, 자동용접 0~1mm
  - `manual_max_mm`: 2.5
  - `auto_max_mm`: 1.0
  - `source_standard`: KCS 14 31 05 5.2

## Node — Specification / `Specification:kcs14_31_sec5-2_fillet`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec5-2
- properties:
  - `name_ko`: 필릿용접 사이즈 허용차
  - `requirement`: 관리허용차 0~+0.5S, 최대 5mm
  - `tolerance`: 0~+0.5S
  - `max_mm`: 5
  - `source_standard`: KCS 14 31 05 5.2

## Node — Specification / `Specification:kcs14_31_sec5-2_hole`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec5-2
- properties:
  - `name_ko`: 고장력볼트 구멍중심 허용차
  - `requirement`: ±1mm 이내
  - `tolerance_mm`: 1
  - `source_standard`: KCS 14 31 05 5.2

## Node — Specification / `Specification:kcs14_31_sec6-3_ut`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec6-3
- properties:
  - `name_ko`: 초음파탐상검사(UT) 기준
  - `requirement`: 그루브용접부 내부결함 검사, KS B 0896 적용(페라이트계 강 용접부), 표본 검사로트마다 30개, 로트 구성 용접 300개소 이하
  - `ks_code`: KS B 0896
  - `sample_per_lot`: 30
  - `lot_max`: 300
  - `source_standard`: KCS 14 31 20 3.15.2

## Node — Specification / `Specification:kcs14_31_sec6-4_judgement`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec6-4
- properties:
  - `name_ko`: 용접 비파괴검사 합격판정
  - `requirement`: 불합격 0~1개소 합격; 2~3개소 추가 30개 재검사; 재검사 60개 중 4개소 이하 합격, 5개소 이상 불합격
  - `pass_initial`: 0-1 fail
  - `retest_threshold`: 2-3 fail
  - `retest_pass`: ≤4 in 60
  - `retest_fail`: ≥5
  - `source_standard`: KCS 14 31 20 3.15.2

## Node — Specification / `Specification:kcs14_31_sec6-5_delay`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec6-5
- properties:
  - `name_ko`: 초음파탐상 지연시간
  - `requirement`: 용접목두께·입열량·항복강도에 따라 8시간~48시간 경과 후 실시
  - `min_hours`: 8
  - `max_hours`: 48
  - `source_standard`: KCS 14 31 20 3.15.2

## Node — Specification / `Specification:kcs14_31_sec6-6_strength`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec6-6
- properties:
  - `name_ko`: 용접재 강도·인성 기준
  - `requirement`: 강도: 모재 규격과 동등 이상; 인성: 모재 규격과 같거나 이상
  - `source_standard`: KCS 14 31 20

## Node — MaterialReceiptReport / `MaterialReceiptReport:kcs14_31_mill-sheet`
- space: `resource`
- node_type: `MaterialReceiptReport`
- source_article: KCS 14 31 sec3-1
- properties:
  - `name_ko`: 강재 밀시트(규격증명서)
  - `source_standard`: KCS 14 31 05 3.1

## Node — TestReport / `TestReport:kcs14_31_hsfg`
- space: `resource`
- node_type: `TestReport`
- source_article: KCS 14 31 sec3-3
- properties:
  - `name_ko`: 고장력볼트 인장강도·항복강도 시험성적서
  - `source_standard`: KCS 14 31 05 3.3

## Node — TestReport / `TestReport:kcs14_31_ut`
- space: `resource`
- node_type: `TestReport`
- source_article: KCS 14 31 sec6-3
- properties:
  - `name_ko`: 초음파탐상시험(UT) 성적서
  - `test_method`: KS B 0896
  - `source_standard`: KCS 14 31 20 3.15.2

## Node — Checklist / `Checklist:kcs14_31_precision`
- space: `resource`
- node_type: `Checklist`
- source_article: KCS 14 31 sec5-2
- properties:
  - `name_ko`: 강구조 정밀도 검측 체크리스트
  - `items`: ["루트간격", "필릿용접 사이즈", "고장력볼트 구멍중심", "부재길이·폭·변형·비틀림"]
  - `source_standard`: KCS 14 31 05 5.2

## Node — Specification / `Specification:kcs14_31_const-plan`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 31 sec4
- properties:
  - `name_ko`: 강구조 시공계획서
  - `includes`: ["공장제작계획서", "현장설치공사계획서", "공정표·공정관리계획", "안전관리계획"]
  - `source_standard`: KCS 14 31 05 4

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:kcs14_31_sec3_01`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: KCS 14 31 sec3
- properties:
  - `name_ko`: 강재·볼트·용접재료 자재 검수
  - `description`: 밀시트·시험성적서 검토 및 KS 인증 확인, 완비 시 추가 재료시험 생략 가능
  - `source_standard`: KCS 14 31 05 3

## Node — StageApprovalDecision / `StageApprovalDecision:kcs14_31_sec4_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 14 31 sec4
- properties:
  - `name_ko`: 강구조 시공계획서 승인
  - `description`: 시공자가 착수 전 시공계획서를 작성·제출, 감리자 승인
  - `source_standard`: KCS 14 31 05 4

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:kcs14_31_sec5_precision`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 31 sec5
- properties:
  - `name_ko`: 강구조 정밀도 검측
  - `description`: 한계허용차 기준 합부 판정, 초과 시 보수·재제작 협의
  - `source_standard`: KCS 14 31 05 5

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:kcs14_31_sec6_welding`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 31 sec6
- properties:
  - `name_ko`: 용접 검측 및 비파괴검사 판정
  - `description`: 용접부 외관검사 및 UT 비파괴검사, 합격판정 기준 적용
  - `ks_code`: KS B 0896
  - `source_standard`: KCS 14 31 20 3.15

## Node — DecisionOutcome / `DecisionOutcome:kcs14_31_material-approved`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 31 sec3
- properties:
  - `name_ko`: 자재 검수 승인
  - `result`: approved

## Node — DecisionOutcome / `DecisionOutcome:kcs14_31_weld-pass`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 31 sec6-4
- properties:
  - `name_ko`: 용접 비파괴검사 합격
  - `result`: pass
  - `criterion`: 30개 표본 중 불합격 0~1개소 또는 재검사 60개 중 4개소 이하

## Node — DecisionOutcome / `DecisionOutcome:kcs14_31_weld-fail`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 31 sec6-4
- properties:
  - `name_ko`: 용접 비파괴검사 불합격
  - `result`: fail
  - `criterion`: 재검사 60개 중 5개소 이상
  - `next_action`: 보수 후 재검사

## Node — DecisionOutcome / `DecisionOutcome:kcs14_31_precision-pass`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 31 sec5
- properties:
  - `name_ko`: 정밀도 합격
  - `result`: pass
  - `criterion`: 한계허용차 이내

## Node — DecisionOutcome / `DecisionOutcome:kcs14_31_precision-fail`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 31 sec5
- properties:
  - `name_ko`: 정밀도 불합격
  - `result`: fail
  - `next_action`: 보수·재제작 협의

## Edges

## Edge — `qualified_as`
- from: `SiteEngineer:kcs14_31_sec7_01` (subject)
- to: `Qualification:kcs14_31_welder` (concept)
- source_article: KCS 14 31 sec6-1

## Edge — `qualified_as`
- from: `SiteEngineer:kcs14_31_sec6-1_welder` (subject)
- to: `Qualification:kcs14_31_welder` (concept)
- source_article: KCS 14 31 sec6-1

## Edge — `qualified_as`
- from: `SiteEngineer:kcs14_31_sec6-2_ndt` (subject)
- to: `Qualification:kcs14_31_ndt-inspector` (concept)
- source_article: KCS 14 31 sec6-2

## Edge — `qualified_as`
- from: `Supervisor:kcs14_31_sec7_01` (subject)
- to: `Qualification:kcs14_31_supervisor` (concept)
- source_article: KCS 14 31 sec7

## Edge — `qualified_as`
- from: `ChiefSupervisor:kcs14_31_sec7_01` (subject)
- to: `Qualification:kcs14_31_chief-supervisor` (concept)
- source_article: KCS 14 31 sec7

## Edge — `subclass_of`
- from: `Qualification:kcs14_31_chief-supervisor` (concept)
- to: `Qualification:kcs14_31_supervisor` (concept)
- source_article: KCS 14 31 sec7

## Edge — `part_of`
- from: `WorkType:kcs14_31_welding` (concept)
- to: `WorkType:kcs14_31_steel-work` (concept)
- source_article: KCS 14 31 sec6

## Edge — `part_of`
- from: `StructuralComponent:kcs14_31_hsfg-bolt` (concept)
- to: `StructuralComponent:kcs14_31_steel-member` (concept)
- source_article: KCS 14 31 sec3-3

## Edge — `part_of`
- from: `StructuralComponent:kcs14_31_weld-joint` (concept)
- to: `StructuralComponent:kcs14_31_steel-member` (concept)
- source_article: KCS 14 31 sec6

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_31_chief-supervisor` (concept)
- to: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- source_article: KCS 14 31 sec3

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_31_chief-supervisor` (concept)
- to: `StageApprovalDecision:kcs14_31_sec4_01` (decision)
- source_article: KCS 14 31 sec4

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_31_supervisor` (concept)
- to: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- source_article: KCS 14 31 sec5

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_31_supervisor` (concept)
- to: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- source_article: KCS 14 31 sec6

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_31_ndt-inspector` (concept)
- to: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- source_article: KCS 14 31 sec6-2

## Edge — `performs`
- from: `ChiefSupervisor:kcs14_31_sec7_01` (subject)
- to: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- source_article: KCS 14 31 sec3

## Edge — `performs`
- from: `ChiefSupervisor:kcs14_31_sec7_01` (subject)
- to: `StageApprovalDecision:kcs14_31_sec4_01` (decision)
- source_article: KCS 14 31 sec4

## Edge — `performs`
- from: `Supervisor:kcs14_31_sec7_01` (subject)
- to: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- source_article: KCS 14 31 sec5

## Edge — `performs`
- from: `Supervisor:kcs14_31_sec7_01` (subject)
- to: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- source_article: KCS 14 31 sec6

## Edge — `performs`
- from: `SiteEngineer:kcs14_31_sec6-2_ndt` (subject)
- to: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- source_article: KCS 14 31 sec6-2

## Edge — `targets_work_type`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `WorkType:kcs14_31_steel-work` (concept)
- source_article: KCS 14 31 sec3

## Edge — `targets_component`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `StructuralComponent:kcs14_31_steel-member` (concept)
- source_article: KCS 14 31 sec3-2

## Edge — `targets_component`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `StructuralComponent:kcs14_31_hsfg-bolt` (concept)
- source_article: KCS 14 31 sec3-3

## Edge — `targets_work_type`
- from: `StageApprovalDecision:kcs14_31_sec4_01` (decision)
- to: `WorkType:kcs14_31_steel-work` (concept)
- source_article: KCS 14 31 sec4

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- to: `StructuralComponent:kcs14_31_steel-member` (concept)
- source_article: KCS 14 31 sec5

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `StructuralComponent:kcs14_31_weld-joint` (concept)
- source_article: KCS 14 31 sec6

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `WorkType:kcs14_31_welding` (concept)
- source_article: KCS 14 31 sec6

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `Specification:kcs14_31_sec3-1_material` (resource)
- source_article: KCS 14 31 sec3-1

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `Specification:kcs14_31_sec3-2_steel` (resource)
- source_article: KCS 14 31 sec3-2

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `Specification:kcs14_31_sec3-3_hsfg` (resource)
- source_article: KCS 14 31 sec3-3

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `MaterialReceiptReport:kcs14_31_mill-sheet` (resource)
- source_article: KCS 14 31 sec3-1

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `TestReport:kcs14_31_hsfg` (resource)
- source_article: KCS 14 31 sec3-3

## Edge — `based_on`
- from: `StageApprovalDecision:kcs14_31_sec4_01` (decision)
- to: `Specification:kcs14_31_const-plan` (resource)
- source_article: KCS 14 31 sec4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- to: `Specification:kcs14_31_sec5-1_tolerance` (resource)
- source_article: KCS 14 31 sec5-1

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- to: `Specification:kcs14_31_sec5-2_root-gap` (resource)
- source_article: KCS 14 31 sec5-2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- to: `Specification:kcs14_31_sec5-2_fillet` (resource)
- source_article: KCS 14 31 sec5-2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- to: `Specification:kcs14_31_sec5-2_hole` (resource)
- source_article: KCS 14 31 sec5-2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- to: `Checklist:kcs14_31_precision` (resource)
- source_article: KCS 14 31 sec5-2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `Specification:kcs14_31_sec6-3_ut` (resource)
- source_article: KCS 14 31 sec6-3

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `Specification:kcs14_31_sec6-4_judgement` (resource)
- source_article: KCS 14 31 sec6-4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `Specification:kcs14_31_sec6-5_delay` (resource)
- source_article: KCS 14 31 sec6-5

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `Specification:kcs14_31_sec6-6_strength` (resource)
- source_article: KCS 14 31 sec6-6

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `TestReport:kcs14_31_ut` (resource)
- source_article: KCS 14 31 sec6-3

## Edge — `precedes`
- from: `StageApprovalDecision:kcs14_31_sec4_01` (decision)
- to: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- source_article: KCS 14 31 sec4

## Edge — `precedes`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- source_article: KCS 14 31 sec5

## Edge — `precedes`
- from: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- to: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- source_article: KCS 14 31 sec6

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- source_article: KCS 14 31 sec6

## Edge — `yields`
- from: `MaterialReceiptDecision:kcs14_31_sec3_01` (decision)
- to: `DecisionOutcome:kcs14_31_material-approved` (outcome)
- source_article: KCS 14 31 sec3

## Edge — `yields`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `DecisionOutcome:kcs14_31_weld-pass` (outcome)
- source_article: KCS 14 31 sec6-4

## Edge — `yields`
- from: `ConstructionInspectionDecision:kcs14_31_sec6_welding` (decision)
- to: `DecisionOutcome:kcs14_31_weld-fail` (outcome)
- source_article: KCS 14 31 sec6-4

## Edge — `yields`
- from: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- to: `DecisionOutcome:kcs14_31_precision-pass` (outcome)
- source_article: KCS 14 31 sec5

## Edge — `yields`
- from: `ConstructionInspectionDecision:kcs14_31_sec5_precision` (decision)
- to: `DecisionOutcome:kcs14_31_precision-fail` (outcome)
- source_article: KCS 14 31 sec5
