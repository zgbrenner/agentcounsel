---
name: Red-Team Verifier
description: Use when adversarially stress-testing a draft legal work product before attorney review to surface invented authority, unsupported claims, hidden assumptions, confidence overstatement, and structural defects.
---

# Red-Team Verifier

## Purpose

Adversarially stress-test a draft legal work product before it reaches the reviewing attorney. The skill conducts a systematic, category-by-category challenge pass across the draft, hunting for: invented or unverifiable authority (cases, statutes, citations, quotations); unsupported factual claims; hidden or unstated assumptions; missing or silently-resolved placeholders; overstated confidence and legal-advice framing; blended fact/assumption/analysis/strategy layers; unconfirmed jurisdiction; and computed or asserted deadlines. It produces a verification findings report — a structured, categorized list of defects with severity ratings and recommended fixes — plus an overall PASS / REVISE verdict. It produces draft legal work product for attorney review, not legal advice.

## Use When

- Any AgentCounsel draft is complete and is about to be finalized or passed to attorney review.
- An AI-generated legal draft of any type has been produced and a defect check is warranted before reliance.
- The user wants to confirm that a draft contains no fabricated authority, no silently-resolved gaps, and no confidence overstatement before it is used.
- A draft has been revised and a targeted re-check of the changed sections is needed.
- Quality-control review is required before a deliverable is circulated within a legal team.

## Required Inputs

- The complete draft to be verified (uploaded or pasted). Do not verify from a description alone.
- The skill or workflow that produced the draft, if known — this tells the verifier what structure and sourcing standards apply.
- The stated purpose and intended recipient of the draft.
- Optional: the jurisdiction and governing law the draft is supposed to address — if provided, the verifier can flag jurisdiction mismatches in addition to structural defects.

If the draft text is not provided, stop and request it. Do not conduct verification on a paraphrase or description of a draft.

## Do Not Use When

- The document is already a final, attorney-approved work product — verification before attorney review is the function of this skill; post-approval review is out of scope.
- The task is to create new legal analysis — run the relevant substantive skill first, then apply this skill to the output.
- The user needs a substantive legal review or opinion rather than a structural defect check (use the appropriate substantive skill).
- The input is a source document (contract, filing, statute) rather than a draft work product — use a review or research skill instead.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- This skill identifies defects; it does not fix them. Recommended fixes are directions for correction, not substitute analysis.
- Do not invent corrections. A finding that a citation may be fabricated is a flag for attorney verification, not a conclusion that it is fabricated.
- Never assert that an authority exists or does not exist based on model background knowledge. Mark all unverifiable citations as unverified and route them for attorney confirmation.
- Do not resolve jurisdiction gaps, compute deadlines, or fill in missing analysis in the course of verification. Flag each gap as a defect with a `[VERIFY: ...]` or `[CONFIRM: ...]` placeholder.
- A PASS verdict means the draft survived this adversarial pass; it does not mean the draft is legally correct, accurate, or final. Attorney review remains mandatory.
- Do not place client-sensitive facts from the draft into reusable templates or outputs beyond this findings report.
- Keep the findings report clearly labeled as draft work product.

## Workflow

Work through the draft category by category, in this order. Record every finding before moving to the next category.

1. **Confirm inputs.** Verify that you have the complete draft text, the draft's stated purpose, and the intended recipient. If the draft is incomplete or the purpose is unclear, record that as the first finding and continue with what is available.

2. **Authority and citation audit.** For every case, statute, regulation, rule, secondary source, citation, and quotation in the draft:
   - Classify the source as: (a) user-provided document (the highest-trust tier), (b) independently researched and verified, or (c) model background knowledge or unverifiable.
   - Flag every citation that cannot be traced to a user-provided or independently verified source as `[UNVERIFIED — must be confirmed before reliance]`.
   - Flag every quotation that cannot be verified against its source text.
   - Flag section numbers, docket numbers, reporter references, and URLs that cannot be confirmed.
   - Record each finding with its location in the draft, the authority name or claim as stated, and the recommended action.

3. **Factual claim audit.** For every factual claim in the draft:
   - Identify whether it traces to a user-provided document, a client-provided representation, or neither.
   - Flag facts with no stated source as unsupported.
   - Flag facts that contradict or go beyond the provided inputs.
   - Note any fact that appears to have been inferred or assumed but is stated as if established.

4. **Assumption audit.** For every assumption the draft makes:
   - Check whether the assumption is explicitly labeled as such.
   - Flag hidden assumptions — conclusions that depend on an unstated premise.
   - Flag assumptions that have been silently resolved rather than presented for attorney confirmation.

5. **Placeholder audit.** Scan for:
   - Missing placeholders: gaps in jurisdiction, governing law, deadline, party, or required input that should carry a `[CONFIRM: ...]` or `[VERIFY: ...]` marker but do not.
   - Silently resolved placeholders: markers that were present in an earlier stage but appear to have been filled in without verification.
   - Incomplete placeholders: markers like `[TBD]` or `[INSERT]` that signal unfinished work.

6. **Confidence and framing audit.** Check every conclusion, summary, and recommendation for:
   - Legal-advice framing ("you must," "you are required to," "this is legal," "this is illegal") not accompanied by a clear draft disclaimer.
   - Overstatement of certainty (unhedged conclusions on unsettled or jurisdiction-specific questions).
   - Statements that present analysis as a holding or final determination.
   - Missing qualification of confidence level on contested or uncertain points.

7. **Layer-separation audit.** Verify that the draft visibly separates:
   - Facts from assumptions.
   - Legal authority from analysis.
   - Analysis from strategy or recommendation.
   - Verification items from resolved conclusions.
   Flag any passage where two or more layers are blended without labeling.

8. **Jurisdiction and deadline audit.** Confirm:
   - Jurisdiction is stated or explicitly flagged as unknown with a `[verify jurisdiction]` marker.
   - Governing law is identified or flagged.
   - No deadline has been computed or asserted by the draft. Flag any date presented as a computed deadline, limitations period, or notice period as `[deadline verification required]`.
   - Any jurisdiction-specific legal proposition is either (a) verified to the stated jurisdiction or (b) carries a `[verify jurisdiction]` flag.

9. **Completeness check.** Verify that the draft:
   - Addresses all issues it was scoped to address, or explains why an issue is out of scope.
   - Includes the required draft label ("draft legal work product for attorney review — not legal advice").
   - Includes an attorney verification checklist or routes the reader to one.
   - Does not omit an adverse authority or unfavorable analysis that would be material to attorney review.

10. **Assign severity to each finding.** Rate each recorded finding:
    - **Critical** — a defect that, if unaddressed, could cause an attorney to rely on invented authority, a missed deadline, a waived right, or a fundamentally incorrect conclusion. Must be resolved before the draft proceeds.
    - **Material** — a defect that materially affects the reliability or completeness of the draft. Should be resolved before the draft is relied upon.
    - **Minor** — a formatting, labeling, or style defect that does not affect substance but should be corrected.

11. **Assign the overall verdict:**
    - **REVISE** — one or more Critical or Material findings are present. The draft must be corrected and re-verified (or reviewed by the attorney with the findings report in hand) before reliance.
    - **PASS** — no Critical or Material findings. Minor findings, if any, are listed for optional correction. Attorney review remains mandatory regardless of a PASS verdict.

12. **Assemble the findings report** using the output format below.

## Output Format

Deliver a Verification Findings Report with the following sections:

1. **Report Header** — Draft title or description; date of verification; overall verdict (PASS / REVISE); count of Critical, Material, and Minor findings.
2. **Overall Verdict** — PASS or REVISE, with a one-paragraph explanation of the basis.
3. **Findings by Category** — One section per audit category above. Within each section, list findings as a table:

   | # | Location | Finding | Severity | Recommended Action |
   |---|----------|---------|----------|--------------------|

   If a category produced no findings, record "No findings in this category."

4. **Critical Findings Summary** — A consolidated list of all Critical findings only, for rapid attorney attention.
5. **Verification Items for Attorney** — Items the verifier flagged as unverifiable by this skill and that require attorney or researcher confirmation (for example, citation existence, governing-law accuracy, deadline verification).
6. **Limitations of This Report** — A brief statement of what this skill cannot verify: whether authority says what is claimed, whether analysis is legally correct, whether strategy is sound, and whether the draft is complete for its legal purpose. Those are attorney functions.

Label the report: **Draft legal work product for attorney review. Not legal advice.**

## Attorney Verification Checklist

- [ ] All Critical findings have been reviewed and resolved or consciously accepted with a documented rationale.
- [ ] All Material findings have been reviewed; any accepted without correction are documented.
- [ ] Every citation flagged as unverified has been independently confirmed to exist and to support the stated proposition.
- [ ] Every quotation flagged as unverified has been checked against the source text.
- [ ] Every jurisdiction gap has been resolved; no jurisdiction-specific analysis relies on an unconfirmed jurisdiction.
- [ ] No deadline, limitations period, or notice period in the draft was computed by the agent; all dates have been attorney-verified.
- [ ] All hidden assumptions have been surfaced and either confirmed or corrected.
- [ ] All silently-resolved placeholders have been reviewed and properly completed.
- [ ] The draft's confidence framing is appropriate; no statement presents analysis as legal advice or a final determination.
- [ ] Fact, assumption, authority, analysis, and strategy layers are visibly separated in the revised draft.
- [ ] The PASS verdict (if given) has been noted; attorney review is still required regardless of that verdict.
- [ ] The revised draft carries the required draft label and an attorney verification checklist.
