---
name: NDA Review
description: Use when reviewing a non-disclosure or confidentiality agreement to produce a structured risk summary and prioritized redline points for attorney review.
---

# NDA Review

## Purpose

Produce a structured, attorney-ready review of a non-disclosure agreement (NDA) or confidentiality agreement. The skill identifies key terms, flags risk-allocation issues, and proposes prioritized redline points. It produces draft legal work product for attorney review — not legal advice and not a final negotiating position.

## Use When

- A user asks to "review this NDA," "check this confidentiality agreement," or "tell me what's risky here."
- A counterparty has sent an NDA and the user needs a first-pass risk read.
- The user wants a redline priority list before negotiation.
- The user wants a plain-language summary of an NDA's obligations.

## Required Inputs

- The full NDA text (uploaded or pasted). Do not review from a description alone.
- The client's role: disclosing party, receiving party, or mutual.
- The business context: what is being shared and why.
- Optional: the user's standard NDA position or playbook, governing-law preference, and any deal deadline.

If the NDA text is not provided, stop and request it. Do not reconstruct or assume contract language.

## Do Not Use When

- The document is not an NDA (use `contract-risk-review` for general commercial agreements).
- The user needs a summary of tracked edits between drafts (use `redline-summary`).
- The confidentiality terms are one section of a larger commercial agreement (use `contract-risk-review`).
- The request is for a statement of legal advice or a final negotiating position — those require an attorney.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice.
- Review only the language actually present in the provided document. Quote it accurately.
- Do not invent contract terms, defined terms, section numbers, or quotations.
- Do not invent statutes, regulations, or case law. If legal authority is relevant, mark it as an attorney verification item.
- Do not invent or assume deadlines. Treat any signing or negotiation deadline as user-supplied or unverified.
- Distinguish what the contract says from what you assume and from what the attorney must confirm.
- Do not place client-sensitive facts into reusable templates.
- Flag every point of uncertainty rather than resolving it silently.

## Workflow

1. **Confirm inputs.** Verify you have the full NDA text and the client's role. If anything is missing, request it before proceeding.
2. **Identify the structure.** Locate and label the core provisions: parties, definition of Confidential Information, permitted use, standard exclusions, term and survival, return/destruction, remedies, governing law, and any extras (non-solicit, non-compete, IP, residuals, publicity, non-disparagement).
3. **Summarize each key term** in plain language, citing the section number as written.
4. **Assess risk allocation from the client's role.** A receiving party and a disclosing party care about opposite asymmetries; analyze from the client's actual position.
5. **Flag missing or one-sided terms** — for example, no standard exclusions, a perpetual term on all information, broad injunctive-relief language, or unilateral obligations in a document labeled "mutual."
6. **Build the risk table** using `templates/nda-risk-table.md`.
7. **Draft prioritized redline points:** High / Medium / Low, each with the issue, why it matters, and a suggested direction of change (not final language unless the user asks for it).
8. **List attorney verification items** — governing-law implications, enforceability questions, and anything requiring legal judgment.
9. **Assemble the output** and label it as a draft for attorney review.

## Output Format

Deliver:

1. **Summary** — 3-5 sentences: document type, client role, overall risk posture.
2. **Key Terms Table** — plain-language summary with section references.
3. **Risk Table** — from `templates/nda-risk-table.md`.
4. **Prioritized Redline Points** — High / Medium / Low, each with rationale.
5. **Attorney Verification Items** — open questions and items requiring legal judgment.
6. **Assumptions** — every assumption made, listed explicitly.

Use placeholders like `[CONFIRM: governing law]` wherever information is missing. Do not fill gaps with invented content.

## Attorney Verification Checklist

- [ ] The NDA text reviewed is complete and final.
- [ ] The client's role (disclosing / receiving / mutual) is correctly identified.
- [ ] All section references and quotations match the source document.
- [ ] No legal authority, statute, or case law has been asserted without verification.
- [ ] Enforceability of remedies and any restrictive covenants has been assessed under the governing law.
- [ ] Governing law and jurisdiction are appropriate for the client.
- [ ] Term and survival periods are acceptable for the type of information being shared.
- [ ] Risk ratings reflect the client's actual negotiating position and leverage.
- [ ] All assumptions and open items are resolved before the review is relied upon.
