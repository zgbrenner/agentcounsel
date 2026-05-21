> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Litigation

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Litigation |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and forum in which this group regularly litigates or appears. Agents will gate procedural and substantive analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Litigation Jurisdictions | `[CONFIRM: e.g., specific courts, state/federal districts]` |
| Secondary / Occasional Jurisdictions | `[CONFIRM: list or "none at this time"]` |
| Federal Court Practice | `[CONFIRM: yes/no; if yes, list circuits and districts]` |
| Administrative / Regulatory Forums | `[CONFIRM: agencies and tribunals where the group appears]` |
| International Arbitration or Foreign Proceedings | `[CONFIRM: yes/no; if yes, list forums and applicable procedural rules]` |
| Preferred Venue (where group initiates) | `[CONFIRM: venue preferences when client is plaintiff or petitioner]` |

**Guiding prompts for this section:**
- In which courts does this group file most frequently?
- Are there specific district or circuit courts where the group has standing preferences or established practices?
- Does the group appear before administrative agencies, arbitration panels, or international tribunals?
- Are there jurisdictions the group avoids for strategic or practical reasons?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., business units, risk management, finance]` |
| External Client Types | `[CONFIRM: e.g., corporate defendants, insurance carriers, plaintiffs]` |
| Team Composition | `[CONFIRM: trial partners, litigation associates, paralegals, e-discovery staff]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how litigation matters are opened and assigned]` |
| Conflicts-Check Process | `[CONFIRM: reference to conflicts system by name only]` |

**Guiding prompts for this section:**
- Who is the primary internal or external client this group represents?
- Is there a designated litigation-hold or records-preservation coordinator?
- How does the group handle conflicts-of-interest checks at matter intake?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Settlement demand or authority | `[CONFIRM: e.g., any settlement above $[X] requires partner approval]` | `[CONFIRM: role or name]` |
| Litigation hold required | `[CONFIRM: any matter with identified or reasonably anticipated litigation]` | `[CONFIRM: role or name]` |
| Conflicts flag at intake | `[CONFIRM: any potential conflict identified by the conflicts-check system]` | `[CONFIRM: role or name]` |
| Dispositive-motion strategy | `[CONFIRM: e.g., summary judgment, motion to dismiss — requires partner sign-off]` | `[CONFIRM: role or name]` |
| Expert retention | `[CONFIRM: any recommendation to retain or designate an expert witness]` | `[CONFIRM: role or name]` |
| Deadline near or uncertain | Any deadline within `[CONFIRM: X days]` or any deadline the agent cannot confirm | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Class action or mass-tort exposure | `[CONFIRM: escalate whenever the pleadings allege class or mass claims]` | `[CONFIRM: role or name]` |
| Regulatory investigation overlap | `[CONFIRM: any matter involving a pending or potential regulatory inquiry]` | `[CONFIRM: role or name]` |
| Adverse-party is a government entity | `[CONFIRM: always escalate]` | `[CONFIRM: role or name]` |
| Any step outside the litigation workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What is the settlement-authority ceiling below which a case can be resolved without senior-partner approval?
- Does the group have a defined litigation-hold trigger — specific events or matter types that automatically trigger a hold?
- At what claim value or case type is a second-chair partner required?
- How does the group handle matters that begin as a contract dispute but develop regulatory exposure?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., issue-spotting memo, chronology, deposition outline, discovery matrix]` |
| Tone | `[CONFIRM: e.g., adversarial advocacy in filings; objective analysis in internal memos]` |
| Length convention | `[CONFIRM: e.g., internal case summary ≤ 2 pages; full issue memo as needed]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Citation format | `[CONFIRM: citation style used in court filings for this jurisdiction — do not populate authority; agent flags gaps]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- What is the preferred internal format for a new-matter issue-spotting memo?
- Does the group use a standard format for deposition outlines or discovery matrices?
- How should litigation chronologies be presented — tabular or narrative?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, checklists, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| Litigation hold policy and template | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Case-intake checklist | `[CONFIRM: file name and location]` | |
| Discovery-management playbook | `[CONFIRM: file name and location]` | |
| Deposition-preparation checklist | `[CONFIRM: file name and location]` | |
| Settlement-authority matrix | `[CONFIRM: file name and location]` | |
| Standard protective-order template | `[CONFIRM: file name and location]` | |
| Conflicts-check system | `[CONFIRM: system name only]` | Do not reference matter data |
| Matter-management / docketing system | `[CONFIRM: system name only]` | Deadline source of truth — always confirm with attorney |

**Guiding prompts for this section:**
- Where does the group store its litigation-hold templates and preservation notices?
- Is there a master playbook for discovery strategy or e-discovery protocols?
- What docketing or deadline-tracking system is authoritative for this group?

---

## Standard Positions / Playbooks

Record the group's default strategic and procedural positions. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Litigation hold — trigger timing | `[CONFIRM: e.g., at first notice of potential claim, not at filing]` | |
| Venue preference (as plaintiff) | `[CONFIRM: preferred jurisdiction and basis]` | |
| Venue objection threshold (as defendant) | `[CONFIRM: conditions under which the group contests venue]` | |
| Settlement-authority tiers | `[CONFIRM: tiered approval structure by dollar amount]` | |
| Expert designation — default timing | `[CONFIRM: group's standard approach to early vs. late expert retention]` | |
| Protective order — default scope | `[CONFIRM: e.g., attorneys' eyes only tier for trade secrets as a default ask]` | |
| E-discovery preservation scope | `[CONFIRM: custodian categories and data types group preserves as a default]` | |
| Conflicts — opening-matter rule | `[CONFIRM: group's default rule on matters involving former clients or adverse parties]` | |
| Counterclaim analysis | `[CONFIRM: e.g., always assess counterclaim exposure before filing or answering]` | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- Does the group have a standing position on when to send a litigation-hold notice versus waiting for formal litigation?
- What are the tiers of settlement authority — who can approve at what dollar level without escalation?
- Does the group have a default position on venue objections or removal to federal court?
- Are there case types the group always evaluates for counterclaim or cross-claim exposure?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Issue-spotting memo | `[CONFIRM: e.g., supervising associate or partner]` | All; no exceptions |
| Litigation-hold notice | `[CONFIRM: role]` | Before transmission to any recipient |
| Draft court filing or pleading | Partner-level review | All; no exceptions |
| Settlement recommendation | `[CONFIRM: role]` | Before communication to client |
| Discovery response (substantive) | `[CONFIRM: role]` | Before service |
| Expert designation recommendation | `[CONFIRM: role]` | Before retention |
| Any output relating to a deadline | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` | No deadline is final until attorney-verified |

**Guiding prompts for this section:**
- Is there a separate sign-off requirement for court filings versus internal work product?
- Who must approve a draft litigation-hold notice before it goes out?
- Does the group require a second-attorney review for all settlement recommendations?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| No litigation hold is required | Any matter with potential claims may require a hold; agent must flag for attorney determination |
| A deadline has been correctly calculated | Deadline calculation is always an attorney task; `[deadline verification required]` |
| No conflicts of interest exist | Conflicts must be confirmed through the authoritative conflicts system |
| The matter is in the correct jurisdiction | Removal, transfer, or change-of-venue issues must be attorney-assessed |
| A prior pleading or brief reflects the current state of the law | Law changes; every legal proposition must be independently verified |
| Settlement authority has been obtained | Must be confirmed against the settlement-authority matrix for the matter |
| The client has been advised of all material developments | Communication history is outside the agent's scope; attorney must confirm |
| Class exposure has been ruled out | Must be attorney-assessed based on the pleadings and facts |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/litigation-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for attorney review.

Do not include client names, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
