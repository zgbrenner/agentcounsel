---
name: Vendor Agreement Status
description: "Use when assembling a consolidated status report of the agreements in place with a given vendor — what is executed, current, expired, or missing — with a gap analysis, upcoming dates, and surviving obligations for attorney review."
practice_area: contracts
task_type: extraction
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The vendor's identity, including known name variations and parent or subsidiary relationships"
  - "The executed agreements, amendments, statements of work, DPAs, NDAs, and related records the user provides"
  - "The relationship context and whether the vendor handles personal data"
  - "Optional: the agreement types the firm expects for a vendor of this type"
outputs:
  - "Vendor overview and records-reviewed summary"
  - "Agreement inventory with apparent status and key dates"
  - "Gap analysis, upcoming dates, and surviving obligations"
related_skills:
  - skills/contracts/contract-risk-review/SKILL.md
  - skills/contracts/nda-review/SKILL.md
  - skills/contracts/sow-review/SKILL.md
  - skills/privacy/dpa-review/SKILL.md
tags:
  - contracts
  - vendor-management
  - agreement-inventory
  - gap-analysis
  - contract-lifecycle
---

# Vendor Agreement Status

## Purpose

Produce a structured, attorney-ready draft status report of the agreements in place with a given vendor. The skill inventories the agreement records provided, reports the apparent status of each, runs a gap analysis against the agreement types the firm expects for a vendor of that kind, and flags upcoming dates and surviving obligations.

This skill provides workflow discipline and structure. It produces draft legal work product for attorney review. This is not legal advice, and a status report is not a legal opinion on the enforceability of any agreement or the adequacy of coverage.

## Use When

- A user says "what agreements do we have with this vendor?", "pull the vendor agreement status," or "consolidate everything we have with this supplier."
- A renewal, a new engagement, or a vendor risk review is approaching and the team needs a consolidated view.
- The user needs a gap analysis showing which expected agreements with a vendor are missing.

## Required Inputs

- **Vendor identity**: the vendor's name, including known name variations, abbreviations, and any parent-or-subsidiary relationships that affect which entity contracted.
- **Agreement records**: the executed agreements, amendments, statements of work, data processing agreements, NDAs, insurance certificates, and related documents the user provides. The skill reviews the materials supplied; it does not query a CLM, CRM, email, or any other external system.
- **Relationship context**: what the vendor does for the organization and whether the vendor handles personal data.
- **Expected agreement set** (optional): the agreement types the firm expects for a vendor of this type. If not provided, use a general expected set and flag it as not firm-specific.

If no agreement records are provided, stop and request them.

## Do Not Use When

- The user expects the agent to search a CLM, CRM, email, or document store — this skill reviews only the records the user supplies, and notes which expected sources were not available.
- The task is to review one agreement for risk — use `contract-risk-review`, or `nda-review` / `sow-review` / `dpa-review` for those document types.
- The task is to summarize the changes between two drafts — use `redline-summary`.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice; a status report is not a legal opinion on enforceability or coverage.
- Report only on the documents actually provided. Never invent agreements, amendments, dates, parties, or terms.
- State clearly which records were reviewed and which expected sources were not available, so the report's coverage is transparent.
- Report the apparent status of an agreement (in force, expired, superseded) as drawn from the document — not as a legal conclusion. Status must be verified against the original documents.
- Compute renewal, expiry, and notice dates only from dates in the documents. Flag every date `[CONFIRM: date]`. Do not invent or assume dates.
- Flag any agreement that appears expired but may carry surviving obligations.
- Flag any case where the vendor handles personal data but no data processing agreement was provided.
- Distinguish: facts drawn from the documents, the gap analysis, upcoming dates, and verification items.
- Preserve confidentiality; do not place vendor-identifying terms into reusable templates.
- Flag every gap and every record that could not be located.

## Workflow

1. **Confirm the vendor identity.** Reconcile name variations and abbreviations, and confirm which entity in any parent-or-subsidiary group is the actual counterparty. Flag any ambiguity as `[CONFIRM: vendor entity]`.

2. **Inventory the agreement records.** List every record the user provided, with its document type and an identifier.

3. **Report each agreement.** For each agreement, record: type; the contracting parties; apparent status; effective and expiry dates; auto-renewal or notice terms; key provisions relevant to status (term, termination, survival); and amendment history.

4. **Run the gap analysis.** Compare the agreements found against the expected agreement set for a vendor of this type — typically an NDA, a master services agreement, a data processing agreement, statements of work, a service-level agreement, and insurance certificates. Flag each expected agreement that is missing.

5. **Run the personal-data check.** If the vendor handles personal data and no data processing agreement is among the records, flag it prominently.

6. **Identify upcoming dates.** List agreements expiring within a near-term window, and any renewal or notice deadlines. Flag every date `[CONFIRM: date]`.

7. **Identify surviving obligations.** For each expired or terminated agreement, note any clause — confidentiality, indemnity, IP, data return or deletion — that may survive termination.

8. **Note coverage limits.** Record which expected sources or records were not available for review.

9. **Assemble the report** and label it a draft.

## Output Format

Deliver the following sections in order:

**DRAFT VENDOR AGREEMENT STATUS REPORT — FOR ATTORNEY REVIEW**

1. **Vendor Overview** — the vendor identity, the contracting entity, the relationship context, and whether the vendor handles personal data.

2. **Records Reviewed and Sources Not Available** — the records reviewed and a clear statement of which expected sources or records were not available.

3. **Agreement Inventory** — table: agreement type, parties, apparent status, effective date, expiry date, auto-renewal or notice terms, amendment history.

4. **Gap Analysis** — the expected agreement set and which agreements appear to be missing.

5. **Personal-Data / DPA Check** — whether the vendor handles personal data and whether a data processing agreement is in place.

6. **Upcoming Dates and Deadlines** — agreements expiring soon and any renewal or notice deadlines, each flagged `[CONFIRM: date]`.

7. **Surviving Obligations** — for expired or terminated agreements, the clauses that may survive.

8. **Open Questions** — vendor-identity ambiguities, missing records, and items needing follow-up.

9. **Attorney Verification Items** — see the Attorney Verification Checklist below.

## Attorney Verification Checklist

- [ ] The vendor identity and the correct contracting entity have been confirmed.
- [ ] The status of each agreement has been verified against the original executed document.
- [ ] Every effective, expiry, renewal, and notice date has been verified against the documents; no date was invented or assumed.
- [ ] The gap analysis reflects the agreement types the firm actually expects for a vendor of this type.
- [ ] Where the vendor handles personal data, a current data processing agreement is in place, or its absence has been escalated.
- [ ] Surviving obligations in expired or terminated agreements have been reviewed and are being honored where they apply.
- [ ] The sources that were not available for review have been noted, and any material agreement believed to exist but not located has been retrieved.
- [ ] Auto-renewal and notice deadlines have been calendared so no renewal or termination window is missed.
- [ ] The report is labeled appropriately and its coverage limits are understood by anyone relying on it.
