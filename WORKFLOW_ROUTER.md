# AgentCounsel — Workflow Router

This guide maps a task to the right skill. Use it to go from "I need to do X" to the correct `SKILL.md`.

> Before running any skill, read the `core/` operating rules. Every skill produces **draft legal work product for attorney review** — never legal advice.

## How routing works

1. Identify the task type from the user's request.
2. Match it to a row below and open that `SKILL.md`.
3. If the request spans several skills, pick the **narrowest** one that fits the immediate task; the skill will point to siblings if needed.
4. If nothing matches, say so — do not improvise a legal workflow.

## Choose the right surface

Use this order before selecting a skill:

| User need | Route to | When to choose it |
|---|---|---|
| A single self-contained task | One `skills/<area>/<skill>/SKILL.md` | The user supplied one document/request and wants one draft output. |
| Repeated work in one practice area | Practice-area platform pack | The user will run several tasks in the same practice area in ChatGPT, Claude, Gemini, Cursor, Codex, or another repo agent. See `metadata/packs.json`. |
| A recurring multi-step matter type | `matter-packs/<area>.md` | The matter needs an ordered sequence of skills. |
| A live matter with parties, facts, documents, deadlines, and multiple outputs | `matter-workspaces/<matter-type>.md` through `skills/setup/create-matter-workspace/SKILL.md` | Context must persist across skill runs or deadlines/open items must be tracked. |
| Review an output before reliance | Quality check skill or core checklist | Use `skills/legal-methodology/source-validation/SKILL.md`, `skills/legal-methodology/red-team-verifier/SKILL.md`, and `core/attorney-review-checklist.md`. |
| Structured sign-off status | Review panel pattern | Use the skill's Attorney Verification Checklist for now; a reusable review-panel block is planned in `docs/IMPLEMENTATION_SEQUENCE.md`. |

## Routing gates

Before running any legal skill, identify missing facts and stop to ask for them
if the skill cannot safely proceed.

| Gate | Ask for or flag |
|---|---|
| Required inputs | The document, facts, client role, business context, and objective named in the selected skill. |
| Jurisdiction | Jurisdiction, governing law, venue, agency, court, or regulatory authority. If unknown, mark `[JURISDICTION UNKNOWN]` and avoid legal conclusions. |
| Deadlines | Any response date, filing date, effective date, hearing date, closing date, notice period, or user-supplied deadline. Never calculate a legal deadline without attorney verification. |
| Attorney escalation | Escalate when facts are missing, authority is uncertain, privilege/confidentiality is implicated, an adversarial filing or communication is involved, a deadline is present, or the user asks for a final legal conclusion. |
| Source validation | Mandatory for legal research, rule summaries, authority-cited analysis, filings, adversarial communications, or any output that cites cases, statutes, regulations, agency materials, or quotations. |
| Follow-up quality checks | Use `source-validation` for authority, `red-team-verifier` for high-risk output, `jurisdiction-and-deadline-gates` for date/jurisdiction issues, and the Attorney Verification Checklist for every output. |

Machine-readable routing data is generated in `metadata/router.json`.

## Examples for vague requests

| Request | Route | Missing facts to ask for | Mandatory gates and checks |
|---|---|---|---|
| "Review this NDA" | `skills/contracts/nda-review/SKILL.md` | Full NDA text; client role; transaction context; governing law if supplied; client playbook if any. | Jurisdiction if governing law matters; attorney review; source validation for any cited authority; legal prose quality. |
| "Help me respond to opposing counsel" | Start with `skills/litigation/matter-intake/SKILL.md`; then route to `skills/litigation/demand-letter/SKILL.md` or `skills/legal-research/legal-research-memo/SKILL.md` as needed. | Communication from opposing counsel; matter posture; jurisdiction/venue; response deadline; client objective; authorized tone. | Matter workspace recommended; deadline gate; privilege/confidentiality; source validation; red-team verifier; attorney review. |
| "Summarize this new privacy rule" | `skills/regulatory/rule-change-summary/SKILL.md` | Official rule source; issuing authority; effective date; affected business/process; jurisdiction. | Source validation mandatory; jurisdiction and effective-date gate; attorney review. |
| "Draft a demand letter" | `skills/litigation/demand-letter/SKILL.md` | Parties; factual chronology; counsel-approved claim theory; jurisdiction; response deadline; settlement authority. | Deadline gate; source validation for legal assertions; red-team verifier; attorney review before sending. |
| "Check this contract for risk" | `skills/contracts/contract-risk-review/SKILL.md`; use a contracts practice-area pack for repeated contract work. | Contract text; client role; deal context; governing law; fallback positions or playbook. | Attorney review; source validation if legal authority is cited; legal prose quality. |
| "I need help with a California employee termination" | `skills/employment/termination-risk/SKILL.md`; create a matter workspace if this is a live matter. | Employee role/tenure; reason; protected-class, leave, accommodation, retaliation, complaint, and wage facts; policies; planned date. | California jurisdiction gate; deadline/final-pay timing gate; confidentiality/privilege; source validation; red-team verifier; attorney review. |

## Before you start: complex or multi-step matters

If the task is more than a single, self-contained skill run — it spans several skills, multiple documents, more than one deadline, or more than one team member — create a **matter workspace** first. Run `skills/setup/create-matter-workspace/SKILL.md`: it recommends the right template from `matter-workspaces/` and produces a populated workspace draft. The workspace is the single file that carries the matter's parties, facts, jurisdiction, deadlines, and the draft work product produced by every skill you run, so context is not lost between steps. For a one-off task, skip this and go straight to the skill.

For a recurring, multi-step matter *type*, `matter-packs/` bundles a recommended sequence of skills to run end to end — see `matter-packs/real-estate.md` for the Real Estate workflow bundles.

## Task -> Skill

### Contracts and agreements

| The task sounds like... | Use this skill |
|---|---|
| "Review this NDA" / "check this confidentiality agreement" | `skills/contracts/nda-review/SKILL.md` |
| "Summarize the risks in this vendor agreement / MSA / services contract" | `skills/contracts/contract-risk-review/SKILL.md` |
| "What changed between these two contract drafts?" / "summarize this redline" | `skills/contracts/redline-summary/SKILL.md` |
| "Review this statement of work" / "does this SOW match the MSA?" | `skills/contracts/sow-review/SKILL.md` |
| "What agreements do we have with this vendor?" / "vendor agreement status" | `skills/contracts/vendor-agreement-status/SKILL.md` |
| "Review this data processing agreement / DPA" | `skills/privacy/dpa-review/SKILL.md` |
| "Review this AI vendor's terms" | `skills/ai-governance/ai-vendor-terms-review/SKILL.md` |
| "Review these terms of service" | `skills/product-legal/terms-of-service-review/SKILL.md` |

### Corporate and transactions

| The task sounds like... | Use this skill |
|---|---|
| "Draft minutes for this board meeting" | `skills/corporate/board-minutes/SKILL.md` |
| "Draft a board written consent" / "action by written consent" | `skills/corporate/written-consent/SKILL.md` |
| "Build a closing checklist for this deal" | `skills/corporate/closing-checklist/SKILL.md` |
| "Pull the issues out of these diligence documents" | `skills/corporate/diligence-issue-extraction/SKILL.md` |
| "Build the material contracts schedule" | `skills/corporate/material-contract-schedule/SKILL.md` |
| "Review our entities' annual-report / good-standing status" | `skills/corporate/entity-compliance/SKILL.md` |

### Real estate

| The task sounds like... | Use this skill |
|---|---|
| "Abstract this lease" / "pull the key terms from this commercial lease" | `skills/real-estate/lease-abstract/SKILL.md` |
| "Reconcile the lease and its amendments" / "what are the current controlling lease terms" | `skills/real-estate/lease-amendment-reconciliation/SKILL.md` |
| "Review this commercial lease" / "flag the lease issues from our side" | `skills/real-estate/commercial-lease-review/SKILL.md` |
| "Review this purchase and sale agreement" / "review this real estate PSA" | `skills/real-estate/psa-review/SKILL.md` |
| "Organize the title and survey objections" / "track the title exceptions" | `skills/real-estate/title-survey-objection-tracker/SKILL.md` |
| "Build a real estate due-diligence checklist" | `skills/real-estate/real-estate-diligence-checklist/SKILL.md` |
| "Build a closing checklist for this real estate deal" | `skills/real-estate/closing-deliverables-tracker/SKILL.md` |
| "Review this estoppel certificate or SNDA" | `skills/real-estate/estoppel-snda-review/SKILL.md` |
| "Spot the zoning and use-restriction issues" | `skills/real-estate/zoning-use-restriction-issue-spotter/SKILL.md` |

### Mergers and acquisitions

| The task sounds like... | Use this skill |
|---|---|
| "Review this LOI" / "review this term sheet" | `skills/m-and-a/loi-term-sheet-review/SKILL.md` |
| "Build an M&A diligence request list" | `skills/m-and-a/acquisition-diligence-request-list/SKILL.md` |
| "Review this data room index" / "what is missing from the data room" | `skills/m-and-a/data-room-index-review/SKILL.md` |
| "Review this purchase agreement" / "issues in this merger, stock, or asset purchase agreement" | `skills/m-and-a/purchase-agreement-issue-list/SKILL.md` |
| "Compare the reps against the disclosure schedules" | `skills/m-and-a/reps-warranties-disclosure-schedule-review/SKILL.md` |
| "Review the indemnity and escrow terms" | `skills/m-and-a/indemnity-escrow-risk-review/SKILL.md` |
| "Build the M&A closing checklist" | `skills/m-and-a/closing-deliverables-tracker/SKILL.md` |
| "What third-party consents does this deal need?" | `skills/m-and-a/third-party-consents-assignment-review/SKILL.md` |
| "Track the post-closing obligations" | `skills/m-and-a/post-closing-obligations-tracker/SKILL.md` |
| "Build a legal integration checklist" | `skills/m-and-a/integration-legal-issues-checklist/SKILL.md` |


### Antitrust / competition

| The task sounds like... | Use this skill |
|---|---|
| "Intake this antitrust risk" | `skills/antitrust-competition/antitrust-risk-intake/SKILL.md` |
| "Review this competitor collaboration/JV/benchmarking plan" | `skills/antitrust-competition/competitor-collaboration-review/SKILL.md` |
| "Review this clean-team or information-sharing protocol" | `skills/antitrust-competition/information-sharing-clean-team-review/SKILL.md` |
| "Triage antitrust risk in this pricing algorithm" | `skills/antitrust-competition/pricing-algorithm-risk-triage/SKILL.md` |
| "Review distribution restraints or reseller restrictions" | `skills/antitrust-competition/distribution-restraints-review/SKILL.md` |
| "Review exclusivity/MFN/loyalty pricing terms" | `skills/antitrust-competition/exclusivity-mfn-pricing-review/SKILL.md` |
| "Issue-spot merger antitrust concerns" | `skills/antitrust-competition/merger-antitrust-issue-spotter/SKILL.md` |
| "Build pre-closing gun-jumping checklist" | `skills/antitrust-competition/gun-jumping-clean-team-checklist/SKILL.md` |
| "Review trade-association agenda/minutes" | `skills/antitrust-competition/trade-association-meeting-review/SKILL.md` |
| "Review antitrust compliance policy/training" | `skills/antitrust-competition/antitrust-compliance-policy-review/SKILL.md` |

### Litigation and disputes

| The task sounds like... | Use this skill |
|---|---|
| "Open / intake a new litigation matter" | `skills/litigation/matter-intake/SKILL.md` |
| "Build a factual timeline from these documents" | `skills/litigation/litigation-chronology/SKILL.md` |
| "Draft a demand letter" | `skills/litigation/demand-letter/SKILL.md` |
| "We received a subpoena — what now?" | `skills/litigation/subpoena-triage/SKILL.md` |
| "Prepare for a deposition" / "build a deposition outline" | `skills/litigation/deposition-prep/SKILL.md` |
| "Issue a litigation hold" / "preserve documents for a matter" | `skills/litigation/legal-hold/SKILL.md` |
| "Review our privilege log" | `skills/litigation/privilege-log-review/SKILL.md` |
| "Build a claim chart" / "map claim elements to the evidence" | `skills/litigation/claim-chart/SKILL.md` |
| "Draft a section of a brief" | `skills/litigation/brief-section-drafter/SKILL.md` |
| "Research this legal question and write a memo" | `skills/legal-research/legal-research-memo/SKILL.md` |

### Employment

| The task sounds like... | Use this skill |
|---|---|
| "Help assess a termination" / "is it risky to let this person go?" | `skills/employment/termination-risk/SKILL.md` |
| "Is this worker an employee or a contractor?" / "classify a worker" | `skills/employment/worker-classification/SKILL.md` |
| "Review this offer letter before we send it" | `skills/employment/hiring-review/SKILL.md` |
| "Wage-and-hour question" / "overtime, exempt status, or final-pay question" | `skills/employment/wage-hour-qa/SKILL.md` |
| "Run an internal investigation" / "investigate this complaint" | `skills/employment/internal-investigation/SKILL.md` |
| "Employee is on (or returning from) protected leave" / "medical or family leave situation" | `skills/employment/protected-leave-review/SKILL.md` |
| "Review this severance / separation agreement" | `skills/employment/severance-review/SKILL.md` |
| "Review our employee handbook / this workplace policy" | `skills/employment/employee-policy-review/SKILL.md` |
| "Review our internal employee AI-use policy" | `skills/ai-governance/employee-ai-policy/SKILL.md` |

### Privacy and data

| The task sounds like... | Use this skill |
|---|---|
| "Review a DPA" | `skills/privacy/dpa-review/SKILL.md` |
| "We got a data subject access request" / "handle this DSAR" | `skills/privacy/dsar-workflow/SKILL.md` |
| "Check our privacy policy for gaps" | `skills/privacy/privacy-policy-gap-review/SKILL.md` |
| "Run a privacy impact assessment" / "do a PIA or DPIA" | `skills/privacy/pia-generation/SKILL.md` |

### Product, marketing, and AI features

| The task sounds like... | Use this skill |
|---|---|
| "Do a legal review before this product / feature launches" | `skills/product-legal/launch-review/SKILL.md` |
| "Review this marketing / advertising copy" | `skills/product-legal/marketing-claims-review/SKILL.md` |
| "Review the legal risk of this AI feature" | `skills/product-legal/ai-feature-review/SKILL.md` |
| "Intake / triage a proposed AI use case" | `skills/ai-governance/ai-use-case-intake/SKILL.md` |
| "Triage the risk of this AI model / system" | `skills/ai-governance/model-risk-triage/SKILL.md` |

### Regulatory and compliance

| The task sounds like... | Use this skill |
|---|---|
| "Assess our enforcement exposure on this" | `skills/regulatory/enforcement-risk-memo/SKILL.md` |
| "Summarize this new rule / regulation and its impact" | `skills/regulatory/rule-change-summary/SKILL.md` |
| "Map these requirements against our controls" | `skills/regulatory/compliance-gap-matrix/SKILL.md` |
| "Track our compliance with this framework over time" / "audit prep" | `skills/regulatory/compliance-program-tracker/SKILL.md` |

### Intellectual property

| The task sounds like... | Use this skill |
|---|---|
| "Is this brand / product name available?" (preliminary triage) | `skills/ip/trademark-clearance-triage/SKILL.md` |
| "We received a cease-and-desist letter" | `skills/ip/cease-and-desist-response/SKILL.md` |
| "Patent freedom-to-operate triage for this product" | `skills/ip/fto-triage/SKILL.md` |
| "Screen this invention disclosure" | `skills/ip/invention-intake/SKILL.md` |
| "Is this infringing?" / "triage a possible IP infringement" | `skills/ip/infringement-triage/SKILL.md` |
| "Prepare / respond to a DMCA takedown" | `skills/ip/dmca-takedown/SKILL.md` |
| "Review the open-source licenses in this project" | `skills/ip/open-source-license-review/SKILL.md` |

### Financial crime and AML

| The task sounds like... | Use this skill |
|---|---|
| "Run KYC on this new client" / "review this onboarding packet" | `skills/financial-crime/kyc-onboarding-review/SKILL.md` |
| "Review these screening hits" / "adjudicate these sanctions or PEP matches" | `skills/financial-crime/sanctions-screening-review/SKILL.md` |

### Securities / capital markets

The Securities / Capital Markets skills produce **draft work product for a qualified, licensed securities attorney**. They stay inside issue spotting, intake, document review, and checklist workflows — never securities legal advice, exemption determinations, registration calls, or deadline calculations.

| The task sounds like... | Use this skill |
|---|---|
| "Build a private offering checklist" | `skills/securities-capital-markets/private-placement-checklist/SKILL.md` |
| "Issue-spot securities exemption pathways" | `skills/securities-capital-markets/securities-exemption-issue-spotter/SKILL.md` |
| "Review this offering document disclosure draft" | `skills/securities-capital-markets/offering-document-disclosure-review/SKILL.md` |
| "Review the risk factors" | `skills/securities-capital-markets/risk-factor-review/SKILL.md` |
| "Compare these SEC filing drafts for consistency" | `skills/securities-capital-markets/sec-filing-consistency-check/SKILL.md` |
| "Track Form D and state notice filings" | `skills/securities-capital-markets/form-d-blue-sky-tracker/SKILL.md` |
| "Review this investor rights or governance agreement" | `skills/securities-capital-markets/investor-rights-agreement-review/SKILL.md` |
| "Review this insider-trading policy" | `skills/securities-capital-markets/insider-trading-policy-review/SKILL.md` |
| "Triage Section 16 or 13D/G beneficial ownership facts" | `skills/securities-capital-markets/section-16-beneficial-ownership-triage/SKILL.md` |
| "Build a capital-markets closing checklist" | `skills/securities-capital-markets/capital-markets-closing-checklist/SKILL.md` |
| "Track comfort and backup requests" | `skills/securities-capital-markets/comfort-backup-request-tracker/SKILL.md` |
| "Intake public-company reporting calendar facts" | `skills/securities-capital-markets/public-company-reporting-calendar-intake/SKILL.md` |

### Tax

The Tax skills produce **draft work product for qualified tax counsel or a licensed tax professional**. They stay inside issue spotting, intake, diligence, document organization, and reviewer-ready working papers — never tax computation, return preparation, filing, or tax advice. For a recurring multi-step tax matter, see the workflow bundles in `matter-packs/tax.md`.

| The task sounds like... | Use this skill |
|---|---|
| "Intake a tax-sensitive matter and map the issues" | `skills/tax/tax-issue-intake/SKILL.md` |
| "Organize entity facts for a tax-classification review" | `skills/tax/entity-tax-classification-checklist/SKILL.md` |
| "Build a transaction tax diligence request list" | `skills/tax/transaction-tax-diligence-request-list/SKILL.md` |
| "Map sales/use tax nexus facts by jurisdiction" | `skills/tax/sales-use-tax-nexus-triage/SKILL.md` |
| "Intake worker and payroll facts for an employment-tax review" | `skills/tax/employment-tax-worker-classification-intake/SKILL.md` |
| "Review the tax provisions of a contract" | `skills/tax/tax-provision-review-checklist/SKILL.md` |
| "Organize a tax document set into a source-cited inventory" | `skills/tax/tax-document-organizer/SKILL.md` |
| "Review tax covenants and indemnities in a transaction agreement" | `skills/tax/tax-covenants-indemnities-review/SKILL.md` |
| "Issue-spot cross-border tax questions" | `skills/tax/international-tax-issue-spotter/SKILL.md` |
| "Intake crypto and digital-asset activity and records" | `skills/tax/crypto-digital-asset-tax-intake/SKILL.md` |

### Bankruptcy / restructuring

The Bankruptcy / Restructuring skills produce **draft work product for a qualified, licensed attorney**. They stay inside intake, issue spotting, document tracking, and checklist workflows — never bankruptcy legal advice, pleadings, filings, deadline calculations, or legal conclusions. For a recurring multi-step matter, see the workflow bundles in `matter-packs/bankruptcy-restructuring.md`.

| The task sounds like... | Use this skill |
|---|---|
| "Intake a bankruptcy or restructuring matter" | `skills/bankruptcy-restructuring/bankruptcy-matter-intake/SKILL.md` |
| "Organize a creditor's facts for a potential claim" | `skills/bankruptcy-restructuring/creditor-claim-intake/SKILL.md` |
| "Build a proof-of-claim preparation checklist" | `skills/bankruptcy-restructuring/proof-of-claim-checklist/SKILL.md` |
| "Issue-spot automatic stay concerns" | `skills/bankruptcy-restructuring/automatic-stay-issue-spotter/SKILL.md` |
| "Respond to a preference demand" | `skills/bankruptcy-restructuring/preference-demand-response-triage/SKILL.md` |
| "Review executory contract assumption/rejection issues" | `skills/bankruptcy-restructuring/executory-contract-assumption-rejection-checklist/SKILL.md` |
| "Build a bankruptcy or distressed-transaction diligence request list" | `skills/bankruptcy-restructuring/bankruptcy-diligence-request-list/SKILL.md` |
| "Review a restructuring support, forbearance, or workout document" | `skills/bankruptcy-restructuring/restructuring-term-sheet-review/SKILL.md` |
| "Issue-spot a Chapter 11 plan and disclosure statement" | `skills/bankruptcy-restructuring/plan-disclosure-statement-issue-spotter/SKILL.md` |
| "Build a bankruptcy or distressed asset-sale checklist" | `skills/bankruptcy-restructuring/distressed-asset-sale-checklist/SKILL.md` |
| "Issue-spot a cash collateral or DIP financing document" | `skills/bankruptcy-restructuring/cash-collateral-dip-financing-issue-spotter/SKILL.md` |
| "Intake bankruptcy dates into a draft deadline tracker" | `skills/bankruptcy-restructuring/bankruptcy-deadline-tracker-intake/SKILL.md` |

### Insurance

The Insurance skills produce **draft work product for a qualified, licensed attorney**. They stay inside issue spotting, intake, source-cited summaries, chronologies, trackers, and reviewer-ready working papers — never insurance coverage advice, coverage determinations, claim approvals or denials, reserve calculations, bad-faith conclusions, or insurance sales advice. For a recurring multi-step matter, see the workflow bundles in `matter-packs/insurance.md`.

| The task sounds like... | Use this skill |
|---|---|
| "Summarize this insurance policy" | `skills/insurance/insurance-policy-summary/SKILL.md` |
| "Issue-spot the coverage questions on this claim" | `skills/insurance/coverage-issue-spotter/SKILL.md` |
| "Build a claim chronology from the claim file" | `skills/insurance/claims-chronology-builder/SKILL.md` |
| "Review this reservation of rights letter or coverage correspondence" | `skills/insurance/reservation-of-rights-review/SKILL.md` |
| "Review this tender, claim notice, or additional insured tender" | `skills/insurance/tender-letter-review/SKILL.md` |
| "Assemble a coverage-position outline" | `skills/insurance/coverage-position-outline/SKILL.md` |
| "Triage claim-handling and bad-faith risk themes" | `skills/insurance/bad-faith-risk-triage/SKILL.md` |
| "Review this certificate of insurance against contract requirements" | `skills/insurance/certificate-of-insurance-review/SKILL.md` |
| "Review the insurance and indemnity clauses of a contract" | `skills/insurance/insurance-requirements-contract-review/SKILL.md` |
| "Organize potential subrogation and recovery facts" | `skills/insurance/subrogation-recovery-tracker/SKILL.md` |
| "Build a renewal or placement diligence checklist" | `skills/insurance/policy-renewal-placement-diligence-checklist/SKILL.md` |
| "Review insurer/insured/claimant/broker communications" | `skills/insurance/insurer-insured-communications-review/SKILL.md` |

### Trusts & estates

The Trusts & Estates skills produce **draft work product for a qualified, licensed attorney**. They stay inside intake, issue spotting, document inventories, administration trackers, chronology tables, and reviewer-ready working papers — never estate-planning, probate, or tax advice, instruments or court forms, capacity or undue-influence conclusions, beneficiary-entitlement or fiduciary-breach conclusions, or calculated taxes or deadlines. For a recurring multi-step matter, see the workflow bundles in `matter-packs/trusts-estates.md`.

| The task sounds like... | Use this skill |
|---|---|
| "Intake an estate-planning matter" | `skills/trusts-estates/estate-planning-intake/SKILL.md` |
| "Summarize a will, trust, or related estate document" | `skills/trusts-estates/estate-document-summary/SKILL.md` |
| "Build a probate document checklist" | `skills/trusts-estates/probate-document-checklist/SKILL.md` |
| "Track trust administration tasks" | `skills/trusts-estates/trust-administration-tracker/SKILL.md` |
| "Issue-spot fiduciary-duty questions" | `skills/trusts-estates/fiduciary-duty-issue-spotter/SKILL.md` |
| "Review beneficiary designations and account titling" | `skills/trusts-estates/beneficiary-designation-review/SKILL.md` |
| "Build an estate or trust asset and liability inventory" | `skills/trusts-estates/asset-liability-inventory-builder/SKILL.md` |
| "Organize capacity or undue-influence facts" | `skills/trusts-estates/capacity-undue-influence-facts-organizer/SKILL.md` |
| "Build a chronology for a will or trust contest or fiduciary dispute" | `skills/trusts-estates/estate-litigation-facts-chronology/SKILL.md` |
| "Build a trust funding checklist" | `skills/trusts-estates/trust-funding-checklist/SKILL.md` |
| "Build a post-death administration task tracker" | `skills/trusts-estates/post-death-administration-task-tracker/SKILL.md` |
| "Intake estate, gift, GST, or inheritance tax issues" | `skills/trusts-estates/estate-tax-issue-intake/SKILL.md` |

### Family law

The Family Law skills produce **draft work product for a qualified, licensed attorney**. They organize facts and surface issues — they never calculate child or spousal support, recommend custody outcomes, draft pleadings, or supply safety plans. A potential domestic-violence concern routes to `domestic-violence-safety-referral-checklist` and to the attorney; the library does not create safety plans.

| The task sounds like... | Use this skill |
|---|---|
| "Open a new family law matter" | `skills/family-law/matter-intake/SKILL.md` |
| "Divorce or dissolution intake" | `skills/family-law/divorce-intake-organizer/SKILL.md` |
| "Build a custody / parenting chronology" | `skills/family-law/custody-parenting-facts-chronology/SKILL.md` |
| "Organize parenting schedule facts" | `skills/family-law/parenting-schedule-facts-organizer/SKILL.md` |
| "Review this custody or parenting order" | `skills/family-law/custody-order-review-checklist/SKILL.md` |
| "Child support facts intake" | `skills/family-law/child-support-facts-intake/SKILL.md` |
| "Spousal support / alimony facts intake" | `skills/family-law/spousal-support-facts-intake/SKILL.md` |
| "Build the asset and debt schedule" | `skills/family-law/asset-debt-schedule-builder/SKILL.md` |
| "Review this marital settlement / parenting / support agreement" | `skills/family-law/settlement-agreement-issue-spotter/SKILL.md` |
| "Family law discovery tracker" | `skills/family-law/discovery-tracker/SKILL.md` |
| "Family law hearing preparation" | `skills/family-law/hearing-prep-checklist/SKILL.md` |
| "Domestic violence safety referral considerations" | `skills/family-law/domestic-violence-safety-referral-checklist/SKILL.md` |

### Legal operations

| The task sounds like... | Use this skill |
|---|---|
| "Draft a response to this data subject request / litigation hold / vendor question" | `skills/legal-ops/templated-legal-response/SKILL.md` |
| "Prepare me for this meeting" / "build a meeting briefing" | `skills/legal-ops/legal-meeting-briefing/SKILL.md` |
| "Is this ready to sign?" / "set up signing for this document" | `skills/legal-ops/signature-routing-checklist/SKILL.md` |

### Setting up and configuring AgentCounsel

| The task sounds like... | Use this skill |
|---|---|
| "Configure the contracts practice" / "set up our contracts profile" | `skills/setup/contracts-cold-start-interview/SKILL.md` |
| "Configure the litigation practice" / "set up our litigation profile" | `skills/setup/litigation-cold-start-interview/SKILL.md` |
| "Configure the privacy practice" / "set up our privacy profile" | `skills/setup/privacy-cold-start-interview/SKILL.md` |
| "Configure the corporate practice" / "set up our corporate profile" | `skills/setup/corporate-cold-start-interview/SKILL.md` |
| "Configure the employment practice" / "set up our employment profile" | `skills/setup/employment-cold-start-interview/SKILL.md` |
| "Configure the IP practice" / "set up our IP profile" | `skills/setup/ip-cold-start-interview/SKILL.md` |
| "Configure the AI-governance practice" / "set up our AI-governance profile" | `skills/setup/ai-governance-cold-start-interview/SKILL.md` |
| "Configure the M&A practice" / "set up our M&A profile" | `skills/setup/m-and-a-cold-start-interview/SKILL.md` |
| "Configure the tax practice" / "set up our tax profile" | `skills/setup/tax-cold-start-interview/SKILL.md` |
| "Configure the trusts-and-estates practice" / "set up our trusts-and-estates profile" | `skills/setup/trusts-estates-cold-start-interview/SKILL.md` |
| "Configure the real-estate practice" / "set up our real-estate profile" | `skills/setup/real-estate-cold-start-interview/SKILL.md` |
| "Configure the securities practice" / "set up our securities profile" | `skills/setup/securities-capital-markets-cold-start-interview/SKILL.md` |
| "Configure the regulatory practice" / "set up our regulatory profile" | `skills/setup/regulatory-cold-start-interview/SKILL.md` |
| "Configure the antitrust practice" / "set up our antitrust profile" | `skills/setup/antitrust-competition-cold-start-interview/SKILL.md` |
| "Configure the bankruptcy practice" / "set up our bankruptcy profile" | `skills/setup/bankruptcy-restructuring-cold-start-interview/SKILL.md` |
| "Configure the insurance practice" / "set up our insurance profile" | `skills/setup/insurance-cold-start-interview/SKILL.md` |
| "Configure the family-law practice" / "set up our family-law profile" | `skills/setup/family-law-cold-start-interview/SKILL.md` |
| "Configure the product-legal practice" / "set up our product-legal profile" | `skills/setup/product-legal-cold-start-interview/SKILL.md` |
| "Set up a workspace for this matter" / "create a matter file" / "organize this matter" | `skills/setup/create-matter-workspace/SKILL.md` |

The cold-start interviews fill in a profile under `practice-profiles/`; `create-matter-workspace` sets up a single matter file under `matter-workspaces/` (see "Before you start" above). See also `COMMANDS.md` for command shorthands and `matter-workspaces/` for per-matter scaffolds.

### Methodology and verification

| The task sounds like... | Use this skill |
|---|---|
| "Red-team this draft" / "is this good enough?" / "check this memo, contract review, demand letter, or filing" / "find the weaknesses, missing issues, or hallucinations" | `skills/legal-methodology/red-team-verifier/SKILL.md` |
| "Interpret this provision" / "work through this statute or clause" | `skills/legal-methodology/statutory-interpretation/SKILL.md` |
| "Assess the legal risk" / "rate and prioritize these risks" | `skills/legal-methodology/risk-assessment/SKILL.md` |
| "Validate the sources" / "check these citations and claims" | `skills/legal-methodology/source-validation/SKILL.md` |

These cross-cutting skills support work in any practice area — run them alongside the practice-area skill, not instead of it.

**Final quality-control pass.** Run `red-team-verifier` after any high-stakes legal output — a memo, a contract or document review, a demand letter, a risk matrix, a client email, a research summary, or a draft filing — before it is finalized, sent, filed, or relied upon. It adversarially stress-tests the draft for invented authority, unsupported claims, weak legal reasoning, jurisdiction and deadline gaps, and professional-responsibility issues, and returns a PASS / REVISE verdict. It works on the output of any skill in this library, and on legal output produced by other tools or by a person. A PASS does not replace attorney review.

## Briefing a business stakeholder

When a skill's output needs to go to a non-lawyer decision-maker — a product owner, deal lead, manager, founder, or executive — ask for that skill's **optional Business Stakeholder Summary**. Most commercial skills (contracts, product legal, privacy, regulatory, employment, and corporate) can append one: a plain-language **Business Summary**, the **Decision Needed**, a **Recommended Ask**, a **Fallback Position**, and an **Escalation Needed?** call. It is an addition to the normal deliverable, not a replacement, and it does not change the attorney-review requirement. See `core/business-stakeholder-communication.md`.

## When several skills could apply

- **A contract that is an NDA** -> `nda-review` (not `contract-risk-review`).
- **A contract that is a DPA** -> `dpa-review`.
- **A contract that is a SOW** -> `sow-review`.
- **An AI vendor contract** -> `ai-vendor-terms-review` for the AI-specific terms; pair with `contract-risk-review` for the broader agreement and `dpa-review` for data terms.
- **A product launch that raises many issues** -> start with `launch-review`, which spots issues and routes to specialist skills.
- **A new AI use case** -> start with `ai-use-case-intake`, which triages and routes onward.
- **A received cease-and-desist letter** -> `cease-and-desist-response`; **drafting an outbound cease-and-desist or demand** -> `demand-letter`.
- **A possible IP infringement** -> `infringement-triage` for a first-pass factor triage; `fto-triage` for patent freedom-to-operate against specific patents; `trademark-clearance-triage` for clearing a proposed new mark.
- **Compliance work** -> `compliance-gap-matrix` for a one-time, point-in-time requirement-to-control gap analysis; `compliance-program-tracker` for ongoing tracking with an audit calendar and evidence management.
- **A vendor** -> `vendor-agreement-status` to inventory all agreements in place with the vendor; `contract-risk-review` (or `nda-review` / `sow-review` / `dpa-review`) to review one of those agreements for risk.

## When nothing matches

If the request does not fit a skill, do not invent a workflow. Tell the user the library does not yet cover the task and — if useful — point to the closest skill and explain the gap. New skills can be proposed per `CONTRIBUTING.md`.
