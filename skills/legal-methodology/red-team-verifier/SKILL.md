---
name: Red-Team Verifier
description: "Use when checking whether a legal memo, contract review, demand letter, risk matrix, research summary, draft filing, or other legal AI output is reliable enough to rely on — adversarially stress-testing it before attorney review to surface invented authority, unsupported claims, weak reasoning, jurisdiction and deadline gaps, and professional-responsibility issues."
practice_area: legal-methodology
task_type: verification
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The legal draft or AI output to verify"
  - "The sources, record, or instructions it relied on"
  - "The intended use and audience of the output"
outputs:
  - "Verification findings report with a reliability verdict for attorney review"
related_skills:
  - skills/legal-methodology/source-validation/SKILL.md
  - skills/legal-methodology/risk-assessment/SKILL.md
tags:
  - legal-methodology
  - quality-control
  - verification
  - red-team
  - hallucination-check
---

# Red-Team Verifier

## Purpose

Adversarially stress-test a legal work product before anyone relies on it. This is AgentCounsel's universal quality-control workflow: it applies to any legal output — a memo, a contract or document review, a demand letter, a risk matrix, a client email, a research summary, a draft filing, or any other analysis — whether the output was produced by an AgentCounsel skill, another AI tool, or a person.

The skill conducts a systematic, category-by-category challenge pass across the draft, hunting for: invented or unverifiable authority; unsupported legal and factual claims; unstated jurisdiction and unverified timing; hidden assumptions and missing facts; weak or incomplete legal reasoning; professional-responsibility problems (language that reads as legal advice, lost attorney-review framing, confidentiality and privilege exposure); confidence overstatement; and structural defects. It produces a verification findings report — a structured set of defects with severity ratings and recommended fixes — plus an overall PASS / REVISE verdict.

It produces draft legal work product for attorney review. It is not legal advice, and a PASS verdict is not a substitute for attorney review.

## Use When

- The user asks to check, sanity-check, or quality-control a legal memo, a contract or document review, a demand letter, a legal analysis, a risk matrix, a client email, a research summary, or a draft filing.
- The user asks "is this good enough?", "is this ready to send?", or "can I rely on this?"
- The user asks for the weaknesses, blind spots, or missing issues in a legal draft.
- The user asks for a hallucination check, a citation check, or a check for invented authority.
- The user asks whether a draft is ready for — or has been adequately prepared for — attorney review.
- Any AgentCounsel skill has produced a draft and a defect check is warranted before it is finalized or relied upon.
- A high-stakes legal output is about to be sent, filed, or acted on and a final adversarial pass is wanted.
- A draft has been revised and a targeted re-check of the changed sections is needed.

## Required Inputs

- The complete draft or output to be verified (uploaded or pasted). Do not verify from a description or summary alone.
- The type of output and the skill or process that produced it, if known — this tells the verifier what structure and sourcing standards apply.
- The stated purpose and intended recipient of the output (internal attorney, client, court, opposing party, regulator).
- Any source materials the draft relied on — provided documents, research, cited authority — if available, so the verifier can check claims against them rather than only flagging them.
- Optional: the jurisdiction and governing law the output is meant to address — if provided, the verifier can flag jurisdiction mismatches as well as structural defects.

If the draft text is not provided, stop and request it. Do not conduct verification on a paraphrase or description of a draft.

## Do Not Use When

- The document is already a final, attorney-approved work product — verification before attorney review is the function of this skill; post-approval audit is out of scope.
- No draft exists yet — run the relevant substantive skill to create the analysis first, then apply this skill to the output.
- The user needs a substantive legal review, a legal opinion, or the actual legal analysis rather than a quality-control defect check — use the appropriate substantive skill. This skill checks reasoning for completeness and rigor; it does not supply the missing reasoning.
- The input is a source document (a contract, filing, or statute to be analyzed) rather than a draft work product about it — use a review or research skill instead.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- This skill identifies defects; it does not fix them. Recommended revisions are directions for correction, not substitute analysis.
- This skill checks the quality of reasoning; it does not perform the underlying legal analysis. Where reasoning is weak or an element is missing, flag it for the drafter or the attorney — do not supply the missing analysis.
- Do not invent corrections. A finding that a citation may be fabricated is a flag for attorney verification, not a conclusion that it is fabricated.
- Never assert that an authority exists or does not exist based on model background knowledge. Mark all unverifiable citations as unverified and route them for attorney confirmation.
- Do not resolve jurisdiction gaps, compute deadlines, or fill in missing analysis in the course of verification. Flag each gap as a defect with a `[VERIFY: ...]` or `[CONFIRM: ...]` placeholder.
- A PASS verdict means the draft survived this adversarial pass; it does not mean the draft is legally correct, complete, or final. Attorney review remains mandatory.
- Do not place client-sensitive facts from the draft into reusable templates or any output beyond this findings report.
- Keep the findings report clearly labeled as draft work product.

## Workflow

Work through the draft category by category, in this order. Record every finding — its location, the issue, and the recommended action — before moving to the next category.

1. **Confirm inputs.** Verify that you have the complete draft text, the draft's type and stated purpose, and the intended recipient. If the draft is incomplete or the purpose is unclear, record that as the first finding and continue with what is available.

2. **Source-support audit — authority and citations.** For every legal claim and every cited or quoted authority (case, statute, regulation, rule, secondary source, citation, quotation) in the draft:
   - Sort each legal claim into one of three support states: (a) **supported** — backed by a provided source or by independently verified authority that is cited; (b) **needs citation** — a proposition that may well be correct but carries no citation and must have one before reliance; (c) **unsupported** — a claim with no source and no evident basis, or one that goes beyond what any cited source actually says.
   - Classify each cited source's trust tier: user-provided document (highest trust), independently researched and verified, or model background knowledge / unverifiable.
   - Flag every citation that cannot be traced to a user-provided or independently verified source as `[UNVERIFIED — must be confirmed before reliance]`.
   - Flag every quotation that cannot be verified against its source text, and every section number, docket number, reporter reference, or URL that cannot be confirmed.
   - Record each finding with its location in the draft, the claim or authority as stated, its support state, and the recommended action.

3. **Factual claim audit.** For every factual claim in the draft:
   - Identify whether it traces to a user-provided document, a client representation, or neither.
   - Flag facts with no stated source as unsupported.
   - Flag facts that contradict or go beyond the provided inputs.
   - Flag any fact that appears to have been inferred or assumed but is stated as if established.

4. **Assumption and missing-fact audit.**
   - For every assumption the draft makes: check whether it is explicitly labeled as an assumption; flag hidden assumptions — conclusions that depend on an unstated premise; flag assumptions that have been silently resolved rather than presented for attorney confirmation.
   - Identify missing facts: facts not present in the draft whose answer could change the analysis or the result. For each, note how a different answer would change the conclusion.
   - Flag any conclusion stated more confidently than the underlying facts support.

5. **Legal-reasoning audit.** For each legal conclusion or argument in the draft, test the structure of the reasoning:
   - **Rule statement.** Is the governing rule, standard, or test stated, and stated accurately and completely? Flag a missing, vague, or partial rule statement.
   - **Element coverage.** If the rule has elements or factors, does the analysis address each one? Flag any element or factor that is skipped, assumed satisfied, or merged with another.
   - **Application.** Does the draft apply the rule to the specific facts, or does it state a conclusion without connecting it to the facts? Flag conclusory analysis.
   - **Counterarguments.** Does the draft acknowledge the strongest opposing argument and any adverse authority? Flag a one-sided analysis that omits the obvious counterargument.
   - **Exceptions and limits.** Are exceptions, defenses, carve-outs, and limits on the rule identified? Flag an analysis that states a rule without its known exceptions.
   - **Ambiguity.** Where the law is unsettled, the facts are ambiguous, or the outcome is genuinely close, does the draft say so? Flag false certainty on an open question.
   - **Analogies.** Are comparisons to other cases, deals, or situations sound, or do they rest on a weak or superficial similarity? Flag weak analogies.
   Record each finding. Do not supply the missing reasoning — flag it for the drafter or the attorney.

6. **Jurisdiction and timing audit.** Confirm:
   - The relevant jurisdiction is stated, or explicitly flagged as unknown with a `[verify jurisdiction]` marker. Flag any jurisdiction-specific proposition that is not tied to a confirmed jurisdiction.
   - Governing law is identified or flagged.
   - Every date that matters legally — a deadline, limitations period, notice period, filing date, effective date, or renewal date — is identified, and none has been computed or asserted by the draft. Flag each as `[deadline verification required]`.
   - Time-sensitive legal statements — a rule that may have changed, a regulation with a future effective date, an assertion that depends on the current state of the law — are flagged to be confirmed as of a stated date.

7. **Placeholder audit.** Scan for:
   - Missing placeholders: gaps in jurisdiction, governing law, deadline, party, or required input that should carry a `[CONFIRM: ...]` or `[VERIFY: ...]` marker but do not.
   - Silently resolved placeholders: markers that were present at an earlier stage but appear to have been filled in without verification.
   - Incomplete placeholders: markers like `[TBD]` or `[INSERT]` that signal unfinished work.

8. **Confidence and framing audit.** Check every conclusion, summary, and recommendation for:
   - Overstatement of certainty — unhedged conclusions on unsettled or jurisdiction-specific questions.
   - Statements that present analysis as a holding or a final determination.
   - Missing qualification of the confidence level on contested or uncertain points.
   - A summary or executive section that reads as more confident than the detailed analysis beneath it.

9. **Professional-responsibility audit.** Check the draft against core professional-responsibility risks:
   - **Unauthorized-advice framing.** Flag language that reads as legal advice to a non-client or as a directive — for example, telling the reader what they "must" do, what they "are required" to do, or that something "is legal" or "is illegal" — where it is not clearly framed as analysis for attorney review. Flag any passage that, if read by a non-lawyer recipient, would function as a legal opinion they could act on without an attorney.
   - **Attorney-review framing.** Confirm the draft is labeled as draft legal work product for attorney review and that the label has not been dropped, buried, or contradicted by confident closing language. Flag a draft that no longer reads as a draft.
   - **Confidentiality and privilege.** Flag client-sensitive facts, privileged communications, or attorney work product that appear in a section meant to be shared more widely, or that would lose protection if the draft were sent to its stated recipient. Flag the absence of a privilege or confidentiality designation where one is warranted, and any reusable or template-bound portion that has absorbed client-specific facts.
   - **Recipient mismatch.** Compare the draft's content and framing to its stated recipient (internal attorney, client, court, opposing party, regulator). Flag content that is inappropriate or risky to disclose to that recipient.
   Do not resolve these issues — flag each for attorney judgment.

10. **Layer-separation audit.** Verify that the draft visibly separates:
    - Facts from assumptions.
    - Legal authority from analysis.
    - Analysis from strategy or recommendation.
    - Verification items from resolved conclusions.
    Flag any passage where two or more layers are blended without labeling.

11. **Completeness check.** Verify that the draft:
    - Addresses every issue it was scoped to address, or explains why an issue is out of scope.
    - Includes the required draft label ("draft legal work product for attorney review — not legal advice").
    - Includes an attorney verification checklist or routes the reader to one.
    - Does not omit an adverse authority or unfavorable analysis that would be material to attorney review.
    - Follows the output structure its originating skill or the task called for.

12. **Assign severity to each finding.** Rate each recorded finding:
    - **Critical** — a defect that, if unaddressed, could cause an attorney to rely on invented authority, a missed deadline, a waived right, a professional-responsibility violation, or a fundamentally incorrect conclusion. Must be resolved before the draft proceeds.
    - **Material** — a defect that materially affects the reliability or completeness of the draft. Should be resolved before the draft is relied upon.
    - **Minor** — a formatting, labeling, or style defect that does not affect substance but should be corrected.

13. **Assign the overall verdict:**
    - **REVISE** — one or more Critical or Material findings are present. The draft must be corrected and re-verified (or reviewed by the attorney with the findings report in hand) before reliance.
    - **PASS** — no Critical or Material findings. Minor findings, if any, are listed for optional correction. Attorney review remains mandatory regardless of a PASS verdict.

14. **Assemble the findings report** using the output format below.

## Output Format

Deliver a Verification Findings Report with the following sections. Label the report: **Draft legal work product for attorney review. Not legal advice.**

1. **Executive Risk Summary** — The overall verdict (PASS / REVISE); the count of Critical, Material, and Minor findings; the draft title or description and the date of verification; and a short plain-language paragraph stating how reliable the draft is, what the most serious risks are, and whether it is ready to go to attorney review.

2. **Major Problems** — A consolidated list of every Critical and Material finding, ordered by severity. For each: its location in the draft, the audit category it came from, the defect, and why it matters. This is the section a reviewing attorney should read first.

3. **Unsupported Claims Table** — A table of every legal and factual claim that lacks adequate support:

   | # | Claim (as stated) | Location | Support state | Recommended action |
   |---|-------------------|----------|---------------|--------------------|

   Support state is one of: supported, needs citation, or unsupported. Include every `[UNVERIFIED]` authority and every unsourced factual claim.

4. **Missing Facts** — Facts not present in the draft whose answer could change the analysis or the result. For each, note what is missing and how a different answer would change the conclusion.

5. **Jurisdiction and Deadline Flags** — Every jurisdiction gap, every governing-law assumption, and every legally significant date (deadline, limitations period, notice period, filing date, effective date) that requires verification, plus every time-sensitive legal statement flagged to be confirmed as of a stated date. No date in this section is asserted as correct; each is flagged for attorney verification.

6. **Suggested Revisions** — Recommended directions for correction, organized by priority (Critical first, then Material, then Minor). Each is a direction for the drafter or the attorney, not substitute analysis. Note where a revision requires legal judgment the verifier cannot supply.

7. **Attorney Verification Checklist** — The checklist below, with every item the verification surfaced as still open marked for the reviewing attorney.

Close the report with a brief **Scope and Limitations** note: this skill checks a draft for defects in support, reasoning structure, framing, and completeness; it does not verify that authority says what is claimed, that the analysis is legally correct, that strategy is sound, or that the draft is complete for its legal purpose. Those remain attorney functions.

## Attorney Verification Checklist

- [ ] All Critical findings have been reviewed and resolved, or consciously accepted with a documented rationale.
- [ ] All Material findings have been reviewed; any accepted without correction are documented.
- [ ] Every citation flagged as unverified has been independently confirmed to exist and to support the stated proposition.
- [ ] Every quotation flagged as unverified has been checked against the source text.
- [ ] Every claim in the Unsupported Claims Table has been given a verified citation or removed.
- [ ] Every jurisdiction gap has been resolved; no jurisdiction-specific analysis relies on an unconfirmed jurisdiction.
- [ ] No deadline, limitations period, notice period, or other legally significant date in the draft was computed by the agent; all dates have been attorney-verified.
- [ ] Every missing fact identified has been obtained, or its absence consciously accepted.
- [ ] The legal reasoning has been checked: the governing rule is stated correctly, each element is addressed, counterarguments and exceptions are considered, and genuine ambiguity is acknowledged.
- [ ] All hidden assumptions have been surfaced and either confirmed or corrected.
- [ ] All silently-resolved placeholders have been reviewed and properly completed.
- [ ] The draft's confidence framing is appropriate; no statement presents analysis as legal advice or as a final determination.
- [ ] Professional-responsibility flags have been resolved: no passage reads as unauthorized legal advice, the attorney-review framing is intact, and confidentiality and privilege are protected for the stated recipient.
- [ ] Fact, assumption, authority, analysis, and strategy layers are visibly separated in the revised draft.
- [ ] The PASS verdict (if given) has been noted; attorney review is still required regardless of that verdict.
- [ ] The revised draft carries the required draft label and an attorney verification checklist.
