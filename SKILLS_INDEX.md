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
| Contracts | Vendor Agreement Status | `skills/contracts/vendor-agreement-status/SKILL.md` | Consolidating the agreements in place with a vendor into a status report | Vendor identity, agreement records, relationship context | Vendor agreement status report |
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
| Regulatory | Compliance Program Tracker | `skills/regulatory/compliance-program-tracker/SKILL.md` | Tracking framework requirements, controls, evidence, and audit dates over time | Framework source, control inventory, audit context | Compliance program tracker |
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
| Financial Crime / AML | KYC Onboarding Review | `skills/financial-crime/kyc-onboarding-review/SKILL.md` | Reviewing a client or investor onboarding packet against the firm's KYC/AML rules | Onboarding packet, KYC/AML rules grid, screening results | KYC onboarding review |
| Financial Crime / AML | Sanctions Screening Review | `skills/financial-crime/sanctions-screening-review/SKILL.md` | Adjudicating sanctions, PEP, and adverse-media screening hits by confidence | Screening results, party identifiers, disposition policy | Screening review |
| Real Estate | Lease Abstract | `skills/real-estate/lease-abstract/SKILL.md` | Extracting commercial lease terms into a structured, source-cited abstract | Lease document, property type, party role | Source-cited lease abstract |
| Real Estate | Lease Amendment Reconciliation | `skills/real-estate/lease-amendment-reconciliation/SKILL.md` | Reconciling a base lease and its amendments to the current controlling terms | Base lease, amendments, side letters, party role | Controlling-term table |
| Real Estate | Commercial Lease Review | `skills/real-estate/commercial-lease-review/SKILL.md` | Issue-spotting a commercial lease from a specified party's perspective | Lease, party perspective, property type | Risk matrix + issue list |
| Real Estate | Purchase and Sale Agreement Review | `skills/real-estate/psa-review/SKILL.md` | Reviewing a real estate purchase and sale agreement from a party's perspective | PSA text, party perspective, property type | Risk matrix + issue list |
| Real Estate | Title and Survey Objection Tracker | `skills/real-estate/title-survey-objection-tracker/SKILL.md` | Organizing title exceptions and survey matters into a tracked objection list | Title commitment, survey, parcel(s) | Objection tracker |
| Real Estate | Real Estate Diligence Checklist | `skills/real-estate/real-estate-diligence-checklist/SKILL.md` | Generating a tailored real estate due-diligence checklist | Transaction type, property type, jurisdiction, party role | Diligence checklist + request list |
| Real Estate | Closing Deliverables Tracker | `skills/real-estate/closing-deliverables-tracker/SKILL.md` | Building a closing-deliverables checklist for a real estate deal | Transaction type, party role, transaction agreement | Closing deliverables tracker |
| Real Estate | Estoppel and SNDA Review | `skills/real-estate/estoppel-snda-review/SKILL.md` | Reviewing estoppels and SNDAs and comparing them against the lease | Estoppel or SNDA, perspective, lease if available | Issue list + discrepancy table |
| Real Estate | Zoning and Use Restriction Issue Spotter | `skills/real-estate/zoning-use-restriction-issue-spotter/SKILL.md` | Issue-spotting zoning and use-restriction concerns from provided materials | Intended use, provided materials, jurisdiction | Issue list + questions for local counsel |
| Mergers & Acquisitions | LOI and Term Sheet Review | `skills/m-and-a/loi-term-sheet-review/SKILL.md` | Reviewing an LOI, term sheet, or IOI for deal terms and binding provisions | LOI or term sheet, side, deal type | Binding/non-binding table + issue list |
| Mergers & Acquisitions | Acquisition Diligence Request List | `skills/m-and-a/acquisition-diligence-request-list/SKILL.md` | Generating a tailored M&A diligence request list by workstream | Deal type, industry, target profile, side | Diligence request list |
| Mergers & Acquisitions | Data Room Index Review | `skills/m-and-a/data-room-index-review/SKILL.md` | Reviewing a data room index for diligence coverage gaps | Data room index, deal type, side | Data-room gap matrix |
| Mergers & Acquisitions | Purchase Agreement Issue List | `skills/m-and-a/purchase-agreement-issue-list/SKILL.md` | Reviewing an acquisition agreement from a buyer or seller perspective | Purchase agreement, side, deal type | Issue list + risk matrix |
| Mergers & Acquisitions | Reps and Warranties Disclosure Schedule Review | `skills/m-and-a/reps-warranties-disclosure-schedule-review/SKILL.md` | Comparing reps and warranties against the disclosure schedules | Reps article, disclosure schedules, side | Rep-by-rep review table |
| Mergers & Acquisitions | Indemnity and Escrow Risk Review | `skills/m-and-a/indemnity-escrow-risk-review/SKILL.md` | Analyzing indemnity and escrow architecture and recovery mechanics | Indemnity and escrow provisions, side | Indemnity architecture + risk matrix |
| Mergers & Acquisitions | M&A Closing Deliverables Tracker | `skills/m-and-a/closing-deliverables-tracker/SKILL.md` | Building a closing-deliverables checklist for an M&A transaction | Deal type, side, agreement and ancillary documents | Closing deliverables tracker |
| Mergers & Acquisitions | Third-Party Consents and Assignment Review | `skills/m-and-a/third-party-consents-assignment-review/SKILL.md` | Identifying consent and change-of-control issues from diligence contracts | Contracts or diligence summaries, deal structure, side | Consent tracker |
| Mergers & Acquisitions | Post-Closing Obligations Tracker | `skills/m-and-a/post-closing-obligations-tracker/SKILL.md` | Extracting post-closing obligations from the acquisition agreement | Acquisition agreement and ancillary documents, side | Post-closing obligation tracker |
| Securities / Capital Markets | Private Placement Checklist | `skills/securities-capital-markets/private-placement-checklist/SKILL.md` | Building private offering process checklist by workstream | Offering facts, issuer status, investor profile, source docs | Checklist tracker |
| Securities / Capital Markets | Securities Exemption Issue Spotter | `skills/securities-capital-markets/securities-exemption-issue-spotter/SKILL.md` | Spotting exemption pathways and missing facts without conclusions | Offering structure, investor facts, solicitation facts | Pathway/risk matrix |
| Securities / Capital Markets | Offering Document Disclosure Review | `skills/securities-capital-markets/offering-document-disclosure-review/SKILL.md` | Reviewing PPM/prospectus/registration disclosure issues | Draft disclosure documents and sources | Disclosure issue list |
| Securities / Capital Markets | Risk Factor Review | `skills/securities-capital-markets/risk-factor-review/SKILL.md` | Reviewing risk factor specificity and consistency | Risk factors plus related disclosures | Risk factor inventory |
| Securities / Capital Markets | SEC Filing Consistency Check | `skills/securities-capital-markets/sec-filing-consistency-check/SKILL.md` | Cross-checking filing drafts for inconsistencies | Multiple SEC filing drafts or excerpts | Inconsistency tracker |
| Securities / Capital Markets | Form D and Blue Sky Tracker | `skills/securities-capital-markets/form-d-blue-sky-tracker/SKILL.md` | Tracking Form D / state notice workflow facts | Offering facts, investor jurisdictions, source docs | Filing tracker |
| Securities / Capital Markets | Investor Rights Agreement Review | `skills/securities-capital-markets/investor-rights-agreement-review/SKILL.md` | Reviewing investor rights and governance agreements | Agreement set, role perspective | Key terms + risk matrix |
| Securities / Capital Markets | Insider Trading Policy Review | `skills/securities-capital-markets/insider-trading-policy-review/SKILL.md` | Reviewing insider-trading governance and procedures | Policy documents, covered-person definitions | Policy issue list |
| Securities / Capital Markets | Section 16 and Beneficial Ownership Triage | `skills/securities-capital-markets/section-16-beneficial-ownership-triage/SKILL.md` | Organizing ownership/reporting facts for counsel review | Ownership data, role/status facts, source docs | Facts-to-verify table |
| Securities / Capital Markets | Capital Markets Closing Checklist | `skills/securities-capital-markets/capital-markets-closing-checklist/SKILL.md` | Building offering closing deliverables and dependencies tracker | Transaction docs and role assignments | Closing tracker |
| Securities / Capital Markets | Comfort and Backup Request Tracker | `skills/securities-capital-markets/comfort-backup-request-tracker/SKILL.md` | Tracking factual support and comfort-style requests | Offering docs, metrics claims, source references | Numbered request tracker |
| Securities / Capital Markets | Public Company Reporting Calendar Intake | `skills/securities-capital-markets/public-company-reporting-calendar-intake/SKILL.md` | Intaking reporting workflow facts for calendar drafting | Filer profile, governance cadence, workflow facts | Intake checklist + matrix |
| Mergers & Acquisitions | Integration Legal Issues Checklist | `skills/m-and-a/integration-legal-issues-checklist/SKILL.md` | Generating a legal integration checklist by workstream | Deal type, pre/post-close status, target profile | Integration legal checklist |
| Tax | Tax Issue Intake | `skills/tax/tax-issue-intake/SKILL.md` | Intaking a tax-sensitive matter and mapping the tax issues for a professional | Taxpayer/entity type, jurisdictions, tax period, activity facts, source docs | Intake summary + tax issue map |
| Tax | Entity Tax Classification Checklist | `skills/tax/entity-tax-classification-checklist/SKILL.md` | Organizing entity formation, ownership, and election facts for classification review | Entity type, formation, ownership, governing documents, elections | Classification facts table + questions |
| Tax | Transaction Tax Diligence Request List | `skills/tax/transaction-tax-diligence-request-list/SKILL.md` | Building a transaction tax diligence request list by workstream | Transaction type, jurisdictions, role, workstreams, documents | Request list + follow-up tracker |
| Tax | Sales Use Tax Nexus Triage | `skills/tax/sales-use-tax-nexus-triage/SKILL.md` | Mapping sales/use tax nexus facts jurisdiction by jurisdiction | Jurisdictions, product/service type, presence and activity facts | Nexus fact map + jurisdiction tracker |
| Tax | Employment Tax Worker Classification Intake | `skills/tax/employment-tax-worker-classification-intake/SKILL.md` | Intaking worker and payroll facts for employment-tax classification review | Worker roles, engagement and payment facts, contracts, payroll records | Facts-to-verify table + risk themes |
| Tax | Tax Provision Review Checklist | `skills/tax/tax-provision-review-checklist/SKILL.md` | Reviewing the tax provisions of a contract and flagging negotiation points | Agreement text, role/perspective, transaction type, tax sections | Key tax terms table + risk matrix |
| Tax | Tax Document Organizer | `skills/tax/tax-document-organizer/SKILL.md` | Organizing a tax document set into a source-cited inventory with masked identifiers | Tax returns, notices, and supporting records | Document inventory + missing-docs list |
| Tax | Tax Covenants Indemnities Review | `skills/tax/tax-covenants-indemnities-review/SKILL.md` | Mapping tax covenant and indemnity architecture for tax counsel | Transaction agreement, role/perspective, transaction type | Covenant/indemnity review table |
| Tax | International Tax Issue Spotter | `skills/tax/international-tax-issue-spotter/SKILL.md` | Issue-spotting cross-border tax questions without conclusions | Cross-border structure, jurisdictions, activity facts, source docs | International tax issue map |
| Tax | Crypto Digital Asset Tax Intake | `skills/tax/crypto-digital-asset-tax-intake/SKILL.md` | Intaking crypto and digital-asset activity and records for a tax professional | Wallet/exchange accounts, transaction types, tax period, records | Intake matrix + missing-records list |
| Bankruptcy / Restructuring | Bankruptcy Matter Intake | `skills/bankruptcy-restructuring/bankruptcy-matter-intake/SKILL.md` | Capturing the facts of a bankruptcy or restructuring matter | Parties, party role, case status, chapter/court if known, document set | Matter summary + risk themes |
| Bankruptcy / Restructuring | Creditor Claim Intake | `skills/bankruptcy-restructuring/creditor-claim-intake/SKILL.md` | Organizing a creditor's facts for a potential bankruptcy claim | Debtor/creditor, claim basis, amount as stated, collateral, disputes | Claim facts table + dispute flags |
| Bankruptcy / Restructuring | Proof of Claim Checklist | `skills/bankruptcy-restructuring/proof-of-claim-checklist/SKILL.md` | Building a proof-of-claim preparation checklist and document tracker | Claimant, debtor/case, claim basis, supporting documents | Preparation checklist + document tracker |
| Bankruptcy / Restructuring | Automatic Stay Issue Spotter | `skills/bankruptcy-restructuring/automatic-stay-issue-spotter/SKILL.md` | Issue-spotting automatic stay concerns from user-provided facts | Debtor, party role, the actions or proceedings in question | Stay-risk fact map + escalation flags |
| Bankruptcy / Restructuring | Preference Demand Response Triage | `skills/bankruptcy-restructuring/preference-demand-response-triage/SKILL.md` | Organizing the facts for responding to a preference demand | Demand letter, alleged transfers, invoice and payment history | Transfer timeline + defense-facts checklist |
| Bankruptcy / Restructuring | Executory Contract Assumption Rejection Checklist | `skills/bankruptcy-restructuring/executory-contract-assumption-rejection-checklist/SKILL.md` | Organizing executory contract and unexpired lease facts for review | Contract identity, roles, cure amounts as provided, defaults | Contract status table + cure/default tracker |
| Bankruptcy / Restructuring | Bankruptcy Diligence Request List | `skills/bankruptcy-restructuring/bankruptcy-diligence-request-list/SKILL.md` | Generating a bankruptcy or distressed-transaction diligence request list | Transaction/matter type, party role, workstreams in scope | Request list by workstream + tracker |
| Bankruptcy / Restructuring | Restructuring Term Sheet Review | `skills/bankruptcy-restructuring/restructuring-term-sheet-review/SKILL.md` | Reviewing a restructuring support, forbearance, or workout document | The document, party role/perspective, parties, debt instruments | Key terms table + issue list |
| Bankruptcy / Restructuring | Plan Disclosure Statement Issue Spotter | `skills/bankruptcy-restructuring/plan-disclosure-statement-issue-spotter/SKILL.md` | Issue-spotting a Chapter 11 plan and disclosure statement | The plan/disclosure statement, party role, treatment provisions | Treatment table + issue list |
| Bankruptcy / Restructuring | Distressed Asset Sale Checklist | `skills/bankruptcy-restructuring/distressed-asset-sale-checklist/SKILL.md` | Building a bankruptcy or distressed asset-sale checklist and trackers | Asset description, sale process, party role, sale documents | Sale checklist + closing trackers |
| Bankruptcy / Restructuring | Cash Collateral DIP Financing Issue Spotter | `skills/bankruptcy-restructuring/cash-collateral-dip-financing-issue-spotter/SKILL.md` | Issue-spotting a cash collateral or DIP financing document | The financing document, party role, lenders, collateral, budget | Key terms table + issue list |
| Bankruptcy / Restructuring | Bankruptcy Deadline Tracker Intake | `skills/bankruptcy-restructuring/bankruptcy-deadline-tracker-intake/SKILL.md` | Intaking user-provided bankruptcy dates into a draft tracker for verification | Dates the user provides with sources, party role, task deadlines | Draft deadline tracker |
| Insurance | Insurance Policy Summary | `skills/insurance/insurance-policy-summary/SKILL.md` | Summarizing an insurance policy into a source-cited overview | Policy document set, policy type, role, policy period | Source-cited policy summary |
| Insurance | Coverage Issue Spotter | `skills/insurance/coverage-issue-spotter/SKILL.md` | Issue-spotting coverage questions from a policy and claim | Policy, claim facts, tender, pleadings, role | Coverage issue matrix |
| Insurance | Claims Chronology Builder | `skills/insurance/claims-chronology-builder/SKILL.md` | Building a source-cited claim chronology from the claim file | Notices, correspondence, adjuster notes, payment history | Claim chronology |
| Insurance | Reservation of Rights Review | `skills/insurance/reservation-of-rights-review/SKILL.md` | Reviewing a reservation of rights letter or coverage correspondence | ROR letter or correspondence, the policy, role | Issue list + provision-reference table |
| Insurance | Tender Letter Review | `skills/insurance/tender-letter-review/SKILL.md` | Reviewing a tender, claim notice, or additional insured tender | Tender letter, asserted policy/contract basis, role | Tender completeness checklist + risk flags |
| Insurance | Coverage Position Outline | `skills/insurance/coverage-position-outline/SKILL.md` | Assembling a coverage-position outline for a coverage attorney | Policy, claim facts, correspondence, role, claim stage | Coverage-position outline |
| Insurance | Bad Faith Risk Triage | `skills/insurance/bad-faith-risk-triage/SKILL.md` | Issue-spotting claim-handling and bad-faith risk themes | Claim file materials, the policy, role, claim stage | Risk-theme list + questions for counsel |
| Insurance | Certificate of Insurance Review | `skills/insurance/certificate-of-insurance-review/SKILL.md` | Reviewing certificates of insurance against contract requirements | Certificate(s), endorsements, contract requirements | COI comparison table |
| Insurance | Insurance Requirements Contract Review | `skills/insurance/insurance-requirements-contract-review/SKILL.md` | Reviewing the insurance and indemnity clauses of a contract | Contract, contract type, role | Requirements table + risk matrix |
| Insurance | Subrogation Recovery Tracker | `skills/insurance/subrogation-recovery-tracker/SKILL.md` | Organizing potential subrogation and recovery facts from a loss | Loss facts, payment documents, contracts, policy provisions | Recovery fact map |
| Insurance | Policy Renewal Placement Diligence Checklist | `skills/insurance/policy-renewal-placement-diligence-checklist/SKILL.md` | Generating a legal and compliance diligence checklist for a renewal or placement | Renewal context, expiring policies, claims history, lines in scope | Diligence checklist + document requests |
| Insurance | Insurer Insured Communications Review | `skills/insurance/insurer-insured-communications-review/SKILL.md` | Reviewing insurer, insured, claimant, or broker communications | Communications, policy/claim context, role, review purpose | Communication issue list + suggested edits |
| Family Law | Family Law Matter Intake | `skills/family-law/family-law-matter-intake/SKILL.md` | Capturing a new family law matter in a structured intake | Parties and roles, matter type, case stage, jurisdiction, issues, safety concerns | Intake summary + issue map |
| Family Law | Divorce Intake Organizer | `skills/family-law/divorce-intake-organizer/SKILL.md` | Organizing the facts of a divorce or dissolution matter | Marriage/separation dates, children, income, assets, debts, posture | Divorce facts table + issue map |
| Family Law | Custody / Parenting Facts Chronology | `skills/family-law/custody-parenting-facts-chronology/SKILL.md` | Building a source-cited parenting and caregiving chronology | Communications, records, incident notes, orders, schedules | Custody/parenting chronology |
| Family Law | Parenting Schedule Facts Organizer | `skills/family-law/parenting-schedule-facts-organizer/SKILL.md` | Organizing the facts relevant to a parenting schedule discussion | Current/proposed schedule, school, transportation, holidays, distance | Schedule facts table + conflict list |
| Family Law | Child Support Facts Intake | `skills/family-law/child-support-facts-intake/SKILL.md` | Gathering the facts relevant to a child support review | Jurisdiction, children, income facts, costs, existing orders | Support facts intake table |
| Family Law | Spousal Support Facts Intake | `skills/family-law/spousal-support-facts-intake/SKILL.md` | Gathering the facts relevant to a spousal support or alimony review | Jurisdiction, duration, income, expenses, employment, disclosures | Support facts intake table |
| Family Law | Asset / Debt Schedule Builder | `skills/family-law/asset-debt-schedule-builder/SKILL.md` | Building a source-cited property and debt schedule | Statements, deeds, account and loan records, user-provided values | Asset/debt schedule |
| Family Law | Domestic Violence Safety Referral Checklist | `skills/family-law/domestic-violence-safety-referral-checklist/SKILL.md` | Organizing facts and referral/escalation for a safety concern | Safety concerns, protective orders, records, court dates | Safety/escalation flags + referral checklist |
| Family Law | Family Law Discovery Tracker | `skills/family-law/family-law-discovery-tracker/SKILL.md` | Organizing family-law discovery requests, responses, and disclosures | Discovery set, response status, deficiencies, role | Discovery tracker |
| Family Law | Settlement Agreement Issue Spotter | `skills/family-law/settlement-agreement-issue-spotter/SKILL.md` | Reviewing a marital settlement, parenting, or support agreement | Agreement text, parties, matter type, jurisdiction | Key terms table + issue list |
| Family Law | Custody Order Review Checklist | `skills/family-law/custody-order-review-checklist/SKILL.md` | Reviewing a custody or parenting order for clarity and administration | Order text, parties, children, jurisdiction | Order-clarity checklist + ambiguity table |
| Family Law | Family Law Hearing Prep Checklist | `skills/family-law/family-law-hearing-prep-checklist/SKILL.md` | Building a hearing-preparation checklist for a family law hearing | Hearing type, pleadings, declarations, exhibits, witnesses | Hearing-prep checklist |
| Legal Operations | Templated Legal Response | `skills/legal-ops/templated-legal-response/SKILL.md` | Drafting a templated response to a recurring legal inquiry with an escalation gate | The inquiry, response template, customization facts | Draft response + escalation check |
| Legal Operations | Legal Meeting Briefing | `skills/legal-ops/legal-meeting-briefing/SKILL.md` | Preparing a structured briefing for a meeting with legal relevance | Meeting context, background materials | Meeting briefing + action tracker |
| Legal Operations | Signature Routing Checklist | `skills/legal-ops/signature-routing-checklist/SKILL.md` | Running a pre-signature readiness check and routing plan for a final document | The document, intended signers, approvals | Signature readiness review |
| Setup | Contracts Cold-Start Interview | `skills/setup/contracts-cold-start-interview/SKILL.md` | Interviewing a contracts practice group to fill its practice profile | Access to a contracts attorney or designee | Filled practice profile draft |
| Setup | Litigation Cold-Start Interview | `skills/setup/litigation-cold-start-interview/SKILL.md` | Interviewing a litigation practice group to fill its practice profile | Access to a litigation attorney or designee | Filled practice profile draft |
| Setup | Privacy Cold-Start Interview | `skills/setup/privacy-cold-start-interview/SKILL.md` | Interviewing a privacy practice group to fill its practice profile | Access to a privacy attorney or designee | Filled practice profile draft |
| Setup | Corporate Cold-Start Interview | `skills/setup/corporate-cold-start-interview/SKILL.md` | Interviewing a corporate practice group to fill its practice profile | Access to a corporate attorney or designee | Filled practice profile draft |
| Setup | Create Matter Workspace | `skills/setup/create-matter-workspace/SKILL.md` | Selecting a matter template and producing a populated workspace draft for a new matter | Matter type, client, responsible attorney, known parties / dates / documents | Populated matter workspace draft |
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
- **Financial Crime / AML** — KYC onboarding review and sanctions / PEP / adverse-media screening review.
- **Real Estate** — commercial lease abstraction and review, amendment reconciliation, purchase and sale agreement review, title and survey objection tracking, diligence and closing checklists, estoppel and SNDA review, and zoning and use-restriction issue spotting.
- **Mergers & Acquisitions** — LOI and term-sheet review, acquisition diligence request lists and data-room review, purchase-agreement and disclosure-schedule review, indemnity and escrow analysis, third-party consents, and closing, post-closing, and integration tracking.
- **Antitrust / Competition** — antitrust risk intake, competitor-collaboration and information-sharing review, pricing-algorithm and distribution-restraint review, merger issue-spotting, gun-jumping checklists, and compliance-policy review.
- **Securities / Capital Markets** — private and public offerings, exemption issue-spotting, offering-document and risk-factor review, SEC filing consistency, Form D and blue-sky tracking, investor-rights and insider-trading review, beneficial-ownership triage, and capital-markets closings.
- **Tax** — tax issue intake, entity tax-classification facts, transaction tax diligence, sales/use tax nexus triage, employment-tax worker-classification intake, contract tax-provision and covenant/indemnity review, tax document organization, international tax issue-spotting, and crypto/digital-asset tax intake.
- **Bankruptcy / Restructuring** — bankruptcy and creditor-claim intake, proof-of-claim checklists, automatic-stay and preference issue-spotting, executory-contract assumption/rejection review, distressed-M&A diligence and asset-sale checklists, restructuring term-sheet review, plan and disclosure-statement issue-spotting, DIP financing issue-spotting, and deadline-tracker intake.
- **Insurance** — insurance policy summaries, coverage issue-spotting, claim chronologies, reservation of rights and tender review, coverage-position outlines, bad-faith risk triage, certificate of insurance and contract insurance-requirements review, subrogation/recovery tracking, and renewal/placement diligence checklists.
- **Family Law** — family law matter intake, divorce intake organization, custody and parenting chronologies and schedule organization, child and spousal support facts intake, property and debt schedules, domestic violence safety referral checklists, discovery tracking, settlement-agreement issue-spotting, custody-order review, and hearing-prep checklists.
- **Legal Operations** — templated legal responses, meeting briefings, and signature routing.
- **Setup** — cold-start interviews that configure AgentCounsel for a practice group by filling in a practice profile.
- **Legal Methodology** — cross-cutting analytical disciplines: red-team verification, statutory interpretation, risk assessment, and source validation.

## Related references

- `practice-profiles/` — per-practice-area configuration profiles an agent loads alongside `core/` and a skill.
- `matter-workspaces/` — single-file scaffolds for organizing one specific matter.
- `COMMANDS.md` — slash-style command shorthands mapped to these skills.
- `skills/contracts/references/` — shared reference material for the contracts skills.
- `skills/m-and-a/references/` — shared M&A output-pattern reference for the M&A skills.
- `skills/tax/references/` — shared Tax output-pattern reference for the Tax skills.
- `skills/bankruptcy-restructuring/references/` — shared Bankruptcy / Restructuring output-pattern reference for those skills.


## Antitrust / Competition

- `skills/antitrust-competition/antitrust-risk-intake/SKILL.md`
- `skills/antitrust-competition/competitor-collaboration-review/SKILL.md`
- `skills/antitrust-competition/information-sharing-clean-team-review/SKILL.md`
- `skills/antitrust-competition/pricing-algorithm-risk-triage/SKILL.md`
- `skills/antitrust-competition/distribution-restraints-review/SKILL.md`
- `skills/antitrust-competition/exclusivity-mfn-pricing-review/SKILL.md`
- `skills/antitrust-competition/merger-antitrust-issue-spotter/SKILL.md`
- `skills/antitrust-competition/gun-jumping-clean-team-checklist/SKILL.md`
- `skills/antitrust-competition/trade-association-meeting-review/SKILL.md`
- `skills/antitrust-competition/antitrust-compliance-policy-review/SKILL.md`

## Insurance

- `skills/insurance/insurance-policy-summary/SKILL.md`
- `skills/insurance/coverage-issue-spotter/SKILL.md`
- `skills/insurance/claims-chronology-builder/SKILL.md`
- `skills/insurance/reservation-of-rights-review/SKILL.md`
- `skills/insurance/tender-letter-review/SKILL.md`
- `skills/insurance/coverage-position-outline/SKILL.md`
- `skills/insurance/bad-faith-risk-triage/SKILL.md`
- `skills/insurance/certificate-of-insurance-review/SKILL.md`
- `skills/insurance/insurance-requirements-contract-review/SKILL.md`
- `skills/insurance/subrogation-recovery-tracker/SKILL.md`
- `skills/insurance/policy-renewal-placement-diligence-checklist/SKILL.md`
- `skills/insurance/insurer-insured-communications-review/SKILL.md`
