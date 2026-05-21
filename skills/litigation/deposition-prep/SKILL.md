---
name: Deposition Preparation
description: Use when building a structured deposition outline from the case theory, witness profile, and documentary record to produce a focused, attorney-ready map for taking or defending a deposition.
---

# Deposition Preparation

## Purpose

Produce a structured deposition outline for attorney review and use. The outline is a strategic map — not a script — that organizes topic blocks, document anchors, and a pivot-fact sequence around the case theory. It is draft legal work product for attorney review; it is not legal advice. The attorney drives the deposition. The skill never drafts a witness statement in the witness's own voice.

## Use When

- Counsel needs to prepare for an upcoming deposition and wants a structured question outline organized around topic blocks.
- A user asks to "prep for a deposition," "draft a depo outline," or "organize the documents for the [witness] deposition."
- The case theory and witness role are clear enough to define a deposition goal.
- Preparing for an adverse, neutral, friendly, or organizational-representative witness.

## Required Inputs

- **Matter identification** — matter name, matter number, or a brief description sufficient to identify the case.
- **Case theory** — one sentence stating the factual and legal proposition the deposing party is trying to establish or defend.
- **Witness profile** — the witness's name, role in the matter, why this witness is being deposed, and posture: adverse, friendly, neutral, or organizational representative (an entity's designated representative).
- **Deposition rules of the forum** — the procedural rules governing the deposition (duration limits, objection conventions, scope limitations). Treat any statement of forum rules as `[verify jurisdiction]` until confirmed by the responsible attorney.
- **Documentary record** — documents to be used in the deposition, provided in full or described with Bates range or a clear identifying description. At minimum, a list of the key documents must be provided.
- **Prior testimony** — prior deposition transcripts, sworn statements, or hearing testimony, if any (pasted or described). If none exists, state that explicitly.

If the matter identification, case theory, witness profile, or at least a summary of the documentary record is not provided, stop and request the missing information. Do not begin the outline. Do not fabricate any of these inputs.

## Do Not Use When

- The user intends to take or defend the live deposition without attorney involvement — the skill produces a draft; attorney judgment governs execution.
- The user needs to draft a witness statement in the witness's own voice. Some jurisdictions restrict how a trial witness statement may be prepared and prohibit drafting it in the witness's own voice — confirm the applicable rule `[verify jurisdiction]`; this skill never drafts a witness statement in the witness's voice.
- A litigation chronology has not yet been built and the factual record is unsettled — use `litigation-chronology` first, then return to this skill.
- The matter is in the pleading or pre-litigation stage and no deposition is imminent — use matter-intake or a case-assessment skill instead.
- The user needs to evaluate or respond to deposition notices, subpoenas, or protective orders — those are separate workflow skills.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- The deposition outline must not be used as a final litigation strategy document or as a substitute for attorney preparation. The attorney drives every phase of the deposition.
- **Record fidelity.** Every quotation from a document or prior testimony must be verbatim, exact, and pinpointed to the source (Bates number, transcript page and line, exhibit number). A paraphrase or summarized quotation must be flagged as `[VERIFY: paraphrase — confirm exact language and pinpoint citation]`. Never attribute language to a document or witness that has not been confirmed from the actual text.
- Do not predict witness answers, invent testimony, or speculate about how the witness will respond. An outline anticipates topics, not answers.
- Do not assert legal authority (statutes, rules, case law) without attorney direction. Flag any rule-based proposition as `[CONFIRM: attorney to verify rule and current authority in forum]`.
- Do not compute, state, or imply any deadline. Use `[deadline verification required]` wherever a date or time limit is relevant.
- Treat all deposition rules and procedural limits as `[verify jurisdiction]` until confirmed by the responsible attorney.
- Flag every assumption — about posture, scope, document relevance, or legal standard — explicitly, rather than resolving it silently.
- This skill never drafts a witness statement in the witness's own voice. If requested to do so, explain the prohibition and decline.
- Preserve confidentiality and privilege. Keep client-sensitive facts and privileged communications out of any reusable copy of the template.
- Separate facts (from documents and testimony), assumptions (flagged), legal propositions (flagged for attorney confirmation), and strategic judgments (labeled as attorney work product).

## Workflow

1. **Confirm inputs.** Verify that the matter identification, case theory, witness profile (including posture), deposition forum rules, and documentary record have been provided. If any required input is missing, stop and request it. Do not proceed with fabricated or assumed inputs.

2. **Identify the witness and posture.** Record the witness's name, role, and relationship to the key facts. Determine deposition posture:
   - **Adverse** — use closed, leading questions to control the record and lock in damaging admissions.
   - **Friendly or aligned** — use open questions to elicit narrative and build the record.
   - **Neutral** — use a mixed approach: open to establish context, closed to lock specifics.
   - **Organizational representative** — confirm the scope of designation `[CONFIRM: attorney to verify scope of notice or designee]`; treat as adverse on disputed topics unless otherwise directed.
   Flag posture with `[CONFIRM: attorney to verify]` if it is uncertain or if the witness's alignment may shift.

3. **Check deposition rules of the forum.** Identify stated limits on duration, scope, objection conventions, and any applicable restrictions on witness preparation. Treat all stated rules as `[verify jurisdiction]`. Flag any rule that may affect question strategy or timing, including limits on speaking objections, coaching, or breaks during testimony.

4. **Flag the witness-statement restriction.** Note explicitly: some jurisdictions restrict how a trial witness statement may be prepared, including prohibiting drafting it in the witness's own voice. Confirm the applicable rule `[verify jurisdiction]`. This skill does not draft a witness statement in the witness's voice.

5. **Organize the documentary record.** Review and organize every provided document chronologically. For each document, note: Bates number or identifier, date, author, recipient, a one-sentence description, and the deposition section where it is most relevant. Flag the documents most important to the case theory. Flag any document whose relevance or authenticity requires attorney confirmation with `[CONFIRM]`.

6. **Review prior testimony.** If prior testimony is provided, identify statements that are favorable (to lock in), unfavorable (to confront or impeach), or inconsistent (to use for impeachment). Record exact transcript citations (page and line). Flag every quotation: if verbatim, mark as confirmed; if paraphrased, mark `[VERIFY: confirm exact language at p. ___, l. ___]`.

7. **Identify the pivot-fact sequence.** Identify the two to four questions that are most directly case-turning — the sequence where, if the witness answers truthfully, the answer either builds or damages the opponent's position. This sequence is the structural spine of the outline. Draft it before building topic blocks.

8. **Build topic blocks in the following arc:**
   - **Background** — establish undisputed biographical and role facts; lock uncontroversial facts the witness cannot credibly walk back.
   - **Lock in good facts** — open or closed questions (depending on posture) to lock favorable facts already documented.
   - **Confront with bad facts** — closed, controlled questions (adverse) or open questions (friendly) to build the record on facts that damage the opponent's position.
   - **Impeachment** — prior inconsistent statements, document contradictions, or prior testimony. Each impeachment point must carry its pinpoint citation.
   - **Pivot-fact sequence** — the case-turning question chain from step 7.

9. **Calibrate to 3–4 topic blocks.** A focused outline beats an exhaustive one. Lead with the strongest confrontation or the most case-dispositive topic. Trim or defer topics that are secondary. Mark deferred topics as `[DEFERRED — attorney to decide whether to include]`.

10. **Flag open items and attorney verification points.** Compile all `[CONFIRM]`, `[VERIFY]`, `[verify jurisdiction]`, `[deadline verification required]`, and `[ATTORNEY TO CONFIRM]` items into the open-items section of the outline.

11. **Assemble the draft outline** using `templates/deposition-outline.md`. Label the output: "DRAFT — Attorney Work Product — For Attorney Review and Use Only."

## Output Format

Deliver a complete draft deposition outline using `templates/deposition-outline.md`. The outline includes:
- A header block (matter, witness, posture, forum rules, deposition goal, connection to the case theory)
- Background section (locking undisputed facts)
- Three to four topic blocks (good facts / bad facts / impeachment) each with stated goal, documents used, and draft questions
- Pivot-fact sequence (the case-turning question chain)
- Exhibit list table
- Notes for the attorney (demeanor considerations, weak points, suggested areas to expand)
- Open items for attorney verification

Use `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and `[deadline verification required]` wherever information is unconfirmed or requires attorney judgment. Label the assembled draft as attorney work product for attorney review.

## Attorney Verification Checklist

- [ ] Case theory is accurately captured and confirmed by the responsible attorney.
- [ ] Witness posture (adverse / friendly / neutral / organizational representative) is correct.
- [ ] Deposition forum rules confirmed, including duration limits, scope limitations, and objection conventions `[verify jurisdiction]`.
- [ ] Witness-statement restriction confirmed for the applicable jurisdiction `[verify jurisdiction]`.
- [ ] Every document quotation is verbatim and pinpointed to the source; paraphrases have been verified.
- [ ] Every quotation from prior testimony is verbatim with page and line citation confirmed.
- [ ] No legal authority has been asserted without attorney verification.
- [ ] No deadlines have been stated or computed; all date-sensitive items carry `[deadline verification required]`.
- [ ] Deposition goal and topic block structure are strategically sound and approved by the responsible attorney.
- [ ] Pivot-fact sequence reviewed and approved by the responsible attorney.
- [ ] Exhibit list is complete, accurate, and cross-referenced to the correct topic sections.
- [ ] All assumptions, deferred topics, and flagged items have been resolved before the outline is used.
- [ ] Output is labeled attorney work product and held in the appropriate client file.
