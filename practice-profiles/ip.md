> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Intellectual Property

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Intellectual Property |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and forum in which this group regularly works. Agents will gate jurisdiction-specific analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Filing Jurisdictions | `[CONFIRM: countries and regions where the group regularly files for patent, trademark, or copyright protection]` |
| Secondary / Occasional Jurisdictions | `[CONFIRM: list or "none at this time"]` |
| Patent Filing Regimes | `[CONFIRM: national and regional patent systems the group uses — describe by region, not by body acronym]` |
| Trademark Filing Regimes | `[CONFIRM: national and regional trademark systems the group uses]` |
| Copyright Registration Jurisdictions | `[CONFIRM: jurisdictions where the group registers copyrights, or "registration not used"]` |
| IP Enforcement Jurisdictions | `[CONFIRM: jurisdictions where the group actively enforces or defends IP rights]` |
| International / Cross-Border IP Work | `[CONFIRM: yes/no; if yes, list international filing systems used — describe by function, not acronym]` |

**Guiding prompts for this section:**
- In which countries or regions does the client portfolio require active patent, trademark, or copyright coverage?
- Which international filing systems does the group use for multi-jurisdiction protection?
- In which jurisdictions does the group enforce IP rights or respond to infringement claims?
- Are there jurisdictions where the group regularly retains local counsel for prosecution or enforcement?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., product, R&D, engineering, brand, marketing, executive team]` |
| External Client Types | `[CONFIRM: e.g., technology companies, consumer brands, life sciences, creative industries]` |
| Team Composition | `[CONFIRM: patent attorneys, trademark attorneys, IP litigators, patent agents, paralegals, docket managers]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted work]` |
| Matter-Intake Process | `[CONFIRM: how IP matters reach the group — invention disclosures, clearance requests, enforcement notices]` |
| Local Counsel Network | `[CONFIRM: how the group manages local-counsel relationships for foreign filing — reference by system or process, not by firm name]` |

**Guiding prompts for this section:**
- Who is the primary R&D or product contact that routes invention disclosures to this group?
- How does the group manage its IP docket and renewal obligations?
- Does the group have a local-counsel network for foreign prosecution, and how is it managed?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Third-party IP clearance — potential conflict | `[CONFIRM: any clearance search result with an identified potential conflict]` | `[CONFIRM: role or name]` |
| Clearance threshold not met | `[CONFIRM: any search result falling below the group's minimum clearance standard]` | `[CONFIRM: role or name]` |
| Filing deadline at risk | Any IP filing deadline — never computed by the agent | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Prosecution disclaimer or claim amendment | `[CONFIRM: any prosecution decision that could affect claim scope or create prosecution history estoppel]` | `[CONFIRM: role or name]` |
| Inter partes or post-grant proceeding | `[CONFIRM: any challenge to the validity or registration of an IP right]` | `[CONFIRM: role or name]` |
| Infringement allegation received | `[CONFIRM: any cease-and-desist letter or infringement assertion]` | `[CONFIRM: role or name]` |
| Infringement allegation to send | `[CONFIRM: any decision to assert a third-party infringement — requires attorney sign-off]` | `[CONFIRM: role or name]` |
| IP assignment or exclusive license | `[CONFIRM: any agreement transferring or exclusively licensing core IP assets]` | `[CONFIRM: role or name]` |
| Open-source incorporation | `[CONFIRM: any incorporation of open-source code or content that may affect IP ownership or create copyleft obligations]` | `[CONFIRM: role or name]` |
| Any step outside the IP workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What is the minimum clearance standard — search scope, opinion threshold — below which the group will not clear a proposed mark, product name, or technology?
- Does the group have a defined rule for when a freedom-to-operate opinion is required before launch?
- What is the escalation path when a cease-and-desist letter is received?
- What level of prosecution decision requires partner sign-off?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., clearance search summary, trademark watch report, invention disclosure review, IP audit summary, claim-chart outline]` |
| Tone | `[CONFIRM: e.g., technical precision in patent work; plain brand-team language for trademark clearance summaries]` |
| Length convention | `[CONFIRM: e.g., trademark clearance summary ≤ 2 pages; full FTO analysis as needed]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-rating scheme | `[CONFIRM: e.g., clear / caution / conflict / block, or group's internal scheme]` |
| Privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"]` |

**Guiding prompts for this section:**
- What format does the group use for trademark clearance summaries presented to brand teams?
- How should freedom-to-operate analyses be structured — by claim element, by prior-art reference, or by product feature?
- Does the group use a standard risk-rating scheme for clearance results?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| IP filing strategy guidelines | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Clearance standard and threshold document | `[CONFIRM: file name and location]` | Governs all clearance decisions |
| Trademark clearance checklist | `[CONFIRM: file name and location]` | |
| Invention disclosure form | `[CONFIRM: file name and location]` | |
| IP docket management system | `[CONFIRM: system name only]` | Agent never computes deadlines; docket is authoritative |
| Open-source license review policy | `[CONFIRM: file name and location]` | Coordinate with product-legal profile |
| IP audit template | `[CONFIRM: file name and location]` | |
| Enforcement decision matrix | `[CONFIRM: file name and location]` | |

**Guiding prompts for this section:**
- Where does the group store its IP filing strategy guidelines and clearance threshold documents?
- Is there an authoritative docket management system, and who has authority to confirm deadlines from it?
- What document governs the group's enforcement decision process?

---

## Standard Positions / Playbooks

Record the group's default positions on common IP matters. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Filing strategy — patent | `[CONFIRM: e.g., provisional first, then PCT; national-phase strategy by primary markets]` | |
| Filing strategy — trademark | `[CONFIRM: e.g., file in primary market on intent-to-use or use basis; international extension based on business plan]` | `[verify jurisdiction]` |
| Clearance threshold — trademark | `[CONFIRM: e.g., identical and confusingly similar marks in the same and related classes; minimum search scope]` | |
| Freedom-to-operate analysis trigger | `[CONFIRM: e.g., required before any product launch in a jurisdiction with an identified patent risk]` | |
| Open-source incorporation — default posture | `[CONFIRM: e.g., review required for any copyleft-licensed code; permissive licenses reviewed on request]` | |
| Assignment vs. license default | `[CONFIRM: e.g., group's default position on assigning vs. licensing IP in transactions]` | |
| Work-for-hire and contractor IP assignment | `[CONFIRM: e.g., written assignment required from all contractors before work begins or before payment]` | `[verify jurisdiction]` |
| IP maintenance and renewal | `[CONFIRM: e.g., all maintenance fees and renewal decisions routed through the docket management system]` | `[deadline verification required]` |
| Enforcement decision threshold | `[CONFIRM: e.g., group's criteria for pursuing infringement — commercial significance, business impact, budget]` | |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- What is the group's standard patent filing strategy — provisional first, direct national, international?
- What minimum clearance scope does the group apply for trademark searches?
- Does the group have a standing rule on written IP assignment from contractors?
- What criteria govern the group's decision to pursue or respond to an infringement claim?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| Trademark or copyright clearance summary | `[CONFIRM: e.g., supervising attorney]` | All; before use by brand or product team |
| Freedom-to-operate analysis | `[CONFIRM: role]` | All; no exceptions; before any product launch decision |
| Invention disclosure review | `[CONFIRM: role]` | Before filing decision is made |
| Cease-and-desist letter (inbound response) | `[CONFIRM: role]` | Before any response is sent |
| Cease-and-desist letter (outbound draft) | Partner-level review | Before transmission |
| IP assignment or exclusive license agreement | `[CONFIRM: role]` | Before execution |
| Post-grant or inter partes proceeding strategy | Partner-level review | All |
| Any output relating to a deadline | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` | All filing, maintenance, and response deadlines |

**Guiding prompts for this section:**
- Is there a tiered review structure for clearance opinions based on transaction size or strategic importance?
- Who must approve an FTO analysis before a product launches?
- Does the group require a second attorney to review any outbound enforcement letter?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| A proposed mark or product name is clear to use | Clearance requires a defined search; absence from the agent's knowledge is not clearance |
| A filing deadline is known or has been met | All IP filing and maintenance deadlines are attorney-verified from the docket management system |
| An IP right is valid and in force | IP rights require maintenance, renewal, and may be subject to challenge; status must be confirmed |
| Work created by a contractor is owned by the client | Written assignment is required; absence of a signed agreement means ownership is uncertain |
| Open-source code can be incorporated without restriction | License terms vary materially; must be reviewed and confirmed |
| A prior FTO analysis covers a modified product | Changes to product scope or new prior art may affect the analysis; confirm with attorney |
| An IP assignment conveys all rights needed | Assignment scope must be read from the actual document; do not assume breadth |
| No third-party rights are implicated | Background IP, licensed-in technology, and third-party content must be identified and confirmed |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

This profile is populated directly by the practice group. Work through each section with the supervising attorney, confirm all filing strategies, clearance thresholds, and enforcement criteria, and record the approved answers in place of the bracketed placeholders.

Do not include application numbers, registration numbers, client trade secrets, or privileged analysis in this profile. This is a configuration document, not a work-product file.
