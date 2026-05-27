---
name: Regulatory History Tracer
description: "Use when tracing the amendment history of a specific CFR section — what the text said on a given date, which Federal Register rulemakings amended it, and what version was in effect at a specific point in time — producing a date-stable history table for attorney review, verified through `connectors/ecfr.md` and `connectors/federal-register.md`."
practice_area: legal-research
task_type: research
jurisdictions: []
risk_level: medium
requires_attorney_review: true
inputs:
  - "The CFR citation to trace (e.g., 17 C.F.R. § 240.10b-5)"
  - "The relevant date or date range"
  - "The matter or research question this trace supports"
  - "Any specific question about the amendment history"
outputs:
  - "Date-stable regulatory history table with version snapshots and FR amendment references, for attorney review"
related_skills:
  - skills/legal-research/legal-research-memo/SKILL.md
  - skills/regulatory/rule-change-summary/SKILL.md
  - skills/regulatory/enforcement-risk-memo/SKILL.md
tags:
  - legal-research
  - regulatory-history
  - cfr
  - federal-register
  - citations
---

# Regulatory History Tracer

## Purpose

Trace the amendment history of a specific federal regulation — typically a single CFR section — to produce a date-stable history table the attorney can rely on. The trace records what the regulation said on each requested date, which Federal Register rulemakings amended it between dates, and which version was in effect at the date relevant to the matter. The skill produces draft legal work product for attorney review; it is not legal advice, and it does not determine which version of the regulation applies to any specific facts.

The most important disciplines this skill enforces:

- **Date is load-bearing.** Every version snapshot in the trace is anchored to a specific date — usually `[the date relevant to the matter]`, the date of conduct, and today's date. The skill never collapses "the regulation" into a single timeless text.
- **Codified text and rulemaking publication are different artifacts.** The trace separates *what the CFR said on this date* (verified through `connectors/ecfr.md`) from *which Federal Register documents made that text possible* (verified through `connectors/federal-register.md`). Each row of the history table cites both.
- **Codified is not operative.** A regulation can be codified in the CFR but stayed by a court, enjoined, or pending vacatur. The trace records publication and codification only; operative status is a `[verify litigation]` attorney-verification item that the skill does not attempt to resolve.

## Use When

- A matter turns on what a regulation said on a specific date — the date of the conduct, the date of a transaction, a filing date, the effective date of a different rule.
- A litigation team needs to know which version of a CFR section governed during a contested period.
- A regulatory advice matter requires a side-by-side of past, current, and proposed versions of a section.
- A compliance assessment requires knowing which Federal Register documents amended a CFR section in a given window.
- A research workflow has identified a CFR citation but the version, effective date, and history must be locked down before the citation is used.

## Required Inputs

- **The CFR citation to trace** — title, chapter / subchapter / part / subpart, and section (e.g., `17 C.F.R. § 240.10b-5`). The skill traces one citation per run; tracing multiple citations is multiple runs.
- **The relevant date or date range** — the date the matter turns on. If only a date is provided, the trace anchors at that date and today; if a range is provided, the trace anchors at the range endpoints and key amendment dates within the range.
- **The matter or research question this trace supports** — used to focus the trace and to write the *Relevance* slot per row.
- **Operative jurisdiction** — federal regulations apply nationally, but operative interpretation may turn on the circuit; `[verify jurisdiction]` for any forum-specific interpretation.
- Optional: **a specific question about the history** — e.g., "did paragraph (b) read differently before 2020?" or "which FR rulemakings amended this section between 2018 and 2022?"

If the CFR citation or the relevant date is missing, stop and request them. Do not trace a regulation the skill cannot anchor to a date.

## Do Not Use When

- The task is to summarize a single Federal Register document (an NPRM or final rule) — use `regulatory/rule-change-summary`.
- The task is to assess enforcement exposure under a current regulation — use `regulatory/enforcement-risk-memo`.
- The task is to map an organization's controls against a regulation — use `regulatory/compliance-gap-matrix`.
- The regulation is non-federal (state, local, foreign) — `connectors/ecfr.md` and `connectors/federal-register.md` are federal only; this skill is out of scope for non-federal sources.
- The task is to predict whether a regulation will be amended or vacated — that is attorney work informed by the trace, not the trace itself.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Every version snapshot and every Federal Register reference traces to a verified source — `connectors/ecfr.md` for the codified text on a date, `connectors/federal-register.md` for the publication of the rulemaking that amended the text. No version snapshot appears in the trace unless the codified text has been retrieved at that snapshot date or the snapshot is explicitly flagged as `[VERIFY: snapshot — eCFR connector not available in this session]`.
- Produce draft legal work product for attorney review. This is not legal advice and is not a determination of which version applies to any specific matter.
- **Do not trace from memory.** If the eCFR connector is not available in the session, the trace records what the user has provided (e.g., a pasted version) and flags every other snapshot as unverified. The skill does not reconstruct regulatory history from background knowledge.
- **Codified is not operative.** The trace records publication and codification only. Whether a version was stayed, enjoined, or vacated during a window is an attorney-verification item the trace flags but does not resolve.
- **Effective vs. compliance dates.** Where the source rulemaking distinguished an effective date from one or more compliance dates, preserve every date as the FR document recorded it. Do not collapse them.
- **Paraphrase is not the regulation.** Where the trace summarizes what a version said, the summary is labeled as a paraphrase and the verbatim text is available via the eCFR URL recorded in the row. Quotations in the trace appear in quotation marks only when verbatim from a connector-retrieved snapshot.
- **Snapshot date is on the face of every row.** No version statement appears without a snapshot date and a connector URL (or a `[VERIFY: ...]` flag if no connector is available).
- **Consult `connectors/ecfr.md` and `connectors/federal-register.md`.** Where a connector is unavailable, the trace continues but every snapshot and every Federal Register reference carries the `not verified — no <X> connector available` flag.
- **Litigation status is `[verify litigation]`.** The trace does not attempt to determine whether any version was stayed, enjoined, or under court challenge. Where the matter raises that question, the trace flags it and routes to attorney review or to `connectors/courtlistener.md` for case-law research.
- Use `[CONFIRM: ...]` and `[VERIFY: ...]` placeholders for any element whose support is unsettled.

## Workflow

1. **Confirm inputs.** Verify the CFR citation, the relevant date or date range, and the matter context. If any required input is missing, stop and request it.

2. **Anchor the trace.** Identify the snapshot dates the trace will produce. By default: (a) the relevant date, (b) today, and (c) any user-specified additional dates. For a date range, also include the range endpoints and any known amendment dates between.

3. **Retrieve each snapshot via `connectors/ecfr.md`.** For each anchor date, query the eCFR Versioner API to retrieve the codified text of the cited section on that date. Record the snapshot date, the eCFR URL, and either the verbatim text or a labeled paraphrase, per the discipline above. If a snapshot date is outside eCFR's historical coverage (roughly 2017 forward, varies by title), retain a `[VERIFY: snapshot — outside eCFR historical coverage]` flag.

4. **Identify amendment dates between snapshots.** Compare consecutive snapshots. Where the text differs, an amendment occurred between the two dates. Note the difference in a Diff block (added language, removed language, structural change).

5. **Locate amending Federal Register documents.** For each amendment identified, query `connectors/federal-register.md` for final rules that amended the section between the two snapshot dates. Record the FR citation, document number, agency, publication date, effective date, and any stated compliance dates. Use the agency name as a filter when the publishing agency is known.

6. **Per amendment, write a History Row.** Each row records: amendment date (effective date from the FR document), the FR document reference (citation + verified URL), the agency, a one-paragraph description of what changed, the pre-amendment and post-amendment text (or verbatim references to the snapshots), and a `[verify litigation]` flag where there is any indication the amendment may have been stayed, enjoined, or otherwise challenged.

7. **Identify gaps in the history.** Time windows where a snapshot is unavailable (pre-2017 history, missing eCFR data, missing FR match) are recorded as gaps with `[VERIFY: ...]` flags. The trace does not fill gaps from memory.

8. **Operative-status flag.** For each row, add a `[verify litigation]` flag if the amendment is recent or if the user has indicated litigation may have affected the regulation. The trace does not attempt to resolve operative status.

9. **Per-row Relevance.** For each row, write a short *Relevance to this matter* slot noting whether the version was in effect on the matter's relevant date and what the matter-side question might be (without answering it).

10. **List assumptions and open items.** Note jurisdictional assumptions, connector availability, the temporal coverage of eCFR for this title, and every `[CONFIRM: ...]` / `[VERIFY: ...]` flag.

11. **Assemble the trace** and label it as a draft for attorney review.

## Output Format

A regulatory-history trace with the following sections, in order:

1. **Header** — CFR citation, operative jurisdiction, relevant date, matter context, privilege designation.
2. **Version Snapshots Table** — one row per anchor date: snapshot date, eCFR URL (or `[VERIFY: ...]` flag), verbatim text or labeled paraphrase, source confidence.
3. **Amendment History Rows** — one row per amendment identified between snapshots: effective date, FR citation + verified URL, agency, what changed, pre / post text references, `[verify litigation]` flag.
4. **Gaps** — windows with no available snapshot or no located FR amendment; each gap explicit.
5. **Per-row Relevance** — short note tying each amendment to the matter's relevant date and question.
6. **Operative-status flags** — explicit list of `[verify litigation]` items.
7. **Assumptions** — connector availability, eCFR temporal coverage, jurisdictional scope.
8. **Open items / Attorney verification** — checklist.

## Attorney Verification Checklist

- [ ] The CFR citation is correct and the trace covers the section the matter actually turns on.
- [ ] Every snapshot date is the date intended; the relevant date in particular has been confirmed.
- [ ] Each snapshot's verbatim text or paraphrase has been verified against the eCFR URL recorded in the row.
- [ ] Each amendment row's FR document reference has been verified via the Federal Register connector.
- [ ] Every `[verify litigation]` flag has been resolved through case-law research or attorney confirmation that no litigation affected the regulation.
- [ ] Gaps in coverage have been addressed — either by an alternative source for pre-eCFR history or by attorney acceptance that the gap is acceptable for the matter.
- [ ] The version in effect on the matter's relevant date has been confirmed and is the version the matter analysis will use.
- [ ] Operative status (stayed / enjoined / vacated) has been independently verified through case-law and agency-action research; the trace alone does not establish operative status.
- [ ] All `[CONFIRM: ...]` and `[VERIFY: ...]` placeholders have been resolved before the trace is relied upon.
- [ ] The trace is approved as the basis for downstream memo, advice, or compliance work, or revised before reliance.
