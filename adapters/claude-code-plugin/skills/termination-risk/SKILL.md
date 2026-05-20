---
name: Termination Risk
description: Use when organizing and reviewing the facts surrounding a proposed employee termination so an attorney can assess legal risk before the termination occurs.
---

# Termination Risk

## Purpose

Produce a structured, attorney-ready fact-and-risk summary for a proposed employee termination. The skill organizes available facts, surfaces risk factors, and generates a checklist for attorney review. It does NOT decide whether the termination is lawful, evaluate jurisdiction-specific statutes, or substitute for employment counsel. This is draft legal work product — not legal advice.

## Use When

- A manager or HR professional is preparing to terminate an employee and wants to surface legal risk factors before proceeding.
- An attorney needs a structured intake of termination facts to begin their risk assessment.
- A user says "we want to let someone go — what should we be thinking about?" or "help me think through the risk of this termination."
- A separation is being planned in the context of a reduction in force, performance management conclusion, or misconduct investigation.
- The user needs to organize documentation in advance of a termination meeting.

## Required Inputs

- **Employee identifier**: a role description or anonymized identifier. Do not use the employee's real name in reusable templates.
- **Employment status**: at-will, fixed-term contract, collective bargaining agreement, or unknown. If unknown, flag for attorney confirmation.
- **Stated reason for termination**: the specific reason the employer intends to assert (e.g., performance, misconduct, position elimination, restructuring).
- **Documentation history**: what written documentation exists — performance improvement plans, written warnings, investigation reports, or records showing the business reason.
- **Tenure and role**: length of employment, job title or level, and reporting structure.

If any required input is missing, stop and request it before proceeding. Do not fabricate facts, documentation status, or employment terms.

## Do Not Use When

- The termination has already occurred and the question is how to respond to a claim or charge (use `termination-response` or a litigation-support skill instead).
- The user is asking to draft the termination letter itself rather than assess risk (a separate drafting skill applies).
- The question concerns an independent contractor, not an employee (employment classification is a separate, threshold question requiring attorney guidance).
- The user needs jurisdiction-specific legal conclusions about lawfulness — this skill provides workflow discipline, not legal opinions.

## Legal Safety Rules

- Produce draft legal work product for attorney review only. This is not legal advice.
- Do not assert what is or is not lawful in any jurisdiction. Employment law is highly jurisdiction-specific and fact-specific.
- Do not invent facts, documentation, statutory deadlines, notice requirements, final-pay rules, or protected-class definitions.
- Separate facts provided by the user from assumptions and from items requiring attorney verification. Label each category clearly.
- Flag every potential risk factor — including protected characteristics, timing concerns, and comparator issues — as items for attorney assessment. Never conclude whether a risk factor is legally significant.
- Use `[CONFIRM: ...]` placeholders wherever governing law, employment status, jurisdiction, or factual basis is uncertain.
- Do not place client-sensitive identifying information into reusable template files.
- Treat the user's documents as the primary source. Background knowledge about employment law is unverified unless supported by provided or researched authority.
- Timing of the termination relative to protected activity, leave, complaints, or benefit vesting is a legal question — flag it; do not resolve it.

## Workflow

1. **Confirm inputs.** Verify that the required inputs (employee identifier, employment status, stated reason, documentation history, tenure and role) are available. If any are missing, stop and request them before proceeding.

2. **Identify employment status and governing framework.** Record whether the employment is at-will, under a written contract, or subject to a collective bargaining agreement. If unknown, mark `[CONFIRM: employment status]`. Note whether any implied-contract issues arise from handbook language (flag for attorney).

3. **Document the stated business reason.** Record the employer's articulated reason precisely as stated. Assess whether written documentation exists to support that reason. Note gaps between the stated reason and the documentation record.

4. **Identify protected activity and leave.** Review the timeline for: recent complaints of discrimination or harassment by the employee; requests for or use of medical, family, or other protected leave; workers' compensation claims; whistleblower reports; union activity; or any other legally protected activity. Flag the proximity of any such activity to the proposed termination date. Do not conclude on legal significance — flag for attorney.

5. **Identify membership in or proximity to protected categories.** Note any known or apparent protected characteristics (e.g., age, race, sex, disability, national origin, religion, pregnancy status). Do not draw conclusions about discrimination. Flag every characteristic present for attorney review.

6. **Identify comparators.** Ask whether other employees in similar roles, with similar conduct or performance, were treated differently. Note any comparators treated more favorably. Flag for attorney assessment of disparate treatment risk.

7. **Assess timing concerns.** Note the relationship between the termination date and: vesting events (stock, pension, bonus); end of performance improvement plan periods; conclusion of investigations; medical certification deadlines; contract renewal or notice periods; or any other timing factor provided. Flag all timing issues for attorney review.

8. **Review process and notice.** Assess whether the employer followed its own disciplinary or termination procedures (progressive discipline, investigation requirements, approvals). Note any procedural gaps. Identify whether advance notice of termination or pay-in-lieu may apply — flag as `[CONFIRM: notice and final pay requirements]`.

9. **Identify severance and release considerations.** Note whether severance is being offered and whether a release of claims is contemplated. Flag consideration-period and revocation-period requirements as attorney-verification items, noting that these requirements vary by jurisdiction and by the age and number of employees being released. Do not assert specific statutory timeframes.

10. **Review communications plan.** Note the proposed internal announcement and reference policy. Flag any statements about the reason for departure that could create evidentiary issues.

11. **Populate the checklist template.** Complete the `templates/termination-risk-checklist.md` template with the gathered facts and flagged items.

12. **Assemble the output.** Produce: (1) Fact Summary, (2) Risk Factor Summary, (3) Completed checklist referencing the template, (4) Open Items for attorney verification, (5) Stated assumptions. Label the entire output as a draft for attorney review.

## Output Format

Deliver the following sections, clearly labeled:

1. **Fact Summary** — anonymized summary of the key facts organized by input category.
2. **Risk Factor Summary** — plain-language description of each flagged risk factor, labeled as "identified for attorney review" rather than as a legal conclusion.
3. **Termination Risk Checklist** — completed instance of `templates/termination-risk-checklist.md`, with checkboxes marked and notes populated.
4. **Open Items for Attorney Verification** — numbered list of unresolved questions requiring legal confirmation.
5. **Assumptions** — explicit list of any facts assumed in the absence of confirmed information.

Use `[CONFIRM: ...]` throughout wherever any fact, legal requirement, or procedural step is unverified. Label the complete output: *Draft legal work product for attorney review. Not legal advice.*

## Attorney Verification Checklist

- [ ] Employment status (at-will, contract, union) has been confirmed and governing documents reviewed.
- [ ] The stated business reason is accurate, consistent with prior communications, and supported by contemporaneous documentation.
- [ ] All documentation relied upon has been reviewed in its original form and confirmed to be complete.
- [ ] The timeline of protected activity, leave, and complaints has been reviewed for retaliation risk.
- [ ] Protected characteristics of the affected employee and comparator employees have been assessed under applicable anti-discrimination law.
- [ ] Comparator analysis is complete: similarly situated employees with similar conduct have been identified and their treatment confirmed.
- [ ] Timing of termination relative to vesting events, investigations, leave, or complaints has been reviewed.
- [ ] All employer-required procedures (progressive discipline, investigation, approvals) have been followed or deviations documented.
- [ ] Jurisdiction-specific final pay, notice, and WARN Act (or equivalent) requirements have been confirmed.
- [ ] Severance and release terms, including any required consideration and revocation periods, have been reviewed under applicable law.
- [ ] The communications plan and reference policy have been reviewed for evidentiary and reputational risk.
- [ ] No legal conclusions in this document have been relied upon without attorney review and confirmation.
