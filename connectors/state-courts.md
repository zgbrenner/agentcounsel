# State Courts and State Registers

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This connector points at the **category** of state-court and state-register sources — state judiciary portals, state-court opinion databases, the state-court coverage inside aggregators such as [CourtListener](https://www.courtlistener.com), and, where a state publishes one, the state administrative register. It documents the surface a skill can consult to confirm that a **state appellate opinion exists** with a given citation, or that a **state administrative-register document exists**, where the source covers that state — as a fact on the record, for attorney review.

Unlike the federal connectors, this connector is deliberately **generic**: there is no single national system for state courts, coverage differs by state and by source, and **the absence of a result proves nothing.** The broader connector contract is in [`README.md`](README.md). See [`courtlistener.md`](courtlistener.md) for the one aggregator already documented in this library (federal case law plus partial state-supreme-court coverage), and route any good-law / treatment question to `skills/legal-research/negative-treatment-check/SKILL.md` — this connector does not judge whether an authority is still good law.

## 1. Source

- **Publisher:** No single publisher. Sources in this category include:
  - **State judiciary portals** — each state court system publishes opinions and, sometimes, a searchable database on its own website. Formats, coverage depth, and access methods vary by state.
  - **State-court opinion aggregators** — CourtListener and similar open databases carry varying subsets of state case law (see [`courtlistener.md`](courtlistener.md)).
  - **State administrative registers** — where a state publishes an official register or administrative code (the state analogue of the Federal Register / CFR), that publication is the source for state regulatory documents.
- **Cost:** Most state judiciary portals and official registers are free and public; aggregators such as CourtListener are free for read access. Some states route official reporting through paid vendors — treat any paid tier as out of scope for the documented surface.
- **Surface:** Because sources differ by state, this connector does **not** hard-code a national endpoint. It documents how to consult *whatever* source covers the operative state. `[CONFIRM: the specific state source and its access method before relying on it — describe the surface generically rather than assuming a national endpoint exists]`.
- **Coverage:** Uneven by design. Appellate coverage is common for courts of last resort and often for intermediate appellate courts; trial-court coverage is absent in most states. Historical depth and update lag vary widely.
- **License of returned content:** State opinions and official-register documents are public records; a specific aggregator's own metadata may carry its own license. `[CONFIRM: applicable terms for the specific source before redistribution]`.

## 2. In scope — what state sources can verify

Where a source **covers the operative state**, this category supports verifying:

- **That a state appellate opinion exists** — an opinion of a state court of last resort or (where covered) an intermediate appellate court, identified by case name and citation, is on the record in that source.
- **State-court citation metadata** — case name, deciding court, decision date, and the citation form(s) the source records (official reporter and/or regional reporter, and any neutral/public-domain citation the state uses).
- **That a state administrative-register document exists** — where the state publishes an official register or administrative code, confirm that a cited register document or code section is on the record, with its date and citation form.
- **A stable URL or record identifier** — a public link to the opinion or register document to record for attorney review.
- **Reverse lookup** — given a citation or case name, locate the matching opinion in a source that covers the state.

What "verify" means here: confirm that the cited state opinion or register document **exists in the consulted source**, that the **citation form matches** what that source records, and that a **public URL** can be recorded. **Whether the opinion is still good law, whether it binds the operative court, and whether it supports the proposition for which it is cited are not what this connector confirms.** And because coverage is uneven, a confirmation is only ever "found in this source," never "this is the complete or authoritative record." See Sections 3 and 7.

## 3. Out of scope — what state sources do not cover

A skill must keep its existing placeholder discipline for anything in this list:

- **Uneven and incomplete coverage — absence proves nothing.** State coverage varies by state, by court level, and by source. A "not found" result means "not in the source consulted," **never** "the opinion does not exist" or "the citation is wrong." This is the single most important limit of this connector: never treat a negative result as verification of non-existence, and flag partial coverage prominently in any deliverable.
- **Trial-court records in most states.** Most states do not publish trial-court opinions or dockets in a searchable public source; this connector does not reach them.
- **Good-law / treatment judgment.** Whether a state opinion has been reversed, overruled, superseded, questioned, or distinguished is a treatment determination this connector does not make. Route it to `skills/legal-research/negative-treatment-check/SKILL.md` and to attorney review. Existence in a source is not currency.
- **Whether an authority binds the operative forum.** State appellate structure, horizontal and vertical stare decisis, and the weight of intermediate-appellate versus court-of-last-resort authority are attorney determinations; the connector labels the deciding court and date, nothing more.
- **Pinpoint accuracy and parallel-citation completeness.** Neutral, official, and regional citation forms differ by state and era; confirming a case exists is not confirming a pinpoint page or that every parallel citation is captured.
- **Statutes, secondary sources, and non-covered states.** Statutory verification, treatises, and any state whose source is unavailable in the session remain placeholder items.
- **Any deadline.** State appellate deadlines, filing windows, and register comment periods are never computed here; every such date stays `[deadline verification required]`.

If a skill needs any of the above, treat the connector as unavailable for that placeholder and retain the existing `[VERIFY-CITE: ...]` / `[CONFIRM: ...]` flag.

## 4. Surface — where to hit

Because there is no national state-court API, the surface is chosen per state:

### 4a. Aggregator coverage (documented surface)

- **CourtListener** carries partial state coverage — see [`courtlistener.md`](courtlistener.md) for its Search API (`https://www.courtlistener.com/api/rest/v4/search/`), Citation Lookup endpoint, and opinion-page URL pattern. Treat any state result as "partial coverage" per that connector's Section 3.

Use this first when the operative state is one CourtListener covers, because its surface is already documented and its Citation Lookup endpoint parses citation forms robustly.

### 4b. State judiciary portals (generic)

- Each state court system publishes opinions on its own portal, often with a search interface and stable per-opinion URLs. **Do not assume a national endpoint or invent a URL.** Identify the specific state's official opinion source, confirm its coverage window, and record the exact URL it provides. `[CONFIRM: the operative state's official opinion source and its access method]`.

Use this when the aggregator does not cover the state, or to confirm against the official source of record.

### 4c. State administrative registers (generic)

- Where a state publishes an official register or administrative code, consult that publication for state regulatory documents. Formats and access vary; identify the specific state's official register and record the citation and URL it provides. `[CONFIRM: whether the operative state publishes an official register and its access method]`.

### 4d. MCP tool surface

When the user's environment includes an MCP server that wraps a state source or a state-covering aggregator, prefer it over raw fetches. The connector contract is the same: query, record the verified URL and citation form, and — because coverage is uneven — never read a negative result as verification. **This connector does not configure or install any MCP server** — see `connectors/README.md`.

## 5. Calling pattern from a skill

The skills that most often consult this connector are the **legal-research** skills — `skills/legal-research/case-brief/SKILL.md`, `skills/legal-research/authority-synthesis/SKILL.md`, and `skills/legal-research/negative-treatment-check/SKILL.md` — and any skill doing **state-jurisdiction citation verification**. Each consults it to confirm **that a cited state opinion or register document exists** in a covering source and **what citation form it carries, as a fact** — never to conclude that the authority is good law, binds the forum, or supports the proposition.

When a skill's Workflow reaches a state-court citation it would otherwise mark `[VERIFY-CITE: ...]` or `[CONFIRM: ...]` and the citation is in scope under Section 2:

1. **Identify the operative state and a covering source.** Prefer the documented aggregator (4a) when it covers the state; otherwise identify the state's official portal or register (4b/4c). If no source in the session covers the state, treat the connector as unavailable for that placeholder.
2. **Look up the citation.** Resolve the citation or case name against the chosen source. Record the source consulted and its coverage caveat.
3. **Branch on the result:**
   - **Exact match:** Record the opinion/document with the verified URL and the citation form the source records, plus the deciding court and date. Replace the `[VERIFY-CITE: ...]` placeholder with `[ATTORNEY TO CONFIRM: existence and citation form confirmed in <source> (partial state coverage) — good-law status, binding effect, and support for the proposition remain attorney items]`. Route currency to `skills/legal-research/negative-treatment-check/SKILL.md`.
   - **Multiple matches:** Do not pick one. Record the candidates with their citations and URLs and retain a `[VERIFY-CITE: multiple matches — attorney to select]` flag.
   - **No match:** Retain a `[VERIFY-CITE: not found in <source> — coverage is partial; attorney to verify in the official reporter]` flag. **Do not read a negative result as verification that the case does not exist.**
   - **Out of scope (per Section 3):** Keep the original placeholder. Never use this connector to conclude good-law status, binding effect, or any deadline.
4. **If no covering source is available:** retain the original placeholder unchanged. Add `[VERIFY-CITE: not verified — no state-court connector covering this jurisdiction in this session]` so the attorney sees the gap.

## 6. Fallback behavior

| Outcome | Action |
|---|---|
| Single match | Record verified URL + citation form + deciding court + date; mark `[ATTORNEY TO CONFIRM: existence and citation form only (partial coverage) — good-law status via negative-treatment-check]` |
| Multiple matches | List candidates with citations; mark `[VERIFY-CITE: multiple matches — attorney to select]` |
| No match | Mark `[VERIFY-CITE: not found in <source> — partial coverage; verify in the official reporter]`; absence is not proof of non-existence |
| Out of scope per Section 3 (treatment, binding effect, deadline) | Retain the original placeholder; route treatment to `negative-treatment-check`; keep `[deadline verification required]` |
| Connector unavailable / state not covered | Retain the original placeholder; add `not verified — no covering state-court connector` note |

## 7. Limits and known failure modes

- **Coverage is uneven and a negative result is not verification.** This is the governing limitation. Sources differ by state, court level, and era; a "not found" means "not in this source." Always flag the partial-coverage caveat in the deliverable and never let a negative result stand as proof a case does not exist.
- **Currency is separate from existence.** A state opinion existing in a source is not the same as the opinion still being good law. Reversal, overruling, superseding legislation, and later treatment are outside this connector — route to `skills/legal-research/negative-treatment-check/SKILL.md`.
- **Binding effect is attorney work.** Whether a state intermediate-appellate opinion binds a given court, and how it interacts with court-of-last-resort authority, depends on the state's stare decisis rules. The connector labels the deciding court and date only.
- **Citation-form variance.** States use different official, regional, and neutral/public-domain citation forms, and these change over time. A citation that fails in one form may succeed in another; confirm the citation form against the state's official reporter.
- **Trial courts and unpublished opinions.** Most states do not publish trial-court opinions, and unpublished appellate opinions may be absent or carry citation restrictions the connector does not evaluate.
- **Register availability varies.** Not every state publishes an official administrative register, and those that do differ in format, depth, and access. Confirm the specific state's source before relying on it.
- **No deadline is ever computed.** Appellate deadlines, filing windows, and comment periods stay `[deadline verification required]`; this connector does not compute one.

## 8. What this connector does not do

- Does not verify that a state opinion is still good law, has not been reversed or overruled, or remains binding — route to `skills/legal-research/negative-treatment-check/SKILL.md`.
- Does not treat a negative result as proof that a case or document does not exist — coverage is partial and absence proves nothing.
- Does not determine whether an authority binds or persuades the operative forum.
- Does not reach trial-court records in states that do not publish them.
- Does not verify statutes, secondary sources, or any state whose source is unavailable in the session.
- Does not compute, confirm, or imply any deadline — every such date stays `[deadline verification required]`.

All of those remain attorney-verification items. The connector closes the "does this state opinion or register document exist, with this citation, in a source that covers this state" question — and no more, always subject to the partial-coverage caveat.
