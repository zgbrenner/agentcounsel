---
name: Launch Review
description: "Use when conducting a pre-launch legal issue-spotting review for a new product or feature to produce a structured issues register and a draft go/hold/conditions recommendation for attorney sign-off."
practice_area: product-legal
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "A description of the product or feature to launch"
  - "The data, claims, and integrations involved"
  - "The launch timeline and markets"
outputs:
  - "Structured issues register"
  - "Draft go / hold / conditions recommendation for attorney sign-off"
related_skills:
  - skills/product-legal/marketing-claims-review/SKILL.md
  - skills/product-legal/ai-feature-review/SKILL.md
  - skills/privacy/privacy-policy-gap-review/SKILL.md
  - skills/contracts/contract-risk-review/SKILL.md
tags:
  - product-legal
  - launch-review
  - issue-spotting
  - product-counsel
  - go-no-go
---

# Launch Review

## Purpose

Produce a structured, attorney-ready legal issues register for a product or feature before it launches. This skill spots potential legal exposure across multiple practice areas, routes each issue to the right specialist skill or attorney, and frames a draft go / hold / conditions recommendation. It produces draft legal work product for attorney review — not legal advice, not a legal clearance, and not a certification of compliance.

## Use When

- A team is preparing to launch a new product, feature, app, or major update and needs a legal issues review before go-live.
- A product manager, engineer, or counsel asks to "do a legal review of this launch," "check if we're good to ship," or "flag legal risks before we release."
- A release date is approaching and legal has not yet reviewed the new functionality.
- A prior launch review exists but material scope has changed (new data types, new markets, new claims, new third-party integrations).
- Post-launch monitoring identifies a gap that requires a retroactive review.

## Required Inputs

- **Product or feature description**: what it does, how users interact with it, and what is new or changed.
- **Target markets and users**: geographies, user demographics, whether it serves consumers (B2C) or businesses (B2B), and any vulnerable populations (minors, healthcare patients, financial consumers).
- **Data collected and processed**: types of personal data, sensitive data categories (health, financial, biometric, location, children's data), how data flows, and any third-party data sharing.
- **Marketing claims and user-facing representations**: copy, screenshots, landing pages, onboarding text, or links to assets.
- **Third-party dependencies**: APIs, SDKs, open-source libraries, AI model providers, data vendors, or embedded services — with their names and, if known, their license or contract type.
- **Launch date**: the target date or window.

If any of these inputs are missing, stop and request them before proceeding. Do not fabricate facts, assume data practices, or guess at claims.

## Do Not Use When

- The document under review is primarily a contract (use `contract-risk-review` or `nda-review`).
- The review is limited to a privacy policy or data practices document (use `privacy-policy-gap-review`).
- The review concerns only marketing copy without a broader product launch context (use `marketing-claims-review`).
- The scope is exclusively AI/ML model behavior (use `ai-feature-review` or `model-risk-triage`).
- The team needs advice on whether the product is legally compliant — this skill spots issues and routes them; it does not provide clearance.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice, a compliance opinion, or a go/no-go decision.
- Do not assert that the product is compliant or lawful. The output is an issues register, not a clearance memo.
- Do not invent statutes, regulations, case law, agency guidance, or procedural deadlines. If a legal framework is relevant, name it and flag it for attorney verification.
- Separate facts (as provided), assumptions (flagged explicitly), and open questions (flagged with `[CONFIRM: ...]`).
- Identify jurisdiction, governing law, user population, and applicable regulatory context based on provided inputs — flag as unknown if not provided.
- Do not place client-sensitive product details or business strategy into reusable templates.
- Treat model background knowledge about legal frameworks as unverified unless supported by provided materials or separately researched authority.
- If the launch date creates a deadline pressure, flag it explicitly — do not compress or skip issue areas because of time constraints.

## Workflow

1. **Confirm inputs.** Verify that all required inputs are present. If any are missing, stop and request them. List what was received and what, if anything, was assumed.

2. **Identify jurisdiction and regulatory context.** Based on target markets and user population, identify the likely legal jurisdictions and regulatory frameworks in play (e.g., U.S. federal, state-level consumer protection, EU/EEA, UK, APAC). Flag any jurisdictions that require specialist local counsel review.

3. **Intellectual property and ownership.** Review what IP the product creates or relies on. Spot issues: ownership of outputs, use of third-party content, trademark clearance for product name and claims, patent exposure, and trade-secret handling. Flag for IP counsel.

4. **Privacy and data protection.** For each category of personal data collected: identify the likely legal basis for processing, flag sensitive data categories, assess whether a privacy notice update is required, and identify consent, data retention, cross-border transfer, or data subject rights issues. Route to privacy counsel or `privacy-policy-gap-review` as appropriate.

5. **Marketing claims and advertising.** Review all user-facing representations. For each material claim, flag whether it is objective, comparative, superlative, health/efficacy, environmental, AI-related, or pricing-related, and identify substantiation requirements. Route detailed claim-by-claim analysis to `marketing-claims-review`.

6. **Terms of service and contract impact.** Assess whether the launch changes the scope of the existing terms of service, creates new obligations for users, modifies payment or subscription terms, or creates new liabilities. Flag whether existing terms cover the new functionality or require amendment. Route detailed ToS review to `terms-of-service-review`.

7. **Regulatory exposure.** Spot regulated-industry issues: fintech/payments, healthcare/wellness, children's products, employment/HR tools, real estate, insurance, gambling, alcohol, firearms, or other sector-specific regulation. Flag each area for specialist counsel.

8. **AI and automated decision-making.** If the feature uses AI, machine learning, or algorithmic decision-making, flag training-data rights, output ownership, transparency and disclosure obligations, high-risk use cases, and vendor terms. Route to `ai-feature-review`.

9. **Open-source and third-party licensing.** Review declared third-party dependencies and open-source libraries. Flag any license type (GPL, AGPL, copyleft) that may impose distribution or disclosure obligations. Flag for IP or licensing counsel.

10. **Accessibility.** Flag whether the product has accessibility obligations (e.g., ADA/WCAG in the U.S., EN 301 549 in the EU) based on the product type and market. Note: accessibility technical assessment is outside this skill's scope.

11. **Consumer protection.** Spot unfair, deceptive, or abusive acts or practices exposure, dark patterns, auto-renewal disclosure requirements, and any sector-specific consumer protection obligations.

12. **Compile the issues register.** Assemble every flagged issue into the structured table described in the Output Format section. Assign severity (High / Medium / Low / Unknown), owner (practice area or specialist skill), and blocking status.

13. **Draft the go / hold / conditions recommendation.** Based on the issues register, draft a recommendation framed as follows: Go (no blocking issues identified), Hold (one or more blocking issues require resolution before launch), or Conditions (launch may proceed subject to specified conditions). Label this as a draft for attorney sign-off — it is not a legal clearance.

14. **List assumptions and open items.** State every assumption made and every `[CONFIRM: ...]` item that must be resolved before the review can be relied upon.

## Output Format

Deliver the following sections, in order, labeled as **DRAFT — FOR ATTORNEY REVIEW ONLY**:

1. **Review Summary**: product/feature name, launch date, target markets, review date, inputs received, and inputs missing or assumed.

2. **Launch Issues Register**: a table with columns — Issue Description | Practice Area | Severity (High / Medium / Low / Unknown) | Recommended Owner / Skill | Blocking? (Yes / No / TBD) | Status.

3. **Routing Map**: a brief list linking each High or blocking issue to the recommended next step (specialist attorney, sibling skill, or external counsel).

4. **Go / Hold / Conditions Recommendation** *(draft for attorney sign-off)*: state the draft recommendation and the conditions or prerequisites it depends on.

5. **Assumptions and Open Items**: numbered list of every assumption and `[CONFIRM: ...]` item.

6. **Attorney Verification Checklist**: checkbox items (see below).

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] All required inputs have been received and are complete and accurate.
- [ ] The target markets and user populations are correctly identified and no additional jurisdictions apply.
- [ ] Every sensitive data category has been identified and routed to privacy counsel.
- [ ] Marketing claims have been reviewed against substantiation requirements by counsel with advertising law expertise.
- [ ] Open-source and third-party license obligations have been reviewed by IP counsel.
- [ ] Any AI or algorithmic decision-making features have been reviewed using `ai-feature-review` or by counsel with AI law expertise.
- [ ] Regulated-industry exposure (fintech, health, children's products, etc.) has been routed to appropriate specialist counsel.
- [ ] The existing terms of service and privacy policy have been confirmed to cover the new functionality, or amendments have been drafted.
- [ ] No legal authority, statute, or regulation has been asserted without verification.
- [ ] All assumptions and `[CONFIRM: ...]` items have been resolved.
- [ ] The go / hold / conditions recommendation has been reviewed and approved by responsible counsel before it is communicated to the launch team.
- [ ] This document is labeled as a draft and is not shared with third parties or used as a compliance certification.
