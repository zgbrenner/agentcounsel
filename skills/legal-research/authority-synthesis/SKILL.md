---
name: Authority Synthesis
description: "Use when synthesizing a rule statement from multiple judicial opinions (and, where relevant, statutory or secondary sources) for a single Question Presented, producing a structured synthesis with explicit majority-and-minority handling, a temporal-confidence pass for older authority, and a Holding / Relevance / Weight block per authority — capped at the smallest set that supports the rule."
practice_area: legal-research
task_type: research
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The Question Presented the synthesis answers"
  - "The set of authorities (cases, statutes, regulations, secondary sources) to be synthesized"
  - "The applicable jurisdiction"
  - "The relevant date for the analysis"
outputs:
  - "Rule-synthesis worksheet with authority blocks, majority / minority split, and temporal-confidence flag, for attorney review"
related_skills:
  - skills/legal-research/legal-research-memo/SKILL.md
  - skills/legal-research/case-brief/SKILL.md
  - skills/legal-methodology/source-validation/SKILL.md
tags:
  - legal-research
  - authority-synthesis
  - rule-synthesis
  - case-law
  - citations
---

# Authority Synthesis

## Purpose

Synthesize a **rule statement** from multiple authorities for a single Question Presented. The output names the rule the authorities support, surfaces majority and minority lines explicitly, applies a *temporal-confidence pass* that downgrades the synthesis when the supporting authority is old or uncorroborated by recent decisions, and records each authority in a fixed Holding / Relevance / Weight block. It produces draft legal work product for attorney review; it is not legal advice, and it does not determine whether the synthesized rule binds the operative forum.

The most important disciplines this skill enforces:

- **The rule statement matches what the authorities actually say.** Synthesized rules that smooth over disagreement among authorities, ignore narrower holdings, or import dicta as rule are flagged and corrected before output.
- **Majority and minority lines are named separately.** A synthesis that presents only the supporting line and omits a meaningful minority position is a confirmation-bias failure; the skill explicitly searches the input set for contradicting authority and surfaces it.
- **Temporal confidence is a first-class output.** If the supporting authorities are concentrated in older cases without recent corroboration, the synthesis downgrades confidence and instructs the attorney to verify whether the rule has shifted.
- **Authority count is capped per issue.** A synthesis citing every case in the input set rather than the cases that actually support the rule is citation padding; the skill caps the per-Question authority set at the smallest that supports the synthesis and routes the remainder to the appendix or to attorney follow-up.

## Use When

- A Question Presented has surfaced multiple authorities (cases, statutes, regulations, secondary sources) and the rule across them must be stated before the result is written into a memo.
- A `legal-research-memo` Discussion section requires a rule statement and the rule is not stated in one authority but emerges from several.
- A litigation team has a set of cases on a doctrine and needs the rule synthesized before drafting a brief section.
- An advisory matter requires a rule statement that fairly accounts for split authority.
- A workflow has produced multiple case briefs (via `case-brief`) and the next step is to synthesize their holdings into a rule.

## Required Inputs

- **The Question Presented** — the discrete legal question the synthesis answers, framed as in `legal-research-memo` or `research-plan`.
- **The set of authorities** — the cases, statutes, regulations, and secondary sources to be synthesized. Each authority must be provided as either (a) a `case-brief` output, (b) the verbatim text of the source (statute, regulation, treatise excerpt), or (c) a verified link the skill can read (e.g., a `connectors/courtlistener.md` URL). The skill **does not synthesize from background knowledge**; every authority must be in the session.
- **Jurisdiction and forum** — the operative forum whose law governs. If unknown, flag as `[CONFIRM: jurisdiction]` and either stop or proceed with explicitly jurisdiction-conditional rule statements.
- **The relevant date** — the date on which the legal question turns (e.g., the date of conduct, the date of filing). Required for the temporal-confidence pass.
- Optional: **prior synthesis or analysis** the attorney wants the new synthesis to confirm, refine, or contradict. The skill will run the new synthesis independently and then compare.

If the Question Presented, the authority set, the jurisdiction, or the relevant date are missing, stop and request them. Do not synthesize from authorities the skill remembers but cannot read in the session.

## Do Not Use When

- The synthesis is from a single case — use `case-brief` instead and let the Rule slot do the work.
- No authorities have been gathered yet — use `research-plan` to scope, then locate authorities, then return.
- The task is a full memo — use `legal-research-memo`, which consumes a synthesis as input.
- The task is to verify that authorities exist or that quotations are accurate — use `legal-methodology/source-validation`.
- The task is to apply the synthesized rule to a specific set of facts to produce a result — the synthesis is the input to that step; the application belongs in `legal-research-memo` or a brief section.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Every rule fragment, holding statement, and paraphrase in the synthesis traces to a pinpoint passage in a provided authority. No quotation appears in the synthesis unless it has been verified verbatim against the source.
- Produce draft legal work product for attorney review. This is not legal advice and is not a determination of how the synthesized rule applies to any matter.
- **Do not synthesize from memory.** If an authority is not provided in the session — as a `case-brief`, as verbatim text, or as a connector-readable URL — the authority is excluded from the synthesis. The skill does not fill the rule from background knowledge of unprovided cases.
- **Adversarial-jurisprudence pass.** After drafting the rule, the skill explicitly searches the input authority set for contradicting authority — circuit splits, dissents, recent reversals, minority positions, secondary critiques — and records every contradiction it surfaces. A synthesis that has not run this pass is flagged incomplete.
- **Temporal-confidence pass.** After drafting the rule, the skill checks the dates of the supporting authorities. Where the most recent supporting authority is more than three years old and no recent corroborating authority is in the input set, the synthesis downgrades confidence and adds a `[VERIFY: temporal — confirm rule has not shifted; date-filtered recent search not in scope of this synthesis]` flag. The skill does not run a fresh search; it flags the need.
- **Majority and minority are separate sections.** A meaningful minority position from any provided authority is surfaced as a Minority Line block, not absorbed into the rule statement. The skill does not characterize the minority as "incorrect"; it records it.
- **Dicta vs. holding.** Synthesis cites holdings, not dicta. Where a passage is dicta in its source authority, the synthesis labels it as dicta and does not state the dicta as rule.
- **Consult `connectors/` when a verification path is available.** When the session has access to `connectors/courtlistener.md` and a case authority is in scope, confirm the citation form for each authority before it enters the synthesis. A confirmed citation closes "does this case exist with this citation"; it does not confirm "does it support this proposition" — that remains attorney work.
- **Cap authority count per issue.** The synthesis cites the smallest set of authorities that supports the rule statement, the majority position, and the minority position. Additional authorities from the input set are routed to an Appendix block as "additional authorities reviewed" — recorded but not cited in the rule statement itself. The default cap per Question is five authorities in the main rule statement (any cap deviations are flagged and explained).
- **Authority weight is on its face.** Each authority is recorded with its issuing court, date, and precedential level on its face; binding-vs-persuasive in the operative forum is `[verify jurisdiction]` and is an attorney determination.
- Use `[CONFIRM: ...]` and `[VERIFY: ...]` placeholders for any synthesis element whose support is unsettled.

## Workflow

1. **Confirm inputs.** Verify the Question Presented, the authority set, the jurisdiction, and the relevant date are provided. If any required input is missing, stop and request it.

2. **Catalog the authorities.** Read each provided authority (case brief, verbatim text, or connector-readable URL). Record its issuing court, date, citation form, and what it stands for *as the authority itself states it*. Authorities not provided in the session are excluded from the synthesis.

3. **Per-authority Holding / Relevance / Weight block.** For each authority, produce a short block: **Holding** (one to two sentences, pinpoint cited); **Relevance** (one sentence tying the holding to the Question Presented); **Weight** (issuing court, date, precedential level on its face). This is the same structure as `case-brief`'s output but condensed; if a `case-brief` has already been produced, the synthesis pulls from it directly.

4. **Connector verification.** For each case authority in scope, confirm citation form via `connectors/courtlistener.md`. Record the verified URL alongside the block. For authorities out of scope or with no connector access, retain a `[VERIFY-CITE: ...]` flag.

5. **Draft the rule statement.** Synthesize the rule that the supporting authorities, as written, actually support. State it as narrowly as the authorities support and no more broadly. Pinpoint each rule fragment to the authority block that supports it.

6. **Adversarial-jurisprudence pass.** Reread the input authority set and surface every contradiction: circuit splits, dissents, narrower holdings, qualifying language, secondary critiques. Record each as a **Minority Line** block, with its own Holding / Relevance / Weight. If the input set contains no contradiction, state that explicitly and add `[VERIFY: search for contradicting authority — not in scope of this synthesis]` so the attorney knows the synthesis did not search beyond the provided set.

7. **Temporal-confidence pass.** Identify the most recent supporting authority. If the most recent supporting case is more than three years before the relevant date (or before today, if the relevant date is contemporaneous), downgrade the synthesis confidence to "Tentative" and add the `[VERIFY: temporal — confirm rule has not shifted]` flag. Note the most recent supporting date and any anomalies.

8. **Cap the authority count.** Identify the smallest set of authorities that supports the rule statement and the minority position. Move authorities outside that set to an Appendix block as "additional authorities reviewed." Note any cap deviations.

9. **Note jurisdictional scope.** State explicitly which jurisdictions the supporting authorities are from and whether the synthesis is tied to one forum or holds across forums. Where the input set spans multiple jurisdictions, surface forum splits as their own minority blocks.

10. **List assumptions.** Note every assumption (jurisdiction, scope of synthesis, exclusion of out-of-session authorities, etc.).

11. **List open items for attorney verification.** Enumerate every `[CONFIRM: ...]`, `[VERIFY: ...]`, and `[verify jurisdiction]` placeholder, plus the temporal-confidence flag and any cap deviations.

12. **Assemble the synthesis** and label it as a draft for attorney review.

## Output Format

A rule-synthesis worksheet with the following sections, in order:

1. **Header** — Question Presented, operative jurisdiction, relevant date, privilege designation.
2. **Rule Statement** — the synthesized rule, pinpoint cited to authority blocks below. State the rule as narrowly as the authorities support.
3. **Authority Blocks** — one per authority cited in the rule statement, in Holding / Relevance / Weight form, with verified URL where available. Capped per the discipline above.
4. **Majority Line** — short note describing the majority position and which authority blocks comprise it.
5. **Minority Line(s)** — one block per meaningful minority or split, with its own Holding / Relevance / Weight.
6. **Forum / jurisdictional scope** — explicit statement of which jurisdictions the synthesis covers.
7. **Temporal-confidence note** — most recent supporting date; "Tentative" flag if the supporting authority is older than three years without recent corroboration in the input set.
8. **Adversarial-jurisprudence note** — explicit statement of whether the input set contained contradicting authority, and a `[VERIFY: ...]` flag if the search was confined to the input set.
9. **Appendix — additional authorities reviewed** — authorities read but not cited in the rule statement.
10. **Assumptions** — explicit list.
11. **Open items / Attorney verification** — checklist.

## Attorney Verification Checklist

- [ ] Every authority cited in the rule statement exists with the citation form recorded (connector-verified where possible).
- [ ] The rule statement is stated no more broadly than the supporting authorities allow.
- [ ] Dicta has been distinguished from holding in every authority block.
- [ ] Majority and minority lines are separate; no minority position has been absorbed into the rule statement.
- [ ] The adversarial-jurisprudence pass has been run against the input set, and the `[VERIFY: ...]` flag has been resolved — either by a fresh search outside the input set, or by attorney confirmation that the input set was complete.
- [ ] The temporal-confidence pass has been run; if the synthesis was downgraded to "Tentative," the rule has been confirmed against recent authority or the synthesis has been revised.
- [ ] The jurisdictional scope of the synthesis matches the operative forum, or any forum mismatch has been resolved.
- [ ] The authority cap has not omitted authority the attorney considers necessary; the Appendix has been reviewed for anything material.
- [ ] All `[CONFIRM: ...]` and `[VERIFY: ...]` placeholders have been resolved before the synthesis is relied upon.
- [ ] The synthesis is approved as the rule statement for downstream memo or brief work, or revised before reliance.
