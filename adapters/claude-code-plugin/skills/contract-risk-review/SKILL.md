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

If the contract text or the client's role is not provided, stop and request it. Do not begin risk assessment by guessing at facts.

## Do Not Use When

- The document is an NDA or confidentiality agreement (use `nda-review`).
- The user needs to summarize changes between two contract versions (use `redline-summary`).
- The document is a statement of work or work order (use `sow-review`, and also confirm consistency with the governing MSA).
- The contract is a consumer-facing terms of service or privacy policy — those require a compliance-oriented review this skill does not cover.
- The user needs a formal legal opinion or a certified compliance review — those require attorney sign-off this skill cannot provide.

## Legal Safety Rules

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

## Workflow

This skill draws on shared contract-review reference material in `skills/contracts/references/`: `red-flags.md` (red-flag catalogue), `negotiability-ratings.md` (negotiability rubric), `market-benchmark-framework.md` (benchmarking discipline), `document-type-checklists.md` (per-document-type checklists), and `redline-output-guidance.md` (how to frame redline direction). Consult them at the steps noted below.

1. **Confirm inputs.** Verify that you have the full contract text, the client's role, business context, and whether this is the counterparty's form or a negotiated draft. If anything is missing, request it before proceeding.

2. **Identify and orient.** State the document title, parties, effective date (or `[CONFIRM: effective date]`), governing law (or `[CONFIRM: governing law]`), and the client's contractual role. Note whose form this appears to be.

3. **Map the structure.** Identify each major section and confirm which standard clause categories are present and which are absent. Missing provisions are themselves a risk finding. Use the matching checklist in `skills/contracts/references/document-type-checklists.md` for this document type.

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

8. **Rate negotiability and benchmark.** For each material issue, assign a negotiability rating using the rubric in `skills/contracts/references/negotiability-ratings.md`, with a one-line rationale drawn from leverage, who drafted the form, the deal value, and any regulatory floor. Record any market comparison using `skills/contracts/references/market-benchmark-framework.md`: state the basis for each benchmark and flag every unverified benchmark as an attorney-verification item. AgentCounsel does not supply market data.

9. **Draft prioritized issue list.** Rank all identified issues as High / Medium / Low priority for the client based on likelihood and impact. For each High and Medium item, following `skills/contracts/references/redline-output-guidance.md`, state a **Preferred Position**, a **Fallback Position**, and a **Suggested Redline Direction** — the direction of the change, not final clause language. Route substantive drafting to an attorney.

10. **Internal consistency check.** Confirm that defined terms, party names, cross-references, exhibit and schedule references, and section numbers are used consistently throughout the contract. Flag any defined-but-unused term, used-but-undefined term, broken cross-reference, mismatched party label, missing exhibit, or numbering gap.

11. **List open items for attorney verification.** Include every unverified assumption, every `[CONFIRM: ...]` placeholder, and every issue requiring legal judgment before execution.

12. **Assemble the output** and label it clearly as a draft for attorney review.

## Output Format

Deliver, in order:

1. **Document Summary** — parties, effective date, governing law, client's role, counterparty's form or negotiated draft, approximate transaction value/risk profile.
2. **Structural Map** — list of sections present and absent.
3. **Red Flags Quick Scan** — each red-flag pattern from `skills/contracts/references/red-flags.md` found in the contract, or a note that none surfaced in the scan.
4. **Clause-by-Clause Summary** — plain-language summary of each category with risk note.
5. **Risk Matrix** — completed using `templates/contract-risk-matrix.md`, with two severity dimensions rated per clause: **Legal Risk** (High / Med / Low) for the client's legal exposure, and **Business Friction** (Blocking / Slowing / Confusing / None) for the practical operational impact. A term can be legally enforceable yet operationally damaging, or legally marginal yet a deal-blocker operationally — both dimensions should be captured.
6. **Negotiability Rating** — for each material issue, a rating from the rubric in `skills/contracts/references/negotiability-ratings.md`, with a one-line rationale.
7. **Market Benchmark Notes** — any market comparison, recorded using `skills/contracts/references/market-benchmark-framework.md`, with its basis stated; every unverified benchmark flagged for attorney verification.
8. **Prioritized Issue List** — ranked High / Medium / Low. Each High and Medium item states a **Preferred Position**, a **Fallback Position**, and a **Suggested Redline Direction** (direction of change, not final language), following `skills/contracts/references/redline-output-guidance.md`.
9. **Missing Provisions** — list of standard protections absent from the agreement.
10. **Internal Consistency Check** — whether defined terms, party names, cross-references, exhibit/schedule references, and section numbers are used consistently, with any inconsistency flagged.
11. **Open Items for Attorney Verification** — checkbox list.
12. **Assumptions** — explicit list of all assumptions made about business context, facts, or legal standard.

Use `[CONFIRM: ...]` wherever a fact, clause meaning, or legal conclusion is unverified or ambiguous.

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
- [ ] The red-flag quick scan and negotiability ratings have been reviewed; every market benchmark has a stated basis and was independently verified.
- [ ] Preferred and fallback positions reflect the client's actual leverage and risk tolerance.
- [ ] The internal consistency check is complete; defined terms, cross-references, and exhibits are sound.
- [ ] All missing provisions have been assessed for materiality and whether their absence is acceptable.
- [ ] All `[CONFIRM: ...]` placeholders and open items have been resolved before the review is relied upon.
- [ ] The review has been assessed by counsel before it is used in negotiation, execution, or reliance.
