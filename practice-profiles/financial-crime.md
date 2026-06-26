> **Internal practice-group configuration reference. This is not legal work product and is not legal advice.** This profile configures AI agent behavior for this practice group. It must be maintained and approved by a supervising attorney before use. This file must NOT contain privileged or client-sensitive facts. Source-of-truth documents are referenced by name and location only — never pasted in.

# Practice Profile: Financial Crime

## Profile Information

| Field | Value |
|---|---|
| Practice Group | Financial Crime (AML / sanctions / KYC) |
| Profile Owner | `[CONFIRM: name and title of profile owner]` |
| Approving Attorney | `[CONFIRM: name and bar number of approving attorney]` |
| Last Reviewed Date | `[CONFIRM: date of last attorney review]` |
| Version | `[CONFIRM: version number, e.g., 1.0]` |

---

## Jurisdictions

Identify every jurisdiction, governing-law regime, and regulatory forum in which this group regularly works. Agents will gate jurisdiction-specific analysis on this list and flag anything outside it for attorney escalation.

| Field | Value |
|---|---|
| Primary Financial-Crime Jurisdictions | `[CONFIRM: countries, states, or regions where the regulated entity operates and the group advises]` |
| Secondary / Occasional Jurisdictions | `[CONFIRM: list or "none at this time"]` |
| Supervisory / Regulatory Bodies Monitored | `[CONFIRM: describe by jurisdiction and function — do not use acronyms; e.g., "national financial intelligence unit," "national sanctions authority," "prudential banking supervisor"]` |
| Sanctions Regimes In Scope | `[CONFIRM: describe by issuing-authority function the regimes the group screens against; reference the firm's sanctions-lists source-of-truth document for the authoritative list]` `[VERIFY current law / jurisdiction]` |
| Applicable AML / Counter-Financing Frameworks | `[CONFIRM: describe the AML / counter-terrorist-financing regimes that govern the entity by jurisdiction and function — keep generic and confirm specifics]` `[VERIFY current law / jurisdiction]` |
| Cross-Border / Multi-Jurisdictional Exposure | `[CONFIRM: yes/no; if yes, list the jurisdictions whose financial-crime regimes may apply and any conflict-of-law coordination framework]` |

**Guiding prompts for this section:**
- In which jurisdictions is the regulated entity licensed or operating, and which financial-crime regimes therefore apply?
- Which supervisory bodies and financial intelligence units does the group monitor for new rules, guidance, and enforcement priorities?
- Which sanctions regimes does the entity screen against, and where is the authoritative list of those regimes maintained?
- Does any customer base, payment flow, or counterparty relationship create exposure to a financial-crime regime outside the primary jurisdictions?

---

## Client / Team Context

Describe who this group serves and how it is organized. Agents use this section to understand escalation paths and supervision structure.

| Field | Value |
|---|---|
| Internal Clients Served | `[CONFIRM: e.g., compliance, the financial-crime / AML function, onboarding operations, risk, business lines, executive team]` |
| External Client Types | `[CONFIRM: e.g., regulated financial institutions, payment firms, investment managers, the entity's own AML program]` |
| Team Composition | `[CONFIRM: financial-crime counsel, AML / sanctions specialists, onboarding and screening analysts, the BSA/AML officer or equivalent, paralegals]` |
| Supervising Attorney(s) | `[CONFIRM: name(s) with oversight responsibility for AI-assisted financial-crime work]` |
| Relationship to the AML / Compliance Function | `[CONFIRM: relationship between this group and the entity's designated AML / financial-crime compliance officer — reference by function name, not personal names]` |
| Matter-Intake Process | `[CONFIRM: how financial-crime matters reach the group — onboarding referrals, screening alerts, transaction-monitoring escalations, regulatory inquiries]` |

**Guiding prompts for this section:**
- Who is the designated AML / financial-crime compliance officer, and how do matters route between that function and this group?
- At what stage does the group engage — onboarding, alert adjudication, suspicious-activity assessment, or only on regulatory inquiry?
- How does the group coordinate with onboarding and screening operations on KYC and alert-disposition work?

---

## Escalation Thresholds

Define the conditions under which an agent must stop autonomous work and route to a human reviewer. Agents treat these thresholds as hard stops.

| Trigger | Threshold / Description | Route To |
|---|---|---|
| Potential or confirmed sanctions match | `[CONFIRM: any sanctions hit classified as a possible or likely true match — escalate to compliance and counsel; do not clear]` | `[CONFIRM: role or name — halt processing of the party]` |
| Politically exposed person (PEP) identified | `[CONFIRM: any party classified as a possible or likely PEP match]` | `[CONFIRM: role or name]` |
| Adverse-media hit of financial-crime relevance | `[CONFIRM: any adverse-media result implicating fraud, corruption, money laundering, or terrorist financing]` | `[CONFIRM: role or name]` |
| Suspicious-activity indicator / potential reporting trigger | `[CONFIRM: any indicator that may give rise to a suspicious-activity or transaction report — never assessed or filed by the agent]` | `[CRITICAL — ATTORNEY / COMPLIANCE TO ASSESS]` |
| Mandatory reporting deadline | Any financial-crime reporting deadline — never computed by the agent | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` |
| Enhanced-due-diligence trigger | `[CONFIRM: any high-risk factor — jurisdiction, ownership opacity, PEP exposure, source-of-funds concern — requiring EDD before onboarding proceeds]` | `[CONFIRM: role or name]` |
| Beneficial-ownership opacity | `[CONFIRM: any case where the ownership or control chain cannot be resolved to the firm's standard]` | `[CONFIRM: role or name]` |
| Regulatory inquiry or examination on a financial-crime matter | `[CONFIRM: any formal or informal contact from a supervisor or financial intelligence unit — escalate immediately]` | `[CONFIRM: role or name]` |
| Customer-acceptance or decline decision | `[CONFIRM: the agent recommends but never decides acceptance, decline, or final risk rating]` | `[CONFIRM: role or name]` |
| Any step outside the financial-crime workflow | `[CONFIRM: agent flags and pauses rather than improvising]` | `[CONFIRM: role or name]` |

**Guiding prompts for this section:**
- What is the group's escalation path the moment a possible sanctions match is identified, and at what point is processing of the party halted?
- Which factors automatically trigger enhanced due diligence before onboarding can proceed?
- How is a potential suspicious-activity indicator routed for human assessment, given that the agent never assesses or files a report?
- Who decides customer acceptance, decline, and the final risk rating, and how is that decision recorded?

---

## Preferred Output Style

Specify the format, tone, and length conventions agents must follow when producing deliverables for this group.

| Preference | Setting |
|---|---|
| Deliverable format | `[CONFIRM: e.g., KYC onboarding review file, sanctions / PEP / adverse-media screening adjudication, alert-disposition memo, enhanced-due-diligence summary]` |
| Tone | `[CONFIRM: e.g., precise operational prose for the compliance function; formal legal prose for regulatory-facing or counsel memos]` |
| Length convention | `[CONFIRM: e.g., screening adjudication and onboarding file as long as the alert or packet requires; internal summary ≤ 2 pages]` |
| Heading style | `[CONFIRM: e.g., numbered sections, H2/H3 Markdown]` |
| Risk-rating format | `[CONFIRM: e.g., low / medium / high aligned with the firm's KYC/AML risk-rating methodology]` |
| Confidentiality / privilege designation line | `[CONFIRM: e.g., "Privileged and Confidential — Attorney Work Product"; note that party-identifying data must not enter reusable templates]` |

**Guiding prompts for this section:**
- What format does the group use for a KYC onboarding review file and for a screening adjudication?
- How are operational alert-disposition outputs distinguished from attorney-work-product memos?
- What risk-rating scale and labels does the firm's methodology use?

---

## Source-of-Truth Documents

List the authoritative playbooks, templates, and reference materials this group uses. Reference by name and location only. Do not paste content here.

| Document | Location / Path | Notes |
|---|---|---|
| KYC/AML rules grid or CDD policy | `[CONFIRM: file name and location]` | Trusted source for all rule outcomes; agent never constructs rules from memory |
| Risk-rating methodology | `[CONFIRM: file name and location]` | Defines the risk factors and the rating scale |
| Sanctions / PEP / adverse-media screening policy | `[CONFIRM: file name and location]` | Sets match thresholds, false-positive criteria, and alert-disposition rules |
| Sanctions-lists and regimes reference | `[CONFIRM: file name or system name]` | Authoritative list of regimes screened against; `[VERIFY current law / jurisdiction]` |
| High-risk jurisdiction list | `[CONFIRM: file name and location]` | `[CONFIRM: version or last-updated date]` |
| Required-document matrix by customer type | `[CONFIRM: file name and location]` | Drives the required-document check |
| Enhanced-due-diligence (EDD) protocol | `[CONFIRM: file name and location]` | |
| Suspicious-activity escalation and reporting protocol | `[CONFIRM: file name or system name]` | Agent never assesses or files reports; routes to the named function |
| Mandatory reporting calendar | `[CONFIRM: file name or system name]` | Agent never computes deadlines; attorney / compliance verifies |

**Guiding prompts for this section:**
- Where does the group store its KYC/AML rules grid and CDD policy, and which version is authoritative?
- Where is the authoritative list of sanctions regimes screened against maintained, and how often is it updated?
- What protocol governs how a suspicious-activity indicator is escalated for human assessment and any reporting decision?

---

## Standard Positions / Playbooks

Record the group's default positions on common financial-crime matters. These are starting positions — an agent uses them to flag deviations but always defers final judgment to an attorney.

| Topic | Group's Default Position | Notes / Conditions |
|---|---|---|
| Sanctions match — default disposition | `[CONFIRM: e.g., any possible or likely true sanctions match is escalated to compliance and counsel and never cleared by an analyst alone]` | |
| PEP identification — default treatment | `[CONFIRM: e.g., a confirmed PEP triggers enhanced due diligence and senior sign-off]` | `[verify jurisdiction]` |
| Customer risk rating | `[CONFIRM: who assigns the rating, the scale used, and the factors that drive it]` | Agent proposes; the compliance officer and counsel decide |
| Enhanced-due-diligence trigger | `[CONFIRM: e.g., high-risk jurisdiction, PEP exposure, opaque ownership, or unclear source of funds triggers EDD before onboarding]` | `[verify jurisdiction]` |
| Beneficial-ownership resolution | `[CONFIRM: e.g., the full ownership and control chain must be resolved to the firm's standard before clearance; opacity escalates]` | |
| Source of funds / source of wealth | `[CONFIRM: e.g., evidence required to be adequate for the assessed risk level before clearance]` | |
| Screening cadence | `[CONFIRM: e.g., screening at onboarding and on a defined ongoing-monitoring frequency]` | |
| Suspicious-activity indicators | `[CONFIRM: e.g., any potential reporting indicator is escalated for human assessment; the agent never assesses or files]` | `[CRITICAL — ATTORNEY / COMPLIANCE TO ASSESS]` |
| Reporting deadlines | `[CONFIRM: e.g., all mandatory reporting deadlines are tracked in the authoritative calendar; agent never computes]` | `[deadline verification required]` |
| `[CONFIRM: additional standard position]` | `[CONFIRM: group's default]` | |

**Guiding prompts for this section:**
- What is the group's standing position when a possible sanctions match is identified — and who may clear it?
- Which factors automatically place a customer into enhanced due diligence?
- To what standard must beneficial ownership and control be resolved before a customer can be cleared?
- How does the group handle a potential suspicious-activity indicator, given that assessment and any filing are human tasks?

---

## Attorney Review Requirements

Specify what must be reviewed by a qualified attorney before any deliverable produced with this profile is used, sent, or relied upon.

| Deliverable Type | Required Reviewer | Conditions |
|---|---|---|
| KYC onboarding review file | `[CONFIRM: e.g., supervising attorney and the compliance function]` | All; before any customer-acceptance decision |
| Sanctions / PEP / adverse-media screening adjudication | `[CONFIRM: role — compliance and counsel]` | All; no sanctions match cleared without that review |
| Customer risk rating | `[CONFIRM: role]` | Decision made by compliance and counsel, not by the draft |
| Enhanced-due-diligence summary | `[CONFIRM: role]` | Before onboarding proceeds for any high-risk customer |
| Suspicious-activity assessment | `[CRITICAL — ATTORNEY / COMPLIANCE TO ASSESS]` | Any potential reporting indicator; assessment and filing are human tasks |
| Regulatory submission or response on a financial-crime matter | Partner-level review | All; no exceptions; before any submission |
| Any output relating to a deadline | `[CRITICAL — ATTORNEY TO VERIFY DEADLINE]` | All reporting and response deadlines |

**Guiding prompts for this section:**
- Does every onboarding file require both compliance and attorney sign-off, or only those above a defined risk level?
- Who must approve clearance of a sanctions or PEP match before a party is processed?
- Is there a separate, escalated review for any matter touching a potential suspicious-activity report?

---

## Prohibited Assumptions

List what an agent must never assume and must always confirm with a human before proceeding.

| Item | Why It Cannot Be Assumed |
|---|---|
| A screening hit is a false positive | False-positive determination requires identifier verification against the firm's policy; do not default-clear |
| A party "is sanctioned," "is a PEP," or "is clear" | These are dispositions for the compliance function and counsel, not agent conclusions; classify confidence and route |
| No suspicious-activity report is required | Suspicious-activity assessment and any filing are legal / compliance judgments; never assessed or filed by the agent |
| A reporting or response deadline is known | Financial-crime deadlines are jurisdiction- and regime-specific; `[deadline verification required]` |
| The applicable AML or sanctions framework is current | Frameworks and list contents change frequently; `[VERIFY current law / jurisdiction]` |
| The beneficial-ownership chain is fully resolved | Ownership and control may be opaque or layered; resolution to the firm's standard must be confirmed |
| Source of funds / source of wealth is adequately evidenced | Adequacy is risk-dependent and a human judgment; must be confirmed for the assessed risk level |
| A customer's risk rating is known | The rating is a proposed workflow assessment; the decision belongs to compliance and counsel |
| Enhanced due diligence is not required | EDD triggers vary by jurisdiction, product, and risk factor; must be confirmed |
| Every named party has been screened | Unscreened parties must be flagged as screening-pending, never assumed clear |
| `[CONFIRM: any additional group-specific prohibited assumption]` | `[CONFIRM: reason]` |

---

## How to Populate This Profile

Complete every bracketed placeholder with information specific to this practice group. Have a supervising attorney review and approve the completed profile before it is loaded alongside any skill.

This profile is populated directly by the practice group. Work through each section with the supervising attorney and the designated AML / financial-crime compliance officer, confirm all monitored supervisors, sanctions regimes, screening thresholds, and escalation paths against the firm's current policies, and record the approved answers in place of the bracketed placeholders. Keep the specifics of any applicable AML, sanctions, or reporting framework flagged for verification — financial-crime rules and list contents change frequently and are jurisdiction-specific.

Do not include client names, party identifiers, account or transaction details, matter numbers, confidential facts, or privileged analysis in this profile. This is a configuration document, not a work-product file.
