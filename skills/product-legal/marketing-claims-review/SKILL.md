---
name: Marketing Claims Review
description: Use when reviewing marketing or advertising copy for legal risk to produce a claim-by-claim analysis, substantiation requirements, and flagged disclosures for attorney review.
---

# Marketing Claims Review

## Purpose

Produce a structured, attorney-ready review of marketing or advertising copy. For each claim, this skill classifies the claim type, identifies what substantiation would be required, flags disclosure and disclaimer needs, and highlights unverifiable or absolute statements. It produces draft legal work product for attorney review — not legal advice, not a determination that any claim is lawful, and not a certification that copy is FTC-compliant or cleared for use.

## Use When

- A user asks to "review this ad copy," "check our marketing for legal issues," or "tell me which claims might be a problem."
- New marketing assets (website copy, email campaigns, app store listings, social media posts, press releases, product packaging, or video scripts) are being prepared for publication.
- Existing copy is being updated and requires re-review after material changes to claims, products, or evidence.
- A team is preparing claims in a regulated industry (health/wellness, financial services, environmental/green, AI-powered features) and needs a structured issues list before legal sign-off.
- An attorney needs a first-pass triage of a large volume of copy before conducting a detailed substantive review.

## Required Inputs

- **The copy to be reviewed**: full text of all marketing or advertising material (uploaded, pasted, or linked). Screenshots or image-based copy must be transcribed.
- **Product or service description**: what is being advertised, what it does, and what it does not do.
- **Client's role**: the advertiser (making the claims) or a platform/agency (publishing or distributing them).
- **Target audience**: consumer (B2C) or business (B2B); any vulnerable populations (minors, patients, financially distressed consumers).
- **Jurisdiction(s)**: the primary markets where the copy will run. If unknown, flag as `[CONFIRM: target jurisdictions]`.
- **Available substantiation** *(if any)*: studies, test results, clinical trials, certifications, or other evidence the client holds for specific claims.

If the copy itself is not provided, stop and request it. Do not fabricate claims, invent evidence, or assume what the copy says.

## Do Not Use When

- The review is of a full product launch across multiple legal areas (use `launch-review`).
- The document is a terms of service, privacy policy, or contract (use `terms-of-service-review` or `contract-risk-review`).
- The question is whether a specific claim violates a specific statute — this skill flags risk and routes; it does not provide a legal opinion on lawfulness.
- The user wants only proofreading or brand-voice editing without legal analysis.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice and does not constitute advertising counsel sign-off.
- Do not assert that any claim is lawful, permissible, or cleared. The output is a risk register and a list of questions for counsel — not a green light.
- Do not invent regulatory standards, FTC guidance, NAD decisions, consent decrees, or case law. If a legal framework is relevant, name it and flag it for attorney verification.
- Distinguish what the copy actually says (quoted), from what it implies (inferred), from what is assumed (flagged), and from what must be confirmed (`[CONFIRM: ...]`).
- Identify the target jurisdiction and applicable regulatory framework — if unknown, flag prominently.
- Do not omit claims because they seem minor. Every material claim should appear in the register.
- Flag urgency if the copy is scheduled for imminent publication.
- Do not place client-sensitive business strategy or unreleased product information into reusable templates.

## Workflow

1. **Confirm inputs.** Verify that copy and context are provided. List what was received and flag anything missing. If the copy is not provided, stop.

2. **Extract all claims.** Read through the copy and extract every material claim — express and implied. Include: product performance claims, comparative claims, pricing and savings claims, testimonials and endorsements, origin claims, environmental claims, health or wellness claims, AI-capability claims, superlatives ("best," "only," "guaranteed"), and any factual assertion about the product, the company, or a competitor.

3. **Classify each claim.** Assign one or more of the following claim types:
   - **Objective / measurable**: a verifiable factual assertion (e.g., "charges in 30 minutes").
   - **Comparative**: a claim comparing the product to a competitor or category (e.g., "faster than Brand X").
   - **Superlative**: a claim of uniqueness or market leadership ("the best," "the only," "number one").
   - **Testimonial / endorsement**: a quote, review, or expert statement used to support a claim.
   - **Environmental / green**: sustainability, carbon, recyclability, or similar claims.
   - **Health / efficacy**: claims about physical or mental health outcomes, wellness, treatment, cure, or prevention.
   - **Pricing / savings**: discount claims, comparative pricing, "free" offers, subscription pricing.
   - **AI-related**: claims about AI capabilities, accuracy, autonomy, or intelligence.
   - **Puffery** *(low-risk)*: obvious exaggeration not likely to be taken literally ("the world's tastiest coffee").

4. **Assess substantiation requirements.** For each non-puffery claim, identify what substantiation standard likely applies and what evidence would be needed to support the claim. Note: substantiation standards vary by jurisdiction and claim type — flag for attorney verification rather than stating a legal conclusion.

5. **Flag disclosure and disclaimer needs.** Identify claims that likely require disclosures, disclaimers, or qualifications — including: material connections in testimonials, results-not-typical language, fine print for pricing offers, asterisked qualifications, and jurisdiction-specific disclosure requirements.

6. **Flag high-risk claims.** Highlight claims that are:
   - Absolute or unqualified ("always," "never," "100%," "guaranteed").
   - Unverifiable based on provided substantiation.
   - Comparative without identified evidence.
   - Health or efficacy claims in a consumer product context.
   - Environmental claims that may constitute greenwashing.
   - AI-capability claims that overstate or anthropomorphize the product.

7. **Compile the claims register.** Assemble all findings into the structured table described in the Output Format section.

8. **Draft substantiation requests.** For each High-risk claim, draft a substantiation request — a brief description of what evidence would be needed and who should provide it.

9. **List assumptions and open items.** State every assumption and every `[CONFIRM: ...]` item.

## Output Format

Deliver the following sections, in order, labeled as **DRAFT — FOR ATTORNEY REVIEW ONLY**:

1. **Review Summary**: copy reviewed (describe or quote the title/source), product/service, client role, target jurisdiction(s), review date, inputs received, and inputs missing or assumed.

2. **Claims Register** *(one row per claim)*: a table with columns — Claim (quoted) | Claim Type | Risk Level (High / Medium / Low / Puffery) | Substantiation Needed | Disclosure / Disclaimer Flag | Notes / Open Questions.

3. **High-Risk Claims — Substantiation Requests**: for each High-risk claim, a brief description of what evidence or qualification is needed and who should provide it.

4. **Recommended Disclosures and Disclaimers**: a list of recommended additions to the copy, framed as drafts for attorney review, not final language.

5. **Assumptions and Open Items**: numbered list of every assumption and `[CONFIRM: ...]` item, including unresolved jurisdictional questions.

6. **Attorney Verification Checklist**: checkbox items (see below).

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] All copy has been provided and is complete; no material claims appear only in images or video that were not reviewed.
- [ ] The target jurisdiction(s) have been confirmed, and jurisdiction-specific rules (including state consumer protection laws, EU/UK rules, or sector-specific standards) have been applied by counsel.
- [ ] Each High-risk claim has been reviewed against actual available substantiation.
- [ ] Comparative claims have been reviewed for accuracy and competitor-identification issues.
- [ ] Environmental/green claims have been assessed under applicable greenwashing standards.
- [ ] Health or efficacy claims have been reviewed by counsel with regulatory expertise for the relevant product category.
- [ ] AI-capability claims have been reviewed for accuracy and applicable disclosure requirements.
- [ ] Testimonials and endorsements comply with applicable disclosure requirements (e.g., FTC Endorsement Guides or equivalent).
- [ ] All recommended disclosures and disclaimers have been reviewed and approved by counsel before use.
- [ ] No legal authority, standard, or agency guidance has been asserted without verification.
- [ ] All assumptions and `[CONFIRM: ...]` items have been resolved.
- [ ] This document is labeled as a draft and is not shared with third parties or used as advertising counsel sign-off.
