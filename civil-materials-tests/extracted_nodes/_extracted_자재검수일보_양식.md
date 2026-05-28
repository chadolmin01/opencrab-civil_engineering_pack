# Extracted graph — 자재검수일보_양식.jsonl

_source jsonl: 자재검수일보_양식.jsonl_

## Nodes

## Node — MaterialReceiptReport / `MaterialReceiptReport:form_material_receipt_01`
- space: `resource`
- node_type: `MaterialReceiptReport`
- source_article: 자재검수일보 표준양식
- properties:
  - `issuer`: 국토교통부 / LH / 대한건설협회
  - `source`: 국토교통부 건설사업관리 표준, LH 품질관리지침
  - `legal_basis`: 건설기술 진흥법, KCS 국가건설기준
  - `language`: ko
  - `material_types`: ["ready_mixed_concrete", "reinforcing_bar", "cement_admixture", "aggregate", "pile_phc_steel"]
  - `name`: 자재검수일보 표준양식

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:form_material_receipt_01`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: 자재검수일보 [3-4] 검수 항목 및 자재별 시험
- properties:
  - `decision_stage`: primary_supervisor_confirm
  - `decision_type`: material_receipt
  - `material_type`: common_all
  - `material_types_covered`: ["ready_mixed_concrete", "reinforcing_bar", "cement_admixture", "aggregate", "pile_phc_steel"]
  - `inspection_items`: ["외관", "수량", "규격", "표시", "시험성적서", "운반보관"]
  - `verifies`: ["KS 표준", "KCS 기준", "Mill Sheet", "공급원 승인"]
  - `material_specific_tests`: {"ready_mixed_concrete": ["호칭강도", "슬럼프", "공기량", "염화물량", "운반시간"], "reinforcing_bar": ["등급(SD400/500/600)", "직경(D10-D32)", "Mill Sheet 항복/인장/연신율"], "cement_admixture": ["종류", "분말도", "시험성적서"], "aggregate": ["입도시험", "흡수율", "단위용적질량", "0.08mm 통과율"], "pile_phc_steel": ["외경/두께/길이", "강도", "시험성적서"]}
  - `name`: 자재 반입 검수 결정 (담당감리 1차)

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:form_material_receipt_02`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: 자재검수일보 [6. 서명란] 책임감리원 최종 승인
- properties:
  - `decision_stage`: chief_supervisor_final_approval
  - `decision_type`: material_receipt
  - `material_type`: major_materials
  - `scope`: 주요자재 최종 승인
  - `name`: 자재 반입 검수 결정 (책임감리 최종 승인)

## Node — SiteEngineer / `SiteEngineer:form_material_receipt_site_engineer`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: 자재검수일보 [6. 서명란] 현장대리인/자재관리자
- properties:
  - `role`: site_representative_and_qm
  - `ko`: 현장대리인 / 자재관리자 / 품질관리자
  - `qualification`: 시공기술자 (건설기술인 특급/고급) + 품질관리책임자 교육 이수
  - `responsibility`: 시공사 자체 1차 검수
  - `name`: 현장대리인 (자재관리자/품질관리자)

## Node — Supervisor / `Supervisor:form_material_receipt_supervisor`
- space: `subject`
- node_type: `Supervisor`
- source_article: 자재검수일보 [6. 서명란] 담당감리원
- properties:
  - `role`: primary_supervisor
  - `ko`: 담당감리원
  - `qualification`: 건설사업관리기술자
  - `responsibility`: 감리단 1차 확인
  - `name`: 담당감리원

## Node — ChiefSupervisor / `ChiefSupervisor:form_material_receipt_chief_supervisor`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: 자재검수일보 [6. 서명란] 책임감리원
- properties:
  - `role`: chief_supervisor
  - `ko`: 책임감리원
  - `qualification`: 책임감리원 (특급 + 교육 이수)
  - `responsibility`: 주요자재 최종 승인
  - `name`: 책임감리원 (감리단장)

## Node — DecisionOutcome / `DecisionOutcome:form_material_receipt_01`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: 자재검수일보 [5. 종합판정]
- properties:
  - `status_enum`: ["pass", "conditional_pass", "fail"]
  - `ko_status`: {"pass": "합격", "conditional_pass": "조건부 합격", "fail": "불합격(반품)"}
  - `actions`: ["반품", "등급 하향 사용", "보수후 사용", "폐기"]
  - `name`: 자재 검수 결과
