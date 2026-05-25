---
name: AI Use Case Intake
description: "Use when a new or modified AI/ML use case needs to be documented and triaged so legal, compliance, and governance teams can assess risk and route it to the right specialists."
practice_area: ai-governance
task_type: intake
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "Description of the proposed or modified AI/ML use case"
  - "The model or system involved and its provider"
  - "The data the use case will use, including any personal data"
  - "Intended users and the decisions the use case affects"
outputs:
  - "Structured AI use-case intake record"
  - "Preliminary risk signal"
  - "Routing recommendations to specialist reviewers"
related_skills:
  - skills/ai-governance/ai-vendor-terms-review/SKILL.md
  - skills/ai-governance/model-risk-triage/SKILL.md
  - skills/ai-governance/employee-ai-policy/SKILL.md
tags:
  - ai-governance
  - ai
  - intake
  - risk-triage
  - routing
---

# AI Use Case Intake

## Purpose

Produce a structured, attorney-ready intake record for a proposed or in-flight AI/ML use case. The record captures the information legal and compliance teams need to triage, route, and assess the use case — it does not render a legal conclusion about lawfulness or compliance. The preliminary risk tier is a triage signal only.

## Use When

- A product, engineering, or business team is proposing a new AI or ML feature, product, or workflow and needs legal sign-off or triage.
- An existing AI use case is being materially changed (new model, new data, new affected population, new market).
- Legal or compliance has received a question like "is this AI thing okay?" and needs a structured starting point.
- A governance or AI review committee requires a standardized intake record before approving a use case.
- A vendor is proposing an AI-enabled product or service and the organization must assess it before contracting.

## Required Inputs

- **Use case description**: A plain-language description of what the AI system does and why, provided by the requester.
- **AI system or model details**: The specific model(s), provider(s), or platform(s) involved (e.g., OpenAI GPT-4o via API, AWS SageMaker custom model, Microsoft Copilot).
- **Input data description**: What data goes into the model — sources, types, whether it includes personal data, and any sensitivity classifications.
- **Output description**: What the system produces and how outputs are used or acted upon.
- **Affected persons**: Who is impacted by the system's outputs (employees, consumers, job applicants, patients, students, etc.).
- **Deployment markets**: Countries and states or regions where the use case will operate.

If any required input is missing, stop and request it from the requester. Do not fabricate or assume facts about the system, data, or affected individuals.

## Do Not Use When

- You have a vendor AI contract to review — use `ai-vendor-terms-review` for that.
- You need to triage the risk of a specific model already under consideration — use `model-risk-triage`.
- The question is primarily about employee use of AI tools — use `employee-ai-policy`.
- The primary legal question is a data privacy assessment — route to the relevant privacy skill after completing this intake.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- The preliminary risk tier is a triage signal for routing, not a legal conclusion about lawfulness or compliance.
- Do not assert that any AI use case is lawful, compliant, or permissible under any law or regulation.
- Do not invent facts, citations, regulatory requirements, or legal standards.
- AI law and regulation is fast-moving and jurisdiction-specific; flag all jurisdiction-dependent questions for attorney verification.
- Separate facts provided by the requester, assumptions made in the intake, and open questions requiring verification.
- Do not embed client-sensitive facts into reusable templates; redact or generalize before storing.
- Use `[CONFIRM: ...]` placeholders wherever information is uncertain, incomplete, or requires attorney or compliance verification.

## Workflow

1. **Confirm inputs.** Verify all required inputs are present. If any are missing, stop and request them by name before proceeding.

2. **Capture the business purpose.** Summarize the use case in two to four sentences: what it does, why the organization wants it, and what decision or action it supports.

3. **Document the AI system.** Record the model(s), provider(s), API or platform, version or snapshot if known, and whether it is a foundation model, fine-tuned model, or custom-trained model.

4. **Document input and training data.** Record the data sources (internal, third-party, public), data types (text, images, audio, structured records), whether personal data is involved, any sensitive categories (health, financial, biometric, protected characteristics), and whether any of the data was or will be used to train or fine-tune the model. Flag any gaps in data provenance.

5. **Document outputs and decision use.** Record what the system outputs (scores, recommendations, generated text, classifications, etc.), whether outputs are used to make or inform consequential decisions about individuals, and what human review or override mechanisms exist.

6. **Document affected persons.** List all groups of people whose data is processed or who are affected by outputs. Note whether any are in protected categories (consumers, employees, minors, patients).

7. **Document human oversight design.** Describe the human-in-the-loop design: who reviews outputs, what decisions are fully automated vs. assisted, what escalation or appeal paths exist, and how errors are caught and corrected.

8. **Document deployment markets.** List every country, state, and region where the use case will operate or where affected individuals are located.

9. **Document vendor involvement.** List all third-party vendors, sub-processors, or API providers, and note which have signed data processing agreements or AI-specific terms.

10. **Assign a preliminary risk tier.** Using the information gathered, assign a triage risk tier — Low, Medium, or High — based on the following signals only (this is not a legal conclusion):
    - *High*: consequential decisions about individuals, sensitive personal data, regulated industry or context, high-volume or broad deployment, limited human oversight, novel or untested use case, multiple uncertain jurisdictions.
    - *Medium*: moderate impact on individuals, some personal data involved, human review present but not comprehensive, one or two uncertain regulatory questions.
    - *Low*: internal tooling with no personal data, no consequential individual decisions, well-understood technology, established oversight.

11. **Identify routing recommendations.** Based on the intake record, flag which specialist skills or teams should review the use case next (see Output Format below).

12. **Assemble the intake record.** Compile all sections into the structured output, label it as a draft for attorney review, and include all assumptions and open items.

## Output Format

Deliver the following sections in order:

**1. Intake Summary**
A two-to-four sentence plain-language summary of the use case, system, and key risk signals.

**2. Use Case Record**

| Field | Detail |
|---|---|
| Business purpose | |
| AI system / model | |
| Provider / platform | |
| Model type | |
| Input data sources | |
| Personal data involved | Yes / No / `[CONFIRM]` |
| Sensitive data categories | |
| Training data use | `[CONFIRM]` if unknown |
| Output type | |
| Decision use | |
| Consequential decisions about individuals | Yes / No / `[CONFIRM]` |
| Human oversight design | |
| Affected persons | |
| Deployment markets | |
| Vendor involvement | |
| Data processing agreements in place | Yes / No / Partial / `[CONFIRM]` |

**3. Preliminary Risk Tier**
State Low / Medium / High and list the two to five signals that drove the tier. Note that this is a triage signal only, not a legal conclusion.

**4. Routing Recommendations**
Bullet list of recommended next steps and skill or team referrals, for example:
- `ai-vendor-terms-review` — if vendor AI terms have not been reviewed.
- `model-risk-triage` — if the model's reliability, bias, or failure modes need deeper assessment.
- Privacy / DPA review — if personal data is processed.
- IP review — if training data rights or output ownership are uncertain.
- `employee-ai-policy` — if the use case involves employees using AI tools.
- Regulatory specialist — if a regulated industry (financial services, health, employment) is involved.

**5. Open Items and Assumptions**
Bullet list of every `[CONFIRM: ...]` item and assumption recorded during the intake.

**6. Attorney Triage Flag**
A single highlighted note: whether the intake record should be escalated to attorney review before the use case proceeds, and the primary reason.

*Label the full document: DRAFT — For Attorney Review — Not Legal Advice.*

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — the requesting product owner, business sponsor, AI governance committee, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language: the use case, its preliminary risk tier, and the two or three signals that drove the tier.
- **Decision Needed** — the specific business decision(s) now on the table (proceed to specialist review / pause / proceed without further review), stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended next step (which specialist reviews to run, with what scope), framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the AI governance committee, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] All required inputs have been provided and are accurate; nothing has been assumed or fabricated.
- [ ] The business purpose and system description match the requester's actual intent.
- [ ] Data sources, data types, and personal data involvement have been confirmed with the technical or product team.
- [ ] Training data use has been confirmed with the vendor or engineering team, not assumed.
- [ ] The affected persons list is complete, including any indirect impacts.
- [ ] All deployment markets have been identified, including markets where affected individuals are located.
- [ ] Vendor involvement and DPA status have been confirmed with procurement or legal operations.
- [ ] The preliminary risk tier has been reviewed by an attorney and adjusted as needed — it is a triage signal, not a legal conclusion.
- [ ] All open items and `[CONFIRM: ...]` placeholders have been resolved before the use case proceeds.
- [ ] Routing recommendations have been acted upon and the relevant specialist reviews have been completed.
- [ ] No AI-specific law, regulation, or legal standard has been asserted without attorney verification.
