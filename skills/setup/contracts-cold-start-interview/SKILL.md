---
name: Contracts Cold-Start Interview
description: Use when a contracts practice group is adopting AgentCounsel and needs to configure its practice profile by answering a structured interview covering jurisdictions, client context, escalation thresholds, output preferences, source documents, standard positions, review requirements, and prohibited assumptions.
---

# Contracts Cold-Start Interview

## Purpose

Conduct a structured, staged interview with a contracts practice group — led by a supervising attorney or authorized designee — to gather the information required to populate `practice-profiles/contracts.md`. The skill walks through all eight profile fields in sequence, records every answer, and assembles a filled draft of the profile for the practice group's review and approval. It produces draft legal work product for attorney review — not legal advice and not a final configuration.

## Use When

- A team is adopting AgentCounsel and needs to configure `practice-profiles/contracts.md` for the first time.
- A contracts practice group is being onboarded to the library and no current profile exists.
- The library is being stood up for the first time and the contracts area is included in scope.
- A practice group wishes to revisit or rebuild its profile from scratch rather than make incremental updates.

## Required Inputs

- A knowledgeable person from the contracts practice group — a supervising attorney or an authorized designee — who can answer questions about the group's jurisdiction, positions, escalation rules, and review requirements.
- Any existing playbooks, clause libraries, contract templates, or standard-form documents the group already uses, so they can be referenced or cited in the profile.

## Do Not Use When

- The group is actively working a live contract matter. This skill configures the library; it does not support an open matter.
- A `practice-profiles/contracts.md` already exists and is current. In that case this is a refresh, not a cold start — though the skill may still be used to rebuild the profile deliberately.
- No authorized person is available to answer. Do not complete the interview with guessed or inferred answers; record all gaps as `[CONFIRM: ...]` placeholders.
- The purpose is to review, redline, or negotiate a specific contract (use the appropriate matter-level skill for that task).

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Never guess or infer an answer to any interview question. If the interviewee cannot answer a question, record `[CONFIRM: answer required from practice group]` and move on.
- The filled profile is a draft. It must be reviewed and explicitly approved by the supervising attorney or practice group before it governs any AgentCounsel work product.
- Do not invent standard positions, clause preferences, signing-authority thresholds, or escalation rules. Record only what the interviewee provides.
- Do not include client-specific facts, client names, matter identifiers, or privileged details in the profile. The profile is a reusable group-level configuration, not a matter record.
- Do not state or imply that any threshold, position, or rule in the profile satisfies a legal requirement under any jurisdiction. Jurisdiction-specific legal obligations are for the attorney to verify.
- Flag every item the interviewee defers or leaves open with a visible `[CONFIRM: ...]` placeholder so the reviewer can see exactly what is unresolved.

## Workflow

**Stage 1 — Jurisdictions**

Ask the interviewee:
- In which countries, states, or provinces does the group primarily form and perform contracts?
- Does the group work in any jurisdictions where it operates under significant constraints, local counsel requirements, or special approval rules?
- What governing-law clause does the group default to, and are there jurisdictions where that default must be overridden?
- Are there jurisdictions the group treats as out of scope entirely, requiring escalation or outside counsel?

Record answers. Mark any unanswered item `[CONFIRM: jurisdiction not yet specified]`.

**Stage 2 — Client and Team Context**

Ask the interviewee:
- Who are the primary clients of the contracts group — internal business units, external clients, or both?
- What types of contracts does the group handle most frequently (commercial agreements, vendor agreements, licensing, services agreements, master agreements, or other types)?
- How large is the contracts team, and does it include non-attorney contract professionals whose work must be supervised?
- Are there business units or counterparty categories that require special handling, separate workflows, or additional sign-off?

Record answers. Mark any unanswered item `[CONFIRM: client/team context not yet specified]`.

**Stage 3 — Escalation Thresholds**

Ask the interviewee:
- What contract value threshold triggers mandatory attorney review before signature?
- What categories of clause — for example, unlimited liability, IP ownership transfer, exclusivity, change-of-control, or multi-year auto-renewal — always require attorney escalation regardless of value?
- Is there a counterparty category (such as a competitor, regulated entity, or government body) that triggers mandatory escalation?
- Who is the designated escalation contact for contracts that exceed these thresholds, and what is the expected turnaround?

Record answers. Mark any unanswered item `[CONFIRM: escalation threshold not yet specified]`.

**Stage 4 — Preferred Output Style**

Ask the interviewee:
- Should contract work product be delivered as a narrative memo, a structured risk table, a redline comment set, or another format?
- What level of detail does the practice group expect — executive summary only, full clause-by-clause analysis, or both?
- Are there house style rules for how risk levels, recommendations, or open items should be labeled or formatted?
- Should drafts include a summary of assumptions and open items as a separate section, or integrated into the body?

Record answers. Mark any unanswered item `[CONFIRM: output style preference not yet specified]`.

**Stage 5 — Source-of-Truth Documents**

Ask the interviewee:
- What documents constitute the group's authoritative source of truth for standard contract terms — for example, a master clause library, a playbook document, an approved template set, or an internal wiki?
- Where are those documents stored, and how should an agent reference them in work product?
- Are any of those documents currently under revision or not yet finalized? If so, which version governs until a new one is approved?
- Is there a formal process for updating or approving changes to the source documents?

Record answers and document names. Mark any unanswered item `[CONFIRM: source document not yet identified]`.

**Stage 6 — Standard Positions and Playbooks**

Ask the interviewee:
- What is the group's default position on limitation of liability — cap formula, carve-outs, and any "never accept" terms?
- What is the group's default position on indemnification — unilateral vs. mutual, scope of covered losses, and any "never accept" terms?
- What is the group's preferred or required governing law and dispute-resolution clause?
- What is the group's position on auto-renewal clauses — acceptable, unacceptable, or acceptable only with specified notice and opt-out terms?
- What signing and approval authority rules apply — who may sign at each contract-value tier, and does a matrix or delegation of authority document govern this?
- Are there any other clause categories the group has a documented "always" or "never" position on?
- Does the group maintain a formal playbook document that captures these positions? If so, what is it called and where is it stored?

Record answers. Mark any unanswered item `[CONFIRM: standard position not yet specified]`.

**Stage 7 — Attorney Review Requirements**

Ask the interviewee:
- At what stage of the contracting process is attorney review required — initial draft, before sending to counterparty, before signing, or at multiple stages?
- Are there contract types or counterparty categories for which attorney review is always required, regardless of value?
- What is the designated reviewer's role — reviewing attorney, practice group lead, general counsel, or another role?
- What is the expected turnaround time for attorney review, and how are urgent reviews handled?
- Is there a formal sign-off step — for example, a required signature, approval stamp, or logged confirmation — before a contract is executed?

Record answers. Mark any unanswered item `[CONFIRM: review requirement not yet specified]`.

**Stage 8 — Prohibited Assumptions**

Ask the interviewee:
- Are there facts, terms, or positions that agents must never assume or infer without explicit confirmation — for example, that a counterparty is an affiliate, that a prior course of dealing governs, or that a template is current?
- Are there clause types where a silence or absence should never be treated as agreement?
- Are there business or legal risks that the group has identified as areas where agents must stop and escalate rather than reason through independently?
- Are there prior incidents or lessons learned that should be encoded as explicit prohibitions for agents working on contracts matters?

Record answers. Mark any unanswered item `[CONFIRM: prohibited assumption not yet specified]`.

**Stage 9 — Assemble the Draft Profile**

Compile all answers into a filled draft of `practice-profiles/contracts.md`, populating each of the eight profile sections. For every item that was not answered, insert a visible `[CONFIRM: ...]` placeholder with enough context for the reviewer to understand what needs to be supplied. Append a list of all open placeholders so the reviewing attorney can see at a glance what remains unresolved.

## Output Format

Deliver:

1. **Filled draft of `practice-profiles/contracts.md`** — all eight sections populated with answers from the interview. Every unanswered item is a visible `[CONFIRM: ...]` placeholder.
2. **Open-items list** — an explicit enumeration of every placeholder inserted, with the stage and question it corresponds to, so the reviewing attorney can resolve them efficiently.

Label the entire output: **Draft legal work product for attorney review. Not legal advice. This profile draft must be reviewed and approved by the supervising attorney or practice group before it is relied upon.**

## Attorney Verification Checklist

- [ ] All eight profile sections have been reviewed by a supervising attorney or authorized practice-group representative.
- [ ] Jurisdictions listed are accurate and complete for the group's current practice.
- [ ] Escalation thresholds — value-based, clause-based, and counterparty-based — have been confirmed and are consistent with the group's current authority matrix.
- [ ] Standard positions and playbook references reflect current, approved group positions, not outdated or superseded ones.
- [ ] Source-of-truth documents listed are finalized and in effect; any documents under revision are flagged.
- [ ] Attorney review requirements match the group's current engagement and supervision model.
- [ ] Prohibited assumptions are accurate and do not inadvertently exclude items that should be permitted.
- [ ] No client-specific facts, matter identifiers, or privileged details appear in the profile.
- [ ] All `[CONFIRM: ...]` placeholders have been resolved or explicitly accepted as pending.
- [ ] The approved profile has been saved to `practice-profiles/contracts.md` and its effective date recorded.
- [ ] A process for periodic profile review and update has been identified.
