# Reporters and Courts (reporters-db / courts-db)

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This connector points at two companion open-source reference datasets
maintained by the Free Law Project: **reporters-db**, a structured catalog of
case-law reporter abbreviations and their publishers, and **courts-db**, a
structured catalog of federal and state court names and abbreviations. It
documents the lookup surface a skill can consult to confirm that a **reporter
abbreviation** used in a citation, or a **court name or abbreviation** used in
a case citation, actually corresponds to a real, catalogued reporter or
court — a narrow but useful check against exactly the kind of well-formed,
entirely fabricated citation described in
`skills/legal-research/references/citation-type-taxonomy.md`.

The broader connector contract is in [`README.md`](README.md). See
[`courtlistener.md`](courtlistener.md) for the companion connector that
verifies whether a *case itself* exists — this connector verifies only
whether the *reporter or court referenced in a citation string* is a real,
catalogued one, which is a smaller and different question.

## 1. Source

- **Publisher:** Free Law Project (the same organization that publishes
  CourtListener and the eyecite citation-extraction library).
- **Cost:** Free. Both datasets are openly published data files; no API key
  or authentication is required to consult them.
- **Surfaces:** The datasets are distributed as structured data (JSON) within
  the `reporters-db` and `courts-db` open-source projects, and are also used
  internally by `eyecite` and by CourtListener's own citation-matching
  pipeline. `[CONFIRM: current distribution format and repository location
  against the live projects before integrating in a long-lived tool]`.
- **Coverage:** reporters-db catalogs case-law reporters used in the United
  States (federal and state, historical and current, including many regional
  and topical reporters); courts-db catalogs federal courts and state courts
  and their common abbreviations. Coverage is **US-centric** — see Section 3.
- **Output formats:** Structured data (JSON) keyed by reporter or court
  abbreviation, with associated names, jurisdictions, and (for reporters)
  publication date ranges where known.
- **Rate limits:** Not applicable in the same sense as a live API — these are
  data lookups, whether performed via a local copy of the dataset, a package
  that bundles it (such as `eyecite`), or an MCP tool that wraps it.
  `[CONFIRM: rate or usage guidance if consulted through a hosted service
  rather than a local dataset]`.
- **License of returned content:** Both `reporters-db` and `courts-db` are
  published under BSD-2-Clause by the Free Law Project. This connector
  documents them as a verification resource; it does not redistribute the
  datasets themselves.

## 2. In scope — what reporters-db / courts-db can verify

- **Whether a reporter abbreviation exists** — whether a string like "F.3d"
  or "Cal. App. 4th" (or a less common regional or topical reporter
  abbreviation) corresponds to a catalogued reporter, and what full name and
  publisher it maps to.
- **Whether a court name or abbreviation exists** — whether a string like
  "9th Cir." or "S.D.N.Y." (or a state trial or appellate court's
  abbreviation) corresponds to a catalogued court, and what full court name
  and jurisdiction it maps to.
- **Plausible reporter/court pairing** — whether the court a citation
  attributes a decision to is a court that plausibly reports in the cited
  reporter (for example, flagging a case cited to a state-specific reporter
  but attributed to a federal circuit court).
- **Historical reporter identity** — whether an abbreviation corresponds to a
  reporter that existed during the cited year, where the dataset records a
  publication date range, which helps catch an anachronistic citation.

What "verify" means here: confirm that the **abbreviation string itself**
names a real, catalogued reporter or court, and retrieve the full name,
jurisdiction, and (where available) publication date range associated with
it. **This is not confirmation that the cited case exists, that the citation
is complete, or that the case says what the draft claims.** See Section 7.

## 3. Out of scope — what reporters-db / courts-db do not cover

A skill must keep its existing placeholder discipline for anything in this
list:

- **Whether a cited case actually exists.** A real reporter abbreviation and
  a real court do not confirm that a specific case at a specific volume and
  page exists — see [`courtlistener.md`](courtlistener.md) and
  [`state-courts.md`](state-courts.md) for existence checks on the case
  itself.
- **Whether a citation is complete or correctly formatted beyond the
  reporter/court strings** — party names, pin cites, and parenthetical dates
  are not checked by this connector.
- **Non-US reporters and courts.** Coverage is US-centric. A citation to a
  foreign or international tribunal, or a foreign law report, is out of scope
  `[verify jurisdiction]` — treat the connector as unavailable for that
  citation and retain the existing placeholder.
- **Very new, very obscure, or unofficial reporters.** A reporter or court
  not yet catalogued is not proof that it does not exist — see Section 7.
- **Currency of a court's name or jurisdiction.** Courts are occasionally
  renamed, merged, or restructured; the dataset may lag such changes.
- **Whether the citation supports the proposition it is attached to, or
  whether the underlying case is good law.** That is attorney work in every
  case, regardless of what this connector confirms.

If a skill needs to verify any of the above, treat the connector as
unavailable for that placeholder and retain the existing `[CONFIRM: ...]`
flag.

## 4. Surface — where to hit

### 4a. Local dataset lookup

- **Pattern:** Consult a local or bundled copy of the `reporters-db` or
  `courts-db` JSON data (for example, as bundled inside an installed copy of
  `eyecite`, which depends on both datasets) and look up the abbreviation
  string as a dictionary key.
- **Returns:** The full reporter or court name, jurisdiction, and — for
  reporters — any recorded publication date range and variant abbreviations.

Use this for: environments where a copy of the dataset is available as a
file or as a dependency of an installed citation tool.

### 4b. Public repository browse

- **Pattern:** Browse the `reporters-db` and `courts-db` source repositories
  directly (Free Law Project's public GitHub organization) to inspect the
  data files or search their contents.
- **Returns:** The same structured data as 4a, viewed directly rather than
  through a package dependency.

Use this for: a one-off manual lookup, or confirming the dataset's current
contents when no local copy is available.

### 4c. Via eyecite (indirect)

- **Pattern:** Where an environment has `eyecite` available (see
  `skills/legal-research/references/citation-type-taxonomy.md` for the
  citation-type classification eyecite is drawn from), running its citation
  extraction over a text will resolve recognized reporter and court
  abbreviations as a side effect of parsing — a citation eyecite classifies
  as a well-formed `FullCaseCitation` with a resolved reporter is, by
  construction, one whose reporter string matched `reporters-db`.
- **Returns:** Parsed citation objects with resolved reporter and (where
  determinable) court metadata; an unresolved or ambiguous reporter string
  surfaces as a parsing failure or an unresolved match rather than a clean
  result.

Use this for: environments already running `eyecite` for citation
extraction, where a reporter/court check can be read off the parse results
rather than performed as a separate lookup.

### 4d. MCP tool surface

When the user's environment includes an MCP server or tool that wraps
`reporters-db` / `courts-db` (directly or via `eyecite`), prefer it over a
manual dataset lookup. The connector contract is the same: query, record the
resolved reporter/court name and jurisdiction, fall back to placeholder if
unavailable. **This connector does not configure or install any MCP
server** — see `connectors/README.md`.

## 5. Calling pattern from a skill

The skills that most often consult this connector are the citation-focused
legal-methodology skills —
`skills/legal-methodology/citation-integrity-check/SKILL.md` and
`skills/legal-methodology/source-validation/SKILL.md` — and the
legal-research skills that assemble or check case citations, such as
`skills/legal-research/legal-research-memo/SKILL.md`,
`skills/legal-research/case-brief/SKILL.md`, and
`skills/legal-research/authority-synthesis/SKILL.md`.

When a skill's Workflow reaches a full case citation it would otherwise mark
`[CONFIRM: ...]` and the reference is in scope under Section 2:

1. **Classify the citation type first.** Use
   `skills/legal-research/references/citation-type-taxonomy.md` to confirm
   this is a full case citation (or a short form resolvable to one) before
   attempting a reporter/court lookup — short forms, supras, and `Id.`
   citations should be resolved to their antecedent full citation first.
2. **Extract the reporter and court strings** from the citation as written.
3. **Look up each string** (4a-4d) against the catalogued reporters and
   courts.
4. **Branch on the result:**
   - **Both resolve, and the pairing is plausible:** Record the resolved
     reporter name, court name, and jurisdiction alongside the citation, and
     replace the reporter/court portion of the `[CONFIRM: ...]` placeholder
     with `[ATTORNEY TO CONFIRM: reporter and court abbreviations confirmed
     against reporters-db/courts-db — existence of the specific case, pin
     cite accuracy, and current legal status remain attorney items]`.
   - **One or both do not resolve:** Retain a `[CONFIRM: reporter/court
     abbreviation not found in reporters-db/courts-db — attorney to verify
     independently; absence may reflect an obscure, foreign, or miscatalogued
     source rather than a fabricated citation]` flag. Do not conclude the
     citation is fabricated from a lookup miss alone.
   - **Pairing is implausible** (e.g., a court attributed to a reporter it
     would not plausibly publish in): Flag prominently as a hallucination
     risk indicator per
     `skills/legal-research/references/citation-type-taxonomy.md`, and
     escalate to attorney review rather than silently correcting it.
   - **Out of scope (per Section 3):** Keep the original placeholder. Do not
     use this connector to conclude a case exists, is current, or supports
     the cited proposition.
5. **If the connector is unavailable:** retain the original placeholder.
   Add `[CONFIRM: not verified — no reporters-db/courts-db lookup available
   in this session]` so the attorney sees the gap.

## 6. Fallback behavior

| Outcome | Action |
|---|---|
| Reporter and court both resolve, pairing plausible | Record resolved names and jurisdiction; mark `[ATTORNEY TO CONFIRM: reporter/court confirmed — case existence and legal status remain attorney items]` |
| Reporter or court does not resolve | Mark `[CONFIRM: abbreviation not found in reporters-db/courts-db — attorney to verify]`; absence is not proof of fabrication |
| Pairing implausible (mismatched court/reporter) | Flag as a hallucination risk indicator; escalate to attorney review |
| Out of scope per Section 3 (non-US, case existence, currency) | Retain the original placeholder; do not query |
| Connector unavailable | Retain the original placeholder; add `not verified — no reporters-db/courts-db lookup` note |

## 7. Limits and known failure modes

- **Existence of a reporter is not existence of a case.** Confirming "F.3d"
  is a real reporter says nothing about whether the specific volume and page
  cited actually contains the case named. This connector answers a narrower
  question than [`courtlistener.md`](courtlistener.md) or
  [`state-courts.md`](state-courts.md), and should typically be used
  alongside one of them, not instead of them.
- **US-centric coverage.** Foreign reporters, foreign courts, and
  international tribunals are largely or entirely outside these datasets'
  scope; a "not found" result for a non-US citation is expected and is not a
  hallucination signal.
- **Dataset lag.** Newly created reporters or courts, or newly renamed or
  restructured courts, may not yet be catalogued. A miss on a very recent or
  very obscure source should be treated as inconclusive, not as evidence of
  fabrication.
- **Abbreviation variants and ambiguity.** Some reporter abbreviations are
  used inconsistently across style guides or jurisdictions (the same short
  string can map to more than one reporter depending on context); resolve
  ambiguity by cross-checking the surrounding citation's jurisdiction, not by
  guessing.
- **No text-of-the-case content.** These datasets contain metadata about
  reporters and courts only — no case text, no holdings, no docket
  information. They cannot confirm anything about what a case says.
- **Indirect exposure via eyecite.** Where this connector is consulted
  through `eyecite`'s parsing rather than a direct dataset lookup, a citation
  that fails to parse cleanly is not necessarily a fabricated citation — it
  may simply be a citation form eyecite's tokenizer does not recognize.

## 8. What this connector does not do

- Does not confirm that a cited case exists, that a pin cite is accurate, or
  that the case is current, good law, or correctly applied.
- Does not compute, confirm, or imply any filing or briefing deadline.
- Does not cover non-US reporters, courts, or tribunals.
- Does not verify statutory, regulatory, or law-journal citations — see
  `skills/legal-research/references/citation-type-taxonomy.md` for those
  citation forms' separate verification needs.

All of those remain attorney-verification items. The connector closes the
"does this reporter or court abbreviation correspond to a real, catalogued
reporter or court" question. Nothing more.
