---
name: Entity Compliance Review
description: Use when organizing and reviewing an organization's corporate-entity compliance status — periodic filings, registered-agent status, and good standing — into a structured review that flags overdue, due-soon, and unknown items as draft work product for attorney review.
---

# Entity Compliance Review

## Purpose

Produce a structured, attorney-ready review of an organization's corporate-entity compliance posture. The review organizes what the user supplies about each entity's periodic filing obligations — annual reports, franchise filings, foreign-qualification registrations, registered-agent status, and good-standing currency — and flags items that are overdue, due soon, of unknown status, or otherwise requiring verification.

This skill records and organizes information supplied by the user. It does not populate, calculate, or infer any filing deadline, fee, due date, or filing requirement from model background knowledge. Every obligation in the output comes from the user; everything else is flagged for confirmation with the registered agent or the relevant authority. The output is draft legal work product for attorney review — not legal advice and not a substitute for a registered-agent compliance calendar.

## Use When

- A user asks to "review our entity compliance," "check our good-standing status," or "organize our filing obligations" across a portfolio of legal entities.
- An in-house team or outside counsel wants a structured snapshot of where each entity stands on periodic filing and good-standing obligations before a transaction, audit, or board presentation.
- A prior registered-agent compliance report or internal tracker needs to be organized and gap-flagged in attorney-ready format.
- The user needs to identify which entities are overdue, due soon, or without a recent good-standing confirmation, so the attorney can prioritize remediation.

## Required Inputs

- **Entity list.** For each entity:
  - Legal name (as formed or registered).
  - Entity type (corporation, LLC, limited partnership, limited liability limited partnership, or other — specify).
  - Jurisdiction of formation.
  - Any additional jurisdictions where the entity is qualified or registered to do business (foreign qualification).
  - Name of registered agent and, if applicable, whether a registered-agent service is managing the compliance calendar.
  - Formation date or, if unavailable, the approximate year of formation.

- **Filing obligations the user is tracking.** For each obligation:
  - Filing type (e.g., annual report, biennial report, franchise tax filing, foreign-qualification renewal, registered-agent designation — use the user's own label; do not rename or recharacterize).
  - Due basis: whether the due date is tied to a fixed calendar date, an anniversary of formation, an anniversary of qualification, or another basis (describe; do not infer).
  - Last-filed date (or "unknown" if not on file).
  - Current status as reported by the user: current, due soon, overdue, unknown, or managed by registered-agent service.

Optional but recommended:
- A prior compliance review or registered-agent compliance report, to use as a reference for gap identification.
- Any notes the user has about dormant or inactive entities under consideration for dissolution.

If the entity list is not provided, stop and request it. Do not proceed on a partial entity list without noting which entities are absent and flagging all outputs accordingly. If filing obligations for a given entity and jurisdiction are not provided, record the status as "unknown" and flag it for confirmation — do not supply obligations from model background knowledge.

## Do Not Use When

- The user wants a filing made, a good-standing certificate obtained, or a registered agent appointed — this skill produces a review document, not filings.
- The user wants to know whether the entity is legally required to qualify to do business in a particular jurisdiction — that is a fact-dependent legal determination for the attorney; this skill can flag a potential foreign-qualification gap but cannot resolve it.
- The user wants a regulatory-compliance gap analysis against a body of substantive regulation (environmental, securities, licensing, etc.) — use `compliance-gap-matrix` instead.
- The user wants to analyze the entity structure for tax efficiency, restructuring, or M&A purposes — those are separate legal and tax engagements.
- The entity list has not been provided and the user is asking the agent to generate a hypothetical entity list — do not fabricate entities or obligations.

## Legal Safety Rules

- Produce draft legal work product for attorney review. This is not legal advice. Attorney review and sign-off are required before any filing obligation or compliance posture is relied upon.
- **Never populate a filing obligation, deadline, fee, or requirement from model background knowledge.** Filing rules are jurisdiction-specific, entity-type-specific, and subject to change. If the user has not supplied an obligation, record its status as "unknown" and flag it for confirmation with the registered agent or the relevant authority.
- **Entity-type discipline.** Filing obligations depend on both the jurisdiction and the entity type. A corporation, an LLC, and a limited partnership formed in the same jurisdiction can have materially different obligations, due dates, and fees. Never transfer an obligation from one entity type to another. Never assume that because one entity in a jurisdiction has a particular obligation, another entity of a different type in the same jurisdiction shares it.
- **Compute nothing.** Do not calculate whether a filing is overdue or due soon based on a date you derive or assume. Record the status the user provides. Mark every date in the output `[deadline verification required]` to signal that it has not been confirmed against the filing authority or the registered agent.
- Every deadline, fee, and filing requirement is reference-only. Confirm all items with the registered agent or the relevant authority before relying on them. A registered-agent service's compliance calendar is authoritative; where one is in place, note that the agent's calendar governs.
- Do not invent citations, statutes, regulations, administrative rules, or case law. Treat all model background knowledge about corporate law and filing requirements as unverified.
- Distinguish facts (what the user supplied), assumptions (what was inferred), and items requiring verification. Label each category explicitly.
- Flag every point of uncertainty with a bracketed placeholder: `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[citation needed]`, `[verify jurisdiction]`, or `[deadline verification required]`. Never resolve uncertainty silently.
- Foreign-qualification gap flags are informational only. Whether an entity is legally required to qualify in a given jurisdiction depends on the nature and extent of its activities there — a fact-dependent question for the attorney. The skill flags the gap; it does not answer the question.
- Preserve confidentiality and privilege. Do not place client-sensitive entity names, ownership details, or transaction context into a reusable copy of the template.

## Workflow

1. **Confirm inputs.** Verify that the entity list has been provided with, at minimum, each entity's name, entity type, and jurisdiction of formation. Verify that the user has supplied filing obligations for each entity and jurisdiction combination, or has indicated that obligations are unknown. If the entity list is missing or materially incomplete, stop and request it. If filing obligations are not supplied for one or more entities, proceed but record each missing item as "unknown" and note the gap prominently.

2. **Map the entity roster.** List each entity in the order supplied. For each entity, record: legal name, entity type, jurisdiction of formation, foreign-qualification jurisdictions (if any), registered agent, and formation date. Do not add entities, entity types, or jurisdictions that the user has not mentioned.

3. **Record filing obligations — user-supplied only.** For each entity and each jurisdiction (formation and any foreign-qualification jurisdictions), record the filing obligations the user has supplied. Use the user's own labels for filing types; do not rename or recharacterize them. For each obligation, capture:
   - Filing type (user-supplied label).
   - Due basis (as described by the user: fixed date, anniversary of formation, anniversary of qualification, or other).
   - Last-filed date (or "unknown").
   - Current status (current, due soon, overdue, unknown, or managed by registered-agent service).
   - Any notes the user has provided.

   For every obligation not supplied by the user for a given entity-jurisdiction-type combination, insert a row with status "unknown" and flag it: `[VERIFY: confirm filing obligations with registered agent or filing authority for this jurisdiction and entity type]`.

4. **Apply entity-type discipline.** Before finalizing the table, confirm that no obligation has been copied or inferred across entity types. Each entity's obligations must derive solely from what the user supplied for that entity. Insert a note wherever entity-type uncertainty exists: `[ATTORNEY TO CONFIRM: entity type determines applicable filing obligations — confirm before relying on this row]`.

5. **Flag dates.** Mark every due date and last-filed date in the output `[deadline verification required]`. Do not compute whether a filing is overdue or due soon from a date you derive. Record the status the user provides.

6. **Build the status summary.** From the recorded obligations, produce three lists:
   - **Overdue items:** obligations where the user-reported status is "overdue." List entity, entity type, jurisdiction, filing type, and any date provided, each marked `[deadline verification required]`.
   - **Due-soon items:** obligations where the user-reported status is "due soon." Same columns.
   - **Unknown-status items:** obligations where the status is "unknown" or where no obligation was supplied. Flag each for confirmation with the registered agent or the relevant authority.

   Note: where a registered-agent service is managing an entity's compliance calendar, record that fact and note that the agent's calendar is authoritative for due dates and status.

7. **Build the audit view.** Flag the following for attorney attention:
   - **Dormant or inactive entities:** entities the user has identified as dormant, or entities with no recent filings or activity noted in the supplied information. Flag each for attorney review regarding potential dissolution or withdrawal from foreign jurisdictions.
   - **Stale good-standing confirmations:** entities for which the user has not supplied a recent good-standing confirmation, or for which the last-confirmed date is not provided. Flag: `[VERIFY: obtain current good-standing certificate before reliance — confirm with filing authority or registered agent]`.
   - **Potential foreign-qualification gaps:** entities with operational presence in a jurisdiction for which no foreign qualification is noted in the supplied information. Flag each as a potential gap and note: `[ATTORNEY TO CONFIRM: whether this entity's activities in this jurisdiction require foreign qualification is a fact-dependent legal determination — do not rely on this flag as a legal conclusion]`. Do not assert that qualification is or is not required.

8. **Assemble the output.** Combine: (a) the entity compliance table from `templates/entity-compliance-table.md`, populated from the user-supplied information with placeholders for every unknown item; (b) the overdue / due-soon / unknown-status summary; (c) the audit view; (d) the assumptions section; and (e) the attorney verification checklist. Label the entire output as a draft for attorney review.

## Output Format

Deliver:

1. **Entity Compliance Review** — a complete draft using `templates/entity-compliance-table.md`, populated from the user-supplied information. Every date flagged `[deadline verification required]`. Every unknown obligation flagged for confirmation.
2. **Overdue / Due-Soon / Unknown-Status Summary** — three labeled lists drawn from the table, each identifying the entity, entity type, jurisdiction, filing type, and user-reported status.
3. **Audit View** — flagged items for attorney attention: dormant entities, stale good-standing confirmations, and potential foreign-qualification gaps, each with the appropriate placeholder and a note on what the attorney must confirm.
4. **Assumptions** — an explicit list of every assumption made in producing the review, including any inference about entity type, jurisdiction, or filing status drawn from context rather than from a user-supplied statement.
5. **Attorney Verification Checklist** — the checklist from this skill.

Use placeholders consistently. Do not fill any gap with content derived from model background knowledge about filing rules or deadlines.

## Attorney Verification Checklist

- [ ] The entity list is complete and reflects all active legal entities in the organization's portfolio, including wholly owned subsidiaries, joint ventures, and foreign-qualified entities.
- [ ] Each entity's name, entity type, and jurisdiction of formation are confirmed against the entity's formation documents or official records.
- [ ] Filing obligations for each entity in each jurisdiction have been confirmed with the registered agent or the relevant filing authority — not derived from model background knowledge. `[verify jurisdiction]`
- [ ] Entity-type distinctions have been respected: obligations for one entity type have not been applied to an entity of a different type in the same jurisdiction. `[verify jurisdiction]`
- [ ] Every due date and last-filed date has been confirmed against the registered agent's calendar or the filing authority's records. `[deadline verification required]`
- [ ] All items marked "overdue" have been reviewed and a remediation plan (cure filing, penalty assessment, or reinstatement) has been initiated or documented. `[verify jurisdiction]`
- [ ] All items marked "due soon" are on the registered agent's or counsel's docket for timely action. `[deadline verification required]`
- [ ] All items marked "unknown" have been investigated and resolved before any reliance on the review.
- [ ] Good-standing status for each entity in each jurisdiction has been confirmed by a current good-standing certificate from the filing authority, not by reliance on the last-known status in this review.
- [ ] Dormant or inactive entities flagged in the audit view have been reviewed for dissolution, cancellation, or withdrawal from foreign jurisdictions, as appropriate. `[verify jurisdiction]`
- [ ] Foreign-qualification gaps flagged in the audit view have been reviewed by the attorney to determine whether qualification is legally required given the entity's actual activities in each jurisdiction. `[verify jurisdiction]`
- [ ] Registered-agent designations are current and accurate in every jurisdiction where each entity is formed or qualified.
- [ ] No filing deadline, fee, or legal requirement stated in this review has been asserted on the basis of model background knowledge without independent verification.
- [ ] No legal authority, statute, or regulation has been cited in this review without verification by the attorney.
- [ ] All placeholders and open items are resolved before this review is relied upon for any filing, transaction, or compliance certification.
- [ ] The finalized review has been approved by the reviewing attorney before distribution or filing.
