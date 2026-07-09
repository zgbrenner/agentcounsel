---
name: Motion Opposition Drafter
description: "Use when organizing and drafting a DRAFT opposition or response brief to a pending motion — deconstructing the movant's arguments into a point-by-point response outline, mapping the movant's cited authorities to verification placeholders, and assembling a source-cited opposition draft for attorney review before filing."
practice_area: litigation
task_type: drafting
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The movant's motion, memorandum, and any supporting declarations or exhibits"
  - "The case theory and the client's position in opposition"
  - "The relevant record materials that support the opposition"
  - "The response deadline as stated on the docket or scheduling order"
outputs:
  - "Point-by-point response outline mapped to the movant's arguments"
  - "Draft opposition brief cited to the record and flagged for attorney verification"
  - "Authority-verification and research-referral list for every movant citation"
related_skills:
  - skills/litigation/brief-section-drafter/SKILL.md
  - skills/legal-research/legal-research-memo/SKILL.md
  - skills/legal-research/negative-treatment-check/SKILL.md
  - skills/litigation/litigation-chronology/SKILL.md
tags:
  - litigation
  - opposition-brief
  - motion-practice
  - drafting
  - record-citation
  - response-brief
---

# Motion Opposition Drafter

## Purpose

Produce a first draft of an opposition or response brief to a pending motion, for attorney review, revision, and sign-off. The skill deconstructs the movant's motion into its component arguments, builds a point-by-point response outline, and drafts opposition prose that answers each movant argument, cites only to the record materials the user has provided, and flags every one of the movant's cited authorities for attorney verification rather than accepting it at face value. It never invents counter-authority — where a response argument needs a case, statute, or rule the user has not supplied, the skill states the research need and routes it to a research skill. This is draft legal work product for attorney review; it is not legal advice. The draft is never filed unreviewed.

This skill does not decide litigation strategy, does not evaluate whether the movant is likely to prevail, and does not produce a final, file-ready document. It gives the supervising attorney a disciplined, honestly-flagged working draft of the opposition — not a shortcut around professional judgment about whether and how to fight the motion.

## Use When

- Counsel has received a motion (dispositive or non-dispositive — e.g., a motion to dismiss, motion for summary judgment, motion to compel, motion for sanctions, motion in limine, or similar) and needs a first-draft opposition or response brief.
- A user asks to "draft an opposition to this motion," "respond to their motion for summary judgment," "outline our response to the motion to dismiss," or "help me push back on this motion."
- The movant's motion papers and the record materials needed to answer it are available and can be provided as inputs.
- The matter is in active litigation, a motion has been filed against the client, and a response is due or anticipated.
- The draft is for a written opposition or response brief, or, with appropriate scope adjustment, a structured outline for oral argument in opposition to the motion.

## Required Inputs

- **Matter identification** — matter name, matter number, or a brief description sufficient to identify the case.
- **The movant's motion papers** — the motion itself, the supporting memorandum or brief, and any supporting declarations, affidavits, or exhibits. Without the full motion papers, the skill cannot deconstruct the movant's arguments and will stop to request them. A summary or description of the motion is not a substitute for the papers themselves.
- **Case theory and opposition position** — one sentence stating the client's position and the reason the motion should be denied or the relief refused. The draft turns on this sentence.
- **Record materials** — the documents, deposition transcripts, declarations, pleadings, or other record items that support the opposition. Every fact in the draft must be tied to a provided record item or flagged `[VERIFY: record cite needed]`. If no record materials are provided beyond the movant's own papers, the skill can still outline the response but will flag every factual counter-point as unsupported until record materials are supplied.
- **Response deadline** — the date stated on the docket, scheduling order, or local rule, exactly as the user states it. The skill never calculates this date from a filing date or a rule's stated period; it records what the user provides and flags it `[deadline verification required]`.
- **Forum and local rules** — the relevant local rules, standing orders, or page and word-count limits, pasted directly into the input. If not provided, the skill flags all format and length requirements as `[CONFIRM: forum rules not provided — attorney to verify]`.
- **Authorities already identified by counsel** — any cases, statutes, rules, or secondary sources the supervising attorney has already confirmed and directed the skill to use in response. The skill inserts these as placeholders in the proper locations; it does not add authority beyond what is provided and directed.
- **Standard of review** — the applicable standard as stated by counsel or as it appears in the movant's papers. The skill never supplies a standard of review from its own background knowledge; it treats the standard as `[CONFIRM: standard of review — verify jurisdiction]` unless the user directs otherwise.
- Optional: the practice group's `practice-profiles/litigation.md` if it has been populated and is loaded alongside this skill. If present, the skill benchmarks the draft against its Preferred Output Style and Standard Positions. If absent, the skill proceeds without practice-profile benchmarking.

If matter identification, the movant's motion papers, or the case theory is missing, stop and request the missing information before proceeding. Do not fabricate any input, and do not draft an opposition to a motion the skill has not been shown.

## Do Not Use When

- The user wants a first draft of an affirmative brief — a motion, a reply in support of the client's own motion, or another section not responding to an opposing party's motion. Use `skills/litigation/brief-section-drafter/SKILL.md` for affirmative brief sections; this skill is the opposition-side counterpart and answers a motion the other side filed.
- The user needs new legal research to find authority supporting the opposition — cases, statutes, or secondary sources the user has not already identified. Use `skills/legal-research/legal-research-memo/SKILL.md` to research the question, then return to this skill once counsel has identified the authorities to apply. This skill drafts around directed authority; it does not go find it.
- The user wants to know whether the movant's cited cases are still good law, have been reversed, or have received negative subsequent treatment. Use `skills/legal-research/negative-treatment-check/SKILL.md` for that citator-style analysis; this skill flags every movant citation for verification but does not perform the verification itself.
- The user needs a full factual chronology built from the record before the opposition can be drafted. Use `skills/litigation/litigation-chronology/SKILL.md` first, then return here with the chronology as a record material.
- No motion papers have been provided — the skill cannot deconstruct arguments it has not been shown, and will not draft an opposition from a description or summary of the motion.
- The matter is in a pre-litigation or counseling posture with no motion pending — use a matter-assessment or contract-review skill as appropriate.
- The user wants the skill to conclude how the court is likely to rule, whether the opposition will succeed, or what the motion's merits are as a matter of law. The skill organizes and drafts; it does not predict outcomes or weigh in on the correctness of the movant's legal position.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- **Never invent counter-authority.** The skill does not know the current state of the law in any jurisdiction and does not manufacture a case or statute to rebut the movant's position. Every response argument that needs supporting authority is marked `[citation needed]`, and where the gap is a genuine research need rather than a drafting gap, the skill states that explicitly and routes it: "This point requires legal research — see `skills/legal-research/legal-research-memo/SKILL.md`."
- **Every movant authority is a verification placeholder, never an accepted proposition.** For each case, statute, rule, or other authority the movant's papers cite, the draft records the citation as given and marks it `[VERIFY: confirm this citation, that it says what the movant claims, and its current treatment]`. The skill never assumes the movant's characterization of an authority is accurate, never assumes the authority remains good law, and never independently confirms it — that confirmation is attorney or research-skill work, most naturally through `skills/legal-research/negative-treatment-check/SKILL.md`.
- **Draft legal work product for attorney review. This is not legal advice.** The draft must be reviewed, revised, and approved by a licensed attorney before any reliance, filing, or transmission to any tribunal, party, or third party.
- **Treat the standard of review as user-supplied or unverified.** The applicable standard of review, burden of proof, and legal test for the motion type depend on forum-specific law. The skill records the standard exactly as the user states it or as `[CONFIRM: standard of review — verify jurisdiction]`; it never supplies a standard from background knowledge, and never assumes the movant's stated standard is correct.
- **Record fidelity is mandatory, and only to provided record materials.** Every factual statement responding to the motion is tied to a record item the user has actually provided (with a citation to the document and, where applicable, a page, line, paragraph, or Bates number) or is flagged `[VERIFY: record cite needed]`. The skill does not cite to, quote, or characterize any document it has not been given — including documents the movant's papers describe but the user has not supplied.
- **A quotation that is "almost right" is worse than a paraphrase.** If record language or movant-brief language is provided verbatim, quote it exactly and pinpoint it to the source. If the skill is paraphrasing, it flags the passage: `[VERIFY: paraphrase — confirm exact language and record cite]`.
- **Never mischaracterize the movant's argument.** Before responding to any argument, restate it accurately from the movant's own papers. If the skill is uncertain what the movant is arguing, it flags the ambiguity rather than guessing at a weaker version of the argument to knock down.
- **Flag weak counter-arguments honestly.** If a proposed response point appears weak, unsupported by the provided record, or strategically risky, the skill says so in the Drafting Notes and offers the attorney options. Dressing up a weak response as solid briefing exposes the attorney to professional-responsibility risk.
- **The duty of candor to the court is the attorney's professional obligation.** The skill does not assess candor compliance, but it flags every response argument it cannot substantiate from the provided record and directed authority.
- **Do not compute, state, or imply any deadline.** The response deadline, and any deadline referenced in the motion (e.g., a hearing date, a discovery cutoff the motion implicates), is recorded exactly as the user states it and flagged `[deadline verification required]`. The skill never calculates a deadline from a filing date, a rule's stated response period, or any other starting point.
- **Treat all forum rules as unverified unless provided.** Format, length, citation style, and local-rule requirements must be confirmed from the pasted source material; the skill never asserts a court rule from background knowledge.
- **Preserve confidentiality and privilege.** Client-sensitive facts, privileged communications, and attorney work product must not be included in any reusable or shareable copy of this output.
- **Separate facts, assumptions, law, analysis, and verification items.** The Drafting Notes section makes these categories explicit so the attorney can assess each independently.
- **Filing without attorney review carries professional-responsibility exposure.** The output carries a "DRAFT FOR ATTORNEY REVIEW — DO NOT FILE UNREVIEWED" banner. This is not a formality; filing an AI-generated opposition without verification of every citation, quotation, and factual statement — including every movant citation the draft merely flagged — creates serious professional risk.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/litigation.md` is loaded, its Preferred Output Style and Standard Positions inform the draft but never substitute for attorney judgment.

## Workflow

1. **Confirm inputs.** Verify that matter identification, the movant's full motion papers, and the case theory/opposition position have been provided. If required inputs are missing, stop and request them. Do not proceed with a fabricated or summarized version of the motion.

2. **Check for an affirmative-brief or research request.** If the user is actually asking for a first draft of the client's own motion or another affirmative section, decline and route to `brief-section-drafter`. If the user needs new authority located rather than directed authority applied, decline substantive research and route to `legal-research-memo`. State the reason and stop, or proceed only with the parts of the request this skill covers.

3. **Deconstruct the movant's motion.** Read the motion and memorandum and break it into its constituent arguments — typically one entry per numbered argument heading or per distinct legal proposition the movant advances. For each:
   - State the argument as the movant frames it, in the movant's own terms, with a pinpoint citation to the motion papers.
   - List every authority (case, statute, rule, regulation, or other source) the movant cites for that argument, recorded exactly as cited in the motion.
   - Note any factual assertion the movant makes in support, with a pinpoint citation to the movant's papers.
   - Do not paraphrase the movant's argument into a weaker form. If the argument's scope or theory is ambiguous, flag the ambiguity rather than resolving it in the client's favor.

4. **Mark every movant authority for verification.** For each authority identified in step 3, insert `[VERIFY: confirm citation, confirm it says what the movant claims, confirm current treatment]` beside it in the deconstruction. Do not assess, from background knowledge, whether the movant's characterization of any authority is accurate or whether the authority remains good law. Where the response will turn on whether a movant authority has been undermined by subsequent treatment, note in the Drafting Notes that this is a candidate for `skills/legal-research/negative-treatment-check/SKILL.md`.

5. **Build the point-by-point response outline.** For each movant argument from step 3, draft a corresponding response point:
   - The client's counter-position on that specific argument.
   - The record materials that support the counter-position, each with a pinpoint citation, or `[VERIFY: record cite needed]` where support is not yet provided.
   - The type of authority the response point will need (e.g., "authority distinguishing the movant's lead case on its facts," "authority stating the correct standard `[verify jurisdiction]`") — marked `[citation needed]` and, where it is a genuine research gap rather than directed authority counsel has not yet supplied as text, flagged for referral to `legal-research-memo`.
   - Any procedural response available (e.g., the motion is untimely, fails to meet a threshold requirement, or misapplies the standard of review) — each flagged for the applicable rule citation.

6. **Confirm standard of review and procedural posture.** Record the standard of review and burden of proof exactly as directed by counsel or as `[CONFIRM: standard of review — verify jurisdiction]`. Record the motion type, the procedural posture, and any threshold or timeliness issue that could dispose of the motion without reaching the merits, each cited to the docket or rules as provided.

7. **Review forum rules and house style.** From the pasted local rules, standing orders, and style sample — or, where loaded, `practice-profiles/litigation.md` — note the applicable page or word limit, heading requirements, and citation format, flagging anything not confirmed: `[CONFIRM: forum rule not verified — attorney to confirm]`.

8. **Flag weak points before drafting.** If any proposed response point appears weak, unsupported by the provided record, unsupported by any directed authority, or strategically risky, note it in the Drafting Notes with a candid assessment and at least two attorney options: (a) pursue the point with specified caveats, or (b) omit or reframe it.

9. **Draft the opposition** following the point-by-point outline, applying four disciplines simultaneously:
   - **Accurate characterization:** the movant's argument is restated fairly before it is answered.
   - **Record fidelity:** every fact carries a pinpointed record cite from provided materials only; quotations are exact and marked as such; paraphrases are flagged.
   - **Citation discipline:** every legal proposition in the response — and every movant authority discussed — carries the appropriate placeholder (`[citation needed]` / `[pin cite needed]` for the response's own authority, `[VERIFY: ...]` for every movant authority). The skill adds no authority beyond what counsel has directed.
   - **Candor about weak points:** weak response arguments are flagged inline, e.g., `[NOTE TO ATTORNEY: this response point is not supported by the provided record — see Drafting Notes item ___]`.

10. **Assemble the output** in the three-part format described below, using `templates/opposition-response-outline.md` to structure the deconstruction, verification list, and response outline, with the response deadline and every other date flagged `[deadline verification required]`.

## Output Format

Deliver the output in three clearly labeled parts:

---

### Part 1 — Drafting Notes (Internal Work Product)

- **Motion summary:** the motion type, relief sought, and procedural posture, cited to the movant's papers. Populate the header block and Sections 1–4 of `templates/opposition-response-outline.md`.
- **Argument deconstruction:** the movant's arguments as framed, each with its cited authorities and factual assertions, pinpointed to the motion.
- **Movant-authority verification list:** every authority the movant cited, each flagged `[VERIFY: confirm citation, characterization, and current treatment]`, with a note on which entries are candidates for `negative-treatment-check`.
- **Response outline:** the point-by-point counter-position map built in Workflow step 5.
- **Record gaps:** every response point that lacks a confirmed record cite, listed with the `[VERIFY]` flag used in the draft.
- **Authority gaps:** every response proposition that requires a citation, with a note on whether it is directed-authority-pending or a genuine research referral to `legal-research-memo`.
- **Standard of review and procedural posture:** as confirmed or flagged `[CONFIRM: standard of review — verify jurisdiction]`.
- **Weak points and options:** a candid assessment of any response argument that appears weak or unsupported, with the attorney's options stated plainly.
- **Forum-rule confirmations needed** and **open questions for the attorney**, as in `brief-section-drafter`.

---

### Part 2 — Opposition Draft

> **DRAFT FOR ATTORNEY REVIEW — DO NOT FILE UNREVIEWED**
> *This opposition is draft legal work product. Every citation marked `[citation needed]` or `[pin cite needed]` must be supplied and verified. Every movant authority marked `[VERIFY]` must be independently checked — its citation, its holding, and its current treatment — before the draft relies on any characterization of it. Every passage marked `[VERIFY]` for record fidelity must be confirmed against the source. This draft has not been reviewed for professional-responsibility compliance and must not be filed, transmitted, or relied upon until the supervising attorney has reviewed, corrected, and approved it.*

The opposition brief in the house style, with:

- A preliminary statement summarizing the client's opposition position.
- The standard of review stated as a placeholder: `[standard of review: [verify jurisdiction]]` unless counsel has directed otherwise.
- Each response point organized to track the movant's argument order (or a stated, attorney-approved reorganization), with the movant's argument fairly restated before it is answered.
- Every fact cited to the record with the provided identifier and pinpoint, or flagged `[VERIFY: record cite needed]`.
- Every movant authority discussed carrying `[VERIFY: confirm citation, characterization, and current treatment]`.
- Every response-side legal proposition followed by `[citation needed]` and, where needed, `[pin cite needed]`.
- Weak response arguments flagged inline: `[NOTE TO ATTORNEY: see Drafting Notes item ___]`.
- The response deadline and any other date referenced flagged `[deadline verification required]`.
- Forum-rule compliance flagged where unconfirmed: `[CONFIRM: page/word limit not verified]`.

---

### Part 3 — Attorney Verification Checklist

The checklist below, pre-populated with the specific gaps identified in this draft.

---

## Attorney Verification Checklist

- [ ] Case theory and opposition position are accurately captured and the drafted opposition is consistent with them.
- [ ] The movant's motion and every supporting paper, declaration, and exhibit were reviewed in full — not summarized or assumed.
- [ ] Every movant argument in the deconstruction accurately reflects what the movant's papers actually argue.
- [ ] Every `[VERIFY]` placeholder on a movant-cited authority has been resolved: the citation confirmed, the movant's characterization checked against the actual source, and current treatment confirmed (directly or via `negative-treatment-check`).
- [ ] Every `[citation needed]` placeholder for the opposition's own authority has been replaced with a verified, primary-source citation.
- [ ] Every `[pin cite needed]` placeholder has been replaced with the correct page, paragraph, or section number.
- [ ] Every verbatim quotation — from the record or from the movant's papers — has been checked character-by-character against the original.
- [ ] Every `[VERIFY: paraphrase]` passage has been confirmed or corrected against the source.
- [ ] Every `[VERIFY: record cite needed]` flag has been resolved: either a record cite has been supplied and confirmed, or the factual assertion has been removed or rewritten.
- [ ] Standard of review and procedural posture are correct for the motion type and forum. `[verify jurisdiction]`
- [ ] All weak points identified in the Drafting Notes have been assessed and the attorney has decided whether to pursue, reframe, or omit each one.
- [ ] All forum-rule confirmations flagged in the Drafting Notes have been resolved.
- [ ] The response deadline stated in this draft has been independently confirmed against the docket, scheduling order, and applicable rules — not accepted from this draft. `[deadline verification required]`
- [ ] Any research referral flagged for `legal-research-memo` has been completed and the resulting authority incorporated by the attorney, not the skill.
- [ ] Duty of candor to the court has been considered by the responsible attorney as to every argument advanced and every characterization of the movant's position and authorities.
- [ ] All open questions from the Drafting Notes have been resolved before the draft is submitted for filing.
- [ ] Output is held in the appropriate client file and no confidential or privileged content has been shared outside the matter team.
- [ ] The responsible attorney has reviewed, revised, and approved the opposition and accepts professional responsibility for its contents before filing.
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.
