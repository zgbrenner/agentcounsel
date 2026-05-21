---
name: Claim Chart
description: "Use when building an element-by-element claim chart — mapping patent claim limitations or the elements of a civil cause of action or affirmative defense against evidence — to produce a structured gap analysis for attorney review."
practice_area: litigation
task_type: analysis
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The patent claim, pleaded cause of action, or affirmative defense"
  - "The evidence to map against each element"
  - "The applicable jurisdiction"
outputs:
  - "Element-by-element claim chart with a structured gap analysis for attorney review"
related_skills:
  - skills/litigation/brief-section-drafter/SKILL.md
  - skills/litigation/litigation-chronology/SKILL.md
  - skills/litigation/privilege-log-review/SKILL.md
tags:
  - litigation
  - claim-chart
  - elements-analysis
  - patent
  - gap-analysis
---

# Claim Chart

## Purpose

Produce a structured, attorney-ready claim chart that maps discrete elements — either limitations of a patent claim or the required elements of a civil cause of action or affirmative defense — against the available evidence or accused features. The chart surfaces what is supported, what is partial, what is disputed, and where gaps remain. It is a draft analytical aid for attorney review, never a filed contention, never a conclusion on infringement or liability, and never a substitute for attorney judgment on any legal question it raises.

## Use When

- Counsel needs an element-by-element mapping of patent claim limitations against an accused product, system, or process (infringement analysis) or against prior art (invalidity analysis).
- Counsel needs the required elements of a civil cause of action or affirmative defense mapped against the evidence corpus to identify what is supported and what still needs to be developed.
- A matter is approaching a case-dispositive filing — summary judgment, trial preparation, or a pre-filing infringement analysis — and a structured gap analysis is needed before strategy decisions are made.
- Discovery is closing and counsel needs to audit which elements are evidentially supported and which require additional fact or expert development.
- A party is evaluating whether to assert or defend a claim and needs a preliminary map of the elements against available evidence before making that decision.

## Required Inputs

**For all modes:**

- Matter name and a one-line case theory (e.g., "Plaintiff contends Defendant's product infringes Claim 1; we are defending").
- Mode: **patent** (infringement or invalidity) or **civil** (cause of action or affirmative defense).
- Side: asserting or defending.
- Jurisdiction and court. If not provided, insert `[verify jurisdiction]` throughout and flag for attorney confirmation before proceeding.
- Phase: pleadings / discovery / summary judgment / trial preparation.
- Whether any documents were obtained via discovery or are subject to a protective order or other use restriction — a use-restriction check must be run before mapping begins.

**Patent mode — additional inputs:**

- The patent (text or key excerpts) and the specific asserted claim(s).
- Any claim-construction ruling, agreed constructions, or disputed terms. If none are provided, flag all potentially disputed terms as `[VERIFY: construction not confirmed]`.
- The accused product, system, or process description (for infringement) or the prior-art reference(s) (for invalidity).

**Civil mode — additional inputs:**

- The pleaded claim or defense as stated in the operative pleading.
- The controlling elements — from the jurisdiction's pattern jury instruction, approved jury charge, or governing statute. If not provided, insert `[ATTORNEY TO CONFIRM: elements source and governing authority — verify jurisdiction]` and do not proceed with mapping until the elements are confirmed.
- The evidence corpus: documents, deposition excerpts, declarations, expert reports, or other materials to be mapped.

If mode, side, or jurisdiction is not provided, stop and request them before proceeding. Do not begin mapping without confirmed controlling elements.

## Do Not Use When

- The user needs a conclusion on infringement, non-infringement, liability, or non-liability — that is an attorney determination; this skill produces a mapping, not a conclusion.
- The user needs claim construction resolved — flag all disputed claim terms and construction questions; do not resolve them. Claim construction is an attorney and court determination.
- The user needs to draft a brief, motion, or pleading section (use `brief-section-drafter`).
- The user needs a factual timeline or event chronology as a predicate step (use `litigation-chronology` first, then return to this skill).
- The chart would be filed or served as-is — the output of this skill is an internal analytical draft requiring attorney review before any portion is incorporated into a filed document.
- The matter is at a stage where a privilege log or document review is the primary need (use `privilege-log-review`).

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice and must not be treated as a legal conclusion.
- The claim chart is an internal analytical aid. It must not be filed, served, or produced without attorney review and authorization. Label every output "Privileged & Confidential — Attorney Work Product."
- Do not conclude on infringement, non-infringement, validity, invalidity, liability, or non-liability. State mappings as analytical characterizations — supported, partial, disputed, gap, or needs-evidence — not as legal determinations.
- Do not resolve disputed claim constructions or disputed element definitions. Flag them with `[VERIFY: disputed construction — attorney to confirm]` and leave them open for attorney and, where applicable, court determination.
- Do not invent, fabricate, or extrapolate evidence. Every mapping entry must tie to a specific passage in a provided document or material, with a verbatim quote and a pinpoint cite. Where evidence is thin or ambiguous, use "needs-evidence" — never silently fill a gap.
- Every mapping is a lead the attorney must verify against the source. Model background knowledge about products, technologies, or legal standards is unverified and must not be treated as a substitute for documentary evidence.
- Run a use-restriction check before beginning: if any material was produced in discovery under a protective order or is otherwise use-restricted, flag those documents and note the restriction before incorporating them into any analysis.
- Do not assert governing statutes, regulations, case names, or rule numbers. The controlling elements and authority come from the jurisdiction and are always `[verify jurisdiction]`. Never name a specific legal authority.
- For invalidity analysis, note — without asserting legal authority — that the burden of proof for invalidity is heightened compared to other civil standards; `[ATTORNEY TO CONFIRM: applicable burden and standard — verify jurisdiction]`.
- Distinguish facts (from evidence), assumptions, analysis (the mapping), strategy (attorney judgment), and open verification items. Keep these categories separate within the output.
- Flag every uncertainty rather than resolving it. Use `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[citation needed]`, `[pin cite needed]`, `[verify jurisdiction]`, and `[deadline verification required]` as appropriate.
- Preserve confidentiality and privilege. Keep client-sensitive facts out of any reusable copy of the template.

## Workflow

1. **Confirm inputs.** Verify that all required inputs for the selected mode are present. If mode, side, jurisdiction, or the controlling elements are missing, stop and request them. Do not begin mapping until the elements list is confirmed.

2. **Jurisdiction and posture check.** Record the jurisdiction, court, phase, and side. Insert `[verify jurisdiction]` wherever the applicable legal standard, burden, or procedural rule is referenced. Note the case theory in one line.

3. **Use-restriction check.** Before mapping any document, confirm whether it was produced in discovery or is subject to a protective order or confidentiality designation. Flag any use-restricted material with a note: `[VERIFY: use restriction — attorney to confirm permissible use in this context]`. Do not incorporate use-restricted material into the chart without attorney clearance.

4. **Parse elements.**
   - **Patent mode:** Parse the asserted claim(s) limitation by limitation. Number each limitation sequentially. Preserve the verbatim claim language — do not paraphrase. Identify any term for which a construction ruling or agreed construction exists and record it. Flag all other potentially disputed terms as `[VERIFY: construction not confirmed — attorney to advise]`.
   - **Civil mode:** List the required elements of the cause of action or affirmative defense in the sequence established by the controlling source (pattern jury instruction, approved charge, or governing statute). Record the source as `[ATTORNEY TO CONFIRM: elements source — verify jurisdiction]`. Do not determine the elements yourself; use only what has been provided or confirmed.

5. **Flag construction and element-definition questions.** Before mapping, identify terms or elements whose scope is disputed or ambiguous. List them separately. Do not resolve any disputed construction — preserve all open questions for attorney determination.

6. **Map each element against the evidence.** For each element or limitation, search the provided materials and record:
   - A verbatim quote from the most probative passage, with a pinpoint cite (document name, page, paragraph, or bates number). Mark any paraphrase as `[VERIFY: paraphrase — pin cite needed]`.
   - A mapping state, chosen from: **Supported** (evidence directly addresses the element), **Partial** (evidence addresses the element in part but not completely), **Disputed** (evidence exists on both sides), **Gap** (no evidence found for this element), or **Needs-evidence** (the element cannot be assessed without further discovery, production, or expert input).
   - Never silently extrapolate from thin or ambiguous evidence. Use "needs-evidence" rather than forcing a "supported" characterization from insufficient material.

7. **Patent-specific passes (patent mode only).**
   - **Doctrine-of-equivalents pass:** For each limitation not literally met, note whether a doctrine-of-equivalents theory may be available. Record the function, way, and result for the accused feature if the evidence permits. Flag each such entry as `[ATTORNEY TO CONFIRM: equivalents analysis — attorney judgment required]`. Do not conclude that equivalents are or are not met.
   - **Indirect and divided infringement flag:** If the accused conduct may involve divided infringement (multiple actors) or induced or contributory infringement, flag those limitations as `[ATTORNEY TO CONFIRM: indirect or divided infringement — attorney judgment required]`. Do not conclude on any such theory.
   - **Invalidity burden note:** If the chart is for invalidity, include a general note — without citing authority — that the applicable burden of proof for invalidity is heightened; `[ATTORNEY TO CONFIRM: applicable standard — verify jurisdiction]`.

8. **Gap detection.** After completing the mapping, compile a gap list: every element or limitation in a "Gap" or "Needs-evidence" state, with a note of what type of evidence, witness, document, or expert input would be needed to address it. Also list any element where the mapping depends on a disputed construction that has not been resolved.

9. **Assemble the output.** Populate `templates/claim-chart-table.md`. Retain all placeholders. Label the output "Privileged & Confidential — Attorney Work Product — Draft for Attorney Review." Compile the attorney verification checklist.

10. **Label and deliver.** Deliver the chart with a clear statement that every mapping is a lead requiring attorney verification against the source, that no legal conclusion has been drawn, and that the chart must not be filed or served without attorney review and authorization.

## Output Format

Deliver a labeled draft comprising:

1. **Intake summary** — matter, case theory, mode, side, jurisdiction and court, phase, elements source, use-restriction check result, and any flagged construction questions. Label "Privileged & Confidential — Attorney Work Product."
2. **Claim chart** — the element-by-element mapping table, populated from `templates/claim-chart-table.md`, with verbatim quotes, pinpoint cites, mapping states, and notes for attorney review. Retain every placeholder.
3. **Gap list** — a consolidated table of all "Gap" and "Needs-evidence" elements, what is needed to address each, and any elements dependent on unresolved construction questions.
4. **Patent-specific flags (patent mode only)** — doctrine-of-equivalents leads and any indirect or divided infringement flags, each marked for attorney judgment.
5. **Attorney Verification Checklist** — every item requiring attorney review before any portion of the chart is relied upon or incorporated into a filed document.

## Attorney Verification Checklist

- [ ] Jurisdiction, court, governing law, and phase confirmed.
- [ ] The controlling elements (civil mode) or the asserted claim limitations (patent mode) have been confirmed by attorney against the authoritative source.
- [ ] Use-restriction check completed; no use-restricted materials have been incorporated without attorney clearance.
- [ ] All disputed claim terms or element definitions have been flagged and none have been silently resolved.
- [ ] Every mapping entry has been verified against the source document; no entry is based on model background knowledge or extrapolation.
- [ ] All verbatim quotes are accurate; all paraphrases are flagged `[VERIFY]`.
- [ ] Pinpoint cites are complete and accurate for every mapping entry.
- [ ] No mapping state has been overstated; thin or ambiguous evidence is recorded as "needs-evidence," not "supported."
- [ ] The gap list is complete; attorney has reviewed what additional discovery, expert input, or construction resolution is needed.
- [ ] Doctrine-of-equivalents leads (patent mode) have been reviewed by attorney; no equivalents conclusion has been drawn by the agent.
- [ ] Indirect and divided infringement flags (patent mode) have been reviewed by attorney.
- [ ] Invalidity burden note (patent mode, invalidity) confirmed as accurate for the applicable jurisdiction.
- [ ] No legal conclusion on infringement, non-infringement, validity, invalidity, liability, or non-liability appears in the chart.
- [ ] No statute-section number, case name, court-rule number, or named doctrine has been asserted as authority.
- [ ] The chart is labeled as a draft for attorney review and has not been filed, served, or produced.
- [ ] Any portion of the chart to be incorporated into a filed document has been reviewed, revised as needed, and authorized by the responsible attorney of record.
