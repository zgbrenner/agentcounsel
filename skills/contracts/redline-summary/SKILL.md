---
name: Redline Summary
description: Use when summarizing the substantive changes between two versions of a contract — or a set of tracked changes — to produce a change-by-change table and narrative of the most material shifts for attorney review.
---

# Redline Summary

## Purpose

Produce a structured, attorney-ready summary of the substantive edits between two versions of a contract, or within a single document containing tracked changes. For each change, this skill identifies what was modified, which party the change favors, whether the change is material, and whether it warrants pushback or further negotiation. It produces draft legal work product for attorney review only. It is not legal advice and does not constitute a final negotiating position.

The core discipline of this skill: **report only edits that are actually present in the provided documents.** Do not invent, interpolate, or assume changes that are not visible in the text. Do not characterize a change as "standard" or "acceptable" without flagging that characterization for attorney confirmation.

## Use When

- A counterparty has returned a redlined draft and the user needs a structured summary of what changed.
- The user asks to "summarize the redlines," "what did they change," "walk me through the markups," or "what should I push back on."
- The user has two versions of a contract (clean or tracked) and needs to understand what is different between them.
- Negotiations have progressed through multiple rounds and the user needs a record of which issues have moved and which remain open.
- An in-house team needs a quick summary of outside counsel redlines before a negotiation call.
- The user wants to compare a counterparty's proposed edits against the client's original draft to assess concession patterns.

## Required Inputs

- **Both contract versions** — the base version (typically the client's draft or the prior round) and the revised version (the counterparty's return or the new round). Both are required; do not proceed with only one version.
- **OR a single document with accepted tracked changes visible** — the tracked-change markup must be present in the document, not a clean copy.
- **The client's role** — which party is the client? This determines which party each change favors.
- **Context** — what stage of negotiation is this? (e.g., first redline return, third round, pre-execution final review)

If only one version is provided, stop and request the other. If a clean document is provided without tracked changes and without a base version, stop and explain that a comparison cannot be performed.

## Do Not Use When

- The user needs a full risk review of a contract from scratch (use `contract-risk-review`).
- The user needs to review an NDA for the first time without a prior version (use `nda-review`).
- The user needs to review a statement of work (use `sow-review`).
- The document has no prior version and no tracked changes — a first-pass review is needed instead of a change summary.
- The user needs a legal opinion on whether the changes are acceptable — that requires attorney judgment this skill does not substitute for.

## Legal Safety Rules

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

1. **Confirm inputs.** Verify that you have both versions (or a tracked-change document) and the client's role. If either version is missing or the tracking is not visible, stop and request it.

2. **Orient.** State the document title, the two versions being compared (version labels, dates, or party identifiers), the client's role, and the stage of negotiation.

3. **Inventory the changes.** Read through the full document and identify every substantive change — additions, deletions, and substitutions. Do not skip changes based on apparent triviality; include all and rate materiality separately.

4. **Classify each change.** For each identified change:
   - **Location** — section number and clause topic.
   - **What changed** — before (base version) and after (revised version), quoted or closely paraphrased.
   - **Party favored** — does the change favor the client, the counterparty, or is it neutral / bilateral?
   - **Materiality** — High / Medium / Low.
   - **Nature** — categorize as: Risk Shift, Scope Change, Financial Term, IP / Ownership, Confidentiality, Liability / Indemnity, Termination, Procedural / Administrative, or Other.
   - **Warrants pushback?** — Yes / No / Attorney judgment required.
   - **Suggested response** — if pushback is warranted, a short note on the client's position or fallback.

5. **Identify concession patterns.** Across all changes, note whether the counterparty's edits reflect a consistent strategy (e.g., shifting liability, narrowing scope, weakening client protections) or are isolated adjustments.

6. **Identify open items.** Note any issues from the prior round that were not addressed in this revision — unresolved open items are a negotiation tracking point.

7. **Draft the narrative summary.** Write a short (one to two paragraph) narrative describing the most material shifts in this redline round, the overall direction of the counterparty's edits, and the top issues requiring attorney attention.

8. **List open items for attorney verification.**

9. **Assemble the output** and label it as a draft for attorney review.

## Output Format

Deliver, in order:

1. **Header** — Document title, base version, revised version, client's role, negotiation stage, review date.
2. **Change-by-Change Table** — one row per substantive change, with columns: # | Section | Clause Topic | What Changed (Before → After) | Party Favored | Materiality (High/Med/Low) | Nature | Warrants Pushback (Yes/No/Attorney) | Suggested Response.
3. **Materiality Summary** — count of High / Medium / Low items; count of changes favoring client vs. counterparty vs. neutral.
4. **Concession Pattern Analysis** — brief note on any consistent counterparty strategy visible across the redlines.
5. **Unresolved Prior-Round Issues** — list of issues flagged in prior rounds that were not addressed in this revision (if applicable and known).
6. **Narrative Summary** — one to two paragraphs on the most material shifts and top priorities for the next negotiation step.
7. **Open Items for Attorney Verification** — checkbox list.
8. **Assumptions** — explicit list.

Use `[CONFIRM: ...]` wherever document version, authorship, or change intent is uncertain.

## Attorney Verification Checklist

- [ ] Both versions compared are the correct and complete documents for this round.
- [ ] The version labels, dates, and party attributions are accurate.
- [ ] All substantive changes have been identified; no changes have been missed.
- [ ] All "Before → After" quotations match the source documents.
- [ ] Party-favored assessments correctly reflect the client's actual contractual role.
- [ ] Materiality ratings reflect the client's specific business context, risk tolerance, and deal value.
- [ ] No change has been characterized as "standard," "market," or "acceptable" without independent attorney verification.
- [ ] Unresolved prior-round issues have been identified and tracked.
- [ ] Strategic recommendations in the "Suggested Response" column have been reviewed and approved by the supervising attorney before use in negotiation.
- [ ] All `[CONFIRM: ...]` placeholders and open items have been resolved before the summary is relied upon.
