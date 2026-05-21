> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: AI Governance

## Profile Information

| Field | Value |
|---|---|
| Practice Group | AI Governance |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and regulatory forum relevant to this group's AI governance work. Agents will gate jurisdiction-specific analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary AI-Regulatory Jurisdictions | `[CONFIRM: countries and states/regions where the group advises on AI governance and compliance]` |
| Secondary / Emerging Jurisdictions | `[CONFIRM: jurisdictions with developing AI regulatory frameworks the group is tracking]` |
| Sector-Specific AI Regulatory Frameworks | `[CONFIRM: yes/no; if yes, describe applicable sectors, e.g., financial services AI, health AI, automated hiring, content moderation]` |
| International / Cross-Border AI Deployment | `[CONFIRM: yes/no; if yes, list regions where AI systems are deployed and any applicable transfer or localization requirements]` |
| Regulatory Bodies Monitoring AI | `[CONFIRM: describe by jurisdiction and function — do not use acronyms; e.g., "national digital markets regulator," "sectoral financial supervisor"]` |

**Guiding prompts for this section:**
- In which jurisdictions does the group advise on AI regulatory compliance?
- Are there jurisdictions with active or proposed AI governance frameworks the group must monitor?
- Does the group advise on sector-specific AI rules — for example, automated decision-making in financial services, or AI-assisted healthcare tools?
- Where are the organization's AI systems deployed, and does that trigger cross-border compliance requirements?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., AI/ML engineering, product, compliance, risk management, executive team]` |
| External Client Types | `[CONFIRM: e.g., AI developers, AI deployers, regulated entities using AI systems, technology companies]` |
| Team Composition | `[CONFIRM: AI-law counsel, technology-law associates, privacy counsel, regulatory specialists, paralegals]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted work on AI matters]` |
| Matter-Intake Process | `[CONFIRM: how AI governance matters reach the group — model-deployment reviews, product launches, regulatory inquiries, incident reports]` |
| Relationship to Other Practice Groups | `[CONFIRM: how AI governance coordinates with privacy, product-legal, regulatory, and IP practices]` |

**Guiding prompts for this section:**
- Who is the primary AI or ML engineering contact that routes model-deployment matters to this group?
- How does this group interact with the organization's AI ethics, model risk, or responsible-AI function?
- At what stage in the AI model lifecycle does this group typically engage?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| High-risk AI system deployment | `[CONFIRM: any system classified as high-risk under the applicable AI risk tier]` | `[CONFIRM: role or name]` |
| Prohibited use case identified | `[CONFIRM: any system or application matching a prohibited-use-case category in this profile]` | `[CONFIRM: role or name — halt deployment]` |
| Fundamental-rights impact identified | `[CONFIRM: any AI system that could materially affect employment, creditworthiness, housing, healthcare, or similar decisions]` | `[CONFIRM: role or name]` |
| Regulatory AI notification or registration | `[CONFIRM: any AI system triggering a mandatory notification, registration, or conformity assessment]` | `[CONFIRM: role or name]` |
| Regulatory inquiry about an AI system | `[CONFIRM: any contact from a regulator about an AI system — escalate immediately]` | `[CONFIRM: role or name]` |
| AI-related incident or harm event | `[CONFIRM: any AI system output causing or contributing to harm, bias finding, or regulatory violation]` | `[CONFIRM: role or name]` |
| New AI system touching personal data | `[CONFIRM: coordinate with privacy practice profile; privacy impact assessment required]` | `[CONFIRM: role or name — and privacy counsel]` |
| Third-party AI model or vendor | `[CONFIRM: any deployment of a third-party AI model requiring contract and governance review]` | `[CONFIRM: role or name]` |
| Any step outside the AI governance workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What risk tier classification triggers automatic partner or senior-attorney review?
- Does the group have a defined list of prohibited AI use cases for which deployment must be halted?
- How does the group handle an AI system that starts as low-risk but its use expands into higher-risk territory?
- What is the escalation path when an AI-related harm or bias event is identified?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., AI risk assessment, model governance checklist, prohibited-use-case analysis, regulatory-readiness gap analysis, third-party AI vendor review]` |
| Tone | `[CONFIRM: e.g., plain technical-and-legal hybrid for engineering teams; formal legal prose for regulatory submissions and board-level reports]` |
| Length convention | `[CONFIRM: e.g., engineering-facing risk summary ≤ 1 page; full governance assessment as needed]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-tier format | `[CONFIRM: e.g., tiered rating aligned with internal model-risk framework]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- How does the group communicate AI risk assessments to engineering and product teams?
- What format does the group use for board-level AI governance reporting?
- Does the group produce regulatory-readiness gap analyses, and in what format?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| AI model risk tier framework | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Prohibited AI use cases list | `[CONFIRM: file name and location]` | Governs deployment halt decisions |
| AI governance review checklist | `[CONFIRM: file name and location]` | |
| AI risk assessment template | `[CONFIRM: file name and location]` | |
| AI incident-response protocol | `[CONFIRM: file name and location]` | |
| Third-party AI vendor review checklist | `[CONFIRM: file name and location]` | Coordinate with procurement and privacy |
| AI regulatory monitoring tracker | `[CONFIRM: file name and location]` | |
| Responsible-AI policy | `[CONFIRM: file name and location]` | |

**Guiding prompts for this section:**
- Where does the group store its model risk tier framework?
- Is there an authoritative list of prohibited AI use cases, and how is it maintained?
- What document governs the group's AI incident-response protocol?

---

## Standard Positions / Playbooks

Record the group's default positions on common AI governance matters. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Model risk tier assignment | `[CONFIRM: who classifies new AI systems and what tiers exist; e.g., low / limited / high / unacceptable]` | |
| Prohibited use cases | `[CONFIRM: list category labels, not specific systems; e.g., real-time biometric surveillance, social scoring, subliminal manipulation]` | Reference the prohibited-use-cases list document for full definitions |
| High-risk system — default governance requirements | `[CONFIRM: e.g., human-oversight mechanism, logging, audit trail, conformity documentation — all required before deployment]` | `[verify jurisdiction]` |
| Third-party AI model — default due diligence | `[CONFIRM: e.g., vendor AI governance review required before procurement for any non-trivial use case]` | |
| Personal data in AI training or inference | `[CONFIRM: e.g., privacy review required for any AI system trained on or processing personal data]` | Coordinate with privacy profile |
| Automated decision-making with material effects | `[CONFIRM: e.g., human-in-the-loop required for AI decisions with material effects on individuals]` | `[verify jurisdiction]` |
| AI incident reporting | `[CONFIRM: e.g., any AI-related harm event triggers incident-response protocol within a defined timeframe]` | `[CONFIRM: timeframe — not computed by agent]` |
| Regulatory monitoring cadence | `[CONFIRM: frequency and scope of monitoring for new AI governance rules and guidance]` | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- How are new AI systems assigned a risk tier, and who makes that determination?
- Does the group maintain a formal list of prohibited AI use cases, and how is it updated?
- What governance requirements does the group apply by default to high-risk AI systems?
- What is the group's standing position on automated decision-making with material individual effects?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| AI risk assessment | `[CONFIRM: e.g., supervising attorney]` | All; no exceptions |
| Prohibited-use-case analysis | `[CONFIRM: role]` | All; halt determination requires attorney sign-off |
| AI governance gap analysis | `[CONFIRM: role]` | Before presentation to engineering or executive teams |
| Third-party AI vendor review | `[CONFIRM: role — coordinate with privacy and procurement]` | Before vendor engagement |
| AI incident response | Partner-level review | Any incident with potential regulatory or legal consequences |
| Regulatory submission or notification | Partner-level review | All; no exceptions |
| Any output touching personal data in AI systems | `[CONFIRM: role — coordinate with privacy practice]` | Always |

**Guiding prompts for this section:**
- Is there a tiered review structure for AI risk assessments based on the risk tier of the system?
- Who must sign off on a prohibited-use-case determination before a deployment is halted or cleared?
- Does the group require cross-practice sign-off — privacy, regulatory, product-legal — for high-risk AI deployments?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| An AI system's risk tier is known | Tier classification requires attorney assessment under the applicable framework; it is not self-evident |
| A use case is not on the prohibited list | Prohibited-use-case categories require attorney interpretation; do not assume clearance |
| No regulatory notification or conformity assessment is required | Requirements vary by jurisdiction, sector, and system type; must be confirmed |
| An AI system does not process personal data | Data flows in AI systems may not be obvious; privacy review is required |
| A third-party AI vendor's governance meets the group's standards | Vendor practices must be independently assessed against the group's checklist |
| Prior AI governance review covers a modified system | Material changes to training data, model architecture, or deployment scope require fresh review |
| Automated decisions do not have material individual effects | Effect analysis is a legal determination; must be attorney-confirmed |
| The applicable AI governance framework is finalized | AI governance rules are actively developing in many jurisdictions; confirm the current state |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

This profile is populated directly by the practice group. Work through each section with the supervising attorney, confirm all model-risk tiers, prohibited use cases, and escalation thresholds, and record the approved answers in place of the bracketed placeholders.

Do not include system names, model identifiers, vendor names, client-specific information, or privileged analysis in this profile. This is a configuration document, not a work-product file.
