---
name: Severance Review
description: "Use when reviewing a severance or separation agreement to produce a structured analysis of consideration, release scope, restrictive covenants, and open legal issues for attorney review."
practice_area: employment
task_type: review
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The severance or separation agreement text"
  - "The party the review is for: employer or employee"
  - "The termination and consideration context"
outputs:
  - "Structured analysis of consideration, release scope, and restrictive covenants"
  - "Open legal issues for attorney review"
related_skills:
  - skills/contracts/contract-risk-review/SKILL.md
  - skills/employment/termination-risk/SKILL.md
tags:
  - employment
  - severance
  - separation-agreement
  - release-of-claims
  - contract-review
---

# Severance Review

## Purpose

Produce a structured, attorney-ready review of a severance or separation agreement. The skill identifies the key provisions, assesses their scope and risk from the perspective of the indicated party, flags claims that may not be waivable and statutory requirements that must be confirmed, and surfaces issues for attorney resolution. This is draft legal work product — not legal advice.

## Use When

- A user asks to "review this severance agreement" or "what am I giving up if I sign this?"
- An employee or employer has received a proposed separation agreement and needs a first-pass structured review.
- Counsel needs a provision-by-provision issues list to begin their own analysis.
- A user wants to understand what claims a release covers before agreeing or rejecting.
- The user phrases it as: "help me understand what this says," "is this a good deal," or "what should we look at before signing?"

## Required Inputs

- **The full agreement text**: uploaded or pasted. Do not review from a description — the actual document text is required.
- **Reviewing party**: employee/departing worker or employer/company. The analysis will be framed from this party's perspective.
- **Jurisdiction**: the state, province, or country whose law governs the agreement, or flag as unknown.
- **Employee age**: confirm whether the employee is age 40 or over, as this affects statutory disclosure and timing requirements. If unknown, flag for attorney confirmation.

If the agreement text is not provided, stop and request it. Do not summarize, analyze, or opine on an agreement that has not been provided.

## Do Not Use When

- The document is a general employment contract rather than a severance or separation agreement (use `contract-risk-review` or a general contract review skill).
- The termination has not yet occurred and the question is whether to proceed with it (use `termination-risk`).
- The user is asking whether a particular claim is legally viable or what damages they might recover — those questions require legal advice from counsel, not this skill.
- The user wants to draft a severance agreement from scratch rather than review an existing one (a separate drafting skill applies).

## Legal Safety Rules

- Produce draft legal work product for attorney review only. This is not legal advice.
- Review only the language actually present in the provided document. Do not infer or supply terms that are not written.
- Do not assert what claims are or are not waivable in any jurisdiction. Flag all waiver questions for attorney confirmation.
- Do not assert specific statutory timeframes, disclosure requirements, or consideration-period rules. Flag them as `[CONFIRM: with counsel]` — these vary by jurisdiction, agreement type, and circumstances.
- Do not place client-identifying or sensitive factual information into reusable template copies.
- Separate what the document says from what you assume and from what the attorney must verify. Label each category.
- Flag every non-standard or one-sided provision rather than characterizing it as acceptable or unacceptable — that assessment belongs to the attorney.
- Do not calculate monetary values, tax obligations, or net consideration without flagging the calculation as unverified and in need of accountant/counsel review.
- Use `[CONFIRM: ...]` wherever governing law, enforceability, or factual basis is uncertain.

## Workflow

1. **Confirm inputs.** Verify that the agreement text, reviewing party, and jurisdiction are available. If the agreement text is missing, stop and request it. If jurisdiction or employee age is unknown, flag for attorney confirmation and proceed with the remaining review.

2. **Identify the document structure.** Read through the full agreement and identify: the parties, the effective date, the recitals or context, and the overall organization of provisions. Note any defined terms that control the scope of key provisions.

3. **Analyze consideration offered.** Identify what the employer is providing (severance pay amount and schedule, benefits continuation, equity treatment, outplacement, references, other). Note whether additional consideration beyond existing entitlements is provided, and flag for attorney assessment of whether it is adequate to support the release.

4. **Analyze the release of claims.** Identify: the scope of claims released (described claims, time period covered, released parties), explicit carve-outs (workers' compensation, EEOC charge rights, vested benefits), and any language purporting to release future claims, pending claims, or non-waivable claims. Flag all potentially non-waivable claim waivers for attorney review — do not conclude on their enforceability.

5. **Assess statutory disclosure and timing requirements.** Note whether the agreement includes recitations about review period, right to consult counsel, and revocation rights. Flag the adequacy of these provisions for attorney confirmation, noting that requirements vary by jurisdiction and by the employee's age and circumstances. Use `[CONFIRM: applicable periods and disclosures]`.

6. **Identify restrictive covenants.** Extract and summarize every non-compete, non-solicitation (customer and employee), non-disparagement, and confidentiality/non-disclosure provision. For each: note the scope (geographic, industry, duration, parties covered), any carve-outs, and remedies stated. Flag enforceability for attorney review — do not assert enforceability conclusions.

7. **Identify cooperation and return-of-property obligations.** Note any post-separation cooperation requirements (litigation support, government inquiries), duration, compensation, and reimbursement terms. Flag open-ended cooperation obligations for attorney assessment.

8. **Review confidentiality provisions.** Note what the employee is required to keep confidential, any exceptions (e.g., communications with government agencies, attorneys, tax advisors), and what obligations apply to the employer. Flag overly broad confidentiality provisions.

9. **Review reference and announcement provisions.** Identify what, if anything, the agreement says about employment references, the reason for departure stated internally or externally, and LinkedIn or other social media references to the separation.

10. **Identify tax allocation provisions.** Note how the agreement allocates the severance payment for tax purposes (e.g., wages, damages, attorneys' fees). Flag the allocation for review by a tax professional and counsel — do not assert tax treatment.

11. **Assess missing or unusual provisions.** Note any provisions that are absent from the agreement that are commonly included (e.g., no mutual non-disparagement, no indemnification carve-out, no equity treatment clause) or that are unusual in scope. List them as potential negotiation points or gaps for attorney assessment.

12. **Build the issues table.** Organize identified issues by provision, priority (High / Medium / Low), party burdened, and recommended attorney action.

13. **Assemble the output.** Produce the full structured review labeled as a draft for attorney review.

## Output Format

Deliver the following sections, clearly labeled:

1. **Agreement Overview** — parties, effective date, structure, and defined terms of significance.
2. **Consideration Summary** — what is being offered and by whom; flag adequacy question for attorney.
3. **Release Analysis** — scope of claims released, carve-outs, and flagged concerns about non-waivable claims.
4. **Statutory Disclosures & Timing** — summary of review period and revocation right language present in the document; `[CONFIRM: adequacy with counsel]`.
5. **Restrictive Covenants Summary** — plain-language table of each covenant's scope, duration, and geographic reach; enforceability flagged for attorney.
6. **Other Key Provisions** — cooperation, return of property, confidentiality, reference, tax allocation.
7. **Issues Table** — structured table: Provision | Summary of Issue | Priority | Party Burdened | Attorney Action.
8. **Open Items for Attorney Verification** — numbered list of unresolved legal questions.
9. **Assumptions** — explicit list of facts assumed in the absence of confirmed information.

Use `[CONFIRM: ...]` throughout for any unverified legal or factual point. Label the complete output: *Draft legal work product for attorney review. Not legal advice.*

## Attorney Verification Checklist

- [ ] The complete, final agreement text was reviewed; no pages or attachments are missing.
- [ ] The reviewing party and their objectives have been confirmed.
- [ ] Consideration is confirmed as adequate and legally sufficient to support the release under applicable law.
- [ ] The scope of the release has been reviewed against the employee's actual claims and circumstances.
- [ ] Claims identified as potentially non-waivable have been assessed under applicable federal, state, and local law.
- [ ] All statutory disclosure and timing requirements (consideration period, revocation right, required language) have been confirmed for the applicable jurisdiction and employee characteristics.
- [ ] OWBPA requirements confirmed if the employee is age 40 or older or the release involves a group termination.
- [ ] Each restrictive covenant has been assessed for enforceability under applicable law.
- [ ] Cooperation obligations have been reviewed for scope, duration, and compensation.
- [ ] Tax allocation has been reviewed by a qualified tax professional and/or tax counsel.
- [ ] All open items and `[CONFIRM]` placeholders have been resolved before the agreement is signed or presented.
- [ ] No legal conclusions in this document have been relied upon without attorney review.
