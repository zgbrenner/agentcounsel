> Shared reference material supporting the AgentCounsel contracts skills, used to help produce draft legal work product for attorney review — not legal advice.

# Market-Standard Baselines (Open Standard Agreements)

This reference explains how a reviewing skill may use a handful of publicly
published, open standard commercial agreements as a **comparison baseline**
when reviewing a contract — and, just as importantly, the safety rule that
keeps that comparison from turning into a legal conclusion it cannot support.

This reference supplements, and does not replace,
`skills/contracts/references/market-benchmark-framework.md`. That framework
governs every benchmark observation in AgentCounsel and is stricter than this
document in one respect: it treats "market standard" claims as prohibited
unless sourced to one of four permitted sources (client playbook,
attorney-provided comparables, counterparty's prior form, or an
attorney-supplied industry norm). A published open standard agreement is a
close cousin of an attorney-provided comparable — it is a specific, named,
inspectable document, not a vague assertion about "the market" — but it is
still only one reference point among many possible market positions, and a
divergence from it is still, at most, a labeled legal inference for the
attorney to weigh.

**Attribution.** The descriptions of oneNDA, Bonterms, and Common Paper below
are written independently in AgentCounsel's own words. Each project's
published template text is separately licensed CC-BY-4.0 by its respective
publisher; this reference does not reproduce that template text.

---

## What Each Standard Covers

### oneNDA

oneNDA is a single, freely available standard-form mutual non-disclosure
agreement developed by a cross-industry legal-community initiative, intended
to replace bespoke NDA drafting and negotiation with one widely adopted
template. It is narrow by design — it covers only confidentiality and does
not attempt to be a general commercial agreement — which makes it a
particularly clean baseline for the `nda-review` skill specifically: a
reviewed NDA's structure (definition of confidential information, permitted
use, term, return/destruction, remedies) can be compared against a single,
named, publicly inspectable reference point rather than a vague sense of
"typical" NDA terms.

### Bonterms

Bonterms is a nonprofit initiative that publishes a family of standardized
commercial contract templates — including cloud/SaaS terms, mutual NDAs, and
data processing terms — built with input from technology-company and law-firm
contributors, designed to be adopted largely as-is or with a companion
cover-page of deal-specific variables. Because Bonterms spans multiple
document types, it is a useful baseline across several contracts skills, not
only NDA review — for example, comparing a SaaS agreement's liability,
termination, or data-handling terms against the Bonterms Cloud Terms
structure.

### Common Paper

Common Paper is an initiative that publishes standardized, modular commercial
agreement templates (including a cloud service agreement, mutual NDA, and
data processing addendum) designed around a "parameters" model — a short
cover sheet capturing the deal-specific variables while the underlying legal
text stays standard and unmodified — with the stated goal of reducing
negotiation cycles for common commercial deals. Its modular structure makes
it a useful baseline for confirming whether a reviewed contract separates
deal-specific variables from boilerplate in a way that would make future
negotiations faster, in addition to substantive clause comparison.

---

## How to Phrase a Baseline-Comparison Finding

When a reviewing skill compares a reviewed contract against one of these
open standards, follow the recording structure from
`skills/contracts/references/market-benchmark-framework.md` and identify the
open standard as the benchmark source:

```
Benchmark Observation
Clause / Term:        [name of the clause or issue]
Observed term:        [what the reviewed contract says, quoted or precisely described]
Benchmark source:     Open standard agreement — [oneNDA / Bonterms / Common Paper], [document name/version if known]
Benchmark position:   [what the open standard's published template provides for this term, in general terms]
Deviation:            [how the reviewed contract is more restrictive, more permissive, or structurally different, and for which party]
Verification status:  UNVERIFIED — attorney confirmation required
```

Frame the deviation itself using the controlled vocabulary from the market
benchmark framework — most often **Aggressive** (a familiar construction
drafted notably toward one party, relative to the open-standard baseline) or
**Unusual** (a construction that departs from the open standard's approach in
a way not commonly seen). Never state the deviation as "non-compliant,"
"incorrect," or "a defect" — an open standard is one available template, not
a rule the reviewed contract must follow.

Every baseline-comparison finding is flagged, using the same placeholder
convention as the market benchmark framework:

`[ATTORNEY TO CONFIRM: reviewed contract's [clause] is more [restrictive/unusual] than the [oneNDA / Bonterms / Common Paper] baseline — confirm whether this divergence matters for this deal]`

---

## The Safety Rule

**Baseline divergence is a discussion point for the attorney, not a defect.**

A finding that a reviewed contract's liability cap, termination right, or
confidentiality term is more restrictive or differently structured than the
corresponding open-standard baseline is exactly that — a factual comparison
between two specific, named documents. It is never:

- A statement that the reviewed contract is non-compliant, unenforceable, or
  legally deficient.
- A statement that the open standard is "what the market requires" or "what
  a court would expect."
- A substitute for the client's own playbook, an attorney-supplied industry
  norm, or a counterparty's prior form when those are available — where a
  playbook or comparable exists, benchmark against it first and treat the
  open-standard comparison as a secondary, supporting reference.
- A basis for a Common / Aggressive / Unusual characterization used
  anywhere else in the deliverable without restating the open-standard
  source and the UNVERIFIED flag.

An open standard is one widely circulated template published by one
organization. A different negotiator, industry segment, or deal size may
reasonably expect different terms. Only the attorney can decide how much
weight, if any, a specific baseline divergence deserves for this client, in
this deal.

---

## Reviewer Notes

- Use an open-standard baseline comparison only where the reviewed document
  is a plausible match for the standard's subject matter (e.g., oneNDA for a
  stand-alone mutual NDA; Bonterms or Common Paper for a SaaS/cloud
  agreement or a DPA).
- If the reviewed contract's document type does not correspond to any
  published open standard, say so rather than forcing a comparison —
  `[ATTORNEY TO CONFIRM: no open-standard baseline available for this
  document type]`.
- See `skills/contracts/references/market-benchmark-framework.md` for the
  full benchmarking discipline, the controlled vocabulary, and the
  prohibited-assertions list that also governs baseline comparisons made
  under this reference.
