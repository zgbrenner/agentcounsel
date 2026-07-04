# Example: Termination Risk

> **Illustrative example — not legal advice.** This is a sample of what the Termination Risk skill (`skills/employment/termination-risk/SKILL.md`) produces. Every party, person, date, and fact in it is **fictional** and was invented for illustration. It organizes and flags risk factors; it does **not** decide whether any termination is lawful. It is the kind of draft work product a supervising attorney would review — not a finished deliverable, and not legal advice. See `examples/README.md`.

## Scenario

Northwind Systems, Inc. is a fictional ~200-person enterprise-software company. A regional sales director wants to terminate a **Senior Account Manager (referred to here as "Employee A")** for performance — two consecutive quarters below quota — and has asked the people team to think through the risk before scheduling a separation meeting. The facts are a deliberate mix of clean and complicated: there is a written performance-improvement plan (PIP) and documented quota misses (clean), but the PIP was opened only after Employee A requested intermittent medical leave and filed an internal complaint against a different manager, and the proposed termination date falls shortly before an equity-vesting tranche (risk-flagged). Employee A has about four years' tenure. Employment is described as at-will, though the employee handbook contains progressive-discipline language. This example shows the draft fact-and-risk organization the skill produces for the reviewing attorney. It states **no** conclusion about whether the termination is lawful — it organizes the factors and questions so an attorney can.

## Illustrative Output

> **Draft legal work product for attorney review. Not legal advice.** This document organizes facts and flags risk factors for attorney assessment. It does not conclude whether the proposed termination is lawful, and it computes no deadline. Every risk factor below is *identified for attorney review*, not a legal determination.

### 1. Fact Summary

Organized by input category; all facts are user-provided unless labeled otherwise.

- **Employee identifier:** Senior Account Manager, Enterprise Sales (Employee A). Anonymized; real name withheld from this working document.
- **Employment status:** Described by the business as at-will. `[CONFIRM: employment status — the employee handbook contains progressive-discipline language that may raise an implied-contract question. Attorney to review handbook and offer letter.]`
- **Tenure and role:** Approximately 4 years; Senior Account Manager reporting to the Regional Sales Director.
- **Stated reason for termination (as the employer intends to assert it):** "Sustained failure to meet sales quota for two consecutive quarters (Q-minus-2 and Q-minus-1) despite a performance improvement plan."
- **Documentation history (user-provided):**
  - Quarterly attainment reports showing Employee A at roughly 68% and 74% of quota for the two quarters at issue.
  - A written PIP dated approximately six weeks ago, with a 60-day cure period still running.
  - Two prior informal coaching emails from the manager.
- **Protected activity / leave in the record (user-provided):**
  - Approximately seven weeks ago, Employee A submitted a request for **intermittent medical leave** `[CONFIRM: leave type and applicable law — route leave-specific analysis to protected-leave-review]`.
  - Approximately six weeks ago, Employee A filed an **internal complaint** alleging inappropriate conduct by a *different* manager (not the Regional Sales Director proposing the termination).
- **Timing (user-provided):** The proposed termination date falls roughly two weeks before a scheduled **equity-vesting tranche** for Employee A.
- **Comparators (user-provided):** Another Senior Account Manager on the same team reportedly finished one of the two quarters below quota and was **not** placed on a PIP `[CONFIRM: comparator facts, quota figures, and whether circumstances were similar].`

### 2. Risk Factor Summary

Each item below is **identified for attorney review**, not a legal conclusion. Proximity, sequence, and significance are legal questions reserved for counsel.

- **PIP-as-pretext pattern (identified for attorney review).** The PIP was opened *after* — and in close temporal proximity to — both the intermittent-leave request and the internal complaint. A PIP initiated or accelerated shortly after protected activity is a recognized discrimination/retaliation-claim trigger. The chronological proximity is flagged; its legal significance is for the attorney to assess. Route the leave-specific interference/retaliation analysis to `protected-leave-review`.
- **Recent protected leave request (identified for attorney review).** The intermittent-leave request precedes the proposed termination. Whether any leave-related interference or retaliation exposure exists is a leave-specific analysis, flagged for `protected-leave-review` and counsel.
- **Pending internal complaint (identified for attorney review).** Employee A has an open internal complaint. Terminating a complainant while the complaint is pending raises a retaliation-timing question for attorney assessment. The complaint targets a different manager, which the attorney may weigh — but the proximity is flagged regardless.
- **Timing near an equity-vesting tranche (identified for attorney review).** The proposed date falls shortly before a vesting event. Timing relative to benefit vesting is flagged for counsel; no forfeiture or vesting determination is made here `[CONFIRM: equity plan terms and forfeiture-on-termination provisions].`
- **Comparator inconsistency (identified for attorney review).** A peer reportedly missed quota without being placed on a PIP. Whether that peer is a similarly situated comparator, and whether the difference in treatment is significant, is for the attorney to assess.
- **Employment-status / implied-contract question (identified for attorney review).** Handbook progressive-discipline language may bear on the at-will characterization `[CONFIRM].`

### 3. Termination Risk Checklist

*Completed instance of `templates/termination-risk-checklist.md`. Boxes are marked from the facts provided; every unresolved legal or factual point is flagged for counsel. `[x]` = confirmed present in the record; `[ ]` = not established or not confirmed.*

#### Matter Header

| Field | Value |
|---|---|
| Matter / File Reference | Northwind Systems, Inc. — Employee A separation review (no matter number assigned) |
| Employee Identifier | Senior Account Manager, Enterprise Sales (Employee A) — real name withheld |
| Prepared by | Drafting agent, for assigned employment counsel |
| Review date | `[CONFIRM: date of preparation]` |
| Jurisdiction | `[CONFIRM: governing state/province/country]` |
| Employment status | `[CONFIRM: at-will / fixed-term / CBA — handbook progressive-discipline language noted]` |
| Stated reason for termination | Sustained quota failure across two consecutive quarters despite a PIP |

#### Section 1 — Documentation & Performance History

- [x] Written performance improvement plan (PIP) in file — dated ~6 weeks ago; 60-day cure period still running
- [x] Written warnings issued and documented — two prior coaching emails
- [x] Contemporaneous performance reviews support stated reason — quarterly attainment reports (68%, 74%)
- [ ] Investigation report completed and signed (if misconduct basis) — N/A; performance basis, not misconduct
- [x] Documentation is consistent with stated reason for termination
- [ ] **Documentation predates any known protected activity or complaint** — **No.** The PIP post-dates both the leave request and the complaint. Flag for attorney.
- [ ] No gaps between documented concerns and proposed termination date `[CONFIRM]`
- [x] HR and manager communications reviewed for consistency — reviewed; see PIP-as-pretext flag

**Notes:** PIP timing relative to protected activity is the central documentation concern — see Section 2 and the risk table.

#### Section 2 — Protected Activity & Leave

- [ ] Employee has not recently filed or supported a discrimination or harassment complaint — **filed an internal complaint ~6 weeks ago**
- [ ] Employee is not currently on or recently returned from protected leave — **requested intermittent medical leave ~7 weeks ago** `[CONFIRM: leave type and applicable law]`
- [x] Employee has not recently filed a workers' compensation claim — none in record
- [x] Employee has not engaged in recent whistleblower activity or internal reporting — none in record beyond the complaint noted above
- [x] Employee has not recently exercised union or collective rights — none in record
- [ ] Employee has not recently requested a disability accommodation `[CONFIRM: whether the leave request implicates an accommodation analysis]`
- [ ] Timeline between any protected activity and the termination date has been reviewed `[CONFIRM: with counsel]`

**Notes:** Both the leave request and the complaint precede the PIP and the proposed termination. Proximity flagged; legal significance is for the attorney. **Route to `protected-leave-review` for the leave-specific interference/retaliation analysis.**

#### Section 3 — Protected Characteristics & Comparators

- [ ] Protected characteristics of the affected employee have been identified and flagged for attorney review `[CONFIRM: none recorded in this working document; attorney to assess]`
- [x] Comparator employees in similar roles with similar conduct have been identified — one peer Senior Account Manager
- [ ] Comparator employees were treated consistently with the affected employee — **peer reportedly not placed on a PIP after a below-quota quarter**
- [ ] No pattern of disparate treatment is apparent in the documented record `[CONFIRM]`
- [ ] If a reduction in force: demographics of the affected group flagged for statistical review — N/A; individual separation

**Identified characteristics to flag for attorney review:** `[CONFIRM: not assessed here — attorney to review]`

**Comparator notes:** Peer's quota figures, timing, and circumstances need confirmation before any similarly-situated assessment `[CONFIRM].`

#### Section 4 — Timing Factors

- [ ] Termination does not coincide with a benefit vesting event — **falls ~2 weeks before an equity-vesting tranche** `[CONFIRM]`
- [ ] Termination does not fall within a protected leave period `[CONFIRM: leave status on the proposed date]`
- [ ] Termination does not immediately follow a complaint, report, or protected activity — **follows a complaint and a leave request**
- [ ] Termination does not fall during or immediately after a medical certification or accommodation process `[CONFIRM]`
- [ ] Any contractual notice period or end-of-term date has been identified `[CONFIRM]`
- [ ] WARN Act or equivalent advance-notice obligations assessed — N/A on current facts (single separation) `[CONFIRM: with counsel]`

**Notes:** Two timing concerns stack — proximity to protected activity and proximity to vesting. Both flagged for counsel. No deadline computed `[deadline verification required]`.

#### Section 5 — Process & Notice

- [ ] Employer followed its own disciplinary or termination procedure `[CONFIRM: handbook progressive-discipline steps completed]`
- [ ] Required internal approvals obtained (HR, legal, senior management) `[CONFIRM]`
- [x] Investigation completed before termination — N/A (performance basis)
- [ ] Employee given opportunity to respond `[CONFIRM: PIP cure period still running]`
- [ ] Termination meeting participants identified and documented `[CONFIRM]`
- [ ] Termination letter reviewed before delivery `[CONFIRM: with counsel]`

**Notes:** The PIP cure period appears not yet to have expired — terminating mid-cure-period is flagged for attorney review against the handbook and the stated reason.

#### Section 6 — Final Pay & Benefits

> All items require attorney and/or payroll confirmation; requirements vary by jurisdiction and agreement.

- [ ] Final paycheck timing requirements confirmed `[CONFIRM: jurisdiction-specific]`
- [ ] Accrued, unused vacation or PTO payout obligation confirmed `[CONFIRM: jurisdiction-specific]`
- [ ] Expense reimbursement obligations reviewed `[CONFIRM]`
- [ ] Equity, commission, or bonus proration obligations confirmed `[CONFIRM: equity vesting tranche and any in-flight commissions]`
- [ ] Benefits continuation (COBRA or equivalent) notice obligations confirmed `[CONFIRM]`
- [ ] Company property return process in place `[CONFIRM]`

**Notes:** Equity proration interacts with the vesting-timing flag — confirm plan terms with counsel and payroll.

#### Section 7 — Severance & Release

- [ ] Severance is / is not being offered `[CONFIRM: business decision pending]`
- [ ] Consideration offered has been identified and confirmed as adequate `[CONFIRM: with counsel]`
- [ ] Claims to be released are specified in the agreement `[CONFIRM]`
- [ ] Release does not purport to waive non-waivable claims `[CONFIRM: with counsel]`
- [ ] Consideration period provided to employee `[CONFIRM: applicable period under governing law]`
- [ ] Revocation period provided (if applicable) `[CONFIRM: with counsel]`
- [ ] OWBPA or equivalent requirements reviewed if employee is age 40 or older `[CONFIRM: age not recorded here — attorney to assess]`
- [ ] Non-compete, non-solicit, and non-disparagement clauses reviewed `[CONFIRM: enforceability in jurisdiction]`
- [ ] Cooperation clause reviewed for scope and duration `[CONFIRM]`

**Notes:** If severance and a release are contemplated given the flagged risks, all periods and waivable-claim limits are attorney items. No statutory timeframe is asserted here.

#### Section 8 — Communications Plan

- [ ] Internal announcement language drafted and reviewed `[CONFIRM]`
- [ ] Reference policy confirmed and applied consistently `[CONFIRM]`
- [ ] Reason given externally is consistent with stated internal reason `[CONFIRM]`
- [ ] Social media and public communications plan reviewed `[CONFIRM]`
- [ ] No statements made that could create admission or defamation risk `[CONFIRM: with counsel]`

**Notes:** Given the pending complaint, external messaging about the reason for departure carries evidentiary risk — flagged for counsel.

#### Risk Factor Table

| Risk Factor | Present? | Severity | Notes | Attorney Note |
|---|---|---|---|---|
| Recent protected activity or complaint | [x] Yes | High | Internal complaint filed ~6 weeks ago | Assess retaliation-timing exposure |
| Currently on or recently returned from protected leave | [x] Yes | High | Intermittent-leave request ~7 weeks ago | Route to `protected-leave-review` |
| Timing proximity to vesting event | [x] Yes | High | ~2 weeks before equity tranche | Review plan and forfeiture terms |
| Documentation gaps or inconsistencies | [x] Yes | High | PIP post-dates protected activity | PIP-as-pretext review |
| Known protected characteristic — disparate treatment risk | [ ] Unknown | `[CONFIRM]` | Not assessed here | Attorney to assess |
| Comparator inconsistency identified | [x] Yes | Medium | Peer not PIP'd after below-quota quarter | Confirm similarly-situated status |
| Procedural deviation from employer policy | [ ] Unknown | Medium | Termination mid-PIP-cure-period | Review handbook procedure |
| Contract or CBA obligation unresolved | [ ] Unknown | `[CONFIRM]` | Handbook implied-contract question | Review handbook / offer letter |
| WARN Act or notice-period obligation flagged | [ ] No | Low | Single separation | Confirm no aggregation issue |
| Final pay or benefits obligation unresolved | [ ] Unknown | `[CONFIRM]` | Jurisdiction-specific | Confirm with payroll/counsel |
| Severance/release adequacy unconfirmed | [ ] Unknown | `[CONFIRM]` | Severance decision pending | Confirm with counsel |
| Communications risk identified | [x] Yes | Medium | Pending complaint raises messaging risk | Review external messaging |

### 4. Open Items for Attorney Verification

1. `[CONFIRM: employment status and applicable governing documents — resolve the handbook progressive-discipline / implied-contract question.]`
2. `[CONFIRM: jurisdiction and jurisdiction-specific final pay, notice, and any WARN-equivalent requirements — verify jurisdiction.]`
3. `[CONFIRM: retaliation-timing exposure given the sequence of leave request, internal complaint, PIP, and proposed termination date — no legal significance concluded here.]`
4. `[CONFIRM: leave-specific interference/retaliation analysis via protected-leave-review.]`
5. `[CONFIRM: comparator facts and whether the peer is similarly situated.]`
6. `[CONFIRM: equity plan vesting and forfeiture terms relative to the proposed termination date; no vesting or forfeiture determination made here.]`
7. `[CONFIRM: whether terminating during the running PIP cure period deviates from employer procedure.]`
8. `[CONFIRM: protected characteristics of Employee A and any comparators — not assessed in this working document.]`
9. `[deadline verification required]` for any period referenced above; no deadline has been computed.

### 5. Assumptions

- Assumed the quarterly attainment reports, PIP, and coaching emails provided are complete and authentic; not independently verified.
- Assumed "at-will" as described by the business, subject to the flagged handbook question.
- Assumed the leave request is a protected-leave request pending confirmation of leave type and governing law `[CONFIRM]`.
- Assumed the internal complaint qualifies as protected activity for flagging purposes; legal significance reserved for counsel.
- Assumed the equity tranche and its date as provided by the business; plan terms not reviewed here.
- No assumption was made about jurisdiction, governing law, protected characteristics, or the lawfulness of the termination; each is flagged for attorney verification.

---

## Attorney Verification Checklist

- [ ] Employment status (at-will, contract, union) has been confirmed and governing documents reviewed.
- [ ] The stated business reason is accurate, consistent with prior communications, and supported by contemporaneous documentation.
- [ ] All documentation relied upon has been reviewed in its original form and confirmed to be complete.
- [ ] The timeline of protected activity, leave, and complaints has been reviewed for retaliation risk. If the employee is on, recently took, or recently returned from protected leave, the `protected-leave-review` skill has been used to complete the leave-specific interference and retaliation analysis.
- [ ] Protected characteristics of the affected employee and comparator employees have been assessed under applicable anti-discrimination law.
- [ ] Comparator analysis is complete: similarly situated employees with similar conduct have been identified and their treatment confirmed.
- [ ] Timing of termination relative to vesting events, investigations, leave, or complaints has been reviewed.
- [ ] All employer-required procedures (progressive discipline, investigation, approvals) have been followed or deviations documented.
- [ ] Any wage-and-hour concern surfaced during review — including exempt/non-exempt classification or back-pay exposure — has been routed to the `wage-hour-qa` skill and reviewed by counsel; no pay figures have been computed or relied upon from this document.
- [ ] Jurisdiction-specific final pay, notice, and WARN Act (or equivalent) requirements have been confirmed.
- [ ] Severance and release terms, including any required consideration and revocation periods, have been reviewed under applicable law.
- [ ] The communications plan and reference policy have been reviewed for evidentiary and reputational risk.
- [ ] PIP-as-pretext pattern has been considered: any PIP initiated or modified within temporal proximity to protected activity has been flagged for retaliation-risk review.
- [ ] If the employee is an executive or senior individual contributor: restrictive covenants, garden leave, equity-forfeiture-for-competition, and change-in-control provisions have all been reviewed; enforcement posture in the governing jurisdiction has been confirmed.
- [ ] No legal conclusions in this document have been relied upon without attorney review and confirmation.

---

*This example is illustrative and built on fictional facts. It demonstrates the structure and discipline of the Termination Risk skill; it is not legal advice and must not be used as a template for a real matter. Run the skill on your own inputs and have qualified employment counsel review the result.*
