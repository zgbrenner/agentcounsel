---
name: Model Risk Triage
description: "Use when triaging the legal and governance risk of a specific AI model or AI system before or during deployment, to produce a structured risk register and recommended controls for attorney and governance review."
practice_area: ai-governance
task_type: triage
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "Description of the AI model or system"
  - "Its intended use and deployment context"
  - "The data it processes and its individual-facing outputs"
outputs:
  - "Structured risk register"
  - "Risk tier"
  - "Recommended controls for attorney and governance review"
related_skills:
  - skills/ai-governance/ai-use-case-intake/SKILL.md
  - skills/ai-governance/ai-vendor-terms-review/SKILL.md
  - skills/product-legal/ai-feature-review/SKILL.md
  - skills/privacy/pia-generation/SKILL.md
tags:
  - ai-governance
  - ai
  - model-risk
  - risk-triage
  - controls
---

# Model Risk Triage

## Purpose

Produce a structured triage of the legal, governance, and operational risk dimensions of a specific AI model or AI system. The output is a risk register with ownership assignments and recommended controls — not a legal opinion on whether the model may be deployed. It equips attorneys and governance reviewers with the structured information they need to make deployment decisions.

This skill is model-level and technical in focus. It complements `ai-use-case-intake` (which covers the business use case) and `ai-vendor-terms-review` (which covers vendor contractual terms).

## Use When

- Engineering, product, or legal teams need to assess a specific model before integration or deployment.
- A governance committee requires a pre-deployment risk assessment for an AI model.
- A model is being upgraded, retrained, or replaced and a delta risk assessment is needed.
- An audit, incident, or regulatory inquiry requires documentation of what risk assessment was performed before deployment.
- A user asks "what are the risks of using this model?" or "what do we need to have in place before we deploy this?"

## Required Inputs

- **Model identification**: Name, version, provider or source (vendor API, open-source repository, internally trained), and a link to model documentation or model card if available.
- **Intended use description**: How the organization plans to use the model — inputs, outputs, and the decision or action outputs will inform or automate.
- **Affected individuals**: Who will be impacted by the model's outputs (employees, consumers, patients, job applicants, etc.) and the estimated population size or scope.
- **Deployment context**: The application, product, or system the model will be embedded in, and whether outputs will be directly user-facing.
- **Available technical documentation**: Model card, data sheet, evaluation reports, accuracy benchmarks, bias evaluation results — whatever is available. Note what is not available.

If the model identification and intended use are not provided, stop and request them. Do not fabricate technical facts, benchmark results, or model characteristics. If documentation is not available, flag the gap explicitly.

## Do Not Use When

- The question is about whether to adopt an AI use case at all — start with `ai-use-case-intake`.
- The primary question is about the vendor's contractual terms — use `ai-vendor-terms-review`.
- The question is about internal employee use of AI tools — use `employee-ai-policy`.
- A full algorithmic audit or technical bias evaluation is required — this triage identifies the need for specialist review; it does not perform the technical evaluation.
- The model is used solely for internal tooling with no individual-facing outputs and no personal data — a lightweight intake record may suffice.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Do not assert that a model is safe, unbiased, accurate, or fit for a particular use — flag these as matters requiring technical and legal verification.
- Do not fabricate benchmark results, accuracy metrics, or technical characteristics. If documentation is not provided, state that the information is unavailable.
- Do not assert that any law or regulation applies to the model or its use; flag potential regulatory considerations for attorney review.
- AI regulation is fast-moving and jurisdiction-specific — regulatory risk items require attorney verification.
- Bias and fairness issues require specialist (technical and legal) review; this triage identifies the need, it does not resolve it.
- Distinguish facts from the provided documentation, assumptions, and open items requiring verification.
- Use `[CONFIRM: ...]` placeholders wherever information is missing or uncertain.

## Workflow

1. **Confirm inputs.** Verify all required inputs are present. Document which technical materials were provided and which are missing.

2. **Characterize the model.** Record the model type (generative, classification, regression, ranking, etc.), architecture if known, training data description as disclosed, known evaluation benchmarks, and the provider's own characterization of intended use and limitations from any model card or documentation.

3. **Assess intended use and foreseeable misuse.** Compare the organization's intended use to the provider's stated intended use and known limitations. Identify foreseeable misuse scenarios — including use outside the intended context, adversarial inputs, prompt injection (for LLMs), and use by unexpected user populations.

4. **Assess affected individuals and potential harms.** Identify who is affected and how: direct users, downstream affected individuals, third parties. Assess the severity and reversibility of potential harms from model errors or misuse (physical, financial, reputational, discriminatory, legal). Flag high-severity or irreversible harm scenarios.

5. **Assess accuracy and reliability.** Summarize available accuracy, precision, recall, or performance metrics from documentation. Identify known failure modes, edge cases, and performance degradation scenarios. Flag uses where accuracy requirements are high and the model's documented performance is insufficient or unknown. Note if independent evaluation has not been performed.

6. **Assess bias and fairness considerations.** Identify whether the model has been evaluated for disparate performance across demographic groups relevant to the use case (race, sex, age, disability, national origin, and others depending on context). Flag any known bias findings from documentation. Note that this assessment identifies the need for specialist review — it does not constitute a bias evaluation. Recommend specialist review if the use case involves consequential decisions about individuals in protected categories.

7. **Assess transparency and explainability.** Assess whether the model's outputs can be explained to the degree required by the use case and any applicable regulatory context. Flag use cases where explainability is required (credit, employment, housing, healthcare) but the model is a black-box. Note whether the model provides confidence scores or uncertainty estimates.

8. **Assess data provenance and rights.** Identify what is known about the model's training data — sources, third-party content, personal data, and rights clearance. Flag gaps in training data provenance. Note whether the training data is consistent with the intended use context (e.g., a model trained on English-language professional text used for consumer-facing multilingual applications).

9. **Assess security and abuse resistance.** Identify known security vulnerabilities — adversarial attacks, prompt injection, data extraction, model inversion. Assess the provider's security posture from documentation. Flag uses where the model could be weaponized or misused by adversarial actors.

10. **Assess human oversight and escalation design.** Evaluate whether the proposed deployment design includes adequate human review, override, and escalation for model errors and edge cases. Flag uses where outputs will be applied automatically to consequential decisions without human review.

11. **Assess monitoring and incident response.** Identify whether a plan exists to monitor model outputs in production (accuracy drift, bias drift, unexpected outputs) and to respond to incidents. Flag if no monitoring plan is in place.

12. **Assign risk tier and build the risk register.** For each dimension assessed, assign a risk level (Low / Medium / High) and an owner. Assign an overall risk tier.

13. **Recommend controls.** For each High and Medium risk item, recommend a specific control or action (technical, process, contractual, legal, or governance).

14. **Assemble the output.** Compile all sections, list all assumptions and open items, and label the document as a draft for attorney and governance review.

## Output Format

Deliver the following sections in order:

**1. Triage Summary**
Three to five sentences: model identity, intended use, overall risk tier, and the two or three dominant risk drivers.

**2. Model Characterization**
Table: Model name/version, provider/source, model type, training data (as documented), intended use per provider documentation, key documented limitations, and model card / documentation availability.

**3. Risk Register**

| Risk Dimension | Finding | Risk Level | Recommended Control | Owner |
|---|---|---|---|---|
| Intended use / foreseeable misuse | | | | |
| Affected individuals / harm severity | | | | |
| Accuracy and reliability | | | | |
| Bias and fairness | | | | |
| Transparency / explainability | | | | |
| Data provenance and rights | | | | |
| Security and abuse resistance | | | | |
| Human oversight design | | | | |
| Monitoring and incident response | | | | |

**4. Overall Risk Tier**
State Low / Medium / High with a two-to-three sentence rationale. Note that this is a governance triage signal, not a legal conclusion.

**5. Recommended Controls Summary**
Numbered list of priority actions, sorted High to Low, each with owner and recommended timeline.

**6. Routing Recommendations**
- `ai-use-case-intake` — if a full use case intake has not been completed.
- `ai-vendor-terms-review` — if vendor contractual terms have not been reviewed.
- Technical bias specialist — if the use case involves consequential decisions about individuals in protected categories.
- Privacy specialist — if personal data is processed or the model was trained on personal data.
- Regulatory specialist — if a regulated industry or jurisdiction-specific AI regulation applies.

**7. Open Items and Assumptions**
Bullet list of every `[CONFIRM: ...]` item, missing documentation, and assumption made in the absence of provided information.

*Label the full document: DRAFT — For Attorney and Governance Review — Not Legal Advice.*

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, engineering lead, data science lead, founder, AI governance committee, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language: the risk tier and what is driving it, separate from any compliance question.
- **Decision Needed** — the specific business decision(s) now on the table (deploy / deploy with controls / pause / specialist review), stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative (e.g., narrower deployment, additional human oversight) if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the AI governance committee, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] Model identification and version have been confirmed with the engineering or product team.
- [ ] All available technical documentation (model card, evaluation reports, bias assessments) has been provided and reviewed.
- [ ] The intended use has been confirmed against the provider's documented intended use and limitations.
- [ ] Affected individuals and potential harm scenarios have been reviewed for completeness.
- [ ] Accuracy and reliability findings are based on provided documentation, not assumed.
- [ ] Bias and fairness assessment has been escalated to a technical specialist if the use case involves consequential decisions about protected categories.
- [ ] Explainability requirements have been assessed in light of the applicable regulatory and legal context, verified by an attorney.
- [ ] Training data provenance gaps have been identified and are being addressed.
- [ ] Human oversight design has been confirmed as sufficient by the governance or product team.
- [ ] A monitoring plan is in place or required before deployment.
- [ ] No law or regulation has been asserted as applying without attorney verification.
- [ ] All open items and `[CONFIRM: ...]` placeholders have been resolved before the model is deployed.
