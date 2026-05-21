---
name: Wage and Hour Question Triage
description: Use when a specific wage-and-hour or related employment question — such as overtime eligibility, exemption status, break entitlements, final-pay timing, paid-time-off payout, or leave eligibility — needs to be structured and analyzed against verified, jurisdiction-specific rules, producing a draft analysis for attorney review.
---

# Wage and Hour Question Triage

## Purpose

Produce a structured, attorney-ready draft analysis of a specific wage-and-hour or related employment question. The skill organizes the question, confirms the jurisdiction and operative facts, identifies what controlling rules must be researched and verified, applies those researched rules to the facts in a disciplined way, and flags whether the answer is clear, borderline, or in flux. It produces draft legal work product for attorney review — not legal advice, not a legal conclusion, and not a substitute for employment counsel.

This skill's entire value is the discipline it imposes: identify the jurisdiction, route every controlling rule to verified research, apply the researched rule to the facts, and flag close calls. It does not state any wage-and-hour rule, threshold, multiplier, deadline, exemption criterion, or computation formula from memory.

## Use When

- A user asks a specific question about overtime eligibility, exempt vs. non-exempt status, meal or rest break entitlements, final-pay timing, paid-time-off payout obligations, or leave eligibility for a particular worker or role.
- An employer, HR professional, or attorney needs a structured, research-ready intake of a wage-and-hour issue before legal analysis begins.
- A user asks: "Is this employee eligible for overtime?", "Do we have to pay out accrued PTO on termination?", "What are our break obligations for this schedule?", or a similar specific question.
- A question involves computing back-pay or unpaid wages and the user needs to understand what must be researched and verified before any figure is calculated.
- A question arises in a multi-jurisdiction employment context and the most-restrictive jurisdiction must be identified before analysis can begin.

## Required Inputs

- **The specific question**: the precise wage-and-hour or employment question to be analyzed. If the question is vague, clarify it before proceeding.
- **The jurisdiction(s)**: the state, province, or country whose law governs the work. For a multi-jurisdiction employer, all relevant jurisdictions where the work is performed. If unknown, flag as `[CONFIRM: governing jurisdiction]` and do not proceed past fact-gathering.
- **The operative facts**: the job title, a description of the worker's actual day-to-day duties and responsibilities, compensation structure and pay rate, hours worked and schedule, and the specific actions, payments, or events that gave rise to the question. General or conclusory descriptions of duties are not sufficient; the analysis depends on what the worker actually does.

If any required input is missing, stop and request it. Do not infer jurisdiction from the employer's headquarters, assume compensation structures, or fabricate duties not provided. Do not proceed with incomplete facts.

## Do Not Use When

- The question is whether a worker **should be classified** as an employee or independent contractor for a proposed engagement — use `worker-classification` instead.
- The user needs a formal legal research memorandum on a wage-and-hour topic — use `legal-research-memo` instead.
- The user wants a survey of the rules across multiple jurisdictions without a specific question to answer — that is a multi-jurisdiction survey task outside the scope of this skill; direct the user to counsel for that work.
- The question involves a pending or active litigation matter; active litigation strategy and discovery decisions require attorney direction from the outset.
- The user is seeking a legal conclusion that a particular pay practice or classification is lawful or unlawful — that determination requires attorney review and is beyond the scope of this skill.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review only. This is not legal advice and does not constitute a legal conclusion.
- **Do not state any wage-and-hour rule, threshold, multiplier, exemption criterion, lookback period, penalty rule, or computation formula from memory.** Treat all background knowledge about wage-and-hour standards as unverified until confirmed by current, jurisdiction-specific research. A confident wrong number is the worst-case output this skill can produce.
- Do not assert, quote, or paraphrase any statute, regulation, agency guidance, or case law from memory. Use `[citation needed]` wherever legal authority would be referenced and flag it for verified research.
- For any question involving back-pay, unpaid wages, or wage computation: identify the components that must be researched and verified before any figure is calculated. Do not produce a computed figure. Flag every variable `[VERIFY]`.
- Do not invent facts, assume job duties, infer compensation arrangements, or fabricate relevant dates or events not provided by the user.
- Separate facts, assumptions, law, analysis, and verification items. Label each category clearly.
- Identify the governing jurisdiction; if unknown, flag with `[CONFIRM: governing jurisdiction]` and do not proceed.
- For multi-jurisdiction questions: flag that the most-restrictive jurisdiction may control certain obligations and that identifying it requires verified research — do not assume which jurisdiction is most restrictive from memory.
- If a controlling rule has recently changed or is known to be in flux, flag it as `[VERIFY: rule may have changed — confirm effective date]`. Do not state what the prior or current rule is from memory.
- Preserve confidentiality and privilege; do not include client-identifying details in reusable templates or shared outputs.
- Flag every point of uncertainty rather than resolving it silently. Where facts are ambiguous or a question could go either way under the researched rule, note it as borderline and recommend attorney review before any action is taken.

## Workflow

1. **Confirm and clarify the question.** Restate the specific wage-and-hour question in precise terms. If the question is ambiguous — for example, "are we handling overtime correctly?" without specifying a role, schedule, or concern — clarify it before proceeding. A vague question produces a vague analysis; the question must be specific enough to frame the research.

2. **Confirm required inputs.** Verify that all required inputs are present: the specific question, the jurisdiction(s), and the operative facts (job title, actual duties, compensation structure, schedule, and the events giving rise to the question). If any input is missing, stop and request it. Do not infer, assume, or fabricate.

3. **Identify and confirm the jurisdiction.** State the jurisdiction(s) whose law will govern the analysis. If the employer operates in multiple jurisdictions, flag that identifying the most-restrictive jurisdiction for the specific obligation at issue requires verified research, and mark the jurisdiction analysis `[CONFIRM: governing jurisdiction]` until confirmed. Do not assume which jurisdiction applies or which is most restrictive.

4. **Identify the controlling legal framework — route to verified research.** Identify the category of rule that governs the question (for example: overtime eligibility, an exemption test, break obligations, final-pay timing, or leave entitlement). For each category:
   - State what type of rule applies in general terms (e.g., "overtime eligibility is typically governed by state wage-and-hour law and, where applicable, federal law, whichever provides greater protection").
   - Flag every specific threshold, criterion, deadline, multiplier, and formula as `[VERIFY]` / `[citation needed]` / `[verify jurisdiction]` — do not state any of those specifics from memory.
   - Note if the rule is known to vary significantly by jurisdiction without stating what the rule is in any particular jurisdiction.
   - If the question involves an exemption, identify the categories of facts that bear on exemption analysis (for example: duties actually performed, compensation method, compensation level) and flag each element as requiring verified research. Do not state exemption criteria, salary thresholds, or duties tests from memory.

5. **Apply the researched rule to the facts.** Using only rules that have been identified and flagged for verified research (not asserted from memory), apply the framework to the operative facts provided. Present the application as a structured analysis:
   - **Facts as provided**: summarize the operative facts without embellishment.
   - **Framework elements**: for each element of the applicable rule `[citation needed]`, state what fact is relevant and how it bears on the element — but do not supply the rule's numeric content from memory; use `[VERIFY: applicable threshold/criterion]` placeholders throughout.
   - **Preliminary assessment**: based on the facts as stated and the framework as identified, state whether the answer appears to be clear (facts fall clearly on one side), borderline (facts are close or ambiguous), or in flux (the governing rule has recently changed or is subject to pending legal developments).

6. **Apply the borderline / in-flux flag.** For each question, make one of the following findings and explain it:
   - **Clear**: the operative facts, applied to the relevant framework, point strongly in one direction. Note that attorney confirmation is still required before any action is taken.
   - **Borderline**: the facts are close, ambiguous, or disputed; the framework requires judgment calls that may not be clear without further research or attorney analysis. Recommend the more conservative course of action where identifiable, and flag for formal attorney opinion before reliance.
   - **In flux**: the controlling rule has recently changed, is subject to pending regulatory or legislative activity, or has been the subject of conflicting authority. Flag as `[VERIFY: rule may have changed — confirm effective date and current status]`. Do not characterize what the prior or current rule is.

7. **For back-pay or computation questions: identify components only.** If the question involves calculating unpaid wages, back pay, or a similar figure, do not compute any number. Instead:
   - List the components that must be researched and verified before any calculation is performed. These will typically include: the jurisdiction's definition of the compensable pay base `[VERIFY]`, the applicable rate or multiplier `[VERIFY]`, the lookback period `[VERIFY]`, any additional damages, interest, or penalty rules `[VERIFY]`, and any offsets or credits `[VERIFY]`.
   - Flag the entire computation as `[ATTORNEY TO CONFIRM: all inputs must be verified before any figure is calculated]`.
   - State clearly that producing a computed figure without verified inputs is outside the scope of this skill.

8. **Compile attorney verification items.** List every open item that must be resolved before the analysis can be relied upon. Include: jurisdiction confirmation, each rule or criterion flagged `[citation needed]` or `[verify jurisdiction]`, each computation component flagged `[VERIFY]`, the effective date of any rule identified as potentially in flux, and any factual gaps or ambiguities in the operative facts.

9. **Assemble the output.** Label the complete output as a draft for attorney review and structure it using the Output Format below.

## Output Format

Deliver the output as a labeled draft, headed **DRAFT — ATTORNEY REVIEW REQUIRED. NOT LEGAL ADVICE.**, with the following sections:

1. **Question Analyzed** — restate the specific wage-and-hour question in precise, unambiguous terms.
2. **Jurisdiction** — state the confirmed jurisdiction(s), or flag `[CONFIRM: governing jurisdiction]`. For multi-jurisdiction situations, flag the need to identify the most-restrictive jurisdiction through verified research.
3. **Operative Facts** — summarize the facts as provided: job title, actual duties, compensation structure, schedule, and the events giving rise to the question. Note any factual gaps or ambiguities.
4. **Assumptions** — list any assumption made where a fact was unclear; flag each `[CONFIRM: ...]`.
5. **Controlling Legal Framework** — identify the category of rule that governs the question. Flag every specific threshold, criterion, multiplier, formula, or deadline `[VERIFY]` / `[citation needed]` / `[verify jurisdiction]`. Do not state any rule from memory.
6. **Application to Facts** — apply the identified framework to the operative facts, element by element. Use `[VERIFY: applicable threshold/criterion]` placeholders in place of any specific rule content not yet verified.
7. **Assessment** — state whether the answer is Clear, Borderline, or In Flux, with a brief explanation. For borderline answers, identify the more conservative course of action. For in-flux rules, flag `[VERIFY: rule may have changed — confirm effective date and current status]`.
8. **Computation Components** (if applicable) — if the question involves a wage or back-pay calculation, list each component that must be researched and verified before any number is calculated; flag each `[VERIFY]`. Do not compute any figure.
9. **Attorney Verification Items** — every open item requiring attorney or verified-research confirmation before this analysis can be relied upon.

## Attorney Verification Checklist

- [ ] The specific question as restated accurately reflects the matter to be analyzed.
- [ ] The governing jurisdiction has been confirmed, and the correct jurisdiction's rules will govern the analysis.
- [ ] For multi-jurisdiction matters: the most-restrictive jurisdiction for each obligation has been identified through current, verified research.
- [ ] Every rule, threshold, criterion, multiplier, and deadline has been verified against current, authoritative sources for the confirmed jurisdiction — none has been accepted from model memory.
- [ ] All citations marked `[citation needed]` have been located, verified, and confirmed as current and in force.
- [ ] Any rule flagged as potentially in flux has been confirmed as to its current status and effective date.
- [ ] The operative facts as summarized are complete, accurate, and not embellished or inferred beyond what the user provided.
- [ ] All assumptions listed in the Assumptions section have been confirmed or corrected.
- [ ] For borderline assessments: the recommended conservative course of action has been evaluated and is appropriate for the client's situation.
- [ ] For computation questions: every component has been verified through current research before any figure is calculated; no number in this output has been relied upon without that verification.
- [ ] No legal conclusion has been communicated to the client without attorney review.
- [ ] Confidentiality and privilege have been preserved in the handling of the output.
- [ ] The attorney has confirmed that this draft is appropriate for the client's specific situation before it is relied upon or acted on.
