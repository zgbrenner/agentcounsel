# Launch Review — Consumer Mobile App (US + EU)

> **Draft for attorney review. Not legal advice.** This is draft attorney work product. The skill produces an issues register and a Go / Hold / Conditions framing for attorney sign-off — it does **not** clear the product to ship.

## 1. Summary

- **Product:** Consumer mobile app launching in the United States and the European Union.
- **User population:** Teenagers (minors) — sensitive population.
- **Data collected:** Location data, device identifiers — sensitive data categories.
- **AI feature:** Personalized recommendations powered by a third-party model provider.
- **Marketing claim:** "Safest option for families."
- **Third-party dependencies:** Two SDKs; one open-source library under a copyleft license.
- **Launch date:** Four weeks away — **flagged explicitly**, not used to compress analysis.

## 2. Launch Issues Register

| # | Issue | Severity | Recommended Owner / Skill | Blocking? | Notes |
|---|---|---|---|---|---|
| 1 | Minors in the user population | High | Privacy counsel | Blocking | Sensitive-population review. `[CONFIRM: applicable framework for minors in the US and EU markets]`. |
| 2 | Location and device-identifier collection | High | Privacy counsel | Blocking | Sensitive-data review; route to `dpa-review` for any third-party data processing. |
| 3 | "Safest option for families" marketing claim | High | Marketing counsel | Blocking | Representation needing substantiation; route to `marketing-claims-review`. |
| 4 | AI feature using third-party model | High | AI governance counsel | Conditional-blocking | Route to `ai-feature-review`; review for data flow, model provider terms, and any youth-specific concerns. |
| 5 | Copyleft open-source library | Medium | IP / open-source counsel | Conditional | Route to `open-source-license-review`. License obligations may interact with distribution of the mobile app binary. |
| 6 | Two third-party SDKs | Medium | Privacy / IP counsel | Conditional | Review SDK terms and data-collection behavior; route to vendor-terms review. |
| 7 | EU launch | Medium | Privacy counsel | Conditional | Sectoral overlay for EU framework. `[verify jurisdiction]`. |

The register is the deliverable; the skill does not issue a compliance certification.

## 3. Routing Map

- Privacy counsel: items 1, 2, 7.
- Marketing counsel: item 3.
- AI governance counsel: item 4.
- IP / open-source counsel: items 5, 6.

## 4. Recommendation Framing

The skill frames the recommendation as **Hold** with **Conditions for attorney sign-off**. Conditions include:

1. Privacy counsel sign-off on the minors / location / device-identifier issues (items 1, 2).
2. Marketing counsel sign-off on the "safest option for families" claim, with substantiation file (item 3).
3. AI governance review of the third-party model integration (item 4).
4. Open-source license review and an open-source compliance plan (item 5).
5. Privacy counsel sign-off on the EU sectoral overlay (item 7).

This framing is **not** a clearance. The product is not characterized as compliant; no launch-clearance representation is made by this skill.

## 5. Open Items for Attorney Verification

- [ ] Each routed issue is owned by the named specialist; sign-off documented.
- [ ] Confirm applicable framework(s) for minors, location data, and device identifiers in each market `[verify jurisdiction]`.
- [ ] Verify the marketing-claim substantiation file; do not rely on the claim until substantiated.
- [ ] Confirm AI-vendor terms and data-flow representations.
- [ ] Confirm open-source license compliance path.
- [ ] Re-evaluate the launch date once conditions are addressed.

## 6. Assumptions vs. Confirmed Facts

**Confirmed facts (from the user / product team):**

- Markets, user population, data categories, AI feature, marketing claim, third-party dependencies, and launch date were provided by the product team.

**Assumptions:**

- Assumed the product description is complete; further data flows may emerge in specialist review.
- Assumed no other marketing claims; further claims may emerge in marketing review.
- No assumptions made about which legal frameworks apply or about whether the product satisfies any framework.
