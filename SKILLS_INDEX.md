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
| Employment | Termination Risk | `skills/employment/termination-risk/SKILL.md` | Organizing the facts around a proposed termination | Employee facts, stated reason, history | Risk checklist + factors |
| Employment | Severance Review | `skills/employment/severance-review/SKILL.md` | Reviewing a severance / separation agreement | Severance agreement, party served | Review + issues table |
| Employment | Employee Policy Review | `skills/employment/employee-policy-review/SKILL.md` | Reviewing a handbook or workplace policy for gaps | Policy or handbook text | Gap + issues table |
| Employment | Worker Classification | `skills/employment/worker-classification/SKILL.md` | Structuring the employee vs. contractor analysis for a proposed engagement | Proposed engagement facts, classification purpose, jurisdiction | Classification analysis memo |
| Employment | Hiring Review | `skills/employment/hiring-review/SKILL.md` | Reviewing an employment offer letter against the work jurisdiction | Offer letter, work location, role and pay | Hiring review memo |
| Employment | Wage and Hour Question Triage | `skills/employment/wage-hour-qa/SKILL.md` | Structuring a wage-and-hour question and routing rules to verified research | The question, jurisdiction, operative facts | Wage-and-hour analysis |
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

## Practice areas at a glance

- **Legal Research** — turning questions into structured, verifiable memos.
- **Litigation** — intake, chronology, demand letters, subpoena triage, deposition preparation, legal holds, privilege-log review, claim charts, and brief drafting.
- **Contracts** — NDAs, commercial contracts, redlines, and statements of work.
- **Employment** — terminations, worker classification, hiring review, wage-and-hour questions, severance, and workplace policies.
- **Privacy** — data processing agreements, impact assessments, data subject requests, and policy gaps.
- **Product Legal** — launch, marketing claims, terms of service, and AI features.
- **Regulatory** — enforcement risk, rule changes, and compliance gaps.
- **AI Governance** — AI use-case intake, vendor terms, model risk, and AI policies.
- **Intellectual Property** — trademark triage, cease-and-desist response, patent FTO triage, invention intake, DMCA, and open-source licensing.
