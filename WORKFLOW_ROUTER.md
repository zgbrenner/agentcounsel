# AgentCounsel — Workflow Router

This guide maps a task to the right skill. Use it to go from "I need to do X" to the correct `SKILL.md`.

> Before running any skill, read the `core/` operating rules. Every skill produces **draft legal work product for attorney review** — never legal advice.

## How routing works

1. Identify the task type from the user's request.
2. Match it to a row below and open that `SKILL.md`.
3. If the request spans several skills, pick the **narrowest** one that fits the immediate task; the skill will point to siblings if needed.
4. If nothing matches, say so — do not improvise a legal workflow.

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
