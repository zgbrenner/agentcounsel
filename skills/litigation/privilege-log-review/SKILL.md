---
name: Privilege Log Review
description: Use when conducting a first-pass review of a privilege log to sort entries into three tiers — confidently privileged, uncertain (flagged for attorney decision), and recommend-remove — so attorney review time focuses on the entries that require judgment.
---

# Privilege Log Review

## Purpose

Produce a structured, attorney-ready first-pass review of a privilege log. The skill sorts each log entry into one of three tiers — confidently privileged, uncertain and flagged for attorney decision, or recommend-remove — and surfaces patterns, format deficiencies, and anomalies. It does not make final privilege calls, strip designations, or decide what to produce or withhold. That judgment belongs to the attorney. The output is draft legal work product for attorney review — not legal advice.

## Use When

- Counsel needs a first-pass triage of a privilege log before conducting a detailed privilege review.
- A privilege log has been received from opposing counsel and counsel wants a structured analysis before a meet-and-confer or motion challenge.
- A party is preparing its own privilege log and wants a quality-control pass to identify thin descriptions, format deficiencies, and likely-challengeable designations before service.
- A large log needs to be organized so attorney review time is concentrated on the close calls rather than the clear cases.

## Required Inputs

- The full privilege log. Each entry must contain at minimum: **date**, **author**, **recipients (To / CC / BCC)**, **document type**, **privilege claimed**, and **description**. If any of these fields are missing across entries, note those entries as format-deficient and proceed with what is available.
- The matter name and number.
- The forum and jurisdiction (court, arbitral body, or regulatory proceeding). If not provided, stop and request it; the applicable privilege rule varies by forum.
- The applicable privilege rule text, if available (e.g., a local rule, standing order, or agreed ESI protocol specifying log format and required fields). If not provided, flag as `[CONFIRM: applicable privilege log rule — verify with counsel]` and proceed using the required-fields list above as the baseline.
- Whether any underlying documents are available for spot-check purposes. If so, identify which entries will be spot-checked; do not review underlying documents beyond the scope provided.
- Whether any use-restriction order or clawback agreement is in effect that limits how the log or its contents may be used.

If the privilege log itself is not provided, stop and request it. Do not proceed without it. Do not fabricate or assume log entries.

## Do Not Use When

- The task is to make a final privilege call on a disputed entry — that is attorney judgment and is out of scope.
- The task is to strip privilege designations from the log and produce a revised log — this skill recommends; it does not modify the log.
- The task is to decide what documents to produce or withhold from production — that is a production decision requiring attorney direction.
- The task is to draft a privilege log from scratch — use a privilege-log-drafting skill instead.
- The document set is a witness's prior statement or deposition transcript being reviewed for privilege issues — that is a separate workflow.
- The matter involves a common-interest arrangement, joint-defense agreement, or other multi-party privilege structure that requires a specialized analysis; flag those entries as `[CONFIRM: multi-party privilege structure — verify with counsel]` and do not attempt to resolve them independently.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- The attorney confirms every privilege designation. This skill produces a recommended tier assignment and flags issues; it does not make or finalize privilege calls.
- **Three-state rule — never silently resolve an uncertain call.** When content is mixed (legal and business advice), when third-party presence is ambiguous, or when litigation-anticipation timing is borderline, keep the privilege designation and route the entry to the Uncertain tier. Do not silently downgrade or upgrade a designation. Prefer the recoverable error: under-marking can waive privilege (potentially irreversible); over-marking is corrected in review (reversible).
- Do not invent, fabricate, or assume log entries, document contents, dates, party identities, or legal authority.
- Do not assert jurisdiction-specific privilege rules as established facts. The scope of attorney-client privilege, the treatment of in-house counsel communications, and the scope of any waiver vary by jurisdiction — treat the applicable rule as `[verify jurisdiction]` until confirmed by the attorney.
- Distinguish what is stated in the log from what is assumed and from what the attorney must confirm. Use `[CONFIRM: ...]`, `[VERIFY: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[citation needed]`, `[verify jurisdiction]`, and `[deadline verification required]` as appropriate.
- If a use-restriction order or clawback agreement is in effect, note at the top of the output that the log and underlying documents are subject to that restriction; do not analyze or disclose contents beyond what is permitted.
- Keep client-sensitive facts and document contents out of reusable versions of this template.
- Flag every point of uncertainty rather than resolving it silently.

## Workflow

1. **Confirm inputs.** Verify that the privilege log, matter, and forum/jurisdiction have been provided. If the log is absent, stop and request it. If the forum or jurisdiction is missing, stop and request it — the applicable privilege rule cannot be identified without it. If the applicable rule text is not provided, note `[CONFIRM: applicable privilege log rule — verify with counsel]` and proceed using the baseline required fields.

2. **Use-restriction check.** Before reviewing any entry, confirm whether a use-restriction order, clawback agreement, or protective order governs this log or the underlying documents. If so, note the restriction prominently at the top of the output and limit the analysis to what is permitted. Flag as `[VERIFY: confirm scope of use restriction with counsel before sharing this review]`.

3. **Format check.** Review the log for required fields. For each entry that is missing one or more required fields (date, author, recipients, document type, privilege claimed, description), flag it as **format-deficient** and note which fields are absent. Format deficiencies are independent of the privilege tier assignment — an entry may be format-deficient and still be placed in a tier based on available information.

4. **Identify the applicable privilege framework.** Note the forum, the claimed privilege types present in the log (e.g., attorney-client, work product, common interest), and the applicable rule text if provided. Note any jurisdiction-specific issues that affect the analysis — in particular, whether in-house counsel communications are treated as privileged in this jurisdiction is `[verify jurisdiction]`. Do not state any specific case name, statute number, or rule number as authority; describe the framework generically and flag all legal propositions for attorney confirmation.

5. **Sort each entry into a tier.** Apply the three-tier framework to each log entry:

   - **Tier 1 — Confidently Privileged:** The entry reflects a clear request for or provision of legal advice between an attorney and client, with no third parties outside the privilege, and the description is sufficient to support the designation. Work-product entries with a clear nexus to anticipated litigation and no indication of waiver also belong here. Do not upgrade an entry to this tier based on a thin description alone.

   - **Tier 2 — Uncertain — Flag for Attorney Decision:** Route entries here when any of the following applies: in-house counsel is an author or recipient and the communication may mix legal advice with business guidance; a third party is present whose relationship to the privilege is unclear; the document appears to have a mixed purpose; an attachment has an independent privilege status that differs from the parent email; litigation anticipation is borderline; a document was shared in a way that may have affected the privilege; or the description is ambiguous. When in doubt, route to this tier rather than Tier 1 or Tier 3. This is the three-state rule in practice.

   - **Tier 3 — Recommend Remove:** Route entries here only when the record clearly supports removal: no attorney is involved in the communication; a lawyer is merely copied on a business communication with no legal-advice nexus evident; the entry describes underlying facts rather than a privileged communication; a third party is clearly outside the privilege; or an attachment is independently non-privileged. Do not place an entry in Tier 3 based on a thin description — route to Tier 2 instead. This skill recommends removal; the attorney decides.

6. **Spot-check underlying documents (if provided).** For any underlying document made available for spot-check purposes, compare the document to its log entry. Note any material discrepancy between the description and the document's actual content, any privilege issue not reflected in the description, and any indication that the document is not what the entry describes. Limit spot-check review to documents specifically provided for this purpose.

7. **Identify patterns and anomalies.** After sorting individual entries, note any of the following patterns that appear across the log: systemic over-designation (e.g., a high proportion of business emails designated as privileged); thin or boilerplate descriptions that impede entry-by-entry evaluation; anomalies in date ranges, parties, or document types that warrant attorney attention; clusters of entries that may involve the same underlying issue or transaction; and any entries where the privilege claimed does not correspond to the description.

8. **Assemble the output.** Using `templates/privilege-log-review-table.md`, produce the structured output: the header block, tier counts, the Tier 2 flagged-entry table, the Tier 3 recommend-remove table, pattern observations, and the open-items list. Label the entire output as draft work product for attorney review.

## Output Format

Deliver a labeled draft using `templates/privilege-log-review-table.md`. The output includes:

- A header block identifying the matter, forum and jurisdiction, applicable rule (or `[CONFIRM]` placeholder), reviewer, and date.
- A tier-count summary: total entries reviewed, Tier 1 count, Tier 2 count, Tier 3 count, and format-deficient count.
- A **Tier 2 — Flagged for Attorney Decision** table: Entry # | Bates/ID | Issue Summary | Points Toward Privilege | Points Against Privilege | Attorney Decision Needed.
- A **Tier 3 — Recommend Remove** table: Entry # | Bates/ID | Reason for Recommendation.
- A **Pattern Observations** narrative section.
- An **Open Items for Attorney Verification** section with `[CONFIRM: ...]` and `[VERIFY: ...]` placeholders.

Use `[CONFIRM: ...]` where attorney confirmation is required. Use `[ATTORNEY TO CONFIRM: ...]` for any designation that the attorney must personally resolve before the log is served or relied upon. Label the full output: `DRAFT — Attorney Work Product — For Attorney Review Only`.

## Attorney Verification Checklist

- [ ] The privilege log provided for review is complete and final, and no entries have been omitted.
- [ ] The forum and jurisdiction have been confirmed, and the applicable privilege rule has been identified and verified.
- [ ] The treatment of in-house counsel communications as privileged (and the scope of any waiver) has been confirmed for this jurisdiction. `[verify jurisdiction]`
- [ ] Every Tier 1 entry has been independently confirmed as privileged by the reviewing attorney.
- [ ] Every Tier 2 entry has been evaluated and a final designation assigned by the reviewing attorney.
- [ ] Every Tier 3 entry has been reviewed by the attorney before any designation is removed and before any document is produced.
- [ ] No privilege designation has been removed or altered based solely on this skill's recommendation.
- [ ] Format deficiencies identified in the review have been addressed or a decision has been made to serve the log as-is.
- [ ] Any use-restriction order, clawback agreement, or protective order has been reviewed and complied with.
- [ ] Pattern observations have been reviewed and any systemic issues have been addressed.
- [ ] All `[CONFIRM]`, `[VERIFY]`, `[ATTORNEY TO CONFIRM]`, and `[verify jurisdiction]` placeholders have been resolved before the log is served or relied upon.
- [ ] Spot-check findings (if any) have been reviewed and any discrepancies between log entries and underlying documents have been resolved.
- [ ] The final log has been reviewed and authorized by the responsible attorney before service.
