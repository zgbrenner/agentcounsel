---
name: Internal Investigation
description: Use when supporting an attorney-directed internal investigation to track evidentiary coverage, connect evidence to issues, and draft a privileged investigation memorandum and audience-specific summaries as draft work product for attorney review.
---

# Internal Investigation

## Purpose

Provide structured workflow support for an attorney-directed internal investigation. The skill helps track evidentiary coverage as documents and interview notes arrive, surface gaps between gathered evidence and the issues in scope, connect evidence to each issue, and draft a privileged investigation memorandum with audience-specific summaries. All output is draft legal work product for attorney review — not legal advice, not a disciplinary decision, and not a privilege guarantee.

## Use When

- An attorney is directing an internal investigation into employee misconduct, workplace complaints, financial irregularities, executive conduct, or whistleblower allegations and needs a structured framework to organize evidence and draft findings.
- An attorney or HR professional needs to track evidentiary coverage across documents and interview notes and identify what has not yet been gathered.
- A draft investigation memorandum needs to be assembled from gathered facts, organized by issue rather than by witness.
- Audience-specific summaries (HR, leadership/board, outside counsel) need to be drafted from a completed investigation record.
- The user needs a privileged, attorney-ready work product structure for an ongoing or completed investigation.

## Required Inputs

- **Allegation summary**: the nature of the conduct at issue, the individual(s) alleged to have engaged in it (respondent identifier), the individual(s) who reported it (complainant identifier, if applicable), and the relevant timeframe.
- **Investigation type**: HR/workplace conduct, financial irregularity, executive misconduct, whistleblower retaliation, or other. If unclear, describe and flag.
- **Attorney-direction confirmation**: whether a supervising attorney has formally directed the investigation for the purpose of obtaining legal advice. If not confirmed, see the privilege-formation gate in the Workflow.
- **Workforce and organizational context**: whether the workforce is unionized, whether the employer is a public-sector entity, and any other structural facts bearing on applicable rules. If unknown, flag with `[CONFIRM: workforce/organizational context]`.
- **Gathered materials**: documents, communications, policies, and interview notes received to date. These may be provided incrementally as the investigation proceeds.
- **Prior summaries or memos**: any investigation summary, prior draft memo, or interim report already prepared.

If the allegation summary is not provided, stop and request it before proceeding. If attorney-direction status is unconfirmed, apply the privilege-formation gate before labeling any output as privileged. If other inputs are missing, note gaps and flag them as `[CONFIRM: ...]` items rather than proceeding on assumptions.

## Do Not Use When

- The investigation is not attorney-directed and no attorney is involved or being engaged — the privilege foundation is absent. Stop, and advise that counsel should be retained before proceeding with an investigation intended to produce privileged work product.
- The user wants interviews conducted or wants to generate interview questions for use in a live investigatory interview. This skill does not conduct interviews. Interview preparation, witness rights, and the conduct of investigatory interviews require attorney oversight and jurisdiction-specific analysis outside the scope of this skill.
- The user wants the disciplinary decision made or wants a recommendation on the level of discipline to impose. This skill produces factual findings and conclusions for attorney review; disciplinary decisions belong to the employer, informed by counsel.
- The user wants to assess the legal risk of a specific proposed termination following a completed investigation (use `termination-risk`).
- The underlying matter involves active litigation or regulatory proceedings where separate privilege and work-product rules may govern. Escalate to litigation counsel.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- All output is draft legal work product for attorney review and sign-off. This is not legal advice.
- Do not assert privilege. Privilege depends on how the investigation is structured, who directed it, for what purpose, and applicable jurisdiction-specific doctrine — not on labeling. The skill surfaces the privilege-formation question and flags it; it does not guarantee or confirm privilege.
- Do not invent facts, dates, quotations, witness statements, policy language, citations, or legal authority. If something is not in the provided materials, say so and flag it as a gap.
- Separate what the materials show (facts), what is assumed or inferred (assumptions), what requires further gathering (coverage gaps), what requires legal analysis (legal questions), and what requires attorney judgment (attorney items). Label each category in the output.
- Do not make credibility determinations. Surfaces conflicts in the evidence and flag them for attorney assessment. Where a credibility call is unavoidable for the investigation's conclusions, frame it as a question for attorney judgment, not a finding.
- Do not name, apply, or incorporate any specific statute, regulation, case name, or named legal doctrine as authority. Describe applicable legal frameworks generically and mark them `[verify jurisdiction]`.
- In some jurisdictions and workplace contexts, employees have rights — including representation rights or use-immunity protections — in connection with investigatory interviews. The applicable rules must be researched before any interview is conducted. `[verify jurisdiction]` This skill does not conduct interviews and does not issue investigatory-interview advisements.
- Distribution of any summary or memorandum beyond the privilege circle can waive privilege over the entire investigation. Flag this risk at every summary output and require attorney authorization for distribution decisions.
- Preserve confidentiality and privilege. Keep client-sensitive facts out of reusable template files; populate only matter-specific instances.
- Flag every point of uncertainty with the appropriate placeholder rather than resolving it silently.

## Workflow

1. **Confirm inputs.** Verify that the allegation summary and attorney-direction status are present. If the allegation summary is missing, stop and request it. For any other missing inputs, note the gap and proceed with explicit `[CONFIRM: ...]` flags rather than assumptions.

2. **Apply the privilege-formation gate.** Before labeling any output "Privileged & Confidential — Attorney Work Product," confirm that a supervising attorney has formally directed the investigation for the purpose of obtaining legal advice, and that the investigation's structure supports a privilege claim under the applicable jurisdiction's doctrine. `[verify jurisdiction]`

   - If the investigation is genuinely attorney-directed: note this in the output header and apply the work-product designation.
   - If the investigation is HR-led with legal in an advisory role only: the privilege analysis is materially different. Do not apply the work-product label without attorney confirmation. Flag as `[ATTORNEY TO CONFIRM: privilege basis and labeling]`.
   - If attorney-direction is unconfirmed or unclear: stop, flag the issue, and request confirmation before proceeding.

3. **Apply the interview-rights gate.** Before any portion of the output bears on an upcoming interview, note that in some jurisdictions and workplace contexts, employees may have representation rights, use-immunity protections, or other procedural rights in connection with an investigatory interview — and that the applicable rules must be researched and confirmed by the supervising attorney before any interview takes place. `[verify jurisdiction]` Record this gate as an open item in the Attorney Verification Checklist.

4. **Scope the issues and source map.** Based on the allegation summary, identify the discrete factual and legal issues the investigation must address. For each issue, identify the categories of sources — documents, communications, policy records, and witnesses — that ought to be covered to address that issue competently. This becomes the evidentiary coverage map.

5. **Record incoming materials and update coverage gaps.** As each document or interview note is provided:
   - Record what it shows (a factual summary, not a legal conclusion).
   - Identify which issue(s) it bears on.
   - Note whether it corroborates or conflicts with other gathered evidence, and identify the specific conflict.
   - Mark each issue's coverage status (covered, partially covered, not yet covered).
   - Update the list of outstanding coverage gaps — sources identified as relevant but not yet gathered.

   Flag coverage gaps as `[VERIFY: source not yet gathered — confirm whether available]`. Do not proceed to a conclusions draft until the supervising attorney has confirmed that coverage is sufficient or has authorized proceeding with identified gaps.

6. **Identify synthesis gaps.** Before drafting findings, cross-check: for every issue in the scope, is there at least one piece of gathered evidence bearing on it? For every piece of gathered evidence, has it been connected to at least one issue? Flag any evidence that has been gathered but not yet connected to an issue, and any issue not yet addressed by any gathered evidence.

7. **Draft the investigation memorandum.** Using `templates/investigation-memo-outline.md` as the structural template:
   - Write factual findings organized by issue, not by witness. For each issue, synthesize all relevant evidence, surface conflicts directly, and note the basis for each finding.
   - Include a credibility assessment only where a witness's credibility is determinative to a factual finding, and frame it as an item for attorney judgment rather than a resolved conclusion.
   - Insert the relevant policy versions in effect at the time of the alleged conduct, marked `[VERIFY: confirm policy version and effective date]`.
   - Draft conclusions and recommendations as items for attorney review, not as final determinations.
   - Populate Appendix A (chronology) and Appendix B (documents reviewed) from the gathered materials.
   - Label the entire document as a draft for attorney review.

8. **Draft audience-specific summaries.** After the investigation memorandum is complete and has received attorney review, prepare:
   - **HR summary**: factual findings and policy conclusions relevant to HR action; exclude privileged legal strategy, outside-counsel communications, and attorney mental impressions.
   - **Leadership/board summary**: executive-level findings and any governance or organizational implications; exclude privileged legal analysis and attorney communications.
   - **Outside-counsel summary**: complete privileged record including legal analysis, strategy considerations, and open evidentiary questions.
   
   Label each summary with its intended audience and its privilege status. Do not generate summaries without attorney authorization for distribution.

9. **Apply the distribution-discipline warning.** At the header of every summary, include a prominent notice: each summary inherits the privilege status of the underlying investigation; distributing it beyond the privilege circle — including to business personnel without a need to know — can waive attorney-client privilege and work-product protection over the entire investigation record. Distribution must be authorized by the supervising attorney. `[ATTORNEY TO CONFIRM: distribution list and privilege waiver risk]`

10. **Assemble the Attorney Verification Checklist.** Compile all open items, unresolved conflicts, coverage gaps, `[CONFIRM: ...]` items, `[VERIFY: ...]` items, and `[ATTORNEY TO CONFIRM: ...]` items into the checklist at the end of the memo. No finding should be marked final until every checklist item is resolved.

## Output Format

Deliver a labeled draft package with the following components, each clearly identified:

1. **Investigation Memorandum** — structured per `templates/investigation-memo-outline.md`, organized by issue, labeled "DRAFT — For Attorney Review."
2. **Evidentiary Coverage Map** — a table listing each issue, the sources intended to address it, the sources gathered, and any coverage gaps outstanding.
3. **Audience-Specific Summaries** — HR summary, leadership/board summary, and outside-counsel summary, each labeled with audience and privilege status. Include the distribution-discipline warning on each.
4. **Attorney Verification Checklist** — all open items compiled from across the investigation record.

Each component must begin with a clear label identifying it as draft legal work product for attorney review.

## Attorney Verification Checklist

- [ ] The investigation was formally directed by an attorney for the purpose of obtaining legal advice, and the privilege basis has been confirmed for the applicable jurisdiction. `[verify jurisdiction]`
- [ ] The privilege label (or absence of one) on each document has been reviewed and approved by the supervising attorney.
- [ ] All applicable interview-rights rules for the relevant jurisdiction and workforce context have been researched and confirmed before any investigatory interview was or will be conducted. `[verify jurisdiction]`
- [ ] The evidentiary coverage map has been reviewed and all coverage gaps are either resolved or expressly accepted as investigated-but-not-gathered.
- [ ] All synthesis gaps — gathered evidence not connected to an issue, and issues not addressed by any gathered evidence — have been reviewed.
- [ ] Factual findings are organized by issue; no findings are attributed to a single witness without corroboration or an explicit conflict note.
- [ ] Conflicts in the evidence are surfaced in the memo and not silently resolved.
- [ ] Credibility assessments, where included, are limited to determinative witnesses and are framed as items for attorney judgment.
- [ ] Policy versions cited in the memo are confirmed as the versions in effect at the time of the alleged conduct. `[VERIFY: policy version and effective date]`
- [ ] No legal authority — statute, regulation, case, or named doctrine — has been asserted without verification by the supervising attorney. `[citation needed]`
- [ ] The investigation's scope was adequate to address all identified issues; any limitations in methodology are disclosed in the memo.
- [ ] Conclusions and recommendations have been reviewed by the supervising attorney before the memo is finalized or distributed.
- [ ] Distribution of the memorandum and each summary has been authorized by the supervising attorney, and the distribution list has been confirmed as within the privilege circle.
- [ ] No client-sensitive identifying information has been placed in reusable template files.
- [ ] All `[CONFIRM: ...]`, `[VERIFY: ...]`, and `[ATTORNEY TO CONFIRM: ...]` placeholders in the output have been resolved before the work product is relied upon.
- [ ] Relevant deadlines — including any statutes of limitations, regulatory filing windows, or board-reporting obligations — have been identified and verified. `[deadline verification required]`
