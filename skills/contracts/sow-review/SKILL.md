---
name: SOW Review
description: "Use when reviewing a statement of work or work order to assess scope clarity, deliverables, acceptance criteria, timeline, pricing, and — critically — consistency with the governing master agreement."
practice_area: contracts
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The statement of work or work order text"
  - "The governing master services agreement"
  - "The client's role and the business context"
outputs:
  - "Structured SOW review"
  - "Issues table flagging scope, deliverable, and MSA-consistency gaps"
related_skills:
  - skills/contracts/contract-risk-review/SKILL.md
  - skills/contracts/redline-summary/SKILL.md
  - skills/contracts/nda-review/SKILL.md
tags:
  - contracts
  - sow
  - statement-of-work
  - contract-review
  - msa-consistency
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
- Optional: the practice group's `practice-profiles/contracts.md` if it has been populated and is loaded alongside this skill. If present, the skill uses its Standard Positions and Escalation Thresholds tables to benchmark the output and to gate escalation. If absent, the skill proceeds without practice-profile benchmarking and asks the user to supply standing positions inline if needed.

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
- Do not draft new clause language or restructure provisions. Propose the direction of a change and route substantive drafting to an attorney.
- Identify (or flag as unknown): which document controls in a conflict (MSA order of precedence clause), governing law, effective date, and which party's form this is.
- Scope disputes frequently arise from ambiguous SOW language — flag ambiguity explicitly rather than resolving it by assumption.
- Do not place client-sensitive facts into reusable templates.
- Use `[CONFIRM: ...]` placeholders wherever information is missing or uncertain.
- Flag every point of uncertainty rather than resolving it silently.
- **Severity floor.** Once an issue has been rated High severity in the risk table or issues list, that rating must not be silently downgraded. Any reduction in severity is an explicit attorney decision and must be recorded as such (e.g., "Downgraded from High to Medium by [attorney], [date], reason: [brief rationale]"). This applies regardless of the counterparty's explanation or commercial commonness of the provision.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/contracts.md` is loaded, its Standard Positions and Escalation Thresholds inform the draft but never substitute for attorney judgment. The profile is a configuration record approved by the practice group; it is not legal advice and does not override the skill's normal attorney-verification gates. If the profile's standing positions conflict with the matter facts or with what the supervising attorney concludes, the attorney prevails.

## Workflow

This skill draws on shared contract-review reference material in `skills/contracts/references/`: `red-flags.md` (red-flag catalogue), `negotiability-ratings.md` (six-rating negotiability rubric), `market-benchmark-framework.md` (benchmarking discipline and market-practice vocabulary), `fallback-language-bank.md` (sample preferred and fallback positions by clause type), `document-type-checklists.md` (per-document-type checklists, including the statement-of-work checklist), and `redline-output-guidance.md` (how to frame redline direction). Consult them at the steps noted below.

1. **Confirm inputs.** Verify that you have the SOW text, the governing MSA (or a flag that it is not available), and the client's role. Note whether the MSA-consistency analysis will be complete or limited.

2. **Orient.** State the SOW title and number (if any), parties, effective date (or `[CONFIRM: effective date]`), governing law (or `[CONFIRM: governing law]`), and the client's contractual role. Identify the governing MSA by name and date if provided.

3. **Red flags quick scan.** Run a fast first pass against the red-flag catalogue in `skills/contracts/references/red-flags.md` and the statement-of-work checklist in `skills/contracts/references/document-type-checklists.md`. Record each red-flag pattern present, or note that none surfaced in the scan. This scan orients the deeper review; it does not replace it.

4. **Assess scope and deliverables clarity.**
   - Are the deliverables defined with enough specificity to determine when they are complete?
   - Are there ambiguous scope terms that could support a dispute (e.g., "reasonable efforts," "industry standard," undefined output formats)?
   - Is there a defined mechanism for scope changes, or is the scope implicitly open-ended?

5. **Assess acceptance criteria.**
   - Are acceptance criteria defined? Are they objective and measurable?
   - Is there a defined acceptance process — testing period, acceptance sign-off, deemed-acceptance if no response?
   - What are the consequences of rejection? Is there a right to cure? A limit on rejection cycles?

6. **Assess timeline and milestones.**
   - Are milestones and delivery dates clearly defined?
   - Are milestone dates conditions to payment, conditions to further performance, or aspirational only?
   - What happens if a milestone is missed — does liability attach? Is there a cure period?
   - Are there dependencies or client obligations that could shift responsibility for delay?

7. **Assess pricing and payment triggers.**
   - Is the fee structure clear — fixed fee, time-and-materials, milestone-based, or hybrid?
   - What are the exact payment triggers? Are they tied to milestone acceptance, calendar dates, or deliverable delivery?
   - Are out-of-pocket expenses addressed? Is there a cap or pre-approval requirement?
   - Are there late payment provisions, and do they favor the client or the vendor?

8. **Assess assumptions and dependencies.**
   - What assumptions is the SOW built on (e.g., client-provided access, data, personnel, environments)?
   - Are the assumptions listed? Are the consequences of failed assumptions defined (e.g., schedule extension, additional fees)?
   - Are client obligations stated with enough specificity to allocate responsibility for dependency failures?

9. **Assess the change-order process.**
   - Is there a defined change-order or change-request process?
   - Can the vendor perform out-of-scope work and bill for it without written approval? This is a scope creep risk.
   - Does the change-order process require written authorization from both parties?

10. **Assess personnel and staffing.**
   - Are key personnel identified? Are there substitution restrictions?
   - Does the client have approval rights over personnel changes?
   - Are subcontractor restrictions addressed?

11. **Assess IP and deliverable ownership.**
    - Who owns custom work product and deliverables created under this SOW?
    - Does the SOW incorporate or conflict with the MSA's IP provisions?
    - Are background IP, third-party components, and open-source software addressed?
    - Is there a license-back provision if the vendor retains ownership?

12. **Assess MSA-SOW consistency** (if MSA is available).
    - Identify any provision in the SOW that conflicts with, overrides, or silently expands an MSA term.
    - Review the MSA's order-of-precedence clause — which document controls in a conflict?
    - Flag any SOW provision that purports to modify MSA terms (e.g., expanded liability, shorter notice periods, different IP ownership) without an explicit MSA amendment.
    - Flag any MSA protection that the SOW appears to waive or narrow.

13. **Build the gap and issues table.** Populate a structured table summarizing each area reviewed with a rating of No Issue / Low / Medium / High and a recommended action.

14. **Rate negotiability and benchmark.** For each material issue, assign one of the six negotiability ratings from `skills/contracts/references/negotiability-ratings.md` — Must Push, Strong Push, Business Call, Acceptable if Balanced, Low Priority, or Do Not Spend Leverage — with a one-line rationale. Where the practice group's `practice-profiles/contracts.md` is loaded, treat its Standard Positions as the playbook for this step; deviations from the profile's positions become the basis for ratings, and profile-silent terms are flagged for attorney review rather than benchmarked. Record any market comparison using `skills/contracts/references/market-benchmark-framework.md`: characterize each relevant term with the controlled vocabulary (Common, Aggressive, Unusual, Depends on Leverage, Needs Attorney Confirmation), state the basis and supporting source, and flag every characterization not backed by a playbook (inline or profile-supplied), comparable, counterparty prior form, or attorney-supplied norm as an attorney-verification item. AgentCounsel does not supply market data.

15. **Draft a prioritized issue list.** Rank the material issues High / Medium / Low. For each High and Medium item, following `skills/contracts/references/redline-output-guidance.md`, state a **Preferred Position**, a **Fallback Position**, and a **Suggested Redline Direction** — the direction of the change, not final clause language. Use `skills/contracts/references/fallback-language-bank.md` to help articulate preferred and fallback positions. Route substantive drafting to an attorney.

16. **Draft a business-friendly summary.** Produce a short, plain-language summary for non-lawyer stakeholders: the handful of things that matter most, what to push on and why, the key tradeoffs that need a business decision, and what — if anything — should stop signature. Use the stakeholder-communication language patterns in `skills/contracts/references/negotiability-ratings.md`. Avoid legal jargon.

17. **List open items for attorney verification.**

18. **Assemble the output** and label it as a draft for attorney review.

## Output Format

Deliver, in order:

1. **Document Summary** — SOW title and number, parties, effective date, governing MSA (if provided), client's role, fee structure summary, delivery timeline summary.
2. **Red Flags Quick Scan** — each red-flag pattern from `skills/contracts/references/red-flags.md` found in the SOW, or a note that none surfaced in the scan.
3. **Scope and Deliverables Assessment** — plain-language summary with flagged ambiguities.
4. **Acceptance Criteria Assessment** — summary of defined (or missing) criteria and process.
5. **Timeline and Milestone Assessment** — summary with risk flags.
6. **Pricing and Payment Assessment** — summary with risk flags.
7. **Assumptions and Dependencies Assessment** — summary of stated assumptions and gaps.
8. **Change-Order Process Assessment** — summary with risk flags.
9. **Personnel and Staffing Assessment** — summary with risk flags.
10. **IP and Deliverable Ownership Assessment** — summary with risk flags.
11. **MSA-SOW Consistency Analysis** — clause-by-clause conflict and consistency findings, or a prominent flag if MSA was not provided.
12. **Gap and Issues Table** — structured table: # | Topic | Finding | Severity (High/Med/Low/None) | Recommended Action | Attorney Note.
13. **Negotiability Table** — a table covering each material issue, with columns: Issue | Negotiability Rating | Basis | Recommended Lawyer Action. The Negotiability Rating is one of the six ratings defined in `skills/contracts/references/negotiability-ratings.md` (Must Push, Strong Push, Business Call, Acceptable if Balanced, Low Priority, Do Not Spend Leverage); the Basis is a one-line rationale.
14. **Market Practice Notes** — any market comparison, recorded using `skills/contracts/references/market-benchmark-framework.md`. Characterize each relevant term with the controlled vocabulary (Common, Aggressive, Unusual, Depends on Leverage, Needs Attorney Confirmation), state the basis and supporting source, and flag every characterization not backed by a playbook, comparable, counterparty prior form, or attorney-supplied norm for attorney verification. AgentCounsel does not supply market data.
15. **Prioritized Issue List** — ranked High / Medium / Low. For each High and Medium item, present these labeled components, following `skills/contracts/references/redline-output-guidance.md`: the issue and why it matters; **Preferred Position**; **Fallback Position**; and **Suggested Redline Direction** (the direction of the change, not final clause language). Use `skills/contracts/references/fallback-language-bank.md` to help articulate preferred and fallback positions.
16. **Business-Friendly Summary** — a short, plain-language summary for non-lawyer stakeholders: the few things that matter most, what to push on and why, the key tradeoffs that need a business decision, and what — if anything — should stop signature. Avoid legal jargon.
17. **Open Items for Attorney Verification** — checkbox list.
18. **Assumptions** — explicit list of all assumptions made about business context, MSA terms, or legal standard.

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
- [ ] The red-flag quick scan and the negotiability table have been reviewed; each of the six-scale negotiability ratings reflects the client's actual leverage and risk tolerance.
- [ ] Every market-practice characterization has a stated basis and supporting source; no market-data assertion has been relied upon without independent verification.
- [ ] Preferred and fallback positions reflect the client's actual leverage and risk tolerance.
- [ ] The business-friendly summary accurately reflects the review and neither overstates nor understates any risk.
- [ ] All `[CONFIRM: ...]` placeholders and open items have been resolved before the SOW is executed or relied upon.
- [ ] The review has been assessed by counsel before it is used in negotiation, execution, or dispute analysis.
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged; profile-silent items are flagged as not-yet-addressed by the playbook.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.
