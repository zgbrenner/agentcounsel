# Connectors

> Reference material supporting the AgentCounsel skill library, used to help produce draft legal work product for attorney review — not legal advice.

This directory documents **connectors** — external sources a skill can consult to verify the authority placeholders it would otherwise leave for the attorney. Connectors are how AgentCounsel turns "Never invent authority" from a *flag-the-gap* discipline into a *flag-the-gap-and-here-is-how-to-close-it* discipline, without abandoning the rule that an attorney must still verify everything before reliance.

## What a connector is — and is not

A connector is **a documented integration point**, not a runtime component of this library. AgentCounsel is Markdown-only; nothing here makes a network call. A connector doc tells the agent or the lawyer running a skill:

- What the external source is and what it verifies.
- The URL or MCP tool surface to hit.
- What is in scope for the source (and, just as importantly, what is not).
- How to record a successful verification and how to handle "not found," "ambiguous," or "unavailable."

The user's environment supplies the actual connection — an MCP server, a browser tab, a curl command, an HTTP-capable agent tool, or a manual web visit. If no connection is available, the skill falls back to its existing placeholder discipline. **A connector never replaces the Attorney Verification Checklist; it narrows what an attorney still has to do.**

## The connector contract

Every connector doc in this directory follows the same outline:

1. **Source** — what the connector points at (publisher, project, free vs. licensed, rate limits).
2. **In scope** — what kinds of citations the source can verify (jurisdictions, document types, date range).
3. **Out of scope** — what the source does *not* cover. A skill must keep its placeholder behavior for anything out of scope.
4. **Surface** — the MCP tool names (when applicable) and the URL patterns to use, with example queries.
5. **Calling pattern from a skill** — how a skill workflow consults the connector and what to write into the Authorities Cited table or equivalent.
6. **Fallback behavior** — how to record an unavailable connector, an ambiguous match, or a not-found result.
7. **Limits and known failure modes** — coverage lag, ambiguous citation handling, version drift, anything else a reviewer should know.

A connector doc is not a recommendation that any particular external service be used. It records how to integrate *if* the user's environment provides access. The reviewing attorney is the gate.

## How a skill consumes a connector

A skill that has a `[VERIFY-CITE: ...]`, `[CONFIRM: ...]`, or `[citation needed]` placeholder consults the relevant connector doc — typically named in the skill's Workflow or Legal Safety Rules section — and:

1. Attempts to resolve the placeholder against the connector's surface.
2. **If resolved:** records the verified URL or stable identifier in the Authorities Cited table (or equivalent), keeps the `[ATTORNEY TO CONFIRM]` flag, and notes the source as the connector.
3. **If ambiguous or not found:** retains the placeholder and adds a more specific note (`not found in <connector>` / `multiple matches in <connector>`), escalating to attorney verification.
4. **If the connector is unavailable:** retains the original placeholder. The skill's discipline is unchanged from the no-connector path.

A connector verification is never sufficient on its own. Every verified authority remains an attorney-verification item — the citation is real, but whether it supports the proposition for which it is cited is still attorney work.

## Available connectors

| Connector | Source | Coverage | License |
|---|---|---|---|
| [courtlistener.md](courtlistener.md) | [Free Law Project — CourtListener](https://www.courtlistener.com) | US federal case law (SCOTUS, federal appellate, federal district); selective state supreme court coverage | Free, no API key required for many endpoints (5,000 req/hr) |
| [federal-register.md](federal-register.md) | [Federal Register](https://www.federalregister.gov) (NARA) | US Federal Register documents since 1994 — final rules, proposed rules, notices, presidential documents; pre-publication Public Inspection | Free, no API key, fully public |
| [ecfr.md](ecfr.md) | [eCFR](https://www.ecfr.gov) (NARA / GPO) | Currently codified Code of Federal Regulations and date-versioned historical snapshots back to roughly 2017 | Free, no API key, fully public |
| [sec-edgar.md](sec-edgar.md) | [SEC EDGAR](https://www.sec.gov/edgar) (U.S. Securities and Exchange Commission) | SEC filings — full-text search of filings since roughly 2001; filing metadata, accession numbers, and as-filed documents back to EDGAR's early-1990s phase-in | Free, no API key; fair-access guidance (declared User-Agent, modest request rate) |
| [pacer-recap.md](pacer-recap.md) | [PACER](https://pacer.uscourts.gov) (Administrative Office of the U.S. Courts) and the [RECAP Archive](https://www.courtlistener.com/recap/) (Free Law Project) | Federal district, appellate, and bankruptcy docket entries and filings that are in RECAP — existence, docket numbers, and recorded filed dates (never a deadline) | PACER paywalled (account + per-page fees); RECAP free read access, no API key required to begin |
| [uspto.md](uspto.md) | [USPTO](https://www.uspto.gov) (U.S. Patent and Trademark Office) | US patent and published-application existence and status metadata; US trademark registration/application existence and prosecution-status metadata; recorded assignments (never validity, claim scope, FTO, or registrability) | Free; some APIs (e.g., TSDR) require a free USPTO-issued API key |
| [state-courts.md](state-courts.md) | State judiciary portals, state-court opinion aggregators (incl. [CourtListener](https://www.courtlistener.com)), and state administrative registers | Existence and citation metadata of state appellate opinions and state register documents where the source covers that state — partial and uneven, so absence proves nothing | Mostly free and public; varies by state and source |
| [reporters-and-courts.md](reporters-and-courts.md) | [Free Law Project](https://free.law) — reporters-db and courts-db | Existence of case-law reporter abbreviations and court names/abbreviations (US-centric) — not existence of the cited case itself | Free, open data; BSD-2-Clause |
| [congress-gov.md](congress-gov.md) | [Congress.gov](https://www.congress.gov) (Library of Congress) and [GovInfo](https://www.govinfo.gov) (GPO) | Federal bill and resolution existence, status, committee actions, text versions, and public-law numbers from the 93rd Congress (1973) forward | Free; Congress.gov public site needs no key, GovInfo API requires a free key |
| [municipal-ordinances.md](municipal-ordinances.md) | Official municipal code hosts (e.g. Municode, American Legal Publishing, Code Publishing), general aggregators, and the LOCUS-v1 research corpus (`nberk/local_law_explorer`) | Existence-check pointers for local ordinances — radically uneven coverage, no baseline expectation; always re-verify against the municipality's own official code | Official hosts free and public; LOCUS-v1 is CC-BY-NC-4.0, non-commercial existence-check use only |

This list grows as additional connectors are added. Future candidates include statutory and legislative sources, additional federal and state regulatory feeds, and foreign or international tribunals.

## What this directory does not do

- **No runtime code.** Connector docs are Markdown. Nothing under `connectors/` is invoked by the library itself; the library has no runtime.
- **No recommendation of paid services.** Where a connector has a paid tier, the doc records what is available on the free tier and notes the paid tier as out of scope for the documented surface.
- **No replacement for attorney verification.** A verified citation is still an item on the Attorney Verification Checklist. The connector closes the "does this case exist with this citation" question; the attorney still owns "does this case stand for the proposition we are using it for, under the current law of the operative jurisdiction."

## Adding a new connector

1. Create `connectors/<connector-name>.md` following the contract above.
2. Add the connector row to the table in this README.
3. Update each skill that should consult the new connector — add a verification step in Workflow, a citation-source bullet in Legal Safety Rules, and (where the Output Format has an Authorities Cited table) a verification-source column.
4. Add a `connectors/<connector-name>.md` reference to the relevant entry in `SKILLS_INDEX.md`.
5. Note the addition under "Unreleased" in `CHANGELOG.md`.
6. Run the validators: `python scripts/sync_plugin_skills.py --check`, `python scripts/validate_repo.py`, `python scripts/check_evals.py`, `python scripts/run_evals.py --strict --quiet`.
