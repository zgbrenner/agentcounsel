---
name: Written Consent
description: "Use when drafting a board or board-committee action by written consent in lieu of a meeting to produce a structured draft for attorney review."
practice_area: corporate
task_type: drafting
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The corporate action to be approved"
  - "The signatories and the approving body"
  - "The intended effective date"
outputs:
  - "Draft action by written consent for attorney review and sign-off"
related_skills:
  - skills/corporate/board-minutes/SKILL.md
tags:
  - corporate
  - governance
  - written-consent
  - board-action
  - drafting
---

# Written Consent

## Purpose

Produce a structured, attorney-ready draft of a corporate action taken by written consent in lieu of a meeting. The skill drafts the consent instrument — recitals, resolved paragraphs, and signature blocks — classifies the action as routine or major, flags any director conflicts, and surfaces open verification items. It produces draft legal work product for attorney review — not legal advice, not an executed corporate record, and not authorization to act.

## Use When

- A user asks to "draft a written consent," "prepare a board consent," or "document a board action in lieu of a meeting."
- The board of directors or a board committee is taking a formal action outside a meeting and needs a consent instrument to evidence that action.
- The user has a specific corporate action to document — for example, an officer appointment, an equity grant, a financing approval, or a contract authorization — and the relevant body is acting by written consent rather than at a noticed meeting.
- A precedent consent is available for format reference and the user wants to conform the draft to the company's house style.

## Required Inputs

- **Action description.** A clear, one-sentence description of the action being approved (e.g., "appointment of Jane Smith as Chief Financial Officer effective June 1").
- **Supporting detail.** Names, titles, amounts, counterparty identities, and any specific agreement or instrument that the action authorizes, approves, or references. The more detail provided, the more precise the recitals and resolved paragraphs can be.
- **Effective date.** The date on which the consent is to take effect. If not provided, flag as `[CONFIRM: effective date]` and note that the effective date is a legal determination in some jurisdictions.
- **Signatories.** The full board, a named committee, or a specific subset, with each signatory's full name and title. If not provided, the draft cannot include accurate signature blocks; stop and request this information.
- **Director conflicts.** Whether any signatory has a disclosed financial or other interest in the action. Even a "none known" confirmation is useful.
- **Optional — precedent consent.** A prior consent from the company for format and house-style reference. If not provided, the draft uses the neutral standard form in `templates/written-consent-outline.md` and flags it to be conformed to house style.

If the action description or the signatory list is not provided, stop and request it before proceeding. Do not fabricate names, titles, amounts, or agreement terms.

## Do Not Use When

- The board is acting at a duly noticed meeting (use `board-minutes` to document that action instead).
- The user is asking whether board approval is legally required for the action — that is a legal determination for the attorney and is outside this skill's scope.
- The user wants advice on fiduciary duties, the business judgment rule, or how a director conflict should be resolved — flag those issues and refer them to the attorney.
- The action is of a type that categorically requires a shareholder vote, a regulatory filing, or a specific court or governmental approval; flag and refer to the attorney.
- The user wants to circulate or obtain signatures on the consent — this skill produces a draft instrument for attorney review and sign-off, not a circulated execution copy.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- An executed written consent is a corporate record. The draft produced by this skill is work product only; it must not be circulated for signature, treated as effective, or filed anywhere without attorney review and sign-off.
- Do not invent names, titles, amounts, dates, agreement terms, or factual recitals. Every factual element in the draft must come from the inputs provided; flag anything missing with `[CONFIRM: ...]`.
- Do not assert or apply any jurisdiction-specific statute, corporate code section, case law, or regulatory requirement. Consent rules — unanimity, majority threshold, notice, signature form, counterparts permissibility, and any charter or bylaw override — vary by jurisdiction and by the entity's governing documents; treat all of them as `[verify jurisdiction]` unless the attorney confirms the applicable rule.
- Do not invent or assume an effective date. If disputed or missing, flag as `[CONFIRM: effective date — legal determination required in some jurisdictions]`.
- Classify the action as routine or major before drafting and apply the appropriate safeguard (see Workflow). Never mark a major-action consent as ready to sign without outside-counsel review.
- Flag any director conflict prominently and do not resolve it — resolving conflicts requires legal judgment.
- Distinguish what was provided by the user from what you assumed and from what the attorney must confirm.
- Preserve confidentiality and privilege: this draft is attorney work product. Do not carry client-sensitive facts into the reusable template.
- Flag every point of uncertainty rather than resolving it silently.

## Workflow

1. **Confirm inputs.** Verify you have the action description, supporting detail, effective date, and signatory list. If any required input is missing, request it. Note whether a precedent consent was provided.

2. **Identify the action.** Restate the action in precise terms. List the names, titles, amounts, instruments, and counterparties that will appear in the consent. Flag any element that is ambiguous, incomplete, or that you are inferring rather than drawing from the inputs, using `[CONFIRM: ...]`.

3. **Classify the action — routine or major.**

   - **Routine.** Examples: officer appointment or removal under existing authority; equity grant within an existing board-approved plan and within authorized limits; update to bank signatories; registered-agent or registered-office change; a standard commercial contract below a materiality threshold established in the governing documents or prior board authorization. Routine actions proceed to drafting with standard diligence.

   - **Major.** Examples: merger, acquisition, or material asset sale; a new debt or equity financing, a new credit facility, or any transaction that commits the company to material new obligations; issuance of equity to a new investor; a change of control transaction; an action that the charter, bylaws, or a material agreement requires board or stockholder approval for specifically; dissolution or winding up; a material real property transaction; any consent that is expected to become a due-diligence exhibit in a financing or M&A transaction.

   If the action is major: flag it prominently at the top of the draft as `[MAJOR ACTION — outside-counsel review required before consent is signed or effective]`. Do not mark a major-action consent as complete or ready to sign. If a major action is being rushed to same-day signature, flag that urgency as a serious concern and note that expedited attorney review, not waiver of review, is the appropriate response.

   If the classification is unclear, treat the action as major and flag the uncertainty.

4. **Identify applicable consent rules.** Note the questions the attorney must resolve before the consent can be finalized: the required approval threshold (unanimity, a majority, or another standard) `[verify jurisdiction]`; whether notice or advance circulation is required `[verify jurisdiction]`; the required form of signature and whether electronic or counterpart signatures are permitted `[verify jurisdiction]`; and whether the charter, bylaws, or any stockholder agreement contains overriding requirements `[ATTORNEY TO CONFIRM: governing documents]`. Do not state a rule as settled; surface the questions.

5. **Flag director conflicts.** If any signatory has a disclosed financial interest, familial relationship, or other potential conflict with respect to the action, flag the signatory by name using `[CONFLICT FLAGGED: attorney review required — [name]]`. Do not omit a known conflict. Do not advise on how to resolve it.

6. **Draft the consent instrument.** Using `templates/written-consent-outline.md` as the structural base:
   - Draft the header: entity name, the body acting (full board or named committee), and the effective date.
   - Draft the recitals (WHEREAS clauses): set out the factual background concisely — the authority of the body to act, the nature of the action, and any documents being approved or authorized.
   - Draft the RESOLVED paragraphs: one RESOLVED per discrete action being approved. State the action precisely. Where a document is being approved, reference it by title and date; use `[CONFIRM: agreement title and date]` if those details are missing. Where an officer is being authorized to take further action, identify the officer by name and title.
   - Add a FURTHER RESOLVED omnibus paragraph authorizing officers to execute any ancillary documents and take any further action necessary to carry out the consent, if appropriate.
   - Add counterparts language (flagged `[verify jurisdiction]` for permissibility and required form).
   - Populate signature blocks for each signatory with name, title, and a signature line.
   - If a precedent was provided, note where the draft departs from the precedent's format and flag those departures for attorney review.
   - If no precedent was provided, flag the entire draft as using a neutral standard form that should be conformed to the company's house style before execution.

7. **Compile open items.** Gather every `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and conflict flag from the draft into a consolidated checklist.

8. **Assemble the output.** Deliver the draft consent, the signatory and conflicts checklist, the open items list, and a list of assumptions made during drafting. Label the entire output as a draft for attorney review.

## Output Format

Deliver, in order:

1. **Action Classification** — ROUTINE or MAJOR, with a one-line rationale. If MAJOR, a prominent flag that outside-counsel review is required before the consent is signed or effective.
2. **Draft Written Consent** — from `templates/written-consent-outline.md`, fully populated with the inputs provided and bracketed placeholders where information is missing or must be confirmed.
3. **Signatory and Conflicts Checklist** — each signatory listed by name and title; any conflict flags noted.
4. **Consent-Rules Open Items** — the jurisdiction and governing-document questions the attorney must resolve before the consent is finalized (threshold, notice, signature form, governing-document overrides).
5. **Attorney Verification Items** — all `[CONFIRM]`, `[VERIFY]`, `[ATTORNEY TO CONFIRM]`, `[verify jurisdiction]`, and conflict flags consolidated in one place.
6. **Assumptions** — every assumption made during drafting, stated explicitly.

Use `[CONFIRM: ...]` for missing or unverified facts. Use `[verify jurisdiction]` for consent rules. Use `[ATTORNEY TO CONFIRM: ...]` for legal determinations. Do not fill any gap with invented content.

## Attorney Verification Checklist

- [ ] The action description and all supporting detail (names, titles, amounts, counterparties, instrument references) are accurate and complete.
- [ ] The body acting (full board or committee) has authority to take this action under the entity's governing documents and applicable law.
- [ ] The action has been correctly classified as routine or major; if major, outside-counsel review has been completed.
- [ ] The required approval threshold — unanimity, majority, or otherwise — has been confirmed under the governing documents and applicable law. `[verify jurisdiction]`
- [ ] Any notice or advance-circulation requirement has been satisfied or waived in the manner required by the governing documents and applicable law. `[verify jurisdiction]`
- [ ] Electronic signatures and/or counterpart execution are permitted in the applicable jurisdiction and under the governing documents. `[verify jurisdiction]`
- [ ] The effective date is correct and, where the effective date carries legal significance, has been confirmed by the attorney.
- [ ] All director conflicts have been identified, disclosed, and resolved in the manner required by the governing documents and applicable law; no conflicted director has voted on an action from which they should be recused.
- [ ] The recitals accurately reflect the factual background and do not contain inaccurate or misleading statements.
- [ ] Each RESOLVED paragraph states the action precisely; where an agreement or instrument is approved, it has been reviewed by the attorney and the title and date match the executed document.
- [ ] Any ancillary authorization in the consent is appropriately scoped and does not grant broader authority than intended.
- [ ] If the consent will become a due-diligence exhibit, it has been reviewed for completeness and accuracy in that context.
- [ ] The draft has been conformed to the company's house style and compared against any prior consent precedents.
- [ ] No legal authority, statute, or case law has been asserted in the draft without verification.
- [ ] All assumptions and open items are resolved before the consent is signed or treated as effective.
- [ ] Attorney sign-off has been obtained before the consent is circulated for signature or filed.
