> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Product Legal

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Product Legal |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and forum in which this group regularly works. Agents will gate jurisdiction-specific analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Launch Jurisdictions | `[CONFIRM: countries and states/regions where the group approves product launches]` |
| Secondary / Phased Jurisdictions | `[CONFIRM: jurisdictions added in subsequent launch phases or "none at this time"]` |
| Regulatory Bodies Monitored | `[CONFIRM: consumer protection, product safety, digital-markets, or other regulators — describe by jurisdiction, not by acronym]` |
| Sector-Specific Regulatory Frameworks | `[CONFIRM: yes/no; if yes, describe applicable sectors, e.g., financial products, health tools, children's services]` |
| International / Cross-Border Product Distribution | `[CONFIRM: yes/no; if yes, list regions and any import/export considerations]` |

**Guiding prompts for this section:**
- In which jurisdictions must the group provide legal clearance before a product or feature launches?
- Which regulatory bodies does the group monitor for product-affecting guidance?
- Are there sector-specific frameworks — financial products, medical devices, children's platforms — that require specialized legal review before launch?
- Does the group manage launches in phases, and does jurisdiction coverage expand over time?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Field |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., product management, engineering, design, marketing, growth]` |
| External Client Types | `[CONFIRM: e.g., product-company legal departments, technology startups, platform operators]` |
| Team Composition | `[CONFIRM: product-legal counsel, associates, privacy counsel, IP counsel, regulatory specialists]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how product-legal reviews reach the group — design reviews, launch tickets, escalations from product managers]` |
| Relationship to Other Practice Groups | `[CONFIRM: how product-legal coordinates with privacy, IP, employment, and regulatory practices]` |

**Guiding prompts for this section:**
- Who is the primary product-management or engineering contact that routes matters to this group?
- How early in the product development cycle does this group typically engage?
- How does the group coordinate with privacy, IP, and regulatory counsel on launches?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Launch-gate criteria not met | `[CONFIRM: any product or feature that has not cleared all launch-gate requirements]` | `[CONFIRM: role or name]` |
| New data processing or collection | `[CONFIRM: any feature that collects, processes, or shares new categories of personal data]` | `[CONFIRM: role or name — coordinate with privacy practice]` |
| IP clearance not confirmed | `[CONFIRM: any feature using third-party content, marks, or technology without confirmed clearance]` | `[CONFIRM: role or name — coordinate with IP practice]` |
| Sector-specific regulatory trigger | `[CONFIRM: any product feature touching financial services, health, children, or other regulated sectors]` | `[CONFIRM: role or name — coordinate with regulatory practice]` |
| Consumer-facing terms or disclosures | `[CONFIRM: any change to terms of service, privacy notice, or material-facing disclosures]` | `[CONFIRM: role or name]` |
| Advertising or promotional content | `[CONFIRM: any advertising claim that may require substantiation or regulatory review]` | `[CONFIRM: role or name]` |
| Open-source or third-party code | `[CONFIRM: any incorporation of open-source or third-party technology requiring license review]` | `[CONFIRM: role or name — coordinate with IP practice]` |
| Deprecation or material change | `[CONFIRM: any removal or material change to an existing feature that created user expectations]` | `[CONFIRM: role or name]` |
| Any step outside the product-legal workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What are the mandatory legal gates a product or feature must clear before launch?
- Which product feature types automatically require privacy review, IP clearance, or regulatory sign-off?
- Does the group have a standing rule on when terms-of-service updates require legal review?
- What is the escalation path when a product feature does not fit any existing launch-gate category?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., launch-gate checklist, legal-risk summary, issues list for product managers, terms-of-service redline]` |
| Tone | `[CONFIRM: e.g., plain product-team language for launch gates; formal legal prose for external terms and regulatory responses]` |
| Length convention | `[CONFIRM: e.g., product-facing summary ≤ 1 page; full risk memo as needed]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Launch-gate status format | `[CONFIRM: e.g., color-coded status, pass/hold/escalate labels, or checklist format]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- How does the group communicate launch-gate status to product teams — a green/yellow/red system, a checklist, a memo?
- What level of detail do product managers need in a legal-risk summary?
- Does the group produce public-facing documents (terms of service, privacy notices) or only internal work product?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| Product launch-gate criteria | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Launch-review checklist template | `[CONFIRM: file name and location]` | |
| Terms-of-service template | `[CONFIRM: file name and location]` | |
| Privacy notice template | `[CONFIRM: file name and location]` | |
| Open-source license review policy | `[CONFIRM: file name and location]` | Coordinate with IP practice |
| Advertising-claims clearance procedure | `[CONFIRM: file name and location]` | |
| Product risk-rating framework | `[CONFIRM: file name and location]` | |
| Known regulatory guidance tracker | `[CONFIRM: file name and location]` | Agent does not cite specific guidance; attorney verifies |

**Guiding prompts for this section:**
- Where does the group store its current launch-gate criteria document?
- Is there an authoritative product risk-rating framework agents should align with?
- What document governs open-source license review for new product features?

---

## Standard Positions / Playbooks

Record the group's default positions on common product-legal matters. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Launch-gate — all gates must clear | `[CONFIRM: e.g., all required gates must have attorney sign-off before any launch]` | |
| New data collection — default posture | `[CONFIRM: e.g., privacy review required before any new personal data category is collected]` | Coordinate with privacy profile |
| Third-party content — default posture | `[CONFIRM: e.g., IP clearance required before any third-party content is incorporated into product]` | Coordinate with IP profile |
| Consumer-facing terms changes | `[CONFIRM: e.g., any material change to user-facing terms requires legal review before publication]` | |
| Advertising claims — default posture | `[CONFIRM: e.g., substantiation required for all product performance claims]` | |
| Children's product features | `[CONFIRM: e.g., dedicated regulatory review required for any feature available to users under a specified age]` | `[verify jurisdiction]` |
| Sector-specific product features | `[CONFIRM: group's default routing to regulatory practice for sector-specific features]` | |
| Deprecation notice | `[CONFIRM: e.g., minimum notice period to users before material feature removal]` | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- Are all launch gates mandatory, or can some be waived with documented attorney approval?
- What is the group's default position on collecting new categories of personal data in a feature?
- How does the group handle product features that span multiple practice areas — who coordinates?
- What is the minimum user-notice period the group requires before a material feature is deprecated?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Launch-gate clearance | `[CONFIRM: e.g., supervising attorney]` | All; no exceptions |
| Terms-of-service or privacy-notice draft or update | `[CONFIRM: role]` | Before publication |
| Advertising-claims clearance memo | `[CONFIRM: role]` | Before any campaign goes live |
| Product risk memo | `[CONFIRM: role]` | Before presentation to product or executive team |
| Open-source license review | `[CONFIRM: role — coordinate with IP practice]` | Before code is incorporated |
| Any output touching sector-specific features | `[CONFIRM: role with sector expertise]` | Always |
| Regulatory inquiry or consumer complaint response | Partner-level review | All; no exceptions |

**Guiding prompts for this section:**
- Is launch-gate clearance a sole-attorney sign-off, or does it require cross-practice approval?
- Who must approve public-facing terms and disclosures before they are published?
- Does the group require a second review for any sector-regulated product feature?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| All launch gates have been cleared | Each gate must have documented attorney sign-off; presence in the review queue is not clearance |
| A prior privacy review covers a modified feature | Changes to data flows or processing activities require a fresh review |
| IP clearance for one use extends to all uses | IP clearance is use-specific; scope must be confirmed for each application |
| Regulatory requirements in a new jurisdiction match existing markets | Requirements vary materially by jurisdiction; `[verify jurisdiction]` |
| Sector-specific requirements do not apply | Sector applicability is a legal determination; must be attorney-confirmed |
| Prior terms of service or privacy notice remain current | User-facing documents require periodic review; confirm the current version is authoritative |
| A third-party component's license is known | License terms must be read and confirmed; do not rely on descriptions |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

This profile is populated directly by the practice group. Work through each section with the supervising attorney, confirm all positions, thresholds, and launch-gate criteria, and record the approved answers in place of the bracketed placeholders.

Do not include product names, unreleased feature details, client-specific information, or privileged analysis in this profile. This is a configuration document, not a work-product file.
