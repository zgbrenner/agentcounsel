> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Privacy

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Privacy |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and forum in which this group regularly works. Agents will gate jurisdiction-specific analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Privacy Regimes | `[CONFIRM: list the data-protection frameworks the group regularly advises under — do not name specific statutes; use descriptive labels, e.g., "EU general data protection regime," "US state consumer privacy laws"]` |
| Secondary / Occasional Regimes | `[CONFIRM: list or "none at this time"]` |
| Cross-Border Transfer Regimes | `[CONFIRM: yes/no; if yes, describe the transfer mechanisms the group regularly uses — no statute names; e.g., "standard contractual clauses," "binding corporate rules," "adequacy-based transfers"]` |
| Sector-Specific Regimes | `[CONFIRM: yes/no; if yes, describe sectors — e.g., health data, financial data, children's data, telecommunications]` |
| Enforcement Authorities | `[CONFIRM: data-protection or privacy regulatory bodies the group monitors or appears before — describe by jurisdiction, not by acronym or name]` |

**Guiding prompts for this section:**
- Which data-protection frameworks govern most of this group's advisory work?
- Does the group advise on cross-border data transfers, and if so, which transfer mechanisms does it use?
- Are there sector-specific privacy regimes — health data, financial records, children's data — that the group regularly navigates?
- Which enforcement authorities does the group monitor for guidance and enforcement trends?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., product, engineering, marketing, HR, procurement]` |
| External Client Types | `[CONFIRM: e.g., technology companies, healthcare organizations, financial institutions, adtech platforms]` |
| Team Composition | `[CONFIRM: privacy partners, associates, data-protection specialists, paralegals]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how privacy matters reach the group — product-review requests, DPA reviews, incident reports]` |
| Default Client Posture | `[CONFIRM: e.g., data controller, data processor, joint controller, or varies by matter]` |

**Guiding prompts for this section:**
- Does the group advise primarily data controllers, data processors, or both?
- Who is the primary internal contact for product-feature privacy reviews?
- How does the group receive and triage breach-incident reports?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Potential breach or security incident | `[CONFIRM: any suspected or confirmed unauthorized access to personal data — escalate immediately]` | `[CONFIRM: role or name]` |
| Breach-notification deadline | Any breach-notification deadline — deadlines vary by regime and are never computed by the agent | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| New cross-border transfer mechanism | `[CONFIRM: any new or changed data-transfer arrangement]` | `[CONFIRM: role or name]` |
| High-risk processing activity | `[CONFIRM: e.g., new processing requiring a privacy impact assessment under applicable regime]` | `[CONFIRM: role or name]` |
| Controller vs. processor classification in dispute | `[CONFIRM: any ambiguity in controller/processor status]` | `[CONFIRM: role or name]` |
| Data-subject rights request — complex | `[CONFIRM: e.g., requests requiring court order, third-party rights, or competing legal obligations]` | `[CONFIRM: role or name]` |
| Regulatory inquiry or investigation | `[CONFIRM: any contact from a data-protection authority]` | `[CONFIRM: role or name]` |
| Sector-specific regime triggered | `[CONFIRM: any processing touching a sector-specific regime, e.g., health, financial, children's data]` | `[CONFIRM: role or name]` |
| Any step outside the privacy workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What is the group's escalation path the moment a potential data breach is identified?
- Are there specific processing activities that automatically trigger a privacy impact assessment?
- How does the group handle data-subject rights requests that have competing legal obligations?
- At what point in a regulatory inquiry does outside counsel become involved?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., privacy impact assessment, DPA redline, gap analysis, breach-response checklist, data-mapping summary]` |
| Tone | `[CONFIRM: e.g., plain product-team language for PIAs; formal legal prose for DPAs and regulatory responses]` |
| Length convention | `[CONFIRM: e.g., product-facing privacy summary ≤ 1 page; full PIA or gap analysis as needed]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| DPA / contract-redline conventions | `[CONFIRM: track-changes Word, Markdown markup, or inline annotations]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- What format does the group use for privacy impact assessments or data-protection impact assessments?
- How should data-processing-agreement redlines be presented?
- Does the group produce product-team-facing privacy summaries, and in what format?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| Data-processing agreement template | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Privacy impact assessment template | `[CONFIRM: file name and location]` | |
| Breach-notification response playbook | `[CONFIRM: file name and location]` | Governs all breach-response timelines |
| Data-subject rights request procedure | `[CONFIRM: file name and location]` | |
| Cross-border transfer mechanism documentation | `[CONFIRM: file name and location]` | |
| Privacy notice templates | `[CONFIRM: file name and location]` | |
| Records of processing activities | `[CONFIRM: system or file name only]` | Do not paste ROPA data |
| Vendor privacy assessment checklist | `[CONFIRM: file name and location]` | |

**Guiding prompts for this section:**
- Where does the group store its current DPA template and any approved fallback clauses?
- Is there an authoritative breach-response playbook with regime-specific notification timelines?
- What document governs the group's data-subject rights request procedures?

---

## Standard Positions / Playbooks

Record the group's default positions on common privacy matters. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Controller vs. processor default | `[CONFIRM: e.g., group advises clients as controllers unless processing agreement designates processor status]` | Confirm per engagement |
| DPA — group's standard starting position | `[CONFIRM: e.g., group's own DPA template; will accept counterparty's template subject to review]` | |
| Cross-border transfer — preferred mechanism | `[CONFIRM: e.g., group's preferred transfer mechanism for outbound transfers]` | `[verify jurisdiction]` |
| Breach-notification posture | `[CONFIRM: e.g., err toward notification when risk to individuals is unclear; confirm with attorney]` | `[verify jurisdiction]` |
| Breach-notification timing | Not computed by agent — always attorney-verified | `[deadline verification required]` |
| Privacy impact assessment trigger | `[CONFIRM: e.g., required for any new processing of sensitive categories or large-scale profiling]` | `[verify jurisdiction]` |
| Data retention — default approach | `[CONFIRM: e.g., minimum necessary retention; no indefinite retention without legal basis]` | |
| Sub-processor approval | `[CONFIRM: e.g., general authorization vs. specific approval required by default]` | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- Does the group default to controller posture or processor posture for new client engagements?
- What is the group's default cross-border transfer mechanism for data flowing outside the primary regime?
- Does the group have a standing position on when a privacy impact assessment is required?
- What is the group's default approach to breach notification when the risk to individuals is uncertain?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Privacy impact assessment | `[CONFIRM: e.g., supervising attorney]` | All; no exceptions |
| DPA (draft or redline) | `[CONFIRM: role]` | Before execution |
| Breach-notification analysis | `[CONFIRM: role]` | Before notification is sent or decision is made not to notify |
| Data-subject rights response | `[CONFIRM: role]` | Before transmission to data subject |
| Cross-border transfer documentation | `[CONFIRM: role]` | Before transfer arrangement is implemented |
| Regulatory inquiry response | Partner-level review | All; no exceptions |
| Any output touching sector-specific regimes | `[CONFIRM: role with sector expertise]` | Always |
| Any output relating to a deadline | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` | All notification and response deadlines |

**Guiding prompts for this section:**
- Is there a separate sign-off requirement for breach-notification decisions versus routine DPA reviews?
- Who must approve a regulatory inquiry response before submission?
- Does the group require sector-specialist review for health or financial data matters?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| Client is a data controller (not a processor) | Controller/processor status is a legal determination that depends on the processing arrangement |
| No breach-notification obligation exists | Notification obligations vary by regime and risk assessment; attorney must confirm |
| A breach-notification deadline is known | Deadlines vary by regime and triggering event; `[deadline verification required]` |
| Cross-border transfer is lawful under current mechanism | Transfer mechanisms require ongoing legal validity; must be confirmed at time of use |
| A prior privacy impact assessment covers the new processing | New or changed processing activities require fresh assessment |
| Applicable privacy regime is the group's primary regime | Sector-specific or local regimes may overlay; must be confirmed |
| Data is not personal data under the applicable regime | Classification of data as personal is regime-specific and must be attorney-confirmed |
| Sub-processors have all been approved | Sub-processor list changes; must be confirmed from the current records |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

For a guided, question-by-question setup process, use the cold-start interview skill at `skills/setup/privacy-cold-start-interview/SKILL.md`. That skill walks through each section of this profile and produces a draft-completed version for attorney review.

Do not include client names, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
