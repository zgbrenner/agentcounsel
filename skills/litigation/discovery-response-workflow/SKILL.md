---
name: Discovery Response Workflow
description: "Use when organizing responses to written discovery — document requests, interrogatories, or requests for admission — inventorying each request verbatim into a response tracker, organizing objection candidates and privilege candidates as questions for counsel, planning collection and custodians, and drafting response shells with placeholders, without ever drafting a final objection or recommending an admit/deny."
practice_area: litigation
task_type: analysis
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The written discovery served: the document requests, interrogatories, and/or requests for admission, in full"
  - "The matter context: parties, claims, the client's role, and the governing forum as stated"
  - "The response deadline as stated (recorded, never computed)"
  - "Optional: the operative pleadings and any prior discovery in the matter"
  - "Optional: a custodian and data-source list, if collection has begun"
outputs:
  - "Request-by-request response tracker with each request quoted verbatim"
  - "Objection candidates and privilege candidates organized as questions for counsel"
  - "Collection and custodian plan, and draft response shells with placeholders"
related_skills:
  - skills/litigation/subpoena-triage/SKILL.md
  - skills/litigation/privilege-log-review/SKILL.md
  - skills/litigation/legal-hold/SKILL.md
  - skills/litigation/litigation-chronology/SKILL.md
  - skills/legal-methodology/privilege-confidentiality-check/SKILL.md
tags:
  - litigation
  - discovery
  - interrogatories
  - requests-for-admission
  - document-requests
  - objections
---

# Discovery Response Workflow

## Purpose

Produce a structured, attorney-ready organization of a response to written discovery — requests for production of documents, interrogatories, and requests for admission (RFAs). The skill inventories each request verbatim into a response tracker, organizes objection candidates and privilege candidates as questions for counsel, plans collection and custodians, and drafts response shells with placeholders for counsel's positions. It never drafts a final objection, never asserts that an objection applies, and — for RFAs — never recommends an admit or deny, because the effect of an admission is an attorney decision. This is draft legal work product for attorney review, not legal advice.

## Use When

- Written discovery has been served and the team needs it organized into a trackable, request-by-request response plan.
- A responding party wants objection candidates and privilege candidates surfaced for counsel before drafting responses.
- Interrogatories or document requests need to be mapped to custodians, data sources, and owners for collection.
- Requests for admission have been served and each needs to be organized with its factual basis for counsel's admit/deny decision.
- Counsel wants response shells drafted with placeholders so the substantive positions can be filled in efficiently.

## Required Inputs

- **The written discovery served**, in full — the document requests, interrogatories, and/or RFAs. If only a description is provided, stop and request the actual text. Never reconstruct a request.
- **The matter context**: the parties, the claims and defenses, the client's role (plaintiff, defendant, third party), and the governing forum as stated.
- **The response deadline as stated** — recorded exactly as provided and flagged `[deadline verification required]`; never computed.
- Optional: **the operative pleadings and any prior discovery** — needed to assess relevance and scope.
- Optional: **a custodian and data-source list**, if collection has begun.

If the discovery text or the matter context is missing, stop and request it before substantive work.

## Do Not Use When

- The discovery is a third-party subpoena rather than party discovery — use `subpoena-triage`; this skill is for responding to discovery served on the client as a party.
- The task is to build or review a privilege log — use `privilege-log-review`; this skill flags privilege candidates and routes them there.
- The task is to issue a litigation hold or organize preservation — use `legal-hold`; collection planning here assumes preservation is handled.
- The user wants the final objections drafted, or a decision on whether to admit or deny an RFA — those are attorney decisions this skill only organizes.
- The task is to draft affirmative discovery requests to serve on another party — that is a separate drafting task, not covered here.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- **Never draft a final objection or assert that an objection applies.** Organize objection *candidates* (relevance, overbreadth, burden, vagueness, privilege) as questions for counsel. Whether to object, and on what grounds, is a counsel decision with waiver consequences.
- **For requests for admission, never recommend admit or deny.** The legal effect of an admission — including a deemed admission from a missed or improper response — is significant and is an attorney decision. Organize each RFA with its factual basis and the open questions; do not resolve it.
- **Privilege is handled with care.** Flag privilege candidates and route them to `privilege-log-review` and `privilege-confidentiality-check`; never make a final privilege call, and never place potentially privileged content into a shared response draft without counsel's direction.
- **Never compute a deadline.** Discovery response deadlines, extensions, and meet-and-confer timing are recorded as stated and flagged `[deadline verification required]`. Missing or near-term deadlines are surfaced prominently for immediate attorney attention.
- Do not assert what the governing rules require as to scope, proportionality, or response form — those are `[verify jurisdiction]` `[Verify current law]` items keyed to the forum's rules.
- Quote each request verbatim; do not paraphrase a request in a way that narrows or broadens it.
- Distinguish throughout: what the request says (quoted), what the pleadings or user stated, what is assumed, and what counsel must verify.
- Preserve confidentiality and work-product protection: discovery responses are attorney work product; flag sensitive material rather than exposing it, and keep matter facts out of reusable templates.

## Workflow

1. **Confirm inputs.** Verify the discovery text, the matter context, and the stated response deadline are provided. Request anything missing before proceeding.
2. **State the gates.** Record the parties, the client's role, the governing forum (`[verify jurisdiction]` for the applicable discovery rules), the discovery type(s) served, and the response deadline exactly as stated (`[deadline verification required]`). Surface any near-term deadline at the top for immediate attorney attention.
3. **Inventory every request verbatim.** Assign each request an ID and record its exact text, its type (RFP / interrogatory / RFA), and any sub-parts. Note discrete-subpart counts where the forum's numerical limits may matter — as a question for counsel, `[ATTORNEY TO CONFIRM: subpart counting and numerical limits]`.
4. **Map each request to the pleadings.** For each request, note the claim, defense, or allegation it appears to bear on, drawn from the operative pleadings. Where relevance is unclear from the face of the request, flag it as a scope question for counsel — never conclude a request is or is not relevant.
5. **Organize objection candidates.** For each request, list the objection candidates the language raises (relevance, overbreadth, undue burden, vagueness/ambiguity, proportionality, privilege, premature/expert-timing, form) as questions for counsel, with the feature of the request that prompts each. Never draft the objection or assert it applies; note that unasserted objections may be waived — a reason to route promptly to counsel.
6. **Flag privilege candidates.** Identify requests likely to capture privileged or work-product material, and note the need for a privilege log. Route the privilege calls to `privilege-log-review` and `privilege-confidentiality-check`. Do not make a final privilege determination.
7. **Plan collection and custodians (RFPs and interrogatories).** For requests calling for documents or data, organize the likely custodians, data sources, date ranges, and search parameters as facts and open questions. Confirm that preservation is handled (route to `legal-hold` if not). Flag proportionality questions for counsel.
8. **Organize interrogatory answers as fact-gathering.** For each interrogatory, list the information sought, the likely owner of the answer, and the source documents needed — as a fact-gathering task, not a drafted answer. Flag contention interrogatories for counsel (their timing and the level of detail are counsel decisions).
9. **Organize each RFA with its factual basis.** For each RFA, record the fact it asks the party to admit, the documents or witnesses bearing on it, and the open questions — never a recommended admit/deny. Flag RFAs whose wording is compound or ambiguous as `[CONFIRM: RFA wording]` for a possible objection question.
10. **Draft response shells.** For each request, draft a response shell with placeholders: `[COUNSEL: objections]`, `[COUNSEL: response / admit-deny position]`, and a statement-of-production or answer placeholder — following the forum's response form as a `[verify jurisdiction]` item. The shells are scaffolding for counsel, never final responses.
11. **Assemble the tracker and open items.** Consolidate the request-by-request tracker, the collection plan, the privilege-candidate list, and every deadline (each `[deadline verification required]`).
12. **List attorney verification items and assemble the output**, labeled a draft for attorney review, with the unchecked checklist attached.

## Output Format

Deliver the following, in order, labeled `DRAFT — For Attorney Review — Not Final Discovery Responses`:

1. **Summary** — one paragraph: the discovery served, the client's role, the response deadline (`[deadline verification required]`), and the top scope, privilege, and collection issues.
2. **Gates** — parties, role, forum (`[verify jurisdiction]`), discovery types, response deadline.
3. **Response Tracker** — table: Req ID | Type | Verbatim Text | Bears On (claim/defense) | Objection Candidates | Privilege Flag | Owner | Status.
4. **Objection-Candidate Notes** — per request, the candidates and the prompting feature, framed as questions.
5. **Privilege Candidates** — requests likely to capture privileged/work-product material, routed to `privilege-log-review`.
6. **Collection and Custodian Plan** — custodians, sources, date ranges, and search parameters, with proportionality questions.
7. **RFA Organization** — per RFA, the fact, its basis, and the open questions — no admit/deny.
8. **Response Shells** — per request, the placeholder scaffold for counsel.
9. **Deadlines** — every date as stated, each `[deadline verification required]`, near-term dates surfaced.
10. **Attorney Verification Items** — every placeholder consolidated.
11. **Assumptions** — every assumption made, listed explicitly.

Use `[COUNSEL: ...]` and `[CONFIRM: ...]` throughout. Do not fill gaps with invented content.

## Attorney Verification Checklist

- [ ] Every request served has been captured verbatim, with sub-parts, and none omitted.
- [ ] The response deadline (and any extension) has been confirmed under the governing rules — no deadline in this draft was computed. `[deadline verification required]` `[verify jurisdiction]`
- [ ] The governing discovery rules and any local rules or standing orders have been identified. `[verify jurisdiction]`
- [ ] Objections have been decided by counsel; grounds not asserted have been consciously waived, not overlooked.
- [ ] Relevance, scope, and proportionality positions have been set by counsel, not inferred by this draft.
- [ ] Privilege and work-product calls have been made by counsel, and a privilege log prepared where needed (via `privilege-log-review`).
- [ ] Preservation is in place for all responsive sources (via `legal-hold`), and collection is proportional and defensible.
- [ ] Each interrogatory answer has been verified against source documents and, where required, verified/sworn by the client.
- [ ] Each request for admission has been decided by counsel; the effect of every admission — and of any deemed admission — has been assessed.
- [ ] Compound, vague, or objectionable RFA and interrogatory wording has been addressed by counsel.
- [ ] Confidentiality designations and any protective-order requirements have been applied to the production.
- [ ] No objection was drafted as final, and no admit/deny position was recommended, without attorney decision.
- [ ] All `[COUNSEL: ...]`, `[CONFIRM: ...]`, `[verify jurisdiction]`, and `[deadline verification required]` placeholders have been resolved before the responses are served.
