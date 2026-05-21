---
name: Risk Assessment
description: "Use when applying a structured, jurisdiction-agnostic method to identify, rate, and prioritize legal risks in a situation, producing a risk register with severity bands and a prioritized summary for attorney review."
practice_area: legal-methodology
task_type: analysis
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The situation to be assessed"
  - "The known facts"
  - "The client's posture and objectives"
outputs:
  - "Prioritized risk register with severity bands and a summary for attorney review"
related_skills:
  - skills/legal-research/legal-research-memo/SKILL.md
  - skills/contracts/nda-review/SKILL.md
  - skills/legal-methodology/statutory-interpretation/SKILL.md
tags:
  - legal-methodology
  - risk-assessment
  - risk-register
  - prioritization
---

# Risk Assessment

## Purpose

Apply a structured, jurisdiction-agnostic method for identifying, rating, and prioritizing legal risk across a situation, transaction, document, or matter. The skill guides systematic decomposition of the situation into discrete risks; for each risk, it rates likelihood and impact, assigns a severity band, and separates legal risk from business and operational impact. The output is a prioritized risk register — a structured reference that enables a supervising attorney to focus attention, allocate resources, and make informed judgments.

All ratings produced by this skill are preliminary triage signals for attorney judgment. They are not predictions of litigation outcome, not legal conclusions, and not legal advice. The skill does not assess the enforceability of any right, the validity of any claim, or the probability of any legal result. Those determinations belong to the supervising attorney.

## Use When

- A user asks to "assess the risks," "identify the legal exposure," "flag the issues," or "map the risk" in a transaction, document, agreement, matter, or situation.
- An attorney or legal team needs a structured first-pass risk inventory before deciding how to proceed.
- Multiple risk areas are potentially in play and need to be organized, compared, and prioritized for attorney attention.
- A preliminary risk picture is needed to support a business or internal decision, with the explicit understanding that attorney review is required before reliance.
- A matter intake, contract review, or legal research memo has been completed and the next step is organizing identified issues into a risk register for the responsible attorney.
- Recurring risk-assessment needs (portfolio management, transaction screening, compliance review) call for a repeatable, structured methodology.

## Required Inputs

- A description of the situation, transaction, document, or matter to be assessed. The more specific the input, the more targeted the risk identification.
- The client's role and posture: who the client is, what position they occupy, and what they are trying to achieve or protect.
- The practice area or subject-matter scope of the assessment — specifying whether the assessment is limited to, for example, contract risk, regulatory exposure, employment risk, or all legal risk.
- Optional but recommended: the jurisdiction and governing law. If not provided, all jurisdiction-specific risk characterizations must carry `[verify jurisdiction]`.
- Optional: any documents, provisions, facts, or prior work product bearing on the risks — for example, a contract reviewed under `nda-review`, an intake summary, or a prior legal research memo. These are incorporated as inputs, not verified independently by this skill.
- Optional: any known risk tolerance, materiality threshold, or risk-management policy the client applies.

If the client's role and a description of the situation are not provided, stop and request them. Do not assume the client's position, fabricate facts, or populate a risk register from hypothetical scenarios.

## Do Not Use When

- The user needs a specific legal analysis rather than a structured risk inventory — use the appropriate substantive skill (for example, `legal-research-memo`, `nda-review`, `statutory-interpretation`).
- The user is asking for a legal opinion or a final judgment about whether a risk will materialize — this skill produces a preliminary triage register, not a prediction or legal opinion.
- The situation involves only a single, well-defined legal question with no competing risk dimensions — a targeted analysis skill is more appropriate.
- The user needs only a business risk or financial risk assessment without a legal dimension — this skill covers legal risk and its interaction with business impact, not standalone business analysis.
- The assessment would require reaching legal conclusions about enforceability, liability, or outcome in a specific jurisdiction that have not been researched — flag those as verification items and route to a research skill.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- All risk ratings — likelihood, impact, and severity bands — are preliminary triage signals for attorney judgment. They are not predictions of outcome, not legal conclusions, and not assessments of enforceability. Label every rating explicitly with `[ATTORNEY TO CONFIRM: preliminary triage signal — not a legal conclusion]`.
- Do not assert the existence or content of any statute, regulation, case, or named legal doctrine. If a legal basis for a risk is relevant, describe the risk in functional terms and mark the legal underpinning as a research and verification item.
- Do not invent, compute, or assert deadlines, limitations periods, or notice periods. Mark every time-sensitive risk item with `[deadline verification required]`.
- Do not resolve jurisdiction gaps — flag every jurisdiction-specific risk characterization with `[verify jurisdiction]`.
- Separate legal risk from business and operational impact. Do not blend legal exposure into a business recommendation. Strategy and business judgment belong to the attorney and client.
- Do not state that a risk is eliminated, waived, or unenforceable unless the user has provided a specific, verified source for that proposition. Mark such conclusions as `[ATTORNEY TO CONFIRM: enforceability / waiver — verify jurisdiction]`.
- Preserve confidentiality and privilege: the risk register is attorney work product. Do not place client-sensitive facts into reusable templates.

## Workflow

1. **Confirm inputs.** Verify that you have a description of the situation, the client's role, and the scope of the assessment. If inputs are incomplete, request them before proceeding. Record any scoping limitation as an assumption.

2. **Define the assessment scope.** Confirm and record the practice area(s) covered, the factual perimeter of the assessment (what is included and what is not), and any exclusions the user has specified. Record the jurisdiction if provided; otherwise record `[verify jurisdiction]` as a global flag.

3. **Decompose the situation into risk domains.** Organize the situation into discrete risk domains relevant to the scope — for example: contractual risk, regulatory or compliance risk, litigation exposure, intellectual property risk, employment and labor risk, data and privacy risk, corporate and governance risk, tax risk, cross-border risk, and any other domain the facts raise. List only the domains that are potentially implicated; do not pad the register with domains that have no factual basis.

4. **Identify discrete risks within each domain.** For each domain, identify the specific, discrete risks the situation presents. State each risk as a concrete, addressable legal exposure — not a broad category. A risk statement follows the form: "Risk that [specific event or claim] arises because [factual basis], resulting in [potential legal consequence]." If the factual basis is uncertain, mark it with `[CONFIRM: factual basis]`.

5. **Rate each risk.** For each discrete risk, assign preliminary ratings using only the information provided:

   - **Likelihood** — the relative probability that the risk materializes, on a three-point scale:
     - **High** — materially likely given the facts as described.
     - **Medium** — possible but not clearly indicated by the facts as described.
     - **Low** — unlikely given the facts as described, but not excluded.

   - **Impact** — the severity of the legal consequence if the risk materializes, on a three-point scale:
     - **High** — significant legal exposure: potential for major liability, injunctive relief, license loss, regulatory sanction, material contract breach, or comparable consequence.
     - **Medium** — moderate legal exposure: potential for a claim, dispute, or sanction with manageable consequences if addressed.
     - **Low** — minor legal exposure: technical issue, administrative correction, or low-stakes dispute.

   - **Severity band** — the combined triage signal:
     - **Critical** — High Likelihood + High Impact.
     - **Elevated** — High Likelihood + Medium Impact, or Medium Likelihood + High Impact.
     - **Moderate** — Medium Likelihood + Medium Impact, or High Likelihood + Low Impact, or Low Likelihood + High Impact.
     - **Watch** — Low Likelihood + Medium Impact, or Medium Likelihood + Low Impact.
     - **Informational** — Low Likelihood + Low Impact.

   Tag every rating: `[ATTORNEY TO CONFIRM: preliminary triage signal — not a legal conclusion]`.

6. **Separate legal risk from business and operational impact.** For each risk, record:
   - The legal exposure (the legal basis for the risk, stated functionally without asserting jurisdiction-specific authority).
   - The business or operational impact (what the risk means practically for the client's operations, relationships, or finances — separately stated).
   - Whether the legal risk and the business impact are congruent or diverge (for example, a low-probability legal risk with catastrophic business impact if it materializes).

7. **Identify interdependencies and compounding risks.** Note where two or more risks interact: where the materialization of one risk raises the likelihood or impact of another, where a single factual trigger affects multiple risk domains, or where risks share a common root cause that, if addressed, would reduce multiple risks simultaneously.

8. **Identify time-sensitive risks.** Flag any risk that depends on a deadline, notice period, limitations period, or other time-sensitive trigger. Mark each as `[deadline verification required]` and route for immediate attorney attention. Do not compute or assert the deadline.

9. **Build the risk register.** Compile all identified risks into the risk register table described in the Output Format section. Order by severity band from Critical to Informational.

10. **Draft the prioritized summary.** Summarize the top risks in priority order, with a plain-language explanation of what each is, why it ranks where it does, and what the key attorney action is.

11. **List attorney verification items.** Enumerate every point that requires attorney research, jurisdiction-specific legal analysis, factual confirmation, or professional judgment — including every jurisdiction-specific risk characterization and every asserted legal basis that has not been independently researched.

12. **Assemble the risk register** using the output format below. Label it as a draft for attorney review.

## Output Format

Deliver a Risk Assessment Register with the following sections:

1. **Register Header** — Client role; situation description (brief); assessment scope and practice areas covered; jurisdiction (or `[verify jurisdiction]`); date; privilege designation.
2. **Scope and Limitations** — What is included, what is excluded, any assumptions about scope.
3. **Risk Register Table** — One row per discrete risk:

   | # | Domain | Risk Statement | Likelihood | Impact | Severity | Legal Exposure | Business/Operational Impact | Key Action | Notes / Flags |
   |---|--------|---------------|------------|--------|----------|----------------|----------------------------|------------|---------------|

   Every Likelihood, Impact, and Severity entry carries the tag: `[ATTORNEY TO CONFIRM: preliminary triage signal — not a legal conclusion]`.

4. **Prioritized Summary** — Top risks in priority order (Critical and Elevated first), with a plain-language explanation of each risk and the key attorney action recommended.
5. **Time-Sensitive Items** — A separate list of all risks flagged `[deadline verification required]`, for immediate attorney attention.
6. **Interdependencies and Compounding Risks** — A note on any risk clusters or compounding relationships identified.
7. **Assumptions** — Every assumption made in the assessment, explicitly listed.
8. **Attorney Verification Items** — A checklist of all jurisdiction-specific points, unresearched legal bases, factual gaps, and judgment calls requiring attorney confirmation.

Use `[CONFIRM: ...]` for every factual gap. Use `[verify jurisdiction]` at every jurisdiction-specific point. Use `[deadline verification required]` for every time-sensitive item. Use `[ATTORNEY TO CONFIRM: ...]` for every rating and legal-exposure characterization.

## Attorney Verification Checklist

- [ ] All identified risk domains are appropriate given the client's situation, role, and the scope confirmed with the attorney.
- [ ] Every risk statement is grounded in the facts provided; no risk has been fabricated or padded.
- [ ] Every Likelihood, Impact, and Severity rating has been reviewed; ratings reflect attorney judgment, not triage signals alone.
- [ ] Every jurisdiction-specific risk characterization has been verified for the applicable jurisdiction `[verify jurisdiction]`.
- [ ] Every legal basis for a risk has been independently researched and confirmed; no legal basis is asserted solely from model background knowledge.
- [ ] Every time-sensitive item has been reviewed; actual deadlines, limitations periods, and notice periods have been confirmed by the attorney `[deadline verification required]`.
- [ ] Legal risk and business impact are correctly separated; no legal conclusion is embedded in the business impact description.
- [ ] All interdependencies and compounding risks have been reviewed for accuracy.
- [ ] The risk register does not assert enforceability, validity, or outcome without verified legal basis.
- [ ] All assumptions are confirmed or corrected.
- [ ] All `[CONFIRM: ...]` placeholders are resolved before the register is relied upon.
- [ ] The register is appropriately labeled as draft legal work product for attorney review, not legal advice.
- [ ] Privilege and confidentiality of the register are protected; distribution is limited to authorized recipients.
