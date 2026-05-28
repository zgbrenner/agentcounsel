# Fictional Quality-Layer Example: Demand Letter Hallucination Red-Team

This example is fictional and illustrative. It uses no real client facts and
no legal citations. It shows how `hallucination-red-team` can mark a draft as
not ready for use when unsupported legal claims appear. Attorney review
remains required.

## Scenario

A fictional draft demand letter for North Pier Design Studio asserts breach of
a services contract against a fictional counterparty. The draft included legal
claims generated without supplied authority.

## Red-Team Findings

Status: Not ready for use. Not ready for attorney review until unsupported
claims are revised or sourced.

| Item | Classification | Source status | Risk |
|---|---|---|---|
| "The counterparty missed the March 4 milestone." | Factual claim | Source-supported by project timeline supplied by user | Attorney should confirm timeline and any extensions. |
| "The agreement required payment within 15 days of invoice." | Factual/contract claim | Source-supported by section 5 of the supplied agreement | Attorney should confirm invoice date and any waiver facts. |
| "State law entitles our client to treble damages." | Legal claim | Unsupported | High hallucination risk. No authority supplied. |
| "A court will award fees." | Legal claim | Unsupported and overcertain | Outcome prediction without authority or attorney judgment. |
| "The counterparty acted in bad faith." | Mixed factual/legal characterization | Source-mentioned but insufficient | Requires attorney review and factual support. |

## Required Safer Revision

Draft legal work product for attorney review. Not legal advice.

Based on the supplied project timeline, the counterparty appears to have
missed the March 4 milestone. Based on section 5 of the supplied agreement,
payment appears due within 15 days of invoice, subject to attorney review of
the full agreement, invoice history, amendments, waivers, and applicable law.

The draft should not claim treble damages, fee entitlement, bad faith, or a
likely court outcome unless the supervising attorney supplies and verifies the
supporting authority and factual basis.

## Attorney Follow-Up

- Verify governing law and venue.
- Confirm payment and cure deadlines.
- Confirm available remedies under the contract and current law.
- Decide whether the tone should remain business-facing or become
  litigation-facing.
