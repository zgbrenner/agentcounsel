# Example: Data Processing Agreement (DPA) Review

> **Illustrative example — not legal advice.** This is a sample of what the DPA Review skill (`skills/privacy/dpa-review/SKILL.md`) produces. Every party, date, and clause in it is **fictional** and was invented for illustration. It is the kind of draft work product a supervising attorney would review — not a finished deliverable, and not legal advice. See `examples/README.md`.

## Scenario

Lumen Health Apps, Inc. is a fictional company that builds a consumer wellness mobile application. It collects account information, self-reported health and symptom logs, and device usage data from individual users. Lumen wants to migrate its application database and file storage to a new cloud hosting vendor, DataNest Hosting Ltd., and DataNest has presented its standard form data processing addendum for signature. Lumen acts as the **data controller** for the user personal data, and DataNest would act as the **processor** hosting that data on Lumen's behalf. The privacy team has asked for a first-pass risk review of the DataNest DPA before the matter goes to outside counsel and before the next negotiation round. The main hosting services agreement has been provided in draft. Because the application handles self-reported health information, the review also flags a possible sector-specific overlay for specialist attention.

## Illustrative Output

### 1. Summary

This is a review of the **DataNest Standard Data Processing Addendum, v4.2, dated March 9, 2026** ("the DPA"), presented for signature by **DataNest Hosting Ltd.** ("DataNest") to **Lumen Health Apps, Inc.** ("Lumen"). The DPA designates Lumen as controller and DataNest as processor `[CONFIRM: client role and counterparty role under applicable law — the document's labels are not conclusive]`. The DPA would govern DataNest's hosting of personal data that Lumen collects from individual application users, including self-reported health and symptom information. The top risks identified are: (1) sub-processor use is permitted under a general authorization with no meaningful objection right; (2) the cross-border transfer mechanism is referenced only by a placeholder and no instrument is attached; (3) the breach-notification trigger is narrow and the timeframe may not allow Lumen to meet its own reporting obligations `[CONFIRM: verify deadline under applicable law]`; (4) audit rights are limited to a third-party report that may be up to 18 months old; and (5) the DPA's liability cap and the absence of a data-breach indemnity may leave Lumen exposed. The presence of self-reported health data also raises a possible sectoral overlay `[CONFIRM: possible sectoral overlay — specialist review recommended]`.

### 2. Document Structure Map

Sections present in the DPA:

- § 1 — Definitions and roles of the parties
- § 2 — Scope and nature of processing
- § 3 — Processor's processing instructions
- § 4 — Sub-processors
- § 5 — Security measures
- § 6 — Personal data breach notification
- § 7 — Audits and compliance verification
- § 8 — International data transfers
- § 9 — Deletion and return of data
- § 10 — Liability
- § 11 — Governing law

Standard sections that appear **absent or thin**:

- No dedicated data-subject-rights assistance clause; assistance is mentioned only in passing within § 3.
- No processing schedule or annex itemizing data categories, data subjects, and purposes; § 2 describes scope in general prose only.
- No sub-processor list is attached or referenced by link.
- No indemnity provision; § 10 addresses a liability cap only.

### 3. Risk Table

| Field | Value |
|---|---|
| Matter / Project | Lumen — DataNest hosting migration DPA review |
| Document Reviewed | DataNest Standard Data Processing Addendum, v4.2, dated March 9, 2026 |
| Counterparty | DataNest Hosting Ltd. |
| Client Role | `[CONFIRM: controller — confirm under applicable law]` |
| Reviewer | Priya Sandoval |
| Review Date | April 2, 2026 |
| Applicable Framework(s) | `[CONFIRM: framework(s) stated in document or identified by counsel — do not assume]` |
| Main Agreement Referenced | Yes — DataNest Hosting Services Agreement (draft) |

| # | Topic | Section / Clause | What It Says (Plain Language) | Risk to Client | Severity | Suggested Change | Attorney Note |
|---|---|---|---|---|---|---|---|
| 1 | Party Role Designation | § 1 | Labels Lumen as controller and DataNest as processor. | The labels may not reflect the actual relationship under the governing privacy regime; an incorrect designation can misallocate compliance obligations. | Med | Confirm roles with counsel; add a recital stating the factual basis for the designation. | `[CONFIRM: verify role under applicable framework]` |
| 2 | Scope and Nature of Processing | § 2 | Describes processing in general prose; no annex itemizing data categories, data subjects, or purposes. | Vague scope may authorize processing beyond what Lumen intends and leaves no clear record of what was agreed. | Med | Attach a detailed processing schedule listing data categories, subject groups, and purposes. | `[CONFIRM: scope matches actual processing activity]` |
| 3 | Processing Instructions | § 3 | Limits DataNest to Lumen's instructions but adds a broad carve-out for processing "as DataNest reasonably considers necessary to operate the service." | The carve-out grants the processor wide discretion that could permit processing outside documented instructions. | Med | Narrow the carve-out; require written instructions for any non-standard processing. | |
| 4 | Sub-Processor Authorization | § 4.1 | Grants general authorization for sub-processors; Lumen is notified by a webpage update with no objection right. | General authorization without a meaningful notice-and-objection right limits Lumen's visibility and control. | High | Require prior written approval or a genuine notice-and-objection right with a stated objection window. | |
| 5 | Sub-Processor Obligations | § 4.3 | States sub-processors will be bound by "substantially similar" terms; silent on whether DataNest remains liable for sub-processor acts. | Weak flow-down and unclear residual liability may leave Lumen exposed for sub-processor failures. | High | Require equivalent obligations and confirm DataNest remains fully liable for sub-processor acts and omissions. | |
| 6 | Security Measures | § 5 | Commits to "industry-standard technical and organizational measures" with no named standard or minimum-measures schedule. | General, aspirational language provides weak contractual protection and no measurable baseline. | Med | Reference a specific standard or attach a minimum-measures schedule; confirm obligations are not diluted by "as updated by DataNest." | |
| 7 | Data Subject Rights Assistance | § 3 (in passing) | Mentions assistance with data subject requests only briefly; no defined scope, timeframe, or cost terms. | An absent or vague assistance obligation shifts burden to Lumen and may impair timely responses to individuals. | Med | Add a dedicated clause specifying scope of assistance, a response timeframe, and cost allocation. | `[CONFIRM: verify assistance requirements under applicable law]` |
| 8 | Breach Notification — Trigger | § 6.1 | DataNest must notify Lumen only upon a "confirmed" personal data breach. | A "confirmed only" trigger may delay notification beyond what the applicable regime expects. | High | Broaden the trigger to when DataNest becomes aware of or reasonably suspects a breach. | `[CONFIRM: verify trigger standard under applicable law]` |
| 9 | Breach Notification — Timeframe | § 6.2 | States DataNest will notify Lumen "without undue delay" with no fixed outer limit. | An open-ended timeframe may not leave Lumen enough time to meet its own reporting obligations. | High | State a fixed outer limit confirmed to allow Lumen to meet any applicable reporting deadline. | `[CONFIRM: verify deadline under applicable law — do not compute]` |
| 10 | Breach Notification — Content | § 6.2 | Requires only "a description of the incident" in the notification. | Insufficient required content forces follow-up exchanges and may delay Lumen's own reporting. | Med | Specify minimum content: nature of the breach, categories and approximate number affected, likely consequences, and measures taken. | |
| 11 | Audit Rights | § 7 | Lumen's only verification right is to receive DataNest's third-party audit report, which may be up to 18 months old; no direct audit right. | A stale report-only substitute limits Lumen's ability to verify compliance in real time. | High | Preserve a right to conduct or commission a direct audit on reasonable notice; require a current report. | |
| 12 | Cross-Border Transfer Mechanism | § 8 | States transfers will be covered by "an appropriate transfer mechanism `[CONFIRM]`"; no instrument is attached. | Reliance on an unspecified, unattached mechanism may render cross-border transfers unlawful. | High | Identify and attach the chosen transfer instrument; confirm it is current and valid. | `[CONFIRM: validity of transfer mechanism under applicable framework]` |
| 13 | Deletion and Return on Termination | § 9 | DataNest will delete or return data "within a reasonable period" after termination; no certification of deletion is offered. | Vague timing allows indefinite retention, and the absence of certification leaves Lumen without evidence of compliance. | Med | Specify a fixed deletion/return timeframe, a certification requirement, and any permitted retention exceptions. | |
| 14 | Liability Cap | § 10.1 | Caps DataNest's DPA liability at the fees paid in the prior three months; states this is part of, not additional to, the main agreement cap. | A low, fee-based cap may provide inadequate protection for breach-related losses and regulatory exposure. | High | Confirm the relationship to the main agreement cap; seek a carve-out or higher sub-cap for data-breach liability. | `[CONFIRM: adequacy of cap under client's risk profile]` |
| 15 | Indemnity | (absent) | The DPA contains no indemnity from DataNest for breaches, regulatory fines, or third-party claims. | Absence of an indemnity may leave Lumen bearing costs caused by a processor failure. | Med | Seek a processor indemnity for losses caused by DataNest's acts or omissions; address regulatory fine allocation. | |
| 16 | Governing Law and Disputes | § 11 | The DPA's governing law differs from the draft main hosting agreement's governing law. | Conflicting governing-law provisions between the DPA and main agreement create enforcement uncertainty. | Med | Align the DPA with the main agreement or set a clear hierarchy. | `[CONFIRM: confirm governing law is appropriate and consistent with main agreement]` |
| 17 | Possible Sectoral Overlay | § 2 / general | The hosted data includes self-reported health and symptom information. | A sector-specific regime may overlay additional requirements on security, breach notification, and deletion terms. | Med | Route to an attorney with relevant sector expertise; revisit affected DPA terms after that review. | `[CONFIRM: possible sectoral overlay — specialist review recommended]` `[verify jurisdiction]` |

### 4. Prioritized Issue List

**High severity — redline or walkaway consideration**

- **Sub-processor controls (Issues 4 and 5).** General authorization with no objection right, weak flow-down terms, and unclear residual liability together mean Lumen could lose visibility into who handles its users' data and could remain exposed for sub-processor failures.
- **Breach notification (Issues 8 and 9).** A "confirmed only" trigger and an open-ended "without undue delay" timeframe may prevent Lumen from learning of and reporting a breach in time `[CONFIRM: verify deadline under applicable law]`.
- **Audit rights (Issue 11).** A report-only substitute that may be up to 18 months old gives Lumen little ability to verify DataNest's compliance.
- **International transfers (Issue 12).** The transfer mechanism is a placeholder with no instrument attached; the arrangement cannot be assessed as drafted.
- **Liability cap (Issue 14).** A three-month, fee-based cap shared with the main agreement may be inadequate for data-breach exposure.

**Medium severity — negotiate or flag for management decision**

- Role designation (Issue 1), vague processing scope (Issue 2), broad instruction carve-out (Issue 3), generic security language (Issue 6), thin data-subject-rights assistance (Issue 7), minimal breach-notification content (Issue 10), vague deletion terms with no certification (Issue 13), absence of an indemnity (Issue 15), governing-law mismatch (Issue 16), and the possible sectoral overlay (Issue 17).

**Low severity — minor drafting improvements**

- No standalone low-severity items were identified in this first pass; several Medium items include drafting clean-ups that can be raised together in negotiation.

### 5. Liability and Indemnity Note

The DPA's § 10.1 cap is fee-based and, by its own terms, is **part of and not additional to** the cap in the draft main hosting agreement. This means a data-breach loss would draw down the same shared cap that covers ordinary service failures, rather than having a dedicated allocation. The DPA contains **no indemnity** for breaches, regulatory fines, or third-party claims. The draft main agreement's indemnity language has not been reconciled with the DPA, and the two documents specify different governing law (Issue 16). The combined effect is that, as drafted, Lumen may bear a substantial share of breach-related costs. `[ATTORNEY TO CONFIRM: whether a data-breach carve-out, a separate sub-cap, or a processor indemnity should be sought, and how the DPA and main agreement liability regimes should interlock.]`

### 6. Attorney Verification Items

- [ ] Confirm Lumen's role as controller and DataNest's as processor under the governing privacy regime; the document's labels are not conclusive.
- [ ] Confirm the applicable privacy framework(s) and assess the DPA against their requirements `[verify jurisdiction]`.
- [ ] Review the possible sectoral overlay for self-reported health data and revisit affected DPA terms `[CONFIRM: possible sectoral overlay — specialist review recommended]`.
- [ ] Verify any breach-notification timeframe against current requirements — no deadline has been computed or assumed in this review.
- [ ] Confirm the cross-border transfer mechanism once identified, and that the instrument is current and valid.
- [ ] Review and approve the sub-processor list once provided.
- [ ] Assess the security measures against applicable minimums and Lumen's risk tolerance.
- [ ] Assess the § 10.1 liability cap against potential breach exposure and regulatory fine risk.
- [ ] Reconcile the DPA with the draft main hosting agreement, including the governing-law mismatch.
- [ ] Resolve every `[CONFIRM: ...]` placeholder in the table and issue list before this review is relied upon.
- [ ] Confirm all High-severity ratings remain High unless an attorney documents a downgrade rationale, name, and date.

### 7. Assumptions

- **Role.** This review assumes Lumen acts as controller and DataNest as processor, as the DPA labels them; this is flagged for attorney confirmation `[CONFIRM: client role]`.
- **Document completeness.** This review assumes DataNest DPA v4.2 dated March 9, 2026 is the complete, current version and that no annex, schedule, or sub-processor list exists beyond what was provided.
- **Main agreement.** This review assumes the draft DataNest Hosting Services Agreement provided is the version that will be executed alongside the DPA.
- **Applicable law.** This review does not assume which privacy regime or sector-specific regime applies; those are attorney-verification items `[verify jurisdiction]`.
- **Processing context.** This review assumes the hosted data includes account data, self-reported health and symptom logs, and device usage data, as described by the Lumen privacy team.
