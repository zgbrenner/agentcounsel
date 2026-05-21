> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Regulatory

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Regulatory |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and regulatory forum in which this group regularly works. Agents will gate jurisdiction-specific analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Regulatory Jurisdictions | `[CONFIRM: countries, states, or regions where the group actively monitors and advises]` |
| Secondary / Occasional Jurisdictions | `[CONFIRM: list or "none at this time"]` |
| Regulatory Bodies Monitored | `[CONFIRM: describe by jurisdiction and function — do not use acronyms; e.g., "federal financial consumer protection agency," "state insurance regulator"]` |
| Sector-Specific Regulatory Frameworks | `[CONFIRM: describe the regulatory sectors the group covers, e.g., financial services, telecommunications, healthcare, energy, digital markets]` |
| International / Multi-Jurisdictional Matters | `[CONFIRM: yes/no; if yes, list applicable international regulatory bodies or coordination frameworks]` |

**Guiding prompts for this section:**
- Which regulatory agencies does this group actively monitor for new rules, guidance, and enforcement actions?
- In which jurisdictions does the group regularly file, respond, or appear before regulators?
- Are there sector-specific regulatory frameworks — financial services, telecommunications, healthcare, energy — that define the group's work?
- Does the group handle coordinated multi-jurisdictional regulatory inquiries?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., compliance, government affairs, finance, product, executive team]` |
| External Client Types | `[CONFIRM: e.g., regulated entities, trade associations, government contractors, licensing applicants]` |
| Team Composition | `[CONFIRM: regulatory partners, associates, government-relations counsel, compliance specialists, paralegals]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how regulatory matters reach the group — regulatory notices, compliance escalations, government inquiries]` |
| Reporting Lines to Compliance Function | `[CONFIRM: relationship between this group and the organization's compliance function — reference by function name, not names]` |

**Guiding prompts for this section:**
- Who is the primary compliance or government-affairs contact that routes matters to this group?
- How does the group coordinate with the organization's compliance function on regulatory filings and responses?
- Does the group work with external government-relations advisors, and how are those relationships managed?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Regulatory inquiry or investigation | `[CONFIRM: any formal or informal contact from a regulatory agency — escalate immediately]` | `[CONFIRM: role or name]` |
| Mandatory reporting deadline | Any regulatory reporting deadline — never computed by the agent | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Enforcement action | `[CONFIRM: any notice of enforcement, investigation, or civil investigative demand]` | `[CONFIRM: role or name]` |
| New regulatory guidance affecting operations | `[CONFIRM: any new rule, guidance, or no-action request affecting business operations]` | `[CONFIRM: role or name]` |
| Licensing or registration trigger | `[CONFIRM: any new business activity that may require a new license, registration, or approval]` | `[CONFIRM: role or name]` |
| Sector-specific threshold crossed | `[CONFIRM: e.g., revenue threshold, customer count, or asset level triggering additional regulatory obligations]` | `[CONFIRM: role or name]` |
| Cross-border regulatory overlap | `[CONFIRM: any matter involving multiple regulators or jurisdictions]` | `[CONFIRM: role or name]` |
| Self-disclosure or voluntary-reporting consideration | `[CONFIRM: any potential self-disclosure or voluntary remediation situation]` | `[CONFIRM: role or name]` |
| Any step outside the regulatory workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What is the group's escalation path the moment a regulatory inquiry is received?
- Are there mandatory reporting thresholds — financial, operational, or incident-related — for which the group has standing escalation rules?
- How does the group handle matters that are simultaneously under inquiry by multiple regulators?
- What is the group's approach to self-disclosure or voluntary remediation situations?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., regulatory gap analysis, compliance checklist, regulatory-response outline, comment-letter draft, license-application summary]` |
| Tone | `[CONFIRM: e.g., formal regulatory prose for agency submissions; plain language for internal compliance summaries]` |
| Length convention | `[CONFIRM: e.g., internal compliance summary ≤ 2 pages; full gap analysis or response as needed]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Regulatory-filing conventions | `[CONFIRM: any specific format requirements for filings with primary regulatory bodies — reference by body function, not name]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- What format does the group use for regulatory-gap analyses?
- Does the group produce comment letters or regulatory submissions in a standardized format?
- How are internal compliance summaries distinguished from attorney-work-product memos?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| Regulatory-monitoring tracker | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Regulatory-response playbook | `[CONFIRM: file name and location]` | Governs all responses to regulatory inquiries |
| Compliance-gap analysis template | `[CONFIRM: file name and location]` | |
| License and registration inventory | `[CONFIRM: file name and location]` | Do not paste license numbers or credentials |
| Mandatory reporting calendar | `[CONFIRM: file name or system name]` | Agent never computes deadlines; attorney verifies |
| Comment-letter template | `[CONFIRM: file name and location]` | |
| Government-inquiry response checklist | `[CONFIRM: file name and location]` | |
| Enforcement-response protocol | `[CONFIRM: file name and location]` | |

**Guiding prompts for this section:**
- Where does the group store its regulatory-monitoring tracker?
- Is there an authoritative playbook for responding to regulatory inquiries and civil investigative demands?
- What system tracks the group's license and registration obligations and renewal dates?

---

## Standard Positions / Playbooks

Record the group's default positions on common regulatory matters. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Response to regulatory inquiry — initial posture | `[CONFIRM: e.g., acknowledge receipt promptly; do not substantively respond without attorney review]` | |
| Document preservation on regulatory inquiry | `[CONFIRM: e.g., litigation-hold equivalent triggered on receipt of any regulatory inquiry]` | |
| Self-disclosure default posture | `[CONFIRM: e.g., attorney assessment required before any voluntary disclosure is made]` | |
| New licensing trigger — default assessment | `[CONFIRM: e.g., any new product or geographic expansion assessed for licensing requirements before launch]` | `[verify jurisdiction]` |
| Regulatory monitoring cadence | `[CONFIRM: e.g., group monitors designated regulators on a specified frequency]` | |
| Reporting deadlines | `[CONFIRM: e.g., all mandatory reporting deadlines are tracked in the authoritative calendar; agent never computes]` | `[deadline verification required]` |
| Cross-agency coordination | `[CONFIRM: e.g., any matter involving multiple agencies is escalated to a named coordinating attorney]` | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- What is the group's default response posture when a regulatory inquiry is received?
- Does the group have a standing document-preservation protocol for regulatory matters?
- How does the group manage the licensing and registration renewal calendar?
- What is the group's default on self-disclosure — when does attorney assessment automatically occur?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Regulatory gap analysis | `[CONFIRM: e.g., supervising attorney]` | All; no exceptions |
| Response to regulatory inquiry (draft) | Partner-level review | All; no exceptions; before any submission |
| Comment letter or rulemaking submission | `[CONFIRM: role]` | Before submission |
| License or registration application | `[CONFIRM: role]` | Before filing |
| Compliance checklist or policy update | `[CONFIRM: role]` | Before distribution to compliance function |
| Enforcement-response strategy | Partner-level review | All; no exceptions |
| Any output relating to a deadline | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` | All reporting and response deadlines |

**Guiding prompts for this section:**
- Does every regulatory inquiry response require partner sign-off, or only those above a certain risk level?
- Who must approve a comment letter before it is submitted to a regulatory agency?
- Is there a separate review requirement for matters involving enforcement versus advisory matters?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| No regulatory filing or notification is required | Thresholds and triggers vary by jurisdiction, sector, and activity; must be confirmed |
| A regulatory deadline is known | Regulatory deadlines are jurisdiction- and regime-specific; `[deadline verification required]` |
| The organization is licensed for a new activity | License scope varies by jurisdiction and activity type; must be confirmed |
| A prior regulatory determination covers the new situation | Regulatory guidance and positions change; must be confirmed as current |
| No cross-agency coordination is required | Multiple regulators may have jurisdiction; must be attorney-assessed |
| Self-disclosure is not an option or is required | Self-disclosure analysis is a legal judgment; must be attorney-confirmed |
| Regulatory monitoring is current | Monitoring trackers require regular updates; confirm against the current version |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

This profile is populated directly by the practice group. Work through each section with the supervising attorney, confirm all monitored regulators, reporting lines, and escalation thresholds, and record the approved answers in place of the bracketed placeholders.

Do not include client names, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
