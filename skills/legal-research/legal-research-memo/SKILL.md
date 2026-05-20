---
name: Legal Research Memo
description: Use when producing a structured legal research memo in response to a specific legal question, organizing analysis using IRAC discipline (Question Presented, Brief Answer, Facts, Assumptions, Discussion/Analysis, Conclusion) with explicit sourcing requirements and attorney verification checkpoints.
---

# Legal Research Memo

## Purpose

Produce a structured, attorney-ready legal research memo in response to a discrete legal question. The memo organizes analysis using IRAC-style discipline — Question Presented, Brief Answer, Facts, Assumptions, Discussion/Analysis, Conclusion — and maintains a strict separation between facts, assumptions, applicable law, analysis, and open verification items. It produces draft legal work product for attorney review only. It is not legal advice and does not substitute for attorney judgment.

The most important discipline this skill enforces: **no legal authority — no case, statute, regulation, rule, secondary source, or quotation — may be stated as if it exists unless it comes from a user-provided document or has been independently researched and verified through a reliable source.** Every asserted authority must be checkable. Unverified authority must be marked with an explicit `[CONFIRM: ...]` placeholder and placed in the attorney verification section.

## Use When

- A user asks to "research this issue," "write a research memo," "what is the law on X," or "can you analyze whether Y is legal."
- A lawyer or legal team needs a first-pass research memo before attorney analysis.
- The user needs to organize known authorities and facts into a structured memo before a client call, brief, or negotiation.
- A question of law or mixed fact-and-law has been identified and needs structured written analysis.
- The user wants to document legal assumptions underlying a transaction, filing, or decision.
- A gap analysis is needed: what authorities support a position, and what do not.

## Required Inputs

- **The legal question(s)** — stated with specificity. Vague questions must be refined before proceeding; do not broaden or narrow the question without user confirmation.
- **Jurisdiction and governing law** — the applicable jurisdiction(s) and the body of law (federal, state, contractual, regulatory). If unknown, flag as `[CONFIRM: jurisdiction]` and note that the analysis cannot be completed without it.
- **Relevant facts** — the facts from which the legal question arises. Do not reconstruct or invent facts; use only facts the user has provided.
- **Procedural posture** — if applicable (e.g., pre-litigation, pending motion, transactional, regulatory inquiry).
- **Relevant date** — the date on which the legal question turns (e.g., the date of the alleged breach, the filing date, the effective date of a statute).
- Optional: any legal authorities, cases, statutes, or secondary sources the user has already identified. These will be incorporated and verified, not assumed to be accurate.
- Optional: the user's desired legal position or outcome (flags potential advocacy posture).

If the legal question, jurisdiction, or relevant facts are not provided, stop and request them. Do not begin analysis by guessing. Do not fabricate facts to make the question answerable.

## Do Not Use When

- The user needs a contract review (use `nda-review` or `contract-risk-review`).
- The user needs a litigation strategy memo or brief (use `litigation-strategy` where available).
- The user needs a regulatory compliance checklist (use the appropriate compliance skill).
- The question requires a formal legal opinion letter — those require an attorney and carry professional responsibility implications this skill cannot satisfy.
- The user is asking for real-time legal advice in an ongoing matter requiring immediate attorney judgment.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- **Do not invent legal authority.** Never state a case name, citation, holding, statute section, regulation, or quotation unless it is present in a user-provided document or has been retrieved from and verified through a reliable research source. Fabricated citations are a serious professional and ethical hazard.
- Every legal authority cited must be either (a) provided by the user or (b) explicitly noted as requiring attorney verification if it cannot be independently confirmed in this session.
- Do not paraphrase a case holding without citing the source. Do not cite a source without identifying where the specific proposition comes from.
- Distinguish clearly: (1) what the facts show, (2) what you are assuming, (3) what the law provides (with source), (4) what the analysis concludes, and (5) what remains for the attorney to confirm.
- Do not assume a statute or regulation is current. Flag recency as an attorney verification item unless the user has provided the current text.
- Do not resolve ambiguous facts in favor of either party without flagging that assumption explicitly.
- Identify any conflict of laws, choice-of-law, or multi-jurisdictional issue as an attorney verification item.
- Do not place client-sensitive facts into reusable templates.
- Use `[CONFIRM: ...]` placeholders wherever information is missing or uncertain. Never fill gaps with invented content.

## Workflow

1. **Confirm inputs.** Verify that you have a specific legal question, identified jurisdiction(s), relevant facts, and a relevant date. If anything is missing, request it before proceeding. Refine vague questions by asking clarifying questions — do not assume scope.

2. **Restate the Question(s) Presented.** Frame each legal question precisely: who did what, under what legal framework, in what jurisdiction, at what time. Limit each question to one discrete legal issue. If the user's question spans multiple issues, break it into separate Questions Presented.

3. **Draft the Brief Answer(s).** Provide a one-to-three sentence direct answer to each question: yes, no, probably, or uncertain — with a one-sentence reason. Do not elaborate here; save analysis for the Discussion section. If the answer depends entirely on unverified facts or law, say so explicitly.

4. **State the Facts.** Set out the legally relevant facts as provided by the user. Do not embellish, infer, or add facts not in the user's account. Note any factual gaps that are legally material. Label inferences as inferences, not facts.

5. **State Assumptions.** List every assumption being made — about facts, about the applicable legal standard, about the procedural posture, about the status of authorities. Each assumption is a potential attorney verification item.

6. **Conduct and document the Discussion/Analysis.** Apply an IRAC structure for each issue:
   - **Issue** — restate the specific sub-question.
   - **Rule** — state the applicable legal rule or standard, citing the source precisely. If the rule comes from a case, identify the court, date, and the specific holding. If from a statute or regulation, identify the section and version. If no verified rule is available, use `[CONFIRM: rule — no verified authority in this session]`.
   - **Application** — apply the rule to the facts. Flag where the facts are disputed, unclear, or assumed. Do not advocate silently; if analysis favors one side, note that.
   - **Conclusion** — state the tentative conclusion for the sub-issue, with confidence level (e.g., "likely," "uncertain," "turns on factual dispute").

7. **Write the Conclusion.** Summarize the overall answer to each Question Presented in two to five sentences. Identify the key legal and factual variables on which the answer depends. Do not overstate certainty.

8. **Compile the Authorities Cited table.** List every legal authority referenced in the memo — cases, statutes, regulations, secondary sources. For each, include: authority name/citation, source (user-provided or researched), proposition it stands for, and a verification checkbox. See `templates/legal-research-memo.md`.

9. **List Open Items for Attorney Verification.** Enumerate every factual gap, unverified authority, jurisdictional question, ambiguity, or strategic judgment that requires attorney review before the memo is relied upon.

10. **Assemble the memo** using `templates/legal-research-memo.md` and label it as a draft for attorney review.

## Output Format

Deliver a complete memo using the structure in `templates/legal-research-memo.md`:

1. **Header block** — To, From, Date, Re, Privilege designation.
2. **Question(s) Presented** — numbered, each limited to one issue.
3. **Brief Answer(s)** — direct, one-to-three sentences each.
4. **Facts** — user-provided facts only, clearly labeled.
5. **Assumptions** — explicit list.
6. **Discussion / Analysis** — IRAC per issue, with source citations for every rule stated.
7. **Conclusion** — summary with qualified confidence.
8. **Authorities Cited** — table with verification checkbox column.
9. **Open Items / Attorney Verification** — checkbox list.

Use `[CONFIRM: ...]` wherever a fact, authority, or conclusion is unverified. Do not omit a section because it is difficult to fill; instead, mark it with a placeholder and a note.

## Attorney Verification Checklist

- [ ] The legal question(s) are accurately and completely stated as the client intends them.
- [ ] Jurisdiction and governing law are correctly identified and appropriate for the matter.
- [ ] All facts stated in the memo are accurate and come from the client or verified sources — no facts have been invented or inferred without flagging.
- [ ] All assumptions are identified and their legal materiality has been assessed.
- [ ] Every case cited exists, the citation is accurate, and the holding attributed to it is correct.
- [ ] Every statute and regulation cited is current, in the correct version, and the section referenced says what the memo claims.
- [ ] No authority has been cited that was not in a user-provided document or independently verified in this session.
- [ ] The rule/holding has not been overstated, paraphrased inaccurately, or taken out of context.
- [ ] Adverse authority has been identified and addressed, not omitted.
- [ ] Any conflict-of-laws or choice-of-law issue has been identified and resolved or flagged.
- [ ] The analysis is presented from a neutral analytical posture, or the advocacy posture is explicitly noted.
- [ ] Confidence levels in the conclusion are appropriate given the state of the law and facts.
- [ ] All open items and `[CONFIRM: ...]` placeholders have been resolved before the memo is relied upon.
- [ ] Privilege and confidentiality designations are appropriate for how the memo will be circulated.
