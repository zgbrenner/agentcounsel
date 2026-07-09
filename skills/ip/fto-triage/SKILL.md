---
name: Patent Freedom-to-Operate Triage
description: "Use when a user needs a structured first-pass review of potential patent blocking issues for a product, process, or feature against a set of identified patents, to flag risk areas and route findings to patent counsel for a formal freedom-to-operate opinion."
practice_area: ip
task_type: triage
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The product, process, or feature description"
  - "The relevant jurisdictions"
  - "The set of identified patents to assess"
outputs:
  - "Freedom-to-operate triage memo flagging risk areas for patent counsel"
related_skills:
  - skills/litigation/claim-chart/SKILL.md
  - skills/ip/invention-intake/SKILL.md
  - skills/ip/infringement-triage/SKILL.md
tags:
  - ip
  - patent
  - freedom-to-operate
  - triage
  - infringement-risk
---

# Patent Freedom-to-Operate Triage

## Purpose

Produce a structured, attorney-ready triage memo that identifies potential patent blocking issues for a described product, process, or feature against a specific set of patents the user has already identified. The memo flags risk areas, surfaces open questions, and orients patent counsel for a formal freedom-to-operate analysis.

This is draft legal work product for attorney review. It is **NOT** a freedom-to-operate opinion. It does **NOT** conclude that a product is "clear to operate," that no infringement exists, or that any patent is invalid. Those conclusions require a formal opinion from qualified patent counsel following a comprehensive search and full legal analysis.

## Use When

- A user asks to "check if our product is blocked by these patents" or "do an FTO triage" against a defined list of patents.
- A product, process, or feature is approaching launch and the team wants a structured first-pass memo to brief patent counsel.
- A user has a set of identified patents and needs a systematic, element-by-element first-pass read organized for counsel review.
- A user needs to document preliminary patent risk considerations before engaging in a licensing or design-around discussion with counsel.

## Required Inputs

- **Technical description**: a clear, precise description of the product, process, or feature being analyzed — the technical essence, not marketing language. The more specific the description, the more useful the triage.
- **Supporting technical detail**: any additional specifications, drawings, flowcharts, claim charts, or design documents the user can provide.
- **Jurisdictions**: the countries or regions where the product will be made, used, sold, offered for sale, or imported. Different jurisdictions may have different governing standards. `[verify jurisdiction]`
- **Patents in scope**: the patents the user is already aware of — identified by patent number, publication number, or pasted claim text. This skill does NOT run a patent-database search.
- **Timing**: the intended launch date or go/no-go decision deadline. `[deadline verification required]`

If the technical description is not provided, stop and request it before proceeding. If no patents are identified, stop and explain that this skill analyzes only patents the user supplies — it does not conduct a patent search. If jurisdiction is not provided, flag it as unknown and note that the triage will be incomplete and potentially misleading without it.

## Do Not Use When

- The user wants a formal freedom-to-operate opinion or a "clear to operate" conclusion — those require a comprehensive patent search and a written opinion from qualified patent counsel.
- The user needs a patent validity or enforceability analysis — validity is outside the scope of this triage.
- The user needs claim construction — interpreting claim terms in light of the prosecution history, specification, and applicable legal standards is an attorney task.
- The user needs a standalone element-by-element infringement claim chart as a deliverable (use `claim-chart`).
- The user is screening a new invention for patentability (use `invention-intake`).
- The patents at issue include design patents or plant patents — those require separate routing to patent counsel experienced in those patent types.
- The user is evaluating whether to assert patents against a third party — that is an enforcement matter, not an FTO triage.

## Legal Safety Rules

- This triage is draft legal work product for attorney review. It is NOT a freedom-to-operate opinion and NOT legal advice. Attorney review and sign-off are required before any reliance on this output.
- **Never conclude "clear to operate," "no infringement," or "the product is free to operate."** The only permissible posture conclusions are: "appears to practice every element of [claim]," "one or more elements appear not present," or "turns on claim construction." Any other conclusion must be flagged as outside the scope of this triage.
- This triage covers only the patents the user has supplied. It does not account for patents not identified, continuation applications, divisionals, foreign counterparts, or any patent that would be revealed by a comprehensive search. State this limitation prominently.
- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available. Do not invent patent claims, claim language, priority dates, expiration dates, assignee names, prosecution history, or licensing status. All patent metadata is treated as unverified unless the user has pasted the source text directly. Flag all dates `[VERIFY]`.
- **Consult `connectors/uspto.md` when a verification path is available** to confirm that a patent or application in scope exists and to record its number, owner of record, and recorded legal status as facts for counsel — for existence and status only, never to construe claims or to reach a freedom-to-operate, infringement, or validity conclusion, and never to compute an expiration or maintenance date (which stays `[deadline verification required]`); when no connector is available, the placeholder discipline is unchanged.
- Do not assert governing legal standards, statutory text, or case law. Describe concepts generically (e.g., "the applicable infringement standard," "claim construction," "the doctrine of equivalents") and flag governing law as `[verify jurisdiction]`.
- Reviewing a triage memo that references specific patents can be relevant to a willfulness analysis under applicable law. Flag this at the outset and instruct the user to keep this document within privileged attorney-client channels. Do not summarize or resolve willfulness exposure — route to patent counsel.
- Separate facts provided by the user, analytical observations, assumptions, and attorney-verification items into distinct labeled sections.
- Preserve confidentiality and privilege. Keep client-sensitive technical facts out of any reusable template outputs.
- Flag every uncertainty with `[CONFIRM: ...]`, `[VERIFY: ...]`, or `[ATTORNEY TO CONFIRM: ...]` rather than resolving it silently.

## Workflow

1. **Open with required disclaimers.** Before any substantive analysis, state both of the following clearly and prominently:
   - *Not an FTO opinion*: This document is a preliminary triage memo and not a freedom-to-operate opinion. It does not conclude that the product is clear to operate or that no infringement risk exists.
   - *Willfulness notice*: Awareness of specific patents and their claims can bear on a willfulness analysis under the applicable infringement standard `[verify jurisdiction]`. This document must be maintained within privileged attorney-client channels and shared only with or at the direction of patent counsel.

2. **Confirm inputs.** Verify that all required inputs have been provided. Record the technical description, jurisdiction(s), launch timing, and patents in scope exactly as provided. If the technical description is absent, stop. If jurisdiction is absent, note the limitation and proceed with explicit `[verify jurisdiction]` flags throughout. If no patents are supplied, stop and explain that this skill requires a user-identified patent set.

3. **State the scope of analysis.** Explicitly state: no patent-database search has been performed; the analysis is limited to the patents the user has supplied; this triage does not account for patents not yet identified, continuation applications, divisionals, foreign counterparts, or unpublished applications. `[ATTORNEY TO CONFIRM: comprehensive search has been or will be commissioned]`

4. **Classify patents in scope.** For each patent or patent number supplied, note the patent type (utility, design, plant, reissue, or unknown). Flag any non-utility patent — including design patents and plant patents — as requiring separate routing to patent counsel experienced in those patent types. Proceed with the element-by-element first pass only for utility patents.

5. **Capture patent metadata.** For each utility patent in scope, record:
   - Patent number and jurisdiction of issuance
   - Assignee or owner as stated by the user `[VERIFY: current ownership]`
   - Priority date `[VERIFY]`
   - Issue date `[VERIFY]`
   - Estimated expiration date `[VERIFY: actual expiration requires prosecution-history review and maintenance-fee status check]`
   - Current status (active, lapsed, expired, reexamination pending) `[VERIFY]`
   - Independent claims — paste or summarize the claim language as provided by the user; do not paraphrase or reconstruct claim language

6. **Conduct an element-by-element first pass.** For each independent claim of each in-scope utility patent, perform a preliminary claim-element read against the technical description:
   - Break the claim into discrete elements (limitations).
   - For each element, assess whether the described product, process, or feature: **Present** — the technical description appears to include this element; **Not Present** — the technical description does not appear to include this element; **Unclear** — insufficient technical detail to assess; or **Construction-Dependent** — the assessment turns on how a claim term is interpreted.
   - Note: a claim is only potentially infringed if the accused product practices every element. If any element is clearly not present, note that the claim appears not infringed on a literal-infringement basis — but flag that the doctrine of equivalents and claim construction remain for patent counsel.
   - Do NOT perform this analysis for dependent claims — flag them as attorney judgment items if an independent claim raises concern.

7. **Flag doctrine of equivalents and indirect infringement.** For any claim where literal infringement appears possible, flag — as attorney-judgment items only, not as conclusions — that:
   - The doctrine of equivalents may extend the reach of a claim beyond its literal terms `[ATTORNEY TO CONFIRM: doctrine of equivalents analysis]`
   - Indirect infringement (including inducement and contributory theories) may be relevant depending on the product's distribution and use model `[ATTORNEY TO CONFIRM: indirect and divided infringement analysis]`
   - Divided infringement may be relevant if elements of a method claim are performed by different parties `[ATTORNEY TO CONFIRM]`

8. **State the decision posture for each claim.** Using only the following permissible conclusions, state the preliminary posture for each independent claim reviewed:
   - "Appears to practice every element of [claim number]" — use when all elements appear present
   - "One or more elements appear not present in [claim number]" — use when at least one element clearly appears absent
   - "Turns on claim construction of [claim number]" — use when the outcome depends on how one or more claim terms are interpreted
   - **Never use:** "clear to operate," "no infringement," "does not infringe," or any equivalent formulation. If the user requests such a conclusion, decline and explain that it requires a formal FTO opinion from patent counsel.

9. **List open questions.** Compile a numbered list of questions whose answers would materially affect the analysis: technical gaps in the product description, claim terms requiring construction, unknown patent status, missing priority or expiration date information, unknown ownership or licensing status, and jurisdictions not yet analyzed.

10. **List next steps.** Recommend concrete next steps for patent counsel, including: commissioning a comprehensive patent search; obtaining formal claim construction; reviewing the prosecution history of flagged patents; evaluating design-around options; assessing validity and enforceability; and confirming patent status and ownership. `[deadline verification required]`

11. **Assemble the output** following the Output Format below, label it a preliminary triage draft for attorney review, and include all required disclaimers, assumptions, and placeholders.

## Output Format

Deliver the triage memo as a labeled draft with the following sections, in order:

**PRELIMINARY FTO TRIAGE MEMO — DRAFT FOR ATTORNEY REVIEW**

1. **Disclaimers** — not an FTO opinion; willfulness notice; scope limitation (patents supplied by user only; no database search conducted)
2. **Inputs as Provided** — technical description, jurisdictions, launch timing, patents in scope
3. **Patents in Scope and Metadata** — for each patent: number, jurisdiction, assignee `[VERIFY]`, priority date `[VERIFY]`, issue date `[VERIFY]`, estimated expiration `[VERIFY]`, status `[VERIFY]`, independent claim text as provided
4. **Element-by-Element First Pass** — for each independent claim: claim elements listed with Present / Not Present / Unclear / Construction-Dependent assessment and brief rationale; doctrine of equivalents and indirect infringement flagged as attorney items
5. **Decision Posture Summary** — one permissible conclusion per claim reviewed, using only the three allowable formulations
6. **Open Questions** — numbered list
7. **Next Steps for Patent Counsel** — numbered list with `[deadline verification required]` where timing is implicated
8. **Assumptions** — explicit list of all assumptions made
9. **Attorney Verification Items** — items requiring confirmation, sourced with `[ATTORNEY TO CONFIRM: ...]` or `[VERIFY: ...]` placeholders

Use `[CONFIRM: ...]` for inputs the user should confirm. Use `[VERIFY: ...]` for facts requiring external verification. Use `[ATTORNEY TO CONFIRM: ...]` for legal judgments reserved for counsel. Use `[citation needed]` if a legal concept is referenced that requires a source. Use `[verify jurisdiction]` whenever a legal standard is described.

## Attorney Verification Checklist

- [ ] The technical description accurately and completely describes the product, process, or feature at issue; no material features were omitted.
- [ ] All patent numbers, claim text, and metadata have been verified against official patent office records; expiration dates have been confirmed including maintenance-fee status.
- [ ] Current ownership and any known licensing, covenant not to sue, or exhaustion considerations have been confirmed for each patent in scope.
- [ ] A comprehensive patent search has been commissioned and completed; this triage does not substitute for that search.
- [ ] Jurisdiction-specific infringement standards have been confirmed and applied; this triage used `[verify jurisdiction]` placeholders throughout.
- [ ] Claim construction has been performed or is scheduled; no claim-term interpretations in this triage have been accepted as legal conclusions.
- [ ] The doctrine of equivalents has been evaluated for each claim where literal elements were flagged as not present.
- [ ] Indirect infringement theories — including inducement, contributory infringement, and divided infringement — have been evaluated where relevant.
- [ ] Validity and enforceability of each flagged patent have been assessed or are scheduled for assessment.
- [ ] No conclusion of "clear to operate" or "no infringement" appears in this memo; if any such language was generated, it has been removed before reliance.
- [ ] Design patents, plant patents, or reissue patents in scope have been separately routed and analyzed.
- [ ] All open questions in Section 6 have been resolved or documented as outstanding before the memo is relied upon.
- [ ] All deadlines — including launch timing and any response or licensing deadlines — have been independently verified. `[deadline verification required]`
- [ ] This document has been maintained within privileged attorney-client channels; willfulness exposure has been evaluated by patent counsel.
- [ ] The output has been reviewed by qualified patent counsel, who confirms it is accurate, complete, and appropriate for its intended use.
