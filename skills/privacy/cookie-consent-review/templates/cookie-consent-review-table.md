# Cookie Consent Review Table

> Draft legal work product for attorney review. Not legal advice.
> Fill-in structure for the Cookie Consent Review skill — Workflow steps 2-7 and the skill's 9-section Output Format.
> No compliance conclusion, dark-pattern label, or jurisdiction-specific rule is settled here — every legal conclusion is `[ATTORNEY TO CONFIRM]` or `[verify jurisdiction]`.

**Site/app reviewed:** [ ]
**Date of scan/audit:** [ ]
**Stated market footprint:** [ ] `[CONFIRM if unstated]`

## Tracker-vs-Disclosure Table

| Tracker | Vendor | Stated Category | Disclosure Coverage |
|---|---|---|---|
| [ ] | [ ] | [ ] | [named specifically / covered by generic category / not addressed] |

*Flag any "not addressed" tracker as a disclosure gap. Flag any disclosed category with no matching tracker as a possible stale entry.*

## Consent-Banner Mechanics

- **Tracking before choice made?** [Yes / No / Unclear]
- **Choices offered:** [Accept all / Reject all / Customize / Close-dismiss / Other: DESCRIBE]
- **Reject-parity observation:** [reject presented with comparable prominence to accept / not comparable — DESCRIBE]
- **Granularity:** [individual category selection available / all-or-nothing]
- **Pre-checked/default state:** [ ]
- **Compliance conclusion:** none drawn — `[ATTORNEY TO CONFIRM]`

## Consent-Record Facts

- **Logged at choice:** [timestamp / choice made / banner-policy version / identifier used]
- **Storage location:** [ ]
- **Retention period:** [ ]
- **Reconstruction gap identified?** [ ] `[ATTORNEY TO CONFIRM]`

## Dark-Pattern Indicators (Named Neutrally)

| Observed Design Choice | Description | Source |
|---|---|---|
| [ ] | [e.g., "Reject requires more clicks than Accept"] | [ ] |

*Named neutrally as design facts — no "dark pattern" conclusion drawn.*

## CMP/TCF-Framework Presence Note

- **Framework in use:** [ ] [none / CMP name / IAB TCF version, etc.]
- **Configuration facts provided:** [ ]
- **Caveat:** Presence of a framework is a fact, not a compliance signal. `[ATTORNEY TO CONFIRM]`

## Cross-Border Divergence Flags

| Market | Consent Model Question | Flag |
|---|---|---|
| [ ] | [prior-consent vs. opt-out / reject-parity / granularity requirement] | `[verify jurisdiction]` |

## Escalation Items

- [ ] Tracker firing with no disclosure coverage at all
- [ ] Tracking occurs before any choice in a market where prior consent may be required
- [ ] Dark-pattern indicator combination appears to materially disadvantage rejection
- [ ] Consent records cannot be reconstructed for a given user/period
- [ ] Other: [ ]

## Attorney Verification Items

- [ ] Tracker inventory current and complete.
- [ ] Disclosure coverage confirmed adequate under applicable law. `[verify jurisdiction]`
- [ ] Banner mechanics assessed against applicable consent model per market.
- [ ] Consent-record evidentiary adequacy assessed.
- [ ] Every dark-pattern indicator assessed by counsel.
- [ ] CMP/TCF configuration reviewed on its own terms.

## Assumptions

- [ ] List every assumption made in this review.
