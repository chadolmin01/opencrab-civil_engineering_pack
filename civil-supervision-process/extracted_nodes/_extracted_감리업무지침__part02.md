# Extracted graph — 감리업무지침__part02.jsonl

_source jsonl: 감리업무지침__part02.jsonl_

## Edges

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_01` (decision)
- to: `WorkType:concrete-placement` (concept)
- source_article: 3.2.1

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_01` (decision)
- to: `WorkType:rebar-assembly` (concept)
- source_article: 3.2.1

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_01` (decision)
- to: `Specification:supervision_guide_sec3-2_01` (resource)
- source_article: 3.2.1

## Edge — `yields`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_01` (decision)
- to: `DecisionOutcome:key-quality-approved` (outcome)
- source_article: 3.2.1

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec3-2_01` (subject)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_02` (decision)
- source_article: 3.2.2

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_02` (decision)
- source_article: 3.2.2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_02` (decision)
- to: `Specification:supervision_guide_sec3-2_01` (resource)
- source_article: 3.2.2

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_02` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_01` (decision)
- source_article: 3.2.2

## Edge — `yields`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_02` (decision)
- to: `DecisionOutcome:quality-plan-approved` (outcome)
- source_article: 3.2.2

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec3-2_01` (subject)
- to: `MaterialReceiptDecision:supervision_guide_sec3-2_01` (decision)
- source_article: 3.2.3-1

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `MaterialReceiptDecision:supervision_guide_sec3-2_01` (decision)
- source_article: 3.2.3-1

## Edge — `based_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-2_01` (decision)
- to: `TestReport:supervision_guide_sec3-2_02` (resource)
- source_article: 3.2.3-1

## Edge — `depends_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-2_01` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_02` (decision)
- source_article: 3.2.3-1

## Edge — `yields`
- from: `MaterialReceiptDecision:supervision_guide_sec3-2_01` (decision)
- to: `DecisionOutcome:material-selection-pass` (outcome)
- source_article: 3.2.3-1

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec3-2_01` (subject)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- source_article: 3.2.3-2

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- source_article: 3.2.3-2

## Edge — `targets_facility`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- to: `Facility:site-test-lab` (concept)
- source_article: 3.2.3-2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- to: `TestReport:supervision_guide_sec3-2_03` (resource)
- source_article: 3.2.3-2

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_02` (decision)
- source_article: 3.2.3-2

## Edge — `yields`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- to: `DecisionOutcome:quality-test-pass` (outcome)
- source_article: 3.2.3-2

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec3-2_01` (subject)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_04` (decision)
- source_article: 3.2.4

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_04` (decision)
- source_article: 3.2.4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_04` (decision)
- to: `TestReport:supervision_guide_sec3-2_01` (resource)
- source_article: 3.2.4

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_04` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- source_article: 3.2.4

## Edge — `yields`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_04` (decision)
- to: `DecisionOutcome:test-fail-rework` (outcome)
- source_article: 3.2.4

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_01` (subject)
- to: `StageApprovalDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.1

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.1

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-3_01` (decision)
- to: `Specification:supervision_guide_sec3-3_01` (resource)
- source_article: 3.3.1

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec3-3_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec2-5_01` (decision)
- source_article: 3.3.1

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec3-3_01` (decision)
- to: `DecisionOutcome:construction-plan-approved` (outcome)
- source_article: 3.3.1

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_01` (subject)
- to: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.2

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.2

## Edge — `targets_component`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `StructuralComponent:reinforcement-bar` (concept)
- source_article: 3.3.2

## Edge — `targets_component`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `StructuralComponent:scaffold-falsework` (concept)
- source_article: 3.3.2

## Edge — `targets_component`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `StructuralComponent:construction-joint` (concept)
- source_article: 3.3.2

## Edge — `targets_component`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `StructuralComponent:concrete-member` (concept)
- source_article: 3.3.2

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `Drawing:supervision_guide_sec3-3_01` (resource)
- source_article: 3.3.2

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `Drawing:supervision_guide_sec2-3_01` (resource)
- source_article: 3.3.2

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `Specification:supervision_guide_sec2-3_01` (resource)
- source_article: 3.3.2

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `StageApprovalDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.2

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `DecisionOutcome:shop-drawing-approved` (outcome)
- source_article: 3.3.2

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec3-2_01` (subject)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.4

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.4

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- to: `StructuralComponent:concrete-member` (concept)
- source_article: 3.3.4

## Edge — `targets_facility`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- to: `Facility:batch-plant` (concept)
- source_article: 3.3.4

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- to: `WorkType:concrete-placement` (concept)
- source_article: 3.3.4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- to: `WorkPermit:supervision_guide_sec3-3_02` (resource)
- source_article: 3.3.4

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- to: `Checklist:supervision_guide_sec3-3_01` (resource)
- source_article: 3.3.4

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.4

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- source_article: 3.3.4

## Edge — `yields`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- to: `DecisionOutcome:concrete-pass` (outcome)
- source_article: 3.3.4

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_01` (subject)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.5

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.5

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `StructuralComponent:reinforcement-bar` (concept)
- source_article: 3.3.5

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `StructuralComponent:concrete-member` (concept)
- source_article: 3.3.5

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `StructuralComponent:scaffold-falsework` (concept)
- source_article: 3.3.5

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `StructuralComponent:foundation` (concept)
- source_article: 3.3.5

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `WorkType:rebar-assembly` (concept)
- source_article: 3.3.5

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `WorkType:concrete-placement` (concept)
- source_article: 3.3.5

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `WorkType:formwork-falsework` (concept)
- source_article: 3.3.5

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `WorkType:earthwork` (concept)
- source_article: 3.3.5

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `Checklist:supervision_guide_sec3-3_01` (resource)
- source_article: 3.3.5

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `WorkPermit:supervision_guide_sec3-3_01` (resource)
- source_article: 3.3.5

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `Specification:supervision_guide_sec3-3_02` (resource)
- source_article: 3.3.5

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.5

## Edge — `yields`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `DecisionOutcome:inspection-pass-next-stage` (outcome)
- source_article: 3.3.5

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_01` (subject)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- source_article: 3.3.6

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- source_article: 3.3.6

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- to: `StructuralComponent:culvert-retaining-wall` (concept)
- source_article: 3.3.6

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- to: `StructuralComponent:foundation` (concept)
- source_article: 3.3.6

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- to: `StructuralComponent:concrete-member` (concept)
- source_article: 3.3.6

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- to: `SupervisionLog:supervision_guide_sec3-3_03` (resource)
- source_article: 3.3.6

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.6

## Edge — `yields`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- to: `DecisionOutcome:dimension-pass` (outcome)
- source_article: 3.3.6

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_01` (subject)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_04` (decision)
- source_article: 3.3.7

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_04` (decision)
- source_article: 3.3.7

## Edge — `targets_component`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_04` (decision)
- to: `StructuralComponent:buried-utility` (concept)
- source_article: 3.3.7

## Edge — `targets_work_type`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_04` (decision)
- to: `WorkType:underwater-buried-work` (concept)
- source_article: 3.3.7

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_04` (decision)
- to: `SupervisionLog:supervision_guide_sec3-3_03` (resource)
- source_article: 3.3.7

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_04` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.7

## Edge — `yields`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_04` (decision)
- to: `DecisionOutcome:buried-pass` (outcome)
- source_article: 3.3.7

## Edge — `performs`
- from: `ChiefSupervisor:supervision_guide_sec1-3_01` (subject)
- to: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- source_article: 3.3.8

## Edge — `grants_authority_for`
- from: `Qualification:chief-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- source_article: 3.3.8

## Edge — `targets_component`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `StructuralComponent:rock-bedrock` (concept)
- source_article: 3.3.8

## Edge — `targets_component`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `StructuralComponent:foundation` (concept)
- source_article: 3.3.8

## Edge — `targets_facility`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `Facility:tunnel` (concept)
- source_article: 3.3.8

## Edge — `targets_work_type`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `WorkType:excavation-rock` (concept)
- source_article: 3.3.8

## Edge — `targets_work_type`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `WorkType:tunnel-excavation` (concept)
- source_article: 3.3.8

## Edge — `targets_work_type`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `WorkType:foundation-work` (concept)
- source_article: 3.3.8

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `Drawing:supervision_guide_sec2-8_01` (resource)
- source_article: 3.3.8

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `TestReport:supervision_guide_sec3-2_02` (resource)
- source_article: 3.3.8

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec2-8_01` (decision)
- source_article: 3.3.8

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec3-3_03` (decision)
- to: `DecisionOutcome:rock-decision-approved` (outcome)
- source_article: 3.3.8

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec3-2_01` (subject)
- to: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.11

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.11

## Edge — `targets_facility`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- to: `Facility:batch-plant` (concept)
- source_article: 3.3.11

## Edge — `based_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- to: `WorkPermit:supervision_guide_sec3-3_03` (resource)
- source_article: 3.3.11

## Edge — `based_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- to: `TestReport:supervision_guide_sec3-2_02` (resource)
- source_article: 3.3.11

## Edge — `based_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- to: `TestReport:supervision_guide_sec3-2_05` (resource)
- source_article: 3.3.11

## Edge — `depends_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_02` (decision)
- source_article: 3.3.11

## Edge — `yields`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- to: `DecisionOutcome:supplier-approved` (outcome)
- source_article: 3.3.11

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec3-2_01` (subject)
- to: `MaterialReceiptDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.12

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `MaterialReceiptDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.12

## Edge — `based_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_02` (decision)
- to: `MaterialReceiptReport:supervision_guide_sec3-3_01` (resource)
- source_article: 3.3.12

## Edge — `depends_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_02` (decision)
- to: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.12

## Edge — `yields`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_02` (decision)
- to: `DecisionOutcome:material-receipt-pass` (outcome)
- source_article: 3.3.12

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_01` (subject)
- to: `MaterialReceiptDecision:supervision_guide_sec3-3_03` (decision)
- source_article: 3.3.13

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `MaterialReceiptDecision:supervision_guide_sec3-3_03` (decision)
- source_article: 3.3.13

## Edge — `based_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_03` (decision)
- to: `MaterialReceiptReport:supervision_guide_sec3-3_02` (resource)
- source_article: 3.3.13

## Edge — `based_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_03` (decision)
- to: `MaterialReceiptReport:supervision_guide_sec3-3_03` (resource)
- source_article: 3.3.13

## Edge — `depends_on`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_03` (decision)
- to: `MaterialReceiptDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.13

## Edge — `yields`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_03` (decision)
- to: `DecisionOutcome:issued-material-approved` (outcome)
- source_article: 3.3.13

## Edge — `performs`
- from: `ChiefSupervisor:supervision_guide_sec1-3_01` (subject)
- to: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.17

## Edge — `grants_authority_for`
- from: `Qualification:chief-supervisor` (concept)
- to: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.17

## Edge — `targets_work_type`
- from: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- to: `WorkType:concrete-placement` (concept)
- source_article: 3.3.17

## Edge — `targets_work_type`
- from: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- to: `WorkType:rebar-assembly` (concept)
- source_article: 3.3.17

## Edge — `targets_work_type`
- from: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- to: `WorkType:formwork-falsework` (concept)
- source_article: 3.3.17

## Edge — `based_on`
- from: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- to: `SupervisionLog:supervision_guide_sec3-3_03` (resource)
- source_article: 3.3.17

## Edge — `based_on`
- from: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- to: `SupervisionLog:supervision_guide_sec3-1_01` (resource)
- source_article: 3.3.17

## Edge — `depends_on`
- from: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.17

## Edge — `depends_on`
- from: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.17

## Edge — `depends_on`
- from: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_04` (decision)
- source_article: 3.3.17

## Edge — `yields`
- from: `WorkPermitDecision:supervision_guide_sec3-3_01` (decision)
- to: `DecisionOutcome:stop-order-issued` (outcome)
- source_article: 3.3.17

## Edge — `performs`
- from: `ChiefSupervisor:supervision_guide_sec1-3_01` (subject)
- to: `StageApprovalDecision:supervision_guide_sec3-4_01` (decision)
- source_article: 3.4

## Edge — `grants_authority_for`
- from: `Qualification:chief-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec3-4_01` (decision)
- source_article: 3.4

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-4_01` (decision)
- to: `Drawing:supervision_guide_sec2-3_01` (resource)
- source_article: 3.4

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-4_01` (decision)
- to: `Specification:supervision_guide_sec2-3_01` (resource)
- source_article: 3.4

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec3-4_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.4

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec3-4_01` (decision)
- to: `DecisionOutcome:design-change-approved` (outcome)
- source_article: 3.4

## Edge — `performs`
- from: `ChiefSupervisor:supervision_guide_sec1-3_01` (subject)
- to: `StageApprovalDecision:supervision_guide_sec3-5_01` (decision)
- source_article: 3.5.2, 3.5.3

## Edge — `grants_authority_for`
- from: `Qualification:chief-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec3-5_01` (decision)
- source_article: 3.5.2, 3.5.3

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-5_01` (decision)
- to: `SupervisionLog:supervision_guide_sec3-1_02` (resource)
- source_article: 3.5.2, 3.5.3

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec3-5_01` (decision)
- to: `ConstructionLog:supervision_guide_sec3-1_01` (resource)
- source_article: 3.5.2, 3.5.3

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec3-5_01` (decision)
- to: `DecisionOutcome:schedule-recovery-approved` (outcome)
- source_article: 3.5.2, 3.5.3

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec3-6_01` (subject)
- to: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- source_article: 3.6.2

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- source_article: 3.6.2

## Edge — `targets_work_type`
- from: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- to: `WorkType:high-risk-work` (concept)
- source_article: 3.6.2

## Edge — `targets_work_type`
- from: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- to: `WorkType:blasting-work` (concept)
- source_article: 3.6.2

## Edge — `targets_work_type`
- from: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- to: `WorkType:fall-risk-work` (concept)
- source_article: 3.6.2

## Edge — `based_on`
- from: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- to: `Specification:supervision_guide_sec3-6_01` (resource)
- source_article: 3.6.2

## Edge — `depends_on`
- from: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec2-5_01` (decision)
- source_article: 3.6.2

## Edge — `yields`
- from: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- to: `DecisionOutcome:safety-plan-approved` (outcome)
- source_article: 3.6.2

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec3-6_01` (subject)
- to: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- source_article: 3.6.3

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- source_article: 3.6.3

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- to: `Facility:bridge` (concept)
- source_article: 3.6.3

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- to: `Facility:tunnel` (concept)
- source_article: 3.6.3

## Edge — `targets_facility`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- to: `Facility:road` (concept)
- source_article: 3.6.3

## Edge — `based_on`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- to: `SafetyInspectionReport:supervision_guide_sec3-6_02` (resource)
- source_article: 3.6.3

## Edge — `based_on`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- to: `SafetyInspectionReport:supervision_guide_sec3-6_03` (resource)
- source_article: 3.6.3

## Edge — `depends_on`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- to: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- source_article: 3.6.3

## Edge — `yields`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- to: `DecisionOutcome:safety-inspection-pass` (outcome)
- source_article: 3.6.3

## Edge — `performs`
- from: `ChiefSupervisor:supervision_guide_sec1-3_01` (subject)
- to: `SafetyInspectionDecision:supervision_guide_sec3-6_02` (decision)
- source_article: 3.6.6

## Edge — `grants_authority_for`
- from: `Qualification:chief-supervisor` (concept)
- to: `SafetyInspectionDecision:supervision_guide_sec3-6_02` (decision)
- source_article: 3.6.6

## Edge — `based_on`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_02` (decision)
- to: `SafetyInspectionReport:supervision_guide_sec3-6_04` (resource)
- source_article: 3.6.6

## Edge — `based_on`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_02` (decision)
- to: `SafetyInspectionReport:supervision_guide_sec3-6_01` (resource)
- source_article: 3.6.6

## Edge — `depends_on`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_02` (decision)
- to: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- source_article: 3.6.6

## Edge — `yields`
- from: `SafetyInspectionDecision:supervision_guide_sec3-6_02` (decision)
- to: `DecisionOutcome:accident-reported` (outcome)
- source_article: 3.6.6

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_02` (subject)
- to: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- source_article: 4.2

## Edge — `grants_authority_for`
- from: `Qualification:non-resident-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- source_article: 4.2

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- to: `TestReport:supervision_guide_sec3-2_01` (resource)
- source_article: 4.2

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- to: `SupervisionLog:supervision_guide_sec3-3_03` (resource)
- source_article: 4.2

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- to: `MaterialReceiptReport:supervision_guide_sec3-3_01` (resource)
- source_article: 4.2

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 4.2

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- source_article: 4.2

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- to: `DecisionOutcome:progress-pass` (outcome)
- source_article: 4.2

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_02` (subject)
- to: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- source_article: 4.3.2

## Edge — `grants_authority_for`
- from: `Qualification:non-resident-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- source_article: 4.3.2

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- to: `TestReport:supervision_guide_sec3-2_01` (resource)
- source_article: 4.3.2

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- to: `Drawing:supervision_guide_sec4-3_01` (resource)
- source_article: 4.3.2

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- source_article: 4.3.2

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- to: `DecisionOutcome:pre-final-pass` (outcome)
- source_article: 4.3.2

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_02` (subject)
- to: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- source_article: 4.3.3

## Edge — `grants_authority_for`
- from: `Qualification:non-resident-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- source_article: 4.3.3

## Edge — `targets_facility`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `Facility:bridge` (concept)
- source_article: 4.3.3

## Edge — `targets_facility`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `Facility:tunnel` (concept)
- source_article: 4.3.3

## Edge — `targets_facility`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `Facility:road` (concept)
- source_article: 4.3.3

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `Drawing:supervision_guide_sec4-3_01` (resource)
- source_article: 4.3.3

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `TestReport:supervision_guide_sec3-2_01` (resource)
- source_article: 4.3.3

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `SupervisionLog:supervision_guide_sec3-3_03` (resource)
- source_article: 4.3.3

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `SafetyInspectionReport:supervision_guide_sec3-6_01` (resource)
- source_article: 4.3.3

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- source_article: 4.3.3

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `DecisionOutcome:final-pass` (outcome)
- source_article: 4.3.3

## Edge — `performs`
- from: `ChiefSupervisor:supervision_guide_sec1-3_01` (subject)
- to: `StageApprovalDecision:supervision_guide_sec4-3_03` (decision)
- source_article: 4.3.4

## Edge — `grants_authority_for`
- from: `Qualification:chief-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec4-3_03` (decision)
- source_article: 4.3.4

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_03` (decision)
- to: `Drawing:supervision_guide_sec4-3_01` (resource)
- source_article: 4.3.4

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_03` (decision)
- to: `SupervisionLog:supervision_guide_sec3-3_03` (resource)
- source_article: 4.3.4

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_03` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- source_article: 4.3.4

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec4-3_03` (decision)
- to: `DecisionOutcome:as-built-approved` (outcome)
- source_article: 4.3.4

## Edge — `performs`
- from: `ChiefSupervisor:supervision_guide_sec1-3_01` (subject)
- to: `StageApprovalDecision:supervision_guide_sec4-3_04` (decision)
- source_article: 4.3.1

## Edge — `grants_authority_for`
- from: `Qualification:chief-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec4-3_04` (decision)
- source_article: 4.3.1

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_04` (decision)
- to: `TestReport:supervision_guide_sec4-3_01` (resource)
- source_article: 4.3.1

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec4-3_04` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- source_article: 4.3.1

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec4-3_04` (decision)
- to: `DecisionOutcome:trial-pass` (outcome)
- source_article: 4.3.1

## Edge — `performs`
- from: `ChiefSupervisor:supervision_guide_sec1-3_01` (subject)
- to: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- source_article: 5.1

## Edge — `grants_authority_for`
- from: `Qualification:chief-supervisor` (concept)
- to: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- source_article: 5.1

## Edge — `targets_facility`
- from: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- to: `Facility:bridge` (concept)
- source_article: 5.1

## Edge — `targets_facility`
- from: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- to: `Facility:tunnel` (concept)
- source_article: 5.1

## Edge — `targets_facility`
- from: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- to: `Facility:road` (concept)
- source_article: 5.1

## Edge — `targets_facility`
- from: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- to: `Facility:drainage-gate` (concept)
- source_article: 5.1

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- to: `Drawing:supervision_guide_sec4-3_01` (resource)
- source_article: 5.1
