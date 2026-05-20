---
name: Worker Classification
description: Use when organizing the facts of a proposed worker engagement and structuring an analysis of whether the worker should be classified as an employee or an independent contractor, producing a draft classification analysis memo for attorney review.
---

# Worker Classification

## Purpose

Produce a structured, attorney-ready classification analysis memo for a **proposed** worker engagement — one that has not yet started. The skill gathers and organizes the factual inputs that bear on worker classification, identifies the test or tests that apply in the governing jurisdiction for the relevant legal purpose, applies those tests to the facts in a structured factor table, and flags gaps between the intended arrangement and what the facts support. It produces draft legal work product for attorney review — not legal advice, not a legal conclusion on the lawfulness of any classification, and not a substitute for employment counsel.

## Use When

- A company or HR professional is planning a new engagement with an individual worker and needs to think through whether the arrangement is supportable as an independent contractor relationship.
- An attorney needs a structured intake of engagement facts to begin a classification risk assessment before work begins.
- A user asks "can we bring this person on as a contractor?" or "what factors should we look at before we classify this engagement?"
- A proposed arrangement involves a staffing agency, vendor SOW, or direct contractor agreement, and classification risk has not yet been assessed.
- The user needs to compare the intended contract structure against the operational facts before the engagement is executed.

## Required Inputs

- **Description of the work**: what the worker will do, day to day; whether the work is core to the company's business or peripheral; whether the engagement is project-based or indefinite in duration; and the level of specialization or skill required.
- **Control facts**: whether the company will set the worker's hours or schedule; whether the work will be performed on company premises; who will direct the method and sequence of work; whether the company will have supervisory authority over the worker.
- **Economic facts**: how the worker will be paid (flat fee, hourly, milestone, retainer); who will provide tools, equipment, and materials; whether the worker has or will have other clients during the engagement; and whether the worker bears any risk of profit or loss on the engagement.
- **Arrangement structure**: whether this is a direct independent contractor agreement, a staffing-agency placement, or a vendor SOW; proposed duration; and whether the worker will be physically co-located with employees.
- **Classification purpose(s)**: the legal purpose(s) for which classification matters (e.g., income tax withholding, wage-and-hour obligations, unemployment insurance, benefits eligibility, workers' compensation coverage). Different purposes may trigger different tests under the governing jurisdiction's law.
- **Jurisdiction**: the state, province, or country whose law will govern the engagement. If unknown, flag as `[CONFIRM: governing jurisdiction]`.

If any required input is missing, stop and request it before proceeding. Do not fabricate facts, assumed durations, assumed pay structures, or inferred control arrangements.

## Do Not Use When

- The engagement has **already started** — retroactive reclassification risk analysis is a distinct, attorney-directed task that this skill does not perform. Stop, and direct the user to employment counsel for a retroactive analysis.
- The user wants the independent contractor agreement or SOW drafted (use a contract-drafting skill).
- The user is asking for a jurisdiction-specific legal conclusion on whether a particular classification is lawful — that determination requires attorney review.
- The user needs back-pay, penalty, or tax-liability estimation for a prior misclassification — those calculations require attorney-directed analysis outside the scope of this skill.
- The engagement concerns an existing employee being converted to contractor status; conversion analysis may involve additional legal considerations that require attorney judgment from the outset.

## Legal Safety Rules

- Produce draft legal work product for attorney review only. This is not legal advice.
- This skill is **prospective only**. If the engagement has already started, stop immediately and do not proceed. Retroactive reclassification risk analysis is a separate attorney-led matter.
- Do not assert, from memory, what the applicable classification test is in any jurisdiction. Tests, factors, and any statutory or regulatory carve-outs must be researched and verified by the attorney. Treat all background knowledge about classification standards as `[verify jurisdiction]` until confirmed by research.
- Do not invent facts, payment terms, control arrangements, or inferred business relationships not provided by the user.
- Do not invent or assert citations, statutes, regulations, agency guidance, or case names. Use `[citation needed]` wherever legal authority would be referenced.
- Separate facts, assumptions, analysis, and attorney-verification items. Label each category clearly.
- Identify the governing jurisdiction and the classification purpose(s); if either is unknown, flag with `[CONFIRM: ...]` and do not proceed past fact-gathering without them.
- Preserve confidentiality and privilege; do not place client-identifying details into reusable templates.
- Flag every point of uncertainty rather than resolving it silently. Where a factor could reasonably support either classification, note it as contested and flag for attorney assessment.
- Do not conclude that a proposed arrangement is legally permissible or impermissible. Provide analysis structure; leave the legal conclusion to the attorney.

## Workflow

1. **Prospective-only gate.** Before gathering any facts, confirm that the engagement has **not yet started**. Ask: "Has the worker already begun performing any work under this arrangement?" If the answer is yes, or if there is any ambiguity, stop. State clearly that this skill covers only prospective engagements; direct the user to employment counsel for retroactive reclassification risk analysis. Do not proceed.

2. **Confirm inputs.** Verify that all required inputs are present: description of the work, control facts, economic facts, arrangement structure, classification purpose(s), and governing jurisdiction. If any input is missing, stop and request it. Do not infer or fabricate missing facts.

3. **Organize and document the facts.** Group the confirmed facts into four categories and present them clearly:
   - **The Work**: tasks, core vs. peripheral, project vs. indefinite, specialization.
   - **Control**: hours, location, method direction, supervisory authority.
   - **Economics**: pay structure, tools, other clients, profit/loss risk, business entity status.
   - **The Arrangement**: contract form (direct IC, agency, SOW), duration, co-location.
   Separate each confirmed fact from any assumption. Label assumptions explicitly.

4. **Identify the applicable test(s).** Based on the governing jurisdiction and the stated classification purpose(s), identify the type of test or tests that apply — noting, for example, whether the purpose implicates a multi-factor common-law test, an economic-realities test, an ABC-style test, or a hybrid. Mark the applicable test as `[verify jurisdiction]` and note that the attorney must confirm the correct test, its current elements, and any statutory or regulatory carve-outs before the analysis is relied upon. Do not name specific statutes, agencies, or case law.

5. **Apply the facts to the test in a factor table.** For each factor or element of the identified test type, apply the gathered facts and assign a directional signal:
   - **Supports Employee**: the fact, as stated, points toward employee classification.
   - **Supports Contractor**: the fact, as stated, points toward independent contractor classification.
   - **Contested / Unclear**: the fact is ambiguous, contested, or missing.
   Flag each "Contested / Unclear" entry for attorney review. Where a factor is not yet determinable from the provided facts, note what additional information is needed.

6. **Run a gap analysis.** Compare the intended arrangement structure (as described and as the contract is expected to read) against what the operational facts actually reflect. Identify any gaps — facts that, if present at engagement time, would undermine the intended classification — and classify each gap as:
   - **High-risk gap**: the fact directly contradicts the intended classification under the identified test type.
   - **Moderate-risk gap**: the fact is ambiguous or creates exposure that the attorney should address.
   - **Low / No gap**: the fact is consistent with the intended classification.
   Produce an overall gap-analysis risk signal (High / Moderate / Low) with a brief plain-language explanation. Do not label this signal as a legal conclusion; it is an indicator for attorney review.

7. **Flag escalation factors.** Identify and call out any of the following, which require heightened attorney attention:
   - The governing jurisdiction is known or suspected to apply a strict classification test (note as `[verify jurisdiction]` — do not name the jurisdiction or test).
   - The work described is core to the company's primary business rather than peripheral.
   - The company will exercise supervisory authority over the worker's method or schedule.
   - The proposed engagement duration is long or indefinite rather than project-specific.
   - Any classification factor is outcome-determinative and presently points toward employee.
   - The company or individual has prior audit, settlement, or enforcement history in the classification area (`[CONFIRM: any prior classification history]`).
   - Multiple classification purposes apply and the tests may yield different results.

8. **List attorney verification items.** Produce a numbered list of the specific questions and confirmations the attorney must resolve before the analysis can be relied upon. These should include: the confirmed governing jurisdiction, the confirmed applicable test(s) for each purpose, any contested factors, all gap items, and any escalation flags.

9. **Assemble the draft memo.** Combine the outputs of the preceding steps into the structured memo described in Output Format. Label the complete output as: *Draft legal work product for attorney review. Not legal advice.*

## Output Format

Deliver the following sections, clearly labeled:

1. **Engagement Summary** — a brief, plain-language description of the proposed arrangement based on the inputs provided.

2. **Fact Record**
   - *Confirmed Facts* — organized into the four categories: The Work / Control / Economics / The Arrangement.
   - *Assumptions* — explicit list of any facts assumed in the absence of confirmed information, each labeled `[CONFIRM: ...]`.

3. **Applicable Test(s)** — identification of the type(s) of classification test that apply for each stated purpose in the governing jurisdiction, marked `[verify jurisdiction]`, with a note that the attorney must confirm the correct test and its current elements before reliance.

4. **Factor Application Table** — a table with columns: Factor | Relevant Facts | Signal (Supports Employee / Supports Contractor / Contested) | Notes for Attorney. One row per factor of the identified test type.

5. **Gap Analysis** — a comparison of the intended arrangement structure against the operational facts, with each gap rated High / Moderate / Low and an overall risk signal. Include a plain-language explanation. Label this section: *Indicator for attorney review — not a legal conclusion.*

6. **Escalation Flags** — a bulleted list of any escalation factors identified, each explained in one or two sentences.

7. **Attorney Verification Items** — a numbered list of the questions and confirmations the attorney must resolve before the analysis is relied upon.

8. **Assumptions** — a consolidated list of all assumptions made throughout the memo, each paired with the corresponding `[CONFIRM: ...]` placeholder.

Use `[CONFIRM: ...]` wherever any fact, legal requirement, or jurisdictional rule is unverified. Use `[VERIFY: ...]` for factual matters to be checked. Use `[ATTORNEY TO CONFIRM: ...]` for points of legal judgment. Use `[verify jurisdiction]` for any classification standard, test, or authority requiring jurisdictional confirmation. Use `[deadline verification required]` for any date or timing item. Label the complete output: *Draft legal work product for attorney review. Not legal advice.*

## Attorney Verification Checklist

- [ ] The engagement has been confirmed as prospective — no work has begun under the arrangement being analyzed.
- [ ] The governing jurisdiction has been confirmed, including any choice-of-law or multi-jurisdiction exposure.
- [ ] The correct classification test(s) for each stated legal purpose (tax, wage-and-hour, unemployment, benefits, workers' compensation, etc.) have been identified and verified through current research, not memory.
- [ ] Any statutory or regulatory carve-outs, safe harbors, or per se categories applicable in the governing jurisdiction have been identified and assessed.
- [ ] All facts in the Fact Record have been confirmed by the client; no assumed facts have been treated as established.
- [ ] Each factor in the Factor Application Table has been assessed under the verified test, not under a generic or assumed test.
- [ ] The gap analysis risk signal has been reviewed in light of the verified test and the client's actual risk tolerance and remediation options.
- [ ] All escalation flags have been reviewed and addressed or accepted with informed client consent.
- [ ] Any prior classification audit, settlement, or enforcement history has been disclosed and incorporated into the analysis.
- [ ] If multiple classification purposes apply, the results under each test have been reconciled and any divergences addressed.
- [ ] The intended contract structure (IC agreement, SOW, agency agreement) has been reviewed to confirm it is consistent with the operational facts and the applicable test.
- [ ] No legal authority, citation, statute, or case name asserted in this memo has been relied upon without independent verification.
- [ ] The client has been advised that this document is draft work product, not legal advice, and that the final classification determination requires attorney sign-off.
