---
name: DPA Review
description: "Use when reviewing a data processing agreement (DPA) or data processing addendum to produce a structured risk summary and prioritized issues for attorney review."
practice_area: privacy
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The data processing agreement or addendum text"
  - "The client's role: controller, processor, or sub-processor"
  - "The processing context and the data involved"
outputs:
  - "Structured risk summary"
  - "Prioritized issues for attorney review"
related_skills:
  - skills/privacy/privacy-policy-gap-review/SKILL.md
  - skills/privacy/dsar-workflow/SKILL.md
  - skills/contracts/contract-risk-review/SKILL.md
tags:
  - privacy
  - dpa
  - data-processing
  - contract-review
  - data-protection
---

# DPA Review

## Purpose

Produce a structured, attorney-ready review of a data processing agreement (DPA) or data processing addendum. A DPA governs the relationship between a controller and a processor (or between a processor and a sub-processor) when personal data is processed on behalf of another party. This skill assesses role designation, scope and instructions, security obligations, sub-processor terms, data subject rights assistance, breach notification, audit rights, cross-border transfer mechanisms, deletion and return obligations, and the liability and indemnity interplay with the main commercial agreement. It produces draft legal work product for attorney review — not legal advice.

Which privacy laws, frameworks, or regulations apply — and what they require — are attorney-verification items. This skill organizes the review; it does not assert what any law mandates.

## Use When

- A user asks to "review this DPA," "redline the data processing addendum," or "flag the risks in this data processing agreement."
- The organization is being asked to sign a vendor DPA or is preparing its own DPA for a customer.
- A DPA has been updated by the other party and the user needs to identify what changed and whether new risks arise.
- A DPA is being negotiated and the user wants a structured issue list before the next round.
- An internal team (legal ops, procurement, privacy) needs a first-pass risk summary before attorney review.
- Due diligence on a transaction requires assessment of the target's data processing arrangements.

## Required Inputs

- **The full DPA text** (uploaded, pasted, or linked). If the document is not provided, stop and request it. Do not draft a hypothetical review.
- **The client's role**: controller, processor, or sub-processor. If unclear from the document, flag as `[CONFIRM: client role]` and note that the risk assessment will differ materially depending on the answer.
- **The main commercial agreement** (or a description of it), if available — needed to assess the liability and indemnity interplay. If not provided, note the gap and flag it as an attorney-verification item.
- Optional: the applicable privacy framework(s) or regulation(s) the parties have identified (e.g., the DPA references GDPR, CCPA/CPRA, or another framework). Note these as stated in the document; do not independently assert which law applies.
- Optional: any prior version of the DPA or a markup showing changes, if this is a revision review.
- Optional: the practice group's `practice-profiles/privacy.md` if it has been populated and is loaded alongside this skill. If present, the skill uses its Standard Positions and Escalation Thresholds tables to benchmark the output and to gate escalation. If absent, the skill proceeds without practice-profile benchmarking and asks the user to supply standing positions inline if needed.

If the DPA text is missing, stop and request it. Never fabricate document terms or infer what a DPA "probably says."

## Do Not Use When

- The document is a privacy policy or privacy notice, not a DPA (use `privacy-policy-gap-review`).
- The user needs to handle an incoming data subject request (use `dsar-workflow`).
- The document is a general commercial contract with data protection provisions as one small component — assess using `contract-risk-review` and flag the data provisions separately.
- The task is to draft a DPA from scratch without a base document — that requires attorney drafting, not a review workflow.
- The user needs a determination of which law applies or whether a DPA is legally required — those are attorney-judgment items.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Do not assert which privacy law or regulatory framework applies to any given processing arrangement. The applicable law is always an attorney-verification item.
- Do not invent, paraphrase, or assume document provisions. Review only the language actually present in the provided document. Quote the document directly when characterizing its terms.
- Do not state or compute statutory response deadlines, notification periods, or regulatory timeframes. Mark all such timeframes as `[CONFIRM: verify deadline under applicable law]`.
- Distinguish clearly: (1) what the document says, (2) what you are assuming about context, (3) what requires legal verification.
- The designation of a party as "controller," "processor," or "sub-processor" carries legal significance that varies by jurisdiction and framework. Flag this role assessment as `[CONFIRM]` — do not treat the document's own labels as necessarily correct or complete.
- Do not place client-sensitive facts or deal-specific information into the reusable risk table template.
- Use `[CONFIRM: ...]` for every point where the legal consequence, applicable rule, or factual context is uncertain.
- Flag but do not resolve: conflicts between the DPA and the main agreement; gaps in the DPA relative to any stated regulatory requirement; provisions that may be unenforceable or non-standard.
- Adverse provisions (provisions unfavorable to the client) must be identified even if the other party's position is commercially common.
- **Severity floor.** Once an issue has been rated High severity in the risk table, that rating must not be silently downgraded. Any reduction in severity is an explicit attorney decision and must be recorded as such (e.g., "Downgraded from High to Medium by [attorney], [date], reason: [brief rationale]"). This applies regardless of the counterparty's explanation or commercial commonness of the provision. Where `practice-profiles/privacy.md` is loaded, the profile's Escalation Thresholds for DPA terms (e.g., minimum acceptable sub-processor approval mechanism, breach-reporting timeline floor, audit-rights floor, SCC-modification posture) inform what constitutes High; the loaded thresholds apply alongside, not instead of, the inline ratings.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/privacy.md` is loaded, its Standard Positions and Escalation Thresholds inform the draft but never substitute for attorney judgment. The profile is a configuration record approved by the practice group; it is not legal advice and does not override the skill's normal attorney-verification gates. If the profile's standing positions conflict with the matter facts or with what the supervising attorney concludes, the attorney prevails.

## Workflow

1. **Confirm inputs.** Verify that the DPA text has been provided and that the client's role is identified or can be flagged. Note whether the main commercial agreement is available. If the DPA text is missing, stop.

2. **Identify the document and parties.** Note the document title, version or date if stated, and the party names. Identify how the document designates each party's role (controller, processor, sub-processor). Flag the role designations as `[CONFIRM: client role and counterparty role under applicable law]`.

3. **Map the document structure.** List the sections and their subjects. Note any sections that appear to be missing relative to a standard DPA structure (scope, instructions, security, sub-processors, data subject rights, breach notification, audit, transfers, deletion, liability). Missing sections are automatic risk flags.

4. **Assess scope and nature of processing.** Identify what personal data categories, data subjects, processing purposes, and processing activities are described. Flag vague or overbroad descriptions as risk items. Note whether the scope matches the commercial relationship as described by the user.

5. **Sectoral-overlay check.** Before proceeding to the term-by-term review, assess whether the personal data categories or processing context identified in step 4 may trigger a sector-specific regulatory regime that overlays additional requirements on top of general data-protection law. Common sectors to consider include — but are not limited to — financial or banking data, health or medical data, children's or minors' data, and education records. This check is not exhaustive; the applicable sectors depend on the jurisdiction and factual context `[verify jurisdiction]`. Where a sectoral overlay may apply: (a) flag it prominently as `[CONFIRM: possible sectoral overlay — specialist review recommended]`; (b) note which data categories or processing activities trigger the concern; and (c) state that the sectoral requirements may change the analysis of several DPA terms reviewed in subsequent steps (e.g., security standards, breach notification timelines, deletion obligations). Do not assert which sectoral law applies or what it requires — those are attorney-verification items.

6. **Review processing instructions.** Assess whether the processor is limited to acting on the controller's documented instructions, and what carve-outs exist (e.g., legal obligation processing). Flag any broad discretion granted to the processor.

7. **Assess sub-processor provisions.** Identify: whether sub-processor use requires prior written approval or general authorization; the notice and objection mechanism; whether the processor must impose equivalent obligations on sub-processors; and whether a sub-processor list is referenced or provided. Flag gaps or weak controls.

8. **Review security measures.** Note what security obligations are specified — whether they reference a standard (e.g., ISO 27001, SOC 2) or are described in general terms only. Flag lack of specificity, absence of minimum standards, and whether security obligations are symmetric or asymmetric.

9. **Review data subject rights assistance.** Assess whether the processor is obligated to assist the controller in responding to data subject requests, what the scope of that assistance is, and whether it is time-limited. Flag vague or absent assistance obligations.

10. **Review breach notification.** Identify the notification trigger, the notification period, and the required content of notification. Mark any stated timeframe as `[CONFIRM: verify deadline under applicable law and contract]`. Flag absence of breach notification provisions.

11. **Review audit rights.** Identify whether the controller has the right to audit the processor, how audits are triggered and conducted, notice requirements, cost allocation, and whether third-party audit reports are accepted as a substitute. Flag provisions that significantly restrict audit rights.

12. **Review cross-border transfer mechanism.** Identify how the DPA addresses transfers of personal data across borders (e.g., by reference to standard contractual clauses, binding corporate rules, adequacy decisions, or other mechanisms). Do not assess whether any mechanism is legally valid — flag for attorney review. Note if no transfer mechanism is addressed. Additionally:
    - **TIA reference check.** If the transfer mechanism cited relies on SCCs or equivalent contractual mechanism, note whether the DPA references or attaches a Transfer Impact Assessment (TIA) or equivalent supplementary-measures analysis. Absence of a TIA reference where one is doctrinally expected is itself a flag `[verify jurisdiction]`.
    - **SCC-modification check.** If the DPA incorporates SCCs by reference, note whether the SCCs are referenced as-issued or with modifications. Material modification of SCC text is generally not permitted under the SCC terms themselves and is a flag for specialist review.
    - **Annex/Schedule completeness.** Standard SCC structure requires processing-description annexes (parties, categories of data, processing purposes, security measures). Note whether the DPA includes these annexes and whether each annex is completed (not left in template form).

13. **Review deletion and return obligations.** Identify what happens to personal data on termination or expiration — whether the processor must return, delete, or certify destruction, within what timeframe, and with what exceptions (e.g., legal retention obligations). Flag absence or vagueness.

14. **Assess liability and indemnity interplay.** Identify liability caps, exclusions, and indemnity obligations in the DPA, and note any stated relationship to the main commercial agreement's liability regime. Flag conflicts, gaps, or provisions that may effectively remove the processor's liability for data breaches.

15. **Build the risk table.** Populate `templates/dpa-risk-table.md` with one row per identified issue, severity-rated High / Medium / Low.

16. **Draft prioritized issue list.** Organize findings: (1) High-severity issues requiring redline or walkaway consideration; (2) Medium-severity issues for negotiation; (3) Low-severity issues or minor drafting improvements.

17. **List attorney verification items.** Enumerate every open legal question — applicable law, role confirmation, regulatory deadline, transfer mechanism validity, liability cap adequacy — that requires attorney judgment.

18. **Assemble output** and label it as draft legal work product for attorney review.

## Output Format

Deliver the following, in order:

1. **Summary** — one paragraph identifying the document, parties, client role (with `[CONFIRM]` if uncertain), and the top three to five risks.
2. **Document Structure Map** — list of sections present and any standard sections that appear to be absent.
3. **Risk Table** — completed `templates/dpa-risk-table.md`, with one row per issue.
4. **Prioritized Issue List** — organized as High / Medium / Low, with plain-language description of each issue and its risk to the client.
5. **Liability and Indemnity Note** — specific observations on the interplay between the DPA's liability provisions and the main agreement.
6. **Attorney Verification Items** — see the Attorney Verification Checklist below.
7. **Assumptions** — explicit list of every assumption made in the review (about role, context, applicable framework, etc.).

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] The document reviewed is the complete, executed or near-final version — no sections are missing or truncated.
- [ ] Any sectoral-overlay flag (`[CONFIRM: possible sectoral overlay]`) has been reviewed by an attorney with relevant sector expertise, and the analysis of affected DPA terms has been updated accordingly `[verify jurisdiction]`.
- [ ] All High-severity issues remain rated High unless an attorney has explicitly documented the rationale for any downgrade, including their name and the date of the decision.
- [ ] The client's role (controller, processor, or sub-processor) is correctly identified under the applicable legal framework — the document's labels alone are not conclusive.
- [ ] The applicable privacy law(s) and regulatory framework(s) have been confirmed, and the DPA satisfies their requirements for a lawful processing arrangement.
- [ ] All statutory or regulatory deadlines referenced in or relevant to the DPA (especially breach notification periods) have been confirmed under current law — no deadline stated in this review has been computed or assumed.
- [ ] The sub-processor approval and notice mechanism is consistent with applicable law and the client's operational requirements.
- [ ] The cross-border transfer mechanism is valid and currently recognized under applicable law.
- [ ] If the transfer mechanism relies on SCCs: any modifications to the SCC text have been identified and reviewed by transfer-mechanism specialist counsel; required annexes are present and completed; and the TIA or equivalent supplementary-measures analysis has been performed or routed to specialist counsel `[verify jurisdiction]`.
- [ ] Security obligations meet applicable legal minimums and the client's risk tolerance.
- [ ] The liability cap in the DPA is appropriate relative to the potential exposure from a data breach or regulatory fine.
- [ ] The DPA is consistent with the main commercial agreement; any conflicts have been identified and resolved.
- [ ] All `[CONFIRM: ...]` placeholders in the risk table and issue list have been resolved before the review is relied upon.
- [ ] No legal authority, regulatory requirement, or deadline has been asserted in this review without attorney verification.
- [ ] Privilege and confidentiality designations are appropriate for the matter.
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged; profile-silent items are flagged as not-yet-addressed by the playbook.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.
