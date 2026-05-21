---
name: Statutory Interpretation
description: "Use when applying a disciplined analytical method to parse and interpret a statutory, regulatory, or contractual provision — mapping structure, defined terms, and competing readings — to produce a structured interpretation worksheet for attorney review."
practice_area: legal-methodology
task_type: analysis
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The statutory, regulatory, or contractual provision text"
  - "The interpretive question to be resolved"
  - "Relevant context such as definitions and related provisions"
outputs:
  - "Structured interpretation worksheet mapping competing readings for attorney review"
related_skills:
  - skills/legal-research/legal-research-memo/SKILL.md
  - skills/contracts/contract-risk-review/SKILL.md
  - skills/legal-methodology/risk-assessment/SKILL.md
tags:
  - legal-methodology
  - statutory-interpretation
  - construction
  - provision-analysis
---

# Statutory Interpretation

## Purpose

Apply a disciplined, jurisdiction-agnostic analytical method for working through a statutory, regulatory, or contractual provision. The skill guides systematic parsing of operative text, mapping of structure and defined terms, framing of the precise interpretive question, identification of ambiguities and competing candidate readings, and flagging of every jurisdiction-specific interpretive question for attorney verification. It produces draft legal work product for attorney review — not legal advice and not an authoritative interpretation.

This skill teaches and applies the analytical method only. It does not and must not assert how any particular jurisdiction's courts interpret text, must not cite or invoke jurisdiction-specific interpretive canons as if they were settled authority, and must flag every jurisdiction-bound interpretive point with `[verify jurisdiction]`. What interpretive tools apply, what weight they carry, and what result they yield in a given jurisdiction are attorney-verification items without exception.

## Use When

- A user needs to analyze what a provision means or whether it applies to a given set of facts.
- The scope, reach, or limits of a statutory, regulatory, or contractual obligation are disputed or unclear.
- A user asks to "parse this provision," "interpret this clause," "what does this section mean," or "does this apply to my situation."
- Competing readings of the same text need to be identified, compared, and evaluated for purposes of drafting a memo, brief section, or negotiation position.
- A provision contains ambiguity, a defined term with contested scope, or a structure question (such as whether a modifier applies to one element or all of them) that requires systematic analysis before attorney resolution.
- A gap or conflict between two provisions needs to be framed before attorney analysis.

## Required Inputs

- The exact text of the provision to be interpreted. Do not analyze from paraphrase or description alone; the operative language must be present.
- The document or instrument in which the provision appears (statute, regulation, contract, ordinance, rule, or other), and the section or clause reference if known.
- The interpretive question: what specific question is the analysis trying to answer? If the user has not stated a specific question, stop and ask — do not assume scope.
- The factual context in which the provision is being applied: the facts or circumstances that trigger or potentially trigger the provision.
- Optional but recommended: the jurisdiction and governing law, so that jurisdiction-specific verification items can be targeted. If not provided, flag all jurisdiction-bound points with `[verify jurisdiction]`.
- Optional: related provisions, definitions sections, or other parts of the same instrument that affect the provision's meaning.

If the provision text or the interpretive question is not provided, stop and request it. Do not reconstruct legislative text or contractual language from memory.

## Do Not Use When

- The user needs a legal research memo on a broad area of law rather than interpretation of a specific provision (use `legal-research-memo`).
- The user needs a contract redline or risk review rather than interpretive analysis (use `nda-review` or `contract-risk-review`).
- The provision has already been definitively construed for the applicable jurisdiction by controlling authority and the question is simply applying that settled construction to new facts — interpretive analysis is unnecessary; apply the settled construction and flag it for attorney confirmation.
- The interpretive question is purely a strategic choice about which reading to advocate — that is an attorney judgment that goes beyond the method this skill supplies.
- The user is asking for legal advice about how a court will rule — this skill frames the question and the competing readings; it does not predict outcomes.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Do not assert how any jurisdiction's courts interpret text. Do not name or invoke jurisdiction-specific interpretive canons as authority. Mark every jurisdiction-bound interpretive point `[verify jurisdiction]`.
- Use only the text provided. Do not reconstruct, paraphrase, or substitute for the operative language. Quote the provision accurately where quotation is needed.
- Do not invent definitions, legislative history, drafting history, or extrinsic materials. If such materials would be relevant to the analysis, note that they should be researched and mark the point as a verification item.
- Do not state which candidate reading is legally correct. Frame and evaluate readings; leave selection to the attorney.
- Do not assert that a provision is ambiguous or unambiguous as a legal conclusion. Identify textual features that support each characterization and flag the ultimate determination as `[ATTORNEY TO CONFIRM: ambiguity determination]`.
- Do not compute, assert, or rely on effective dates, applicability dates, or any deadline. Mark any relevant date as `[deadline verification required]`.
- Do not carry analysis from one matter or provision into another. Each interpretive worksheet is matter-specific.
- Flag every place where the analysis depends on how a jurisdiction-specific interpretive rule would apply, using `[verify jurisdiction]`.

## Workflow

1. **Confirm inputs.** Verify that you have the exact provision text, the instrument it appears in, and a stated interpretive question. If the question is vague or overbroad, ask the user to narrow it before proceeding. If the provision text is missing, stop and request it.

2. **Transcribe and map the provision.** Reproduce the operative text exactly. Identify its structural components:
   - Subject (who or what the provision addresses).
   - Operative verb or obligation (what is required, prohibited, permitted, or defined).
   - Object (what the operative verb acts on).
   - Conditions, qualifications, and exceptions (when the provision applies or does not apply).
   - Any modifier or limiting phrase, and what it modifies.
   - Conjunctions and their role (does "and" mean conjunctive or disjunctive? does "or" mean inclusive or exclusive?) `[verify jurisdiction]`.
   - Lists and their structure (is the list exhaustive or illustrative? does a final modifier apply to all list items or only the last?) `[verify jurisdiction]`.

3. **Identify and map defined terms.** For every capitalized, quoted, or otherwise signaled defined term in the provision:
   - Locate the definition in the instrument if it exists, and transcribe it.
   - Note where the definition is absent, ambiguous, circular, or contested.
   - Note where a term is used in the provision without being defined in the instrument — flag as `[CONFIRM: definition source]`.
   - Substitute the definition into the provision text to test how the language reads with the definition applied.

4. **Frame the precise interpretive question.** Restate the question presented in a single, specific sentence: what word, phrase, structural feature, or interaction between provisions is at issue, and what does it mean to resolve it? If the user's original question is actually several distinct interpretive questions, break them apart and address each separately.

5. **Identify candidate readings.** For each interpretive question, articulate the plausible competing readings of the text:
   - State each reading in plain language.
   - Identify what textual feature, structural choice, or definitional decision each reading turns on.
   - Note which reading appears to be the plain-text reading and which requires a departure from the ordinary meaning of the language.
   - Note if a reading produces an anomalous, absurd, or internally inconsistent result — this is a textual signal that may be relevant to the analysis `[verify jurisdiction]`.

6. **Assess the textual support for each reading.** For each candidate reading, evaluate:
   - Ordinary meaning of the relevant words (without asserting dictionary authority; note that dictionary evidence may be relevant) `[verify jurisdiction]`.
   - Internal consistency: does the reading conflict with another provision in the same instrument?
   - Structural signals: headings, section numbering, organizational features `[verify jurisdiction]`.
   - Punctuation and grammatical structure.
   - Whether the same word or phrase is used elsewhere in the instrument and, if so, whether a consistent meaning is supported.
   Do not assert that any of these tools resolves the question; present them as factors for attorney analysis.

7. **Identify ambiguities and gaps.** Note every place where:
   - The text is susceptible to more than one reasonable reading.
   - A defined term is absent, incomplete, or does not clearly cover the situation.
   - The provision does not address a factual scenario it might have been expected to address.
   - Two provisions in the same instrument appear to conflict or overlap.
   Mark each ambiguity or gap with `[CONFIRM: ambiguity — attorney to assess]` or `[VERIFY: gap — see related provision]`.

8. **Flag jurisdiction-specific interpretive questions.** Identify every point in the analysis where the outcome depends on a jurisdiction-specific interpretive rule, canon, or body of case law — for example, how extrinsic evidence is treated, how ambiguities are resolved against a particular party, how administrative deference doctrines apply, or what the statutory-construction rules of the enacting jurisdiction require. Mark each such point `[verify jurisdiction]` and list it as an attorney verification item. Do not assert what any jurisdiction's rule is.

9. **Identify extrinsic materials that may be relevant.** Note — without asserting their availability, admissibility, or content — categories of extrinsic materials that an attorney may wish to research: legislative history, regulatory preambles, drafting history, prior versions of the text, agency guidance, or contemporaneous interpretive materials. Mark each as a research item, not a finding.

10. **Assemble the interpretation worksheet** using the output format below. Label it as a draft for attorney review.

## Output Format

Deliver a Statutory Interpretation Worksheet with the following sections:

1. **Worksheet Header** — Provision reference (document, section, date); interpretive question(s) stated precisely; jurisdiction (or `[verify jurisdiction]` if unknown); date of analysis.
2. **Provision Text** — The operative text reproduced exactly, with structural components labeled (subject, operative verb, object, conditions, modifiers, lists).
3. **Defined Terms Map** — Table: Term | Definition in instrument | Location | Notes (absent / ambiguous / contested).
4. **Interpretive Question(s)** — Each question stated as a single, specific sentence. If multiple, numbered separately.
5. **Candidate Readings** — For each question: a numbered list of candidate readings, each with a plain-language statement and an identification of what it turns on.
6. **Textual Analysis** — For each candidate reading: a structured assessment of the textual support, organized by analytical factor (ordinary meaning, internal consistency, structural signals, etc.). Presented as factors for attorney analysis, not conclusions.
7. **Ambiguities and Gaps** — A list of identified ambiguities and gaps, each with a `[CONFIRM: ...]` or `[VERIFY: ...]` marker.
8. **Jurisdiction-Specific Verification Items** — A list of every interpretive point that depends on a jurisdiction-specific rule, each marked `[verify jurisdiction]`, for attorney research and confirmation.
9. **Extrinsic Materials Research Items** — A list of categories of extrinsic materials that may be relevant, for attorney research — not findings.
10. **Assumptions** — Every assumption made in the analysis, explicitly listed.
11. **Open Items for Attorney Determination** — A checklist of all unresolved questions and points requiring attorney judgment.

Use `[CONFIRM: ...]` for every gap. Use `[verify jurisdiction]` at every jurisdiction-dependent point. Do not state conclusions on contested interpretive questions.

## Attorney Verification Checklist

- [ ] The provision text reproduced in the worksheet is accurate and complete, and matches the operative version applicable to the matter.
- [ ] The version and effective date of the instrument are confirmed `[deadline verification required]`.
- [ ] Every defined term is correctly identified, and the applicable definition is the one in force at the relevant time.
- [ ] The interpretive question is correctly framed for the legal issue the matter presents.
- [ ] All candidate readings are plausible readings of the text; none is a strawman.
- [ ] The textual analysis accurately identifies the features that bear on the question without importing jurisdiction-specific rules that have not been verified.
- [ ] Every `[verify jurisdiction]` flag has been resolved: the applicable interpretive rules for this jurisdiction have been confirmed by the attorney and applied.
- [ ] Extrinsic materials identified as potentially relevant have been researched and their significance assessed.
- [ ] Any ambiguity determination (ambiguous vs. unambiguous) has been made by the attorney, not the analysis.
- [ ] No legal conclusion about which reading prevails has been stated as settled; selection of the correct reading is an attorney judgment.
- [ ] All assumptions are confirmed or corrected.
- [ ] No deadline or effective date has been computed or assumed; all dates are attorney-verified.
- [ ] The worksheet does not constitute legal advice and is appropriately labeled.
