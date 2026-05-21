---
name: Litigation Cold-Start Interview
description: Use when a litigation practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions.
---

# Litigation Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a litigation practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/litigation.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/litigation.md` for the first time.
- A litigation practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the litigation area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the litigation practice group — a supervising attorney or an authorized designee — who can answer questions about the group's forums, conflicts process, hold triggers, settlement authority, and review requirements.
- Any existing litigation playbooks, hold-notice templates, settlement-authority matrices, or standard procedure documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live litigation matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/litigation.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to intake, triage, or work a specific dispute or proceeding (use the appropriate matter-level skill for that task).

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Never guess or infer an answer to any interview question. If the interviewee cannot answer a question, record `[CONFIRM: answer required from practice group]` and move on.
- The filled profile is a draft. It must be reviewed and explicitly approved by the supervising attorney or practice group before it governs any AgentCounsel work product.
- Do not invent standard positions, settlement-authority figures, conflicts-process steps, or hold-trigger criteria. Record only what the interviewee provides.
- Do not include client-specific facts, client names, matter identifiers, case numbers, or privileged details in the profile. The profile is a reusable group-level configuration, not a matter record.
- Do not state or imply that any threshold, trigger, or rule in the profile satisfies a procedural or ethical requirement under any jurisdiction. Jurisdiction-specific legal obligations are for the attorney to verify.
- Do not assert or imply any deadline. All procedural deadlines and limitations periods are attorney-verified items outside the scope of this profile.
- Flag every item the interviewee defers or leaves open with a visible `[CONFIRM: ...]` placeholder so the reviewer can see exactly what is unresolved.

## Workflow

**Stage 1 — Jurisdictions**

Ask the interviewee:
- In which federal, state, provincial, or foreign courts and tribunals does the group primarily practice?
- Does the group appear before arbitral bodies, administrative agencies, or regulatory forums? If so, which categories?
- Are there jurisdictions or forums that the group treats as out of scope, requiring escalation or outside counsel?
- Are there jurisdictions where local counsel is always required, and if so, under what circumstances is the group's internal team still involved?
- Does the group have jurisdiction-specific procedural guides or local-rules summaries it relies on?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Who are the primary clients of the litigation group — internal business units, external clients, or both?
- What types of matters does the group handle most frequently — commercial disputes, employment litigation, regulatory proceedings, product liability, intellectual property disputes, or other types?
- How is the team structured — are matters handled by individual attorneys, teams, or in a hybrid model?
- Are there matter types or client categories that require special handling, coordination with other practice groups, or involvement of insurance or indemnitors?
- Does the group use a matter-management or docket system, and if so, what is it?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- What claimed-damages or exposure threshold triggers mandatory escalation to senior litigation counsel, general counsel, or the client's risk function?
- Are there matter types — such as class actions, government investigations, regulatory enforcement, or matters involving reputational risk — that always require escalation regardless of claimed amount?
- At what point in a matter's life cycle does the group's escalation process activate — on receipt of a demand, on filing of a complaint, on service, or at another trigger?
- Who is the designated escalation contact for matters that exceed these thresholds, and what is the expected response time?
- Does the group maintain a written escalation matrix or decision tree? If so, what is it called and where is it stored?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should litigation work product be delivered as a narrative memo, a structured chronology, a bullet-point summary, a table of issues, or another format?
- What level of detail does the practice group expect — executive summary only, full issue-by-issue analysis, or both?
- Are there house style rules for how risk ratings, action items, or open questions should be labeled or formatted?
- Should drafts include a separate assumptions section and a separate verification-items section, or are those integrated into the body?
- Are there particular deliverable types — litigation hold notices, intake summaries, chronologies — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What documents constitute the group's authoritative source of truth for litigation procedures and standards — for example, a litigation manual, a playbook, an internal procedures guide, or a matter-management policy?
- Where are those documents stored, and how should an agent reference them in work product?
- Are any of those documents currently under revision or not yet finalized? If so, which version governs until a new one is approved?
- Is there a formal process for updating or approving changes to the source documents?
- Are there external procedural sources — court standing orders, local rules compilations, or approved forms — that the group treats as authoritative?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's standard conflicts-check process — who runs it, at what stage, using what system, and who clears it?
- What are the group's litigation-hold trigger criteria — what events or thresholds require a hold notice to issue, and to whom?
- What are the group's settlement-authority thresholds — who may authorize settlement at each amount tier, and does a written settlement-authority matrix exist?
- What is the group's default position on reporting lines for active litigation — who in the client organization is kept informed, at what frequency, and in what format?
- Does the group have a preferred approach to mediation, arbitration, or other alternative dispute-resolution processes? If so, what is it?
- Does the group maintain a formal playbook document that captures these positions? If so, what is it called and where is it stored?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage of a matter does attorney review of work product become mandatory — initial intake, before any external communication, before any filing, or at other defined stages?
- Are there work-product types for which attorney review is always required regardless of matter stage — for example, litigation hold notices, tolling agreement drafts, or settlement term sheets?
- What is the designated reviewer's role — handling attorney, supervising attorney, practice group lead, or general counsel?
- What is the expected turnaround time for attorney review of standard work product, and how are urgent or deadline-driven reviews handled?
- Is there a formal sign-off step — for example, a required approval notation or logged confirmation — before work product is sent externally?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts, postures, or procedural states that agents must never assume without explicit confirmation — for example, that service has been completed, that a hold is already in place, or that a prior conflicts check remains current?
- Are there litigation-specific risks — such as waiver, spoliation, or privilege — where an agent must stop and escalate rather than reason through independently?
- Are there matter types or counterparty categories where agents must never proceed beyond intake without direct attorney involvement?
- Are there prior incidents or lessons learned that should be encoded as explicit prohibitions for agents working on litigation matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/litigation.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/litigation.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdictions and forums listed are accurate and complete for the group's current practice.
- [ ] Conflicts-check process is correctly described and consistent with the group's current procedures and applicable professional-conduct obligations `[verify jurisdiction]`.
- [ ] Litigation-hold trigger criteria are accurate and consistent with the group's current preservation obligations `[verify jurisdiction]`.
- [ ] Settlement-authority thresholds match the group's current authority matrix and client engagement terms.
- [ ] Escalation thresholds and reporting lines reflect current organizational structure and client requirements.
- [ ] Source-of-truth documents listed are finalized and in effect; any documents under revision are flagged.
- [ ] Attorney review requirements match the group's current supervision model and any applicable professional-conduct rules `[verify jurisdiction]`.
- [ ] Prohibited assumptions are accurate and do not inadvertently exclude items that should be permitted.
- [ ] No client-specific facts, matter identifiers, case numbers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/litigation.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
