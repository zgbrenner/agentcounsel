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

## Setup

Commands for configuring AgentCounsel for a practice group. Each runs a cold-start interview and produces a filled-in practice profile under `practice-profiles/`.

| Command | Skill | Trigger phrases | Required inputs | Expected output | Related |
|---|---|---|---|---|---|
| `/setup:contracts` | `skills/setup/contracts-cold-start-interview/SKILL.md` | "configure the contracts practice", "set up the contracts profile" | A knowledgeable contracts attorney or designee | Filled `practice-profiles/contracts.md` draft | `/contracts:review` |
| `/setup:litigation` | `skills/setup/litigation-cold-start-interview/SKILL.md` | "configure the litigation practice" | A knowledgeable litigation attorney or designee | Filled `practice-profiles/litigation.md` draft | `/litigation:intake` |
| `/setup:privacy` | `skills/setup/privacy-cold-start-interview/SKILL.md` | "configure the privacy practice" | A knowledgeable privacy attorney or designee | Filled `practice-profiles/privacy.md` draft | `/privacy:dpa` |
| `/setup:corporate` | `skills/setup/corporate-cold-start-interview/SKILL.md` | "configure the corporate practice" | A knowledgeable corporate attorney or designee | Filled `practice-profiles/corporate.md` draft | `/corporate:closing-checklist` |

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
