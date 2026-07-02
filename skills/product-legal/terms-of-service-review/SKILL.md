---
name: Terms of Service Review
description: "Use when reviewing a terms of service or terms of use document to produce a structured risk summary, issues table, and prioritized recommendations for attorney review."
practice_area: product-legal
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The terms of service or terms of use text"
  - "The product or service the terms govern"
  - "The user base and business model"
outputs:
  - "Structured risk summary"
  - "Issues table and prioritized recommendations for attorney review"
related_skills:
  - skills/contracts/nda-review/SKILL.md
  - skills/privacy/privacy-policy-gap-review/SKILL.md
  - skills/product-legal/launch-review/SKILL.md
tags:
  - product-legal
  - terms-of-service
  - contract-review
  - consumer-terms
  - risk-summary
---

# Terms of Service Review

## Purpose

Produce a structured, attorney-ready review of a terms of service (ToS) or terms of use (ToU) document, for either a consumer (B2C) or business-to-business (B2B) context. This skill assesses key legal provisions, identifies missing or one-sided terms, flags enforceability concerns, and notes inconsistencies with linked policies. It produces draft legal work product for attorney review — not legal advice, and not a determination that any provision is enforceable or compliant.

## Use When

- A user asks to "review our terms," "check our ToS," "are our terms okay?" or "what are the risks in this agreement?"
- A company is launching a new product or service and needs its first ToS reviewed before publication.
- An existing ToS is being updated and the changes require legal review.
- A company is evaluating a third party's ToS before agreeing to it (e.g., as a developer accepting a platform's terms).
- Legal counsel needs a structured first-pass triage of a lengthy ToS before conducting a detailed substantive review.
- A launch review (see `launch-review`) has flagged the ToS as requiring deeper analysis.

## Required Inputs

- **The full ToS text**: uploaded, pasted, or linked. If linked, the text must be retrieved and reviewed — do not rely on a URL alone.
- **Product or service context**: what the platform or service does, who operates it, and who the users are.
- **B2C or B2B context**: whether the terms govern consumer relationships, business relationships, or both.
- **Jurisdiction**: the governing law and dispute resolution forum as stated in the document, and the primary markets where the service operates. Flag as `[CONFIRM: jurisdiction]` if not provided.
- **Linked policies** *(if available)*: the linked or incorporated privacy policy, acceptable use policy, refund policy, or other referenced documents.

If the ToS text is not provided, stop and request it. Do not fabricate terms or assume what the document says.

## Do Not Use When

- The document is an NDA or confidentiality agreement (use `nda-review`).
- The document is a privacy policy reviewed in isolation (use `privacy-policy-gap-review`).
- The review is of a broad product launch across multiple legal areas (use `launch-review`).
- The goal is to draft a ToS from scratch — this skill reviews existing documents.
- The user wants a legal opinion on whether a specific clause is enforceable in a specific jurisdiction — this skill flags risks and routes; it does not render legal opinions.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice and does not constitute legal sign-off on the document.
- Do not assert that any provision is enforceable, unenforceable, compliant, or lawful. Flag concerns and route to counsel.
- Do not invent statutory standards, case law, regulatory guidance, or consumer protection rules. If a legal framework is relevant, name it and flag it for attorney verification.
- Distinguish what the document actually says (quoted), from what it implies (inferred), from what is assumed (flagged), and from what must be confirmed (`[CONFIRM: ...]`).
- Consumer-facing terms carry heightened scrutiny — flag provisions that may be unconscionable, surprising to a reasonable consumer, or subject to consumer protection regulation.
- Do not omit provisions because they appear standard. Every significant provision should be assessed.
- If the document references but does not include linked policies, flag those gaps prominently.
- Do not place client-sensitive business information into reusable templates.

## Workflow

1. **Confirm inputs.** Verify that the full ToS text and context are provided. List what was received and flag anything missing or assumed.

2. **Identify document structure and scope.** Note the document's title, effective date, version, governing law clause, and the parties it governs. Identify whether it is B2C, B2B, or hybrid. Identify all documents incorporated by reference.

3. **Acceptance mechanism and contract formation.** Assess how users accept the terms: clickwrap, browsewrap, sign-in-wrap, or electronic signature. Flag whether the acceptance mechanism is likely sufficient to form a binding agreement, and note any weaknesses (e.g., browsewrap with no conspicuous notice).

4. **Scope of license and use rights.** Summarize the rights granted to users and the rights reserved by the operator. Flag overly broad operator rights, missing grant language, or ambiguity about what users may and may not do.

5. **User content and intellectual property.** Review user content license provisions: what rights users grant, whether the license is exclusive, sublicensable, irrevocable, or royalty-free, and whether users retain ownership. Flag missing or overbroad provisions. Note any AI training use of user content.

6. **Acceptable use policy.** Assess the prohibited conduct provisions. Flag: overly vague prohibitions, missing categories of prohibited conduct, inconsistency with the linked AUP if separate, and enforcement/termination rights tied to violations.

7. **Payment, subscription, and auto-renewal terms.** Review payment obligations, subscription pricing, auto-renewal mechanics, cancellation rights, and refund policies. Flag missing disclosures, compliance with auto-renewal statutes `[CONFIRM: applicable state/country auto-renewal laws]`, and ambiguous or one-sided terms.

8. **Disclaimers and warranty language.** Assess the warranty disclaimer: whether it is conspicuous (all-caps or equivalent), whether it covers the relevant services, and whether it is consistent with implied warranty obligations in applicable jurisdictions. Flag for consumer law analysis in B2C contexts.

9. **Limitation of liability.** Review the limitation of liability clause: cap amount (if any), excluded categories, mutual or unilateral structure, and any carve-outs. Flag unconscionability risk in consumer contracts and jurisdictions that limit liability caps.

10. **Indemnification.** Assess who indemnifies whom, for what, and subject to what conditions. Flag one-sided indemnification obligations, missing notice requirements, and indemnification for IP infringement.

11. **Dispute resolution and class-action waiver.** Review arbitration clauses, class-action waivers, jury trial waivers, venue selection, and governing law. Flag enforceability concerns `[CONFIRM: applicable jurisdiction's arbitration and class-waiver law]`, unconscionability risks, and opt-out mechanisms.

12. **Termination.** Assess termination rights — for cause, for convenience, and by either party. Flag missing notice requirements, data return or deletion obligations on termination, and survival of obligations.

13. **Modification and notice mechanism.** Review how the operator may amend the terms and how notice is given. Flag: unilateral amendment with no notice, inadequate notice periods, and whether continued use constitutes acceptance of material changes.

14. **Consistency with linked policies.** Compare key provisions against the linked privacy policy and any other incorporated documents. Flag material inconsistencies (e.g., data use rights in the ToS that conflict with the privacy policy).

15. **Compile the issues table.** Assemble all findings into the structured table described in the Output Format section.

16. **Draft prioritized recommendations.** Rank issues as High / Medium / Low and provide a brief recommended action for each.

17. **List assumptions and open items.** State every assumption and every `[CONFIRM: ...]` item.

## Output Format

Deliver the following sections, in order, labeled as **DRAFT — FOR ATTORNEY REVIEW ONLY**:

1. **Review Summary**: document name, effective date, governing law, B2C/B2B context, review date, inputs received, and inputs missing or assumed.

2. **Document Overview**: brief description of structure, acceptance mechanism, scope, and linked documents (noting which were and were not reviewed).

3. **Issues Table** *(one row per provision area)*: a table with columns — Provision Area | Summary of Finding | Risk Level (High / Medium / Low) | Recommended Action | Open Questions / `[CONFIRM: ...]`.

4. **Prioritized Recommendations**: a numbered list of High-priority issues with specific recommended drafting actions, framed as options for attorney review — not final language.

5. **Consistency Gaps**: a brief list of material inconsistencies between the ToS and any linked policies reviewed.

6. **Assumptions and Open Items**: numbered list of every assumption and `[CONFIRM: ...]` item.

7. **Attorney Verification Checklist**: checkbox items (see below).

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] The full and final version of the ToS has been reviewed, not a draft or prior version.
- [ ] All documents incorporated by reference have been reviewed or their absence has been noted.
- [ ] The acceptance mechanism has been evaluated for enforceability under applicable law by counsel.
- [ ] Consumer-facing provisions have been reviewed for compliance with applicable consumer protection laws `[CONFIRM: jurisdictions]`.
- [ ] Auto-renewal and subscription terms have been reviewed against applicable state and country auto-renewal statutes.
- [ ] The arbitration clause and class-action waiver have been reviewed for enforceability in the governing jurisdiction(s).
- [ ] The limitation of liability and warranty disclaimer have been reviewed for conspicuousness and enforceability under applicable law.
- [ ] User content IP provisions, including any AI training use, have been reviewed by IP counsel.
- [ ] All inconsistencies between the ToS and the privacy policy have been resolved.
- [ ] No legal authority, statute, or regulation has been asserted without verification.
- [ ] All assumptions and `[CONFIRM: ...]` items have been resolved.
- [ ] This document is labeled as a draft and is not shared with third parties or used as legal sign-off on the ToS.
