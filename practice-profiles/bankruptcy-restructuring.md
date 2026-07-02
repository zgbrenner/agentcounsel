> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in. The Bankruptcy / Restructuring skills produce draft work product for a qualified, licensed attorney to review — never pleadings, filings, deadline calculations, or legal conclusions.

# Practice Profile: Bankruptcy / Restructuring

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Bankruptcy / Restructuring |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Bankruptcy procedure, local rules, and judge-specific practices vary by court and district and must be confirmed per case — `[verify jurisdiction]`. Agents gate every court-specific point on this list and flag anything outside it for attorney or local-counsel escalation.

| Field | Value |
|---|---|
| Primary Courts / Districts | `[CONFIRM: bankruptcy courts and districts where the group regularly appears]` |
| Secondary / Occasional Courts | `[CONFIRM: list or "none at this time"]` |
| Typical Chapters / Case Types | `[CONFIRM: e.g., Chapter 7, Chapter 11, Chapter 13, out-of-court restructuring, assignment for benefit of creditors]` |
| Local-Counsel Requirement | `[CONFIRM: courts where local counsel is always engaged]` |
| Cross-Border / Recognition Proceedings | `[CONFIRM: yes/no; if yes, note specialist-counsel practice]` |

**Guiding prompts for this section:**
- In which courts does the group regularly appear, and where is local counsel always engaged?
- Which chapters and case types recur, and which are referred out?
- How are local rules and judge-specific procedures confirmed for a new case?

---

## Client / Team Context

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., credit, treasury, workout groups, corporate development]` |
| Typical Party Roles | `[CONFIRM: e.g., creditor-side, debtor-side, buyer-side, lender-side, committee-side, contract counterparty — the user's role is confirmed at intake, never assumed]` |
| Typical Matter Types | `[CONFIRM: e.g., claims, preference demands, executory contracts, distressed M&A, plan and disclosure review, DIP financing]` |
| Team Composition | `[CONFIRM: partners, associates, paralegals, claims and docket coordinators]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight of AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how matters reach the group; intake requires debtor identity, party role, case status/chapter, and dates with sources]` |

**Guiding prompts for this section:**
- Which side does the group most often represent, and how is the user's role confirmed per matter?
- Who monitors dockets and claims registers, and how are findings routed?
- Who is the designated supervising attorney for AI-assisted work?

---

## Escalation Thresholds

Deadline criticality is the defining trait of this practice. No deadline, bar date, or look-back period is ever computed or inferred by an agent — every date is recorded as user-supplied with its source and flagged for attorney verification. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Any bar date or case deadline | Never computed or inferred; recorded only as user-supplied with source | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Near-term user-supplied date | `[CONFIRM: any user-supplied date within [X] days — escalate immediately]` | `[CONFIRM: role or name — immediate]` |
| Possible automatic-stay implication | Any contemplated action touching a debtor or estate property — stay applicability never determined by the agent | `[CONFIRM: role or name]` |
| Claim validity, amount, priority, or secured-status question | Never concluded by the agent | `[CONFIRM: role or name]` |
| Preference or avoidance demand received | `[CONFIRM: escalate on receipt; liability and defenses never concluded]` | `[CONFIRM: role or name]` |
| Executory-contract assumption / rejection decision | `[CONFIRM: facts organized only; the decision is attorney and client work]` | `[CONFIRM: role or name]` |
| Plan voting, confirmation, or disclosure-adequacy question | Never concluded by the agent | `[CONFIRM: role or name]` |
| Distressed-sale bid, objection, or auction date | `[CONFIRM: escalate; never computed]` | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Cash-collateral / DIP financing terms | `[CONFIRM: escalate for attorney review before any position]` | `[CONFIRM: role or name]` |
| Settlement or payment demand | `[CONFIRM: escalate before any response or payment]` | `[CONFIRM: role or name]` |
| Any step outside the workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What near-term window triggers immediate escalation of a user-supplied date?
- What is the routing when a contemplated action may implicate the automatic stay?
- Who reviews a preference demand on receipt, before any triage output is relied upon?

---

## Preferred Output Style

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., Deadline Tracker Intake Table, Stay Issue-Spotting Matrix, Proof of Claim Prep Checklist, Preference Demand Response Timeline, Plan/DS Issue Tracker]` |
| Tone | `[CONFIRM: e.g., plain business language, formal legal prose]` |
| Length convention | `[CONFIRM: e.g., executive summary + full tracker]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-rating scheme | `[CONFIRM: e.g., High / Medium / Low]` |
| Date-sourcing convention | Every date carries its source and `[deadline verification required]`; user-supplied computed entries are recorded as user-supplied basis, never confirmed |
| Redaction convention | Personal identifiers and account numbers flagged for redaction before any output circulates |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- Which named output structures from the area's output-patterns reference do reviewers expect?
- How should agents present a date whose basis the user computed themselves?

---

## Source-of-Truth Documents

List the authoritative sources this group uses. Reference by name and location only — do not paste content.

| Document | Location / Path | Notes |
|---|---|---|
| Court dockets / claims-agent sites | `[CONFIRM: which docket and claims-agent sources are authoritative per case]` | Referenced by name; currency confirmed per use |
| Deadline calendar system | `[CONFIRM: system name]` | Authoritative record of verified dates; agent never computes |
| Claim-form templates and filing conventions | `[CONFIRM: file name and location]` | Used with `skills/bankruptcy-restructuring/proof-of-claim-checklist/SKILL.md` |
| Preference / avoidance response playbook | `[CONFIRM: file name and location]` | Used with `skills/bankruptcy-restructuring/preference-demand-response-triage/SKILL.md` |
| Distressed-sale / diligence checklists | `[CONFIRM: file name and location]` | Used with `skills/bankruptcy-restructuring/distressed-asset-sale-checklist/SKILL.md` |
| Signature / approval authority matrix | `[CONFIRM: file name and location]` | |
| Output patterns | `skills/bankruptcy-restructuring/references/output-patterns.md` | Canonical AgentCounsel reference |

**Guiding prompts for this section:**
- Which docket and claims-agent sources are authoritative, and who confirms their currency?
- What system is the single record of attorney-verified deadlines?

---

## Standard Positions / Playbooks

Record the group's default working rules. An agent uses these to flag deviations and always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Date handling | Every date is user-supplied with a stated source; the agent never computes, converts, or confirms a date | `[deadline verification required]` |
| Near-term-date flag window | `[CONFIRM: dates within [X] days escalate immediately]` | |
| Stay check before action | `[CONFIRM: e.g., no demand, termination, setoff, or collection step is drafted until counsel confirms stay posture]` | Used with `skills/bankruptcy-restructuring/automatic-stay-issue-spotter/SKILL.md` |
| Claim intake conventions | `[CONFIRM: which claim facts and supporting documents are collected at intake]` | Used with `skills/bankruptcy-restructuring/creditor-claim-intake/SKILL.md` |
| Proof-of-claim preparation | `[CONFIRM: who prepares, who verifies; filing is attorney work]` | Used with `skills/bankruptcy-restructuring/proof-of-claim-checklist/SKILL.md` |
| Preference-demand response posture | `[CONFIRM: intake and timeline organization only; defenses assessed by counsel]` | |
| Docket monitoring | `[CONFIRM: who monitors and how new entries are routed]` | |
| Deadline-tracker conventions | `[CONFIRM: intake fields and verification workflow]` | Used with `skills/bankruptcy-restructuring/bankruptcy-deadline-tracker-intake/SKILL.md` |
| Redaction | Personal identifiers and account numbers flagged for redaction | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- What is the group's stay-check rule before any creditor action is drafted?
- Who verifies every tracker entry before the tracker is relied upon?
- What claim facts must intake capture before a proof-of-claim checklist is started?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, filed, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Deadline tracker intake table | `[CONFIRM: role]` | Every entry; every date attorney-verified |
| Stay issue-spotting matrix | `[CONFIRM: role]` | Before any action affecting the debtor or estate property |
| Proof-of-claim prep checklist | `[CONFIRM: role]` | Before any claim submission; filing is attorney work |
| Preference demand response timeline | `[CONFIRM: role]` | Before any response or payment |
| Executory-contract assumption/rejection checklist | `[CONFIRM: role]` | Before any position is taken |
| Plan / disclosure-statement issue tracker | `[CONFIRM: role]` | Before any vote or objection |
| Distressed-sale or DIP / cash-collateral output | `[CONFIRM: role]` | Before reliance |
| Restructuring term sheet review | `[CONFIRM: role]` | Before negotiation reliance |
| Any output echoing a date | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` | Every date, every deliverable |

**Guiding prompts for this section:**
- Is there a tiered review structure by exposure or case size?
- Which deliverables require partner-level review in addition to the supervising attorney?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| A deadline, bar date, or look-back period can be computed | Never computed or inferred; `[deadline verification required]` |
| A user-supplied computed date is correct | Recorded as user-supplied basis; never confirmed by the agent |
| The automatic stay applies, or does not, to a contemplated action | Stay applicability, exceptions, and violations are legal determinations |
| A claim's amount, validity, priority, or secured status | Allowance and priority are legal determinations |
| A transfer is avoidable, or a defense applies | Preference and avoidance analysis is attorney work |
| A plan is confirmable or a disclosure statement adequate | Confirmability and adequacy are never concluded by the agent |
| The case chapter, status, or the user's party role | Must be user-supplied at intake; never defaulted |
| A debt is, or is not, dischargeable | Dischargeability is a legal determination |
| The provided docket or claims register is current or complete | Currency must be confirmed against the authoritative source |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill. The loading order is: `core/` rules first, then this profile, then the skill.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/bankruptcy-restructuring-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for attorney review.

Do not include debtor names, creditor names, claim amounts, case numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
