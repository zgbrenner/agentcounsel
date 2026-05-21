---
name: Create Matter Workspace
description: Use when starting a new legal matter that will span multiple skills, documents, or deadlines, to select the right matter-workspace template, gather core matter information, and produce a populated workspace draft for attorney review.
---

# Create Matter Workspace

## Purpose

Produce a populated matter-workspace draft — the single organizing file that carries one legal matter's parties, facts, jurisdiction, deadlines, documents, open items, and the draft work product produced by every skill run for that matter. This skill selects the correct template from `matter-workspaces/`, interviews the user for the core matter information, fills in what is known, marks what is missing with `[CONFIRM: ...]` and `[ACTION: ...]` placeholders, and explains how to keep the workspace current as further skills are run.

A matter workspace is what preserves context across a multi-step engagement: each skill run is recorded in one place, so facts, deadlines, and drafts are not lost between conversations. This skill produces draft legal work product for attorney review — not legal advice.

## Use When

- A new legal matter is being opened that will involve more than one skill, document, deadline, or team member.
- The user asks to "set up a matter," "create a workspace," "start a new matter file," or "organize this matter."
- Complex or multi-step legal work is about to begin and needs a single organizing file before the first substantive skill is run.
- An existing matter has accumulated drafts, dates, and open items across several conversations and now needs a consolidated workspace.
- The user is unsure which matter-workspace template fits the matter and wants a recommendation.

## Required Inputs

- The matter type, or enough description of the legal work to infer it: litigation or dispute, contract review, privacy, regulatory, corporate transaction, employment, or other.
- The client's identity and the responsible attorney or team, if known.
- A short description of the matter — what it concerns and what outcome is sought.
- Any already-known parties, jurisdiction or governing law, key dates, and source documents.

The skill can proceed with partial information; anything not provided is recorded as a `[CONFIRM: ...]` placeholder. But the matter type (or enough description to infer it) and the client identity are needed to select a template and begin. If the matter type cannot be determined, ask before proceeding — do not guess.

## Do Not Use When

- The task is a single, self-contained skill run with no ongoing matter (for example, a one-off NDA review) — run that skill directly; a workspace is unnecessary overhead.
- The matter is already organized in an existing workspace and the task is to run a substantive skill — open the relevant skill and index its output in the existing workspace.
- The user needs to configure AgentCounsel for a whole practice area rather than a single matter — use the cold-start interview skills in `skills/setup/`.
- The user needs substantive legal analysis — this skill organizes a matter; it does not analyze it. Run the appropriate substantive skill from `WORKFLOW_ROUTER.md`.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Do not invent matter facts, party names, jurisdictions, or dates. Record every unknown as a `[CONFIRM: ...]` placeholder.
- This skill organizes a matter; it does not supply law. Do not invent or assert statutes, regulations, case law, citations, or other legal authority — follow `core/source-and-citation-discipline.md`.
- Do not compute, calculate, or assert any deadline. Every date entered in the workspace carries a `[deadline verification required]` flag and must be independently verified by the responsible attorney.
- Do not resolve the conflicts-check gate or the jurisdiction and deadline gates. Carry them into the workspace as gates for the attorney to clear.
- Separate confirmed facts from client representations and from assumptions, using the workspace's distinct Facts and Assumptions sections. Never blend an assumption into the factual record.
- A populated workspace may be attorney-client privileged and/or attorney work product. Label the populated copy with the privilege designation the responsible attorney confirms, and keep client-sensitive facts out of the blank template.
- Recommend, but do not finalize. The responsible attorney confirms the template choice, the matter scope, and every entry before the workspace is relied upon.

## Workflow

1. **Confirm the matter type and scope.** From the user's description, determine which kind of matter this is. If the matter spans more than one type (for example, a contract dispute), select the template for the primary workflow and record the secondary dimension as an open item.

2. **Select the template.** Map the matter type to a template in `matter-workspaces/`:
   - Litigation or dispute → `matter-workspaces/litigation-matter.md`
   - Contract review, negotiation, or execution → `matter-workspaces/contract-review-matter.md`
   - Privacy event, DPA, DSAR, or processing activity → `matter-workspaces/privacy-matter.md`
   - Regulatory inquiry, compliance review, or enforcement → `matter-workspaces/regulatory-matter.md`
   - Corporate transaction, M&A, financing, or entity matter → `matter-workspaces/corporate-transaction-matter.md`
   - Employment matter — termination, investigation, classification, leave, or policy → `matter-workspaces/employment-matter.md`
   State the recommended template and the basis for the recommendation. If no template fits, say so rather than forcing a poor match.

3. **Gather the matter header information.** Collect the client's full legal name and entity type, the responsible attorney, a matter name, the practice profile in use, the date opened, and the matter status. Record anything missing as a `[CONFIRM: ...]` placeholder.

4. **Interview for the core matter information, section by section.** Work through the selected template's sections and ask targeted questions for what is missing: the parties; the key facts (and, separately, the assumptions); the jurisdiction and governing law; the key dates and deadlines; and the source documents. Ask for one category at a time; do not overwhelm the user with every field at once.

5. **Record what is known; flag what is missing.** Fill each field with the information the user provided, or with a `[CONFIRM: ...]` placeholder. Enter every date exactly as provided and append a `[deadline verification required]` flag — never compute, extend, or infer a date.

6. **Carry the gates into the workspace.** Leave the conflicts-check gate, the jurisdiction and posture gate (Gate 1), and the deadlines gate (Gate 2) as unresolved gates for the responsible attorney. Do not mark any gate cleared.

7. **Seed the work-product index.** List the skills likely to be run for this matter type, drawn from the selected template, with empty status rows to be filled in as each skill is run.

8. **Record an initial open-items list.** Turn every missing required input and every unresolved gate into an action item with an owner and a status of Open.

9. **Assemble the populated workspace draft** using the selected template's structure, preserving the blank-template and privilege banner at the top.

10. **Explain how to maintain the workspace** using the maintenance instructions in the Output Format below.

## Output Format

Deliver the following, labeled as a draft for attorney review:

1. **Template Recommendation** — The recommended template from `matter-workspaces/`, the matter type it matches, and a one-line rationale.

2. **Populated Workspace Draft** — The full selected template with every known field filled in and every unknown marked `[CONFIRM: ...]` or `[ACTION: ...]`. It retains the blank-template and privilege-designation banner at the top.

3. **Maintenance Instructions** — A short, plain set of instructions for keeping the workspace current:
   - Save the populated workspace to a matter-specific location; do not edit the blank template itself.
   - After each skill is run, add a row to the Work-Product Index — the skill, the date, the output, its location, and its review status.
   - Add new facts to the Key Facts section with their source; add new assumptions to the Assumptions section; never blend the two.
   - Add every new date to the deadlines table with a `[deadline verification required]` flag; never compute a date.
   - Update the Open Items list as actions are completed or new ones arise.
   - Run `red-team-verifier` on any high-stakes draft before relying on it.
   - Route the workspace to the responsible attorney to clear the gates and complete the sign-off.

4. **Open Items** — The list of missing information the user or the attorney must still supply before the workspace is complete.

## Attorney Verification Checklist

- [ ] The selected matter-workspace template is appropriate for the matter type.
- [ ] Client identity and the responsible attorney are confirmed.
- [ ] All parties are identified and captured for the conflicts check.
- [ ] The conflicts-check gate and the jurisdiction and posture gate (Gate 1) have been addressed before substantive work begins.
- [ ] Every date in the workspace has been independently verified by the attorney; none was computed by the agent.
- [ ] Confirmed facts, client representations, and assumptions are correctly separated.
- [ ] Jurisdiction and governing law are confirmed.
- [ ] The privilege designation for the populated workspace has been set by the responsible attorney.
- [ ] All `[CONFIRM: ...]` and `[ACTION: ...]` placeholders are tracked for resolution.
- [ ] The populated workspace is stored in an access-controlled location and shared only with authorized personnel.
- [ ] No client-sensitive facts have been written into the blank template.
