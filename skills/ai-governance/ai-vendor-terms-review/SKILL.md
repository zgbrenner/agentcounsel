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

## Workflow

1. **Confirm inputs.** Verify all required inputs are present. Identify which documents were provided (MSA, order form, DPA, AUP, etc.) and flag any referenced documents not included.

2. **Identify the agreement structure.** Note the agreement type, governing law and dispute resolution, effective date, and parties. Flag any rolling terms (terms that update automatically) or incorporation by reference of external policies.

3. **Assess rights to inputs and prompts.** Review what license the vendor receives over customer inputs, prompts, and data submitted to the system. Distinguish between the license needed to provide the service and any broader rights (training, product improvement, third-party sharing).

4. **Assess training data use.** Identify whether the vendor's terms permit use of customer inputs, prompts, or outputs to train, fine-tune, or improve models. Note any opt-out mechanism and its scope and process. Flag if this is unclear or absent.

5. **Assess output ownership and license.** Identify what rights the vendor claims in outputs generated by the system. Distinguish between a license to provide the service and an assertion of ownership or ongoing rights. Note any restrictions on output use (commercial restrictions, attribution requirements, prohibited output uses).

6. **Assess IP infringement indemnity.** Identify whether the vendor indemnifies the customer for third-party IP infringement claims arising from the vendor's model or outputs. Note any carve-outs (customer-provided prompts, customer modifications, use outside approved scope). Flag if indemnity is absent or heavily qualified.

7. **Assess confidentiality and data handling.** Identify what confidentiality obligations apply to customer inputs and outputs. Note whether outputs can be shared with other customers or used as training data for other organizations. Confirm whether the confidentiality terms are adequate for the client's intended data inputs.

8. **Assess security and sub-processors.** Review security commitments (standards, certifications, breach notification). Identify sub-processor disclosure and approval rights. Note any geographic data residency commitments or restrictions.

9. **Assess accuracy disclaimers and liability for outputs.** Identify how the vendor disclaims liability for inaccurate, biased, or harmful outputs. Note any specific disclaimers about the suitability of outputs for particular purposes. Assess whether the disclaimer scope is consistent with the client's intended use.

10. **Assess usage restrictions and acceptable use.** Review the acceptable use policy for restrictions on use cases, prohibited content, and industry restrictions. Flag any restrictions inconsistent with the client's intended use.

11. **Assess service and model change rights.** Identify whether the vendor can modify, deprecate, or replace the model or service, and on what notice. Flag any right to materially change terms without consent.

12. **Assess liability caps and warranty terms.** Note the cap on vendor liability, any exclusions from the cap, and the warranty/disclaimer structure. Compare to the risk profile of the client's intended use.

13. **Assess termination and data deletion.** Review termination rights (for cause, for convenience, for policy violation). Identify data deletion obligations on termination — scope, timing, certification. Note any data retention rights the vendor retains post-termination.

14. **Prioritize redline points.** Categorize all issues as High (significant risk requiring negotiation), Medium (should be addressed if possible), or Low (minor, flag for awareness).

15. **Assemble the output.** Compile all sections, include all assumptions and open items, and label the document as a draft for attorney review.

## Output Format

Deliver the following sections in order:

**1. Review Summary**
Two to four sentences covering the agreement type, key risk themes, and the overall risk profile relative to the client's intended use.

**2. Agreement Structure**
Table: Document(s) reviewed, governing law, dispute resolution, effective date, automatic update / rolling terms provisions, and any documents referenced but not provided.

**3. AI-Specific Terms Assessment**

| Topic | Summary of Vendor's Position | Risk to Client | Priority |
|---|---|---|---|
| Rights to inputs / prompts | | | |
| Training data use / opt-out | | | |
| Output ownership / license | | | |
| IP infringement indemnity | | | |
| Confidentiality of inputs/outputs | | | |
| Security and sub-processors | | | |
| Accuracy disclaimers | | | |
| Usage restrictions / AUP | | | |
| Service / model change rights | | | |
| Liability cap | | | |
| Termination and data deletion | | | |

**4. Prioritized Redline Points**
Numbered list, sorted High / Medium / Low, each with: the provision at issue (section reference), the problem, and the recommended ask.

**5. Routing Recommendations**
- `dpa-review` — if a data processing agreement is included or required and has not been separately reviewed.
- `contract-risk-review` — if the broader commercial terms (payment, warranties, IP ownership) require a full commercial review.
- Privacy specialist — if personal data is processed and regulatory compliance (GDPR, CCPA, etc.) needs verification.
- `model-risk-triage` — if the vendor model's reliability or bias characteristics need further assessment.

**6. Open Items and Assumptions**
Bullet list of every `[CONFIRM: ...]` item, ambiguity, and missing document.

*Label the full document: DRAFT — For Attorney Review — Not Legal Advice.*

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
- [ ] No legal conclusion about enforceability or regulatory compliance has been asserted without attorney verification.
- [ ] A separate DPA review has been completed if personal data is processed.
