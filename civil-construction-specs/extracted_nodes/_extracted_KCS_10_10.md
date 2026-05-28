# Extracted graph — KCS_10_10.jsonl

_source jsonl: KCS_10_10.jsonl_

## Nodes

## Node — Org / `Org:kcsc`
- space: `subject`
- node_type: `Org`
- source_article: KCS 10 10 sec1
- properties:
  - `name_ko`: 국가건설기준센터
  - `name_en`: Korea Construction Standards Center
  - `role`: KDS·KCS 표준 관리 기관

## Node — Org / `Org:ordering-agency-kcs1010`
- space: `subject`
- node_type: `Org`
- source_article: KCS 10 10 sec5
- properties:
  - `name_ko`: 발주자
  - `scope`: 공사 발주, 자재 승인 최종 권한, 검측 결과 종합 판정

## Node — SiteEngineer / `SiteEngineer:kcs10_10_sec3_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS 10 10 sec3
- properties:
  - `name_ko`: 시공자(현장대리인)
  - `duties`: ["설계도서 검토서 작성·제출", "시공계획서 작성", "시공상세도면 작성", "자재 견본 첨부 제출", "검측 요청"]
  - `source_standard`: KCS 10 10 05

## Node — SiteEngineer / `SiteEngineer:kcs10_10_sec3-3_01`
- space: `subject`
- node_type: `SiteEngineer`
- source_article: KCS 10 10 sec3-3
- properties:
  - `name_ko`: 현장대리인
  - `obligation`: 현장 상주
  - `source_standard`: KCS 10 10 05 3.3

## Node — SafetyManager / `SafetyManager:kcs10_10_sec3-3_01`
- space: `subject`
- node_type: `SafetyManager`
- source_article: KCS 10 10 sec3-3
- properties:
  - `name_ko`: 안전관리자
  - `obligation`: 현장 상주
  - `source_standard`: KCS 10 10 05 3.3

## Node — Supervisor / `Supervisor:kcs10_10_sec4-5_01`
- space: `subject`
- node_type: `Supervisor`
- source_article: KCS 10 10 sec4-5
- properties:
  - `name_ko`: 감리원/공사감독자
  - `duties`: ["검측 수행(측량·입회·승인·시험)", "검측 결과 통보", "시공계획서 확인", "시공상세도면 검토", "자재 견본 검수"]
  - `source_standard`: KCS 10 10 10 4.5

## Node — ChiefSupervisor / `ChiefSupervisor:kcs10_10_sec5_01`
- space: `subject`
- node_type: `ChiefSupervisor`
- source_article: KCS 10 10 sec5
- properties:
  - `name_ko`: 책임감리원
  - `scope`: 검측·검수·승인 권한 보유, 자재 승인 위임 받음
  - `source_standard`: KCS 10 10 05 5

## Node — Qualification / `Qualification:kcs10_10_site-engineer`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 10 10 sec3-3
- properties:
  - `name_ko`: 현장대리인 자격
  - `scope`: 건설공사 시공자 측 현장 책임자, 현장 상주 의무
  - `source_standard`: KCS 10 10 05

## Node — Qualification / `Qualification:kcs10_10_safety-manager`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 10 10 sec3-3
- properties:
  - `name_ko`: 안전관리자 자격
  - `scope`: 공사 현장 안전관리 담당, 현장 상주
  - `source_standard`: KCS 10 10 05

## Node — Qualification / `Qualification:kcs10_10_supervisor`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 10 10 sec5
- properties:
  - `name_ko`: 공사감독자/감리원 자격
  - `scope`: 검측·검수·승인 권한
  - `source_standard`: KCS 10 10 05

## Node — Qualification / `Qualification:kcs10_10_chief-supervisor`
- space: `concept`
- node_type: `Qualification`
- source_article: KCS 10 10 sec5
- properties:
  - `name_ko`: 책임감리원 자격
  - `scope`: 검측·검수·승인 총괄, 자재 승인
  - `source_standard`: KCS 10 10 05

## Node — WorkType / `WorkType:kcs10_10_common-construction`
- space: `concept`
- node_type: `WorkType`
- source_article: KCS 10 10 sec2
- properties:
  - `name_ko`: 공통공사
  - `scope`: 건설공사 공통 일반사항이 적용되는 공종
  - `source_standard`: KCS 10 00 00

## Node — Specification / `Specification:kcs10_10_05`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec1
- properties:
  - `name_ko`: KCS 10 10 05 공사일반
  - `code`: KCS 10 10 05
  - `scope`: 공사일반·시공자 의무·감독자 검측 일반 절차
  - `legal_basis`: 건설기술 진흥법 제44조, 시행령 제65조

## Node — Specification / `Specification:kcs10_10_10`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec4
- properties:
  - `name_ko`: KCS 10 10 10 공무행정요건
  - `code`: KCS 10 10 10
  - `scope`: 공무행정 절차(시공계획서·시공상세도면·자재 승인·착공·검측)

## Node — Specification / `Specification:kcs10_10_sec3-1_design-review`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec3-1
- properties:
  - `name_ko`: 설계도서 검토 기준
  - `requirement`: 착수 60일 이내 제출, 2부, 검토항목: 현장 조건 일치성, 시공 가능성, 타 공사 부합성, 도서 일치성
  - `source_standard`: KCS 10 10 05 3.1

## Node — Specification / `Specification:kcs10_10_sec3-2_pre-start-meeting`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec3-2
- properties:
  - `name_ko`: 착공 전 절차 기준
  - `requirement`: 착공 준비회의: 계약 후 15일 이내; 착공 실무회의: 실착공 후 30일 이내; 회의 결과 조치계획서: 3일 이내 제출
  - `source_standard`: KCS 10 10 05 3.2

## Node — Specification / `Specification:kcs10_10_sec3-5_photo-record`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec3-5
- properties:
  - `name_ko`: 사진·동영상 기록 기준
  - `requirement`: 매몰부·주요공정 촬영 의무, 사진에 공사명·공종·위치·치수·촬영일시 표시
  - `source_standard`: KCS 10 10 05 3.5

## Node — Specification / `Specification:kcs10_10_sec3-6_meeting`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec3-6
- properties:
  - `name_ko`: 공사협의 기준
  - `requirement`: 월 1회 이상 정기 진행회의, 작업 착수 3일 전 착수회의 통보
  - `source_standard`: KCS 10 10 05 3.6

## Node — Specification / `Specification:kcs10_10_sec4-1_const-plan`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec4-1
- properties:
  - `name_ko`: 시공계획서 제출 기준
  - `requirement`: 각 공종 착수 14일 전 제출, 공사감독자 확인 7일
  - `source_standard`: KCS 10 10 10 4.1

## Node — Specification / `Specification:kcs10_10_sec4-2_shop-drawing`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec4-2
- properties:
  - `name_ko`: 시공상세도면 제출 기준
  - `requirement`: 공종 착수 15일 전(단순 7일 전), 검토 단순 7일·기술검토 14일, 기일내 미통보 시 자동 승인
  - `source_standard`: KCS 10 10 10 4.2

## Node — Specification / `Specification:kcs10_10_sec4-3_material-approval`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec4-3
- properties:
  - `name_ko`: 자재 승인 기준
  - `requirement`: 자재 반입 15일 전 견본 첨부 제출, 품질시험·검사 결과 전산처리
  - `source_standard`: KCS 10 10 10 4.3

## Node — Specification / `Specification:kcs10_10_sec4-4_start-notice`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec4-4
- properties:
  - `name_ko`: 착공신고 기준
  - `requirement`: 계약 체결일로부터 5일 내, 각 3부, 첨부: 공정표·인력장비계획·안전관리계획
  - `source_standard`: KCS 10 10 10 4.4

## Node — Specification / `Specification:kcs10_10_sec4-5_inspection`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec4-5
- properties:
  - `name_ko`: 검측 절차 기준
  - `requirement`: 검측은 측량·입회·승인·시험으로 수행, 시공자 요청 즉시 수행, 결과 통보, 설계도서 상이 시 즉시 보고
  - `source_standard`: KCS 10 10 10 4.5

## Node — Specification / `Specification:kcs10_10_sec4-6_completion`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec4-6
- properties:
  - `name_ko`: 기성/준공검사 기준
  - `requirement`: 기성검사원 공사비 청구 전 제출, 준공검사 전 부분 검사, 미합격 시 재시공 후 재검사원 제출
  - `source_standard`: KCS 10 10 10 4.6

## Node — Specification / `Specification:kcs10_10_sec4-7_progress`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec4-7
- properties:
  - `name_ko`: 공정관리 기준
  - `requirement`: 일일보고 익일 12:00까지, 부진 기준 월간 10% 이상 또는 누계 5% 이상 지연 시 만회대책 보고
  - `source_standard`: KCS 10 10 10 4.7

## Node — ConstructionLog / `ConstructionLog:kcs10_10_design-review-report`
- space: `resource`
- node_type: `ConstructionLog`
- source_article: KCS 10 10 sec3-1
- properties:
  - `name_ko`: 설계도서 검토서
  - `copies`: 2
  - `deadline`: 착수 60일 이내
  - `source_standard`: KCS 10 10 05 3.1

## Node — Specification / `Specification:kcs10_10_const-plan-document`
- space: `resource`
- node_type: `Specification`
- source_article: KCS 10 10 sec4-1
- properties:
  - `name_ko`: 시공계획서
  - `includes`: ["가설계획", "식재 이식계획", "시공관리체계", "공종별 시공방법·양생계획", "교통처리·환경오염 방지대책", "타 공사·기관 협의 결과"]
  - `source_standard`: KCS 10 10 10 4.1

## Node — Drawing / `Drawing:kcs10_10_shop-drawing`
- space: `resource`
- node_type: `Drawing`
- source_article: KCS 10 10 sec4-2
- properties:
  - `name_ko`: 시공상세도면
  - `source_standard`: KCS 10 10 10 4.2

## Node — Checklist / `Checklist:kcs10_10_inspection-request`
- space: `resource`
- node_type: `Checklist`
- source_article: KCS 10 10 sec4-5
- properties:
  - `name_ko`: 검측 요청서
  - `methods`: ["측량", "입회", "승인", "시험"]
  - `source_standard`: KCS 10 10 10 4.5

## Node — TestReport / `TestReport:kcs10_10_completion-inspection`
- space: `resource`
- node_type: `TestReport`
- source_article: KCS 10 10 sec4-6
- properties:
  - `name_ko`: 기성검사원/준공검사원
  - `source_standard`: KCS 10 10 10 4.6

## Node — SupervisionLog / `SupervisionLog:kcs10_10_daily-report`
- space: `resource`
- node_type: `SupervisionLog`
- source_article: KCS 10 10 sec4-7
- properties:
  - `name_ko`: 공사 일일보고
  - `deadline`: 익일 12:00
  - `source_standard`: KCS 10 10 10 4.7

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:kcs10_10_sec4-5_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 10 10 sec4-5
- properties:
  - `name_ko`: 검측 결정
  - `description`: 감리원이 시공자 요청에 따라 측량·입회·승인·시험 방법으로 검측 수행 후 합부 판정
  - `method`: ["측량", "입회", "승인", "시험"]
  - `source_standard`: KCS 10 10 10 4.5

## Node — MaterialReceiptDecision / `MaterialReceiptDecision:kcs10_10_sec4-3_01`
- space: `decision`
- node_type: `MaterialReceiptDecision`
- source_article: KCS 10 10 sec4-3
- properties:
  - `name_ko`: 자재 승인/검수 결정
  - `description`: 자재 반입 15일 전 견본 첨부 제출 → 감리자 검수 → 발주자 최종 승인
  - `lead_time_days`: 15
  - `source_standard`: KCS 10 10 10 4.3

## Node — StageApprovalDecision / `StageApprovalDecision:kcs10_10_sec4-1_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 10 10 sec4-1
- properties:
  - `name_ko`: 시공계획서 승인
  - `description`: 각 공종 착수 14일 전 시공계획서 제출, 7일 내 감독자 확인 → 승인 시 공사 착수 가능
  - `submit_days_before_start`: 14
  - `review_days`: 7
  - `source_standard`: KCS 10 10 10 4.1

## Node — StageApprovalDecision / `StageApprovalDecision:kcs10_10_sec4-2_01`
- space: `decision`
- node_type: `StageApprovalDecision`
- source_article: KCS 10 10 sec4-2
- properties:
  - `name_ko`: 시공상세도면 승인
  - `description`: 공종 착수 15일 전(단순 7일 전) 제출, 단순 7일·기술검토 14일 내 미통보 시 자동 승인
  - `auto_approval`: True
  - `source_standard`: KCS 10 10 10 4.2

## Node — WorkPermitDecision / `WorkPermitDecision:kcs10_10_sec4-4_01`
- space: `decision`
- node_type: `WorkPermitDecision`
- source_article: KCS 10 10 sec4-4
- properties:
  - `name_ko`: 착공신고
  - `description`: 계약 체결일로부터 5일 내, 각 3부 첨부서류와 함께 신고
  - `deadline_days`: 5
  - `source_standard`: KCS 10 10 10 4.4

## Node — ConstructionInspectionDecision / `ConstructionInspectionDecision:kcs10_10_sec4-6_01`
- space: `decision`
- node_type: `ConstructionInspectionDecision`
- source_article: KCS 10 10 sec4-6
- properties:
  - `name_ko`: 기성·준공검사 결정
  - `description`: 공사비 청구 전 기성검사, 완공 후 전 부분 준공검사, 미합격 시 재시공 후 재검사
  - `source_standard`: KCS 10 10 10 4.6

## Node — DecisionOutcome / `DecisionOutcome:kcs10_10_inspection-pass`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 10 10 sec4-5
- properties:
  - `name_ko`: 검측 합격
  - `result`: pass

## Node — DecisionOutcome / `DecisionOutcome:kcs10_10_inspection-fail`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 10 10 sec4-6
- properties:
  - `name_ko`: 검측 불합격 (재시공)
  - `result`: fail
  - `next_action`: 재시공 후 재검사원 제출

## Node — DecisionOutcome / `DecisionOutcome:kcs10_10_auto-approval`
- space: `outcome`
- node_type: `DecisionOutcome`
- source_article: KCS 10 10 sec4-2
- properties:
  - `name_ko`: 시공상세도면 자동승인
  - `result`: approved
  - `trigger`: 검토기간 내 미통보

## Edges

## Edge — `qualified_as`
- from: `SiteEngineer:kcs10_10_sec3_01` (subject)
- to: `Qualification:kcs10_10_site-engineer` (concept)
- source_article: KCS 10 10 sec3-3

## Edge — `qualified_as`
- from: `SafetyManager:kcs10_10_sec3-3_01` (subject)
- to: `Qualification:kcs10_10_safety-manager` (concept)
- source_article: KCS 10 10 sec3-3

## Edge — `qualified_as`
- from: `Supervisor:kcs10_10_sec4-5_01` (subject)
- to: `Qualification:kcs10_10_supervisor` (concept)
- source_article: KCS 10 10 sec4-5

## Edge — `qualified_as`
- from: `ChiefSupervisor:kcs10_10_sec5_01` (subject)
- to: `Qualification:kcs10_10_chief-supervisor` (concept)
- source_article: KCS 10 10 sec5

## Edge — `subclass_of`
- from: `Qualification:kcs10_10_chief-supervisor` (concept)
- to: `Qualification:kcs10_10_supervisor` (concept)
- source_article: KCS 10 10 sec5

## Edge — `grants_authority_for`
- from: `Qualification:kcs10_10_supervisor` (concept)
- to: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- source_article: KCS 10 10 sec4-5

## Edge — `grants_authority_for`
- from: `Qualification:kcs10_10_supervisor` (concept)
- to: `ConstructionInspectionDecision:kcs10_10_sec4-6_01` (decision)
- source_article: KCS 10 10 sec4-6

## Edge — `grants_authority_for`
- from: `Qualification:kcs10_10_chief-supervisor` (concept)
- to: `MaterialReceiptDecision:kcs10_10_sec4-3_01` (decision)
- source_article: KCS 10 10 sec4-3

## Edge — `grants_authority_for`
- from: `Qualification:kcs10_10_chief-supervisor` (concept)
- to: `StageApprovalDecision:kcs10_10_sec4-1_01` (decision)
- source_article: KCS 10 10 sec4-1

## Edge — `grants_authority_for`
- from: `Qualification:kcs10_10_chief-supervisor` (concept)
- to: `StageApprovalDecision:kcs10_10_sec4-2_01` (decision)
- source_article: KCS 10 10 sec4-2

## Edge — `grants_authority_for`
- from: `Qualification:kcs10_10_site-engineer` (concept)
- to: `WorkPermitDecision:kcs10_10_sec4-4_01` (decision)
- source_article: KCS 10 10 sec4-4

## Edge — `performs`
- from: `Supervisor:kcs10_10_sec4-5_01` (subject)
- to: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- source_article: KCS 10 10 sec4-5

## Edge — `performs`
- from: `Supervisor:kcs10_10_sec4-5_01` (subject)
- to: `ConstructionInspectionDecision:kcs10_10_sec4-6_01` (decision)
- source_article: KCS 10 10 sec4-6

## Edge — `performs`
- from: `ChiefSupervisor:kcs10_10_sec5_01` (subject)
- to: `MaterialReceiptDecision:kcs10_10_sec4-3_01` (decision)
- source_article: KCS 10 10 sec4-3

## Edge — `performs`
- from: `ChiefSupervisor:kcs10_10_sec5_01` (subject)
- to: `StageApprovalDecision:kcs10_10_sec4-1_01` (decision)
- source_article: KCS 10 10 sec4-1

## Edge — `performs`
- from: `ChiefSupervisor:kcs10_10_sec5_01` (subject)
- to: `StageApprovalDecision:kcs10_10_sec4-2_01` (decision)
- source_article: KCS 10 10 sec4-2

## Edge — `performs`
- from: `SiteEngineer:kcs10_10_sec3_01` (subject)
- to: `WorkPermitDecision:kcs10_10_sec4-4_01` (decision)
- source_article: KCS 10 10 sec4-4

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- to: `WorkType:kcs10_10_common-construction` (concept)
- source_article: KCS 10 10 sec2

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-6_01` (decision)
- to: `WorkType:kcs10_10_common-construction` (concept)
- source_article: KCS 10 10 sec2

## Edge — `targets_work_type`
- from: `MaterialReceiptDecision:kcs10_10_sec4-3_01` (decision)
- to: `WorkType:kcs10_10_common-construction` (concept)
- source_article: KCS 10 10 sec4-3

## Edge — `targets_work_type`
- from: `StageApprovalDecision:kcs10_10_sec4-1_01` (decision)
- to: `WorkType:kcs10_10_common-construction` (concept)
- source_article: KCS 10 10 sec4-1

## Edge — `targets_work_type`
- from: `StageApprovalDecision:kcs10_10_sec4-2_01` (decision)
- to: `WorkType:kcs10_10_common-construction` (concept)
- source_article: KCS 10 10 sec4-2

## Edge — `targets_work_type`
- from: `WorkPermitDecision:kcs10_10_sec4-4_01` (decision)
- to: `WorkType:kcs10_10_common-construction` (concept)
- source_article: KCS 10 10 sec4-4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- to: `Specification:kcs10_10_sec4-5_inspection` (resource)
- source_article: KCS 10 10 sec4-5

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- to: `Checklist:kcs10_10_inspection-request` (resource)
- source_article: KCS 10 10 sec4-5

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-6_01` (decision)
- to: `Specification:kcs10_10_sec4-6_completion` (resource)
- source_article: KCS 10 10 sec4-6

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-6_01` (decision)
- to: `TestReport:kcs10_10_completion-inspection` (resource)
- source_article: KCS 10 10 sec4-6

## Edge — `based_on`
- from: `MaterialReceiptDecision:kcs10_10_sec4-3_01` (decision)
- to: `Specification:kcs10_10_sec4-3_material-approval` (resource)
- source_article: KCS 10 10 sec4-3

## Edge — `based_on`
- from: `StageApprovalDecision:kcs10_10_sec4-1_01` (decision)
- to: `Specification:kcs10_10_sec4-1_const-plan` (resource)
- source_article: KCS 10 10 sec4-1

## Edge — `based_on`
- from: `StageApprovalDecision:kcs10_10_sec4-1_01` (decision)
- to: `Specification:kcs10_10_const-plan-document` (resource)
- source_article: KCS 10 10 sec4-1

## Edge — `based_on`
- from: `StageApprovalDecision:kcs10_10_sec4-2_01` (decision)
- to: `Specification:kcs10_10_sec4-2_shop-drawing` (resource)
- source_article: KCS 10 10 sec4-2

## Edge — `based_on`
- from: `StageApprovalDecision:kcs10_10_sec4-2_01` (decision)
- to: `Drawing:kcs10_10_shop-drawing` (resource)
- source_article: KCS 10 10 sec4-2

## Edge — `based_on`
- from: `WorkPermitDecision:kcs10_10_sec4-4_01` (decision)
- to: `Specification:kcs10_10_sec4-4_start-notice` (resource)
- source_article: KCS 10 10 sec4-4

## Edge — `based_on`
- from: `WorkPermitDecision:kcs10_10_sec4-4_01` (decision)
- to: `ConstructionLog:kcs10_10_design-review-report` (resource)
- source_article: KCS 10 10 sec3-1

## Edge — `based_on`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- to: `SupervisionLog:kcs10_10_daily-report` (resource)
- source_article: KCS 10 10 sec4-7

## Edge — `precedes`
- from: `StageApprovalDecision:kcs10_10_sec4-1_01` (decision)
- to: `WorkPermitDecision:kcs10_10_sec4-4_01` (decision)
- source_article: KCS 10 10 sec4-4

## Edge — `precedes`
- from: `StageApprovalDecision:kcs10_10_sec4-2_01` (decision)
- to: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- source_article: KCS 10 10 sec4-5

## Edge — `precedes`
- from: `MaterialReceiptDecision:kcs10_10_sec4-3_01` (decision)
- to: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- source_article: KCS 10 10 sec4-5

## Edge — `precedes`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- to: `ConstructionInspectionDecision:kcs10_10_sec4-6_01` (decision)
- source_article: KCS 10 10 sec4-6

## Edge — `depends_on`
- from: `WorkPermitDecision:kcs10_10_sec4-4_01` (decision)
- to: `StageApprovalDecision:kcs10_10_sec4-1_01` (decision)
- source_article: KCS 10 10 sec4-4

## Edge — `yields`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-5_01` (decision)
- to: `DecisionOutcome:kcs10_10_inspection-pass` (outcome)
- source_article: KCS 10 10 sec4-5

## Edge — `yields`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-6_01` (decision)
- to: `DecisionOutcome:kcs10_10_inspection-pass` (outcome)
- source_article: KCS 10 10 sec4-6

## Edge — `yields`
- from: `ConstructionInspectionDecision:kcs10_10_sec4-6_01` (decision)
- to: `DecisionOutcome:kcs10_10_inspection-fail` (outcome)
- source_article: KCS 10 10 sec4-6

## Edge — `yields`
- from: `StageApprovalDecision:kcs10_10_sec4-2_01` (decision)
- to: `DecisionOutcome:kcs10_10_auto-approval` (outcome)
- source_article: KCS 10 10 sec4-2
