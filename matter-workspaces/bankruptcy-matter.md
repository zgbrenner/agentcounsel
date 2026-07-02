> **Blank template — contains no client facts.** Once populated with matter-specific information this file becomes **draft legal work product for attorney review**. It may be protected by the attorney-client privilege and/or the attorney work-product doctrine. Label and access-limit the populated copy accordingly. This is not legal advice.
>
> Privilege designation (populated copy): `[CONFIRM: attorney to designate — e.g., Privileged & Confidential — Attorney Work Product]`

---

# Bankruptcy / Restructuring Matter Workspace

## Matter Header

| Field | Value |
|---|---|
| Matter Name | `[CONFIRM: matter name]` |
| Matter / File # | `[CONFIRM: matter number]` |
| Client | `[CONFIRM: client full legal name and entity type]` |
| Client Role | `[CONFIRM: debtor / debtor-in-possession / creditor (secured or unsecured) / committee member or committee counsel / lessor or contract counterparty / purchaser / other party in interest]` |
| Responsible Attorney | `[CONFIRM: attorney name and bar admission]` |
| Practice Profile in Use | `[CONFIRM: e.g., bankruptcy-restructuring]` |
| Date Opened | `[CONFIRM: date]` |
| Status | `[CONFIRM: e.g., Active — Pre-Filing / Active — Case Pending / Active — Plan Process / Closed]` |
| Conflicts Check Status | `[ACTION: conflicts check not yet run — matter gated; do not proceed]` |
| Bar-Date Register Status | `[ACTION: attorney must verify every entry in Section 5 before any reliance — see warning there]` |

---

## 1. Parties

| Party Name | Entity Type | Role | Aliases / Related Entities | Counsel (if known) |
|---|---|---|---|---|
| `[CONFIRM: client name]` | `[CONFIRM: e.g., corporation, individual]` | Client / `[CONFIRM: role from Matter Header]` | `[CONFIRM: trade names, affiliates]` | Responsible attorney above |
| `[CONFIRM: debtor name — if client is not the debtor]` | `[CONFIRM: entity type]` | Debtor / Debtor-in-Possession | `[CONFIRM: jointly administered affiliates, if any — as stated in filings]` | `[CONFIRM: debtor's counsel, if known]` |
| `[CONFIRM: trustee — if one has been appointed, per filings]` | `[CONFIRM]` | Trustee | — | `[CONFIRM: if known]` |
| `[CONFIRM: committee(s) — if formed, per filings]` | Committee | `[CONFIRM: e.g., unsecured creditors' committee]` | — | `[CONFIRM: committee counsel, if known]` |
| `[CONFIRM: other key parties — lenders, purchasers, major counterparties]` | | | | |

_Source of party information: `[CONFIRM: petition, docket, notices received, client instructions — identify the source]`_

---

## 2. Case Posture

> Record the case status exactly as user-supplied or as stated in a source document. Do not characterize whether a filing, conversion, or dismissal is likely or appropriate — that is attorney analysis.

| Field | Value |
|---|---|
| Case Filed? | `[CONFIRM: Y / N / Anticipated — per user or source document]` |
| Chapter / Proceeding Type | `[CONFIRM: as user-supplied or stated in the petition — e.g., chapter number, out-of-court workout, receivership; do not infer]` |
| Court | `[CONFIRM: court name and case number, if filed]` |
| Petition Date | `[CONFIRM: date as stated in filings]` [deadline verification required] |
| Voluntary / Involuntary | `[CONFIRM: as stated in filings]` |
| Jointly Administered? | `[CONFIRM: Y / N — lead case number if Y, per filings]` |
| Trustee / Examiner Appointed? | `[CONFIRM: Y / N / Unknown — per filings]` |
| First-Day / Key Orders Entered | `[CONFIRM: list orders as provided — reference Documents Index]` |
| Case Stage | `[CONFIRM: e.g., first days, claims process, sale process, plan and disclosure statement, confirmation, post-confirmation — as user-supplied]` |

---

## 3. Key Facts and Background

> Record only facts provided by the client or established by a source document. Label each fact with its source. Do not blend assumptions or inferences into this section.

| # | Fact | Source | Date of Fact | Confirmed? |
|---|---|---|---|---|
| 1 | `[CONFIRM: describe fact — e.g., nature of the client's claim, contract, or interest]` | `[CONFIRM: source document or client statement]` | `[CONFIRM: date]` | `[CONFIRM]` |
| 2 | | | | |
| 3 | | | | |

**Assumptions (not confirmed facts):**

| # | Assumption | Effect on Analysis if Wrong |
|---|---|---|
| 1 | `[CONFIRM: describe assumption]` | `[CONFIRM: describe effect]` |
| 2 | | |

---

## 4. Jurisdiction, Governing Law, and Procedural Posture

> Required by `core/jurisdiction-and-deadline-gates.md` — Gate 1. Complete before substantive analysis.

| Field | Value |
|---|---|
| Jurisdiction | `[CONFIRM: country, district/state — court identified in Section 2 if filed]` |
| Governing Law (underlying claims/contracts) | `[CONFIRM: law governing the client's underlying contracts or claims — may differ from the forum]` |
| Procedural Posture | `[CONFIRM: e.g., pre-filing planning, case pending, contested matter, adversary proceeding, appeal]` |
| Client Posture | `[CONFIRM: e.g., debtor preparing for filing / creditor asserting a claim / counterparty responding to assumption or rejection / target of an avoidance demand]` |
| Analysis "As Of" Date | `[CONFIRM: date of this workspace entry]` |
| Related Proceedings | `[CONFIRM: adversary proceedings, appeals, state-court actions — as provided]` |
| Open Jurisdiction / Venue Issues | `[CONFIRM: describe any unresolved issues]` |

---

## 5. Bar Dates and Critical Deadlines Register

> **Gate 2 — Required by `core/jurisdiction-and-deadline-gates.md`. This is the most consequence-bearing section of this workspace.**
>
> **[CRITICAL — ATTORNEY TO VERIFY ALL DEADLINES] Bankruptcy deadlines — bar dates, objection deadlines, assumption/rejection deadlines, challenge periods, appeal periods — are often short, non-extendable, and claim- or right-extinguishing if missed. No date in this register has been computed, inferred, or verified by any agent or tool. Every entry is user-supplied or transcribed from a cited source document. Verification of every deadline in this register is always an attorney task and must happen before any reliance.**

| # | Date | Event / Deadline | Source of Date | Applies to Client? | Verification Status |
|---|---|---|---|---|---|
| 1 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., general claims bar date]` | `[CONFIRM: e.g., bar date order, notice received]` | `[CONFIRM: attorney to assess]` | `[CONFIRM: attorney to verify]` |
| 2 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., governmental claims bar date — if applicable]` | `[CONFIRM: source]` | `[CONFIRM]` | `[CONFIRM: attorney to verify]` |
| 3 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., objection deadline for a pending motion]` | `[CONFIRM: e.g., motion, notice of hearing]` | `[CONFIRM]` | `[CONFIRM: attorney to verify]` |
| 4 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., sale objection / bid deadline]` | `[CONFIRM: e.g., bid procedures order]` | `[CONFIRM]` | `[CONFIRM: attorney to verify]` |
| 5 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., assumption/rejection-related deadline]` | `[CONFIRM: source]` | `[CONFIRM]` | `[CONFIRM: attorney to verify]` |
| 6 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., challenge-period deadline under a financing order]` | `[CONFIRM: e.g., cash collateral / DIP order]` | `[CONFIRM]` | `[CONFIRM: attorney to verify]` |
| 7 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., plan voting deadline / confirmation objection deadline]` | `[CONFIRM: e.g., disclosure statement order]` | `[CONFIRM]` | `[CONFIRM: attorney to verify]` |
| 8 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., hearing date]` | `[CONFIRM: source]` | `[CONFIRM]` | `[CONFIRM: attorney to verify]` |

_Skill for organizing user-supplied dates into a tracker: `skills/bankruptcy-restructuring/bankruptcy-deadline-tracker-intake/SKILL.md`. The tracker organizes dates; it never calculates one._

---

## 6. Automatic-Stay Touchpoints Log

> Log every planned, requested, or already-taken action that touches the debtor, the debtor's property, or collection of a claim. Do not conclude whether the stay applies to any action — flag each touchpoint for attorney evaluation before the action is taken or continued.

| # | Action / Touchpoint | Requested / Planned By | Status (Contemplated / Taken / Halted) | Date Logged | Attorney Evaluation Status |
|---|---|---|---|---|---|
| 1 | `[CONFIRM: e.g., sending an invoice or demand, setoff, terminating a contract, continuing pending litigation, repossession]` | `[CONFIRM: client contact or team member]` | `[CONFIRM]` | `[CONFIRM: date]` | `[ATTORNEY TO CONFIRM: stay applicability before this action proceeds]` |
| 2 | | | | | |
| 3 | | | | | |

**Stay relief:** motions for relief from stay filed or contemplated, by any party: `[CONFIRM: as provided — reference Documents Index]`

_Skill for mapping stay-risk facts: `skills/bankruptcy-restructuring/automatic-stay-issue-spotter/SKILL.md`._

---

## 7. Executory Contracts and Leases Inventory

> Inventory the contracts and leases between the client and the debtor (or, for a debtor-side matter, the debtor's key contracts) as provided. Do not conclude whether a contract is executory, assumable, assignable, or rejectable — those are attorney determinations.

| # | Contract / Lease | Counterparties | Status (per filings, if any) | Cure Amount (as asserted, by whom) | Notices Received / Sent | Attorney Review Status |
|---|---|---|---|---|---|---|
| 1 | `[CONFIRM: contract or lease description]` | `[CONFIRM]` | `[CONFIRM: e.g., no motion filed / assumption sought / rejection sought — as stated in filings]` | `[CONFIRM: amount and asserting party — never computed here]` | `[CONFIRM]` | `[ATTORNEY TO CONFIRM]` |
| 2 | | | | | | |
| 3 | | | | | | |

_Skill: `skills/bankruptcy-restructuring/executory-contract-assumption-rejection-checklist/SKILL.md`._

---

## 8. Claims Register

> Record claims as facts — amounts as asserted, scheduled, or filed, with the source for each. Do not conclude on validity, priority, secured status, or allowance.

| # | Claimant | Claim Basis | Amount (as asserted) | Scheduled? (per schedules) | Proof of Claim Filed? | Asserted Priority / Security (per source) | Source |
|---|---|---|---|---|---|---|---|
| 1 | `[CONFIRM: e.g., the client]` | `[CONFIRM: e.g., contract, invoices, lease]` | `[CONFIRM: amount as asserted — never computed here]` | `[CONFIRM: Y / N / Unknown — amount and characterization per schedules]` | `[CONFIRM: Y / N / Planned — claim number and date if filed]` [deadline verification required] | `[CONFIRM: as asserted in the filing — attorney to assess]` | `[CONFIRM]` |
| 2 | | | | | | | |

_Skills: `skills/bankruptcy-restructuring/creditor-claim-intake/SKILL.md`, `skills/bankruptcy-restructuring/proof-of-claim-checklist/SKILL.md`. The bar date for filing lives in Section 5._

---

## 9. DIP Financing / Cash Collateral Status

> Record the status of any debtor-in-possession financing or cash collateral use as stated in the filed documents. If not applicable, mark this section not applicable. Do not conclude on lien validity, perfection, priority, or adequacy of protection.

| Field | Value |
|---|---|
| Applicable? | `[CONFIRM: Y / N — if N, mark section not applicable]` |
| Facility / Order | `[CONFIRM: motion or order reference — interim / final, per docket]` |
| Lender(s) | `[CONFIRM: as stated in the documents]` |
| Budget in Effect | `[CONFIRM: reference and period — as filed]` |
| Milestones (as stated in the documents) | `[CONFIRM: list — each date also belongs in Section 5]` [deadline verification required] |
| Challenge Period (as stated) | `[CONFIRM: as stated in the order — deadline in Section 5]` [deadline verification required] |
| Client's Interest Affected | `[CONFIRM: e.g., liens primed, collateral used, carveout — as described in the documents; attorney to assess]` [ATTORNEY TO CONFIRM] |

_Skill: `skills/bankruptcy-restructuring/cash-collateral-dip-financing-issue-spotter/SKILL.md`._

---

## 10. Conflicts Check

| Field | Value |
|---|---|
| Gate Status | `[ACTION: conflicts check not yet run — matter gated; do not proceed]` |
| Party List Submitted for Check | `[CONFIRM: all party names and aliases — in bankruptcy, include the debtor, affiliates, committee members, and major creditors as appropriate]` |
| Check Run By | `[CONFIRM: name]` |
| Check Run Date | `[CONFIRM: date]` [deadline verification required] |
| Result | `[CONFIRM: cleared / potential conflict identified — see notes]` |
| Attorney Authorization to Proceed | `[CONFIRM: if potential conflict, documented written authorization required before any work]` |

---

## 11. Work-Product Index

> Index every draft deliverable produced by an AgentCounsel skill for this matter. Each entry is draft legal work product for attorney review.

| # | Skill Used | Date Run | Output Description | File / Location | Attorney Reviewer | Review Status |
|---|---|---|---|---|---|---|
| 1 | `skills/bankruptcy-restructuring/bankruptcy-matter-intake/SKILL.md` | `[CONFIRM: date]` | Matter intake summary | `[CONFIRM: file path or location]` | `[CONFIRM]` | `[CONFIRM: Draft / Under Review / Adopted / Superseded]` |
| 2 | `skills/bankruptcy-restructuring/bankruptcy-deadline-tracker-intake/SKILL.md` | `[CONFIRM: date]` | Draft deadline tracker (dates user-supplied, unverified) | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 3 | `skills/bankruptcy-restructuring/automatic-stay-issue-spotter/SKILL.md` | `[CONFIRM: date]` | Stay-risk fact map | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 4 | `skills/bankruptcy-restructuring/creditor-claim-intake/SKILL.md` | `[CONFIRM: date]` | Claim facts table | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 5 | `skills/bankruptcy-restructuring/proof-of-claim-checklist/SKILL.md` | `[CONFIRM: date]` | Proof-of-claim preparation checklist | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 6 | `skills/bankruptcy-restructuring/executory-contract-assumption-rejection-checklist/SKILL.md` | `[CONFIRM: date]` | Contract status and cure/default tracker | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 7 | `skills/bankruptcy-restructuring/plan-disclosure-statement-issue-spotter/SKILL.md` | `[CONFIRM: date]` | Plan / disclosure-statement issue list | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 8 | `skills/legal-research/legal-research-memo/SKILL.md` | `[CONFIRM: date]` | Research memo | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |

---

## 12. Risk and Issue Summary

> This summary is draft legal work product based solely on information recorded in this workspace. It is not a legal conclusion and is not final. The responsible attorney must review, correct, and adopt any risk characterization before it is relied upon.

| # | Issue / Risk | Category | Preliminary Assessment | Priority | Attorney Confirmation Status |
|---|---|---|---|---|---|
| 1 | `[CONFIRM: describe issue]` | `[CONFIRM: e.g., Bar Date, Stay, Contract, Claim Treatment, Financing]` | `[CONFIRM: preliminary notes — not a legal conclusion]` | `[CONFIRM: High / Medium / Low]` | `[ATTORNEY TO CONFIRM]` |
| 2 | | | | | |

**Preliminary Risk Band:** `[CONFIRM: Low / Medium / High]` `[ATTORNEY TO CONFIRM: preliminary triage only — not a legal conclusion]`

---

## 13. Open Items and Action Items

| # | Item | Type | Owner | Due Date | Status |
|---|---|---|---|---|---|
| 1 | Run conflicts check | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 2 | Verify every entry in the bar-date and deadlines register (Section 5) | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 3 | Evaluate every automatic-stay touchpoint before action (Section 6) | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 4 | Confirm claim filing plan against the verified bar date | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 5 | `[CONFIRM: additional action item]` | | `[CONFIRM]` | `[CONFIRM]` [deadline verification required] | Open |

---

## 14. Attorney Sign-Off

> The responsible attorney must review this workspace, resolve all `[CONFIRM: ...]` and `[ACTION: ...]` placeholders, and sign off before this workspace is relied upon or shared.

- [ ] Client identity and role confirmed; conflicts check run and gate status confirmed.
- [ ] Case posture (Section 2) confirmed against the docket — chapter/proceeding type, case number, petition date, and appointments.
- [ ] Every date in the bar-date and deadlines register (Section 5) independently verified by attorney — none computed or inferred; non-extendable deadlines identified.
- [ ] Every automatic-stay touchpoint (Section 6) evaluated before the action was taken or continued.
- [ ] Executory contract and lease inventory reviewed; no assumption, rejection, or termination step taken without attorney direction.
- [ ] Claims register reviewed; any proof of claim reviewed by attorney before filing.
- [ ] DIP / cash-collateral milestones and challenge periods carried into Section 5 and verified.
- [ ] Jurisdiction, governing law, and posture confirmed.
- [ ] All `[CONFIRM: ...]` and `[ACTION: ...]` placeholders in this workspace resolved.
- [ ] Work-product index (Section 11) reflects all drafts produced; each draft reviewed and adopted or superseded by attorney.
- [ ] Risk and issue summary (Section 12) reviewed and confirmed or revised by responsible attorney.
- [ ] Privilege and confidentiality of this workspace protected; distribution limited to authorized personnel.
- [ ] No client-sensitive facts appear in any reusable copy of the blank template.

| Field | Value |
|---|---|
| Responsible Attorney | `[CONFIRM: name and bar admission]` |
| Sign-Off Date | `[CONFIRM: date]` |
| Notes | |
