# Extracted graph — KCS_14_20.jsonl

_source jsonl: KCS_14_20.jsonl_

## Nodes

## Node — Org / `Org:kcsc-kcs1420`
- space: `subject`
- node_type: `Org`
- source_article: KCS 14 20 sec1
- properties:
  - `name_ko`: 국가건설기준센터
  - `role`: KCS 14 20 표준 관리

## Node — Org / `Org:ordering-agency-kcs1420`
- space: `subject`
- node_type: `Org`
- source_article: KCS 14 20 sec6
- properties:
  - `name_ko`: 발주자
  - `scope`: 콘크리트 자재 승인 최종 권한

## Node — SiteEngineer / `SiteEngineer:kcs14_20_sec6_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS 14 20 sec6
- properties:
  - `name_ko`: 시공자
  - `duties`: ["자재 시험성적서 제출", "배합계획서 작성", "시공계획서 제출", "검측 요청"]
  - `source_standard`: KCS 14 20 10

## Node — Supervisor / `Supervisor:kcs14_20_sec6_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: KCS 14 20 sec5
- properties:
  - `name_ko`: 감리자
  - `duties`: ["자재 검수", "거푸집·동바리 검측", "철근배근 검측", "콘크리트 타설 승인", "양생 후 검측"]
  - `source_standard`: KCS 14 20 10

## Node — ChiefSupervisor / `ChiefSupervisor:kcs14_20_sec6_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: KCS 14 20 sec6
- properties:
  - `name_ko`: 책임감리원
  - `scope`: 콘크리트 자재 검수, 압축강도 판정 승인 총괄
  - `source_standard`: KCS 14 20 10

## Node — Qualification / `Qualification:kcs14_20_supervisor`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 14 20 sec6
- properties:
  - `name_ko`: 콘크리트공사 감리자 자격
  - `scope`: 자재 검수·시공 검측·압축강도 판정 승인 권한
  - `source_standard`: KCS 14 20

## Node — Qualification / `Qualification:kcs14_20_chief-supervisor`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 14 20 sec6
- properties:
  - `name_ko`: 콘크리트공사 책임감리원 자격
  - `scope`: 자재 검수·시공 검측·압축강도 판정 승인 총괄
  - `source_standard`: KCS 14 20

## Node — Qualification / `Qualification:kcs14_20_site-engineer`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 14 20 sec6
- properties:
  - `name_ko`: 콘크리트공사 시공자(현장대리인) 자격
  - `scope`: 자재 시험·배합·타설 시공 책임
  - `source_standard`: KCS 14 20

## Node — WorkType / `WorkType:kcs14_20_concrete-work`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20 sec2
- properties:
  - `name_ko`: 콘크리트공사
  - `scope`: 콘크리트구조물 시공
  - `source_standard`: KCS 14 20

## Node — WorkType / `WorkType:kcs14_20_formwork`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20 sec5-1
- properties:
  - `name_ko`: 거푸집·동바리 공사
  - `source_standard`: KCS 14 20 10 5.1

## Node — WorkType / `WorkType:kcs14_20_rebar`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20 sec5-2
- properties:
  - `name_ko`: 철근 배근 공사
  - `source_standard`: KCS 14 20 10 5.2

## Node — WorkType / `WorkType:kcs14_20_placement`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20 sec5-3
- properties:
  - `name_ko`: 콘크리트 타설
  - `source_standard`: KCS 14 20 10 5.3

## Node — WorkType / `WorkType:kcs14_20_curing`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 14 20 sec5-4
- properties:
  - `name_ko`: 양생
  - `source_standard`: KCS 14 20 10 5.4

## Node — StructuralComponent / `StructuralComponent:kcs14_20_concrete-member`
- space: `concept`
- node_type: `StructuralComponent`
- source_article: KCS 14 20 sec2
- properties:
  - `name_ko`: 콘크리트 부재
  - `source_standard`: KCS 14 20

## Node — Specification / `Specification:kcs14_20_01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec1
- properties:
  - `name_ko`: KCS 14 20 01 콘크리트공사 일반사항
  - `code`: KCS 14 20 01
  - `legal_basis`: 건설기술 진흥법 제44조
  - `notice`: 국토교통부고시 제2024-879호 (2024-12-30)

## Node — Specification / `Specification:kcs14_20_10`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec3
- properties:
  - `name_ko`: KCS 14 20 10 일반콘크리트
  - `code`: KCS 14 20 10
  - `scope`: 자재 검수 + 시공 검측

## Node — Specification / `Specification:kcs14_20_sec3-1_cement`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec3-1
- properties:
  - `name_ko`: 시멘트 검수 기준
  - `requirement`: KS L 5201(포틀랜드시멘트), KS L 5210(고로슬래그시멘트) KS 인증 제품, 인수 시 제조사 시험성적서 제출 필수
  - `source_standard`: KCS 14 20 10 3.1

## Node — Specification / `Specification:kcs14_20_sec3-2_aggregate`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec3-2
- properties:
  - `name_ko`: 골재 검수 기준
  - `requirement`: 조립률·흡수율·입도·안정성·알칼리골재반응성 시험; 굵은골재 최대치수: 슬래브/보 25mm 이하, 일반 25~40mm
  - `max_aggregate_slab_mm`: 25
  - `max_aggregate_general_mm`: 40
  - `source_standard`: KCS 14 20 10 3.2

## Node — Specification / `Specification:kcs14_20_sec3-4_remicon`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec3-4
- properties:
  - `name_ko`: 레디믹스트 콘크리트 검수 기준
  - `requirement`: KS F 4009 적용, 호칭강도·슬럼프·굵은골재 최대치수 조합으로 발주, 검사로트 450㎥/로트, 시험빈도 150㎥당 1회
  - `ks_code`: KS F 4009
  - `lot_size_m3`: 450
  - `test_frequency_m3`: 150
  - `source_standard`: KCS 14 20 10 3.4

## Node — Specification / `Specification:kcs14_20_sec4-1_fresh`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec4-1
- properties:
  - `name_ko`: 굳지 않은 콘크리트 검사 시기
  - `requirement`: 배합 변경 시마다; 일일 타설량 150㎥ 미만은 일일 타설량마다 1회; 150㎥ 이상은 150㎥마다 1회
  - `threshold_m3`: 150
  - `source_standard`: KCS 14 20 10 4.1

## Node — Specification / `Specification:kcs14_20_sec4-2_strength-test`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec4-2
- properties:
  - `name_ko`: 압축강도 검사 시험빈도
  - `requirement`: 레디믹스트 콘크리트 150㎥당 1회(KS F 4009); 일반콘크리트 120㎥당 1회 또는 배합 변경 시
  - `remicon_freq_m3`: 150
  - `general_freq_m3`: 120
  - `source_standard`: KCS 14 20 10 4.2

## Node — Specification / `Specification:kcs14_20_concrete-strength-01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec4-3
- properties:
  - `name_ko`: 공시체 압축강도 기준
  - `requirement`: 공시체 28일 강도 ≥ 호칭강도(설계기준압축강도 fck)
  - `age_days`: 28
  - `test_method`: KS F 2405
  - `source_standard`: KCS 14 20 10 4.3

## Node — Specification / `Specification:kcs14_20_slump-01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec4-3
- properties:
  - `name_ko`: 슬럼프 허용오차
  - `requirement`: 슬럼프 80mm 이상 180mm 이하 → 허용오차 ±25mm (표 1.7-2)
  - `tolerance_mm`: 25
  - `slump_range_mm`: 80-180
  - `test_method`: KS F 2402
  - `source_standard`: KCS 14 20 10 4.3

## Node — Specification / `Specification:kcs14_20_air-content-01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec4-3
- properties:
  - `name_ko`: 공기량 기준
  - `requirement`: 보통콘크리트 4.5% ±1.5%, 경량콘크리트 5.0% ±1.5%, AE콘크리트 4~7%
  - `normal_pct`: 4.5±1.5
  - `lightweight_pct`: 5.0±1.5
  - `ae_pct`: 4-7
  - `test_method`: KS F 2421
  - `source_standard`: KCS 14 20 10 4.3

## Node — Specification / `Specification:kcs14_20_chloride-01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec4-3
- properties:
  - `name_ko`: 염화물 함유량 기준
  - `requirement`: 철근콘크리트 0.30 kg/㎥ 이하
  - `limit_kg_per_m3`: 0.3
  - `test_method`: KS F 2515
  - `source_standard`: KCS 14 20 10 4.3

## Node — Specification / `Specification:kcs14_20_unit-water-01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec4-3
- properties:
  - `name_ko`: 단위수량 기준
  - `requirement`: 185 kg/㎥ 이하
  - `limit_kg_per_m3`: 185
  - `source_standard`: KCS 14 20 10 4.3

## Node — Specification / `Specification:kcs14_20_judgement-01`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 14 20 sec4-4
- properties:
  - `name_ko`: 압축강도 판정기준
  - `requirement`: 1회 시험값(3개 공시체 평균)이 호칭강도의 85% 이상이고, 3회 연속 시험값 평균이 호칭강도 이상
  - `single_test_min_pct`: 85
  - `three_test_avg`: ≥ fck
  - `source_standard`: KCS 14 20 10 4.4

## Node — MaterialReceiptReport / `MaterialReceiptReport:kcs14_20_mill-sheet`
- space: `resource`
- node_type: `MaterialReceiptReport`
- source_article: KCS 14 20 sec3
- properties:
  - `name_ko`: 시멘트·골재 시험성적서
  - `source_standard`: KCS 14 20 10 3.1-3.3

## Node — TestReport / `TestReport:kcs14_20_strength`
- space: `resource`
- node_type: `TestReport`
- source_article: KCS 14 20 sec4-2
- properties:
  - `name_ko`: 콘크리트 압축강도 시험성적서
  - `test_method`: KS F 2405
  - `source_standard`: KCS 14 20 10 4.2

## Node — Checklist / `Checklist:kcs14_20_formwork-inspection`
- space: `resource`
- node_type: `Checklist`
- source_article: KCS 14 20 sec5-1
- properties:
  - `name_ko`: 거푸집·동바리 검측 체크리스트
  - `source_standard`: KCS 14 20 10 5.1

## Node — Checklist / `Checklist:kcs14_20_rebar-inspection`
- space: `resource`
- node_type: `Checklist`
- source_article: KCS 14 20 sec5-2
- properties:
  - `name_ko`: 철근배근 검측 체크리스트
  - `source_standard`: KCS 14 20 10 5.2

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:kcs14_20_sec3_01`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: KCS 14 20 sec3
- properties:
  - `name_ko`: 콘크리트 자재 검수
  - `description`: 시멘트·골재·혼화재·레디믹스트 콘크리트 KS 인증 및 시험성적서 검수
  - `ks_codes`: ["KS L 5201", "KS L 5210", "KS F 4009"]
  - `source_standard`: KCS 14 20 10 3

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:kcs14_20_sec5-1_formwork`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 20 sec5-1
- properties:
  - `name_ko`: 거푸집·동바리 검측
  - `description`: 콘크리트 타설 전 거푸집·동바리 검측·승인
  - `timing`: 콘크리트 타설 전
  - `source_standard`: KCS 14 20 10 5.1

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:kcs14_20_sec5-2_rebar`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 20 sec5-2
- properties:
  - `name_ko`: 철근 배근 검측
  - `description`: 콘크리트 타설 전 철근 배근 검측·승인
  - `timing`: 콘크리트 타설 전
  - `source_standard`: KCS 14 20 10 5.2

## Node — StageApprovalDecision / `StageApprovalDecision:kcs14_20_sec5-3_placement`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 14 20 sec5-3
- properties:
  - `name_ko`: 콘크리트 타설 승인
  - `description`: 시공자가 시공계획서·배합계획서 제출 후 감리자 승인
  - `source_standard`: KCS 14 20 10 5.3

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:kcs14_20_sec5-4_curing`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 20 sec5-4
- properties:
  - `name_ko`: 양생 후 검측
  - `description`: 양생 종료 후 감리자 입회 하 검측
  - `source_standard`: KCS 14 20 10 5.4

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:kcs14_20_sec5-5_strength`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 14 20 sec5-5
- properties:
  - `name_ko`: 압축강도 판정 검수
  - `description`: 공시체 28일 압축강도 시험 결과로 호칭강도 적합 여부 판정
  - `judgement_rule`: 1회시험 3공시체 평균 ≥ 호칭강도×0.85 AND 3회연속 평균 ≥ 호칭강도
  - `source_standard`: KCS 14 20 10 4.4 / 5.5

## Node — DecisionOutcome / `DecisionOutcome:kcs14_20_strength-pass`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 20 sec4-4
- properties:
  - `name_ko`: 압축강도 합격
  - `result`: pass
  - `criterion`: 3공시체 평균 ≥ fck×0.85 AND 3회 연속 평균 ≥ fck

## Node — DecisionOutcome / `DecisionOutcome:kcs14_20_strength-fail`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 20 sec4-4
- properties:
  - `name_ko`: 압축강도 불합격
  - `result`: fail
  - `next_action`: 원인 분석·구조검토·보강 또는 재시공

## Node — DecisionOutcome / `DecisionOutcome:kcs14_20_material-approved`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 14 20 sec3
- properties:
  - `name_ko`: 자재 검수 승인
  - `result`: approved

## Edges

## Edge — `qualified_as`
- from: `SiteEngineer:kcs14_20_sec6_01` (subject)
- to: `Qualification:kcs14_20_site-engineer` (concept)
- source_article: KCS 14 20 sec6

## Edge — `qualified_as`
- from: `Supervisor:kcs14_20_sec6_01` (subject)
- to: `Qualification:kcs14_20_supervisor` (concept)
- source_article: KCS 14 20 sec6

## Edge — `qualified_as`
- from: `ChiefSupervisor:kcs14_20_sec6_01` (subject)
- to: `Qualification:kcs14_20_chief-supervisor` (concept)
- source_article: KCS 14 20 sec6

## Edge — `subclass_of`
- from: `Qualification:kcs14_20_chief-supervisor` (concept)
- to: `Qualification:kcs14_20_supervisor` (concept)
- source_article: KCS 14 20 sec6

## Edge — `part_of`
- from: `WorkType:kcs14_20_formwork` (concept)
- to: `WorkType:kcs14_20_concrete-work` (concept)
- source_article: KCS 14 20 sec5

## Edge — `part_of`
- from: `WorkType:kcs14_20_rebar` (concept)
- to: `WorkType:kcs14_20_concrete-work` (concept)
- source_article: KCS 14 20 sec5

## Edge — `part_of`
- from: `WorkType:kcs14_20_placement` (concept)
- to: `WorkType:kcs14_20_concrete-work` (concept)
- source_article: KCS 14 20 sec5

## Edge — `part_of`
- from: `WorkType:kcs14_20_curing` (concept)
- to: `WorkType:kcs14_20_concrete-work` (concept)
- source_article: KCS 14 20 sec5

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_20_supervisor` (concept)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-1_formwork` (decision)
- source_article: KCS 14 20 sec5-1

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_20_supervisor` (concept)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-2_rebar` (decision)
- source_article: KCS 14 20 sec5-2

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_20_supervisor` (concept)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-4_curing` (decision)
- source_article: KCS 14 20 sec5-4

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_20_chief-supervisor` (concept)
- to: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- source_article: KCS 14 20 sec3

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_20_chief-supervisor` (concept)
- to: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- source_article: KCS 14 20 sec5-3

## Edge — `grants_authority_for`
- from: `Qualification:kcs14_20_chief-supervisor` (concept)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- source_article: KCS 14 20 sec5-5

## Edge — `performs`
- from: `Supervisor:kcs14_20_sec6_01` (subject)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-1_formwork` (decision)
- source_article: KCS 14 20 sec5-1

## Edge — `performs`
- from: `Supervisor:kcs14_20_sec6_01` (subject)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-2_rebar` (decision)
- source_article: KCS 14 20 sec5-2

## Edge — `performs`
- from: `Supervisor:kcs14_20_sec6_01` (subject)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-4_curing` (decision)
- source_article: KCS 14 20 sec5-4

## Edge — `performs`
- from: `ChiefSupervisor:kcs14_20_sec6_01` (subject)
- to: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- source_article: KCS 14 20 sec3

## Edge — `performs`
- from: `ChiefSupervisor:kcs14_20_sec6_01` (subject)
- to: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- source_article: KCS 14 20 sec5-3

## Edge — `performs`
- from: `ChiefSupervisor:kcs14_20_sec6_01` (subject)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- source_article: KCS 14 20 sec5-5

## Edge — `targets_work_type`
- from: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- to: `WorkType:kcs14_20_concrete-work` (concept)
- source_article: KCS 14 20 sec3

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-1_formwork` (decision)
- to: `WorkType:kcs14_20_formwork` (concept)
- source_article: KCS 14 20 sec5-1

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-2_rebar` (decision)
- to: `WorkType:kcs14_20_rebar` (concept)
- source_article: KCS 14 20 sec5-2

## Edge — `targets_work_type`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `WorkType:kcs14_20_placement` (concept)
- source_article: KCS 14 20 sec5-3

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-4_curing` (decision)
- to: `WorkType:kcs14_20_curing` (concept)
- source_article: KCS 14 20 sec5-4

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- to: `StructuralComponent:kcs14_20_concrete-member` (concept)
- source_article: KCS 14 20 sec5-5

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- to: `Specification:kcs14_20_sec3-1_cement` (resource)
- source_article: KCS 14 20 sec3-1

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- to: `Specification:kcs14_20_sec3-2_aggregate` (resource)
- source_article: KCS 14 20 sec3-2

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- to: `Specification:kcs14_20_sec3-4_remicon` (resource)
- source_article: KCS 14 20 sec3-4

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- to: `MaterialReceiptReport:kcs14_20_mill-sheet` (resource)
- source_article: KCS 14 20 sec3

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-1_formwork` (decision)
- to: `Checklist:kcs14_20_formwork-inspection` (resource)
- source_article: KCS 14 20 sec5-1

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-2_rebar` (decision)
- to: `Checklist:kcs14_20_rebar-inspection` (resource)
- source_article: KCS 14 20 sec5-2

## Edge — `based_on`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `Specification:kcs14_20_sec4-1_fresh` (resource)
- source_article: KCS 14 20 sec4-1

## Edge — `based_on`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `Specification:kcs14_20_slump-01` (resource)
- source_article: KCS 14 20 sec4-3

## Edge — `based_on`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `Specification:kcs14_20_air-content-01` (resource)
- source_article: KCS 14 20 sec4-3

## Edge — `based_on`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `Specification:kcs14_20_chloride-01` (resource)
- source_article: KCS 14 20 sec4-3

## Edge — `based_on`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `Specification:kcs14_20_unit-water-01` (resource)
- source_article: KCS 14 20 sec4-3

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- to: `Specification:kcs14_20_sec4-2_strength-test` (resource)
- source_article: KCS 14 20 sec4-2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- to: `Specification:kcs14_20_concrete-strength-01` (resource)
- source_article: KCS 14 20 sec4-3

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- to: `Specification:kcs14_20_judgement-01` (resource)
- source_article: KCS 14 20 sec4-4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- to: `TestReport:kcs14_20_strength` (resource)
- source_article: KCS 14 20 sec4-2

## Edge — `precedes`
- from: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- to: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- source_article: KCS 14 20 sec5-3

## Edge — `precedes`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-1_formwork` (decision)
- to: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- source_article: KCS 14 20 sec5-3

## Edge — `precedes`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-2_rebar` (decision)
- to: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- source_article: KCS 14 20 sec5-3

## Edge — `precedes`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-4_curing` (decision)
- source_article: KCS 14 20 sec5-4

## Edge — `precedes`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-4_curing` (decision)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- source_article: KCS 14 20 sec5-5

## Edge — `depends_on`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-1_formwork` (decision)
- source_article: KCS 14 20 sec5-3

## Edge — `depends_on`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `ConstructionInspectionDecision:kcs14_20_sec5-2_rebar` (decision)
- source_article: KCS 14 20 sec5-3

## Edge — `depends_on`
- from: `StageApprovalDecision:kcs14_20_sec5-3_placement` (decision)
- to: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- source_article: KCS 14 20 sec5-3

## Edge — `yields`
- from: `MaterialReceiptDecision:kcs14_20_sec3_01` (decision)
- to: `DecisionOutcome:kcs14_20_material-approved` (outcome)
- source_article: KCS 14 20 sec3

## Edge — `yields`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- to: `DecisionOutcome:kcs14_20_strength-pass` (outcome)
- source_article: KCS 14 20 sec4-4

## Edge — `yields`
- from: `ConstructionInspectionDecision:kcs14_20_sec5-5_strength` (decision)
- to: `DecisionOutcome:kcs14_20_strength-fail` (outcome)
- source_article: KCS 14 20 sec4-4
