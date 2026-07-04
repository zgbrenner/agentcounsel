---
name: Negative Treatment Check
description: "Use when you need to check whether the authorities cited in a draft or research memo are still good law — organizing a citator-style verification plan for each authority, recording provided citator-report signals as attributed claims, and classifying each authority's verification status, without ever asserting from model memory that a case is good law, overruled, or distinguished."
practice_area: legal-research
task_type: analysis
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The draft, memo, or citation list whose authorities need treatment verification"
  - "For each authority: the full citation as it appears in the source"
  - "Optional: any citator reports or validation printouts the user has already obtained"
  - "Optional: access to a citation-verification connector (e.g., connectors/courtlistener.md) for federal case law"
outputs:
  - "Authority-by-authority treatment-verification table"
  - "A verification plan for each authority, using available connectors and user-supplied citator reports"
  - "Verification-status classification and attorney sign-off items"
related_skills:
  - skills/legal-research/authority-synthesis/SKILL.md
  - skills/legal-research/legal-research-memo/SKILL.md
  - skills/legal-methodology/citation-integrity-check/SKILL.md
tags:
  - legal-research
  - citator
  - negative-treatment
  - good-law
  - citation-verification
  - source-validation
---

# Negative Treatment Check

## Purpose

Organize a disciplined "is this still good law" check for every authority cited in a draft or research memo. For each authority, the skill records the citation as provided, structures a verification plan using available connectors and any user-supplied citator reports, and classifies the authority's verification status. It never asserts from model memory that a case is good law, has been overruled, superseded, limited, or distinguished — model-memory treatment claims are exactly the hallucination this library exists to prevent. Every treatment conclusion is either drawn from a provided, attributed source or left as an explicit `[Verify current law]` item for attorney confirmation. This is draft legal work product for attorney review, not legal advice.

## Use When

- A research memo or brief is nearly final and every cited authority needs a good-law check before it is filed or relied upon.
- A user asks "is this case still good law?" or "have any of these authorities been overruled?" and wants the verification organized rather than guessed.
- A citation list has been assembled and the team needs a treatment-verification plan before an attorney signs off.
- Citator reports have been pulled from a vendor service and the signals need to be organized into a per-authority status table.
- A cited authority is old, from a fast-moving area, or central to the argument, and its current status must be confirmed.

## Required Inputs

- **The draft, memo, or citation list** whose authorities need checking, with each authority's full citation as it appears in the source. If only a description is provided, request the actual citations — never reconstruct a citation.
- Optional: **any citator reports or validation printouts** the user has already obtained from a citation service. These are recorded as attributed claims from a provided source.
- Optional: **access to a citation-verification connector** (for example, `connectors/courtlistener.md` for federal case law) — used to confirm that an authority exists and to retrieve its text and later history where the connector supports it.

If no citations are provided, stop and request them. Do not generate or assume citations to check.

## Do Not Use When

- The task is to synthesize authorities into a rule or to build the substantive analysis — use `authority-synthesis`; run this check after synthesis, before finalizing.
- The task is to verify that citations are formatted correctly and that quotations match their sources — use `citation-integrity-check`; this skill checks treatment (still-good-law status), not citation form.
- The task is to draft the research memo itself — use `legal-research-memo`.
- The user wants a definitive statement that a case is or is not good law without any provided citator source — this skill cannot supply that; it organizes verification and flags the gap.
- No authorities are cited — there is nothing to check.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- **Never assert treatment from model memory.** Do not state — from your own knowledge — that any authority is good law, has been overruled, reversed, superseded, abrogated, limited, criticized, or distinguished. Treatment claims not drawn from a provided, attributed source are the exact hallucination risk this skill exists to contain. State this limitation plainly in the output.
- **Record vendor citator signals as attributed claims, never as confirmed facts.** When a user supplies a citator report, record what the report states (its flags, its listed citing references, its date) attributed to that report — never independently "confirm" or upgrade it. Note that citator services can lag and can miss treatment; the attorney verifies.
- **Connector results verify existence and history, not legal status.** A connector can confirm an opinion exists, retrieve its text, and surface later citing documents where supported — it does not adjudicate whether the authority remains good law. Frame connector findings accordingly.
- Classify every authority's status explicitly, and default to `[Verify current law]` whenever the status rests on anything other than a provided, attributed citator source.
- Never compute or assert a date. Record the dates a provided report or connector states, attributed to the source.
- Distinguish throughout: what a provided report or connector states (attributed), what the user stated, what is assumed, and what the attorney must verify.
- Preserve confidentiality: keep the matter's authorities and any work-product framing out of reusable templates.

## Workflow

1. **Confirm inputs.** Verify the citation list (or the draft's authorities) is provided with full citations. Note which citator reports the user supplied and whether a verification connector is available. Request anything missing.
2. **Extract the authority list.** List every authority cited in the source — cases, statutes, regulations, rules, and secondary sources — with its full citation exactly as it appears and the proposition it is cited for. Flag any citation that is incomplete or malformed as `[CONFIRM: citation]` (and route form issues to `citation-integrity-check`).
3. **State the limitation up front.** Open the working notes with the explicit statement that no treatment status in this output is asserted from model memory, and that every "current" status rests on a provided citator source or an attorney's own verification.
4. **Plan verification for each authority.** For each authority, record the verification path: which supplied citator report covers it; whether a connector (e.g., CourtListener for federal case law) can confirm existence and retrieve later history; and what the attorney will still need to run in a full citator service. Note where no verification source is available at all.
5. **Record provided citator signals.** Where the user supplied a citator report, record for each authority: the report's treatment flag or signal (as the report labels it), the citing references it lists, and the report's date — each attributed to the report. Do not translate a vendor's caution flag into a legal conclusion.
6. **Record connector findings.** Where a connector was used, record that the authority exists (or that it could not be located — a prominent flag), its retrieved metadata, and any later citing documents the connector surfaced, each attributed to the connector. Do not infer good-law status from the presence or absence of citing documents.
7. **Note high-risk authorities.** Flag authorities that warrant heightened verification: old cases, cases in fast-moving or recently-legislated areas, cases central to the argument, and any authority relied on for a proposition broader than its holding (route the proposition-scope question to `authority-synthesis`).
8. **Classify each authority's verification status.** Assign one of: **Verified current (attorney-confirmed)** — only where an attorney has confirmed; **Citator report provided** — status per an attributed report, attorney to confirm; **Connector-existence-only** — existence confirmed, treatment not; **Unverified** — no treatment source, treat as `[Verify current law]`. Default to Unverified when in doubt.
9. **Assemble the treatment-verification table** and list, prominently, every authority that is Unverified or that a provided report flags for attention.
10. **List attorney verification items and assemble the output.** Consolidate placeholders, assemble the output in the format below, label it a draft for attorney review, and attach the checklist.

## Output Format

Deliver the following, in order, labeled `DRAFT — For Attorney Review — Treatment Not Confirmed From Model Knowledge`:

1. **Summary** — one paragraph: how many authorities were checked, how many remain Unverified, and the explicit statement that no treatment status is asserted from model memory.
2. **Verification Limitation Notice** — the plain statement from Step 3.
3. **Treatment-Verification Table** — columns: Authority (full citation) | Cited For | Verification Source (report / connector / none) | Reported Signal (attributed) | Status Classification | Flags.
4. **High-Risk Authorities** — the authorities from Step 7 needing heightened verification, with the reason.
5. **Unverified Authorities** — every authority with no treatment source, each `[Verify current law]`.
6. **Verification Plan** — for each authority, what the attorney must still run to confirm status.
7. **Attorney Verification Items** — every placeholder consolidated.
8. **Assumptions** — every assumption made, listed explicitly.

Use `[Verify current law]` on every status not resting on an attorney's own confirmation. Do not fill gaps with invented content.

## Attorney Verification Checklist

- [ ] Every authority in the source has been captured, with a complete, correct citation.
- [ ] No treatment status in this draft was asserted from model knowledge; each status rests on a provided citator source or attorney verification.
- [ ] Every authority has been run through a full citator service by the attorney or a qualified researcher.
- [ ] Any authority a provided report flagged for negative or cautionary treatment has been read and assessed in context.
- [ ] Authorities central to the argument have been independently confirmed as current good law.
- [ ] For each authority, the proposition it supports has been checked against its actual holding, not just its good-law status.
- [ ] Connector-existence-only authorities have had their treatment confirmed through a citator, not inferred from citing-document counts.
- [ ] Old authorities and authorities in fast-moving or recently-amended areas have received heightened verification.
- [ ] Statutes and regulations have been checked for currency against the official code, not only through case citators. `[Verify current law]`
- [ ] Every Unverified authority has been resolved or removed before the draft is relied upon.
- [ ] No date in this draft was computed; all dates are attributed to a provided report or connector.
- [ ] The citation form of every authority has been separately verified (via `citation-integrity-check`).
- [ ] All `[Verify current law]` and `[CONFIRM: ...]` placeholders have been resolved before the memo or brief is filed or relied upon.
