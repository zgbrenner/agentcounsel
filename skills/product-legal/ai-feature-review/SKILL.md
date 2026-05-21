---
name: AI Feature Review
description: "Use when conducting a legal issue-spotting review for a product feature that uses AI or machine learning to produce a structured issues register and recommendations for attorney review."
practice_area: product-legal
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "A description of the AI or machine-learning product feature"
  - "The model and data details"
  - "The intended users and the decisions the feature affects"
outputs:
  - "Structured AI issues register"
  - "Recommendations for attorney review"
related_skills:
  - skills/ai-governance/ai-vendor-terms-review/SKILL.md
  - skills/product-legal/launch-review/SKILL.md
  - skills/ai-governance/model-risk-triage/SKILL.md
tags:
  - product-legal
  - ai
  - feature-review
  - issue-spotting
  - ai-governance
---

# AI Feature Review

## Purpose

Produce a structured, attorney-ready legal issues register for a product feature that uses artificial intelligence or machine learning. This skill spots legal exposure across training-data rights, output ownership and infringement, transparency and disclosure obligations, privacy and data use, automated-decision concerns, vendor terms, and high-risk use cases. It routes AI-vendor contract questions to `ai-vendor-terms-review` and broader AI risk triage to `model-risk-triage`. It produces draft legal work product for attorney review — not legal advice, not a regulatory clearance, and not a determination that the feature is lawful.

## Use When

- A team is building, shipping, or updating a feature that uses an AI model, machine learning system, or algorithmic decision-making component.
- A product manager, engineer, or counsel asks to "review the legal risks of this AI feature," "check if we can use this model," or "what do we need to disclose?"
- A launch review (see `launch-review`) has flagged an AI or algorithmic component for deeper analysis.
- An existing AI feature is being modified in a material way: new model, new data inputs, new output use case, or new user population.
- The feature involves a vendor-supplied AI model and the team needs a legal issues overview before completing vendor contracting (route contract detail to `ai-vendor-terms-review`).
- The feature involves automated decisions that affect users in consequential ways (credit, employment, health, housing, content moderation, pricing).

## Required Inputs

- **Feature description**: what the feature does, how users interact with it, and what is new or changed.
- **Model(s) used**: whether the model is in-house (trained or fine-tuned internally) or vendor-supplied (API, embedded, or licensed). Include model name or vendor name if known.
- **Training and input data**: what data was used to train or fine-tune the model (if in-house), and what data the model receives at inference time (user inputs, uploaded files, third-party data, etc.).
- **Outputs and how they are used**: what the model produces (text, images, scores, classifications, recommendations, decisions), and how those outputs are displayed to or acted upon by users or internal systems.
- **User-facing disclosures**: what, if anything, the product currently discloses to users about AI use, automated decision-making, or the nature of the outputs.
- **Human-oversight design**: whether and how a human reviews, approves, or can override AI outputs before they affect users.
- **Target markets and users**: geographies, user demographics, and any vulnerable populations (minors, patients, financial consumers, job seekers).

If the feature description and model type are not provided, stop and request them. Do not fabricate technical details, data practices, or vendor terms.

## Do Not Use When

- The review concerns only the AI vendor contract (use `ai-vendor-terms-review`).
- The review requires a broader multi-area launch review of which AI is one component (use `launch-review`, which will route AI issues here).
- The review is a high-level AI risk classification or model card assessment (use `model-risk-triage`).
- The feature does not involve AI, machine learning, or algorithmic decision-making — use the appropriate product-legal skill for the relevant issue area.
- The goal is to determine whether the feature complies with a specific AI regulation — this skill spots issues and routes; it does not render legal compliance opinions.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice and does not constitute a regulatory clearance or AI compliance certification.
- Do not assert that the feature is compliant with any AI regulation, data protection law, or consumer protection standard. Flag risks and route to counsel.
- Do not invent statutes, regulations, agency guidance, technical standards, or enforcement precedents. If a legal framework is relevant (e.g., EU AI Act, state AI transparency laws, FTC guidance on AI), name it and flag it for attorney verification with a `[CONFIRM: ...]` marker.
- Distinguish what is known from provided inputs, what is assumed, and what must be confirmed.
- Identify jurisdiction, target user population, and applicable regulatory context based on provided inputs — flag as unknown if not provided.
- High-risk use cases (healthcare, employment, credit, education, housing, law enforcement, critical infrastructure) require escalation to specialist counsel — do not minimize or omit these flags.
- Do not place client-sensitive technical architecture, unreleased model details, or proprietary training data descriptions into reusable templates.
- Treat model background knowledge about AI law as unverified; flag for attorney confirmation before relying on it.

## Workflow

1. **Confirm inputs.** Verify that all required inputs are present. List what was received and flag anything missing or assumed. If the feature description is not provided, stop.

2. **Characterize the feature.** Summarize the AI feature type (generative, classification, recommendation, scoring, decision-automation, or other), its position in the user experience, and whether outputs are directly user-facing or used internally.

3. **Training-data rights and IP.** Assess whether the training data used (if in-house) or the vendor's training data (if vendor-supplied and disclosed) raises rights issues: licensed data, scraped data, copyrighted works, personal data used for training, and applicable consent or contractual restrictions. Flag for IP and privacy counsel.

4. **Output ownership and infringement risk.** Assess who owns the AI outputs, whether the outputs could infringe third-party IP (copyright, trademark, trade dress), and whether the feature's output use case is consistent with the applicable model license or vendor terms. Route detailed vendor contract analysis to `ai-vendor-terms-review`.

5. **Accuracy, reliability, and disclaimer needs.** Assess whether the feature makes representations — express or implied — about the accuracy, completeness, or reliability of AI outputs. Flag: hallucination risk, outputs presented as factual without verification, medical/legal/financial advice risk, and whether existing disclaimers adequately disclose limitations.

6. **Transparency and disclosure to users.** Review what the product currently discloses about AI use. Flag: absence of disclosure that a feature is AI-powered, failure to disclose when outputs are AI-generated (particularly for content, recommendations, or decisions), and obligations under applicable AI transparency laws `[CONFIRM: applicable jurisdictions]`.

7. **Privacy and data use.** Assess how personal data flows through the feature: data collected at inference, data sent to a vendor model API, data used for model improvement or retraining, and applicable consent, data minimization, and data retention obligations. Route detailed privacy analysis to privacy counsel.

8. **Automated decision-making and algorithmic accountability.** Assess whether the feature makes or substantially influences consequential decisions affecting users. Flag: absence of human review, failure to provide explanations or rights of contestation, and applicable automated-decision laws `[CONFIRM: EU GDPR Art. 22, state AI laws, sector-specific requirements]`.

9. **Vendor terms and model license.** Flag whether the vendor's API terms, model license, or acceptable use policy permits the intended use case. Identify provisions that restrict output use, impose disclosure obligations, or limit commercial use. Route detailed vendor contract review to `ai-vendor-terms-review`.

10. **High-risk use cases.** Assess whether the feature operates in a high-risk domain: healthcare or wellness advice, employment screening, credit or insurance decisions, housing, education, legal advice, law enforcement, or critical infrastructure. Flag each domain for specialist counsel and note applicable regulatory frameworks.

11. **Open-source model considerations.** If an open-source model is used, flag: the model license type and commercial use permissions, any attribution or disclosure requirements, and whether fine-tuning or distribution triggers additional obligations.

12. **Compile the issues register.** Assemble every flagged issue into the structured table described in the Output Format section. Assign severity (High / Medium / Low / Unknown), practice area owner, routing (attorney or sibling skill), and whether the issue is blocking for launch.

13. **Draft recommendations.** For High-severity issues, draft a brief recommended action (disclosure language, contractual protection, human-oversight design change, or specialist escalation), framed as options for attorney review — not final guidance.

14. **List assumptions and open items.** State every assumption and every `[CONFIRM: ...]` item that must be resolved before the review can be relied upon.

## Output Format

Deliver the following sections, in order, labeled as **DRAFT — FOR ATTORNEY REVIEW ONLY**:

1. **Review Summary**: feature name, model type (in-house / vendor), target markets, review date, inputs received, and inputs missing or assumed.

2. **Feature Characterization**: brief description of the AI feature type, user-facing behavior, and output use.

3. **AI Feature Issues Register** *(one row per issue)*: a table with columns — Issue Description | Legal Area | Severity (High / Medium / Low / Unknown) | Recommended Owner / Skill | Blocking? (Yes / No / TBD) | Status.

4. **High-Risk Domain Flags**: a separate callout for any issues in healthcare, employment, credit, housing, education, or other high-risk domains, with recommended escalation path.

5. **Routing Map**: a brief list linking each High or blocking issue to the recommended next step (specialist attorney, `ai-vendor-terms-review`, `model-risk-triage`, or other sibling skill).

6. **Recommended Actions** *(draft for attorney review)*: for each High-severity issue, a brief recommended action or options framed as drafts for attorney review.

7. **Assumptions and Open Items**: numbered list of every assumption and `[CONFIRM: ...]` item.

8. **Attorney Verification Checklist**: checkbox items (see below).

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] All required inputs have been received and accurately describe the feature as it will be deployed.
- [ ] Training-data rights and provenance have been reviewed by IP counsel, including any personal data used in training.
- [ ] Output ownership and infringement risk have been assessed by IP counsel for the specific use case.
- [ ] The vendor model license and API terms have been reviewed using `ai-vendor-terms-review` or by counsel with vendor contract expertise.
- [ ] User-facing disclosures of AI use have been reviewed against applicable transparency obligations in all target jurisdictions.
- [ ] Automated-decision-making provisions (GDPR Art. 22 or equivalent) have been assessed by privacy counsel if the feature makes consequential decisions affecting users.
- [ ] Any high-risk domain use case (healthcare, employment, credit, housing, etc.) has been escalated to specialist counsel.
- [ ] Personal data flows through the AI feature (including data sent to vendor APIs) have been reviewed by privacy counsel.
- [ ] Open-source model license obligations have been reviewed by IP counsel if an open-source model is used.
- [ ] Accuracy and disclaimer language has been reviewed and approved by counsel before user-facing deployment.
- [ ] No legal authority, regulation, or agency guidance has been asserted without verification.
- [ ] All assumptions and `[CONFIRM: ...]` items have been resolved.
- [ ] This document is labeled as a draft and is not shared with third parties or used as a regulatory compliance certification.
