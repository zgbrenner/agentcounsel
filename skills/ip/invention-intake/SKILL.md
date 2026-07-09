---
name: Invention Disclosure Intake
description: "Use when a user wants a structured first-pass screen of a proposed invention to assess whether it warrants patent-counsel attention, with filing-deadline urgency flagging."
practice_area: ip
task_type: intake
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The proposed invention disclosure"
  - "The disclosure and publication history"
  - "Any known commercialization or filing timeline"
outputs:
  - "Invention screen with a verdict and a filing-deadline urgency flag for patent counsel"
related_skills:
  - skills/ip/fto-triage/SKILL.md
tags:
  - ip
  - patent
  - invention-disclosure
  - intake
  - filing-deadline
---

# Invention Disclosure Intake

## Purpose

Produce a structured first-pass invention disclosure screen that helps patent counsel quickly orient to a proposed invention, identify obvious patentability signals, and flag any urgent filing-deadline concerns. This is draft legal work product for attorney review. It is NOT a patentability opinion, NOT a prior-art search, and does NOT constitute a legal finding that any invention is patentable or patent-eligible.

## Use When

- A user presents a new invention and asks whether it is worth pursuing a patent.
- An engineer, product team, or inventor needs a structured disclosure captured before meeting with patent counsel.
- A user wants to understand whether public-disclosure timing creates an urgent filing concern.
- A user needs a first-pass triage to decide whether to commission a formal patentability search and opinion.
- A user wants a structured intake document to brief patent counsel efficiently.

## Required Inputs

The following information is needed to run the screen. Provide either a full written disclosure document that covers these points, or answers to each intake question individually.

- **Technical essence**: what the invention does and how it works, in plain language.
- **Problem solved**: the technical or practical problem the invention addresses, and why existing approaches fall short.
- **Points of distinction**: how the invention differs from known prior approaches — in the inventor's own words, without legal characterization.
- **Inventors and conception date**: names of all individuals who contributed to the inventive concept, and the date (or approximate date) the invention was first conceived. `[CONFIRM: conception date with each named inventor]`
- **Public-disclosure history**: any public disclosures already made — including conference presentations, papers, preprints, product launches, trade-show demonstrations, press releases, social media posts, open-source commits, or any disclosure not protected by a non-disclosure agreement — with dates and venues. If all disclosures were made under NDA, confirm the NDA was in place before disclosure. `[CONFIRM: whether any disclosure was made without NDA coverage]`
- **Usage and commercialization status**: whether the invention is already in a shipped product, a limited pilot, on the product roadmap, or described only internally or in a publication.
- **Technical area**: the general field or domain (e.g., software, mechanical, biotech, chemical, electrical) to help route the disclosure to the right specialist.

If a disclosure document or answers to the above questions are not provided, stop and request them. Do not proceed on a partial or half-disclosure; an incomplete intake produces an unreliable screen.

## Do Not Use When

- The user wants a formal patentability opinion — that requires a registered patent professional conducting a prior-art search and rendering a legal opinion.
- The user wants a prior-art search conducted — this skill does not search patent databases or technical literature.
- The user needs patent claims drafted — claim drafting is attorney work and must not be performed by this skill.
- The user needs a freedom-to-operate analysis — whether the product can be made, used, or sold without infringing existing patents is a separate, specialized inquiry (use `fto-triage`).
- The matter involves trademark, copyright, or trade-secret issues as the primary IP concern — those are outside the scope of this intake.
- The invention has already been publicly disclosed without NDA and there is reason to believe the filing-deadline clock has run — route immediately to patent counsel rather than completing this screen.

## Legal Safety Rules

- This screen is draft legal work product for attorney review. It is NOT a patentability opinion and NOT legal advice. Patent counsel must review and sign off before any reliance on this output.
- Do not assert that an invention "is patentable," "is novel," "is non-obvious," or "is patent-eligible." The most this screen can conclude is that the invention passes initial signals and warrants further investigation by counsel.
- Do not compute, estimate, or assert any filing deadline. Filing deadlines depend on jurisdiction-specific rules, the nature and date of any public disclosure, and facts that must be verified by patent counsel. Always flag deadline questions as `[deadline verification required]`.
- Do not invent prior art, cite specific patents or publications as blocking art, or assert that no prior art exists. No prior-art search is conducted as part of this workflow.
- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available. Do not name or apply specific statutes, code sections, regulations, or case law — standards for novelty, non-obviousness, subject-matter eligibility, and filing deadlines vary by jurisdiction and are always `[verify jurisdiction]`. Treat all model background knowledge about patent law, grace periods, and eligibility doctrine as unverified.
- Separate facts provided by the user from analytical observations and from items requiring attorney or specialist verification.
- Flag every uncertainty with `[CONFIRM: ...]`, `[VERIFY: ...]`, or `[ATTORNEY TO CONFIRM: ...]` rather than resolving it silently.
- Preserve confidentiality and privilege. Keep client-identifying details and invention specifics out of any reusable or shared template context.
- If disclosure-timing signals suggest the filing-deadline clock may already be running or may have expired, flag this prominently as `[deadline verification required]` and recommend immediate patent-counsel engagement before completing the rest of the screen.

## Workflow

1. **Orient and disclaim.** Open the screen output with a clear statement that this is a first-pass invention disclosure screen, not a patentability opinion, and that no prior-art search has been conducted. Identify the date the screen is being run.

2. **Confirm inputs are complete.** Verify that all required inputs have been provided. If any are missing or ambiguous — particularly conception date and public-disclosure history — stop and request the missing information. Do not proceed on a partial disclosure. Record the inputs exactly as provided; do not paraphrase the technical description.

3. **Screen 1 — Novelty signals.** Based solely on the disclosure provided, identify whether there are self-evident novelty problems — for example, whether the inventor's own description suggests the idea has been previously published or is already in the public domain. This is not a prior-art search. Note signals only; do not conclude that novelty is present or absent. Apply `[verify jurisdiction]` to any jurisdiction-specific novelty standard referenced.

4. **Screen 2 — Non-obviousness signals.** Assess whether the disclosed invention reads, on its face, as a predictable combination or straightforward extension of approaches the inventor themselves describes as known. Flag combinations that may face non-obviousness scrutiny without asserting a legal conclusion. Apply `[verify jurisdiction]` to the applicable standard.

5. **Screen 3 — Subject-matter eligibility signals.** Identify whether the technical area or the manner in which the invention is described raises eligibility concerns (e.g., software-implemented inventions, mathematical methods, diagnostic or therapeutic methods, natural phenomena). Flag close or hard-to-call eligibility questions explicitly and note that close calls require specialist review. Apply `[verify jurisdiction]` to any eligibility doctrine referenced; eligibility rules vary substantially by jurisdiction and by the nature of the claimed subject matter.

6. **Screen 4 — Public-disclosure and filing-deadline signals (TIME-CRITICAL).** Review the public-disclosure history. If any public disclosure has occurred — even one that the inventor believes is covered by a grace period — flag `[deadline verification required]` and note that:
   - Some jurisdictions require absolute novelty and permit no pre-filing public disclosure.
   - Grace-period availability, scope, and duration vary by jurisdiction and disclosure type and must be verified by patent counsel.
   - Filing deadlines are not computed or estimated by this screen.
   - If disclosure timing is implicated, recommend immediate patent-counsel engagement before any other action. This flag should appear prominently in both the screen-results table and the bottom-line verdict.

7. **Screen 5 — Detectability.** Assess, based on the technical description, whether potential infringement of a patent covering this invention would be detectable from publicly observable products, services, or conduct. Note that low detectability is a factor that counsel may weigh in a patent-versus-trade-secret strategy discussion; this screen does not make that strategic call.

8. **Screen 6 — Strategic value signals.** Note any signals in the disclosure that bear on the invention's strategic importance — for example, whether it appears to be core to a product, whether it is in a crowded or fast-moving technical area, whether it has apparent licensing potential, or whether it addresses a significant competitive differentiation. This is a preliminary observation for counsel; no business judgment is rendered.

9. **Emit the bottom-line verdict.** Assign one of three verdicts:
   - **Pursue** — the disclosure passes all six screens without obvious disqualifying signals and warrants engagement of patent counsel for a formal patentability search and opinion.
   - **Investigate** — the disclosure raises one or more signals that require clarification or specialist input before a patentability search is warranted.
   - **Decline** — the disclosure shows clear and obvious barriers that make patent protection unlikely or inappropriate, in the screen's preliminary assessment.

   If any disclosure-timing concern was identified in Screen 4, add a prominent **TIME-SENSITIVE** flag to the verdict regardless of the overall verdict category.

10. **List open questions.** Enumerate all factual gaps, ambiguities, or points requiring confirmation that could affect the screen result.

11. **List next steps.** Recommend concrete actions — such as engaging patent counsel, clarifying the disclosure, or resolving deadline questions — ordered by urgency.

12. **Assemble and label the output.** Compile the full draft screen per the Output Format below, labeled as a first-pass draft for attorney review.

## Output Format

Deliver the following sections in order, under a header stating: *"DRAFT — Invention Disclosure Screen — For Patent Counsel Review — Not a Patentability Opinion — No Prior-Art Search Conducted."*

**1. Screen Summary**
- Invention title or short descriptor (as provided).
- Inventors and conception date (as provided; flag `[CONFIRM: ...]` if uncertain).
- Technical area.
- Date screen conducted.
- Bottom-line verdict: **Pursue / Investigate / Decline** — with `[TIME-SENSITIVE — deadline verification required]` if any disclosure-timing concern was identified.

**2. Disclosure Under Screen**
- The invention description as provided, reproduced verbatim or with minimal paraphrase for clarity, clearly identified as the source material for the screen. Do not editorialize or reframe the technical description.

**3. Screen Results**

Present as a table with four columns: **Screen**, **Verdict Signal** (Pass / Flag / Unclear), **Note**, and **Verification Required**.

| Screen | Verdict Signal | Note | Verification Required |
|---|---|---|---|
| 1. Novelty signals | | | |
| 2. Non-obviousness signals | | | |
| 3. Subject-matter eligibility signals | | | |
| 4. Public-disclosure / filing-deadline signals | | | |
| 5. Detectability | | | |
| 6. Strategic value signals | | | |

Each "Note" cell should contain a single concise observation. Each "Verification Required" cell should reference the applicable placeholder (`[verify jurisdiction]`, `[deadline verification required]`, `[CONFIRM: ...]`, etc.).

**4. Open Questions**
- Bulleted list of factual gaps, ambiguities, and unresolved inputs, each labeled with the responsible party for resolution (inventor, counsel, or business stakeholder).

**5. Next Steps**
- Numbered list of recommended actions, ordered by urgency. If Screen 4 raised a disclosure-timing concern, the first next step must be immediate patent-counsel engagement.

**6. Assumptions**
- All facts assumed or inferred from context, clearly distinguished from facts stated by the user.

**7. Attorney Verification Items**
- Bulleted list of items patent counsel must confirm or resolve before the screen result can be relied upon for any decision.

## Attorney Verification Checklist

- [ ] The invention description is complete and accurately reflects the full scope of the inventive concept; no material details have been omitted.
- [ ] All inventors have been identified and the conception date confirmed with each named inventor.
- [ ] The public-disclosure history has been verified in full, including whether any disclosure was made without NDA coverage.
- [ ] Filing deadlines have been assessed by patent counsel based on verified disclosure dates and applicable jurisdiction-specific rules — `[deadline verification required]` placeholders have all been resolved.
- [ ] The jurisdiction(s) in which patent protection is being considered have been confirmed, and the applicable novelty, non-obviousness, and subject-matter eligibility standards verified for each `[verify jurisdiction]` flag.
- [ ] Subject-matter eligibility has been evaluated by a patent specialist where flagged as a close or hard-to-call question.
- [ ] No prior-art conclusion has been drawn from this screen; a formal patentability search and opinion has been commissioned where the verdict is Pursue.
- [ ] The patent-versus-trade-secret strategic question has been addressed by counsel if detectability concerns were flagged.
- [ ] No legal authority, statutory text, or case law has been asserted or relied upon from this screen without independent verification.
- [ ] Client has been advised that this screen is not a patentability opinion and does not establish that the invention is patentable, novel, non-obvious, or patent-eligible.
- [ ] All `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, and `[deadline verification required]` placeholders have been resolved before the screen result is acted upon.
