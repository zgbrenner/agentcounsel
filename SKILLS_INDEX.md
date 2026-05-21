# AgentCounsel — Skills Index

A complete catalog of every skill in the library. The canonical source of truth is the `skills/` directory; this index is a map to it.

> All skills produce **draft legal work product for attorney review**. None of them provide legal advice. Read the `core/` operating rules before using any skill.

## How to use this index

- Browse by practice area in the table below, or use `WORKFLOW_ROUTER.md` to go from a task ("review this NDA") to the right skill.
- Open the skill's `SKILL.md`, gather the **Required Inputs**, follow the **Workflow**, and complete the **Attorney Verification Checklist**.

## All skills

| Practice Area | Skill | Path | Best Used For | Typical Inputs | Output Type |
|---|---|---|---|---|---|
| Legal Research | Legal Research Memo | `skills/legal-research/legal-research-memo/SKILL.md` | Structuring a research question into a reviewable memo | Research question, known facts, jurisdiction, any provided authority | Research memo draft |
| Litigation | Matter Intake | `skills/litigation/matter-intake/SKILL.md` | Capturing a new dispute matter in a structured form | Parties, dispute description, posture, known dates | Intake summary |
| Litigation | Litigation Chronology | `skills/litigation/litigation-chronology/SKILL.md` | Building a sourced factual timeline from documents | Documents, records, correspondence | Chronology table |
| Litigation | Demand Letter | `skills/litigation/demand-letter/SKILL.md` | Drafting a demand letter outline and draft | Facts, client position, relief sought | Demand letter draft |
| Litigation | Subpoena Triage | `skills/litigation/subpoena-triage/SKILL.md` | Triaging an incoming subpoena and its deadlines | The subpoena, recipient role | Triage summary |
| Litigation | Deposition Preparation | `skills/litigation/deposition-prep/SKILL.md` | Building a structured deposition outline from the record | Case theory, witness, documents | Deposition outline |
| Litigation | Legal Hold | `skills/litigation/legal-hold/SKILL.md` | Preparing a document-preservation (litigation hold) notice | Matter, preservation scope, custodians, systems | Legal hold notice |
| Litigation | Privilege Log Review | `skills/litigation/privilege-log-review/SKILL.md` | First-pass sorting of privilege log entries by confidence | Privilege log, forum and jurisdiction | Privilege log review report |
| Litigation | Claim Chart | `skills/litigation/claim-chart/SKILL.md` | Mapping patent claim limitations or cause-of-action elements against the evidence | Patent or pleaded claim, evidence, jurisdiction | Claim / element chart |
| Litigation | Brief Section Drafter | `skills/litigation/brief-section-drafter/SKILL.md` | Drafting a section of a litigation brief, cited and flagged for verification | Case theory, section type, record, house style | Brief section draft |
| Contracts | NDA Review | `skills/contracts/nda-review/SKILL.md` | Reviewing an NDA for risk and redline points | NDA text, client role | Risk review + redline points |
| Contracts | Contract Risk Review | `skills/contracts/contract-risk-review/SKILL.md` | Risk-reviewing a general commercial contract | Contract text, client role | Risk matrix + review |
| Contracts | Redline Summary | `skills/contracts/redline-summary/SKILL.md` | Summarizing changes between contract drafts | Two contract versions or tracked changes | Change summary table |
| Contracts | SOW Review | `skills/contracts/sow-review/SKILL.md` | Reviewing a statement of work against its MSA | SOW text, governing MSA | SOW review + issues table |
| Corporate | Board Minutes | `skills/corporate/board-minutes/SKILL.md` | Drafting minutes of a board or committee meeting | Meeting details, attendance, materials | Draft minutes |
| Corporate | Written Consent | `skills/corporate/written-consent/SKILL.md` | Drafting a board action by written consent | The action, signatories, effective date | Draft written consent |
| Corporate | Closing Checklist | `skills/corporate/closing-checklist/SKILL.md` | Building a transaction closing checklist and blocking analysis | Transaction agreement, deal context, diligence findings | Closing checklist |
| Corporate | Diligence Issue Extraction | `skills/corporate/diligence-issue-extraction/SKILL.md` | Extracting material issues from due-diligence documents | Target documents, deal context, materiality threshold | Diligence issues memo |
| Corporate | Material Contract Schedule | `skills/corporate/material-contract-schedule/SKILL.md` | Building a disclosure schedule of material contracts | "Material Contract" definition, contract data | Material contract schedule |
| Corporate | Entity Compliance Review | `skills/corporate/entity-compliance/SKILL.md` | Reviewing corporate-entity filing and good-standing status | Entity list, filing obligations | Entity compliance review |
| Employment | Termination Risk | `skills/employment/termination-risk/SKILL.md` | Organizing the facts around a proposed termination | Employee facts, stated reason, history | Risk checklist + factors |
| Employment | Severance Review | `skills/employment/severance-review/SKILL.md` | Reviewing a severance / separation agreement | Severance agreement, party served | Review + issues table |
| Employment | Employee Policy Review | `skills/employment/employee-policy-review/SKILL.md` | Reviewing a handbook or workplace policy for gaps | Policy or handbook text | Gap + issues table |
| Employment | Worker Classification | `skills/employment/worker-classification/SKILL.md` | Structuring the employee vs. contractor analysis for a proposed engagement | Proposed engagement facts, classification purpose, jurisdiction | Classification analysis memo |
| Employment | Hiring Review | `skills/employment/hiring-review/SKILL.md` | Reviewing an employment offer letter against the work jurisdiction | Offer letter, work location, role and pay | Hiring review memo |
| Employment | Wage and Hour Question Triage | `skills/employment/wage-hour-qa/SKILL.md` | Structuring a wage-and-hour question and routing rules to verified research | The question, jurisdiction, operative facts | Wage-and-hour analysis |
| Employment | Internal Investigation | `skills/employment/internal-investigation/SKILL.md` | Supporting an attorney-directed internal investigation and drafting the memo | Allegation, documents, interview notes | Investigation memorandum |
| Employment | Protected Leave Review | `skills/employment/protected-leave-review/SKILL.md` | Reviewing a protected-leave situation and flagging adverse-action exposure | Leave situation, procedural status, jurisdiction | Protected-leave review |
| Privacy | DPA Review | `skills/privacy/dpa-review/SKILL.md` | Reviewing a data processing agreement | DPA text, client role | Risk table + review |
| Privacy | DSAR Workflow | `skills/privacy/dsar-workflow/SKILL.md` | Triaging and structuring a data subject request | The request, requester details | Request-handling record |
| Privacy | Privacy Policy Gap Review | `skills/privacy/privacy-policy-gap-review/SKILL.md` | Checking a privacy policy against actual practice | Privacy policy, described practices | Gap table + recommendations |
| Privacy | Privacy Impact Assessment | `skills/privacy/pia-generation/SKILL.md` | Drafting a privacy impact assessment for a processing activity | Activity description, data categories, data flows | PIA draft |
| Product Legal | Launch Review | `skills/product-legal/launch-review/SKILL.md` | Pre-launch legal issue-spotting for a product or feature | Launch description, data, claims | Issues register + recommendation |
| Product Legal | Marketing Claims Review | `skills/product-legal/marketing-claims-review/SKILL.md` | Reviewing marketing copy for claim risk | Marketing or advertising copy | Claims register |
| Product Legal | Terms of Service Review | `skills/product-legal/terms-of-service-review/SKILL.md` | Reviewing terms of service / terms of use | Terms of service text | Review + issues table |
| Product Legal | AI Feature Review | `skills/product-legal/ai-feature-review/SKILL.md` | Issue-spotting an AI-powered product feature | Feature description, model and data details | AI issues register |
| Regulatory | Enforcement Risk Memo | `skills/regulatory/enforcement-risk-memo/SKILL.md` | Structuring an enforcement-exposure assessment | Conduct at issue, relevant rules, facts | Risk memo draft |
| Regulatory | Rule Change Summary | `skills/regulatory/rule-change-summary/SKILL.md` | Summarizing a rule change and its impact | Rule text or official document | Summary + impact table |
| Regulatory | Compliance Gap Matrix | `skills/regulatory/compliance-gap-matrix/SKILL.md` | Mapping requirements to controls and gaps | Requirement source, current controls | Gap matrix |
| AI Governance | AI Use Case Intake | `skills/ai-governance/ai-use-case-intake/SKILL.md` | Intaking and triaging a proposed AI use case | Use case description, model, data | Intake record + routing |
| AI Governance | AI Vendor Terms Review | `skills/ai-governance/ai-vendor-terms-review/SKILL.md` | Reviewing AI vendor or AI-service terms | Vendor terms text | Risk table + redline points |
| AI Governance | Model Risk Triage | `skills/ai-governance/model-risk-triage/SKILL.md` | Triaging the risk of an AI model or system | Model/system description, use, data | Risk register + tier |
| AI Governance | Employee AI Policy | `skills/ai-governance/employee-ai-policy/SKILL.md` | Reviewing an internal employee AI-use policy | Draft or existing AI policy | Gap + issues table |
| Intellectual Property | Trademark Clearance Triage | `skills/ip/trademark-clearance-triage/SKILL.md` | Preliminary triage of a proposed brand or name | Proposed mark, goods/services, markets | Triage summary + signal |
| Intellectual Property | DMCA Takedown | `skills/ip/dmca-takedown/SKILL.md` | Preparing or evaluating a takedown / counter-notice | The work, the allegedly infringing material | Draft notice / counter-notice |
| Intellectual Property | Open Source License Review | `skills/ip/open-source-license-review/SKILL.md` | Reviewing OSS license obligations and compatibility | Component / license inventory, distribution model | Obligations table + issues |
| Intellectual Property | Cease and Desist Response | `skills/ip/cease-and-desist-response/SKILL.md` | Triaging a received cease-and-desist letter into response options | The received letter, factual assessment | Response triage memo |
| Intellectual Property | Patent Freedom-to-Operate Triage | `skills/ip/fto-triage/SKILL.md` | First-pass triage of patent blocking risk for a product or feature | Product/feature description, jurisdictions, known patents | FTO triage memo |
| Intellectual Property | Invention Disclosure Intake | `skills/ip/invention-intake/SKILL.md` | Screening a proposed invention and flagging filing-deadline urgency | Invention disclosure, disclosure history | Invention screen + verdict |
| Intellectual Property | Infringement Triage | `skills/ip/infringement-triage/SKILL.md` | First-pass triage of a potential IP-infringement issue | IP right(s), party posture, evidence | Infringement triage memo |
| Setup | Contracts Cold-Start Interview | `skills/setup/contracts-cold-start-interview/SKILL.md` | Interviewing a contracts practice group to fill its practice profile | Access to a contracts attorney or designee | Filled practice profile draft |
| Setup | Litigation Cold-Start Interview | `skills/setup/litigation-cold-start-interview/SKILL.md` | Interviewing a litigation practice group to fill its practice profile | Access to a litigation attorney or designee | Filled practice profile draft |
| Setup | Privacy Cold-Start Interview | `skills/setup/privacy-cold-start-interview/SKILL.md` | Interviewing a privacy practice group to fill its practice profile | Access to a privacy attorney or designee | Filled practice profile draft |
| Setup | Corporate Cold-Start Interview | `skills/setup/corporate-cold-start-interview/SKILL.md` | Interviewing a corporate practice group to fill its practice profile | Access to a corporate attorney or designee | Filled practice profile draft |
| Legal Methodology | Red-Team Verifier | `skills/legal-methodology/red-team-verifier/SKILL.md` | A final quality-control pass on any legal output before it is relied upon | Any legal draft or AI output — memo, review, letter, filing, analysis | Verification findings report |
| Legal Methodology | Statutory Interpretation | `skills/legal-methodology/statutory-interpretation/SKILL.md` | Working through a statutory, regulatory, or contractual provision | Provision text, the interpretive question | Interpretation worksheet |
| Legal Methodology | Risk Assessment | `skills/legal-methodology/risk-assessment/SKILL.md` | Identifying, rating, and prioritizing legal risk | The situation, known facts, client posture | Prioritized risk register |
| Legal Methodology | Source Validation | `skills/legal-methodology/source-validation/SKILL.md` | Checking that cited sources and claims exist and are accurate | A draft and the sources it cites | Source validation table |

> **Before relying on any high-stakes legal output**, run `red-team-verifier` (`skills/legal-methodology/red-team-verifier/SKILL.md`) as a final quality-control pass. It adversarially stress-tests any memo, review, letter, filing, risk matrix, or analysis — the output of any skill in this index, or of another tool — for invented authority, unsupported claims, weak reasoning, jurisdiction and deadline gaps, and professional-responsibility issues. A PASS verdict does not replace attorney review.

## Business-stakeholder summary mode

Many commercial skills — across **contracts**, **product legal**, **privacy**, **regulatory**, **employment**, and **corporate** — offer an **optional Business Stakeholder Summary** in their Output Format. It is a plain-language layer for briefing non-lawyer decision-makers (product owners, deal leads, managers, founders, executives): a **Business Summary**, the **Decision Needed**, a **Recommended Ask**, a **Fallback Position**, and an **Escalation Needed?** call. Ask for it when the output is going to the business rather than to the supervising attorney. It is an addition to the skill's normal deliverable, never a replacement, and it does not change the attorney-review requirement. See `core/business-stakeholder-communication.md`.

## Practice areas at a glance

- **Legal Research** — turning questions into structured, verifiable memos.
- **Litigation** — intake, chronology, demand letters, subpoena triage, deposition preparation, legal holds, privilege-log review, claim charts, and brief drafting.
- **Contracts** — NDAs, commercial contracts, redlines, and statements of work.
- **Corporate** — board minutes, written consents, closing checklists, due-diligence issue extraction, material-contract schedules, and entity compliance.
- **Employment** — terminations, worker classification, hiring review, wage-and-hour questions, internal investigations, protected leave, severance, and workplace policies.
- **Privacy** — data processing agreements, impact assessments, data subject requests, and policy gaps.
- **Product Legal** — launch, marketing claims, terms of service, and AI features.
- **Regulatory** — enforcement risk, rule changes, and compliance gaps.
- **AI Governance** — AI use-case intake, vendor terms, model risk, and AI policies.
- **Intellectual Property** — trademark triage, infringement triage, cease-and-desist response, patent FTO triage, invention intake, DMCA, and open-source licensing.
- **Setup** — cold-start interviews that configure AgentCounsel for a practice group by filling in a practice profile.
- **Legal Methodology** — cross-cutting analytical disciplines: red-team verification, statutory interpretation, risk assessment, and source validation.

## Related references

- `practice-profiles/` — per-practice-area configuration profiles an agent loads alongside `core/` and a skill.
- `matter-workspaces/` — single-file scaffolds for organizing one specific matter.
- `COMMANDS.md` — slash-style command shorthands mapped to these skills.
- `skills/contracts/references/` — shared reference material for the contracts skills.
