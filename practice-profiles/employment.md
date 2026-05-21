> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Employment

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Employment |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and forum in which this group regularly works. Agents will gate jurisdiction-specific analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Employment Jurisdictions | `[CONFIRM: e.g., states, provinces, countries where the group advises]` |
| Secondary / Occasional Jurisdictions | `[CONFIRM: list or "none at this time"]` |
| Federal vs. State Mix | `[CONFIRM: proportion of federal vs. state employment matters]` |
| Administrative Agencies / Tribunals | `[CONFIRM: agencies before which the group appears]` |
| Multi-Jurisdictional / Remote-Work Matters | `[CONFIRM: yes/no; if yes, list jurisdictions with significant remote-work populations]` |

**Guiding prompts for this section:**
- In which jurisdictions does the group advise on employment matters most frequently?
- Does the group handle matters before federal administrative agencies, state labor boards, or similar tribunals?
- Are remote-work arrangements creating multi-jurisdictional employment relationships the group must account for?
- Are there jurisdictions the group avoids and routes to local counsel?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., HR, people operations, executive team, business units]` |
| External Client Types | `[CONFIRM: e.g., employers, employees, HR departments, workforce-management platforms]` |
| Team Composition | `[CONFIRM: employment partners, associates, HR-law specialists, paralegals]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how employment matters are opened, e.g., HR tickets, direct escalation]` |
| Representation Posture | `[CONFIRM: employer-side, employee-side, or both — confirm per matter]` |

**Guiding prompts for this section:**
- Does the group represent primarily employers, employees, or both?
- Who is the primary HR or people-operations contact for internal employment matters?
- How does the group coordinate with external HR advisors or benefits counsel?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Worker classification question | `[CONFIRM: any independent-contractor vs. employee classification question; never assume classification]` | `[CONFIRM: role or name]` |
| At-will posture in question | `[CONFIRM: any matter where at-will status is disputed or unclear]` | `[CONFIRM: role or name]` |
| Potential discriminatory action | `[CONFIRM: any matter involving a protected characteristic; escalate immediately]` | `[CONFIRM: role or name]` |
| Wage-and-hour compliance | `[CONFIRM: any overtime, minimum-wage, or pay-classification question]` | `[CONFIRM: role or name]` |
| WARN or mass-layoff analysis | `[CONFIRM: any reduction in force above $[X] headcount or $[X]% of workforce]` | `[CONFIRM: role or name]` |
| Non-compete or restrictive covenant | `[CONFIRM: enforceability questions are jurisdiction-specific; always escalate]` | `[CONFIRM: role or name]` |
| Retaliation risk | `[CONFIRM: any termination or adverse action following a protected activity]` | `[CONFIRM: role or name]` |
| Agency charge or complaint filed | `[CONFIRM: any formal charge with a labor or employment agency]` | `[CONFIRM: role or name]` |
| Deadline near or uncertain | Any deadline within `[CONFIRM: X days]` or any deadline the agent cannot confirm | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Any step outside the employment workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What classification scenarios automatically require attorney review — gig workers, dual-status workers, statutory employees?
- Does the group have a defined headcount or payroll threshold for WARN-act-type analysis?
- Which restrictive-covenant issues are treated as requiring outside-counsel involvement?
- What is the escalation path for a potential retaliation matter?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., issue-spotting memo, policy-gap analysis, offer-letter review, separation-agreement checklist]` |
| Tone | `[CONFIRM: e.g., plain HR-ready language for policies; formal legal prose for filings and demand responses]` |
| Length convention | `[CONFIRM: e.g., HR-facing summary ≤ 1 page; full legal memo as needed]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Policy-document style | `[CONFIRM: conventions for employee handbooks, policy updates, acknowledgment forms]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- Should agents produce HR-facing summaries in plain language, or attorney-facing legal memos?
- What format does the group use for separation-agreement review checklists?
- Does the group produce employee-handbook sections, and if so, in what format?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| Employee handbook (current version) | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Offer-letter templates | `[CONFIRM: file name and location]` | |
| Separation-agreement templates | `[CONFIRM: file name and location]` | |
| Independent-contractor agreement templates | `[CONFIRM: file name and location]` | |
| Classification-review checklist | `[CONFIRM: file name and location]` | |
| Non-compete / restrictive-covenant playbook | `[CONFIRM: file name and location]` | |
| HR escalation and investigation protocol | `[CONFIRM: file name and location]` | |
| Wage-and-hour compliance checklist | `[CONFIRM: file name and location]` | |

**Guiding prompts for this section:**
- Where does the group store its current offer-letter and separation-agreement templates?
- Is there an authoritative classification-review checklist for independent-contractor engagements?
- What document governs the group's internal HR-investigation protocol?

---

## Standard Positions / Playbooks

Record the group's default positions on common employment matters. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| At-will employment default | `[CONFIRM: e.g., at-will is the default in jurisdictions where permissible; exceptions listed]` | `[verify jurisdiction]` |
| Worker classification default | `[CONFIRM: e.g., favor employee classification when in doubt; confirm with attorney before treating as contractor]` | `[verify jurisdiction]` |
| Non-compete enforceability | `[CONFIRM: group's default risk assessment — e.g., narrow, time-limited agreements preferred]` | `[verify jurisdiction]` |
| Separation agreement — release scope | `[CONFIRM: group's standard position on scope of claims released]` | `[verify jurisdiction]` |
| Separation agreement — review period | `[CONFIRM: group's standard position on the review and revocation period]` | `[verify jurisdiction]` |
| Arbitration agreements | `[CONFIRM: group's default position on including arbitration clauses in offer letters or handbooks]` | `[verify jurisdiction]` |
| Investigation — documentation standard | `[CONFIRM: e.g., written record of all investigative steps as a default]` | |
| Retaliation-risk assessment | `[CONFIRM: default step — assess retaliation risk before any adverse employment action]` | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- Is at-will employment the default in every jurisdiction where the group works, or are there exceptions?
- Does the group have a standing policy on worker classification when a new engagement type arises?
- What is the group's default position on arbitration agreements in employment contracts?
- What review and revocation period does the group treat as standard in separation agreements?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Classification analysis | `[CONFIRM: e.g., supervising attorney]` | All; no exceptions |
| Separation agreement (draft or review) | `[CONFIRM: role]` | Before transmission to any employee |
| Non-compete review or draft | `[CONFIRM: role]` | Before use; confirm jurisdiction |
| Policy or handbook update | `[CONFIRM: role]` | Before distribution to workforce |
| Response to agency charge | `[CONFIRM: role]` | Before submission |
| Offer-letter review (non-standard terms) | `[CONFIRM: role]` | Any deviation from template requires review |
| Any output touching a protected characteristic | Supervising attorney | Always; no exceptions |
| Any output relating to a deadline | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` | All statutory and administrative deadlines |

**Guiding prompts for this section:**
- Is there a tiered review structure for employment matters based on risk level?
- Who must approve a separation agreement before it is sent to an employee?
- Does the group require a second attorney to review any response to a discrimination charge?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| Employment is at-will | At-will status varies by jurisdiction, contract, and course of dealing; must be confirmed |
| A worker is an independent contractor | Classification is a legal determination; agent must flag and escalate for attorney assessment |
| A non-compete is enforceable | Enforceability is highly jurisdiction-specific; `[verify jurisdiction]` |
| A separation agreement releases all claims | Scope of release depends on jurisdiction, age of employee, and specific claims; attorney must confirm |
| No protected activity preceded the adverse action | Must be confirmed through the matter facts before any adverse-action analysis |
| Applicable wage-and-hour rules are known | Wage-and-hour requirements vary significantly by jurisdiction; must be confirmed |
| Handbook policies are current and lawfully compliant | Handbooks require regular review; always confirm against the authoritative current version |
| No agency charge has been filed | Filing status must be confirmed; it triggers specific procedural obligations |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

This profile is populated directly by the practice group. Work through each section with the supervising attorney, confirm all positions and thresholds, and record the approved answers in place of the bracketed placeholders.

Do not include employee names, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
