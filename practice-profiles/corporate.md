> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Corporate

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Corporate |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and forum in which this group regularly works. Agents will gate jurisdiction-specific analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Incorporation / Formation Jurisdictions | `[CONFIRM: e.g., specific states, countries where entities are formed]` |
| Primary Governing-Law Regimes | `[CONFIRM: corporate law regimes applicable to group's work]` |
| Secondary / Occasional Jurisdictions | `[CONFIRM: list or "none at this time"]` |
| Cross-Border / International Work | `[CONFIRM: yes/no; if yes, list jurisdictions and any foreign-investment review considerations]` |
| Securities Regulation Jurisdictions | `[CONFIRM: yes/no; if yes, specify regimes — note: agent never provides securities advice; flag for specialist]` |

**Guiding prompts for this section:**
- In which jurisdictions does the group most frequently form, dissolve, or reorganize entities?
- Are there primary corporate-law regimes that govern most of the group's work?
- Does the group handle cross-border M&A, joint ventures, or foreign-investment matters?
- Are any clients publicly traded or subject to securities-registration requirements?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., executive team, board, finance, treasury]` |
| External Client Types | `[CONFIRM: e.g., startups, private equity sponsors, public companies, family businesses]` |
| Team Composition | `[CONFIRM: M&A partners, corporate associates, paralegals, transaction coordinators]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how corporate matters are opened and assigned]` |

**Guiding prompts for this section:**
- Who is the primary internal or external client this group advises?
- Is there a designated attorney for board-governance or minutes work?
- How does the group coordinate with the tax, employment, and regulatory practices on transactions?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Transaction value | `[CONFIRM: e.g., above $[X], requires partner sign-off]` | `[CONFIRM: role or name]` |
| Board / shareholder approval required | `[CONFIRM: any action requiring board resolution, shareholder vote, or committee approval]` | `[CONFIRM: role or name]` |
| Signing authority outside matrix | `[CONFIRM: any signatory not listed in the approved signing-authority matrix]` | `[CONFIRM: role or name]` |
| Third-party consent required | `[CONFIRM: any transaction triggering consent rights under existing agreements]` | `[CONFIRM: role or name]` |
| Regulatory filing or notification | `[CONFIRM: any transaction triggering a mandatory filing or notification]` | `[CONFIRM: role or name]` |
| Securities law considerations | `[CONFIRM: escalate to securities specialist; agent does not provide securities analysis]` | `[CONFIRM: role or name]` |
| Cross-border or foreign-investment review | `[CONFIRM: any transaction involving foreign acquirers or regulated industries]` | `[CONFIRM: role or name]` |
| Conflict between constituent documents | `[CONFIRM: any inconsistency between charter, bylaws, shareholders' agreement, or board resolutions]` | `[CONFIRM: role or name]` |
| Any step outside the corporate workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- At what transaction value does a deal require full partner-level oversight from inception?
- What categories of corporate action always require a board resolution or unanimous written consent?
- Does the group use a formal signing-authority matrix, and where is it stored?
- Which transaction types trigger mandatory regulatory filings or foreign-investment review?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., issues list, due-diligence summary, board-resolution template, closing checklist]` |
| Tone | `[CONFIRM: e.g., formal, board-ready language; plain business prose for internal memos]` |
| Length convention | `[CONFIRM: e.g., board memo ≤ 2 pages; full due-diligence report as needed]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Board / governance document style | `[CONFIRM: template conventions for board resolutions, consents, and minutes]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- What is the preferred format for a new-matter due-diligence summary?
- Does the group use standard board-resolution or unanimous-written-consent templates?
- How should a closing checklist be structured — tabular by party obligation, or chronological?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| Entity-formation templates | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Board-resolution and consent templates | `[CONFIRM: file name and location]` | |
| Signing-authority matrix | `[CONFIRM: file name and location]` | Governs all execution decisions |
| Due-diligence checklist (M&A) | `[CONFIRM: file name and location]` | |
| Closing-checklist template | `[CONFIRM: file name and location]` | |
| Capitalization-table management system | `[CONFIRM: system name only]` | Do not paste cap-table data |
| Approval / board-convention guidelines | `[CONFIRM: file name and location]` | |
| Corporate minute book location | `[CONFIRM: system or storage name only]` | Do not reference specific minutes |

**Guiding prompts for this section:**
- Where does the group store its standard entity-formation documents and board templates?
- Is there a central repository for executed board resolutions and shareholder consents?
- What system manages capitalization tables and equity records?

---

## Standard Positions / Playbooks

Record the group's default positions on common corporate matters. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Board-meeting notice | `[CONFIRM: e.g., minimum notice period; waiver convention]` | `[verify jurisdiction]` |
| Written-consent in lieu of meeting | `[CONFIRM: e.g., used routinely / used only for specified actions]` | `[verify jurisdiction]` |
| Unanimous written consent | `[CONFIRM: when required vs. majority]` | `[verify jurisdiction]` |
| Quorum requirements | `[CONFIRM: default quorum rules for board and shareholder meetings]` | `[verify jurisdiction]` |
| Officer signing authority | `[CONFIRM: which officers may bind the entity without board approval, by transaction type or dollar amount]` | Confirm against current signing-authority matrix |
| Pre-emptive rights | `[CONFIRM: group's default position on pre-emptive rights in equity financings]` | |
| Tag-along / drag-along rights | `[CONFIRM: group's default position]` | |
| Information rights | `[CONFIRM: group's standard information-rights package]` | |
| Indemnification of directors/officers | `[CONFIRM: group's standard indemnification approach in governing documents]` | `[verify jurisdiction]` |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- What is the group's default position on board-meeting notice requirements and waivers?
- Does the group routinely use written consents in lieu of meetings, and for which action types?
- What signing-authority tiers does the group treat as standard?
- What is the group's standard indemnification position for directors and officers in governing documents?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Due-diligence summary or issues list | `[CONFIRM: e.g., supervising associate or partner]` | All; no exceptions |
| Board resolution or written consent | `[CONFIRM: role]` | Before execution |
| Entity-formation documents | `[CONFIRM: role]` | Before filing |
| Closing checklist | `[CONFIRM: role]` | Before distribution to transaction parties |
| Capitalization-table analysis | `[CONFIRM: role]` | Before use in any transaction or financing |
| Any output touching securities law | Securities-law specialist | Always; agent does not opine on securities matters |
| Any cross-border corporate action | `[CONFIRM: role]` | `[verify jurisdiction]` |

**Guiding prompts for this section:**
- Is there a tiered review structure for board documents — associate prepares, partner approves?
- Who must approve entity-formation documents before they are filed?
- Does the group require a securities-law specialist to review any equity-related deliverable?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| Signing authority has been obtained | Must be confirmed against the current signing-authority matrix for each action |
| A board resolution or consent is valid | Validity depends on quorum, notice, and constituent documents — attorney must confirm |
| The capitalization table is current | Cap tables change with each financing and grant cycle; must be confirmed from the authoritative source |
| No third-party consents are required | Existing agreements may contain change-of-control or consent rights; must be checked |
| No regulatory filing is triggered | Transaction thresholds and notification requirements vary by jurisdiction; must be confirmed |
| Prior minutes or resolutions reflect current governance | Corporate records may be incomplete or superseded; must be confirmed |
| Entity is in good standing | Good-standing status must be confirmed from the relevant authority at the time of each transaction |
| No securities law issues arise | Securities analysis is outside the agent's scope; must be routed to a specialist |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/corporate-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for attorney review.

Do not include client names, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
