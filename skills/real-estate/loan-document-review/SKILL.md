---
name: Loan Document Review
description: "Use when reviewing commercial real-estate financing documents — a loan agreement, promissory note, mortgage or deed of trust, assignment of leases and rents, guaranty, or environmental indemnity — from a borrower, guarantor, or lender perspective, to inventory the documents, record economic terms verbatim, flag recourse and covenant structures, and organize issues for attorney review."
practice_area: real-estate
task_type: review
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The financing documents to review, in full (loan agreement, note, mortgage/deed of trust, assignment of leases and rents, guaranty, environmental indemnity, and any riders)"
  - "The client's perspective: borrower, guarantor, or lender"
  - "The property type and the transaction context (acquisition, refinance, construction, or bridge), as stated"
  - "Optional: the term sheet or commitment letter the documents are meant to implement"
  - "Optional: the practice group's practice-profiles/real-estate.md, if populated"
outputs:
  - "Document inventory and defined-terms map"
  - "Economic-terms and recourse-structure summary with terms quoted verbatim"
  - "Covenant, transfer-restriction, and default/remedies issue list for attorney review"
related_skills:
  - skills/real-estate/psa-review/SKILL.md
  - skills/real-estate/commercial-lease-review/SKILL.md
  - skills/real-estate/estoppel-snda-review/SKILL.md
  - skills/real-estate/title-survey-objection-tracker/SKILL.md
  - skills/insurance/insurance-requirements-contract-review/SKILL.md
tags:
  - real-estate
  - loan-documents
  - mortgage
  - guaranty
  - financing
  - contract-review
---

# Loan Document Review

## Purpose

Produce a structured, attorney-ready review of a commercial real-estate financing package — the loan agreement, promissory note, mortgage or deed of trust, assignment of leases and rents, guaranty, environmental indemnity, and related riders — from a stated party perspective (borrower, guarantor, or lender). The skill inventories the documents and their defined terms, records the economic terms exactly as written, flags the recourse structure and carve-out guaranty triggers, and organizes the covenant, transfer-restriction, and default/remedies issues for counsel. It never computes an interest, yield-maintenance, or prepayment figure, and never confirms lien perfection, priority, or title status. This is draft legal work product for attorney review, not legal advice.

## Use When

- A borrower or guarantor has received a financing package and needs the terms and risk points organized before signing.
- A lender's counsel wants a structured review of a loan package against the deal terms.
- A refinance, construction loan, or bridge facility needs its covenants, recourse structure, and transfer restrictions mapped.
- A guaranty (payment, carry, completion, or "bad-boy" carve-out) needs its triggers quoted and organized.
- Diligence on an acquisition surfaces assumed or new debt whose documents need review alongside the purchase agreement.

## Required Inputs

- **The financing documents**, in full — loan agreement, note, mortgage or deed of trust, assignment of leases and rents, guaranty, environmental indemnity, and any riders or side letters. If key documents are described but not provided, list them as gaps and review only what is present.
- **The client's perspective**: borrower, guarantor, or lender. Risk framing differs materially by side.
- **The property type and transaction context** (acquisition, refinance, construction, bridge), as stated.
- Optional: **the term sheet or commitment letter** the documents implement — to check the documents against the agreed terms.
- Optional: **`practice-profiles/real-estate.md`**, if populated and loaded — used to benchmark against the group's standard positions and escalation thresholds; if absent, proceed without profile benchmarking.

If no loan documents are provided, stop and request them. Never reconstruct financing terms or document language from memory.

## Do Not Use When

- The task is reviewing the purchase and sale agreement rather than the financing — use `psa-review` (which flags how a PSA interacts with loan documents; this skill takes the loan side).
- The task is title or survey review — use `title-survey-objection-tracker`; this skill flags lien-perfection and priority questions and routes them there, never confirming title status.
- The task is the estoppel or SNDA package for tenants at the property — use `estoppel-snda-review`.
- The task is the insurance requirements the loan imposes as a standalone review — route to `insurance-requirements-contract-review`; this skill flags the requirement and hands off.
- The user wants a computed payment, yield-maintenance, prepayment premium, or debt-service-coverage figure — this skill records the formula as written and never computes the number.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- **Never compute a financial figure.** Interest, default interest, yield maintenance, prepayment premiums, exit fees, reserve amounts, and debt-service-coverage or loan-to-value ratios are recorded as the formula or figure the document states — never calculated, tested, or projected.
- **Never confirm lien perfection, priority, or title status.** Whether the mortgage is properly perfected, first in priority, or free of prior liens is a title and recording matter for counsel and the title company. Flag every such point `[ATTORNEY TO CONFIRM]` and route to `title-survey-objection-tracker`.
- **Never conclude enforceability.** Recourse carve-outs, guaranty triggers, prepayment lockouts, and remedies provisions vary in enforceability by jurisdiction — quote them and flag `[verify jurisdiction]` `[Verify current law]`; never state that a provision is or is not enforceable.
- Do not compute or assert a date. Maturity, notice, cure, and reserve-funding dates are recorded as written and flagged `[deadline verification required]`.
- Quote operative language verbatim — recourse triggers, covenants, and default provisions especially. Do not paraphrase a carve-out in a way that changes its reach.
- Distinguish throughout: what the document says (quoted), what the term sheet or user stated, what is assumed, and what counsel must verify.
- Preserve confidentiality: keep deal economics and party-specific terms out of reusable templates.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/real-estate.md` is loaded, its standard positions and escalation thresholds inform the draft but never substitute for attorney judgment; if the profile conflicts with the matter facts or the supervising attorney's conclusions, the attorney prevails.

## Workflow

1. **Confirm inputs.** Verify the financing documents, the client perspective, and the transaction context are provided. List any referenced-but-missing documents. Request anything essential before proceeding.
2. **State the gates.** Record the client perspective, the property type and transaction context, the governing-law and jurisdiction(s) as stated (`[verify jurisdiction]`), and the "as of" date.
3. **Build the document inventory.** List each document in the package by type and title, note which are present and which are referenced but missing, and identify the document hierarchy (which controls on conflict, as the documents state it).
4. **Map the defined terms.** Extract the defined terms that set the deal's reach — Loan, Obligations, Indebtedness, Property, Permitted Transfers, Permitted Liens, Event of Default, Guaranteed Obligations — and note where they are defined. Flag circular or ambiguous definitions.
5. **Record the economic terms verbatim.** Capture, as written and never computed: principal, interest rate and default rate, payment terms, maturity, amortization, prepayment provisions (lockout, yield maintenance, defeasance, exit fee), and any holdbacks or earn-out/advance mechanics. Each figure or formula is quoted; every date `[deadline verification required]`.
6. **Map the recourse structure.** Record whether the loan is recourse, non-recourse, or limited-recourse, and quote the recourse carve-outs ("bad-boy" triggers) verbatim — springing full recourse vs. loss-only carve-outs, and the specific triggering acts (transfers, bankruptcy, waste, fraud, environmental). Flag broad or springing triggers prominently for the client's side. Never conclude enforceability.
7. **Inventory the guaranties.** For each guaranty (payment, carry/carve-out, completion), record the guarantor, the guaranteed obligations, the triggers, any caps or burn-downs, and waivers of guarantor defenses — quoted. Flag guaranties whose scope exceeds the carve-outs they are meant to backstop.
8. **Record the covenants as drafted.** Capture financial covenants (DSCR, LTV, net-worth, liquidity), reporting covenants, and operating covenants — as written, never tested against any number. Note single-purpose-entity and separateness covenants where present.
9. **Map transfer and due-on-sale restrictions.** Record restrictions on transfer, change of control, secondary financing, and lease-related actions, and any permitted-transfer and assumption provisions — quoted, with the consent standards flagged.
10. **Record cash-management and reserve provisions.** Capture lockbox/cash-management triggers, sweep conditions, and required reserves/escrows (tax, insurance, replacement, TI/LC) as written, with funding dates `[deadline verification required]`.
11. **Flag the security, perfection, and title questions.** Note the collateral the mortgage/deed of trust and assignment of leases and rents purport to encumber, and flag perfection, priority, and title-status questions `[ATTORNEY TO CONFIRM]`, routing to `title-survey-objection-tracker`. Never confirm perfection or priority.
12. **Route insurance and casualty/condemnation.** Flag the loan's insurance requirements and route them to `insurance-requirements-contract-review`; record casualty and condemnation provisions (application of proceeds, restoration conditions) as written.
13. **Map default and remedies.** Record events of default, notice and cure provisions (dates `[deadline verification required]`), and the remedies (acceleration, foreclosure, receiver, assignment enforcement) as written, noting the interplay between the note, the mortgage, and the guaranties. Flag `[verify jurisdiction]` on remedy availability.
14. **Check against the term sheet.** Where a term sheet was provided, note where the documents deviate from the agreed terms.
15. **List attorney verification items and assemble the output**, labeled a draft for attorney review, with the checklist attached.

## Output Format

Deliver the following, in order, labeled `DRAFT — For Attorney Review — Not a Confirmation of Lien Priority, Title, or Enforceability`:

1. **Summary** — one paragraph: the facility, the client perspective, the property, and the top issues — with the explicit statement that no title, perfection, priority, or enforceability conclusion is drawn and no figure computed.
2. **Gates** — client perspective, property type, transaction context, governing law/jurisdiction (`[verify jurisdiction]`), relevant date.
3. **Document Inventory** — present, missing, and controlling-on-conflict.
4. **Defined-Terms Map** — the key definitions and any ambiguity flags.
5. **Economic Terms** — quoted verbatim; no computed figures; dates `[deadline verification required]`.
6. **Recourse Structure and Carve-Outs** — quoted triggers, with broad/springing triggers flagged.
7. **Guaranty Inventory** — per guaranty: guarantor, obligations, triggers, caps, waivers.
8. **Covenants** — financial, reporting, operating, and SPE/separateness, as drafted.
9. **Transfer and Due-on-Sale Restrictions** — quoted, with consent standards flagged.
10. **Cash Management and Reserves** — triggers and reserves, dates `[deadline verification required]`.
11. **Security, Perfection, and Title Flags** — `[ATTORNEY TO CONFIRM]`, routed to `title-survey-objection-tracker`.
12. **Insurance / Casualty / Condemnation** — requirements routed to `insurance-requirements-contract-review`; casualty/condemnation as written.
13. **Default and Remedies** — events of default, cure provisions, remedies, cross-document interplay, `[verify jurisdiction]`.
14. **Term-Sheet Deviations** — where the documents differ from the agreed terms.
15. **Attorney Verification Items** — every placeholder consolidated.
16. **Assumptions** — every assumption made, listed explicitly.

Use `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and `[deadline verification required]` throughout. Do not fill gaps with invented content.

## Attorney Verification Checklist

- [ ] The full financing package has been reviewed, and every referenced-but-missing document obtained.
- [ ] The client's perspective (borrower, guarantor, or lender) is correctly identified.
- [ ] Governing law and jurisdiction have been confirmed for each document. `[verify jurisdiction]`
- [ ] Every economic term matches the term sheet/commitment, and no figure in this draft was computed. `[deadline verification required]`
- [ ] The recourse structure and every carve-out ("bad-boy") trigger have been reviewed for scope and, where relevant, enforceability. `[verify jurisdiction]`
- [ ] Each guaranty's scope, triggers, caps, and defense waivers have been reviewed and reconciled with the recourse structure.
- [ ] Financial, reporting, operating, and SPE/separateness covenants have been assessed against the borrower's actual circumstances.
- [ ] Transfer, change-of-control, secondary-financing, and assumption provisions have been reviewed.
- [ ] Cash-management, sweep, and reserve/escrow provisions have been reviewed, and funding dates confirmed. `[deadline verification required]`
- [ ] Lien perfection, priority, and title status have been confirmed by counsel and the title company — not by this draft. `[ATTORNEY TO CONFIRM]`
- [ ] Insurance requirements have been reviewed (via `insurance-requirements-contract-review`), and casualty/condemnation provisions assessed.
- [ ] Events of default, notice and cure periods, and remedies have been reviewed, including cross-document interplay and remedy availability in the jurisdiction. `[verify jurisdiction]` `[deadline verification required]`
- [ ] No maturity, cure, or reserve date was computed by this draft.
- [ ] No statement asserts lien perfection, priority, title status, or enforceability without attorney confirmation.
- [ ] All `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and `[deadline verification required]` placeholders have been resolved before the loan is relied upon or closed.
- [ ] If a practice profile was loaded: every applicable standard position and escalation threshold has been surfaced and deviations flagged; if none was loaded, no standing-position framing was assumed.
