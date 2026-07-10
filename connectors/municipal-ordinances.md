# Municipal Ordinances

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This connector points at the fragmented landscape of **municipal-code sources** — the official code hosts that cities, towns, and counties use to publish their current ordinances (e.g., Municode, American Legal Publishing, Code Publishing Company, and a municipality's own website), general aggregators that mirror or index municipal codes across many jurisdictions, and the **LOCUS-v1** research corpus behind the `nberk/local_law_explorer` project, a bulk dataset of local-law text assembled for research use. It documents a narrow, **existence-check** surface: whether an ordinance section a draft cites appears to exist, roughly what it says, and where to find the municipality's own current version — never whether that version is the operative, currently-in-force text.

The broader connector contract is in [`README.md`](README.md). See [`state-courts.md`](state-courts.md) for the companion connector covering state-level judiciary and register sources — this connector is local (municipal and county) only, and its coverage is far less uniform than any federal or state source documented elsewhere in this directory.

## 1. Source

- **Publishers:** Vary by municipality. Common official code hosts include Municode (municode.com), American Legal Publishing (amlegal.com), and Code Publishing Company (codepublishing.com), each of which hosts current codes for many municipalities under contract; some municipalities publish their own code directly on the municipal website instead. LOCUS-v1 is a research corpus assembled and distributed by the `nberk/local_law_explorer` project, not an official government publisher.
- **Cost:** Official code hosts are free to browse publicly. LOCUS-v1 access terms follow the project's stated license — see Section 3 below; this is not a free-for-any-use dataset.
- **Coverage:** Extremely uneven. Coverage depends entirely on which host, if any, a given municipality has contracted with, and whether that municipality has kept its hosted code current. Many small or rural municipalities have no searchable online code at all. `[CONFIRM: whether the specific municipality at issue has any online code before relying on a "not found" result]`.
- **Output formats:** HTML for official code hosts; the LOCUS-v1 corpus format is whatever the `nberk/local_law_explorer` project distributes it as `[CONFIRM: current corpus format and access method against the live project]`.
- **Rate limits:** Vary by host; not documented centrally. `[CONFIRM: any host's fair-use guidance before a sustained workflow]`.
- **License of returned content:** Official code text is a public government work, though hosting and formatting layers added by a commercial code publisher may carry their own terms. **LOCUS-v1 is licensed CC-BY-NC-4.0 — non-commercial use only.** See Section 3.

## 2. In scope — what this connector can verify

- **That an ordinance section appears to exist** — that a municipal code, as hosted by an official code host or mirrored by an aggregator, contains a section matching the citation a draft asserts (chapter/title, section number, and a matching heading or subject).
- **Roughly what the ordinance says** — the text as currently hosted, for a first-pass read before the attorney or local counsel confirms it against the municipality's own official code.
- **Where to find the municipality's own current code** — the specific official host or municipal website URL to hand to local counsel for authoritative confirmation.
- **Existence-check pointers via LOCUS-v1** — for research use only (see Section 3), a lead on whether a type of local ordinance (e.g., a short-term-rental ban, a specific zoning use restriction) exists in a given municipality's corpus of local law, to be followed up against an official source — never quoted or relied on as the operative text itself.

What "verify" means here: confirm that an ordinance **appears to exist** at a hosted location matching the citation, and record that **pointer URL** for the deliverable. **This connector does not confirm that the hosted text is the current, operative, legally effective version of the ordinance.** See Section 7.

## 3. Out of scope — what this connector does not cover

A skill must keep its existing placeholder discipline for anything in this list:

- **Current, operative status of any ordinance.** A hosted ordinance may have been amended, repealed, or superseded after the host's last update and before it was viewed. Aggregators and even official code hosts routinely lag the municipality's own effective, currently-in-force code. **Always re-verify against the municipality's own official current code** — the hosted text found through this connector is never the last word.
- **Redistribution or reliance on LOCUS-v1 text.** LOCUS-v1 is licensed **CC-BY-NC-4.0 — non-commercial use only.** It is documented here strictly as an **existence-check pointer** — a research lead that a type of ordinance may exist in a jurisdiction — never as source text to quote, redistribute, or rely on in a deliverable, and never in connection with commercial legal work product without independently clearing rights and re-verifying against an official source. Treat any LOCUS-v1 hit as a reason to go look at the municipality's own code, not as the answer itself.
- **Legal interpretation of any ordinance.** Whether an ordinance applies to a given use, property, or fact pattern is local-counsel and attorney work in every case.
- **Zoning classification, permitted-use determinations, or variance/permit outcomes.** This connector, like the skills it supports, never states whether a use is or is not permitted.
- **Any deadline** — appeal periods, hearing dates, application windows, or grandfathering cutoffs. `[deadline verification required]` in every case; this connector does not compute or confirm dates.
- **State preemption or conflict with state law.** Whether a municipal ordinance is valid, preempted, or superseded by state law is attorney work this connector does not address.
- **Uniform or centralized coverage.** There is no single authoritative index of all US municipal codes. Absence of a hit is common and uninformative — most municipalities have partial or no online presence through any of these hosts.

If a skill needs to verify any of the above, treat the connector as unavailable for that placeholder and retain the existing `[CONFIRM: ...]` and `[verify jurisdiction]` flags.

## 4. Surface — where to hit

### 4a. Official code hosts (primary surface)

- **Municode:** `https://library.municode.com/<state>/<municipality>/codes/code_of_ordinances` (pattern varies by jurisdiction).
- **American Legal Publishing:** `https://codelibrary.amlegal.com/codes/<municipality>/latest/overview` (pattern varies).
- **Code Publishing Company:** `https://<municipality>.municipal.codes/` or a similarly patterned subdomain (varies).
- **Municipality's own site:** many municipalities publish their code directly; search `"<municipality name>" municipal code` or `"<municipality name>" ordinances` if the citation gives no host hint.

Use this surface for: locating the section a draft cites, confirming it appears to exist, and capturing the hosted URL as the pointer for local counsel to confirm.

### 4b. General aggregators

- Third-party legal-research aggregators occasionally mirror or index municipal codes across many jurisdictions. Treat any aggregator hit the same as an official-host hit for existence-check purposes, but note explicitly that aggregators are a further step removed from the municipality and lag official updates even more than a code publisher's own hosted page.

### 4c. LOCUS-v1 / `nberk/local_law_explorer` (existence-check pointer only)

- **Use for:** a research lead on whether a *type* of local ordinance (not a specific already-known citation) exists in a jurisdiction's corpus of local law — useful when the user does not yet have a citation and is asking "does this municipality regulate X at all."
- **Do not use for:** quoting operative ordinance text, redistributing corpus content, or any commercial deliverable without independently re-verifying against the municipality's official code and separately clearing the CC-BY-NC-4.0 license for the intended use.
- `[CONFIRM: current access method and corpus scope against the live `nberk/local_law_explorer` project before relying on it]`.

### 4d. MCP tool surface

When the user's environment includes an MCP server or tool that wraps a municipal-code host or aggregator, prefer it over raw URL fetches. The connector contract is the same: query, record the verified pointer URL, fall back to placeholder if unavailable. **This connector does not configure or install any MCP server** — see `connectors/README.md`.

## 5. Calling pattern from a skill

When a skill's Workflow reaches a municipal-ordinance reference it would otherwise mark `[CONFIRM: ...]` or `[verify jurisdiction]`, and the reference is in scope under Section 2:

1. **Confirm the jurisdiction first.** Never proceed without a confirmed municipality and state — `[verify jurisdiction]` if either is missing or ambiguous (e.g., a common town name shared by several states).
2. **Identify the likely host.** Check whether the municipality is hosted by Municode, American Legal Publishing, Code Publishing, or its own site (4a); fall back to an aggregator (4b) only if no official host is found.
3. **Locate the cited section, or search by topic.** If the draft has a chapter/section citation, browse directly to it. If the draft only describes a topic (e.g., "the short-term-rental ordinance"), search the host's index, or use LOCUS-v1 (4c) as a research lead only — never as the source itself.
4. **Branch on the result:**
   - **Found on an official host:** Record the hosted pointer URL, the section citation, and the date viewed. Replace the placeholder with `[ATTORNEY TO CONFIRM: pointer confirms an ordinance appears hosted at this location as of the date viewed — current, operative status must be re-verified against the municipality's own official code before reliance]`.
   - **Found only via aggregator or LOCUS-v1:** Record the same, but add `[CONFIRM: found via aggregator/research corpus, not the municipality's own official host — re-verify against the official code before reliance; if via LOCUS-v1, existence-check pointer only, CC-BY-NC-4.0, non-commercial use]`.
   - **No match:** Retain `[CONFIRM: not found in any municipal-code host — attorney or local counsel to verify directly with the municipality's clerk or code office]`. Absence is not proof the ordinance does not exist — many municipalities have no searchable online presence.
   - **Out of scope (per Section 3):** Keep the original placeholder. Do not use this connector to conclude an ordinance is current, valid, preempted, or that a use is permitted.
5. **If the connector is unavailable:** retain the original placeholder unchanged. Add `[CONFIRM: not verified — no municipal-code connector available in this session]` so the attorney sees the gap.

## 6. Fallback behavior

| Outcome | Action |
|---|---|
| Found on official host | Record pointer URL + citation + date viewed; mark `[ATTORNEY TO CONFIRM: pointer only — re-verify current/operative status against official code]` |
| Found via aggregator or LOCUS-v1 | Record the same, plus `[CONFIRM: not the official host — re-verify; LOCUS-v1 hits are existence-check pointers only, CC-BY-NC-4.0]` |
| No match | Mark `[CONFIRM: not found — attorney/local counsel to verify directly with the municipality]` |
| Out of scope per Section 3 | Retain the original placeholder; do not query |
| Jurisdiction unconfirmed | `[verify jurisdiction]` before any lookup is attempted |
| Connector unavailable | Retain the original placeholder; add `not verified — no municipal-code connector` note |

## 7. Limits and known failure modes

- **Hosted is not operative.** The single most important limit of this connector: a hosted ordinance can be out of date the moment it is viewed. Municipalities amend, repeal, and re-codify ordinances on their own schedule, and every host in Section 4 lags to some degree. Never present a hosted ordinance as the current, legally operative text without the attorney or local counsel re-verifying against the municipality's own official code or code office.
- **Coverage is radically uneven.** Unlike the federal and state connectors in this directory, there is no baseline expectation of coverage. A "not found" result is common and uninformative for smaller or rural municipalities, and proves nothing about whether the ordinance exists.
- **LOCUS-v1 licensing is a hard limit, not a formality.** CC-BY-NC-4.0 forbids commercial use and requires attribution; this connector documents LOCUS-v1 strictly as a non-commercial, existence-check research pointer. Do not quote its text into any deliverable, and do not treat a corpus hit as confirming anything beyond "worth checking the official code."
- **Same-name jurisdiction confusion.** Many municipality names repeat across states (and even within a state, a "City" and unincorporated county area of the same name can have different codes). Confirm the exact municipality and state before any lookup — `[verify jurisdiction]`.
- **Recodification breaks citations.** Municipalities periodically recodify their entire code, renumbering chapters and sections; an older citation may no longer resolve even though the substance survived under a new number.
- **State preemption is invisible to this connector.** A validly hosted, current-looking ordinance may nonetheless be preempted or invalid under state law; this connector has no way to detect that.

## 8. What this connector does not do

- Does not confirm that a hosted ordinance is the current, operative, legally effective text — only that it appears hosted as of the date viewed.
- Does not interpret any ordinance, determine zoning classification, or state whether a use is permitted.
- Does not compute, confirm, or imply any deadline — every date stays `[deadline verification required]`.
- Does not confirm state-law validity or preemption of any municipal ordinance.
- Does not authorize redistribution or commercial use of LOCUS-v1 content — CC-BY-NC-4.0, existence-check pointer only.

All of those remain attorney- and local-counsel-verification items. The connector closes only the "does an ordinance matching this citation or topic appear to be hosted somewhere, and where" question. Nothing more.
