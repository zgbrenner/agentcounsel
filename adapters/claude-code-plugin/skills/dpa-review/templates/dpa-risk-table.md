> Draft legal work product for attorney review. Not legal advice. Do not paste client-sensitive facts, deal-specific details, or personal data into a reusable copy of this template. Complete a fresh copy for each matter.

# DPA Risk Table

## Matter Header

| Field | Value |
|---|---|
| Matter / Project | `[ENTER MATTER NAME OR REFERENCE]` |
| Document Reviewed | `[ENTER DOCUMENT TITLE, VERSION, AND DATE]` |
| Counterparty | `[ENTER COUNTERPARTY NAME]` |
| Client Role | `[CONFIRM: controller / processor / sub-processor — confirm under applicable law]` |
| Reviewer | `[ENTER REVIEWER NAME]` |
| Review Date | `[ENTER DATE]` |
| Applicable Framework(s) | `[CONFIRM: framework(s) stated in document or identified by counsel — do not assume]` |
| Main Agreement Referenced | `[ENTER YES / NO / UNKNOWN — and document title if known]` |

---

## Severity Key

| Severity | Meaning |
|---|---|
| **High** | Material legal or financial risk; requires redline, escalation, or walkaway analysis before execution. |
| **Med** | Meaningful risk or gap; negotiate or flag for management decision. |
| **Low** | Minor drafting improvement, missing boilerplate, or low-impact issue; address if opportunity permits. |

---

## Risk Table

| # | Topic | Section / Clause | What It Says (Plain Language) | Risk to Client | Severity | Suggested Change | Attorney Note |
|---|---|---|---|---|---|---|---|
| 1 | **Party Role Designation** | `[§ —]` | How the DPA labels each party (controller, processor, sub-processor). | Role labels in the document may not reflect the actual legal relationship under applicable law. An incorrect designation can misallocate compliance obligations. | `[H/M/L]` | Confirm roles with counsel before signing. Add recital confirming the factual basis for the designation. | `[CONFIRM: verify role under applicable framework]` |
| 2 | **Scope and Nature of Processing** | `[§ —]` | Description of the categories of personal data, data subjects, processing purposes, and operations. | Vague or overbroad scope may authorize processing beyond what the controller intends. Underspecified scope may create gaps. | `[H/M/L]` | Narrow to specific data categories, subject groups, and purposes. Attach a detailed processing schedule. | `[CONFIRM: scope matches actual processing activity]` |
| 3 | **Processing Instructions** | `[§ —]` | Whether the processor is limited to documented controller instructions and what carve-outs exist. | Broad processor discretion or wide legal-obligation carve-outs may allow processing beyond instructions. | `[H/M/L]` | Tighten carve-outs; require written instructions for any non-standard processing. | |
| 4 | **Sub-Processor Authorization** | `[§ —]` | Whether sub-processor use requires prior written approval or general authorization, and the notice/objection mechanism. | General authorization without notice and objection rights limits the controller's visibility and control. | `[H/M/L]` | Require prior written approval or meaningful notice-and-objection right; maintain updated sub-processor list. | |
| 5 | **Sub-Processor Obligations** | `[§ —]` | Whether the processor must impose equivalent data protection obligations on sub-processors. | Weak flow-down obligations mean the controller may remain liable for sub-processor failures. | `[H/M/L]` | Require equivalent obligations and right to audit sub-processors; processor remains liable for sub-processor acts. | |
| 6 | **Security Measures** | `[§ —]` | What technical and organizational security measures are specified or referenced. | General or aspirational security language provides weak contractual protection; no measurable baseline. | `[H/M/L]` | Reference specific standard (e.g., ISO 27001, SOC 2 Type II) or attach minimum measures schedule. | |
| 7 | **Data Subject Rights Assistance** | `[§ —]` | Whether and how the processor assists the controller in responding to data subject requests. | Absent or vague assistance obligations shift burden to controller and may impair timely response. | `[H/M/L]` | Specify scope of assistance, response timeframe, and cost allocation. | `[CONFIRM: verify assistance requirements under applicable law]` |
| 8 | **Breach Notification — Trigger** | `[§ —]` | What event triggers the processor's notification obligation (e.g., confirmed breach, reasonable belief, suspicion). | A narrow trigger (e.g., only "confirmed" breaches) may delay notification beyond regulatory requirements. | `[H/M/L]` | Align trigger with applicable legal standard; use "becomes aware" or "reasonably suspects." | `[CONFIRM: verify trigger standard under applicable law]` |
| 9 | **Breach Notification — Timeframe** | `[§ —]` | The period within which the processor must notify the controller after a breach. | `[CONFIRM: do not assume or compute. Verify stated timeframe against applicable regulatory deadline.]` | `[H/M/L]` | State timeframe explicitly; confirm it allows the controller to meet its own regulatory notification deadline. | `[CONFIRM: verify deadline under applicable law — never compute from model knowledge]` |
| 10 | **Breach Notification — Content** | `[§ —]` | What information the processor must include in a breach notification. | Insufficient required content forces follow-up exchanges and may delay controller's regulatory reporting. | `[H/M/L]` | Specify minimum content (nature, categories, approximate number of affected individuals, likely consequences, measures taken). | |
| 11 | **Audit Rights** | `[§ —]` | Whether the controller may audit the processor, how audits are triggered, and what substitutes (e.g., third-party reports) are accepted. | Restricted audit rights limit the controller's ability to verify compliance; audit-report-only substitutes may be stale. | `[H/M/L]` | Preserve right to conduct or commission direct audits with reasonable notice; limit cost-shifting. | |
| 12 | **Cross-Border Transfer Mechanism** | `[§ —]` | How the DPA addresses international transfers of personal data (e.g., SCCs, BCRs, adequacy, other). | Absence of a mechanism, or reliance on a mechanism of uncertain validity, may render the transfer unlawful. | `[H/M/L]` | Confirm mechanism is current and valid under applicable law; attach SCCs or other instrument as needed. | `[CONFIRM: validity of transfer mechanism under applicable framework]` |
| 13 | **Deletion and Return on Termination** | `[§ —]` | What the processor must do with personal data after termination or expiration — return, delete, or certify destruction, and within what period. | Absence or vagueness allows the processor to retain data indefinitely. Lack of certification leaves controller without evidence of compliance. | `[H/M/L]` | Specify return/deletion obligation, timeframe, certification requirement, and permitted retention exceptions. | |
| 14 | **Liability Cap** | `[§ —]` | The cap on the processor's liability under the DPA, and how it relates to the main agreement's cap. | A low DPA-specific cap may provide inadequate protection for breach-related losses; cap may be subsumed into (or exclude) the main agreement cap. | `[H/M/L]` | Confirm relationship to main agreement; consider carve-out for data breach liability. | `[CONFIRM: adequacy of cap under client's risk profile]` |
| 15 | **Indemnity** | `[§ —]` | Whether the DPA contains an indemnity from the processor for data breaches, regulatory fines, or third-party claims. | Absence of indemnity or broad exclusions may leave client bearing costs caused by processor failure. | `[H/M/L]` | Seek processor indemnity for breaches caused by processor's acts or omissions; confirm regulatory fine allocation. | |
| 16 | **Governing Law and Disputes** | `[§ —]` | The governing law and dispute resolution mechanism specified in the DPA (may differ from main agreement). | Conflicting governing law provisions between DPA and main agreement create enforcement uncertainty. | `[H/M/L]` | Align with main agreement or provide clear hierarchy; confirm governing law is appropriate. | `[CONFIRM: confirm governing law is appropriate and consistent with main agreement]` |
| 17 | **[Additional Issue]** | `[§ —]` | `[Describe]` | `[Describe risk]` | `[H/M/L]` | `[Describe]` | |

---

## Open Items for Attorney Verification

- [ ] Client role (controller / processor / sub-processor) confirmed under applicable law.
- [ ] Applicable privacy framework(s) confirmed; DPA assessed against its requirements.
- [ ] All breach notification timeframes verified against current regulatory deadlines — no deadline has been computed or assumed in this review.
- [ ] Cross-border transfer mechanism confirmed as valid and current.
- [ ] Sub-processor list reviewed and approved if required.
- [ ] Security measures assessed against applicable legal minimums and client risk tolerance.
- [ ] DPA liability cap assessed against potential breach exposure and regulatory fine risk.
- [ ] DPA provisions confirmed to be consistent with the main commercial agreement; conflicts resolved.
- [ ] All `[CONFIRM: ...]` items in the table above have been resolved.
- [ ] No provisions have been characterized in this table without reference to the actual document text.
- [ ] `[Add matter-specific open items here]`
