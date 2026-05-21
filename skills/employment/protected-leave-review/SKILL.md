---
name: Protected Leave Review
description: Use when organizing and reviewing a protected-leave situation to identify the leave frameworks that may apply, surface procedural obligations and deadlines requiring verified research, and flag adverse-action exposure — producing draft legal work product for attorney review.
---

# Protected Leave Review

## Purpose

Produce a structured, attorney-ready review of an employee's protected-leave situation. The skill organizes the known facts, identifies which leave frameworks may be implicated, surfaces the procedural obligations and entitlement questions that must be researched and confirmed through verified legal authority, identifies how multiple frameworks interact, and — critically — flags adverse-action exposure where a termination, demotion, denial of reinstatement, or discipline is contemplated.

This skill provides decision support and workflow discipline. It does not compute entitlements, calculate deadlines, state rules from background knowledge, or conclude whether any action is lawful. Every entitlement, threshold, and deadline is flagged for verified research. This is draft legal work product for attorney review — not legal advice.

## Use When

- An employer, HR professional, or attorney needs to organize the facts of an employee's leave and identify which protected-leave frameworks may apply.
- A leave situation involves multiple frameworks that may run concurrently or interact (for example, medical leave and disability-accommodation leave arising from the same condition).
- A question arises about what procedural obligations — notices, certifications, designation steps — have been met or remain outstanding.
- An adverse action (termination, demotion, denial of reinstatement, or discipline) affecting an employee who is on, has recently taken, or has requested protected leave is being contemplated, and the employer needs to understand the exposure before proceeding.
- A user asks: "Can we terminate this employee who is on leave?", "What do we owe someone returning from military leave?", "What happens if their leave runs out and they can't come back?", or similar questions about an employee's leave situation.

## Required Inputs

- **The leave situation**: the type or types of leave at issue (e.g., medical, family, military or service-member, disability-related, or a combination). If unclear, describe the underlying reason for the absence.
- **The employee's work schedule and arrangement**: full-time, part-time, or variable hours; whether leave is continuous or intermittent; and, if intermittent, how it has been taken or is anticipated to be taken.
- **Key dates**: the leave start date; the expected or actual return date; any dates on which notices, certifications, or designation decisions were or were not communicated. Flag all dates as `[deadline verification required]` — do not use them to compute deadlines.
- **Procedural status**: whether an eligibility notice has been issued; whether a designation notice has been issued; whether medical or other certification has been requested, received, or found insufficient; whether a cure opportunity has been provided.
- **Jurisdiction(s)**: the jurisdiction(s) in which the employee works. If unknown or in dispute, flag as `[CONFIRM: governing jurisdiction]`.
- **Adverse action contemplated**: whether any termination, demotion, denial of reinstatement, or disciplinary action is under consideration. If yes, describe it and its proposed timing.

If any required input is missing, stop and request it before proceeding. Do not infer jurisdiction from employer headquarters, fabricate leave dates, or assume procedural steps have been completed unless confirmed.

## Do Not Use When

- The user wants leave entitlements, leave balances, or deadlines computed — this skill identifies what must be researched and confirmed; it does not calculate, and AgentCounsel never computes entitlements or deadlines.
- The user wants to draft a designation notice, eligibility notice, or certification request — those are separate drafting tasks.
- The user wants a general assessment of the legal risk of a proposed termination without a leave dimension — use `termination-risk`. Where both apply, use `termination-risk` alongside this skill to address the leave-specific exposure.
- The question is a wage-and-hour question (overtime, exemption, pay rate) — use `wage-hour-qa`.
- The leave at issue has no protected dimension — ordinary employer-granted paid time off, bereavement leave, or jury duty where no protected framework is implicated is outside the scope of this skill.
- The question involves active litigation strategy or responding to a filed administrative charge — that work requires attorney direction from the outset.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review only. This is not legal advice.
- Do not assert any entitlement amount, eligibility threshold, notice period, certification deadline, or measurement period from background knowledge. Every such rule must be confirmed through verified, current legal authority for the governing jurisdiction. Flag each with `[verify jurisdiction]` or `[deadline verification required]`.
- Do not invent facts, procedural history, leave balances, or medical information not provided. Separate facts provided from assumptions and from items requiring attorney confirmation.
- Treat leave exhaustion as a prompt to escalate, not as clearance to act. Do not treat the end of a protected-leave period as automatic permission to terminate or deny reinstatement. Where disability-accommodation frameworks may apply, an interactive process and undue-hardship analysis are required before acting; flag this explicitly.
- Where any adverse action affecting an employee on or returning from protected leave is contemplated, flag interference and retaliation exposure prominently before any other analysis. Escalation to the responsible attorney is required before proceeding with such an action.
- Identify all jurisdictions that may apply and flag multi-jurisdiction complexity for attorney resolution.
- Use `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[citation needed]`, `[verify jurisdiction]`, and `[deadline verification required]` throughout wherever any fact, legal rule, threshold, or procedural step is unverified.
- Preserve confidentiality and privilege. Do not include identifying employee information in reusable template outputs.
- Do not start the adverse-action analysis only after leave has been exhausted. Flag it at the outset if any adverse action is contemplated, and explicitly require attorney review before any such action is taken.

## Workflow

1. **Confirm inputs.** Verify that the required inputs — leave type(s), work schedule and leave pattern, key dates, procedural status, jurisdiction(s), and whether any adverse action is contemplated — are all available. If any are missing, stop and request them before proceeding. Do not fabricate or infer missing information.

2. **Identify potentially applicable leave frameworks.** Based on the facts provided, identify which leave frameworks may be implicated. Consider at minimum: medical or family leave; military or service-member leave; disability-accommodation leave. Note that a single absence or condition may trigger more than one framework simultaneously. For each potentially applicable framework, mark it `[verify jurisdiction]` — do not assert whether it applies or what it requires. Flag any framework whose applicability is unclear as an open question for attorney review.

3. **Surface procedural obligations for each framework.** For each potentially applicable framework, identify the categories of procedural obligation that must be researched and confirmed through verified authority. These include, without limitation:
   - Eligibility requirements and the method of their assessment `[verify jurisdiction]`
   - The eligibility-notice obligation: when it must be issued and what it must contain `[deadline verification required]` `[verify jurisdiction]`
   - The designation-notice obligation: when the employer must designate leave and what the notice must contain `[deadline verification required]` `[verify jurisdiction]`
   - Certification: whether and what type of certification may be required; the timeframe for the employee to provide it; whether a cure or clarification opportunity must be offered before denial `[deadline verification required]` `[verify jurisdiction]`
   - The entitlement amount and its measurement period `[verify jurisdiction]` — do not state a number of weeks, days, or hours from background knowledge
   - Rules governing intermittent or reduced-schedule leave, if applicable `[verify jurisdiction]`
   - Reinstatement obligations: whether the employee is entitled to the same or equivalent position on return, and any exceptions `[verify jurisdiction]`
   - Any applicable employer-size or coverage thresholds `[verify jurisdiction]`

   Do not state any rule, deadline, or threshold from memory. Record only what must be confirmed, not what you believe the rule to be.

4. **Assess procedural status against the framework obligations.** Using the procedural status provided, note which obligations appear to have been met, which appear to be outstanding, and which are unclear or unconfirmed. For each outstanding or unclear obligation, flag it with `[CONFIRM: ...]` and identify it as a verification item. Flag any procedural gap that could independently create exposure — for example, failure to provide a timely eligibility notice or failure to request certification properly.

5. **Identify framework interactions.** Where more than one framework may apply, assess how they interact:
   - Do any frameworks run concurrently by default? `[verify jurisdiction]`
   - Are any frameworks consecutive, and if so, what governs the sequence and total leave duration? `[verify jurisdiction]`
   - Does the employer have an obligation to designate leave under one framework even if the employee did not invoke it by name? `[verify jurisdiction]`
   - Where multiple frameworks apply, which employer-obligation set governs when they conflict? `[verify jurisdiction]`
   Flag all interaction questions for attorney analysis. Do not resolve framework-interaction questions from background knowledge.

6. **Adverse-action gate — flag prominently if any adverse action is contemplated.** If the inputs identify that any termination, demotion, denial of reinstatement, or disciplinary action affecting the employee is under consideration, surface this analysis before moving to the output assembly. Address each of the following:

   - **Interference exposure.** Any adverse action taken against an employee because of the exercise or attempted exercise of a protected-leave right may constitute interference with that right. `[verify jurisdiction]` Flag the specific action, its proposed timing relative to the leave, and the potential interference theory for attorney analysis.
   - **Retaliation exposure.** Adverse action that is causally connected to an employee's request for or use of protected leave, or to a complaint about leave rights, may constitute retaliation. Flag timing proximity — including whether the action is proposed while the employee is on leave, immediately on return, or shortly after a leave request. `[verify jurisdiction]`
   - **Leave exhaustion is not clearance.** Do not treat the expiration of a protected-leave period as automatic permission to terminate or otherwise act adversely. Where a disability-accommodation framework may apply — including where the underlying condition is a disability — flag that additional leave as a reasonable accommodation may be required before any adverse action, and that an interactive process must occur. `[ATTORNEY TO CONFIRM: whether interactive process has been conducted and documented]`
   - **Undue-hardship analysis.** Where denial of additional leave as an accommodation is contemplated, flag that an undue-hardship analysis is required. `[ATTORNEY TO CONFIRM: whether a documented undue-hardship analysis has been completed]`
   - **Reinstatement rights.** Flag whether the employee has reinstatement rights under any applicable framework and whether those rights have been extinguished under any exception. `[verify jurisdiction]`
   - **Escalation requirement.** Any adverse action affecting an employee on or returning from protected leave must be reviewed and approved by the responsible attorney before it is taken. Flag this as a hard stop.

   If no adverse action is contemplated, note that and state that this analysis should be revisited if the situation changes.

7. **Compile open items and assumptions.** List all facts that were assumed in the absence of confirmed information. List all legal questions that require verified research before the analysis can be relied upon. Distinguish factual open items from legal open items.

8. **Assemble the output.** Produce the full protected-leave review in the format below. Label the complete output as draft legal work product for attorney review.

## Output Format

Deliver the following sections, clearly labeled:

1. **Situation Summary** — anonymized summary of the key facts: leave type(s), work schedule, leave pattern (continuous or intermittent), key dates (flagged `[deadline verification required]`), jurisdiction (flagged `[verify jurisdiction]` if unconfirmed), and procedural status as described by the user.

2. **Frameworks Potentially Implicated** — for each framework: name it generically (e.g., "medical or family leave," "military or service-member leave," "disability-accommodation leave"); note the facts that suggest it may apply; mark it `[verify jurisdiction]`; and identify any threshold or coverage question that must be confirmed before applicability can be assessed.

3. **Procedural Obligations to Confirm** — organized by framework. For each obligation category (eligibility assessment, notice, designation, certification, entitlement amount and measurement period, intermittent-leave rules, reinstatement), state what must be researched and confirmed. Do not state the rule — state what must be verified. Flag each item `[deadline verification required]` or `[verify jurisdiction]` as applicable.

4. **Framework Interactions** — summary of how the potentially applicable frameworks may interact: concurrency or consecutiveness, total duration questions, designation obligations, and any conflict-of-obligations question. Flag all for attorney analysis.

5. **Adverse-Action Exposure** — present only if any adverse action is contemplated. Set out: the proposed action and its timing; interference exposure; retaliation exposure; whether leave exhaustion has occurred and why it is not clearance; the interactive-process and undue-hardship questions; reinstatement rights and their status; and the hard-stop escalation requirement. Label this section prominently.

6. **Open Items for Attorney Verification** — numbered list of all unresolved factual and legal questions that must be confirmed before the analysis can be relied upon.

7. **Assumptions** — explicit list of facts assumed in the absence of confirmed information.

Use `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and `[deadline verification required]` throughout. Label the complete output: *Draft legal work product for attorney review. Not legal advice.*

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] All leave frameworks potentially applicable to this situation have been identified under the governing jurisdiction's law, including any state, local, or contractual leave rights that supplement federal or national frameworks.
- [ ] Eligibility for each potentially applicable framework has been confirmed through verified, current legal authority — not background knowledge.
- [ ] All entitlement amounts, measurement periods, and eligibility thresholds have been confirmed through verified authority. No number from this review has been treated as an established rule without confirmation.
- [ ] The employer's eligibility-notice obligations, and whether they were timely met, have been confirmed for each applicable framework.
- [ ] The employer's designation-notice obligations, and whether they were timely met, have been confirmed for each applicable framework.
- [ ] Certification requirements — including what may be requested, the employee's timeframe to respond, and any required cure or clarification opportunity — have been confirmed for each applicable framework.
- [ ] Intermittent-leave rules, if applicable, have been confirmed, including how unscheduled absences must be handled and what documentation the employer may require.
- [ ] Reinstatement rights — including any same-position or equivalent-position entitlement and any applicable exceptions — have been confirmed for each framework.
- [ ] All framework-interaction questions (concurrent vs. consecutive leave, total duration, designation obligations) have been resolved under the governing jurisdiction's law.
- [ ] If any adverse action is contemplated: the interference and retaliation exposure analysis has been completed by the responsible attorney, not left to this draft.
- [ ] If any adverse action is contemplated and a disability-accommodation framework may apply: a documented interactive process has been conducted and an undue-hardship analysis has been completed and documented before the action is taken.
- [ ] Leave exhaustion has not been treated as automatic clearance to take any adverse action without the foregoing attorney review.
- [ ] Jurisdiction has been confirmed, including whether multi-state or local leave laws apply in addition to any federal or national framework.
- [ ] No legal conclusion in this document has been relied upon without attorney review and confirmation of the applicable authority.
- [ ] All facts recorded as confirmed have been verified; all assumptions and open items have been resolved or explicitly preserved as open before this work product is acted upon.
