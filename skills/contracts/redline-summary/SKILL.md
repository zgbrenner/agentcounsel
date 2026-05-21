---
name: Redline Summary
description: Use when summarizing the substantive changes between two versions of a contract, a set of tracked changes, or a base agreement plus a series of amendments — to produce a change-by-change table and narrative of the most material shifts for attorney review.
---

# Redline Summary

## Purpose

Produce a structured, attorney-ready summary of the substantive edits between two versions of a contract, or within a single document containing tracked changes, or across a base agreement and a series of amendments. For each change, this skill identifies what was modified, which party the change favors, whether the change is material, and whether it warrants pushback or further negotiation. When an amendment chain is provided, the skill also establishes the chronological order of the documents and traces how the agreement has evolved across the entire chain. It produces draft legal work product for attorney review only. It is not legal advice and does not constitute a final negotiating position.

The core discipline of this skill: **report only edits that are actually present in the provided documents.** Do not invent, interpolate, or assume changes that are not visible in the text. Do not characterize a change as "standard" or "acceptable" without flagging that characterization for attorney confirmation.

## Use When

- A counterparty has returned a redlined draft and the user needs a structured summary of what changed.
- The user asks to "summarize the redlines," "what did they change," "walk me through the markups," or "what should I push back on."
- The user has two versions of a contract (clean or tracked) and needs to understand what is different between them.
- Negotiations have progressed through multiple rounds and the user needs a record of which issues have moved and which remain open.
- An in-house team needs a quick summary of outside counsel redlines before a negotiation call.
- The user wants to compare a counterparty's proposed edits against the client's original draft to assess concession patterns.
- The user has a base agreement plus one or more amendments and needs to understand how the contract has evolved across the full amendment history.
- The user needs to trace a specific provision through multiple amendments to determine its current controlling language.

## Required Inputs

- **Both contract versions** — the base version (typically the client's draft or the prior round) and the revised version (the counterparty's return or the new round). Both are required; do not proceed with only one version.
- **OR a single document with accepted tracked changes visible** — the tracked-change markup must be present in the document, not a clean copy.
- **OR a base agreement plus a series of amendments** — all documents in the amendment chain are required. Provide the base agreement and each amendment in order. If ordering is ambiguous, the skill will attempt to sequence by execution date or amendment number/title and flag any inferred ordering for confirmation. [CONFIRM: amendment ordering before proceeding]
- **The client's role** — which party is the client? This determines which party each change favors.
- **Context** — what stage of negotiation is this, or what is the purpose of the amendment-chain review? (e.g., first redline return, third round, pre-execution final review, amendment history audit)
- **Optional — Provision-trace target** — if the user wants to trace a single provision through all versions, identify the provision by section number, clause title, or subject matter.

If only one version is provided (and no amendment chain), stop and request the other. If a clean document is provided without tracked changes and without a base version or amendment chain, stop and explain that a comparison cannot be performed.

## Do Not Use When

- The user needs a full risk review of a contract from scratch (use `contract-risk-review`).
- The user needs to review an NDA for the first time without a prior version (use `nda-review`).
- The user needs to review a statement of work (use `sow-review`).
- The document has no prior version and no tracked changes — a first-pass review is needed instead of a change summary.
- The user needs a legal opinion on whether the changes are acceptable — that requires attorney judgment this skill does not substitute for.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Summarize only edits that are actually present in the provided documents. Do not invent, assume, or interpolate changes.
- Quote the before and after language accurately. Do not paraphrase beyond what the text supports.
- Do not characterize any change as "standard," "acceptable," "market," or "not material" without explicitly flagging that characterization for attorney verification.
- Do not assess strategic concession strategy; flag strategic items for attorney judgment.
- Do not invent statutes, regulations, case law, or market-standard claims.
- Identify (or flag as unknown) the governing law, the document version identifiers, and the parties.
- Do not place client-sensitive facts into reusable templates.
- Use `[CONFIRM: ...]` placeholders wherever document version, authorship, or intent is uncertain.
- If the tracked changes are ambiguous — e.g., a deletion that is unclear from context — flag the ambiguity rather than resolving it.

## Workflow

1. **Confirm inputs.** Verify that you have both versions (or a tracked-change document, or the full amendment chain) and the client's role. If a required document is missing or tracking is not visible, stop and request it. If a provision-trace was requested, confirm the target provision.

2. **Establish document order (amendment chains only).** If a base agreement plus amendments is provided, arrange the documents in chronological order. Use execution dates as the primary ordering signal. If dates are missing or ambiguous, use amendment numbers or titles. State the resulting sequence explicitly and flag any inferred ordering for confirmation: `[CONFIRM: amendment sequence is Base Agreement → Amendment No. 1 (dated [CONFIRM: ___]) → ...]`. Do not proceed with the chain analysis until the sequence is confirmed or flagged.

3. **Orient.** State the document title, the versions or amendment sequence being reviewed, the client's role, and the purpose of the review (negotiation stage or amendment-history audit). For an amendment chain, state the span covered (base agreement date through most recent amendment date).

4. **Inventory the changes.** Read through all documents and identify every substantive change — additions, deletions, and substitutions — against the immediately preceding version in the chain. Do not skip changes based on apparent triviality; include all and rate materiality separately. For amendment chains, attribute each change to the specific amendment that introduced it.

5. **Classify each change.** For each identified change:
   - **Location** — section number and clause topic.
   - **Source** — for amendment chains, which amendment introduced this change.
   - **What changed** — before (prior version or base agreement) and after (revised version), quoted or closely paraphrased.
   - **Party favored** — does the change favor the client, the counterparty, or is it neutral / bilateral?
   - **Materiality** — High / Medium / Low.
   - **Nature** — categorize as: Risk Shift, Scope Change, Financial Term, IP / Ownership, Confidentiality, Liability / Indemnity, Termination, Procedural / Administrative, or Other.
   - **Warrants pushback?** — Yes / No / Attorney judgment required.
   - **Suggested response** — if pushback is warranted, a short note on the client's position or fallback.

6. **Provision-trace (optional).** If a provision-trace was requested, produce a separate trace for the target provision showing its language at every stage of the chain in chronological order. For each version: state the version/amendment name, quote the operative text of the provision (or note "not present" if the provision did not yet exist or was deleted), and state what changed from the prior version. Conclude with a plain-language statement of what the provision currently provides. Use `[CONFIRM: ...]` if any version's text is ambiguous or if the provision's location shifted between versions.

7. **Identify watch-items.** Scan the full set of changes for amendment-specific problems that require attorney attention but should not be resolved by this skill. Flag, do not resolve, any of the following:
   - Section numbers or cross-references in an amendment that no longer match the base agreement or a prior amendment (e.g., the amendment references "Section 4.2" but that section was renumbered or deleted). `[VERIFY: cross-reference accuracy]`
   - A provision that was deleted in one amendment and then purportedly modified or referenced in a later amendment, creating a gap or inconsistency. `[VERIFY: provision deletion/re-modification conflict]`
   - Changes in party names, entity names, or defined terms across versions that may or may not have been carried through consistently. `[VERIFY: defined-term and party-name consistency across chain]`
   - Any direct inconsistency between the terms of two amendments (e.g., conflicting definitions, overlapping scope changes) where the controlling version is unclear. `[VERIFY: inter-amendment inconsistency — confirm which version controls]` [verify jurisdiction]
   - Any other drafting anomaly introduced by the amendment structure that an attorney should review before relying on the document.

8. **Identify concession patterns.** Across all changes, note whether the counterparty's edits reflect a consistent strategy (e.g., shifting liability, narrowing scope, weakening client protections) or are isolated adjustments. For amendment chains, note whether the direction of concessions has shifted across amendments.

9. **Identify open items.** Note any issues from the prior round that were not addressed in this revision — unresolved open items are a negotiation tracking point.

10. **Draft the narrative summary.** Write a short (one to two paragraph) narrative describing the most material shifts in this redline round (or across the amendment chain), the overall direction of the counterparty's edits, and the top issues requiring attorney attention.

11. **List open items for attorney verification.**

12. **Assemble the output** and label it as a draft for attorney review.

## Output Format

Deliver, in order:

1. **Header** — Document title, base version and all amendments in sequence (or the two versions being compared), client's role, negotiation stage or review purpose, review date. For amendment chains, include the confirmed document sequence with dates or amendment numbers. Flag any inferred ordering: `[CONFIRM: ...]`.
2. **Change-by-Change Table** — one row per substantive change, with columns: # | Source (amendment or round) | Section | Clause Topic | What Changed (Before → After) | Party Favored | Materiality (High/Med/Low) | Nature | Warrants Pushback (Yes/No/Attorney) | Suggested Response. For two-version comparisons, the Source column may be omitted.
3. **Materiality Summary** — count of High / Medium / Low items; count of changes favoring client vs. counterparty vs. neutral. For amendment chains, break down by amendment if the volume warrants it.
4. **Watch-Items** — a dedicated list of amendment-specific problems flagged for attorney review (see Workflow step 7): mismatched cross-references, deletion/re-modification conflicts, party-name or defined-term inconsistencies, inter-amendment conflicts, and other drafting anomalies. Each item should identify the affected amendment(s), the specific provisions involved, and the nature of the concern. Do not resolve these items; flag each with the appropriate `[VERIFY: ...]` placeholder.
5. **Provision Trace (if requested)** — a chronological trace of the target provision through every version, showing the operative text at each stage and concluding with a plain-language statement of current controlling language. Flag ambiguities with `[CONFIRM: ...]`.
6. **Concession Pattern Analysis** — brief note on any consistent counterparty strategy visible across the redlines or amendment history.
7. **Unresolved Prior-Round Issues** — list of issues flagged in prior rounds that were not addressed in this revision (if applicable and known).
8. **Narrative Summary** — one to two paragraphs on the most material shifts and top priorities for the next negotiation step or for attorney review of the amendment history.
9. **Open Items for Attorney Verification** — checkbox list.
10. **Assumptions** — explicit list.

Use `[CONFIRM: ...]` wherever document version, authorship, amendment ordering, or change intent is uncertain.

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] All versions, documents, or amendments compared are the correct and complete documents for this review.
- [ ] The version labels, dates, party attributions, and (for amendment chains) the document sequence are accurate and confirmed.
- [ ] All substantive changes have been identified across all documents in scope; no changes have been missed.
- [ ] All "Before → After" quotations match the source documents.
- [ ] Party-favored assessments correctly reflect the client's actual contractual role.
- [ ] Materiality ratings reflect the client's specific business context, risk tolerance, and deal value.
- [ ] No change has been characterized as "standard," "market," or "acceptable" without independent attorney verification.
- [ ] Unresolved prior-round issues have been identified and tracked.
- [ ] Strategic recommendations in the "Suggested Response" column have been reviewed and approved by the supervising attorney before use in negotiation.
- [ ] All watch-items (cross-reference mismatches, deletion/re-modification conflicts, term inconsistencies, inter-amendment conflicts) have been reviewed and resolved by attorney before relying on any amendment for its terms.
- [ ] If a provision trace was produced, the quoted operative text at each step matches the source documents, and the statement of current controlling language has been independently confirmed. [verify jurisdiction] for any rule governing which amendment controls in case of conflict.
- [ ] All `[CONFIRM: ...]` and `[VERIFY: ...]` placeholders and open items have been resolved before the summary is relied upon.
