---
name: Rule Change Summary
description: "Use when summarizing a regulatory rule change, proposed rule, or official guidance document and its practical impact on an organization, based on the actual document provided."
practice_area: regulatory
task_type: summarization
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The regulatory rule change, proposed rule, or official guidance document"
  - "The organization's relevant operations"
  - "The business context for the impact assessment"
outputs:
  - "Plain-language summary of the rule change"
  - "Practical impact table for attorney review"
related_skills:
  - skills/regulatory/enforcement-risk-memo/SKILL.md
  - skills/regulatory/compliance-gap-matrix/SKILL.md
tags:
  - regulatory
  - rule-change
  - regulatory-summary
  - impact-analysis
---

# Rule Change Summary

## Purpose

Produce a structured, attorney-ready summary of a regulatory rule change, proposed rule, interim final rule, or official guidance document, and identify its practical implications for a specific organization or practice area. The output captures what changed, who is affected, what new or modified obligations arise, and what implementation steps warrant attention — all grounded in the text actually provided.

This skill provides workflow discipline and output structure. It does not interpret regulations as legal advice or assert compliance conclusions.

## Use When

- A user says "summarize this new rule," "what does this guidance require," or "what changed from the old rule."
- Counsel or a compliance team receives a final or proposed rule and needs a structured first-pass summary to brief leadership or begin gap analysis.
- An organization needs to understand effective dates, compliance deadlines, and who within the organization is affected.
- A user provides a Federal Register notice, agency guidance, proposed rule text, or similar official document and asks for its significance.
- Preliminary scoping is needed before commissioning a full compliance gap review (see `compliance-gap-matrix`).

## Required Inputs

- **The official document**: the full text of the rule, proposed rule, guidance, or notice — uploaded or pasted. This is mandatory. If it is not provided, stop and request it before proceeding. Do not summarize rules from model background knowledge alone.
- **Organization description**: a brief description of the organization's business, size, and the activities likely to be regulated, so the impact summary is relevant.
- **Prior rule or baseline** (if available): the text or description of the prior rule, if the user wants a "what changed" comparison. If not provided, flag that the comparison is limited to what the document itself states about changes.
- **Jurisdiction and regulatory context**: confirm which agency issued the document and in what jurisdiction (federal, state, foreign). Flag as `[CONFIRM]` if not evident from the document.

If the official document is not provided, stop and request it. Do not proceed on the basis of a description alone. Do not invent rule text, citations, or dates.

## Do Not Use When

- The user wants to assess exposure for a specific practice against a rule (use `enforcement-risk-memo`).
- The user wants to map requirements against existing controls (use `compliance-gap-matrix`).
- No official document has been provided and cannot be obtained — model background knowledge about rule content is not a substitute for the actual document.
- The document is a judicial decision, contract, or internal policy rather than a regulatory instrument.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Summarize only the document actually provided. Do not supplement with rule text, preamble language, or agency interpretations from model background knowledge without clearly marking each instance `[UNVERIFIED — attorney must confirm against source]`.
- Do not invent effective dates, compliance deadlines, penalty provisions, or phase-in schedules. Every date in the summary must be drawn from the provided document and marked `[CONFIRM date against source]` until the attorney verifies it.
- Do not assert that the organization is or is not in compliance as a legal conclusion.
- Distinguish: (a) what the document states, (b) what the analyst infers about practical impact, (c) what remains uncertain and requires legal judgment.
- Use `[CONFIRM: ...]` placeholders whenever a material point cannot be determined from the document itself.
- Flag open questions about scope, applicability, and implementation that the attorney must resolve.
- Preserve confidentiality; do not incorporate client-specific sensitive facts into reusable templates.

## Workflow

1. **Confirm inputs.** Verify that the official document has been provided. If not, stop and request it. Identify the organization description and note whether a prior-rule baseline was provided.

2. **Identify the document.** Record:
   - Issuing body (agency name, bureau, or equivalent)
   - Document type (final rule, proposed rule, interim final rule, guidance, no-action letter, etc.)
   - Title and, if present in the document, citation or docket number — copied exactly from the document, not supplied independently
   - Publication or issuance date as stated in the document — marked `[CONFIRM]`

3. **Summarize the document's stated purpose and scope.** In plain language, what problem or policy goal does the issuing body say it is addressing? Who does the agency say is covered?

4. **Identify what changed.** If a prior-rule baseline is provided, compare the new text to it and list specific additions, deletions, and modifications. If no baseline is provided, summarize what the document itself describes as new or modified obligations, and note that a full comparison requires the prior rule.

5. **Extract effective and compliance dates.** List every date referenced in the document (effective date, compliance date, comment deadline, phase-in milestones). Mark each `[CONFIRM date against source text]`. Do not infer or interpolate dates not stated in the document.

6. **Identify who and what is affected.** Based on the document's scope provisions and the organization description provided, identify which parts of the organization, which products or services, and which functions are likely within scope. Flag applicability questions the attorney must resolve.

7. **List new or modified obligations.** Extract discrete, numbered obligations as stated in the document. Do not paraphrase in a way that alters meaning. Flag any obligation whose scope is ambiguous.

8. **Identify implementation considerations.** Based on the obligations and dates extracted, note operational areas likely to require attention: policy updates, system changes, training, reporting, recordkeeping, third-party contracts, board or management actions. These are preliminary observations, not a compliance roadmap.

9. **Flag open questions.** List interpretive questions, definitional ambiguities, and scope uncertainties that the attorney must resolve — either through the document's preamble, agency guidance, or legal research.

10. **Assemble the output.** Mark the document as a draft for attorney review.

## Output Format

Deliver the following sections in order:

**DRAFT RULE CHANGE SUMMARY — FOR ATTORNEY REVIEW ONLY**

1. **Document Identification** — Issuing body, document type, title, docket/citation (from document), issuance date `[CONFIRM]`, document status (proposed/final/interim).

2. **Stated Purpose and Scope** — Plain-language summary of the agency's stated rationale and covered entities/activities, drawn from the document text.

3. **What Changed** — Bulleted list of specific additions, deletions, and modifications. If no prior-rule baseline was provided, note that limitation explicitly.

4. **Key Dates** — Table: Date | Description | Source location in document | `[CONFIRM]` flag. Include effective date, compliance date, comment deadline, and any phase-in milestones.

5. **Applicability to This Organization** — Assessment of which business activities, products, functions, or entity types appear to fall within scope, given the organization description. Flag applicability questions as `[ATTORNEY TO CONFIRM]`.

6. **New and Modified Obligations** — Numbered list of discrete obligations extracted from the document. Quote key operative language where precision matters.

7. **Implementation Considerations** — Bulleted list of operational, policy, system, and governance areas likely requiring attention. Preliminary only — attorney to evaluate and prioritize.

8. **Open Questions and Interpretive Issues** — Bulleted list of ambiguities, undefined terms, scope questions, or areas where the document is unclear and further guidance or legal research is needed.

9. **Impact Summary Table** — An at-a-glance table of the obligations and changes identified:

   | Obligation / Change | Source (doc section) | Affected Function | Effective/Compliance Date | Status |
   |---|---|---|---|---|
   | [extracted from document] | [section ref] | [org function] | [CONFIRM] | Attorney to assess |

10. **Attorney Verification Items** — see the Attorney Verification Checklist below.

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] The document provided is the authoritative, final version; no subsequent amendments, corrections, or agency guidance have been issued.
- [ ] All dates (effective date, compliance date, comment deadline, phase-in milestones) have been verified against the source document and, where applicable, the Federal Register or official agency publication.
- [ ] The document citation, docket number, and title are accurate and complete.
- [ ] The "what changed" comparison is based on the actual prior rule text, not a summary or recollection.
- [ ] The applicability assessment has been confirmed by an attorney with subject-matter expertise; no applicability conclusion has been accepted as final from this draft alone.
- [ ] Each discrete obligation listed accurately reflects the rule text; no obligation was misstated through paraphrase.
- [ ] All interpretive questions and open items have been resolved or escalated appropriately before the summary is relied upon for compliance planning.
- [ ] No rule text, penalty provision, or agency interpretation was assumed from model background knowledge without verification against the provided document.
- [ ] The organization's actual activities have been mapped against the rule's scope by a qualified attorney, not solely by this summary.
- [ ] The draft is labeled appropriately and has not been transmitted to any third party without attorney review and approval.
