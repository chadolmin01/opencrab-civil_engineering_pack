# Extracted graph — 감리업무지침__part03.jsonl

_source jsonl: 감리업무지침__part03.jsonl_

## Edges

## Edge — `based_on`
- from: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- to: `TestReport:supervision_guide_sec3-2_01` (resource)
- source_article: 5.1

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- source_article: 5.1

## Edge — `depends_on`
- from: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-3_03` (decision)
- source_article: 5.1

## Edge — `yields`
- from: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- to: `DecisionOutcome:handover-approved` (outcome)
- source_article: 5.1

## Edge — `performs`
- from: `Supervisor:supervision_guide_sec1-3_01` (subject)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-7_01` (decision)
- source_article: 3.7.2

## Edge — `grants_authority_for`
- from: `Qualification:resident-supervisor` (concept)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-7_01` (decision)
- source_article: 3.7.2

## Edge — `based_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-7_01` (decision)
- to: `Checklist:supervision_guide_sec3-7_01` (resource)
- source_article: 3.7.2

## Edge — `depends_on`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-7_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec2-5_01` (decision)
- source_article: 3.7.2

## Edge — `yields`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-7_01` (decision)
- to: `DecisionOutcome:env-pass` (outcome)
- source_article: 3.7.2

## Edge — `precedes`
- from: `ConstructionInspectionDecision:supervision_guide_sec2-3_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec2-5_01` (decision)
- source_article: 2.3->2.5

## Edge — `precedes`
- from: `StageApprovalDecision:supervision_guide_sec2-5_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 2.5->3.3.1

## Edge — `precedes`
- from: `StageApprovalDecision:supervision_guide_sec3-3_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.1->3.3.2

## Edge — `precedes`
- from: `StageApprovalDecision:supervision_guide_sec3-3_02` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.2->3.3.5

## Edge — `precedes`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-3_02` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_03` (decision)
- source_article: 3.3.5->3.3.6

## Edge — `precedes`
- from: `MaterialReceiptDecision:supervision_guide_sec3-2_01` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- source_article: 3.2.3-1->3.2.3-2

## Edge — `precedes`
- from: `ConstructionInspectionDecision:supervision_guide_sec3-2_03` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-2_04` (decision)
- source_article: 3.2.3-2->3.2.4

## Edge — `precedes`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_01` (decision)
- to: `MaterialReceiptDecision:supervision_guide_sec3-3_02` (decision)
- source_article: 3.3.11->3.3.12

## Edge — `precedes`
- from: `MaterialReceiptDecision:supervision_guide_sec3-3_02` (decision)
- to: `ConstructionInspectionDecision:supervision_guide_sec3-3_01` (decision)
- source_article: 3.3.12->3.3.4

## Edge — `precedes`
- from: `WorkPermitDecision:supervision_guide_sec3-6_01` (decision)
- to: `SafetyInspectionDecision:supervision_guide_sec3-6_01` (decision)
- source_article: 3.6.2->3.6.3

## Edge — `precedes`
- from: `StageApprovalDecision:supervision_guide_sec4-2_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- source_article: 4.2->4.3.2

## Edge — `precedes`
- from: `StageApprovalDecision:supervision_guide_sec4-3_01` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- source_article: 4.3.2->4.3.3

## Edge — `precedes`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-3_03` (decision)
- source_article: 4.3.3->4.3.4

## Edge — `precedes`
- from: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- to: `StageApprovalDecision:supervision_guide_sec5-1_01` (decision)
- source_article: 4.3.3->5.1

## Edge — `precedes`
- from: `StageApprovalDecision:supervision_guide_sec4-3_04` (decision)
- to: `StageApprovalDecision:supervision_guide_sec4-3_02` (decision)
- source_article: 4.3.1->4.3.3
