---
name: Restrictive Covenant Review
description: "Use when reviewing non-compete, non-solicit, no-hire, or confidentiality covenants — in an offer letter, employment agreement, equity award, or separation document, or when assessing an incoming hire's covenants from a prior employer — to inventory each covenant's scope verbatim, organize the enforceability factors as questions, and flag consideration and conflict issues for attorney review."
practice_area: employment
task_type: review
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The document(s) containing the restrictive covenants, in full"
  - "The client's posture: the employer imposing the covenants, the employee bound by them, or the new employer assessing an incoming hire's prior covenants"
  - "The role, compensation, and work location(s) of the affected individual, as provided"
  - "Optional: the consideration offered for the covenants (initial employment, a raise, equity, severance, or other)"
  - "Optional: any prior agreements the same individual has signed that bear on the covenants"
outputs:
  - "Covenant-by-covenant scope inventory with each term quoted verbatim"
  - "Enforceability-factor questions organized for attorney review"
  - "Consideration and conflict-posture flags"
related_skills:
  - skills/employment/severance-review/SKILL.md
  - skills/employment/hiring-review/SKILL.md
  - skills/employment/termination-risk/SKILL.md
tags:
  - employment
  - restrictive-covenants
  - non-compete
  - non-solicit
  - trade-secrets
  - contract-review
---

# Restrictive Covenant Review

## Purpose

Produce a structured, attorney-ready review of restrictive covenants — non-competition, non-solicitation (of customers or employees), no-hire, and confidentiality provisions — wherever they appear: an offer letter, an employment or consulting agreement, an equity or incentive award, or a separation document. The skill inventories each covenant's scope exactly as written, organizes the enforceability factors as questions for counsel, and flags consideration and conflict-posture issues. It never concludes that a covenant is or is not enforceable — enforceability is intensely jurisdiction-specific and is an attorney determination. This is draft legal work product for attorney review, not legal advice.

## Use When

- An employer is drafting or imposing covenants in an offer, employment agreement, equity award, or separation document and wants the scope and risk points organized before finalizing.
- An employee has been asked to sign covenants and wants a structured read of what each one restricts.
- A new employer is assessing the covenants an incoming hire signed with a prior employer, to understand the conflict posture before the hire starts.
- Covenants are being added or expanded at separation and their reach beyond any prior agreement needs to be mapped.
- A user asks "are these non-competes a problem?" or "what do these restrictions actually cover?"

## Required Inputs

- **The document(s) containing the covenants**, in full. If the covenants are described but not provided, stop and request the text. Never reconstruct covenant language from memory.
- **The client's posture**: employer imposing, employee bound, or new employer assessing an incoming hire's prior covenants. The risk framing differs materially by posture.
- **The role, compensation, and work location(s)** of the affected individual, as provided — scope reasonableness and which jurisdiction's law may apply both turn on these.
- Optional: **the consideration** offered for the covenants (initial employment, a raise, promotion, equity, severance, or other).
- Optional: **any prior agreements** the same individual has signed that bear on the covenants (a prior non-compete, an assignment agreement, a handbook acknowledgment).

If the covenant text or the client posture is missing, stop and request it before substantive work.

## Do Not Use When

- The task is a full review of a severance or separation agreement as a whole — use `severance-review`; this skill goes deeper on the covenants specifically and can feed that review.
- The task is a first-pass review of a whole offer or hiring package — use `hiring-review`; route the covenant deep-dive here.
- The question is whether to enforce a covenant through litigation, or to seek or oppose an injunction — that is active-litigation strategy for counsel, not a covenant review.
- The user wants a conclusion on whether a specific covenant is enforceable, void, or safe to ignore — that is a legal determination this skill only frames questions for.
- The document contains no restrictive covenants — there is nothing for this skill to review.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- **Never conclude a covenant is enforceable, unenforceable, void, or safe to ignore.** Enforceability turns on the governing law, the covenant's scope, the consideration, and the facts — all attorney determinations. Organize the factors as questions.
- **Never assert what any jurisdiction's law requires.** Some jurisdictions restrict, limit, or void certain covenants (particularly non-competes), and some regulate them by role, wage level, or industry — describe these only as categories to verify, each flagged `[Verify current law]` `[verify jurisdiction]`. Never state a duration, geographic radius, or wage threshold as a legal rule.
- Quote each covenant's operative language verbatim. Do not paraphrase scope into existence or narrow a broad term in the summary.
- **Never advise an employee to breach, or an employer to enforce or waive.** Whether to sign, to comply, to enforce, or to litigate are decisions for the party on counsel's advice.
- For an incoming-hire assessment, never conclude what the candidate may safely do — the permissible scope of the new role given prior covenants is an attorney call. Organize the conflict facts and flag them.
- Treat trade-secret and confidentiality questions with care: never assert that particular information is or is not a protectable trade secret.
- Do not compute any date — covenant duration, tolling, or a notice deadline. Record durations as written and flag `[deadline verification required]` where a period's running matters.
- Distinguish throughout: what the document says (quoted), what the user stated, what is assumed, and what counsel must verify.
- Preserve confidentiality: covenant reviews often involve sensitive competitive and compensation facts; keep them out of reusable templates.

## Workflow

This skill draws on the Restrictive Covenants section (Section 4) of `skills/employment/references/severance-release-red-flags.md` where covenants appear in a separation context; consult it at Step 5.

1. **Confirm inputs.** Verify the covenant document(s), the client posture, and the role/compensation/location facts are provided. Request anything missing before proceeding.
2. **State the gates.** Record the client posture, the affected individual's role and work location(s), the potentially applicable jurisdiction(s) (each `[verify jurisdiction]`), and the "as of" date. Note that which jurisdiction's law governs may itself be contested — flag `[ATTORNEY TO CONFIRM: governing law and choice-of-law enforceability]`.
3. **Inventory the covenants present.** Identify each restrictive covenant in the document: non-competition, customer non-solicitation, employee non-solicitation / no-hire, no-hire of contractors, confidentiality/trade-secret, non-disparagement (route non-disparagement framing to `severance-review` where relevant), and any IP-assignment or invention provisions that function as restraints. List each with its section reference.
4. **Map each covenant's scope, quoted verbatim.** For each covenant, record: the restricted activity or information; the duration; the geographic scope; the defined terms that set its reach (e.g., "Competing Business," "Customer," "Confidential Information"); and any carve-outs or exceptions. Quote the operative language; flag any term whose breadth is ambiguous as `[CONFIRM: intended scope of "<term>"]`.
5. **Flag scope-reasonableness questions for counsel.** Without concluding, list the questions a court in the governing jurisdiction may weigh: whether the duration, geography, and activity scope are tied to a legitimate protectable interest; whether definitions sweep in activity or customers the individual never touched; whether a "blue-pencil" or reformation posture is available in the jurisdiction. Consult Section 4 of the severance red-flags reference for the patterns to surface. Every point is `[Verify current law]` `[verify jurisdiction]`.
6. **Organize the consideration questions.** Record what consideration is stated for the covenants (initial employment, a raise, equity, severance, or nothing identified). Flag for counsel whether the consideration is adequate under the governing law, particularly where covenants are introduced or expanded after employment began or at separation — never conclude adequacy. `[ATTORNEY TO CONFIRM: consideration sufficiency]`.
7. **Check statutory and role-based restrictions as categories.** Flag, without asserting: whether the jurisdiction restricts non-competes by wage level, role, or industry; whether notice, review-period, or advance-disclosure formalities may apply; and whether any garden-leave or compensation-during-restriction requirement may attach. Each `[Verify current law]` `[verify jurisdiction]`.
8. **Assess the conflict posture (incoming-hire mode).** If the client is a new employer assessing a candidate's prior covenants, organize: what the prior covenants restrict; how the proposed new role overlaps with the restricted activity, customers, or colleagues; what information the candidate must not use or disclose; and any onboarding safeguards to raise with counsel. Never conclude what the candidate may safely do — flag `[ATTORNEY TO CONFIRM: permissible scope of new role given prior covenants]`.
9. **Cross-check against prior agreements.** If prior agreements were provided, note where the current covenants add to, conflict with, or duplicate them, and which document would control — flag the conflict, do not resolve it.
10. **Flag missing documents and open terms.** List every referenced-but-unprovided document (a plan the equity award incorporates, a policy the covenant references) and every ambiguous defined term.
11. **List attorney verification items and assemble the output.** Consolidate every placeholder, assemble the output in the format below, label it a draft for attorney review, and attach the unchecked checklist.

## Output Format

Deliver the following, in order, labeled `DRAFT — For Attorney Review — Not a Determination of Enforceability`:

1. **Summary** — one paragraph: the document(s), the client posture, the covenants present, and the top issues — with an explicit statement that no enforceability conclusion is drawn.
2. **Gates** — client posture, role and location, potentially applicable jurisdiction(s) (`[verify jurisdiction]`), governing-law flag, relevant date.
3. **Covenant Scope Inventory** — table: Covenant | Section | Restricted Activity/Info | Duration | Geography | Key Defined Terms | Carve-outs | Verbatim Quote.
4. **Scope-Reasonableness Questions** — the framed questions from Step 5, each `[Verify current law]` `[verify jurisdiction]`.
5. **Consideration Questions** — what is stated and the sufficiency question for counsel.
6. **Statutory / Role-Based Flags** — the category inventory from Step 7.
7. **Conflict Posture** (incoming-hire mode) — the overlap organization from Step 8, with the permissible-scope question flagged.
8. **Prior-Agreement Interplay** — additions, conflicts, and control questions.
9. **Missing Documents and Open Terms** — referenced-but-unprovided items and ambiguous terms.
10. **Attorney Verification Items** — every placeholder consolidated.
11. **Assumptions** — every assumption made, listed explicitly.

Use `[CONFIRM: ...]` wherever a fact, term, or legal requirement is unverified. Do not fill gaps with invented content.

## Attorney Verification Checklist

- [ ] The full document(s) containing the covenants have been reviewed, and every referenced-but-unprovided document has been obtained.
- [ ] The client's posture (employer, employee, or new employer) is correctly identified.
- [ ] The governing law and the enforceability of any choice-of-law clause have been confirmed. `[verify jurisdiction]`
- [ ] Each covenant's scope — activity, duration, geography, definitions — has been assessed for reasonableness under the governing law. `[Verify current law]`
- [ ] Whether the jurisdiction restricts, limits, or voids any of these covenants by role, wage, industry, or category has been confirmed. `[Verify current law]`
- [ ] The consideration for the covenants has been assessed for sufficiency under the governing law, especially for covenants added after hire or at separation.
- [ ] Any notice, review-period, advance-disclosure, or garden-leave formalities that may apply have been confirmed. `[Verify current law]` `[deadline verification required]`
- [ ] The interplay with any prior agreements has been resolved, and the controlling document identified.
- [ ] For an incoming hire: the permissible scope of the new role given prior covenants has been determined by counsel, and any onboarding safeguards put in place.
- [ ] Confidentiality and trade-secret provisions have been assessed without this draft asserting what qualifies as a protectable trade secret.
- [ ] No covenant duration, tolling period, or notice date was computed by this draft. `[deadline verification required]`
- [ ] No statement in the deliverable asserts or implies that any covenant is enforceable, unenforceable, or safe to ignore.
- [ ] All `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[Verify current law]`, and `[verify jurisdiction]` placeholders have been resolved before the review is relied upon.
