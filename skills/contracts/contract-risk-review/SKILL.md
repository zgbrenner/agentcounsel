---
name: Contract Risk Review
description: "Use when reviewing a general commercial contract — such as a master services agreement, vendor agreement, supplier contract, or professional services agreement — to produce a structured risk assessment and prioritized issue list for attorney review."
practice_area: contracts
task_type: review
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The full commercial contract text"
  - "The client's role under the agreement"
  - "The business and transaction context"
  - "Optional: the client's standard positions or playbook"
outputs:
  - "Structured risk matrix"
  - "Prioritized issues list for attorney review"
related_skills:
  - skills/contracts/nda-review/SKILL.md
  - skills/contracts/redline-summary/SKILL.md
  - skills/contracts/sow-review/SKILL.md
tags:
  - contracts
  - contract-review
  - commercial-contract
  - risk-matrix
  - redline
---

# Contract Risk Review

## Purpose

Produce a structured, attorney-ready risk review of a commercial contract. This skill applies to master services agreements (MSAs), vendor and supplier agreements, professional services agreements, software licenses, and similar commercial instruments. It identifies and assesses risk across standard clause categories, produces a completed risk matrix, and surfaces issues requiring attorney attention before the contract is executed, modified, or relied upon.

This skill produces draft legal work product for attorney review only. It is not legal advice and does not constitute a final negotiating position.

## Use When

- A user asks to "review this contract," "flag the risks in this agreement," "what should I push back on," or "is this MSA standard."
- A vendor, supplier, or service provider has sent a contract and the client needs a first-pass review before negotiation or execution.
- The user is preparing to redline a commercial agreement and needs a structured starting point.
- A contract is being renewed or amended and the user wants to understand baseline risk exposure.
- An in-house team or business owner needs a risk summary before escalating to outside counsel.
- The user needs to compare risk posture across multiple inbound form agreements.

## Required Inputs

- **The full contract text** — uploaded or pasted. Do not review from a description, summary, or excerpt alone; the full document is required.
- **The client's role** — which party is the client (e.g., customer/buyer, vendor/service provider, licensor, licensee)?
- **Business context** — what is the commercial relationship, what is being provided or received, and what is the approximate transaction value or risk exposure?
- **Counterparty form or negotiated draft** — note whether this is the counterparty's standard form (higher scrutiny) or a negotiated draft.
- Optional: the practice group's `practice-profiles/contracts.md` if it has been populated and is loaded alongside this skill. If present, the skill uses its Standard Positions and Escalation Thresholds tables to benchmark the output and to gate escalation. If absent, the skill proceeds without practice-profile benchmarking and asks the user to supply standing positions inline if needed.

If the contract text or the client's role is not provided, stop and request it. Do not begin risk assessment by guessing at facts.

## Do Not Use When

- The document is an NDA or confidentiality agreement (use `nda-review`).
- The user needs to summarize changes between two contract versions (use `redline-summary`).
- The document is a statement of work or work order (use `sow-review`, and also confirm consistency with the governing MSA).
- The contract is a consumer-facing terms of service or privacy policy — those require a compliance-oriented review this skill does not cover.
- The user needs a formal legal opinion or a certified compliance review — those require attorney sign-off this skill cannot provide.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- Review only the language actually present in the provided document. Quote clause language accurately; never paraphrase beyond what the text supports.
- Do not invent contract terms, section numbers, defined terms, or quotations. If you cannot find a clause, say so — do not fabricate its absence or presence.
- Do not invent statutes, regulations, case law, or market-standard assertions. "Market standard" claims require attorney verification unless the user has provided comparative data.
- Do not invent or assume procedural deadlines, notice periods, or cure periods; read them from the document or flag them as missing.
- Distinguish clearly: (1) what the contract says, (2) what you are assuming about the business context, (3) what is flagged for attorney verification.
- Identify (or flag as unknown): jurisdiction and governing law, choice of forum, relevant effective date, and which party's form this is.
- Do not place client-sensitive facts into reusable templates.
- Use `[CONFIRM: ...]` placeholders wherever information is missing or uncertain.
- Flag every point of uncertainty rather than resolving it silently.
- **Severity floor.** Once an issue has been rated High severity in the risk table or issues list, that rating must not be silently downgraded. Any reduction in severity is an explicit attorney decision and must be recorded as such (e.g., "Downgraded from High to Medium by [attorney], [date], reason: [brief rationale]"). This applies regardless of the counterparty's explanation or commercial commonness of the provision.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/contracts.md` is loaded, its Standard Positions and Escalation Thresholds inform the draft but never substitute for attorney judgment. The profile is a configuration record approved by the practice group; it is not legal advice and does not override the skill's normal attorney-verification gates. If the profile's standing positions conflict with the matter facts or with what the supervising attorney concludes, the attorney prevails.

## Workflow

This skill draws on shared contract-review reference material in `skills/contracts/references/`: `red-flags.md` (red-flag catalogue), `negotiability-ratings.md` (six-rating negotiability rubric), `market-benchmark-framework.md` (benchmarking discipline and market-practice vocabulary), `fallback-language-bank.md` (sample preferred and fallback positions by clause type), `document-type-checklists.md` (per-document-type checklists), `clause-category-checklist.md` (cross-document clause-category completeness sweep), `market-standard-baselines.md` (open-standard baseline comparisons), and `redline-output-guidance.md` (how to frame redline direction). Consult them at the steps noted below.

1. **Confirm inputs.** Verify that you have the full contract text, the client's role, business context, and whether this is the counterparty's form or a negotiated draft. If anything is missing, request it before proceeding.

2. **Identify and orient.** State the document title, parties, effective date (or `[CONFIRM: effective date]`), governing law (or `[CONFIRM: governing law]`), and the client's contractual role. Note whose form this appears to be.

3. **Map the structure.** Identify each major section and confirm which standard clause categories are present and which are absent. Missing provisions are themselves a risk finding. Use the matching checklist in `skills/contracts/references/document-type-checklists.md` for this document type, and run the full `skills/contracts/references/clause-category-checklist.md` as a fast completeness sweep across all five clause groups before the deeper clause-by-clause review.

4. **Red flags quick scan.** Run a fast first pass against the red-flag catalogue in `skills/contracts/references/red-flags.md`. Record each red-flag pattern present, or note that none surfaced in the scan. This scan orients the deeper review; it does not replace it.

5. **Review clause by clause across standard categories.** For each category below, summarize what the contract says in plain language, identify the risk to the client, and note what changes — if any — are warranted:
   - Parties and authorized signatories
   - Term and renewal (auto-renewal, notice windows)
   - Scope of services / obligations (specificity, exclusivity, change mechanisms)
   - Fees, payment terms, price adjustment, late payment
   - Intellectual property ownership and license grants (work-for-hire, background IP, residual rights)
   - Confidentiality (scope, carve-outs, duration, return/destruction)
   - Data privacy and security obligations (data types, breach notification, processor terms)
   - Representations and warranties (scope, survival, disclaimers)
   - Indemnification (triggers, scope, procedure, reciprocity)
   - Limitation of liability and caps (exclusions from cap, consequential damages waiver)
   - Insurance requirements
   - Termination rights (for cause, for convenience, cure periods, effects of termination)
   - Dispute resolution and governing law (arbitration, jury waiver, jurisdiction/venue)
   - Assignment and change of control
   - Unusual, one-sided, or non-standard clauses

   **Limitation-of-liability decomposition.** Do not collapse the liability-cap and consequential-damages provisions into a single rating. Break the analysis into four dimensions: (a) the treatment of direct versus indirect/consequential damages — quote the exact exclusion language; (b) the cap base or amount as written (e.g., fees paid in the prior 12 months, total contract value) — quote it verbatim; (c) the carve-outs from the cap and how each interacts with the overall allocation (e.g., IP indemnity, fraud, willful misconduct, death/personal injury, data breach); and (d) how the overall allocation sits relative to the client's realistic risk exposure and the value of the contract. Flag each dimension separately in the risk matrix.

   **IP-clause depth.** When the contract assigns or licenses intellectual property, go beyond ownership labeling. Check for: (a) whether assignment language is in the present tense (a present-tense grant, e.g., "hereby assigns") versus a mere promise to assign in the future — a future promise may require a further act to perfect the transfer [verify jurisdiction]; (b) the treatment of moral rights, including whether any waiver is included [verify jurisdiction]; (c) a further-assurances or cooperation obligation requiring the assignor to execute additional documents to perfect the assignment; and (d) carve-outs from the assignment (e.g., retained background IP, pre-existing tools, residual knowledge). Flag any assignment gap as a potential diligence risk.

   **Specialization note.** SaaS, subscription, and vendor agreements warrant heightened attention to: auto-renewal mechanics and notice windows; unilateral price-escalation rights; service levels, uptime commitments, and associated remedies; and data terms (processing, retention, portability, deletion). If the contract is for an AI vendor, AI-enabled service, or involves AI-generated outputs, route to or also apply the `ai-vendor-terms-review` skill, which covers model transparency, output liability, training-data rights, and AI-specific data terms.

6. **Assess missing protections.** Note standard commercial protections that are absent and assess whether their absence is a material risk.

7. **Build the risk matrix.** Complete `templates/contract-risk-matrix.md` for each clause category reviewed.

8. **Rate negotiability and benchmark.** For each material issue, assign one of the six negotiability ratings from `skills/contracts/references/negotiability-ratings.md` — Must Push, Strong Push, Business Call, Acceptable if Balanced, Low Priority, or Do Not Spend Leverage — with a one-line rationale drawn from leverage, who drafted the form, the deal value, and any regulatory floor. Where the practice group's `practice-profiles/contracts.md` is loaded, treat its Standard Positions as the playbook for this step; deviations from the profile's positions become the basis for ratings, and profile-silent terms are flagged for attorney review rather than benchmarked. Record any market comparison using `skills/contracts/references/market-benchmark-framework.md`: characterize each relevant term with the controlled vocabulary (Common, Aggressive, Unusual, Depends on Leverage, Needs Attorney Confirmation), state the basis and supporting source, and flag every characterization not backed by a playbook (inline or profile-supplied), comparable, counterparty prior form, or attorney-supplied norm as an attorney-verification item. AgentCounsel does not supply market data. Where the contract is a SaaS, cloud, or data-processing agreement, also consider a baseline comparison against the Bonterms or Common Paper open standards using `skills/contracts/references/market-standard-baselines.md`.

9. **Draft prioritized issue list.** Rank all identified issues as High / Medium / Low priority for the client based on likelihood and impact. For each High and Medium item, following `skills/contracts/references/redline-output-guidance.md`, state a **Preferred Position**, a **Fallback Position**, and a **Suggested Redline Direction** — the direction of the change, not final clause language. Use `skills/contracts/references/fallback-language-bank.md` to help articulate preferred and fallback positions. Route substantive drafting to an attorney.

10. **Internal consistency check.** Confirm that defined terms, party names, cross-references, exhibit and schedule references, and section numbers are used consistently throughout the contract. Flag any defined-but-unused term, used-but-undefined term, broken cross-reference, mismatched party label, missing exhibit, or numbering gap.

11. **List open items for attorney verification.** Include every unverified assumption, every `[CONFIRM: ...]` placeholder, and every issue requiring legal judgment before execution.

12. **Draft a business-friendly summary.** Produce a short, plain-language summary aimed at non-lawyer stakeholders: the handful of things that matter most, what the client should push on and why, the key tradeoffs that need a business decision, and what — if anything — would stop the deal. Use the stakeholder-communication language patterns in `skills/contracts/references/negotiability-ratings.md`. Avoid legal jargon.

13. **Assemble the output** and label it clearly as a draft for attorney review.

## Output Format

Deliver, in order:

1. **Document Summary** — parties, effective date, governing law, client's role, counterparty's form or negotiated draft, approximate transaction value/risk profile.
2. **Structural Map** — list of sections present and absent.
3. **Red Flags Quick Scan** — each red-flag pattern from `skills/contracts/references/red-flags.md` found in the contract, or a note that none surfaced in the scan.
4. **Clause-by-Clause Summary** — plain-language summary of each category with risk note.
5. **Risk Matrix** — completed using `templates/contract-risk-matrix.md`, with two severity dimensions rated per clause: **Legal Risk** (High / Med / Low) for the client's legal exposure, and **Business Friction** (Blocking / Slowing / Confusing / None) for the practical operational impact. A term can be legally enforceable yet operationally damaging, or legally marginal yet a deal-blocker operationally — both dimensions should be captured.
6. **Negotiability Table** — a table covering each material issue, with columns: Issue | Negotiability Rating | Basis | Recommended Lawyer Action. The Negotiability Rating is one of the six ratings defined in `skills/contracts/references/negotiability-ratings.md` (Must Push, Strong Push, Business Call, Acceptable if Balanced, Low Priority, Do Not Spend Leverage); the Basis is a one-line rationale.
7. **Market Practice Notes** — any market comparison, recorded using `skills/contracts/references/market-benchmark-framework.md`. Characterize each relevant term with the controlled vocabulary (Common, Aggressive, Unusual, Depends on Leverage, Needs Attorney Confirmation), state the basis and supporting source, and flag every characterization not backed by a playbook, comparable, counterparty prior form, or attorney-supplied norm for attorney verification. AgentCounsel does not supply market data.
8. **Prioritized Issue List** — ranked High / Medium / Low. For each High and Medium item, present these labeled components, following `skills/contracts/references/redline-output-guidance.md`: the issue and why it matters; **Preferred Position**; **Fallback Position**; and **Suggested Redline Direction** (the direction of the change, not final clause language). Use `skills/contracts/references/fallback-language-bank.md` to help articulate preferred and fallback positions.
9. **Missing Provisions** — list of standard protections absent from the agreement.
10. **Internal Consistency Check** — whether defined terms, party names, cross-references, exhibit/schedule references, and section numbers are used consistently, with any inconsistency flagged.
11. **Business-Friendly Summary** — a short, plain-language summary for non-lawyer stakeholders: the few things that matter most, what to push on and why, the key tradeoffs that need a business decision, and what — if anything — would stop the deal. Avoid legal jargon.
12. **Open Items for Attorney Verification** — checkbox list.
13. **Assumptions** — explicit list of all assumptions made about business context, facts, or legal standard.

Use `[CONFIRM: ...]` wherever a fact, clause meaning, or legal conclusion is unverified or ambiguous.

### Optional: Business Stakeholder Summary

When the output will be used to brief a non-lawyer business stakeholder — a product owner, deal lead, people manager, founder, or executive — add a **Business Stakeholder Summary** as a clearly separated, plainly labeled section, following `core/business-stakeholder-communication.md`. Produce it only when the user requests it or when the audience is plainly a business decision-maker. It is an addition to the deliverable above — never a replacement for it, and never a substitute for attorney review. It contains:

- **Business Summary** — the bottom line in plain language, with unnecessary legal jargon removed and legal risk stated separately from business and commercial risk.
- **Decision Needed** — the specific business decision(s) now on the table, stated as concrete choices, each with its owner.
- **Recommended Ask** — the legal team's recommended position or course of action, framed as a recommendation for the business to weigh, not a decision made on its behalf.
- **Fallback Position** — the minimum acceptable alternative if the Recommended Ask cannot be achieved.
- **Escalation Needed?** — whether the matter should be escalated, to whom (senior management, the board, or outside counsel), and why — or a plain statement that no escalation is needed.

## Attorney Verification Checklist

- [ ] The document reviewed is the complete, final, and correct version of the contract.
- [ ] All section references and clause quotations have been verified against the source document.
- [ ] The client's contractual role and business context are accurately stated.
- [ ] Governing law and jurisdiction have been confirmed and are appropriate.
- [ ] Risk ratings reflect the client's actual negotiating leverage and risk tolerance.
- [ ] IP ownership and license grant analysis is correct given the nature of the deliverables.
- [ ] Data privacy obligations have been assessed against applicable regulatory requirements (e.g., GDPR, CCPA) — this skill does not perform a regulatory compliance review.
- [ ] Indemnification scope and limitation-of-liability caps are consistent with the client's insurance coverage.
- [ ] No market-standard assertions have been relied upon without independent verification.
- [ ] The red-flag quick scan and the negotiability table have been reviewed; each of the six-scale negotiability ratings reflects the client's actual leverage and risk tolerance.
- [ ] Every market-practice characterization has a stated basis and supporting source and was independently verified; no unsupported market-data assertion has been relied upon.
- [ ] Preferred and fallback positions reflect the client's actual leverage and risk tolerance.
- [ ] The business-friendly summary accurately reflects the review and neither overstates nor understates any risk.
- [ ] The internal consistency check is complete; defined terms, cross-references, and exhibits are sound.
- [ ] All missing provisions have been assessed for materiality and whether their absence is acceptable.
- [ ] All `[CONFIRM: ...]` placeholders and open items have been resolved before the review is relied upon.
- [ ] The review has been assessed by counsel before it is used in negotiation, execution, or reliance.
- [ ] If a practice profile was loaded: every Standard Position and Escalation Threshold that applies to the matter facts has been surfaced; deviations are flagged; profile-silent items are flagged as not-yet-addressed by the playbook.
- [ ] If no practice profile was loaded: any benchmarking or "standard position" framing in the output is grounded in user-supplied inline data, not assumed.
