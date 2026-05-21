> Shared reference material supporting the AgentCounsel contracts skills, used to help produce draft legal work product for attorney review — not legal advice.

# Market Benchmark Framework

This framework gives a reviewer a disciplined method for recording how a contract term compares to market norms, citing the basis for any benchmark observation, and flagging every unverified benchmark for attorney confirmation.

**AgentCounsel does not supply market data.** This library contains no percentages, no assertions of what terms are "typically" offered, and no claims about what the market "standard" is for any clause. Every benchmark observation in a deliverable must come from a source the attorney can verify — and every such observation is an attorney-verification item until confirmed.

An unverified benchmark is more dangerous than no benchmark. A fabricated or unconfirmed market-data assertion can lead an attorney or client to make a negotiating decision on a false premise. This framework exists to ensure that any benchmark used in a review is clearly sourced, clearly qualified, and clearly flagged for confirmation.

---

## Why Market Benchmarks Are Attorney-Verification Items

Market norms for contract terms vary by:

- **Industry and sector** — what is typical in technology services differs from what is typical in construction, financial services, or life sciences.
- **Transaction type** — MSA terms differ from SaaS subscription terms, which differ from one-time professional services engagements.
- **Transaction size and deal value** — large-enterprise terms differ from mid-market or SMB terms.
- **Geography and governing law** — norms differ across jurisdictions `[verify jurisdiction]`.
- **Time** — what was standard practice several years ago may not reflect current market expectations.
- **Counterparty type** — terms offered by a large platform vendor differ from those offered by a boutique professional services firm.
- **Relative leverage** — "market standard" often means "what the party with more leverage typically gets."

An agent cannot verify any of these variables from a contract document alone. Only the attorney, drawing on active practice experience and current knowledge of the relevant market segment, can assess whether a benchmark observation is accurate for the specific deal.

---

## Permitted Sources for Benchmark Observations

A benchmark observation may only be recorded if it can be attributed to one of the following:

### Source 1: The Client's Practice Profile or Playbook

The client's own standard positions, as provided by the attorney or reflected in the client's supplied template, playbook, or prior agreements. Observations from this source describe what the client's standard is — not what "the market" is. Record as: _"Client's playbook [specify source] provides for [term]. The reviewed contract departs from client's standard in the following way: [description]."_

### Source 2: Attorney-Provided Comparables

Comparable contract terms specifically identified by the supervising attorney or the client as representative of market practice for this type of deal. Record as: _"Attorney-provided comparable [specify, e.g., 'prior agreement with similar vendor supplied by client'] contains [term]. The reviewed contract [matches / departs from] this comparable in the following way: [description]."_

### Source 3: The Counterparty's Own Prior Forms

Where the client has a prior contract with the same counterparty, or has obtained a prior version of the counterparty's standard form, terms from that prior form are a benchmark for what the counterparty has historically offered. Record as: _"Counterparty's prior form [specify source] contained [term]. The reviewed contract [matches / departs from / is more restrictive than] the counterparty's prior form in the following way: [description]."_

### Source 4: Industry Norms Supplied by the Attorney

The attorney identifies specific industry norms applicable to this deal, drawing on active practice knowledge for this sector, transaction type, and deal size. The attorney must supply the norm — the agent records and flags it. Record as: _"Attorney-supplied industry norm for [sector / transaction type]: [description of norm]. Flagged for attorney confirmation."_

---

## Prohibited Assertions

The following assertions must never appear in a deliverable produced using this framework:

- "Market standard is [X]."
- "It is typical for [clause] to be [Y]."
- "[X]% of contracts in this sector include [term]."
- "Most vendors accept [Y] on [term]."
- "Industry practice requires [Z]."
- Any percentage, frequency, or statistical claim about market practice.
- Any assertion about what a counterparty "usually" offers or "would normally" accept.

If a benchmark observation cannot be sourced to one of the four permitted sources above, it must not appear in the deliverable. Record an open item instead: `[ATTORNEY TO CONFIRM: market norm for [clause/term] in [transaction type] — no verified benchmark available]`.

---

## How to Record a Benchmark Observation

Every benchmark observation in a deliverable must follow this structure:

```
Benchmark Observation
Clause / Term:        [name of the clause or issue]
Observed term:        [what the reviewed contract says, quoted or precisely described]
Benchmark source:     [one of the four permitted sources; identify the specific source]
Benchmark position:   [what the benchmark source says about this term]
Deviation:            [how the reviewed contract departs from the benchmark, if at all]
Verification status:  [UNVERIFIED — attorney confirmation required]
                      OR [CONFIRMED by: (attorney / playbook / comparables)]
```

All benchmark observations are marked UNVERIFIED until the supervising attorney confirms them.

---

## Flagging Unverified Benchmarks

Every unverified benchmark in a deliverable must be flagged as an open item. Use the following placeholder form:

`[ATTORNEY TO CONFIRM: benchmark for [clause] — basis is [source]; confirm whether this reflects current market practice for [transaction type / sector / deal size]]`

Do not omit the source basis in the placeholder. A bare `[verify]` tag is not sufficient; the attorney needs to know what assertion is being flagged and what the claimed source is.

---

## Benchmark Observations vs. Risk Ratings

A benchmark observation describes how a term compares to a reference point. A risk rating (High / Medium / Low in the risk matrix) describes the risk to the client. These are distinct assessments:

- A term can depart significantly from a benchmark but pose low risk to the client (e.g., a client-favorable deviation).
- A term can be consistent with a benchmark but still pose meaningful risk to the client (e.g., a term that is "typical" but still creates genuine exposure).

Do not conflate "consistent with market" with "acceptable risk." The risk assessment belongs to the attorney. The benchmark observation is one input to that assessment.

---

## Benchmark Observations in the Risk Matrix

When recording a benchmark observation in the risk matrix (see `skills/contracts/contract-risk-review/templates/contract-risk-matrix.md`), the Attorney Note column is the appropriate place to record the observation and its verification status. Example:

> Attorney Note: _Liability cap formula departs from client playbook standard (12-month fees; playbook calls for 24-month minimum). No external market benchmark available. `[ATTORNEY TO CONFIRM: whether 12-month cap is acceptable for this transaction type and deal value]`_

---

## A Note on "Market Standard" Claims in the Contract Itself

Counterparties sometimes include language in their agreements asserting that a term is "market standard," "industry standard," or "customary." These assertions are counterparty representations — they are not independently verified benchmarks. When such language appears in a reviewed contract, note it as a counterparty claim and flag it for attorney verification: `[ATTORNEY TO CONFIRM: counterparty's "market standard" assertion for [term] — independent verification required]`.
