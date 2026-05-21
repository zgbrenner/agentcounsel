---
name: Corporate Cold-Start Interview
description: Use when a corporate practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions.
---

# Corporate Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a corporate practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/corporate.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/corporate.md` for the first time.
- A corporate practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the corporate area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the corporate practice group — a supervising attorney or an authorized designee — who can answer questions about the group's entity portfolio, approval and signing matrices, board and committee processes, and review requirements.
- Any existing entity charts, approval authority matrices, board resolution templates, transaction checklists, or diligence playbooks the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live corporate transaction or governance matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/corporate.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to prepare board materials, diligence reports, or transaction documents for a specific matter (use the appropriate matter-level skill for that task).

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Never guess or infer an answer to any interview question. If the interviewee cannot answer a question, record `[CONFIRM: answer required from practice group]` and move on.
- The filled profile is a draft. It must be reviewed and explicitly approved by the supervising attorney or practice group before it governs any AgentCounsel work product.
- Do not invent entity lists, approval thresholds, signing authorities, board processes, or diligence standards. Record only what the interviewee provides.
- Do not include client-specific facts, client names, matter identifiers, specific transaction details, or privileged details in the profile. The profile is a reusable group-level configuration, not a matter record.
- Do not state or imply that any threshold, process, or rule in the profile satisfies a statutory or regulatory requirement in any jurisdiction. Jurisdiction-specific legal obligations — including corporate formality requirements — are for the attorney to verify `[verify jurisdiction]`.
- Flag every item the interviewee defers or leaves open with a visible `[CONFIRM: ...]` placeholder so the reviewer can see exactly what is unresolved.

## Workflow

**Stage 1 — Jurisdictions**

Ask the interviewee:
- In which countries, states, or provinces does the group primarily advise on corporate and entity matters — including formation, maintenance, and transactions?
- Does the group advise on entities organized in jurisdictions different from where they operate, and if so, what are the most common combinations?
- Are there jurisdictions where the group's clients face sector-specific corporate requirements — for example, regulated industries, foreign investment restrictions, or public company obligations `[verify jurisdiction]`?
- Are there jurisdictions that the group treats as out of scope, requiring escalation or specialist outside counsel?
- Does the group maintain jurisdiction-specific entity guides, registered-agent arrangements, or corporate formalities checklists? If so, what are they called and where are they stored?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Who are the primary clients of the corporate group — internal business units managing a parent-subsidiary structure, external corporate clients, portfolio companies, or a mix?
- What is the approximate scope of the entity portfolio the group supports — how many entities across how many jurisdictions?
- What types of corporate matters does the group handle most frequently — entity formation and maintenance, equity transactions, M&A, financings, governance and board support, or other types?
- Are there entity types or transaction categories that require special handling, coordination with other practice groups, or involvement of tax, regulatory, or specialist counsel?
- Does the group use an entity-management system or a company-secretary platform, and if so, what is it?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- What transaction-value or equity-dilution threshold triggers mandatory escalation to senior corporate counsel, general counsel, or the board?
- Are there transaction types — such as a change of control, a merger or acquisition above a specified size, an issuance of equity above a specified percentage, or a disposition of a material asset — that always require escalation regardless of headline value?
- Are there counterparty categories — such as competitors, regulated entities, strategic investors, or government bodies — that trigger mandatory escalation?
- What is the group's threshold for involving outside counsel or specialist advisers on a transaction?
- Who is the designated escalation contact for matters that exceed these thresholds, and what is the expected response time?
- Does the group maintain a written escalation matrix or transaction-approval policy? If so, what is it called and where is it stored?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should corporate work product be delivered as a narrative memo, a structured checklist, a diligence summary table, a transaction timeline, or another format?
- What level of detail does the practice group expect — executive summary only, full issue-by-issue analysis, or both?
- Are there house style rules for how risk levels, open items, or action steps should be labeled or formatted?
- Should drafts include a separate assumptions section and a separate verification-items section, or are those integrated into the body?
- Are there particular deliverable types — board resolutions, officer certificates, diligence reports, capitalization-table summaries — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What documents constitute the group's authoritative source of truth for corporate standards and processes — for example, an entity chart, an approval authority matrix, a board-resolution template library, a transaction checklist, or a diligence playbook?
- Where are those documents stored, and how should an agent reference them in work product?
- Are any of those documents currently under revision or not yet finalized? If so, which version governs until a new one is approved?
- Is there a corporate or entity-management system that serves as the record of entity status and organizational documents?
- Is there a formal process for updating or approving changes to the source documents?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's approval and signing authority matrix — who may bind the organization at each transaction-value tier, and does a written delegation of authority document govern this?
- What is the group's standard board and committee process — notice requirements, quorum conventions, consent-in-lieu-of-meeting conventions, and record-keeping approach?
- What is the group's standard diligence threshold and scope for an acquisition or investment — at what deal size does full diligence apply vs. a streamlined scope, and what areas are always covered?
- What is the group's default position on representations and warranties — including materiality qualifiers, knowledge qualifiers, and survival periods — in acquisition agreements?
- Does the group have standard indemnification positions for corporate transactions — including caps, baskets, and carve-outs — and are those positions documented?
- Does the group maintain a formal playbook document that captures these positions? If so, what is it called and where is it stored?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage of a corporate matter does attorney review of work product become mandatory — initial intake, before any board presentation, before any external communication, before signing, or at other defined stages?
- Are there work-product types for which attorney review is always required regardless of matter stage — for example, board resolutions, officer certificates, opinion letters, or transaction closing checklists?
- What is the designated reviewer's role — handling attorney, supervising attorney, general counsel, or outside counsel?
- What is the expected turnaround time for attorney review of standard corporate work product, and how are time-sensitive closings or board deadlines handled?
- Is there a formal sign-off step — for example, a required approval notation, a legal sign-off on a closing certificate, or a logged confirmation — before work product is relied upon or a transaction closes?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts, statuses, or authorizations that agents must never assume without explicit confirmation — for example, that an entity is in good standing, that a prior board approval is still current, that a signing authority matrix has not changed, or that an organizational document is the most recent version?
- Are there corporate-specific risks — such as unauthorized commitments, defective corporate action, or missing consents — where an agent must stop and escalate rather than reason through independently?
- Are there transaction types or entity categories where agents must never proceed beyond intake without direct attorney involvement?
- Are there prior incidents, compliance failures, or lessons learned that should be encoded as explicit prohibitions for agents working on corporate matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/corporate.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/corporate.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdictions listed are accurate and complete for the group's current entity portfolio and transaction practice.
- [ ] The entity portfolio scope is accurate; any entities omitted from the profile have been deliberately excluded and that exclusion is documented.
- [ ] Approval and signing authority matrix is consistent with the organization's current delegation of authority documents and applicable corporate formality requirements `[verify jurisdiction]`.
- [ ] Board and committee process conventions are consistent with the organization's governing documents and applicable legal requirements `[verify jurisdiction]`.
- [ ] Diligence thresholds and scope reflect the group's current approved standards, not outdated ones.
- [ ] Standard transaction positions — representations, warranties, indemnification — reflect current, approved group positions.
- [ ] Source-of-truth documents listed are finalized and in effect; any documents under revision are flagged.
- [ ] Attorney review requirements match the group's current supervision model and any applicable professional-conduct rules `[verify jurisdiction]`.
- [ ] Prohibited assumptions are accurate and do not inadvertently exclude items that should be permitted.
- [ ] No client-specific facts, matter identifiers, transaction details, or privileged information appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/corporate.md` and its effective date recorded.
- [ ] A process for periodic profile review and update — particularly following organizational changes or authority-matrix revisions — has been identified.
