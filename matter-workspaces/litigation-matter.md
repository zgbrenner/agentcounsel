> **Blank template — contains no client facts.** Once populated with matter-specific information this file becomes **draft legal work product for attorney review**. It may be protected by the attorney-client privilege and/or the attorney work-product doctrine. Label and access-limit the populated copy accordingly. This is not legal advice.
>
> Privilege designation (populated copy): `[CONFIRM: attorney to designate — e.g., Privileged & Confidential — Attorney Work Product]`

---

# Litigation Matter Workspace

## Matter Header

| Field | Value |
|---|---|
| Matter Name | `[CONFIRM: matter name]` |
| Matter / File # | `[CONFIRM: matter number]` |
| Client | `[CONFIRM: client full legal name and entity type]` |
| Responsible Attorney | `[CONFIRM: attorney name and bar admission]` |
| Practice Profile in Use | `[CONFIRM: e.g., litigation]` |
| Date Opened | `[CONFIRM: date]` |
| Status | `[CONFIRM: e.g., Active — Pre-Litigation / Active — Discovery / Closed]` |
| Conflicts Check Status | `[ACTION: conflicts check not yet run — matter gated; do not proceed]` |
| Litigation Hold Status | `[ACTION: attorney must evaluate preservation obligation before proceeding]` |

---

## 1. Parties

| Party Name | Entity Type | Role | Aliases / Related Entities | Counsel (if known) |
|---|---|---|---|---|
| `[CONFIRM: client name]` | `[CONFIRM: e.g., corporation, individual]` | Client / `[CONFIRM: plaintiff or defendant]` | `[CONFIRM: trade names, affiliates]` | Responsible attorney above |
| `[CONFIRM: opposing party]` | `[CONFIRM: entity type]` | `[CONFIRM: plaintiff or defendant]` | `[CONFIRM: aliases]` | `[CONFIRM: if known]` |
| `[CONFIRM: additional parties]` | | | | |

_Source of party information: `[CONFIRM: complaint, demand letter, client instructions — identify the source]`_

---

## 2. Key Facts and Background

> Record only facts provided by the client or established by a source document. Label each fact with its source. Do not blend assumptions or inferences into this section.

| # | Fact | Source | Date of Fact | Confirmed? |
|---|---|---|---|---|
| 1 | `[CONFIRM: describe fact]` | `[CONFIRM: source document or client statement]` | `[CONFIRM: date]` | `[CONFIRM]` |
| 2 | | | | |
| 3 | | | | |

**Assumptions (not confirmed facts):**

| # | Assumption | Effect on Analysis if Wrong |
|---|---|---|
| 1 | `[CONFIRM: describe assumption]` | `[CONFIRM: describe effect]` |
| 2 | | |

---

## 3. Claims and Causes of Action

| # | Claim / Cause of Action | Asserted By | Against | Status (Asserted / Anticipated) | Notes |
|---|---|---|---|---|---|
| 1 | `[CONFIRM: claim description]` | `[CONFIRM: party]` | `[CONFIRM: party]` | `[CONFIRM: Asserted / Anticipated]` | |
| 2 | | | | | |
| 3 | | | | | |

_Do not characterize the legal merit of any claim in this workspace. Merit analysis is attorney work product to be produced separately._

**Counterclaims / Cross-Claims:**

| # | Claim | Asserted By | Against | Status | Notes |
|---|---|---|---|---|---|
| 1 | `[CONFIRM]` | | | | |

---

## 4. Jurisdiction, Governing Law, and Procedural Posture

> Required by `core/jurisdiction-and-deadline-gates.md` — Gate 1. Complete before substantive analysis.

| Field | Value |
|---|---|
| Jurisdiction | `[CONFIRM: country, state/province, federal/state/foreign]` |
| Court / Forum | `[CONFIRM: court name, docket/case number if known]` |
| Governing Law | `[CONFIRM: law governing the claims — may differ from forum]` |
| Venue | `[CONFIRM: venue basis and any open challenges]` |
| Procedural Stage | `[CONFIRM: e.g., pre-litigation, complaint filed, answer due, discovery, dispositive motions, trial, appellate]` |
| Client Posture | `[CONFIRM: plaintiff / defendant / third-party defendant / cross-claimant / respondent]` |
| Analysis "As Of" Date | `[CONFIRM: date of this workspace entry]` |
| Open Jurisdiction / Venue Issues | `[CONFIRM: describe any unresolved issues]` |

---

## 5. Documents Index

| # | Document Name / Description | Date | Version | Location / Bates / File Path | Relevance | Produced to Opposing Party? | Privilege Claim? |
|---|---|---|---|---|---|---|---|
| 1 | `[CONFIRM: document name]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM: key fact / background / claim support]` | `[CONFIRM: Y / N / N-A]` | `[CONFIRM: Y / N — if Y, log separately]` |
| 2 | | | | | | | |
| 3 | | | | | | | |

_Skills that generate document-related work product: `skills/litigation/litigation-chronology/SKILL.md`, `skills/litigation/privilege-log-review/SKILL.md`_

---

## 6. Deadlines and Key Dates

> **Gate 2 — Required by `core/jurisdiction-and-deadline-gates.md`.** Every date in this table must be independently verified by the responsible attorney. No date in this table has been computed by any agent or tool. Do not rely on any date here without attorney confirmation.

| # | Date | Event / Deadline | Source of Date | Verification Status |
|---|---|---|---|---|
| 1 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., answer deadline]` | `[CONFIRM: e.g., complaint, service receipt, court order]` | `[CONFIRM: attorney to verify]` |
| 2 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., discovery cutoff]` | `[CONFIRM: source]` | `[CONFIRM: attorney to verify]` |
| 3 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., dispositive motion deadline]` | `[CONFIRM: source]` | `[CONFIRM: attorney to verify]` |
| 4 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., trial date]` | `[CONFIRM: source]` | `[CONFIRM: attorney to verify]` |
| 5 | `[CONFIRM: date — attorney to verify]` [deadline verification required] | `[CONFIRM: e.g., statute of limitations]` | `[CONFIRM: source]` | `[CONFIRM: attorney to verify]` |

**[CRITICAL — ATTORNEY TO VERIFY ALL DEADLINES]** Dates above reflect information provided at intake only. Jurisdiction-specific counting rules, holidays, triggering events, and exceptions have not been applied. The responsible attorney must independently verify every deadline before reliance.

---

## 7. Conflicts Check

| Field | Value |
|---|---|
| Gate Status | `[ACTION: conflicts check not yet run — matter gated; do not proceed]` |
| Party List Submitted for Check | `[CONFIRM: list all party names and aliases submitted]` |
| Check Run By | `[CONFIRM: name]` |
| Check Run Date | `[CONFIRM: date]` [deadline verification required] |
| Result | `[CONFIRM: cleared / potential conflict identified — see notes]` |
| Attorney Authorization to Proceed | `[CONFIRM: if potential conflict, documented written authorization required before any work]` |

_Reference: `skills/litigation/matter-intake/SKILL.md` — Step 9 (Conflicts Check Gate)._

---

## 8. Litigation Hold and Preservation

| Field | Value |
|---|---|
| Hold Evaluation Status | `[ACTION: attorney must evaluate preservation obligation immediately]` |
| Hold Notice Issued? | `[CONFIRM: Y / N / Pending — date if issued]` [deadline verification required] |
| Known Document Custodians | `[CONFIRM: list names and roles]` |
| Known ESI Sources | `[CONFIRM: e.g., email systems, file servers, mobile devices, third-party platforms]` |
| Hold Notice Skill Used | `skills/litigation/legal-hold/SKILL.md` |

---

## 9. Discovery Tracking

> Populate as discovery progresses. Each entry links to work product produced by relevant skills.

**Written Discovery:**

| # | Type | Served By | Served On | Date Served | Response Due | Status |
|---|---|---|---|---|---|---|
| 1 | `[CONFIRM: e.g., interrogatories]` | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` [deadline verification required] | `[CONFIRM]` [deadline verification required] | `[CONFIRM]` |

**Depositions:**

| # | Deponent | Role | Date Noticed | Date Scheduled | Prep Skill Used | Status |
|---|---|---|---|---|---|---|
| 1 | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` [deadline verification required] | `[CONFIRM]` [deadline verification required] | `skills/litigation/deposition-prep/SKILL.md` | `[CONFIRM]` |

**Subpoenas:**

| # | Recipient | Type | Date Issued | Response Due | Triage Skill Used | Status |
|---|---|---|---|---|---|---|
| 1 | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` [deadline verification required] | `[CONFIRM]` [deadline verification required] | `skills/litigation/subpoena-triage/SKILL.md` | `[CONFIRM]` |

---

## 10. Work-Product Index

> Index every draft deliverable produced by an AgentCounsel skill for this matter. Each entry is draft legal work product for attorney review.

| # | Skill Used | Date Run | Output Description | File / Location | Attorney Reviewer | Review Status |
|---|---|---|---|---|---|---|
| 1 | `skills/litigation/matter-intake/SKILL.md` | `[CONFIRM: date]` | Matter intake summary | `[CONFIRM: file path or location]` | `[CONFIRM]` | `[CONFIRM: Draft / Under Review / Adopted / Superseded]` |
| 2 | `skills/litigation/litigation-chronology/SKILL.md` | `[CONFIRM: date]` | Factual chronology | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 3 | `skills/litigation/legal-hold/SKILL.md` | `[CONFIRM: date]` | Legal hold notice draft | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 4 | `skills/litigation/demand-letter/SKILL.md` | `[CONFIRM: date]` | Demand letter draft | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 5 | `skills/litigation/brief-section-drafter/SKILL.md` | `[CONFIRM: date]` | Brief section draft | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 6 | `skills/litigation/privilege-log-review/SKILL.md` | `[CONFIRM: date]` | Privilege log review | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |
| 7 | `skills/legal-research/legal-research-memo/SKILL.md` | `[CONFIRM: date]` | Research memo | `[CONFIRM]` | `[CONFIRM]` | `[CONFIRM]` |

---

## 11. Risk and Issue Summary

> This summary is draft legal work product based solely on information recorded in this workspace. It is not a legal conclusion and is not final. The responsible attorney must review, correct, and adopt any risk characterization before it is relied upon.

| # | Issue / Risk | Category | Preliminary Assessment | Priority | Attorney Confirmation Status |
|---|---|---|---|---|---|
| 1 | `[CONFIRM: describe issue]` | `[CONFIRM: e.g., Deadline, Claims, Discovery, Insurance]` | `[CONFIRM: preliminary notes — not a legal conclusion]` | `[CONFIRM: High / Medium / Low]` | `[ATTORNEY TO CONFIRM]` |
| 2 | | | | | |

**Preliminary Risk Band:** `[CONFIRM: Low / Medium / High]` `[ATTORNEY TO CONFIRM: preliminary triage only — not a legal conclusion]`

**Preliminary Materiality Posture:** `[CONFIRM: None / Monitor / Reserve / Disclose]` `[ATTORNEY TO CONFIRM: preliminary triage only — not a legal conclusion and not accounting or securities advice]`

_Reference: `skills/litigation/matter-intake/SKILL.md` — Step 13 (Preliminary Risk and Materiality Assessment)._

---

## 12. Insurance and Indemnity

| Field | Value |
|---|---|
| Potentially Applicable Policy / Agreement | `[CONFIRM: policy number, insurer, coverage type, or indemnity agreement reference]` |
| Notice Obligation Evaluated? | `[ACTION: verify coverage and notice requirements with client and coverage counsel]` |
| Notice Deadline | `[CONFIRM: date — if applicable]` [deadline verification required] [CONFIRM: attorney to verify] |
| Notice Given? | `[CONFIRM: Y / N / Pending]` |

---

## 13. Open Items and Action Items

| # | Item | Type | Owner | Due Date | Status |
|---|---|---|---|---|---|
| 1 | Run conflicts check | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 2 | Evaluate litigation hold / preservation obligation | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 3 | Verify all deadlines independently | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 4 | Evaluate insurance notice obligation | `[ACTION]` | `[CONFIRM: responsible attorney]` | `[CONFIRM: date]` [deadline verification required] | Open |
| 5 | `[CONFIRM: additional action item]` | | `[CONFIRM]` | `[CONFIRM]` [deadline verification required] | Open |

---

## 14. Attorney Sign-Off

> The responsible attorney must review this workspace, resolve all `[CONFIRM: ...]` and `[ACTION: ...]` placeholders, and sign off before this workspace is relied upon or shared.

- [ ] Client identity and role confirmed with client.
- [ ] All party names and aliases captured; conflicts check run and gate status confirmed.
- [ ] All deadlines in Section 6 independently verified by attorney — none computed or inferred.
- [ ] Statute of limitations and any tolling issues evaluated.
- [ ] Litigation hold / preservation obligation evaluated; hold notice issued if required.
- [ ] Insurance and indemnity notice obligations evaluated; timely notice given if required.
- [ ] Jurisdiction, venue, and governing law confirmed.
- [ ] All `[CONFIRM: ...]` and `[ACTION: ...]` placeholders in this workspace resolved.
- [ ] Work-product index (Section 10) reflects all drafts produced; each draft reviewed and adopted or superseded by attorney.
- [ ] Risk and issue summary (Section 11) reviewed and confirmed or revised by responsible attorney.
- [ ] Privilege and confidentiality of this workspace protected; distribution limited to authorized personnel.
- [ ] No client-sensitive facts appear in any reusable copy of the blank template.

| Field | Value |
|---|---|
| Responsible Attorney | `[CONFIRM: name and bar admission]` |
| Sign-Off Date | `[CONFIRM: date]` |
| Notes | |
