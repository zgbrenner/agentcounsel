---
name: SOW Review
description: Use when reviewing a statement of work or work order to assess scope clarity, deliverables, acceptance criteria, timeline, pricing, and — critically — consistency with the governing master agreement.
---

# SOW Review

## Purpose

Produce a structured, attorney-ready review of a statement of work (SOW) or work order (WO). This skill assesses: scope and deliverables clarity, acceptance criteria, timeline and milestones, pricing and payment triggers, assumptions and dependencies, change-order process, personnel and staffing obligations, IP and deliverable ownership, and — critically — whether the SOW is consistent with its governing master agreement (MSA) or whether it improperly overrides, conflicts with, or silently expands MSA terms.

SOW conflicts with the governing MSA are a distinct and commonly missed risk. This skill treats MSA-SOW consistency as a primary review obligation, not a secondary check.

This skill produces draft legal work product for attorney review only. It is not legal advice and does not constitute a final negotiating position.

## Use When

- A user asks to "review this SOW," "check this work order," "is this statement of work solid," or "does this conflict with our MSA."
- A vendor or service provider has sent a SOW for signature and the user needs a structured first-pass review.
- The user is preparing to negotiate or redline a SOW and needs to understand scope, payment, and IP risks before doing so.
- An in-house team or project owner needs to confirm that a SOW is consistent with the governing MSA before execution.
- A SOW has been executed and a dispute has arisen about scope, deliverables, or payment — the user needs a structured analysis of what the SOW says.
- The user is reviewing a form SOW template for future use and needs a gap analysis.

## Required Inputs

- **The full SOW text** — uploaded or pasted. Do not review from a description or partial excerpt alone.
- **The governing MSA or master agreement** — strongly preferred; if unavailable, flag this as a material gap and note that MSA-SOW consistency analysis cannot be performed. Do not assume MSA terms.
- **The client's role** — which party is the client (e.g., customer/buyer, vendor/service provider)?
- **Business context** — what services are being procured or provided, what is the approximate value, and what is the delivery timeline?

If the SOW text is not provided, stop and request it. If the governing MSA is not provided, proceed with the SOW-only review but prominently flag throughout that MSA-consistency analysis is incomplete.

## Do Not Use When

- The document is a master services agreement or general commercial contract without an attached SOW (use `contract-risk-review`).
- The user needs a full MSA review — review the MSA first using `contract-risk-review`, then review the SOW under it.
- The user needs to summarize tracked changes between two SOW versions (use `redline-summary`).
- The document is an NDA (use `nda-review`).
- The user needs IP or technology licensing advice specific to the deliverables — that analysis requires attorney expertise beyond a structured workflow.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Review only the language actually present in the provided documents. Quote clause language accurately.
- Do not invent SOW or MSA terms, section numbers, defined terms, deliverables, or milestones. If a provision is absent, say so — do not fabricate its presence or absence.
- Do not assume what the MSA says if it has not been provided. Any MSA-consistency observation must be based on the actual MSA text, not on assumed "standard" terms.
- Do not invent statutes, regulations, or case law. Do not make "market standard" assertions without flagging them for attorney verification.
- Identify (or flag as unknown): which document controls in a conflict (MSA order of precedence clause), governing law, effective date, and which party's form this is.
- Scope disputes frequently arise from ambiguous SOW language — flag ambiguity explicitly rather than resolving it by assumption.
- Do not place client-sensitive facts into reusable templates.
- Use `[CONFIRM: ...]` placeholders wherever information is missing or uncertain.
- Flag every point of uncertainty rather than resolving it silently.

## Workflow

1. **Confirm inputs.** Verify that you have the SOW text, the governing MSA (or a flag that it is not available), and the client's role. Note whether the MSA-consistency analysis will be complete or limited.

2. **Orient.** State the SOW title and number (if any), parties, effective date (or `[CONFIRM: effective date]`), governing law (or `[CONFIRM: governing law]`), and the client's contractual role. Identify the governing MSA by name and date if provided.

3. **Assess scope and deliverables clarity.**
   - Are the deliverables defined with enough specificity to determine when they are complete?
   - Are there ambiguous scope terms that could support a dispute (e.g., "reasonable efforts," "industry standard," undefined output formats)?
   - Is there a defined mechanism for scope changes, or is the scope implicitly open-ended?

4. **Assess acceptance criteria.**
   - Are acceptance criteria defined? Are they objective and measurable?
   - Is there a defined acceptance process — testing period, acceptance sign-off, deemed-acceptance if no response?
   - What are the consequences of rejection? Is there a right to cure? A limit on rejection cycles?

5. **Assess timeline and milestones.**
   - Are milestones and delivery dates clearly defined?
   - Are milestone dates conditions to payment, conditions to further performance, or aspirational only?
   - What happens if a milestone is missed — does liability attach? Is there a cure period?
   - Are there dependencies or client obligations that could shift responsibility for delay?

6. **Assess pricing and payment triggers.**
   - Is the fee structure clear — fixed fee, time-and-materials, milestone-based, or hybrid?
   - What are the exact payment triggers? Are they tied to milestone acceptance, calendar dates, or deliverable delivery?
   - Are out-of-pocket expenses addressed? Is there a cap or pre-approval requirement?
   - Are there late payment provisions, and do they favor the client or the vendor?

7. **Assess assumptions and dependencies.**
   - What assumptions is the SOW built on (e.g., client-provided access, data, personnel, environments)?
   - Are the assumptions listed? Are the consequences of failed assumptions defined (e.g., schedule extension, additional fees)?
   - Are client obligations stated with enough specificity to allocate responsibility for dependency failures?

8. **Assess the change-order process.**
   - Is there a defined change-order or change-request process?
   - Can the vendor perform out-of-scope work and bill for it without written approval? This is a scope creep risk.
   - Does the change-order process require written authorization from both parties?

9. **Assess personnel and staffing.**
   - Are key personnel identified? Are there substitution restrictions?
   - Does the client have approval rights over personnel changes?
   - Are subcontractor restrictions addressed?

10. **Assess IP and deliverable ownership.**
    - Who owns custom work product and deliverables created under this SOW?
    - Does the SOW incorporate or conflict with the MSA's IP provisions?
    - Are background IP, third-party components, and open-source software addressed?
    - Is there a license-back provision if the vendor retains ownership?

11. **Assess MSA-SOW consistency** (if MSA is available).
    - Identify any provision in the SOW that conflicts with, overrides, or silently expands an MSA term.
    - Review the MSA's order-of-precedence clause — which document controls in a conflict?
    - Flag any SOW provision that purports to modify MSA terms (e.g., expanded liability, shorter notice periods, different IP ownership) without an explicit MSA amendment.
    - Flag any MSA protection that the SOW appears to waive or narrow.

12. **Build the gap and issues table.** Populate a structured table summarizing each area reviewed with a rating of No Issue / Low / Medium / High and a recommended action.

13. **List open items for attorney verification.**

14. **Assemble the output** and label it as a draft for attorney review.

## Output Format

Deliver, in order:

1. **Document Summary** — SOW title and number, parties, effective date, governing MSA (if provided), client's role, fee structure summary, delivery timeline summary.
2. **Scope and Deliverables Assessment** — plain-language summary with flagged ambiguities.
3. **Acceptance Criteria Assessment** — summary of defined (or missing) criteria and process.
4. **Timeline and Milestone Assessment** — summary with risk flags.
5. **Pricing and Payment Assessment** — summary with risk flags.
6. **Assumptions and Dependencies Assessment** — summary of stated assumptions and gaps.
7. **Change-Order Process Assessment** — summary with risk flags.
8. **Personnel and Staffing Assessment** — summary with risk flags.
9. **IP and Deliverable Ownership Assessment** — summary with risk flags.
10. **MSA-SOW Consistency Analysis** — clause-by-clause conflict and consistency findings, or a prominent flag if MSA was not provided.
11. **Gap and Issues Table** — structured table: # | Topic | Finding | Severity (High/Med/Low/None) | Recommended Action | Attorney Note.
12. **Open Items for Attorney Verification** — checkbox list.
13. **Assumptions** — explicit list of all assumptions made about business context, MSA terms, or legal standard.

Use `[CONFIRM: ...]` wherever a fact, clause meaning, or MSA term is unverified or ambiguous.

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] The SOW reviewed is the complete, correct, and final version.
- [ ] The governing MSA is the correct version in effect for this SOW.
- [ ] The order of precedence between the MSA and SOW has been confirmed, and any conflicts have been assessed under the controlling document.
- [ ] All SOW provisions that purport to modify MSA terms have been identified and assessed for whether an MSA amendment is required.
- [ ] Scope and deliverables are sufficiently specific to support acceptance testing and dispute resolution.
- [ ] Acceptance criteria are objective, measurable, and protective of the client's interests.
- [ ] Milestone-payment linkages are correctly structured and consistent with the fee arrangement.
- [ ] Client obligations and assumptions are accurately stated; consequence of failure is clearly allocated.
- [ ] IP ownership of custom deliverables is correctly assessed given the nature of the work and the MSA terms.
- [ ] Background IP, third-party components, and open-source dependencies have been flagged for counsel review.
- [ ] Change-order process provides adequate written-authorization protection against unauthorized scope expansion.
- [ ] Personnel and subcontractor provisions are appropriate for the nature and sensitivity of the engagement.
- [ ] All `[CONFIRM: ...]` placeholders and open items have been resolved before the SOW is executed or relied upon.
- [ ] The review has been assessed by counsel before it is used in negotiation, execution, or dispute analysis.
