---
name: AI Vendor Terms Review
description: "Use when reviewing the terms of service, API agreement, or usage policies of an AI vendor or AI-enabled service to produce a structured risk summary and prioritized redline points for attorney review."
practice_area: ai-governance
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The AI vendor's terms of service, API agreement, or usage policy text"
  - "The client's role and intended use of the service"
  - "The data the client will send to the service"
outputs:
  - "Structured risk summary"
  - "Issues table"
  - "Prioritized redline points for attorney review"
related_skills:
  - skills/contracts/contract-risk-review/SKILL.md
  - skills/privacy/dpa-review/SKILL.md
  - skills/ai-governance/ai-use-case-intake/SKILL.md
  - skills/ai-governance/employee-ai-policy/SKILL.md
tags:
  - ai-governance
  - ai
  - vendor-terms
  - contract-review
  - redline
---

# AI Vendor Terms Review

## Purpose

Produce a structured, attorney-ready review of an AI vendor's terms of service, API agreement, enterprise license, or acceptable use policy. The review focuses on the provisions that are materially different in AI contracts — rights to inputs and prompts, training data use, output ownership, IP indemnity, accuracy disclaimers, and model-change rights — while also flagging standard contract risk areas that apply with particular force in AI contexts.

This skill produces draft legal work product for attorney review. It does not render a legal conclusion about whether any term is enforceable, whether the contract should be signed, or what any specific law requires.

## Use When

- A team wants to adopt a new AI API, AI platform, or AI-enabled SaaS product and needs the legal terms reviewed.
- An existing AI vendor agreement is up for renewal or the vendor has pushed updated terms.
- A user asks "what are we giving up by signing this?" or "does this vendor own what we generate?"
- Legal has received a vendor-side paper AI agreement and needs a structured risk review.
- A vendor's acceptable use policy or model card terms need review before integration.

## Required Inputs

- **Vendor agreement text**: The full text of the terms of service, API agreement, data processing agreement, and/or acceptable use policy — uploaded or pasted. Identify which document(s) are provided.
- **Client's intended use**: A plain-language description of what the organization plans to do with the vendor's AI system (e.g., generate customer-facing marketing copy, process employee HR queries, analyze legal documents).
- **Client's role**: Whether the organization is an API consumer, enterprise licensee, reseller, or end user.
- **Data the client will input**: The types of data the client will send to the vendor's system — including whether it includes personal data, confidential business information, or privileged material.
- **Privileged or work-product material**: Whether the client intends to input or has historically input material protected by attorney-client privilege or attorney work-product doctrine (drafts of legal memos, analyses for counsel, litigation strategy, etc.). If yes, note the matter context and the governing privilege jurisdiction.
- Optional: the practice group's `practice-profiles/ai-governance.md` if it has been populated and is loaded alongside this skill. If present, the skill uses its Standard Positions and Escalation Thresholds tables to benchmark the output and to gate escalation. If absent, the skill proceeds without practice-profile benchmarking and asks the user to supply standing positions inline if needed.

If the vendor agreement text is not provided, stop and request it. Do not fabricate, paraphrase, or assume contract terms.

## Do Not Use When

- The document is a general commercial software or SaaS agreement with no AI-specific terms — use `contract-risk-review` instead.
- The primary question is about the data processing or privacy terms only — use `dpa-review`, though this skill should be completed first for the full AI terms picture.
- The question concerns an AI use case that has not yet been assessed — complete `ai-use-case-intake` first.
- The agreement is an employment agreement or contractor agreement with AI-generated work provisions — use `employee-ai-policy` for the policy context.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Review only the contract text actually provided; do not infer, assume, or reconstruct missing provisions.
- Do not assert what any law or regulation requires of AI vendor contracts; flag potential regulatory considerations for attorney verification.
- Quote or paraphrase only from the actual provided text; cite section numbers where possible.
- Do not assert that any term is enforceable or unenforceable without attorney review.
- Distinguish findings based on the provided text from assumptions and open items that require verification.
- Use `[CONFIRM: ...]` placeholders for provisions that are ambiguous, potentially missing, or require vendor clarification.
- Flag if a separate data processing agreement or acceptable use policy is referenced but not provided — the review is incomplete without it.
- **Privilege-impact framing.** If the client will input privileged or work-product material, the vendor's terms-of-service may affect the third-party-disclosure prong of privilege under the governing jurisdiction's privilege doctrine. Flag the privilege-impact analysis as attorney-verification only — do not conclude on privilege preservation or waiver.
- **Severity floor.** Once an issue has been rated High priority in the issues list or AI-Specific Terms Assessment table, that rating must not be silently downgraded. Any reduction in priority is an explicit attorney decision and must be recorded as such (e.g., "Downgraded from High to Medium by [attorney], [date], reason: [brief rationale]"). This applies regardless of the vendor's explanation or commercial commonness of the provision. Where `practice-profiles/ai-governance.md` is loaded, the profile's Escalation Thresholds for AI-vendor terms (e.g., minimum acceptable indemnity scope, sub-processor approval mechanism, PHI-training posture) inform what constitutes High; the loaded thresholds apply alongside, not instead of, the inline ratings.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/ai-governance.md` is loaded, its Standard Positions and Escalation Thresholds inform the draft but never substitute for attorney judgment. The profile is a configuration record approved by the practice group; it is not legal advice and does not override the skill's normal attorney-verification gates. If the profile's standing positions conflict with the matter facts or with what the supervising attorney concludes, the attorney prevails.

## Workflow

This skill draws on shared AI-vendor-terms reference material: `skills/ai-governance/references/ai-vendor-terms-red-flags.md` (the AI vendor terms red-flag catalog, organized by topic with per-section Preferred position / Fallback position direction lines). Consult it at the steps noted below. For general commercial contract patterns, the catalog cross-references `skills/contracts/references/red-flags.md`.

1. **Confirm inputs.** Verify all required inputs are present. Identify which documents were provided (MSA, order form, DPA, AUP, etc.) and flag any referenced documents not included.

2. **Identify the agreement structure.** Note the agreement type, governing law and dispute resolution, effective date, and parties. Flag any rolling terms (terms that update automatically) or incorporation by reference of external policies.

3. **Red flags quick scan.** Run a fast first pass against the AI vendor terms red-flag catalog in `skills/ai-governance/references/ai-vendor-terms-red-flags.md`. Record each red-flag pattern present, or note that none surfaced in the scan. This scan orients the deeper assessment steps below; it does not replace them.

4. **Assess rights to inputs and prompts.** Review what license the vendor receives over customer inputs, prompts, and data submitted to the system. Distinguish between the license needed to provide the service and any broader rights (training, product improvement, third-party sharing).

5. **Assess training data use.** Identify whether the vendor's terms permit use of customer inputs, prompts, or outputs to train, fine-tune, or improve models. Note any opt-out mechanism and its scope and process. Flag if this is unclear or absent. Check the language against Section 1 of `skills/ai-governance/references/ai-vendor-terms-red-flags.md` (training and improvement rights, including partial or prospective-only opt-outs, weak de-identification carve-outs, and human review rights).

6. **Assess output ownership and license.** Identify what rights the vendor claims in outputs generated by the system. Distinguish between a license to provide the service and an assertion of ownership or ongoing rights. Note any restrictions on output use (commercial restrictions, attribution requirements, prohibited output uses). Check the language against Section 2 of the red-flag catalog (output ownership ambiguity, non-exclusivity of outputs).

7. **Assess IP infringement indemnity.** Identify whether the vendor indemnifies the customer for third-party IP infringement claims arising from the vendor's model or outputs. Note any carve-outs (customer-provided prompts, customer modifications, use outside approved scope). Flag if indemnity is absent or heavily qualified. Check the language against Section 2 of the red-flag catalog (indemnity excluding AI-generated output, no indemnity for training-data claims).

8. **Assess confidentiality and data handling.** Identify what confidentiality obligations apply to customer inputs and outputs. Note whether outputs can be shared with other customers or used as training data for other organizations. Confirm whether the confidentiality terms are adequate for the client's intended data inputs. Check the language against Section 3 of the red-flag catalog (prompts or outputs excluded from Confidential Information, unbounded abuse-monitoring retention).

9. **Assess privilege impact when privileged material will be input.** If the client has indicated that privileged or work-product material has been or will be input to the vendor's system, assess the vendor's terms against the third-party-disclosure question:
   - Vendor's data-retention rights and duration
   - Vendor's right to use inputs for training, fine-tuning, or other product development
   - Vendor's right to access inputs for support, debugging, or trust-and-safety review
   - Sub-processor disclosure: who else can access the inputs
   - Whether enterprise-tier or "zero-retention" terms are available and whether they have been elected
   - Whether the vendor offers a contractual representation about confidentiality treatment that approximates the duty-of-confidentiality owed by an agent or vendor under privilege doctrine

   Flag every finding as `[ATTORNEY TO CONFIRM: privilege impact under governing jurisdiction's privilege and work-product doctrine]`. Do not conclude on privilege preservation. Note that some courts have held consumer-tier AI vendor terms to effect third-party disclosure that defeats privilege; route to litigation/privilege specialist counsel.

10. **Assess security and sub-processors.** Review security commitments (standards, certifications, breach notification). Identify sub-processor disclosure and approval rights. Note any geographic data residency commitments or restrictions. Check the language against Sections 6 and 10 of the red-flag catalog (AI terms overriding the DPA, undisclosed sub-processing of model providers, no incident notification for model-level failures), and follow the catalog's routing to `skills/privacy/dpa-review/SKILL.md` and `skills/privacy/vendor-privacy-diligence/SKILL.md` where indicated.

11. **Assess accuracy disclaimers and liability for outputs.** Identify how the vendor disclaims liability for inaccurate, biased, or harmful outputs. Note any specific disclaimers about the suitability of outputs for particular purposes. Assess whether the disclaimer scope is consistent with the client's intended use. Check the language against Section 7 of the red-flag catalog (AI-specific disclaimers combined with encouraged reliance) and Section 8 (vendor disclaims regulatory responsibility, no cooperation or transparency-artifact commitments).

12. **Assess usage restrictions and acceptable use.** Review the acceptable use policy for restrictions on use cases, prohibited content, and industry restrictions. Flag any restrictions inconsistent with the client's intended use. Check the language against Section 5 of the red-flag catalog (unilaterally changeable AUPs incorporated by reference, restrictions blocking the client's actual use case, discretionary rate limits and throttling).

13. **Assess service and model change rights.** Identify whether the vendor can modify, deprecate, or replace the model or service, and on what notice. Flag any right to materially change terms without consent. Check the language against Sections 4 and 9 of the red-flag catalog (unilateral model swaps, no version pinning, non-binding quality commitments, sunsets without a migration path, export of fine-tunes or embeddings denied).

14. **Assess liability caps and warranty terms.** Note the cap on vendor liability, any exclusions from the cap, and the warranty/disclaimer structure. Compare to the risk profile of the client's intended use. Check the language against Section 7 of the red-flag catalog (caps and exclusions that carve out AI-related harms).

15. **Assess termination and data deletion.** Review termination rights (for cause, for convenience, for policy violation). Identify data deletion obligations on termination — scope, timing, certification. Note any data retention rights the vendor retains post-termination. Check the language against Sections 9 and 10 of the red-flag catalog (service continuity, logs access).

16. **Prioritize redline points.** Categorize all issues as High (significant risk requiring negotiation), Medium (should be addressed if possible), or Low (minor, flag for awareness). For issues matching a catalog entry, use the per-section **Preferred position / Fallback position** lines in `skills/ai-governance/references/ai-vendor-terms-red-flags.md` to help articulate the recommended ask — they orient the direction of a redline, not final clause language, and never substitute for attorney judgment or a loaded practice profile's Standard Positions.

17. **Assemble the output.** Compile all sections, include all assumptions and open items, and label the document as a draft for attorney review.

## Output Format

Deliver the following sections in order:

**1. Review Summary**
Two to four sentences covering the agreement type, key risk themes, and the overall risk profile relative to the client's intended use.

**2. Agreement Structure**
Table: Document(s) reviewed, governing law, dispute resolution, effective date, automatic update / rolling terms provisions, and any documents referenced but not provided.

**3. Red Flags Quick Scan**
Each red-flag pattern from `skills/ai-governance/references/ai-vendor-terms-red-flags.md` found in the agreement (with section references to the reviewed text), or a note that none surfaced in the scan.

**4. AI-Specific Terms Assessment**

| Topic | Summary of Vendor's Position | Risk to Client | Priority |
|---|---|---|---|
| Rights to inputs / prompts | | | |
| Training data use / opt-out | | | |
| Output ownership / license | | | |
| IP infringement indemnity | | | |
| Privilege impact (if privileged material involved) | | | |
| Confidentiality of inputs/outputs | | | |
| Security and sub-processors | | | |
| Accuracy disclaimers | | | |
| Usage restrictions / AUP | | | |
| Service / model change rights | | | |
| Liability cap | | | |
| Termination and data deletion | | | |

**5. Prioritized Redline Points**
Numbered list, sorted High / Medium / Low, each with: the provision at issue (section reference), the problem, and the recommended ask. Use the per-section **Preferred position / Fallback position** lines in `skills/ai-governance/references/ai-vendor-terms-red-flags.md` to help articulate the recommended ask where an issue matches a catalog entry.

**6. Routing Recommendations**
- `dpa-review` — if a data processing agreement is included or required and has not been separately reviewed.
- `contract-risk-review` — if the broader commercial terms (payment, warranties, IP ownership) require a full commercial review.
- Privacy specialist — if personal data is processed and regulatory compliance (GDPR, CCPA, etc.) needs verification.
- `model-risk-triage` — if the vendor model's reliability or bias characteristics need further assessment.
- Litigation/privilege specialist counsel — if the client will input privileged or work-product material and the vendor's data-retention, training-use, sub-processor, or trust-and-safety access terms could implicate the third-party-disclosure analysis under the governing jurisdiction's privilege doctrine.

**7. Open Items and Assumptions**
Bullet list of every `[CONFIRM: ...]` item, ambiguity, and missing document.

*Label the full document: DRAFT — For Attorney Review — Not Legal Advice.*

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a procurement lead, product owner, AI program owner, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language: what the vendor's terms commit to and reserve, how that fits the intended use, and the headline risks.
- **Decision Needed** — the specific business decision(s) now on the table (sign as-is / push back / walk away), stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the AI governance committee, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] All relevant vendor documents have been provided and reviewed; no referenced documents are missing.
- [ ] All quotations and paraphrases have been verified against the actual contract text with section references.
- [ ] Training data use provisions have been confirmed — including any opt-out process and its actual effect.
- [ ] Output ownership analysis reflects the full agreement, including any order form or addendum terms.
- [ ] IP indemnity scope and carve-outs have been reviewed in light of the client's specific intended use.
- [ ] Confidentiality terms are adequate for the sensitivity of the data the client will input.
- [ ] Security certifications and breach notification timelines have been confirmed with the vendor if not specified in the agreement.
- [ ] Acceptable use policy has been reviewed and is not inconsistent with the client's intended use case.
- [ ] Liability cap adequacy has been assessed relative to the client's risk exposure from the intended use.
- [ ] Data deletion obligations on termination have been confirmed as sufficient.
- [ ] The red-flag quick scan against `skills/ai-governance/references/ai-vendor-terms-red-flags.md` has been reviewed; every flagged pattern is reflected in the assessment table or redline points, and any preferred/fallback direction drawn from the catalog reflects the client's actual leverage and standard positions.
- [ ] No legal conclusion about enforceability or regulatory compliance has been asserted without attorney verification.
- [ ] A separate DPA review has been completed if personal data is processed.
- [ ] If privileged or work-product material has been or will be input, the privilege impact of the vendor's terms has been reviewed under the governing jurisdiction's privilege and work-product doctrine; the enterprise/zero-retention election (if available) has been considered; and the analysis has been routed to litigation/privilege counsel.
- [ ] All High-priority issues remain rated High unless an attorney has explicitly documented the rationale for any downgrade, including their name and the date of the decision.
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged; profile-silent items are flagged as not-yet-addressed by the playbook.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.
