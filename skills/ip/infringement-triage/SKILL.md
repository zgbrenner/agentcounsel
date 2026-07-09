---
name: Infringement Triage
description: "Use when a client needs a first-pass, structured triage of a potential intellectual property infringement issue — identifying the key factors, flagging their direction, and routing to IP counsel — without concluding whether infringement occurred."
practice_area: ip
task_type: triage
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The intellectual property right or rights at issue"
  - "The parties' posture and relationship"
  - "The available evidence of potential infringement"
outputs:
  - "Infringement triage memo identifying key factors and routing to IP counsel"
related_skills:
  - skills/ip/cease-and-desist-response/SKILL.md
  - skills/ip/fto-triage/SKILL.md
  - skills/ip/trademark-clearance-triage/SKILL.md
  - skills/ip/dmca-takedown/SKILL.md
  - skills/litigation/demand-letter/SKILL.md
tags:
  - ip
  - infringement
  - triage
  - ip-enforcement
  - routing
---

# Infringement Triage

## Purpose

Produce a structured first-pass triage memo for a potential intellectual property infringement issue. The memo identifies which legal factors are relevant to the IP right(s) at issue, flags how each factor appears to cut on the disclosed facts, assigns a routing signal, and recommends next steps calibrated to the client's posture as either the potential senior party (asserting a right) or the accused party (defending against a potential claim).

This is draft legal work product for attorney review. It is NOT a legal opinion on whether infringement has occurred or will be found. It does NOT constitute a merits determination, a freedom-to-operate opinion, a formal claim construction, or legal advice of any kind. The infringement conclusion is reserved exclusively to an attorney.

## Use When

- A client believes someone may be infringing its intellectual property right and wants a preliminary read of the situation before engaging IP counsel for an enforcement action.
- A client has received an informal infringement complaint, a demand, or internal notice that its own product or conduct may infringe a third party's intellectual property, and wants a preliminary structured assessment before engaging IP counsel.
- A user asks to "triage this IP issue," "does this look like infringement," "what are the key factors," or similar first-pass framing.
- A client wants a structured briefing document to share with outside IP counsel to frame the engagement efficiently.

## Required Inputs

- **The IP right(s) at issue**: identify which type(s) — trademark, copyright, patent, trade secret, or some combination. If the type is unclear, flag it and attempt to identify the most likely right from the described facts before proceeding.
- **The party posture**: is the client the potential **senior party** (owns or claims the right and believes it is being infringed) or the **accused party** (may be infringing someone else's right)? If unclear, request clarification before proceeding; the posture governs the routing recommendations.
- **The jurisdiction or governing law**: identify the jurisdiction or legal system governing the dispute. If not provided, flag as `[CONFIRM: governing law and jurisdiction]` and note that the applicable factor framework cannot be confirmed without it.
- **The relevant facts and evidence**: a description or copy of the allegedly infringing material, the asserted right (e.g., the claimed mark, the asserted work, the patent claims at issue, or the trade secret), and any known dates, priority dates, registration numbers, or registration status.
- **Timing information** (if known): when the potentially infringing conduct began, any relevant priority or creation dates, and whether there is a known complaint or demand date. Timing may bear on whether a limitations or laches clock is relevant — but no clock is computed in this memo `[deadline verification required]`.

If any required input is missing, stop and request it before proceeding, or note clearly that the analysis covering that input is incomplete. Never fabricate facts, registration details, priority dates, or claim language.

Optional input: the client's IP enforcement posture or policy, if available, which may inform the recommended next steps and the threshold for action.

## Do Not Use When

- The client has received a formal cease-and-desist letter and needs to prepare a structured response — use `cease-and-desist-response`.
- The client needs a freedom-to-operate triage against specific, identified third-party patent claims — use `fto-triage`.
- The client is clearing a proposed new brand, product name, or mark before use — use `trademark-clearance-triage`.
- The client needs to prepare, evaluate, or respond to a DMCA takedown notice — use `dmca-takedown`.
- The client wants an outbound cease-and-desist or demand letter drafted — use `demand-letter`.
- The user wants a definitive legal opinion on whether infringement occurred or will be sustained — that is an attorney determination, outside the scope of any triage workflow.
- The IP right at issue is governed exclusively by non-domestic law and no applicable domestic right is implicated `[ATTORNEY TO CONFIRM: choice-of-law and applicable rights]`.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This memo is NOT legal advice. The client must not commence an enforcement action, cease any conduct, make any demand, or commit to any course of action based solely on this memo.
- This workflow produces a **routing signal**, not an infringement finding. The triage signal (GREEN / YELLOW / RED) is a structured read of the disclosed facts for routing purposes only. It is explicitly NOT a conclusion that infringement has or has not occurred, and it is NOT a prediction of litigation outcome.
- The attorney reviews and determines whether infringement occurred, whether any asserted right is valid, which legal test applies, and what the applicable standard is under governing law. Every factor framework applied in this memo must be confirmed `[verify jurisdiction]` — the controlling test and its elements are attorney determinations.
- For an accused-party posture involving a patent right: the act of reading and retaining a patent infringement analysis may be relevant to a later willfulness inquiry under the governing law `[verify jurisdiction]`. This memo should be treated as privileged attorney-client or work-product material and kept within privileged channels `[ATTORNEY TO CONFIRM: privilege and confidentiality scope]`.
- Do not run, consult, or purport to consult any trademark registry, copyright registry, patent register, docket, or other database. This workflow does not perform a registry or docket search; flag any registration or filing status as `[VERIFY: current status]`.
- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available. Do not invent case names, statute numbers, regulation sections, named acts, or named multi-factor tests; treat model background knowledge about any specific authority as unverified and use `[citation needed]` or `[verify jurisdiction]` as appropriate.
- The two-way-door rule governs factor analysis: over-flagging factors is reversible (the attorney narrows); under-flagging is not (a clock runs, or rights erode). Default to surfacing every plausible factor rather than narrowing prematurely.
- Do not decide any affirmative defense (fair use, invalidity, independent development, prior use, or others). Identify defenses as items to evaluate, and flag each as `[ATTORNEY TO CONFIRM]`.
- Separate clearly throughout: (a) what the client has disclosed as fact, (b) analytical observations drawn from those facts, (c) factors that require attorney or third-party verification, and (d) items that are assumptions.
- Preserve confidentiality and privilege. Do not include client-sensitive facts in any output that might be shared outside the privileged engagement.
- Flag every uncertainty with a placeholder rather than resolving it silently.

## Workflow

1. **Confirm inputs and posture.** Verify that the IP right(s) at issue, the party posture, and a sufficient factual description have been provided. If the party posture is ambiguous, request clarification — the routing recommendations differ materially between the senior-party and accused-party postures. If the jurisdiction is not provided, proceed with the factor analysis but mark every element of the legal framework `[verify jurisdiction]`. Record all inputs exactly as provided; do not recharacterize or embellish facts.

2. **Identify and scope the right(s) at issue.** If more than one IP right may be implicated (e.g., both trademark and copyright), identify each separately. Run a distinct triage analysis for each right; do not blend the factor frameworks across rights. A blended analysis may obscure materially different exposures or strengths. Flag any right whose type is uncertain: `[CONFIRM: which IP right(s) govern this dispute]`.

3. **Apply the factor framework for each right at issue.** For each IP right identified, walk the relevant factor framework. For each factor:
   - State the factor.
   - Identify the disclosed facts relevant to that factor.
   - Flag the apparent direction: **favors the senior party**, **favors the accused party**, **mixed**, or **insufficient information to assess** `[CONFIRM: additional facts needed]`.
   - Mark the factor's weight and the applicable test as `[verify jurisdiction]` — do not assert that any particular weight or test controls.
   - Avoid resolving close calls; flag them as mixed and note what additional information would clarify direction.

   **Trademark** — apply where the asserted right is a mark, trade name, trade dress, or similar source-identifying element:
   - Ownership and validity of the asserted right: whether the mark is registered or unregistered, whether it has been in use, the apparent strength of the mark (arbitrary, suggestive, descriptive, or generic, as appropriate — without asserting a legal conclusion), and any visible weakness signals `[VERIFY: registration status and validity]`.
   - Likelihood of confusion: similarity of the marks in appearance, sound, and meaning; relatedness of the goods or services; channels of trade; conditions of purchase; any evidence of actual confusion; the senior party's intent in selecting the mark; and the strength of the senior party's mark `[verify jurisdiction]` — these are the commonly cited factors; the controlling list and weighting are jurisdiction-specific `[ATTORNEY TO CONFIRM]`.
   - Dilution: if the asserted mark is famous `[VERIFY: whether fame standard is met under applicable law]`, note whether blurring or tarnishment may be implicated — but do not apply a dilution analysis unless the senior party has explicitly raised it `[ATTORNEY TO CONFIRM]`.
   - False advertising or unfair competition: if the facts suggest a passing-off or false-association theory beyond likelihood of confusion, flag it as a separate consideration `[ATTORNEY TO CONFIRM]`.

   **Copyright** — apply where the asserted right is a creative work:
   - Ownership: who created the work, whether authorship is individual or joint or work-made-for-hire, and whether any assignment or license affects ownership `[VERIFY: chain of title]`.
   - Registration status and its implications: whether the work is registered and when, relative to the alleged infringement — note that registration status may bear on available remedies under applicable law `[verify jurisdiction]` `[VERIFY: registration date and status]`.
   - Access and copying: whether the accused party had access to the protected work and whether the accused work is substantially similar to the protectable expression (as distinguished from unprotectable elements such as ideas, facts, functional elements, or standard elements `[verify jurisdiction]`).
   - Fair use or analogous defense: identify whether any fair use factors appear facially implicated — but do not decide whether fair use applies `[ATTORNEY TO CONFIRM]`.
   - Safe harbor: if the allegedly infringing content appears on a platform or service, note whether a safe harbor or host liability defense may be available to consider `[ATTORNEY TO CONFIRM]`.

   **Patent** — apply where the asserted right is a patent or pending patent application:
   - Identify the asserted claim(s) by number if provided; if not provided, flag that a claim-by-claim analysis cannot be performed `[CONFIRM: asserted claims]`.
   - Perform a first-pass, element-by-element comparison of each asserted claim against the accused product or method, using only the claim language provided and the facts disclosed. For each claim element, note whether a corresponding element appears to be present in the accused product or method, absent, or uncertain. This is a preliminary read only — not formal claim construction `[ATTORNEY TO CONFIRM: formal claim construction required]`.
   - Flag whether the doctrine of equivalents may be implicated for any element assessed as absent or uncertain `[ATTORNEY TO CONFIRM]`.
   - Flag whether indirect infringement theories (inducement, contributory) are facially implicated by the disclosed facts `[ATTORNEY TO CONFIRM]`.
   - Flag potential invalidity considerations (prior art, written description, enablement, obviousness, or others) as defenses to evaluate — but do not assess validity `[ATTORNEY TO CONFIRM]`.
   - Willfulness flag (accused-party posture only): note that the existence of this memo and the accused party's knowledge of the asserted patent may be relevant to a willfulness inquiry under the governing law `[verify jurisdiction]`. This memo must be kept within privileged channels `[ATTORNEY TO CONFIRM]`.

   **Trade Secret** — apply where the asserted right is a claimed trade secret:
   - Identification of the alleged trade secret: is the alleged secret described with sufficient specificity to support an analysis? If not, flag `[CONFIRM: specific identification of the claimed trade secret]`.
   - Secrecy: whether the alleged trade secret was actually secret at the relevant time — flag any public disclosure, publication, or prior art that may undercut secrecy `[ATTORNEY TO CONFIRM]`.
   - Reasonable secrecy measures: whether the alleged owner took steps reasonably designed to maintain secrecy (access controls, confidentiality agreements, physical security, etc.) `[CONFIRM: what measures were in place]`.
   - Misappropriation: whether the accused conduct involved acquisition by improper means, breach of a duty of confidentiality, or use of information known or believed to have been improperly obtained `[ATTORNEY TO CONFIRM]`.
   - Independent development defense: whether the accused party can document an independent development path `[ATTORNEY TO CONFIRM]`.

4. **Identify defenses and thresholds.** For each right analyzed, list the affirmative defenses and threshold questions that IP counsel should evaluate. Do not decide whether any defense applies. Flag each as `[ATTORNEY TO CONFIRM]`. Common items include:
   - Validity and enforceability of the asserted right (all rights).
   - Statute of limitations or laches `[verify jurisdiction]` `[deadline verification required]`.
   - License or consent (express or implied).
   - Exhaustion or first sale (patent and copyright, as applicable `[verify jurisdiction]`).
   - Fair use or analogous equitable defense (copyright, trademark `[verify jurisdiction]`).
   - Prior use or prior user rights (trademark, patent `[verify jurisdiction]`).
   - Independent development (trade secret).
   - Inequitable conduct or misuse (patent `[ATTORNEY TO CONFIRM]`).
   - Any other defense visible from the disclosed facts `[ATTORNEY TO CONFIRM]`.

5. **Assign a triage signal.** Assign one of three signals based on the overall picture across all rights analyzed — as a routing signal only, explicitly NOT an infringement conclusion:

   - **RED**: The disclosed facts present a materially strong basis for the senior party's claim across one or more key factors, or present a materially elevated risk for the accused party. Prompt engagement of IP counsel is warranted.
   - **YELLOW**: The disclosed facts present a mixed picture — some factors favor the senior party and some favor the accused party, or the facts are insufficient to assess one or more material factors. IP counsel should evaluate before any action is taken.
   - **GREEN**: The disclosed facts present facially weak support for the claimed infringement, or the accused party's position appears facially strong on the disclosed factors. The matter still warrants IP counsel review, but the urgency level is lower.

   State the signal, identify the one or two factors that most drive it, and conclude with: *This signal is a routing indicator based solely on the disclosed facts. It is not a finding that infringement has or has not occurred. Counsel must evaluate validity, apply the controlling legal standards under the governing jurisdiction, and determine the appropriate course of action* `[ATTORNEY TO CONFIRM]`.

6. **Produce the "what cuts which way" summary table.** Using `templates/infringement-triage-memo.md`, for each right analyzed, produce a table with columns: Factor | Direction | Key Disclosed Fact | Verification Needed. Populate one row per factor assessed. At the bottom of the table, include a bolded statement: **This table is a preliminary organizational tool. It is not a finding of infringement or non-infringement.**

7. **Recommend next steps by posture.** Calibrate next steps to the disclosed party posture.

   *Senior-party posture*: Recommended next steps may include — engaging IP counsel to evaluate the strength of the asserted right and potential enforcement options; conducting a full validity and enforceability review of the asserted right before any demand is made `[ATTORNEY TO CONFIRM]`; gathering and preserving evidence of the infringement and of the senior party's priority `[ATTORNEY TO CONFIRM: legal hold and evidence preservation]`; confirming whether any registration or filing deadline is relevant `[deadline verification required]`; considering whether an informal outreach, a formal cease-and-desist, a takedown, or a licensing approach is most consistent with the client's enforcement posture.

   *Accused-party posture*: Recommended next steps may include — engaging IP counsel promptly, particularly if any demand or deadline has been received `[deadline verification required]`; preserving all evidence of independent development, prior use, or non-use of the asserted right `[ATTORNEY TO CONFIRM: legal hold]`; evaluating invalidity and other defenses before any substantive response is made; confirming whether any applicable insurance policy may be implicated `[CONFIRM: policy terms and notice requirements]`; avoiding any written acknowledgment of the asserted right's validity without counsel's guidance.

   In either posture: note that this workflow does not run registry or docket searches, and that a full enforcement or defense strategy requires counsel to conduct independent verification.

8. **List assumptions and flag missing information.** Enumerate every fact assumed in the analysis and every input that was not provided. Flag the impact of each gap on the reliability of the analysis.

9. **Assemble the output** in the format below, using the skeleton in `templates/infringement-triage-memo.md`. Label the document as a draft infringement triage memo for attorney review.

## Output Format

Deliver a document built on `templates/infringement-triage-memo.md`, labeled:

> **DRAFT — INFRINGEMENT TRIAGE MEMO**
> *Attorney review required before any enforcement action, demand, response, or change in conduct. This is not legal advice. This memo does not conclude whether infringement occurred.*

Sections in order:

1. **Scope and Posture** — the IP right(s) at issue, the party posture (senior or accused), the jurisdiction (or `[CONFIRM: governing law and jurisdiction]`), and the key dates provided.
2. **Factor Analysis by Right** — one subsection per right, walking each factor, its direction, the supporting disclosed fact, and the verification item. Close each subsection with the applicable defenses list.
3. **Triage Signal** — the GREEN / YELLOW / RED signal with the one-sentence rationale and the explicit caveat that it is a routing indicator, not a finding.
4. **What Cuts Which Way — Summary Table** — the direction table per right, with the no-conclusion statement.
5. **Recommended Next Steps** — calibrated to the disclosed posture.
6. **Assumptions and Missing Information** — all assumed facts and all missing inputs, with impact notes.
7. **Attorney Verification Items** — drawn from the checklist below.

Use `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[citation needed]`, `[verify jurisdiction]`, and `[deadline verification required]` throughout wherever information is unverified, uncertain, or jurisdiction-dependent.

## Attorney Verification Checklist

- [ ] The IP right(s) identified in the memo are the correct and complete set of rights implicated by the disclosed facts; no additional rights have been overlooked.
- [ ] The party posture (senior or accused) has been confirmed; the routing and next-step recommendations are appropriate for the actual posture.
- [ ] The governing jurisdiction and applicable law have been confirmed; the factor frameworks applied in this memo match the controlling tests under that law.
- [ ] Each asserted right has been independently verified for status, validity, and enforceability (registration status, ownership chain, maintenance, any cancellation or reexamination proceedings) `[VERIFY: current status for each right]`.
- [ ] For trademark matters: the full likelihood-of-confusion factor framework applicable in the governing jurisdiction has been applied; any dilution or unfair competition theories have been separately evaluated.
- [ ] For copyright matters: ownership and chain of title have been confirmed; registration date and status have been verified; the scope of protectable expression versus unprotectable elements has been assessed by counsel.
- [ ] For patent matters: formal claim construction has been performed by counsel; the element-by-element analysis in this memo has been reviewed and superseded by a counsel-supervised analysis; any willfulness risk has been assessed and this memo has been placed in privileged channels.
- [ ] For trade secret matters: the alleged trade secret has been specifically identified with sufficient particularity; the adequacy of the secrecy measures has been evaluated; the misappropriation theory has been assessed.
- [ ] All affirmative defenses identified in the memo have been evaluated under the governing law; additional defenses not identified in this first-pass memo have been considered.
- [ ] Any limitations, laches, or other timing-sensitive doctrine has been independently evaluated; all relevant dates have been verified and no deadline has been allowed to pass without counsel's assessment `[deadline verification required]`.
- [ ] The triage signal has been reviewed in light of facts not disclosed in this memo; it is not treated as a legal opinion or a litigation prediction.
- [ ] The recommended next steps have been reviewed and tailored to the client's actual situation and enforcement posture; none have been taken based solely on this draft memo.
- [ ] No legal authority, citation, statute, named act, or named test cited or implied in this memo has been asserted without independent verification.
- [ ] A legal hold has been considered and issued or affirmatively declined; relevant documents, communications, and evidence have been preserved.
- [ ] Client confidentiality and attorney-client privilege have been maintained throughout; for patent accused-party matters, this memo has been kept within privileged channels.
- [ ] All assumptions and missing-information items have been resolved before this memo is relied upon or shared with the client.
