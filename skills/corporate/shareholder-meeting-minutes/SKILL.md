---
name: Shareholder Meeting Minutes
description: "Use when drafting minutes of a shareholder or member meeting (annual or special) from user-provided meeting materials — notice, agenda, proxy materials, attendance, and vote tallies — producing a structured draft corporate record for attorney review."
practice_area: corporate
task_type: drafting
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "Meeting details: entity, meeting type (annual or special), date, time, and location or platform"
  - "Notice and proxy record as provided: what was sent, to whom, and when, or waiver information"
  - "Attendance and representation figures as provided, including proxies"
  - "Proposals presented and vote tallies exactly as provided"
outputs:
  - "Draft minutes of the shareholder or member meeting for attorney review"
related_skills:
  - skills/corporate/board-minutes/SKILL.md
  - skills/corporate/written-consent/SKILL.md
tags:
  - corporate
  - governance
  - shareholder-meeting
  - meeting-minutes
  - corporate-records
  - drafting
---

# Shareholder Meeting Minutes

## Purpose

Produce a structured, attorney-ready draft of minutes for a meeting of an entity's shareholders or members — annual or special. The draft records what occurred as reflected in the user-provided meeting materials: the notice and proxy record, attendance and representation as provided, the proposals presented, and the vote tallies as provided. It never reconstructs or infers attendance, quorum, or vote outcomes, and it treats quorum sufficiency and vote-threshold sufficiency as attorney determinations. It produces draft legal work product for attorney review — not legal advice and not an adopted corporate record.

## Use When

- A user asks to "draft the minutes of our annual meeting," "write up the shareholder meeting," or "memorialize the special meeting of members" for a meeting that has already taken place.
- The user has meeting materials — notice, agenda, proxy materials, a meeting script, an inspector of elections report, or vote tabulations — and needs a minutes document prepared for attorney review before adoption.
- A member meeting of an LLC, a membership meeting of a nonprofit, or an equivalent holder-level meeting needs to be memorialized in the same way.
- The user wants a starting draft that conforms to the organization's house format before the attorney finalizes it.

## Required Inputs

- **Meeting identification:** the entity; whether the meeting was annual or special; the date, time, and location or virtual platform.
- **Notice and proxy record as provided:** what notice was given, how, and when (and the record date, if stated), or whether notice was waived — as stated by the user or shown in the materials. Record it; do not assess its sufficiency. `[ATTORNEY TO CONFIRM: notice and record-date compliance]` `[verify jurisdiction]`
- **Attendance and representation as provided:** holders present in person, holders represented by proxy, and the shares, units, or voting power represented — exactly as stated in the materials or by the user. Do not infer, estimate, or reconstruct any figure. Identify the chair, the secretary, and any inspector of elections, as provided.
- **Quorum status as provided:** what the user or the materials state about whether a quorum was represented. Whether that representation satisfies the applicable quorum requirement is an attorney question — `[ATTORNEY TO CONFIRM: quorum sufficiency]`.
- **Proposals and vote tallies as provided:** each item of business as presented, and the vote tallies exactly as recorded in the inspector's report, the tabulation, or the user's statement.
- **Meeting materials:** the notice, agenda, proxy statement or proxy materials, any meeting script, and any inspector of elections report or tabulation.

Optional but recommended:
- A prior set of the organization's shareholder-meeting minutes for house-format reference.
- The practice group's `practice-profiles/corporate.md` if it has been populated and is loaded alongside this skill. If present, the skill uses its Preferred Output Style and Standard Positions tables to benchmark the draft against the group's house style. If absent, the skill proceeds without practice-profile benchmarking and asks the user to supply standing positions inline if needed.

If any required input is missing, stop and request it. Do not fabricate attendance lists, representation figures, vote tallies, quorum determinations, or proposal language.

## Do Not Use When

- The meeting is a board of directors or board-committee meeting — use `board-minutes` instead.
- The holders are acting by written consent in lieu of a meeting — use `written-consent` instead.
- The user is asking whether a quorum was present, whether a proposal passed, or whether a vote satisfied the required threshold — those are legal determinations for the attorney, not a drafting task.
- The task is to draft the meeting notice, proxy materials, or meeting script from scratch — that is a separate drafting task, not a minutes document.
- The meeting has not yet occurred and the user wants a projected record — minutes record only what actually occurred, as provided.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice. An attorney must review, revise, and authorize the finalization and adoption of any minutes before they become a corporate record.
- Record only what the provided materials and the user actually state. **Never reconstruct or infer attendance, share representation, quorum, or vote outcomes.** A tally, figure, or attendee not provided is a placeholder — `[CONFIRM: vote tally for Proposal [N]]` — never an estimate.
- Quorum sufficiency and vote-threshold sufficiency are legal determinations under the entity's governing documents and applicable law. The draft records the reported figures and the chair's announcements as provided; it never states, as its own conclusion, that a quorum requirement was met or that a proposal received the required vote. Flag every such point `[ATTORNEY TO CONFIRM]` `[verify jurisdiction]`.
- Describe statutory meeting formalities — notice periods, record dates, proxy validity, inspector-of-elections requirements, virtual-meeting authorization — generically only, each flagged `[verify jurisdiction]`. Never assert a statute, code section, or day count. Record every date as provided and flag it `[deadline verification required]`.
- Treat model background knowledge about corporate law and meeting procedure as unverified. Do not carry it into the draft as stated authority.
- Distinguish what the meeting materials actually say from what you assume and from what the attorney must confirm. Label assumptions explicitly.
- The draft minutes are attorney work product and should not be circulated as if adopted. The agent does not adopt, finalize, sign, or circulate minutes.
- Preserve confidentiality and privilege. Do not place client-sensitive facts, holder-level personal information, or identifying transaction details into a reusable copy of the draft.
- Flag every uncertainty with a bracketed placeholder (`[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`). Never resolve uncertainty silently.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/corporate.md` is loaded, its Preferred Output Style and Standard Positions inform the draft but never substitute for attorney judgment. The profile is a configuration record approved by the practice group; it is not legal advice and does not override the skill's normal attorney-verification gates. If the profile's standing positions conflict with the matter facts or with what the supervising attorney concludes, the attorney prevails.

## Workflow

1. **Confirm inputs.** Verify that all required inputs are present: meeting identification, the notice and proxy record, attendance and representation as provided, quorum status as provided, and the proposals and vote tallies. If any required input is missing, request it before proceeding. Do not proceed on assumed attendance, representation, or tallies.

2. **Record meeting metadata.** Capture the entity name, meeting type (annual or special), date, time, and location or platform, and the record date as provided `[deadline verification required]`. Note them at the top of the draft.

3. **Record the notice and proxy record as provided.** State how and when notice was given (or that it was waived, and by whom) exactly as the materials or the user state. If proxy materials were distributed, identify them by title and date as provided. Flag sufficiency for the attorney: `[ATTORNEY TO CONFIRM: notice, record-date, and proxy-solicitation compliance]` `[verify jurisdiction]`. Do not assess or assert any notice period.

4. **Capture attendance and representation as provided.** List the chair, the secretary, any inspector of elections, and officers or directors in attendance, as provided. Record the holders present in person, the holders represented by proxy, and the shares, units, or voting power represented — each figure exactly as stated and each attributed to its source (inspector's report, tabulation, or user statement). Insert a placeholder for any missing figure.

5. **Quorum gate.** Record the reported quorum status — what the materials or the user state about the voting power represented and any quorum announcement by the chair. Whether that satisfies the applicable quorum requirement is an attorney determination: `[ATTORNEY TO CONFIRM: quorum sufficiency under the governing documents and applicable law]` `[verify jurisdiction]`. If the materials state that a quorum was **not** represented, or if the quorum status is unknown: **stop drafting the substantive actions.** Insert a defect notice and route to counsel — adjournment, re-noticing, or action by written consent are remediation paths for the attorney to assess, not for the draft to recommend `[verify jurisdiction]`.

6. **Map the order of business.** Working from the agenda, script, and proxy materials, identify each item of business in the order it occurred: procedural openings, each proposal, any polls opened and closed, and any other business, as provided.

7. **Record each proposal as written.** State each proposal in the form presented in the proxy materials or agenda, quoting or reproducing the provided language. Identify who presented it, if provided. Do not paraphrase resolution or proposal language into existence; where the text was not provided, insert `[CONFIRM: text of Proposal [N] as presented]`.

8. **Record vote tallies exactly as provided.** For each proposal, record the votes for, against, and abstaining, and any broker non-votes, exactly as the tabulation or inspector's report states, and label the source. If the chair announced a result, record the announcement as an event that occurred ("the chair announced that the proposal carried"), attributed to the chair. Whether any tally satisfied the applicable approval threshold is flagged, never concluded: `[ATTORNEY TO CONFIRM: vote-threshold sufficiency for each proposal]` `[verify jurisdiction]`.

9. **Record procedural events as provided.** Note the appointment or presence of the inspector of elections, the opening and closing of the polls, any adjournment or postponement announced, and the time of adjournment, in each case only as provided.

10. **Draft the minutes.** Assemble the sections in order: opening (call to order, chair, secretary); notice and record date as provided; attendance and representation as provided; reported quorum status with its attorney flag; each proposal with its recorded tally and announcement; procedural events; adjournment; and a signature block for the secretary (and chair, if house style requires), flagged `[ATTORNEY TO CONFIRM: signature and attestation requirements]`. Use the organization's house format if a precedent was provided; otherwise use a neutral standard form and flag it `[CONFIRM: conform to organization's house style]`.

11. **Flag open items.** At the end of the draft, list every placeholder, every `[verify jurisdiction]` item, every figure or tally not confirmed by a provided source, and every quorum or threshold question flagged for the attorney.

12. **Assemble the output.** Combine the draft minutes, the reported-figures table, the open-items list, the assumptions section, and the attorney verification checklist. Label the entire output as a draft for attorney review.

## Output Format

Deliver:

1. **Draft Minutes** — a complete draft populated only from the provided materials, with bracketed placeholders wherever information is missing or requires attorney confirmation.
2. **Reported Figures Table** — every attendance, representation, quorum, and vote figure used in the draft, each with its source (inspector's report, tabulation, or user statement).
3. **Open Items List** — every unresolved placeholder, `[verify jurisdiction]` item, missing tally or figure, and quorum or vote-threshold question for the attorney.
4. **Assumptions** — an explicit list of every assumption made in drafting, including any format or role inferred from context.
5. **Attorney Verification Checklist** — the checklist from this skill.

Use placeholders consistently. Do not fill any gap with invented content.

## Attorney Verification Checklist

- [ ] The meeting actually took place on the date, at the time, and at the location or platform stated.
- [ ] The record date and the holders entitled to notice and to vote have been confirmed. `[verify jurisdiction]` `[deadline verification required]`
- [ ] Notice was proper under the governing documents and applicable law, or was effectively waived. `[verify jurisdiction]`
- [ ] Any proxy solicitation and proxy materials complied with applicable requirements, and the proxies relied on were valid. `[verify jurisdiction]`
- [ ] Attendance and representation figures have been verified against the inspector's report or official tabulation.
- [ ] Quorum sufficiency has been confirmed under the governing documents and applicable law — the draft records reported figures only. `[verify jurisdiction]`
- [ ] Each vote tally in the minutes matches the official tabulation or inspector's report.
- [ ] Vote-threshold sufficiency for each proposal has been confirmed under the governing documents and applicable law. `[verify jurisdiction]`
- [ ] Each proposal's text in the minutes matches the proposal as actually presented in the proxy materials or at the meeting.
- [ ] Inspector-of-elections appointment, oath, and report requirements, where applicable, were satisfied. `[verify jurisdiction]`
- [ ] If the meeting was virtual or hybrid, that format was authorized under the governing documents and applicable law. `[verify jurisdiction]`
- [ ] The minutes do not contain privileged communications or holder personal data that should be withheld from the formal corporate record.
- [ ] The secretary (and chair, if required) will sign the minutes before they are adopted and filed.
- [ ] No legal authority, statute, or case law has been asserted in the draft without verification.
- [ ] All placeholders and open items are resolved before the minutes are adopted as a corporate record.
- [ ] The finalized minutes are filed in the corporate record book or equivalent repository as required. `[verify jurisdiction]`
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged; profile-silent items are flagged as not-yet-addressed by the playbook.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.
