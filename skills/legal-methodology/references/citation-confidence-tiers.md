> Shared reference material supporting the AgentCounsel legal-research and legal-methodology skills, used to help produce draft legal work product for attorney review — not legal advice.

# Citation Confidence Tiers

`skills/legal-research/references/citation-type-taxonomy.md` classifies what
*kind* of citation a passage is — full case citation, short form, statutory,
regulation, and so on. This reference answers a different question: for a
citation of any of those types, how verified is it *right now, in this
session*? A full case citation and a statutory citation are classified the
same way here if they were checked the same way. Classify type first, then
classify confidence — the two axes are independent and a skill needs both
before deciding what a citation may say in a deliverable.

The tiers below are a ladder, not a menu. A citation starts wherever the
session's evidence actually places it and may move up the ladder only when
better evidence is obtained — never down by assumption, and never up by
restating the same unverified fact more confidently.

---

## How Skills Use This File

`skills/legal-methodology/citation-integrity-check/SKILL.md` and
`skills/legal-methodology/source-validation/SKILL.md` assign a confidence
tier to each citation after classifying its type, and use the tier to decide
what may survive into the deliverable and what must remain a placeholder. The
`connectors/` directory is what typically moves a citation from Tier 3 to
Tier 1 — each connector doc records which authority types it can confirm.
Legal-research skills that assemble authority-heavy drafts, and the review
panels in `review-panels/`, can also consult this file when deciding whether
a citation is ready to appear in an Authorities Cited table or must remain
flagged.

---

## Tier 1 — Connector-verified

**What qualifies:** The citation's existence has been checked against a
documented connector in `connectors/` and the connector returned a match —
not a plausible-looking result, an actual retrieved record with a URL,
docket number, accession number, or equivalent stable identifier. Name the
connector that did the checking; which connector applies depends on the
authority type — case law and dockets through `connectors/courtlistener.md`,
`connectors/pacer-recap.md`, or `connectors/state-courts.md`; codified
federal regulations through `connectors/ecfr.md`; Federal Register
rulemakings through `connectors/federal-register.md`; SEC filings through
`connectors/sec-edgar.md`; patents, applications, and trademarks through
`connectors/uspto.md`; reporter and court abbreviations through
`connectors/reporters-and-courts.md`.

**How to label it:** Record the connector name and the retrieved identifier
or URL alongside the citation, then carry forward the connector's own
`[ATTORNEY TO CONFIRM: ...]` language rather than inventing new phrasing —
each connector doc specifies the exact flag its verified outcome leaves
behind.

**What the attorney must still do:** A Tier 1 result confirms **existence**
only — that the cited thing is really there under that identifier. It never
confirms holding, current legal effect, binding or persuasive weight,
whether the authority actually supports the proposition it is cited for, or
(for a regulation or bill) whether it is presently operative rather than
stayed, superseded, or withdrawn. Every one of those remains an attorney
task regardless of the tier.

## Tier 2 — Secondary-source-verified

**What qualifies:** The citation appears in a document the user provided in
this session, or in a reputable secondary source the user supplied or that
was retrieved and read in this session (a treatise excerpt, a court's own
docket page viewed directly, a law-firm client alert quoting the authority).
No connector lookup was performed, but the citation was actually seen in
context rather than recalled — existence is *likely* on that basis, not
confirmed.

**How to label it:** State plainly where the citation was seen (the document
name, section, or source) and mark it something like `[VERIFY: seen in
<source> — existence not connector-confirmed]`, so the deliverable does not
read as more certain than Tier 1.

**What the attorney must still do:** Confirm existence independently — a
secondary source can misquote a citation or itself rely on an error — before
using it as a Tier 1 item, in addition to everything a Tier 1 result still
leaves open (holding, currency, relevance, applicability).

## Tier 3 — Model-knowledge only

**What qualifies:** The citation is not traceable to anything provided or
retrieved in this session — it reflects only the model's background
training. This is the default tier for any authority the agent "recalls"
rather than looked up, and it is the tier every citation-type-taxonomy entry
warns can look entirely well-formed while being unverified.

**How to label it:** Every Tier 3 citation must carry a visible `[VERIFY:
...]` placeholder naming what needs to be checked (existence, the specific
proposition, the pin cite). It may not appear in a deliverable as if it were
settled — the placeholder is not optional formatting, it is the only thing
distinguishing a Tier 3 citation from an invented one.

**What the attorney must still do:** Independently locate and confirm the
citation exists before relying on it at all. A Tier 3 citation may not
survive into a final deliverable unless it is upgraded to Tier 1 or Tier 2
with a documented verification step, or it is left as a visible placeholder
for the attorney to resolve. Do not resolve it by restating it more
confidently on a second pass — repetition is not verification.

## Tier 4 — Unresolvable

**What qualifies:** A connector was consulted and returned no match, no
connector or secondary source is available to check the citation at all, or
the citation is too fragmentary (an unknown/partial citation type, per the
taxonomy) to check against anything.

**How to label it:** Do not leave the original citation text standing.
Replace it with a placeholder that describes the *authority still needed* —
what proposition it must support, what jurisdiction and rough subject
matter, and why it could not be resolved (`not found`, `no connector
available`, `fragment insufficient to identify`) — so the attorney has a
concrete research task rather than a dangling, unverifiable string.

**What the attorney must still do:** Supply or locate the actual authority
from scratch. Nothing about a Tier 4 item can be salvaged by the agent; it
is a research gap, not a citation to double-check.

---

## Tier Summary

| Tier | Basis | Deliverable label | Attorney still confirms |
|---|---|---|---|
| 1 — Connector-verified | Documented connector returned a match | Connector name + retrieved identifier/URL + connector's own attorney-confirm flag | Holding, currency, binding/persuasive weight, relevance to the proposition, operative status |
| 2 — Secondary-source-verified | Seen in a user-provided document or reputable secondary source | Source named; `[VERIFY: seen in <source> — existence not connector-confirmed]` | Existence (independently), plus everything Tier 1 leaves open |
| 3 — Model-knowledge only | Model background knowledge, nothing retrieved this session | `[VERIFY: ...]` describing what must be checked; never stated as settled | Existence, from scratch, before any reliance |
| 4 — Unresolvable | No match, no source, or an unresolvable fragment | Placeholder describing the authority still needed, not the original text | Locating the authority entirely |

---

## Reviewer Notes

- Tier assignment is orthogonal to citation type: a full case citation and a
  regulation citation can both sit at Tier 3 if neither was checked, and both
  can reach Tier 1 through their respective connectors. Classify type first
  with `skills/legal-research/references/citation-type-taxonomy.md`, then
  assign the tier.
- A short-form, supra, or `Id.` citation inherits no tier of its own — its
  tier is the tier of the antecedent full citation it resolves to. An
  unresolved antecedent is a Tier 4 item on its own terms.
- Never treat a Tier 1 result as resolving anything beyond existence. The
  single most common overclaiming error in citation handling is quietly
  letting "the case exists" stand in for "the case says what the draft
  claims" — those are different findings, and only the second is ever
  attorney work, never the agent's to decide.
- Moving a citation up a tier requires new evidence (a connector hit, a
  supplied document), not a more confident restatement. If in doubt about
  which tier applies, assign the lower one.

<!-- Attribution: the tiering concept here is independently written, inspired by the verification-tiering idea in discover-legal/BigLaw and the provenance-tagging approach in anthropics/claude-for-legal, both Apache-2.0. -->
