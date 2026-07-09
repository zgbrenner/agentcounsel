---
name: Cease and Desist Response
description: "Use when a client has received a cease-and-desist letter or similar IP demand and needs a structured triage memo — covering the assertion, exposure, response options, and immediate actions — for attorney review before responding."
practice_area: ip
task_type: triage
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The received cease-and-desist letter or IP demand"
  - "The client's factual assessment of the assertion"
  - "Any deadlines stated in the letter"
outputs:
  - "Structured response triage memo covering exposure, options, and immediate actions for attorney review"
related_skills:
  - skills/litigation/demand-letter/SKILL.md
  - skills/ip/dmca-takedown/SKILL.md
  - skills/ip/trademark-clearance-triage/SKILL.md
  - skills/ip/infringement-triage/SKILL.md
tags:
  - ip
  - cease-and-desist
  - ip-demand
  - triage
  - inbound-demand
---

# Cease and Desist Response

## Purpose

Produce a structured triage memo for a client who has received a cease-and-desist letter or similar intellectual property demand. The memo summarizes the assertion, assesses the sender's claimed rights and the client's exposure, presents response options with tradeoffs, triages any stated deadline, identifies immediate actions, and offers a draft recommendation — all for attorney review before the client responds, declines to act, or makes any commitment.

This is draft legal work product for attorney review. It is NOT a legal opinion on the merits, NOT advice about whether the client infringes, and does NOT determine the validity of any asserted right.

## Use When

- A client has received a cease-and-desist letter, demand letter, or similar written IP demand asserting trademark, copyright, patent, trade secret, or related rights.
- A user asks to "review this C&D," "what does this letter mean," or "what should we do about this demand."
- A client wants a structured briefing document to share with outside IP counsel.
- A client needs to understand the range of response options and their tradeoffs before consulting an attorney.

## Required Inputs

- **The inbound letter**: the full text, or a detailed description including: the sender's identity; the right(s) asserted (trademark, copyright, patent, trade secret, or other); the alleged infringing conduct; the specific demand (cease use, remove content, pay damages, execute a license, etc.); any stated deadline; and the overall tone.
- **The client's factual self-assessment**: the client's honest account of whether it is actually doing what the letter alleges, and any relevant context (when the conduct began, whether it was aware of the asserted right, any prior dealings with the sender).

If the letter text or description is not provided, stop and request it before proceeding. If the client's factual self-assessment is not provided, flag it as missing and note that the exposure assessment will be incomplete without it. Never fabricate any element of either input.

Optional input: the client's IP enforcement posture or policy, if available, which may inform the recommended response approach.

## Do Not Use When

- The client wants to **draft an outbound** cease-and-desist or demand letter — use `demand-letter`.
- A complaint has already been filed and the matter is in active litigation — this workflow is for pre-litigation demand letters, not filed cases; refer to litigation counsel immediately.
- The user needs a definitive legal opinion on whether the client infringes — that is an attorney determination, not a triage memo.
- The matter involves a DMCA takedown notice directed at a platform or host — use `dmca-takedown`.
- The user needs trademark clearance for a new mark — use `trademark-clearance-triage`.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available. Do not invent registration numbers or filing dates either; treat model background knowledge about any specific case, statute, or regulation as unverified and use `[citation needed]` or `[verify jurisdiction]` as appropriate.
- Produce draft legal work product for attorney review. This memo is NOT legal advice and NOT a merits opinion. The client must not respond, decide to ignore the letter, or commit to any course of action based solely on this memo.
- The triage rating assigned in this memo is a structured read of the letter for routing purposes only. It is NOT a determination of whether the client infringes or whether the asserted right is valid.
- The validity of the asserted right and the applicable legal test are attorney determinations. Do not autonomously verify the sender's cited authority, assert that a cited registration is valid or invalid, or claim that a particular legal test applies. Flag all such points `[verify jurisdiction]` or `[ATTORNEY TO CONFIRM]`.
- A deadline stated in a received cease-and-desist letter does not necessarily bind the recipient — but never compute, assert, or extend any deadline. Apply `[deadline verification required]` to every stated or derived date.
- A received cease-and-desist letter may trigger a duty to preserve documents and other material. Flag issuing a legal hold as an immediate action without rendering any legal opinion about whether such a duty has attached `[ATTORNEY TO CONFIRM]`.
- Separate clearly: (a) what the letter states, (b) what the client has disclosed, (c) your analytical observations, and (d) items requiring attorney or third-party verification.
- Preserve confidentiality and privilege. Do not include client-sensitive facts in reusable templates or in any output that might be shared outside the privileged engagement.
- Flag every uncertainty with a placeholder rather than resolving it silently.

## Workflow

1. **Confirm inputs.** Verify that the inbound letter (or a sufficiently detailed description) and the client's factual self-assessment have been provided. If either is missing, stop and request it. Record both exactly as provided; do not paraphrase or recharacterize the sender's allegations.

2. **Extract the letter's elements.** Identify and record:
   - Sender identity and any named rights-holder (if different).
   - IP right(s) asserted (trademark, copyright, patent, trade secret, other) and any cited registrations, application numbers, or registration dates — flag each as `[VERIFY: registration status and validity]`.
   - The alleged infringing conduct: what the sender claims the client is doing.
   - The specific demand: what the sender requires (cease, remove, pay, license, etc.).
   - Any stated deadline — apply `[deadline verification required]`.
   - The tone and apparent purpose (routine enforcement, targeted litigation threat, licensing solicitation, etc.).

3. **Assess the asserted right.** Without verifying the sender's cited authority:
   - Note whether the asserted right appears to be a registered or unregistered right, and flag the registration status as requiring verification.
   - Identify any facially apparent strength or weakness signals in the assertion (e.g., whether the claimed mark appears descriptive, whether the alleged work is identified with sufficient specificity, whether the patent claim scope is stated). Characterize these as preliminary observations only; mark each `[ATTORNEY TO CONFIRM]`.
   - Note whether the demand appears proportionate to the stated basis, or whether it appears overbroad, and flag for attorney evaluation.
   - Identify any timing signals that may be relevant (e.g., apparent delay in asserting the right, proximity to a product launch) without asserting any legal consequence. Flag `[verify jurisdiction]` for any legal doctrine that might attach to timing.
   - Note the apparent forum or jurisdiction if stated or inferable; flag as `[CONFIRM: governing law and jurisdiction]` if not clear.

4. **Assess the client's exposure.** Based solely on the client's disclosed factual self-assessment:
   - State whether the client acknowledges, disputes, or is uncertain about the alleged conduct.
   - Note any apparent gap between what the sender alleges and what the client discloses — without rendering a legal conclusion.
   - Identify collateral stakes that counsel should weigh: potential injunction impact on operations, customer relationships, brand reputation, precedential effect of either compliance or rejection, and any insurance considerations `[CONFIRM: whether any policy may be implicated]`.
   - Note whether the sender's apparent credibility or litigation history is known from disclosed facts. Do not speculate beyond disclosed facts.

5. **Assign a triage rating.** Assign one of four ratings as a structured read for routing — explicitly labeled NOT a merits opinion:
   - **Substantial**: The assertion, on the face of the letter and disclosed facts, appears facially well-grounded and the alleged conduct appears to overlap meaningfully with the demand. Counsel should treat as requiring prompt attention.
   - **Debatable**: The assertion has identifiable bases but also identifiable weaknesses or gaps; the overlap between the allegation and disclosed conduct is unclear or partial. Counsel should evaluate carefully.
   - **Weak**: The assertion has significant facial gaps, the demand appears overbroad relative to any plausible right, or the alleged conduct does not appear to match the client's disclosed facts. Counsel should evaluate whether and how to respond.
   - **Frivolous**: The assertion on its face lacks any apparent legal or factual basis. Counsel should evaluate whether to respond at all and whether any countermeasure is warranted.

   State the rating, give a one-paragraph rationale citing only the letter's text and the client's disclosures, and conclude with: *This rating is a structured read of the letter for routing. It is not a merits opinion. Counsel must evaluate validity and applicable legal standards* `[ATTORNEY TO CONFIRM]`.

6. **Present response options with tradeoffs.** For each option below, describe what it entails, its primary advantage, and its primary risk — without recommending one as legally correct:

   - **Comply with the demand**: cease the alleged conduct, remove the content, or otherwise satisfy the stated demand. Advantage: eliminates the immediate dispute and litigation risk. Risk: may concede validity of the asserted right; may be operationally costly; may set a precedent.
   - **Negotiate a resolution**: respond to open a dialogue — license, co-existence agreement, modification of conduct, or settlement. Advantage: preserves relationship and operational flexibility; may achieve a cost-effective resolution. Risk: negotiation may be interpreted as an acknowledgment; timeline uncertainty.
   - **Respond firmly rejecting the claim**: send a substantive letter disputing the asserted right or the alleged conduct. Advantage: preserves the client's position and may deter further demands. Risk: may escalate to litigation; requires a well-grounded factual and legal basis `[ATTORNEY TO CONFIRM]`.
   - **Decline to act while preserving documents**: take no external action at this time but issue a legal hold and monitor. Advantage: preserves options; appropriate when the demand appears weak or the sender's intent is unclear. Risk: the stated deadline passes `[deadline verification required]`; may be used against the client if litigation follows.
   - **Escalate to counsel for an affirmative filing**: where the client may have affirmative claims (e.g., declaratory judgment, cancellation, counterclaim), engage counsel to evaluate offensive options. Advantage: may shift leverage; may resolve uncertainty definitively. Risk: cost and duration; escalation may be disproportionate to the threat.

7. **Triage the deadline.** Identify the deadline stated in the letter, if any. Apply `[deadline verification required]` to the stated date. Note that a deadline stated in a cease-and-desist letter does not necessarily bind the recipient as a matter of law, but ignoring it without counsel's guidance carries practical risk. Flag that counsel should confirm whether any external deadline (e.g., a filing deadline, a registration maintenance date, a statutory period) is triggered by this letter `[ATTORNEY TO CONFIRM]`.

8. **Identify immediate actions.** Flag the following for attorney and client consideration, as applicable:
   - **Legal hold**: the receipt of this letter may trigger a duty to preserve documents, communications, and data potentially relevant to the dispute. Flag issuing a legal hold as a potential immediate action `[ATTORNEY TO CONFIRM: whether duty to preserve has attached and scope]`.
   - **Open a matter**: establish an internal matter number and document the letter and the date received.
   - **Assign counsel**: engage or notify outside IP counsel promptly, particularly if a deadline is stated.
   - **Insurance notification**: consider whether any applicable insurance policy (e.g., intellectual property liability, general liability) may cover the claim or require prompt notice `[CONFIRM: policy terms and notice requirements]`.
   - Any other immediate preservation or notification obligations visible from the disclosed facts.

9. **Draft recommendation.** Provide a draft recommendation for attorney consideration, explicitly labeled `[ATTORNEY TO CONFIRM]`. The recommendation should identify: the triage rating and its rationale in one sentence; the response option the memo assesses as most consistent with the client's disclosed posture and the letter's apparent strength; and the most critical immediate action. Conclude with: *This recommendation is a draft for attorney review. The attorney must evaluate the merits, verify the applicable legal standards, and approve any response before the client acts.*

10. **Assemble the output** in the format below. Label the document as a draft cease-and-desist response triage memo for attorney review.

## Output Format

Deliver a document labeled:

> **DRAFT — CEASE AND DESIST RESPONSE TRIAGE MEMO**
> *Attorney review required before client responds, ignores, or commits to any course of action. This is not legal advice.*

Sections in order:

1. **Assertion Summary** — what the letter claims, verbatim where material.
2. **Assessment of Asserted Right** — preliminary observations on the claimed right's facial strength, flagged for verification.
3. **Exposure Assessment** — based on the client's disclosed facts; gap analysis; collateral stakes.
4. **Triage Rating** — rating, rationale, and the explicit caveat that it is a structured read, not a merits opinion.
5. **Response Options** — each option with advantage and risk.
6. **Deadline Triage** — stated deadline(s) with `[deadline verification required]`; counsel verification items.
7. **Immediate Actions** — legal hold flag, matter opening, counsel assignment, insurance notification, other.
8. **Draft Recommendation** — marked `[ATTORNEY TO CONFIRM]`.
9. **Assumptions and Missing Information** — list everything assumed and every input that was not provided.
10. **Attorney Verification Items** — drawn from the checklist below.

Use `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[citation needed]`, `[verify jurisdiction]`, and `[deadline verification required]` throughout wherever information is unverified, uncertain, or jurisdiction-dependent.

## Attorney Verification Checklist

- [ ] The letter reviewed is complete, authentic, and the most recent communication from the sender.
- [ ] The sender's asserted registration(s) or rights have been independently verified for status and validity (registration number, owner of record, goods/services covered, any office actions or cancellation proceedings).
- [ ] The applicable legal test for the asserted right (e.g., likelihood of confusion, substantial similarity, claim construction) has been confirmed under the governing jurisdiction's law.
- [ ] The client's factual self-assessment has been reviewed for completeness and accuracy; no material facts have been omitted.
- [ ] The triage rating has been reviewed in light of facts not disclosed in this memo; the rating is not treated as a legal opinion.
- [ ] Every stated or implied deadline has been independently verified; counsel has confirmed whether and how any deadline binds the client.
- [ ] A legal hold has been considered and issued or affirmatively declined based on counsel's assessment of the preservation duty.
- [ ] Applicable insurance policies have been reviewed for coverage and notice requirements.
- [ ] The governing law and jurisdiction have been confirmed; any jurisdiction-specific defenses or procedural options (e.g., declaratory judgment, cancellation, laches, fair use) have been evaluated.
- [ ] The recommended response option has been selected or modified by counsel and all assumptions in the draft recommendation have been resolved.
- [ ] No legal authority cited or implied in this memo has been asserted without independent verification.
- [ ] Client confidentiality and attorney-client privilege have been maintained throughout.
