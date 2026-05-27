---
name: Board Minutes
description: "Use when drafting minutes of a board of directors or board-committee meeting as a corporate record, producing a structured draft for attorney review."
practice_area: corporate
task_type: drafting
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "Meeting details: entity, body, date, time, and location"
  - "Attendance and quorum information"
  - "Agenda items, materials presented, and actions taken"
outputs:
  - "Draft minutes of the board or committee meeting for attorney review"
related_skills:
  - skills/corporate/written-consent/SKILL.md
tags:
  - corporate
  - governance
  - board-minutes
  - corporate-records
  - drafting
---

# Board Minutes

## Purpose

Produce a structured, attorney-ready draft of minutes for a meeting of a board of directors or a board committee. The draft captures the meeting record — attendance, quorum, agenda items, discussion summaries, and resolutions — in a form that can be reviewed, revised, and finalized by an attorney before adoption. It produces draft legal work product for attorney review — not legal advice and not an adopted corporate record.

## Use When

- A user asks to "draft the board minutes" or "write up the minutes" for a meeting that has already taken place or is being memorialized.
- The user has meeting materials (agenda, slides, pre-reads, or notes) and needs a minutes document prepared for attorney review before adoption.
- A board committee meeting (audit, compensation, nominating/governance, special committee, or other) needs to be memorialized in the same way.
- The user wants a starting draft that conforms to the organization's house format before the attorney finalizes it.

## Required Inputs

- **Meeting identification:** whether this is a full board meeting or a named committee meeting; the date, time, and location or virtual platform.
- **Notice status:** whether proper notice was given (and how) or whether notice was waived.
- **Attendance:** directors or committee members present and absent (by name and capacity); management attendees (name and title); guests (name, firm or role, and the reason for attendance); the name of the person who served as chair; the name of the person who served as secretary.
- **Quorum status:** confirmation from the user that a quorum was or was not present. Do not determine the quorum requirement independently — the applicable threshold must come from the governing documents or be verified against the applicable rules by the attorney. `[verify jurisdiction]`
- **Meeting materials:** agenda, board or committee slides, pre-reads, proposed resolutions, and any exhibits referenced at the meeting.

Optional but recommended:
- A prior set of the organization's minutes for house-format reference.
- The organization's preferred minutes style: narrative (full discussion summaries), action-only (resolutions with minimal discussion), or hybrid.
- The practice group's `practice-profiles/corporate.md` if it has been populated and is loaded alongside this skill. If present, the skill uses its Preferred Output Style and Standard Positions tables to benchmark the draft minutes against the group's house style and resolution-form defaults. If absent, the skill proceeds without practice-profile benchmarking and asks the user to supply standing positions inline if needed.

If any required input is missing, stop and request it. Do not fabricate attendance lists, resolution language, discussion content, or quorum determinations.

## Do Not Use When

- The board is acting by written consent rather than at a meeting — use `written-consent` instead.
- The user wants an agenda or standalone board resolutions drafted from scratch as a separate task, not as part of a minutes document — use the appropriate agenda or resolution drafting skill.
- The user is asking whether a particular action was validly approved — that is a legal determination for the attorney, not a drafting task.
- A quorum was not present at the meeting (see Workflow, Step 4 — Quorum Hard Stop).
- The minutes are for a member or shareholder meeting rather than a board or committee meeting.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice. An attorney must review, revise, and authorize the finalization and adoption of any minutes before they become a corporate record.
- Do not invent discussion content, resolution language, attendee names, exhibit descriptions, voting counts, or quorum thresholds. Where materials are missing, insert a clearly labeled placeholder rather than filling the gap with assumed content.
- Do not assert or apply specific statutes, corporate-code sections, or jurisdiction-specific rules. Quorum requirements, notice rules, voting standards, and procedural requirements vary by jurisdiction and by the entity's governing documents. Treat all such requirements as `[verify jurisdiction]` items for the attorney.
- Treat model background knowledge about corporate law and procedure as unverified. Do not carry it into the draft as stated authority.
- Distinguish what the meeting materials actually say from what you assume and from what the attorney must confirm. Label assumptions explicitly.
- The draft minutes are attorney work product; they reflect the drafting attorney's mental impressions and should not be circulated as if adopted. The agent does not adopt, finalize, sign, or circulate minutes.
- A quorum defect is a substantive legal problem. If a quorum was not present, do not draft minutes that imply a valid meeting occurred (see Workflow, Step 4).
- Preserve confidentiality and privilege. Do not place client-sensitive facts, sensitive discussion content, or identifying transaction details into a reusable copy of the template.
- Flag every uncertainty with a bracketed placeholder (`[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`). Never resolve uncertainty silently.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/corporate.md` is loaded, its Preferred Output Style and Standard Positions inform the draft but never substitute for attorney judgment. The profile is a configuration record approved by the practice group; it is not legal advice and does not override the skill's normal attorney-verification gates. If the profile's standing positions conflict with the matter facts or with what the supervising attorney concludes, the attorney prevails.

## Workflow

1. **Confirm inputs.** Verify that all required inputs are present: meeting identification, notice status, attendance, quorum status, and meeting materials. If any required input is missing, request it before proceeding. Do not proceed on assumed attendance or fabricated materials.

2. **Record meeting metadata.** Capture the entity name, meeting type (full board or named committee), date, time, and location or platform, and note them at the top of the draft.

3. **Capture attendance.** List directors or committee members present and absent, management attendees, and guests (with roles). Identify the chair and the secretary. Note any director or member who joined or departed during the meeting, and at what point, if that information is provided.

4. **Quorum hard stop.** Before drafting the substantive body of the minutes, confirm whether a quorum was present.
   - The quorum requirement must come from the organization's governing documents (charter, bylaws, committee charter) or be verified under applicable law. `[verify jurisdiction]` Do not apply a default rule from model background knowledge.
   - If a quorum **was** present: note it in the opening section and proceed.
   - If a quorum **was not** present, or if the quorum status is unknown: **stop drafting.** Do not produce minutes that imply a valid meeting occurred. Insert a defect notice and route to counsel to assess remediation options — which may include ratification by a properly constituted body, a re-convened meeting at which a quorum is present, or action by written consent in lieu of a meeting — in each case `[verify jurisdiction]`. Do not recommend a specific remediation path; that is a legal determination for the attorney.

5. **Map the agenda.** Working from the provided agenda and materials, identify each agenda item in order. For each item, note: the topic, any pre-read or slide deck section referenced, any proposed resolution, and the exhibit designation (if any).

6. **Draft the minutes.** Using `templates/board-minutes-outline.md`, populate each section:
   - **Opening:** confirm the chair called the meeting to order; state notice was proper or was waived and by whom; state quorum was present `[verify jurisdiction]`; confirm the secretary.
   - **Approval of prior minutes:** note if prior minutes were presented, by whom, and whether they were approved as presented or with corrections.
   - **One section per agenda item:** write a discussion summary and the resolution or action taken. For narrative and hybrid style, summarize the substance of the discussion as reflected in the materials. For action-only style, record the resolution and the vote. Where materials do not describe the discussion, insert `[PLACEHOLDER — summarize discussion based on materials provided]`. Never fabricate discussion.
   - **Resolution language:** use the organization's resolution form if a precedent is provided — either inline by the user or via the loaded `practice-profiles/corporate.md` Preferred Output Style / Standard Positions sections. Otherwise use a neutral standard form and flag it: `[CONFIRM: conform resolution form to organization's house style and governing documents]`. Where the profile is loaded but is silent on a specific resolution form, treat that form as not addressed by the playbook and flag for attorney review.
   - **Adjournment:** note that there being no further business, the chair declared the meeting adjourned, and record the time if provided.
   - **Signature block:** include lines for chair and secretary, flagged for execution and dating `[ATTORNEY TO CONFIRM: signature and attestation requirements]`.

7. **Flag open items.** At the end of the draft, list every item marked as a placeholder or `[verify jurisdiction]`, every resolution that needs to be conformed to house style, and every attendee, exhibit, or date that was not confirmed in the provided materials.

8. **Assemble the output.** Combine the draft minutes (from `templates/board-minutes-outline.md`), the open-items list, the assumptions section, and the attorney verification checklist. Label the entire output as a draft for attorney review.

## Output Format

Deliver:

1. **Draft Minutes** — a complete draft using `templates/board-minutes-outline.md`, populated from the provided materials with bracketed placeholders wherever information is missing or requires attorney confirmation.
2. **Open Items List** — every unresolved placeholder, `[verify jurisdiction]` item, resolution to be conformed, and attendee or exhibit not confirmed in the materials.
3. **Assumptions** — an explicit list of every assumption made in drafting, including assumed meeting format, assumed resolution form used, and any attendee role or title inferred from context.
4. **Attorney Verification Checklist** — the checklist from this skill.

Use placeholders consistently. Do not fill any gap with invented content.

## Attorney Verification Checklist

- [ ] The meeting actually took place on the date, at the time, and at the location stated.
- [ ] Notice was proper under the governing documents and applicable law, or was effectively waived by all required parties. `[verify jurisdiction]`
- [ ] Attendance is accurate and complete, including any directors who joined or left during the meeting.
- [ ] A quorum was present throughout the portions of the meeting at which action was taken, as required by the governing documents and applicable law. `[verify jurisdiction]`
- [ ] Each resolution accurately states the action approved and the vote (or unanimous approval without objection).
- [ ] Resolution language conforms to the organization's governing documents, any applicable shareholder or board approval requirements, and house style.
- [ ] All exhibits referenced in the minutes are identified correctly and are attached or on file.
- [ ] Prior minutes were properly presented and approved.
- [ ] No action taken at the meeting exceeded the authority granted to the board or committee by the governing documents or applicable law. `[verify jurisdiction]`
- [ ] Any conflicted director or member was identified, disclosed, and handled appropriately. `[verify jurisdiction]`
- [ ] Discussion summaries accurately reflect what occurred and do not include content that was not discussed.
- [ ] The minutes do not contain privileged communications that should be withheld from the formal corporate record.
- [ ] The chair and secretary have signed or will sign the minutes before they are adopted and filed.
- [ ] No legal authority, statute, or case law has been asserted in the draft without verification.
- [ ] All placeholders and open items are resolved before the minutes are adopted as a corporate record.
- [ ] The finalized minutes are filed in the corporate record book or equivalent repository as required by the governing documents and applicable law. `[verify jurisdiction]`
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged; profile-silent items are flagged as not-yet-addressed by the playbook.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.
