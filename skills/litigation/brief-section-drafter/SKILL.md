---
name: Brief Section Drafter
description: Use when drafting a single section of a litigation brief — such as a statement of facts, argument section, standard of review, or conclusion — that is cited to the record, consistent with the case theory, and fully flagged for attorney verification before filing.
---

# Brief Section Drafter

## Purpose

Produce a first draft of a single section of a litigation brief for attorney review, revision, and sign-off. The draft is cited to the record, internally consistent with the case theory, and marked throughout with verification placeholders wherever legal authority or factual accuracy must be confirmed. It is draft legal work product for attorney review; it is not legal advice. The draft is never filed unreviewed.

This skill does not decide litigation strategy, invent legal authority, or produce a final, file-ready document. It writes disciplined, honest prose that gives the supervising attorney a solid working draft — not a shortcut around professional judgment.

## Use When

- Counsel needs a first draft of a specific brief section: a statement of facts, an argument section or sub-section, a standard of review section, a conclusion, or a similar discrete component of a written submission.
- A user asks to "draft the argument section," "write the statement of facts," or "put together the standard-of-review section."
- The case theory and the relevant record materials are available and can be provided as inputs.
- The matter is in active litigation or an imminent filing posture and the section type is known.
- The draft is for a written submission (motion, opposition, brief, reply) or, with appropriate scope adjustment, a structured outline for oral argument preparation.

## Required Inputs

- **Matter identification** — matter name, matter number, or a brief description sufficient to identify the case.
- **Case theory** — one sentence stating the factual and legal proposition the filing party is advancing. The entire draft turns on this sentence; without it, the skill cannot produce a coherent section.
- **Section type** — the specific section to be drafted: statement of facts, argument (identify the proposition), standard of review, conclusion, or another named section. If the section type is ambiguous, the skill will ask for clarification before drafting.
- **Written submission or oral argument** — confirm which posture applies. Written submissions call for thorough authority development with full citation placeholders; oral argument preparation produces a leaner structure with a sharper lead and fewer supporting points.
- **Forum and local rules** — paste the relevant local rules, standing orders, or page and word-count limits directly into the input. If this material is not provided, the skill will flag all format and length requirements as `[CONFIRM: forum rules not provided — attorney to verify]`. Do not rely on the skill's background knowledge of any court's rules; treat all unstated rules as unconfirmed.
- **House style sample** — a sample brief or excerpt from the supervising attorney or firm showing the expected tone, heading style, citation format, and prose register. If none is provided, the skill will note the absence and apply a neutral, professional default, flagging the style choice for attorney review.
- **Record materials** — the documents, deposition transcripts, declarations, pleadings, or other record items that will supply the factual predicate for this section. Every fact in the draft must be tied to a provided record item or flagged `[VERIFY: record cite needed]`. If no record materials are provided, the skill cannot draft a fact-intensive section and will stop to request them.
- **Authorities already identified by counsel** — any cases, statutes, rules, or secondary sources that the supervising attorney has already confirmed and directed the skill to use. The skill will insert these as placeholders in the proper locations; it will not add authority beyond what is provided and directed.

If matter identification, case theory, or section type is missing, stop and request the missing information before proceeding. Do not fabricate any input.

## Do Not Use When

- The user wants a complete, final, file-ready brief. This skill produces a single-section draft for attorney review and substantial revision; use it section by section and assemble under attorney supervision.
- The user needs to draft a witness statement in the witness's own voice. Some forums restrict how witness statements may be prepared; this skill never drafts in the witness's voice. Use `deposition-prep` for deposition preparation materials.
- The user needs a standalone legal research memo analyzing authority on a point of law. Use `legal-research-memo` for that purpose and return to this skill once counsel has identified the authorities to apply.
- The user needs to build an element-by-element claim or liability chart. Use `claim-chart` for that purpose.
- No record materials exist and the section requires factual development — the skill cannot draft facts it has not been given; factual content must come from provided record items only.
- The matter is in a pre-litigation or counseling posture where no brief or submission is imminent — use a matter-assessment or contract-review skill as appropriate.

## Legal Safety Rules

- **Draft legal work product for attorney review. This is not legal advice.** The draft must be reviewed, revised, and approved by a licensed attorney before any reliance, filing, or transmission to any tribunal, party, or third party.
- **Never invent, assert, or guess any legal authority.** The skill does not know the current state of the law in any jurisdiction. Every legal proposition in the draft that requires supporting authority is marked `[citation needed]`. Every pinpoint — page number, paragraph, section — is marked `[pin cite needed]`. No case name, holding, quotation, or statutory text is supplied from the skill's background knowledge. These placeholders are the attorney's work to fill.
- **A quotation that is "almost right" is worse than a paraphrase.** If record language is provided verbatim, quote it exactly and pinpoint it to the source. If the skill is paraphrasing, it flags the passage: `[VERIFY: paraphrase — confirm exact language and record cite]`. Quotation marks are never placed around language that has not been confirmed from the actual source document.
- **Record fidelity is mandatory.** Every factual statement in the draft is tied to a provided record item (with a citation to the document and, where applicable, a page, line, paragraph, or Bates number) or is flagged `[VERIFY: record cite needed]`. The skill does not invent facts, fill gaps in the record, or assume what a document says.
- **Flag weak arguments honestly.** If a proposed argument appears weak, contradicted by the record, or strategically risky, the skill says so in the Drafting Notes and offers the attorney options. Dressing up a weak argument as solid briefing exposes the attorney to professional-responsibility risk.
- **The duty of candor to the court is the attorney's professional obligation.** The skill does not assess candor compliance, but it flags every argument it cannot substantiate from the provided record and authority, and it never drafts a statement the skill cannot support from the provided inputs.
- **Do not compute, state, or imply any deadline.** Use `[deadline verification required]` wherever a filing date, response period, or limitations period is relevant.
- **Treat all forum rules as unverified unless provided.** Format, length, citation style, and local-rule requirements must be confirmed from the pasted source material; the skill never asserts a court rule from background knowledge.
- **Treat governing law as `[verify jurisdiction]`.** The applicable standard of review, burden of proof, and legal test depend on forum-specific law that the attorney must confirm.
- **Preserve confidentiality and privilege.** Client-sensitive facts, privileged communications, and attorney work product must not be included in any reusable or shareable copy of this output.
- **Separate facts, assumptions, law, analysis, and verification items.** The Drafting Notes section makes these categories explicit so the attorney can assess each independently.
- **Filing without attorney review carries professional-responsibility exposure.** The output carries a "DRAFT FOR ATTORNEY REVIEW — DO NOT FILE UNREVIEWED" banner. This is not a formality; filing an AI-generated draft without verification of every citation, quotation, and factual statement creates serious professional risk.

## Workflow

1. **Confirm inputs.** Verify that matter identification, case theory, section type, and at least a summary of the record materials have been provided. If required inputs are missing, stop and request them. Do not proceed with fabricated or assumed inputs.

2. **Check for a witness-statement request.** If the section type is a witness statement or the request is to draft prose in a witness's voice, decline and route to `deposition-prep`. This skill never drafts in the witness's voice. State the reason and stop.

3. **Confirm written submission or oral argument posture.**
   - **Written submission:** develop the argument with full logical structure, topic sentences, transitions, and citation placeholders at every proposition.
   - **Oral argument preparation:** produce a leaner structure — lead with the strongest point, limit supporting points to the few most essential, omit extended citation development. Note the condensed format in the Drafting Notes.

4. **Theory-consistency check.** Confirm that the proposed section, as framed, is consistent with the stated case theory. If the proposed section contradicts or undermines the case theory, stop, flag the inconsistency explicitly, and ask the attorney to resolve it before drafting begins. Do not draft a section that cuts against the case theory without explicit attorney direction.

5. **Review forum rules and house style.** From the pasted local rules, standing orders, and style sample:
   - Note the applicable page or word limit, heading requirements, and citation format.
   - Flag any rule the skill cannot confirm from the provided material: `[CONFIRM: forum rule not verified — attorney to confirm]`.
   - Note the tone and register from the house style sample. If no sample was provided, flag the style choice: `[CONFIRM: no style sample provided — attorney to confirm draft register and heading format]`.

6. **Map the record to the section.** For each key fact the section will rely on, identify the record item and the specific page, line, paragraph, or Bates number. Flag every fact that lacks a confirmed record cite as `[VERIFY: record cite needed]`. Do not draft a factual statement you cannot pin to a provided source.

7. **Identify authority gaps.** For each legal proposition the section will advance, note the authority that counsel has provided and directed. For every proposition that lacks a directed authority, insert `[citation needed]` in the draft position and note the gap in the Drafting Notes. Do not add a case name, holding, quotation, or statutory text from background knowledge.

8. **Flag weak points before drafting.** If any proposed argument appears weak, contradicted by the record, unsupported by any directed authority, or potentially harmful to the case theory, note it in the Drafting Notes with a candid assessment and at least two attorney options: (a) pursue the argument with specified caveats, or (b) omit or reframe it. The attorney decides; the skill flags.

9. **Draft the section** applying four disciplines simultaneously:
   - **Record fidelity:** every fact carries a pinpointed record cite, verbatim quotations are exact and marked as such, and paraphrases are flagged `[VERIFY: paraphrase]`.
   - **Citation discipline:** every legal proposition has a citation placeholder — `[citation needed]` for the primary authority and `[pin cite needed]` for the pinpoint — and the attorney's directed authorities are placed in the correct logical position. The skill adds no authority beyond what counsel has provided.
   - **Candor about weak arguments:** weak points are flagged inline with a note — for example, `[NOTE TO ATTORNEY: this argument is not supported by the provided record — see Drafting Notes item 3]` — rather than papered over with confident prose.
   - **Echo, do not repeat:** reinforce the case theory and advance the argument; do not restate earlier sections of the brief verbatim. The section should carry the argument forward.

10. **Assemble the output** in the three-part format described below. Apply the banner to the Section Draft. List all placeholders and open items in the Attorney Verification Checklist.

## Output Format

Deliver the output in three clearly labeled parts:

---

### Part 1 — Drafting Notes (Internal Work Product)

An internal memo for the supervising attorney, organized as follows:

- **Section summary:** the argument or narrative the section advances and how it connects to the case theory.
- **Record items used:** a table or list of every record item cited in the draft, with the document identifier, description, and pinpoint location as provided.
- **Record gaps:** every factual proposition in the draft that lacks a confirmed record cite, listed with the `[VERIFY]` flag used in the draft.
- **Authority gaps:** every legal proposition that requires a citation, listed with the `[citation needed]` placeholder used in the draft and a brief statement of what type of authority is needed (e.g., "standard of review authority in the forum `[verify jurisdiction]`").
- **Weak points and options:** a candid assessment of any argument that appears weak, contradicted, or strategically risky, with the attorney's options stated plainly.
- **Forum-rule confirmations needed:** every local rule, length limit, or format requirement that could not be confirmed from the provided material.
- **Open questions for the attorney:** any threshold issue — theory consistency, scope of the section, strategic framing — that requires attorney resolution before the draft is finalized.

---

### Part 2 — Section Draft

> **DRAFT FOR ATTORNEY REVIEW — DO NOT FILE UNREVIEWED**
> *This section is draft legal work product. Every citation marked `[citation needed]` or `[pin cite needed]` must be supplied and verified by the supervising attorney. Every passage marked `[VERIFY]` must be confirmed against the source. This draft has not been reviewed for professional-responsibility compliance and must not be filed, transmitted, or relied upon until the supervising attorney has reviewed, corrected, and approved it.*

The brief section in the house style, with:

- Headings formatted per the pasted local rules and style sample (or flagged for confirmation if no sample was provided).
- Every fact cited to the record with the provided identifier and pinpoint, or flagged `[VERIFY: record cite needed]`.
- Every verbatim quotation marked as a direct quote with the source pinpointed; every paraphrase flagged `[VERIFY: paraphrase — confirm exact language]`.
- Every legal proposition followed by `[citation needed]` and, where pinpoint is required, `[pin cite needed]`.
- Weak arguments flagged inline: `[NOTE TO ATTORNEY: see Drafting Notes item ___]`.
- Standard of review stated with the applicable legal test as a placeholder: `[standard of review: [verify jurisdiction]]`.
- Forum-rule compliance flagged where unconfirmed: `[CONFIRM: page/word limit not verified]`.

---

### Part 3 — Attorney Verification Checklist

The checklist from the section below, pre-populated with the specific gaps identified in this draft (record cites, citation placeholders, and open items).

---

## Attorney Verification Checklist

- [ ] Case theory is accurately captured and the drafted section is consistent with it.
- [ ] Section type and scope are correct and approved by the responsible attorney.
- [ ] Written submission or oral argument posture confirmed; draft format matches posture.
- [ ] Forum rules confirmed: page or word limit, heading requirements, citation format, and any applicable local rules `[verify jurisdiction]`.
- [ ] House style confirmed; heading format and prose register approved.
- [ ] Every `[citation needed]` placeholder has been replaced with a verified, primary-source citation. No AI-generated citation has been accepted without checking it against the actual source.
- [ ] Every `[pin cite needed]` placeholder has been replaced with the correct page, paragraph, or section number confirmed from the source.
- [ ] Every verbatim quotation has been checked character-by-character against the original document or transcript. No quotation is "close enough."
- [ ] Every `[VERIFY: paraphrase]` passage has been confirmed or corrected against the source record item.
- [ ] Every `[VERIFY: record cite needed]` flag has been resolved: either a record cite has been supplied and confirmed, or the factual assertion has been removed or rewritten.
- [ ] Standard of review is correct for the motion type and forum `[verify jurisdiction]`.
- [ ] All weak points identified in the Drafting Notes have been assessed and the attorney has decided whether to pursue, reframe, or omit each one.
- [ ] All forum-rule confirmations flagged in the Drafting Notes have been resolved.
- [ ] No deadline has been stated or implied in the draft without `[deadline verification required]` having been resolved by the responsible attorney.
- [ ] Duty of candor to the court has been considered by the responsible attorney as to every argument advanced.
- [ ] All open questions from the Drafting Notes have been resolved before the draft is submitted for filing.
- [ ] Output is held in the appropriate client file and no confidential or privileged content has been shared outside the matter team.
- [ ] The responsible attorney has reviewed, revised, and approved the section and accepts professional responsibility for its contents before filing.
