# AgentCounsel — Command Router

Slash-style command shorthands that map to AgentCounsel skills. Commands are a **convenience layer** over `WORKFLOW_ROUTER.md` and `SKILLS_INDEX.md`: a short, memorable name for "run this skill." They add no runtime, no backend, and no vendor dependency — a command is just a pointer to a canonical `SKILL.md`.

> Every command runs a skill that produces **draft legal work product for attorney review**. None of them provide legal advice. Read the `core/` operating rules before running any skill.

## How commands work

1. A command has the form `/<namespace>:<name>` — for example `/contracts:nda`.
2. The namespace is the practice area; the name is the specific workflow.
3. To run a command, open the **Skill** path in its row, gather the **Required inputs**, follow the skill's Workflow, and complete its Attorney Verification Checklist.
4. The **Related** column lists adjacent commands to consider when a task spans more than one skill.
5. If no command fits, do not improvise — see "When nothing matches" in `WORKFLOW_ROUTER.md`.

A command never overrides a skill. The canonical source of truth is the `skills/` directory; this file only maps names to it.

## Contracts

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/contracts:nda` | `skills/contracts/nda-review/SKILL.md` | "review this NDA", "check this confidentiality agreement" | NDA text, client role, transaction context | Triage rating, risk table, prioritized redline points | `/contracts:review`, `/contracts:redline-summary` |
| `/contracts:review` | `skills/contracts/contract-risk-review/SKILL.md` | "review this contract", "flag the risks in this MSA" | Full contract text, client role, business context | Risk matrix and prioritized issue list | `/contracts:nda`, `/contracts:sow`, `/privacy:dpa` |
| `/contracts:redline-summary` | `skills/contracts/redline-summary/SKILL.md` | "what changed between these drafts", "summarize this redline" | Two contract versions or tracked changes | Change summary table | `/contracts:review` |
| `/contracts:sow` | `skills/contracts/sow-review/SKILL.md` | "review this SOW", "does this SOW match the MSA" | SOW text, governing MSA | SOW review and issues table | `/contracts:review` |
| `/contracts:vendor-status` | `skills/contracts/vendor-agreement-status/SKILL.md` | "vendor agreement status", "what agreements do we have with this vendor" | Vendor identity, agreement records, relationship context | Vendor agreement status report | `/contracts:review`, `/privacy:dpa` |

## Litigation

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/litigation:intake` | `skills/litigation/matter-intake/SKILL.md` | "open a new matter", "intake this dispute" | Client identity and role, dispute description | Structured intake summary | `/litigation:chronology`, `/litigation:legal-hold` |
| `/litigation:chronology` | `skills/litigation/litigation-chronology/SKILL.md` | "build a timeline", "chronology from these documents" | Documents, records, correspondence | Sourced chronology table | `/litigation:intake` |
| `/litigation:demand` | `skills/litigation/demand-letter/SKILL.md` | "draft a demand letter", "send an outbound demand" | Facts, client position, relief sought | Demand letter outline and draft | `/ip:cease-desist` |
| `/litigation:subpoena` | `skills/litigation/subpoena-triage/SKILL.md` | "we received a subpoena", "what to do with this subpoena" | The subpoena, recipient role | Triage summary with deadline flags | `/litigation:legal-hold` |
| `/litigation:deposition-prep` | `skills/litigation/deposition-prep/SKILL.md` | "prepare for a deposition", "build a deposition outline" | Case theory, witness, documents | Deposition outline | `/litigation:chronology` |
| `/litigation:legal-hold` | `skills/litigation/legal-hold/SKILL.md` | "issue a litigation hold", "preserve documents" | Matter, preservation scope, custodians, systems | Legal hold notice | `/litigation:intake` |
| `/litigation:privilege-log` | `skills/litigation/privilege-log-review/SKILL.md` | "review our privilege log" | Privilege log, forum and jurisdiction | Privilege log review report | `/method:source-validation` |
| `/litigation:claim-chart` | `skills/litigation/claim-chart/SKILL.md` | "build a claim chart", "map claim elements to evidence" | Patent or pleaded claim, evidence, jurisdiction | Claim / element chart | `/ip:infringement` |
| `/litigation:brief` | `skills/litigation/brief-section-drafter/SKILL.md` | "draft a section of a brief" | Case theory, section type, record, house style | Brief section draft | `/research:memo`, `/method:source-validation` |

## Legal Research

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/research:memo` | `skills/legal-research/legal-research-memo/SKILL.md` | "research this question", "write a research memo" | Research question, known facts, jurisdiction, any authority | Research memo draft | `/method:statutory-interpretation`, `/method:source-validation` |

## Corporate

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/corporate:board-minutes` | `skills/corporate/board-minutes/SKILL.md` | "draft board minutes" | Meeting details, attendance, materials | Draft minutes | `/corporate:written-consent` |
| `/corporate:written-consent` | `skills/corporate/written-consent/SKILL.md` | "draft a written consent", "action by written consent" | The action, signatories, effective date | Draft written consent | `/corporate:board-minutes` |
| `/corporate:closing-checklist` | `skills/corporate/closing-checklist/SKILL.md` | "build a closing checklist" | Transaction agreement, deal context, diligence findings | Closing checklist | `/corporate:diligence` |
| `/corporate:diligence` | `skills/corporate/diligence-issue-extraction/SKILL.md` | "pull issues from these diligence documents" | Target documents, deal context, materiality threshold | Diligence issues memo | `/corporate:material-contracts` |
| `/corporate:material-contracts` | `skills/corporate/material-contract-schedule/SKILL.md` | "build the material contracts schedule" | "Material Contract" definition, contract data | Material contract schedule | `/corporate:diligence` |
| `/corporate:entity-compliance` | `skills/corporate/entity-compliance/SKILL.md` | "review our entities' good-standing status" | Entity list, filing obligations | Entity compliance review | `/regulatory:gap-matrix` |

## Real Estate

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/real-estate:lease-abstract` | `skills/real-estate/lease-abstract/SKILL.md` | "abstract this lease", "pull the key lease terms" | The lease document, property type, party role | Source-cited lease abstract and critical-dates table | `/real-estate:amendment-reconciliation`, `/real-estate:lease-review` |
| `/real-estate:amendment-reconciliation` | `skills/real-estate/lease-amendment-reconciliation/SKILL.md` | "reconcile the lease and amendments", "current controlling terms" | Base lease, all amendments and side letters, party role | Current-controlling-term table with source references | `/real-estate:lease-abstract` |
| `/real-estate:lease-review` | `skills/real-estate/commercial-lease-review/SKILL.md` | "review this commercial lease" | The lease, party perspective, property type | Risk matrix and prioritized issue list | `/real-estate:lease-abstract`, `/contracts:review` |
| `/real-estate:psa-review` | `skills/real-estate/psa-review/SKILL.md` | "review this purchase and sale agreement", "review this PSA" | The PSA, party perspective, property type | Risk matrix and prioritized issue list | `/real-estate:diligence-checklist`, `/real-estate:closing-tracker` |
| `/real-estate:title-survey-tracker` | `skills/real-estate/title-survey-objection-tracker/SKILL.md` | "track the title and survey objections" | Title commitment, survey, parcel(s) | Title and survey objection tracker | `/real-estate:diligence-checklist` |
| `/real-estate:diligence-checklist` | `skills/real-estate/real-estate-diligence-checklist/SKILL.md` | "build a real estate diligence checklist" | Transaction type, property type, jurisdiction, party role | Tailored diligence checklist and request list | `/real-estate:title-survey-tracker`, `/real-estate:closing-tracker` |
| `/real-estate:closing-tracker` | `skills/real-estate/closing-deliverables-tracker/SKILL.md` | "build a closing checklist for this real estate deal" | Transaction type, party role, transaction agreement | Closing-deliverables tracker | `/real-estate:psa-review` |
| `/real-estate:estoppel-snda` | `skills/real-estate/estoppel-snda-review/SKILL.md` | "review this estoppel or SNDA" | The estoppel or SNDA, perspective, lease if available | Issue list and lease discrepancy table | `/real-estate:lease-abstract` |
| `/real-estate:zoning-issues` | `skills/real-estate/zoning-use-restriction-issue-spotter/SKILL.md` | "spot zoning and use-restriction issues" | Intended use, provided materials, jurisdiction | Issue list and questions for local counsel | `/real-estate:diligence-checklist` |

## Mergers & Acquisitions

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/m-and-a:loi-review` | `skills/m-and-a/loi-term-sheet-review/SKILL.md` | "review this LOI", "review this term sheet" | The LOI or term sheet, the side, the deal type | Binding/non-binding table and deal-terms issue list | `/m-and-a:purchase-agreement` |
| `/m-and-a:diligence-request-list` | `skills/m-and-a/acquisition-diligence-request-list/SKILL.md` | "build an M&A diligence request list" | Deal type, industry, target profile, side | Diligence request list by workstream | `/m-and-a:data-room-review` |
| `/m-and-a:data-room-review` | `skills/m-and-a/data-room-index-review/SKILL.md` | "review this data room index" | The data room index, deal type, side | Data-room gap matrix | `/m-and-a:diligence-request-list` |
| `/m-and-a:purchase-agreement` | `skills/m-and-a/purchase-agreement-issue-list/SKILL.md` | "review this purchase agreement" | The purchase agreement, side, deal type | Issue list and risk matrix | `/m-and-a:reps-disclosure`, `/m-and-a:indemnity-escrow` |
| `/m-and-a:reps-disclosure` | `skills/m-and-a/reps-warranties-disclosure-schedule-review/SKILL.md` | "compare reps against the disclosure schedules" | The reps article, the disclosure schedules, the side | Rep-by-rep review table | `/m-and-a:purchase-agreement` |
| `/m-and-a:indemnity-escrow` | `skills/m-and-a/indemnity-escrow-risk-review/SKILL.md` | "review the indemnity and escrow terms" | The indemnity and escrow provisions, the side | Indemnity architecture and risk matrix | `/m-and-a:purchase-agreement` |
| `/m-and-a:closing-tracker` | `skills/m-and-a/closing-deliverables-tracker/SKILL.md` | "build the M&A closing checklist" | Deal type, side, agreement and ancillary documents | Closing-deliverables tracker | `/m-and-a:consents` |
| `/m-and-a:consents` | `skills/m-and-a/third-party-consents-assignment-review/SKILL.md` | "what consents does this deal need" | Contracts or diligence summaries, deal structure, side | Consent tracker | `/m-and-a:closing-tracker` |
| `/m-and-a:post-closing` | `skills/m-and-a/post-closing-obligations-tracker/SKILL.md` | "track the post-closing obligations" | The acquisition agreement and ancillary documents, the side | Post-closing obligation tracker | `/m-and-a:integration` |
| `/m-and-a:integration` | `skills/m-and-a/integration-legal-issues-checklist/SKILL.md` | "build a legal integration checklist" | Deal type, pre/post-close status, target profile, side | Legal integration checklist | `/m-and-a:post-closing` |

## Employment

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/employment:termination` | `skills/employment/termination-risk/SKILL.md` | "assess a termination", "is it risky to let this person go" | Employee facts, stated reason, history | Risk checklist and factors | `/employment:severance`, `/employment:leave` |
| `/employment:severance` | `skills/employment/severance-review/SKILL.md` | "review this severance agreement" | Severance agreement, party served | Review and issues table | `/employment:termination` |
| `/employment:policy` | `skills/employment/employee-policy-review/SKILL.md` | "review our handbook", "review this workplace policy" | Policy or handbook text | Gap and issues table | `/ai:employee-policy` |
| `/employment:classify` | `skills/employment/worker-classification/SKILL.md` | "employee or contractor", "classify a worker" | Proposed engagement facts, classification purpose, jurisdiction | Classification analysis memo | `/employment:wage-hour` |
| `/employment:hiring` | `skills/employment/hiring-review/SKILL.md` | "review this offer letter" | Offer letter, work location, role and pay | Hiring review memo | `/employment:classify` |
| `/employment:wage-hour` | `skills/employment/wage-hour-qa/SKILL.md` | "wage-and-hour question", "overtime or exempt-status question" | The question, jurisdiction, operative facts | Wage-and-hour analysis | `/research:memo` |
| `/employment:investigation` | `skills/employment/internal-investigation/SKILL.md` | "run an internal investigation", "investigate this complaint" | Allegation, documents, interview notes | Investigation memorandum | `/litigation:legal-hold` |
| `/employment:leave` | `skills/employment/protected-leave-review/SKILL.md` | "protected leave situation", "medical or family leave" | Leave situation, procedural status, jurisdiction | Protected-leave review | `/employment:termination` |

## Privacy

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/privacy:dpa` | `skills/privacy/dpa-review/SKILL.md` | "review this DPA", "review a data processing agreement" | DPA text, client role | Risk table and review | `/contracts:review` |
| `/privacy:dsar` | `skills/privacy/dsar-workflow/SKILL.md` | "handle this DSAR", "data subject access request" | The request, requester details | Request-handling record | `/privacy:policy-gap` |
| `/privacy:policy-gap` | `skills/privacy/privacy-policy-gap-review/SKILL.md` | "check our privacy policy for gaps" | Privacy policy, described practices | Gap table and recommendations | `/privacy:pia` |
| `/privacy:pia` | `skills/privacy/pia-generation/SKILL.md` | "run a PIA", "do a privacy impact assessment" | Activity description, data categories, data flows | PIA draft | `/privacy:dpa` |

## Product Legal

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/product:launch-review` | `skills/product-legal/launch-review/SKILL.md` | "legal review before launch" | Launch description, data, claims | Issues register and recommendation | `/product:marketing-claims`, `/product:ai-feature` |
| `/product:marketing-claims` | `skills/product-legal/marketing-claims-review/SKILL.md` | "review this marketing copy" | Marketing or advertising copy | Claims register | `/product:launch-review` |
| `/product:tos` | `skills/product-legal/terms-of-service-review/SKILL.md` | "review these terms of service" | Terms of service text | Review and issues table | `/contracts:review` |
| `/product:ai-feature` | `skills/product-legal/ai-feature-review/SKILL.md` | "review the legal risk of this AI feature" | Feature description, model and data details | AI issues register | `/ai:use-case-intake`, `/ai:model-risk` |

## Regulatory

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/regulatory:enforcement-risk` | `skills/regulatory/enforcement-risk-memo/SKILL.md` | "assess our enforcement exposure" | Conduct at issue, relevant rules, facts | Enforcement risk memo | `/method:risk-assessment` |
| `/regulatory:rule-change` | `skills/regulatory/rule-change-summary/SKILL.md` | "summarize this new rule and its impact" | Rule text or official document | Summary and impact table | `/regulatory:gap-matrix` |
| `/regulatory:gap-matrix` | `skills/regulatory/compliance-gap-matrix/SKILL.md` | "map these requirements against our controls" | Requirement source, current controls | Compliance gap matrix | `/regulatory:rule-change` |
| `/regulatory:compliance-tracker` | `skills/regulatory/compliance-program-tracker/SKILL.md` | "track our compliance with this framework", "audit prep" | Framework source, control inventory, audit context | Compliance program tracker | `/regulatory:gap-matrix`, `/regulatory:rule-change` |

## AI Governance

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/ai:use-case-intake` | `skills/ai-governance/ai-use-case-intake/SKILL.md` | "intake an AI use case", "triage a proposed AI use case" | Use case description, model, data | Intake record and routing | `/ai:model-risk`, `/product:ai-feature` |
| `/ai:vendor-terms` | `skills/ai-governance/ai-vendor-terms-review/SKILL.md` | "review this AI vendor's terms" | Vendor terms text | Risk table and redline points | `/contracts:review`, `/privacy:dpa` |
| `/ai:model-risk` | `skills/ai-governance/model-risk-triage/SKILL.md` | "triage the risk of this AI model" | Model/system description, use, data | Risk register and tier | `/ai:use-case-intake` |
| `/ai:employee-policy` | `skills/ai-governance/employee-ai-policy/SKILL.md` | "review our employee AI-use policy" | Draft or existing AI policy | Gap and issues table | `/employment:policy` |

## Intellectual Property

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/ip:trademark` | `skills/ip/trademark-clearance-triage/SKILL.md` | "is this brand name available" | Proposed mark, goods/services, markets | Triage summary and signal | `/ip:infringement` |
| `/ip:dmca` | `skills/ip/dmca-takedown/SKILL.md` | "prepare a DMCA takedown or counter-notice" | The work, the allegedly infringing material | Draft notice / counter-notice | `/ip:infringement` |
| `/ip:oss-license` | `skills/ip/open-source-license-review/SKILL.md` | "review the open-source licenses in this project" | Component / license inventory, distribution model | Obligations table and issues | `/contracts:review` |
| `/ip:cease-desist` | `skills/ip/cease-and-desist-response/SKILL.md` | "we received a cease-and-desist letter" | The received letter, factual assessment | Response triage memo | `/litigation:demand` |
| `/ip:fto` | `skills/ip/fto-triage/SKILL.md` | "patent freedom-to-operate triage" | Product/feature description, jurisdictions, known patents | FTO triage memo | `/ip:infringement` |
| `/ip:invention` | `skills/ip/invention-intake/SKILL.md` | "screen this invention disclosure" | Invention disclosure, disclosure history | Invention screen and verdict | `/ip:fto` |
| `/ip:infringement` | `skills/ip/infringement-triage/SKILL.md` | "is this infringing", "triage a possible infringement" | IP right(s), party posture, evidence | Infringement triage memo | `/ip:fto`, `/litigation:claim-chart` |

## Financial Crime / AML

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/aml:kyc-onboarding` | `skills/financial-crime/kyc-onboarding-review/SKILL.md` | "run KYC on this client", "review this onboarding packet" | Onboarding packet, KYC/AML rules grid, screening results | KYC onboarding review and escalation packet | `/aml:screening` |
| `/aml:screening` | `skills/financial-crime/sanctions-screening-review/SKILL.md` | "review these screening hits", "adjudicate these sanctions or PEP matches" | Screening results, party identifiers, disposition policy | Screening review with recommended dispositions | `/aml:kyc-onboarding` |

## Legal Operations

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/legal-ops:response` | `skills/legal-ops/templated-legal-response/SKILL.md` | "draft a response to this DSR / litigation hold / vendor question" | The inquiry, response template, customization facts | Draft response with escalation-gate result | `/privacy:dsar`, `/litigation:legal-hold` |
| `/legal-ops:meeting-brief` | `skills/legal-ops/legal-meeting-briefing/SKILL.md` | "prepare me for this meeting", "build a meeting briefing" | Meeting context, background materials | Meeting briefing and action-item tracker | `/corporate:board-minutes` |
| `/legal-ops:signature` | `skills/legal-ops/signature-routing-checklist/SKILL.md` | "is this ready to sign", "set up signing for this document" | The document, intended signers, approvals | Signature readiness review and routing plan | `/contracts:review` |

## Setup

Commands for configuring AgentCounsel and opening a matter. The cold-start interviews configure a practice group and produce a filled-in practice profile under `practice-profiles/`; `create-matter-workspace` sets up a single matter file under `matter-workspaces/`.

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/setup:contracts` | `skills/setup/contracts-cold-start-interview/SKILL.md` | "configure the contracts practice", "set up the contracts profile" | A knowledgeable contracts attorney or designee | Filled `practice-profiles/contracts.md` draft | `/contracts:review` |
| `/setup:litigation` | `skills/setup/litigation-cold-start-interview/SKILL.md` | "configure the litigation practice" | A knowledgeable litigation attorney or designee | Filled `practice-profiles/litigation.md` draft | `/litigation:intake` |
| `/setup:privacy` | `skills/setup/privacy-cold-start-interview/SKILL.md` | "configure the privacy practice" | A knowledgeable privacy attorney or designee | Filled `practice-profiles/privacy.md` draft | `/privacy:dpa` |
| `/setup:corporate` | `skills/setup/corporate-cold-start-interview/SKILL.md` | "configure the corporate practice" | A knowledgeable corporate attorney or designee | Filled `practice-profiles/corporate.md` draft | `/corporate:closing-checklist` |
| `/setup:matter-workspace` | `skills/setup/create-matter-workspace/SKILL.md` | "set up a matter", "create a workspace", "organize this matter" | Matter type, client, responsible attorney, known parties / dates / documents | Populated matter workspace draft | `/litigation:intake` |

## Legal Methodology

Cross-cutting analytical disciplines that support skills in any practice area.

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/method:red-team` | `skills/legal-methodology/red-team-verifier/SKILL.md` | "red-team this draft", "stress-test this work product" | A draft legal work product to review | Verification findings report and verdict | `/method:source-validation` |
| `/method:statutory-interpretation` | `skills/legal-methodology/statutory-interpretation/SKILL.md` | "interpret this provision", "work through this statute" | The provision text, the interpretive question | Interpretation worksheet | `/research:memo` |
| `/method:risk-assessment` | `skills/legal-methodology/risk-assessment/SKILL.md` | "assess the legal risk", "rate and prioritize these risks" | The situation, known facts, client posture | Prioritized risk register | `/regulatory:enforcement-risk` |
| `/method:source-validation` | `skills/legal-methodology/source-validation/SKILL.md` | "validate the sources", "check these citations" | A draft and the sources it cites | Source-by-source validation table | `/method:red-team` |

## Keeping commands accurate

Every Skill path above is a real `SKILL.md` in the canonical `skills/` library. `scripts/validate_repo.py` checks that each path resolves. When a skill is added, renamed, or moved, update this file, `SKILLS_INDEX.md`, and `WORKFLOW_ROUTER.md` together.


## Securities / Capital Markets

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/securities:private-placement` | `skills/securities-capital-markets/private-placement-checklist/SKILL.md` | "private placement checklist" | Issuer/offering facts and source docs | Private placement tracker | `/securities:exemption-issues` |
| `/securities:exemption-issues` | `skills/securities-capital-markets/securities-exemption-issue-spotter/SKILL.md` | "exemption issue spotting" | Offering facts, investor/solicitation facts | Pathways and missing-facts matrix | `/securities:private-placement` |
| `/securities:offering-disclosure` | `skills/securities-capital-markets/offering-document-disclosure-review/SKILL.md` | "review offering document" | Disclosure drafts and sources | Disclosure issue list | `/securities:risk-factors` |
| `/securities:risk-factors` | `skills/securities-capital-markets/risk-factor-review/SKILL.md` | "review risk factors" | Risk factors and related sections | Risk-factor inventory | `/securities:filing-consistency` |
| `/securities:filing-consistency` | `skills/securities-capital-markets/sec-filing-consistency-check/SKILL.md` | "compare SEC drafts" | Filing set and versions | Inconsistency tracker | `/securities:offering-disclosure` |
| `/securities:form-d-blue-sky` | `skills/securities-capital-markets/form-d-blue-sky-tracker/SKILL.md` | "Form D tracker" | Offering and investor-jurisdiction facts | Filing workflow tracker | `/securities:private-placement` |
| `/securities:investor-rights` | `skills/securities-capital-markets/investor-rights-agreement-review/SKILL.md` | "review investor rights" | Financing agreement set and role | Terms/risk matrix | `/securities:private-placement` |
| `/securities:insider-policy` | `skills/securities-capital-markets/insider-trading-policy-review/SKILL.md` | "review insider trading policy" | Policy docs and covered persons | Policy issue list | `/securities:section16-triage` |
| `/securities:section16-triage` | `skills/securities-capital-markets/section-16-beneficial-ownership-triage/SKILL.md` | "Section 16 triage" | Ownership/role facts and docs | Facts-to-verify table | `/securities:reporting-intake` |
| `/securities:closing-checklist` | `skills/securities-capital-markets/capital-markets-closing-checklist/SKILL.md` | "capital markets closing checklist" | Transaction docs and responsibilities | Closing deliverables tracker | `/securities:comfort-backup` |
| `/securities:comfort-backup` | `skills/securities-capital-markets/comfort-backup-request-tracker/SKILL.md` | "comfort backup tracker" | Disclosure statements and source docs | Numbered backup requests tracker | `/securities:closing-checklist` |
| `/securities:reporting-intake` | `skills/securities-capital-markets/public-company-reporting-calendar-intake/SKILL.md` | "reporting calendar intake" | Filer profile and reporting workflow facts | Intake checklist + matrix | `/securities:filing-consistency` |


## Tax

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/tax:intake` | `skills/tax/tax-issue-intake/SKILL.md` | "tax issue intake", "organize tax facts" | Jurisdictions, taxpayer/entity type, tax period, source docs | Intake summary + issue map | `/tax:docs`, `/tax:provision-review` |
| `/tax:entity-classification` | `skills/tax/entity-tax-classification-checklist/SKILL.md` | "entity tax classification" | Entity docs, ownership changes, filings | Classification facts table | `/tax:intake` |
| `/tax:diligence` | `skills/tax/transaction-tax-diligence-request-list/SKILL.md` | "transaction tax diligence" | Deal context, source docs | Request list by workstream | `/tax:provision-review`, `/tax:covenants` |
| `/tax:nexus-triage` | `skills/tax/sales-use-tax-nexus-triage/SKILL.md` | "sales tax nexus", "use tax nexus" | Jurisdictions, product/service facts, filings | Nexus fact map + missing facts | `/tax:intake` |
| `/tax:worker-intake` | `skills/tax/employment-tax-worker-classification-intake/SKILL.md` | "employment tax classification" | Worker facts, contracts, payroll records | Facts-to-verify table | `/tax:intake` |
| `/tax:provision-review` | `skills/tax/tax-provision-review-checklist/SKILL.md` | "tax provision review" | Contract text and tax sections | Risk matrix + negotiation points | `/tax:covenants` |
| `/tax:docs` | `skills/tax/tax-document-organizer/SKILL.md` | "organize tax documents" | Tax document set | Inventory + missing document list | `/tax:intake` |
| `/tax:covenants` | `skills/tax/tax-covenants-indemnities-review/SKILL.md` | "tax indemnity review" | Agreement provisions | Covenant/indemnity architecture | `/tax:provision-review` |
| `/tax:international` | `skills/tax/international-tax-issue-spotter/SKILL.md` | "cross-border tax issue" | Cross-border facts and source docs | Issue map + follow-ups | `/tax:intake` |
| `/tax:crypto-intake` | `skills/tax/crypto-digital-asset-tax-intake/SKILL.md` | "crypto tax intake" | Wallet/exchange records, activity data | Transaction category map | `/tax:docs`, `/tax:intake` |


## Bankruptcy / Restructuring

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/bankruptcy:intake` | `skills/bankruptcy-restructuring/bankruptcy-matter-intake/SKILL.md` | "bankruptcy matter intake", "restructuring intake" | Parties, party role, case status, document set | Matter summary + risk themes | `/bankruptcy:claim-intake`, `/bankruptcy:deadline-tracker` |
| `/bankruptcy:claim-intake` | `skills/bankruptcy-restructuring/creditor-claim-intake/SKILL.md` | "creditor claim intake" | Debtor/creditor, claim basis, amount as stated | Claim facts table + dispute flags | `/bankruptcy:proof-of-claim` |
| `/bankruptcy:proof-of-claim` | `skills/bankruptcy-restructuring/proof-of-claim-checklist/SKILL.md` | "proof of claim checklist" | Claimant, debtor/case, supporting documents | Preparation checklist + tracker | `/bankruptcy:claim-intake` |
| `/bankruptcy:stay-issues` | `skills/bankruptcy-restructuring/automatic-stay-issue-spotter/SKILL.md` | "automatic stay issue spotting" | Debtor, party role, actions in question | Stay-risk fact map + escalation flags | `/bankruptcy:intake` |
| `/bankruptcy:preference-triage` | `skills/bankruptcy-restructuring/preference-demand-response-triage/SKILL.md` | "preference demand response" | Demand letter, alleged transfers, payment history | Transfer timeline + defense-facts checklist | `/bankruptcy:intake` |
| `/bankruptcy:executory-contracts` | `skills/bankruptcy-restructuring/executory-contract-assumption-rejection-checklist/SKILL.md` | "executory contract assumption rejection" | Contract identity, roles, defaults, cure amounts | Contract status table + cure tracker | `/bankruptcy:stay-issues` |
| `/bankruptcy:diligence` | `skills/bankruptcy-restructuring/bankruptcy-diligence-request-list/SKILL.md` | "bankruptcy diligence request list" | Transaction/matter type, party role, workstreams | Request list by workstream | `/bankruptcy:asset-sale` |
| `/bankruptcy:term-sheet` | `skills/bankruptcy-restructuring/restructuring-term-sheet-review/SKILL.md` | "restructuring term sheet review" | The document, party role, parties, debt instruments | Key terms table + issue list | `/bankruptcy:dip-financing` |
| `/bankruptcy:plan-issues` | `skills/bankruptcy-restructuring/plan-disclosure-statement-issue-spotter/SKILL.md` | "plan disclosure statement review" | Plan/disclosure statement, party role | Treatment table + issue list | `/bankruptcy:claim-intake` |
| `/bankruptcy:asset-sale` | `skills/bankruptcy-restructuring/distressed-asset-sale-checklist/SKILL.md` | "distressed asset sale checklist" | Asset, sale process, party role, sale documents | Sale checklist + closing trackers | `/bankruptcy:diligence` |
| `/bankruptcy:dip-financing` | `skills/bankruptcy-restructuring/cash-collateral-dip-financing-issue-spotter/SKILL.md` | "cash collateral DIP financing issues" | Financing document, party role, lenders, collateral | Key terms table + issue list | `/bankruptcy:term-sheet` |
| `/bankruptcy:deadline-tracker` | `skills/bankruptcy-restructuring/bankruptcy-deadline-tracker-intake/SKILL.md` | "bankruptcy deadline tracker" | Dates the user provides with sources, party role | Draft deadline tracker | `/bankruptcy:intake` |


## Insurance

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/insurance:policy-summary` | `skills/insurance/insurance-policy-summary/SKILL.md` | "summarize this insurance policy" | Policy document set, policy type, role, policy period | Source-cited policy summary | `/insurance:coverage-issues` |
| `/insurance:coverage-issues` | `skills/insurance/coverage-issue-spotter/SKILL.md` | "issue-spot coverage on this claim" | Policy, claim facts, tender, pleadings, role | Coverage issue matrix | `/insurance:position-outline` |
| `/insurance:claims-chronology` | `skills/insurance/claims-chronology-builder/SKILL.md` | "build a claim chronology" | Notices, correspondence, adjuster notes, payment history | Claim chronology | `/insurance:bad-faith-triage` |
| `/insurance:ror-review` | `skills/insurance/reservation-of-rights-review/SKILL.md` | "review this reservation of rights letter" | ROR letter or correspondence, the policy, role | Issue list + provision-reference table | `/insurance:communications` |
| `/insurance:tender-review` | `skills/insurance/tender-letter-review/SKILL.md` | "review this tender letter" | Tender letter, asserted policy/contract basis, role | Tender completeness checklist + risk flags | `/insurance:contract-requirements` |
| `/insurance:position-outline` | `skills/insurance/coverage-position-outline/SKILL.md` | "assemble a coverage-position outline" | Policy, claim facts, correspondence, role, claim stage | Coverage-position outline | `/insurance:coverage-issues` |
| `/insurance:bad-faith-triage` | `skills/insurance/bad-faith-risk-triage/SKILL.md` | "triage bad-faith risk themes" | Claim file materials, the policy, role, claim stage | Risk-theme list + questions for counsel | `/insurance:claims-chronology` |
| `/insurance:coi-review` | `skills/insurance/certificate-of-insurance-review/SKILL.md` | "review this certificate of insurance" | Certificate(s), endorsements, contract requirements | COI comparison table | `/insurance:contract-requirements` |
| `/insurance:contract-requirements` | `skills/insurance/insurance-requirements-contract-review/SKILL.md` | "review the insurance clauses in this contract" | Contract, contract type, role | Requirements table + risk matrix | `/insurance:coi-review` |
| `/insurance:subrogation-tracker` | `skills/insurance/subrogation-recovery-tracker/SKILL.md` | "track subrogation and recovery facts" | Loss facts, payment documents, contracts, policy provisions | Recovery fact map | `/insurance:claims-chronology` |
| `/insurance:renewal-diligence` | `skills/insurance/policy-renewal-placement-diligence-checklist/SKILL.md` | "renewal or placement diligence checklist" | Renewal context, expiring policies, claims history, lines in scope | Diligence checklist + document requests | `/insurance:policy-summary` |
| `/insurance:communications` | `skills/insurance/insurer-insured-communications-review/SKILL.md` | "review insurer/insured communications" | Communications, policy/claim context, role, review purpose | Communication issue list + suggested edits | `/insurance:ror-review` |
