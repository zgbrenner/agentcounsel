---
name: Privacy Cold-Start Interview
description: Use when a privacy practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions.
---

# Privacy Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a privacy practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/privacy.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/privacy.md` for the first time.
- A privacy practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the privacy area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the privacy practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdictional scope, controller/processor default posture, breach-notification stance, transfer positions, and review requirements.
- Any existing privacy policies, data-processing agreements, breach-response playbooks, records of processing activities, or data-mapping documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively responding to a live privacy incident, breach, or regulatory inquiry. This skill configures the library; it does not support an open matter.
- A `practice-profiles/privacy.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to draft a privacy notice, a data-processing agreement, or a breach notification for a specific matter (use the appropriate matter-level skill for that task).

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Never guess or infer an answer to any interview question. If the interviewee cannot answer a question, record `[CONFIRM: answer required from practice group]` and move on.
- The filled profile is a draft. It must be reviewed and explicitly approved by the supervising attorney or practice group before it governs any AgentCounsel work product.
- Do not invent standard positions, breach-notification stances, transfer mechanisms, DSAR-handling timelines, or escalation thresholds. Record only what the interviewee provides.
- Do not include client-specific facts, client names, matter identifiers, specific data subjects, or privileged details in the profile. The profile is a reusable group-level configuration, not a matter record.
- Do not state or imply that any position, stance, or threshold in the profile satisfies the requirements of any privacy law or regulation in any jurisdiction. Jurisdiction-specific legal obligations — including notification deadlines — are for the attorney to verify `[verify jurisdiction]`.
- Do not assert or imply any notification deadline or response period. All privacy-law deadlines are attorney-verified items outside the scope of this profile and are marked `[deadline verification required]`.
- Flag every item the interviewee defers or leaves open with a visible `[CONFIRM: ...]` placeholder so the reviewer can see exactly what is unresolved.

## Workflow

**Stage 1 — Jurisdictions**

Ask the interviewee:
- In which countries, states, or provinces does the group primarily advise on privacy and data protection matters?
- Does the group advise on cross-border data transfers, and if so, between which regions or jurisdictions?
- Are there jurisdictions where the group's clients are subject to sector-specific privacy regimes — such as those covering health data, financial data, or children's data — and does the group advise on those regimes?
- Are there jurisdictions that the group treats as out of scope, requiring escalation or specialist outside counsel?
- Does the group maintain jurisdiction-specific guidance documents or reference materials? If so, what are they called and where are they stored?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Who are the primary clients of the privacy group — internal business units, external clients, or both?
- What types of privacy matters does the group handle most frequently — regulatory advice, contract review, incident response, DSAR handling, data-mapping projects, or other types?
- How is the team structured — are matters handled by individual attorneys, teams, or in a hybrid model?
- Are there client categories or data types that require special handling or additional sign-off — for example, clients handling sensitive categories of personal data, health information, or data involving minors?
- Does the group coordinate with an in-house data protection officer or a designated privacy function? If so, how does that coordination work?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- What events or indicators trigger mandatory escalation to a supervising attorney or the group's lead — for example, a confirmed breach affecting more than a specified number of individuals, a regulatory inquiry, or a matter involving a sensitive data category?
- Are there matter types — such as cross-border transfers involving high-risk jurisdictions, matters involving children's data, or matters with a potential notification obligation — that always require escalation regardless of scale?
- What is the group's threshold for involving external specialist counsel or a forensics firm in an incident response?
- Who is the designated escalation contact for matters that exceed these thresholds, and what is the expected response time?
- Does the group maintain a written escalation matrix or incident-severity framework? If so, what is it called and where is it stored?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should privacy work product be delivered as a narrative memo, a structured risk table, a checklist, a gap analysis, or another format?
- What level of detail does the practice group expect — executive summary only, full issue-by-issue analysis, or both?
- Are there house style rules for how risk levels, action items, or open questions should be labeled or formatted?
- Should drafts include a separate assumptions section and a separate verification-items section, or are those integrated into the body?
- Are there particular deliverable types — breach-notification drafts, DSAR response templates, data-mapping summaries — for which the group has mandatory format requirements?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What documents constitute the group's authoritative source of truth for privacy standards and positions — for example, a privacy program policy, a data-processing agreement template library, a breach-response playbook, or a records-of-processing-activities document?
- Where are those documents stored, and how should an agent reference them in work product?
- Are any of those documents currently under revision or not yet finalized? If so, which version governs until a new one is approved?
- Does the group maintain a data map or data inventory that agents should reference when assessing the scope of a privacy matter?
- Is there a formal process for updating or approving changes to the source documents?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default posture when a client's role is ambiguous — controller, processor, or joint controller — and what factors does the group use to assess that question?
- What is the group's default stance on breach notification — conservative (notify when in doubt), threshold-based (notify only when a defined threshold is met), or another approach?
- What is the group's default position on cross-border data transfers — what transfer mechanisms does the group prefer, which does it avoid, and how does it handle transfers to or from jurisdictions with restricted transfer rules `[verify jurisdiction]`?
- What is the group's standard approach to DSAR handling — default response timeline target `[deadline verification required]`, identity-verification process, and scope-limitation criteria?
- Does the group have standard data-processing agreement positions — for example, on sub-processor approval, audit rights, deletion timelines, and liability allocation?
- Does the group maintain a formal playbook document that captures these positions? If so, what is it called and where is it stored?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage of a privacy matter does attorney review of work product become mandatory — initial intake, before any external communication, before any regulatory notification, or at other defined stages?
- Are there work-product types for which attorney review is always required regardless of matter stage — for example, breach notification drafts, regulatory responses, or data-transfer impact assessments?
- What is the designated reviewer's role — handling attorney, supervising attorney, data protection officer, or general counsel?
- What is the expected turnaround time for attorney review of standard privacy work product, and how are urgent reviews handled?
- Is there a formal sign-off step — for example, a required approval notation or logged confirmation — before work product is sent externally or a notification is submitted to a regulator?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts, postures, or legal conclusions that agents must never assume without explicit confirmation — for example, that a prior privacy impact assessment remains current, that a transfer mechanism is still valid, or that a data map is up to date?
- Are there privacy-specific risks — such as a notification obligation, a cross-border transfer restriction, or a sensitive-data classification — where an agent must stop and escalate rather than reason through independently?
- Are there matter types or data categories where agents must never proceed beyond intake without direct attorney involvement?
- Are there prior incidents, regulatory inquiries, or lessons learned that should be encoded as explicit prohibitions for agents working on privacy matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/privacy.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/privacy.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdictions listed are accurate and complete for the group's current practice, including all relevant data-protection regimes `[verify jurisdiction]`.
- [ ] Controller/processor default posture reflects the group's current considered position, not a provisional or informal one.
- [ ] Breach-notification stance is consistent with applicable notification obligations across all in-scope jurisdictions `[verify jurisdiction]` and all notification-related deadlines are marked `[deadline verification required]`.
- [ ] Cross-border transfer positions reference current, valid transfer mechanisms `[verify jurisdiction]`.
- [ ] DSAR-handling conventions are consistent with applicable response-period obligations `[verify jurisdiction]` and all DSAR deadlines are marked `[deadline verification required]`.
- [ ] Source-of-truth documents listed are finalized and in effect; any documents under revision are flagged.
- [ ] Data map or data inventory referenced, if any, is current and maintained.
- [ ] Attorney review requirements match the group's current supervision model and any applicable regulatory requirements `[verify jurisdiction]`.
- [ ] Prohibited assumptions are accurate and do not inadvertently exclude items that should be permitted.
- [ ] No client-specific facts, matter identifiers, data-subject information, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/privacy.md` and its effective date recorded.
- [ ] A process for periodic profile review and update — particularly in response to regulatory change — has been identified.
