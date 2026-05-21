---
name: Closing Checklist
description: Use when building or updating a transaction closing checklist — conditions precedent, closing deliverables, and pre-closing actions — and identifying what is blocking a deal closing, as draft work product for attorney review.
---

# Closing Checklist

## Purpose

Build and maintain a structured transaction closing checklist that captures every condition precedent, closing deliverable, and pre-closing covenant drawn from the transaction agreement. The skill can initialize a checklist from the agreement, fold in items surfaced by diligence, update item status, and produce a blocking and critical-path summary. It produces draft legal work product for attorney review — not legal advice and not a closing certification.

## Use When

- A deal team needs to initialize a closing checklist from a purchase agreement, merger agreement, or financing document.
- Diligence findings have surfaced pre-closing action items — consents, regulatory filings, board or shareholder approvals, releases, or escrow mechanics — that must be tracked to closing.
- The team needs to update the status of existing checklist items and surface what remains open.
- A deal is approaching signing or closing and the team wants a consolidated view of open conditions and deliverables for attorney review.
- The user asks for a "closing checklist," "conditions checklist," "pre-closing action list," or equivalent.

## Required Inputs

- **The transaction agreement** (purchase agreement, merger agreement, financing document, or equivalent) — required to initialize the checklist or verify item sourcing. Do not reconstruct or paraphrase conditions from memory or a description alone.
- **Deal context** — deal name, transaction structure (e.g., stock purchase, asset purchase, merger, or financing [CONFIRM: structure]), and parties. If any of these are missing, ask for them before proceeding.
- **Operating mode** — one of: **initialize** (build from the agreement), **add** (fold in diligence items), **update** (revise item status), or **status report** (surface blocking items and critical path).
- **Diligence findings** — required only for **add** mode; a list or memo of findings that carry pre-closing action items.
- **Existing checklist** — required for **update** and **status report** modes; provide the current checklist to be updated.

If the transaction agreement is not provided and the mode is **initialize**, stop and request it. Do not construct a checklist from deal-type assumptions alone. If the existing checklist is not provided for **update** or **status report** modes, stop and request it.

## Do Not Use When

- The user wants transaction documents drafted (a purchase agreement, merger agreement, ancillary documents, or similar) — route to the appropriate drafting skill.
- The user wants a diligence issues list or red-flag report — use `diligence-issue-extraction`.
- The user wants a material-contracts disclosure schedule built — use `material-contract-schedule`.
- The user wants a certification that closing conditions have been satisfied and the deal is ready to close — that is a legal conclusion requiring attorney review and sign-off; this skill does not produce it.
- The document provided is not a transaction agreement (use `contract-risk-review` for general commercial agreements).

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- A "closing-ready" determination — concluding that all conditions precedent have been satisfied and the deal may close — is a legal judgment. This skill produces a checklist and a blocking analysis to support that judgment; it does not make it. Attorney review and sign-off are required before a closing proceeds.
- Extract closing conditions and deliverables only from the language actually present in the provided agreement. Do not supplement from model background knowledge about what conditions are typical for a given deal type.
- Do not invent, compute, or assert any deadline. Every date field in the checklist is `[deadline verification required]` unless a date is expressly stated in the agreement or provided by the user as a confirmed fact.
- Do not state or imply jurisdiction-specific regulatory mechanics, filing requirements, waiting periods, or statutory timing. All such items are `[verify jurisdiction]` until an attorney confirms them.
- Do not invent responsible parties, consent counterparties, or regulatory bodies. If a condition references a party or authority not named in the agreement, flag it rather than guess.
- Distinguish what the agreement says from what you assume and from what the attorney must confirm. Separate facts, assumptions, analysis, and open verification items.
- A condition marked "Blocking: Yes" reflects that the agreement makes closing contingent on it, or that the user has designated it as blocking — not an independent legal conclusion about materiality or waivability.
- Preserve confidentiality and privilege. Do not include client-sensitive facts in reusable copies of this template.
- Flag every point of uncertainty with a placeholder rather than resolving it silently.

## Workflow

### Step 1 — Confirm inputs and mode

Identify the operating mode: **initialize**, **add**, **update**, or **status report**. Verify that all required inputs for the selected mode are present. If anything is missing, request it before proceeding.

Note the deal name, structure, and parties. Flag as `[CONFIRM: structure]` if the transaction structure is ambiguous.

### Step 2 — Initialize (from the transaction agreement)

*Skip to Step 3 if the mode is **add**, **update**, or **status report**.*

Read the transaction agreement carefully. Extract every:

- **Condition precedent** to each party's obligation to close (typically in the "Conditions to Closing" or "Conditions Precedent" article), including mutual conditions, conditions to the buyer's obligations, and conditions to the seller's obligations.
- **Closing deliverable** — documents, certificates, officer's certificates, consents, payoff letters, and instruments to be delivered at or before closing.
- **Pre-closing covenant** — affirmative or negative covenants that must be performed between signing and closing (e.g., conduct of business in the ordinary course, required filings, required consents, no-shop obligations).

For each extracted item:

- Assign a sequential ID (e.g., CP-001, CD-001, PC-001 by category).
- Record the source (agreement article or section number as written).
- Mark Blocking as **Yes** if the agreement conditions closing on it, **No** if it is a deliverable that can be waived, or **[CONFIRM: blocking status]** if ambiguous.
- Leave Status as **Open** unless otherwise confirmed.
- Leave Due as `[deadline verification required]` unless a specific date appears in the agreement.
- Leave Responsible as `[CONFIRM: responsible party]` unless the agreement designates one.

Do not assume that regulatory mechanics, governmental approvals, or statutory waiting periods apply based on the deal type alone. Where the agreement references a regulatory approval, filing, or governmental consent without specifying mechanics, flag the item as `[verify jurisdiction]`.

### Step 3 — Add diligence items

*Skip to Step 4 if the mode is **initialize**, **update**, or **status report**.*

Review the diligence findings provided. Identify every finding that carries a pre-closing action item, including:

- Required third-party consents (contractual change-of-control, assignment, or consent provisions).
- Board or shareholder authorizations and approvals.
- Regulatory filings or clearances identified through diligence.
- Releases, terminations, or payoffs needed before closing.
- Escrow establishment or funding mechanics.
- Any other item that must be completed before closing can occur.

For each new item:

- Assign an ID in sequence (continuing from the initialized checklist, or beginning a new series for diligence-derived items, e.g., DI-001).
- Record the source as the diligence finding (document title and finding reference, if available).
- De-duplicate carefully: a third-party consent and a release involving the same counterparty are distinct items even if the counterparty is the same. A filing obligation identified in diligence that duplicates a condition in the agreement should be merged, not duplicated; note both sources.

Apply the same placeholder discipline as in Step 2: no computed deadlines, no assumed regulatory mechanics.

### Step 4 — Update item status

*Skip to Step 5 if the mode is **initialize** or **add**.*

For each item being updated, record the new status. Use consistent status values such as: **Open**, **In Progress**, **Pending Counterparty**, **Received / Complete**, or **Waived** — or the team's own conventions if provided. Note any change to the responsible party or due date only if confirmed by the user; do not infer these from context.

If an item is marked **Waived**, flag it for attorney confirmation: `[ATTORNEY TO CONFIRM: waiver of this condition]`.

### Step 5 — Status report and blocking analysis

Identify every item with:

- **Blocking: Yes** and **Status: Open** or **In Progress** — these are the items currently standing between the deal and closing.
- **Blocking: Yes** and **Status: Pending Counterparty** — items in flight but not yet complete.
- Any item carrying `[verify jurisdiction]` or `[CONFIRM]` that has not yet been resolved.

Summarize the critical path: which open blocking items are on the longest path to closing, and what dependencies exist among them (e.g., a regulatory filing must be completed before a clearance can be obtained). Do not assert that any item is legally satisfied — describe status as reported and flag what remains to be confirmed.

### Step 6 — Assemble the output

Produce the closing checklist using `templates/closing-checklist.md`. Follow the Output Format below. Label the entire output as a draft for attorney review.

## Output Format

Deliver:

1. **Closing Checklist** — the completed checklist table from `templates/closing-checklist.md`, grouped by category (Conditions Precedent / Closing Deliverables / Pre-Closing Covenants / Third-Party Consents / Regulatory Filings / Corporate Approvals). Use placeholders throughout; do not fill gaps with invented content.
2. **Blocking and Critical-Path Summary** — a concise narrative identifying every open blocking item, items pending counterparty action, and any unresolved `[verify jurisdiction]` or `[CONFIRM]` items, with a plain-language description of the critical path to closing.
3. **Assumptions** — every assumption made in constructing or updating the checklist, listed explicitly. Include the deal structure assumed, any items treated as blocking by default, and any source material not provided.
4. **Attorney Verification Items** — open questions and items requiring legal judgment, including all `[ATTORNEY TO CONFIRM]` flags, all `[verify jurisdiction]` items, and any condition whose satisfaction is a legal conclusion rather than a factual status.

Use `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, and `[deadline verification required]` throughout. Do not fill gaps with invented content.

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] The transaction agreement reviewed is fully executed and final (or, for pre-signing use, is confirmed to be the agreed form).
- [ ] All conditions precedent, closing deliverables, and pre-closing covenants have been identified from the agreement; no material conditions have been omitted.
- [ ] The transaction structure is correctly identified; if the structure is ambiguous, it has been confirmed with deal counsel.
- [ ] Every item marked "Blocking: Yes" is confirmed to be a condition or covenant on which closing is contractually contingent, and any waivability has been assessed.
- [ ] No waiver of a closing condition has been treated as final without attorney confirmation.
- [ ] All `[verify jurisdiction]` items — regulatory mechanics, filing requirements, waiting periods, and governmental approvals — have been reviewed and confirmed with counsel having relevant jurisdiction and subject-matter expertise.
- [ ] Deadlines and due dates have been confirmed against the agreement and applicable legal requirements; no deadline has been computed from model background knowledge.
- [ ] Responsible parties have been confirmed with the deal team; no responsible party has been assumed from context.
- [ ] Diligence-derived items have been cross-referenced against the agreement to ensure de-duplication is accurate and no consent or filing obligation has been missed.
- [ ] All `[ATTORNEY TO CONFIRM]` flags in the checklist have been reviewed and resolved.
- [ ] No legal authority, statute, regulation, or case law has been asserted without verification.
- [ ] The checklist and blocking analysis have been reviewed by deal counsel before being relied upon to determine closing readiness.
- [ ] All assumptions and open items are resolved before the checklist is used to support a closing determination.
