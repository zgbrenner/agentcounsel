# Example: Product Launch Review

> **Illustrative example — not legal advice.** This is a sample of what the Launch Review skill (`skills/product-legal/launch-review/SKILL.md`) produces. Every product, party, date, and claim in it is **fictional** and was invented for illustration. It is the kind of draft work product a supervising attorney would review — not a finished deliverable, and not legal advice. See `examples/README.md`.

## Scenario

Trailhead Software, Inc. is a consumer mobile app company whose flagship product, "Trailhead," is a hiking and outdoor-navigation app with roughly 2 million monthly active users across the United States, Canada, and the United Kingdom. The product team, led by product manager Devon Park, is preparing to launch a new feature called "SmartRoute AI," an AI-powered route-planning feature that generates personalized hiking routes based on a user's fitness level, real-time location, past activity history, and weather conditions. SmartRoute AI relies on a third-party large language model provider ("NorthStar AI") to generate route narratives and on an open-source elevation-data library to compute terrain difficulty. The feature is slated to launch on August 14, 2026, and the marketing team has drafted landing-page copy describing it as "the safest way to plan any hike" and "trusted by expert guides." SmartRoute AI also introduces an optional premium subscription tier and collects continuous background location data to power real-time rerouting. Legal has not yet reviewed the new functionality, and the launch date is approximately twelve weeks away.

## Illustrative Output

**DRAFT — FOR ATTORNEY REVIEW ONLY**

### 1. Review Summary

- **Product / feature:** SmartRoute AI — AI-powered personalized route-planning feature within the Trailhead consumer mobile app.
- **Company:** Trailhead Software, Inc.
- **Launch date:** August 14, 2026 (approximately 12 weeks out as of this review).
- **Target markets:** United States, Canada, United Kingdom. Consumer (B2C).
- **Review date:** May 21, 2026.
- **Inputs received:** Feature description and user flows; list of data types collected (location, fitness profile, activity history, weather); draft marketing landing-page copy; third-party dependency list (NorthStar AI model API, open-source elevation-data library); launch date.
- **Inputs missing or assumed:**
  - Existing terms of service and privacy policy were referenced but not provided in full — assumed to be the current public versions [CONFIRM: provide controlling versions].
  - The license type of the open-source elevation-data library was not specified [CONFIRM: identify library and license].
  - NorthStar AI vendor contract / API terms were not provided [CONFIRM: provide vendor terms].
  - Whether the feature is marketed to or knowingly used by minors was not stated — assumed general-audience, not directed to children [CONFIRM].

### 2. Launch Issues Register

| Issue Description | Practice Area | Severity | Recommended Owner / Skill | Blocking? | Status |
|---|---|---|---|---|---|
| Continuous background location data is a new sensitive data category not clearly covered by the current privacy notice; legal basis, consent flow, and retention period need confirmation. | Privacy / Data Protection | High | Privacy counsel / `privacy-policy-gap-review` | Yes | Open |
| Marketing claim "the safest way to plan any hike" is an unqualified superlative safety claim that likely requires substantiation. | Marketing / Advertising | High | Advertising counsel / `marketing-claims-review` | Yes | Open |
| Marketing claim "trusted by expert guides" is a testimonial/endorsement-style claim; basis and any guide relationships need verification. | Marketing / Advertising | Medium | Advertising counsel / `marketing-claims-review` | TBD | Open |
| AI-generated route narratives via NorthStar AI raise output-ownership, accuracy/disclaimer, and training-data rights questions. | AI / Product | High | AI counsel / `ai-feature-review` | Yes | Open |
| AI route recommendations affecting user physical safety may be a higher-risk use case requiring disclosure and human-judgment caveats. | AI / Regulatory | High | AI counsel / `ai-feature-review` | TBD | Open |
| NorthStar AI vendor API terms not reviewed; may restrict use, allocate liability, or require user-facing disclosures. | Contracts / Vendor | Medium | Commercial counsel / `contract-risk-review` | TBD | Open |
| Open-source elevation-data library license type unknown; copyleft (e.g., GPL/AGPL) terms could create distribution or disclosure obligations. | IP / Licensing | Medium | IP counsel | TBD | Open |
| New premium subscription tier introduces auto-renewal and recurring billing; auto-renewal disclosure and cancellation requirements may apply. | Consumer Protection | High | Consumer-protection counsel / `terms-of-service-review` | Yes | Open |
| Existing terms of service may not cover AI-generated content, the new subscription, or expanded location processing. | Terms of Service | Medium | Commercial counsel / `terms-of-service-review` | TBD | Open |
| Product name "SmartRoute AI" has not been trademark-cleared for the launch markets. | IP / Trademark | Medium | IP / trademark counsel | TBD | Open |
| Cross-border processing across US, Canada, and UK; UK data transfers and any region-specific requirements need review. | Privacy / International | Medium | Privacy counsel ([verify jurisdiction]) | TBD | Open |
| Accessibility obligations for the new feature UI (e.g., WCAG-aligned standards) not yet assessed. | Accessibility | Low | Product / accessibility specialist | No | Open |
| Personalization based on a user "fitness level" profile — confirm whether any health-adjacent data triggers heightened obligations. | Privacy / Regulatory | Unknown | Privacy counsel | TBD | Open |

### 3. Routing Map

- **Background location data (High, blocking):** Route to privacy counsel and run `privacy-policy-gap-review`; draft privacy notice update and a clear consent flow before launch.
- **"Safest way to plan any hike" superlative claim (High, blocking):** Route to advertising counsel and run `marketing-claims-review` for claim-by-claim substantiation.
- **AI output ownership and accuracy (High, blocking):** Route to AI counsel and run `ai-feature-review`; address output ownership, disclaimers, and training-data rights.
- **AI safety-affecting recommendations (High):** Route to AI counsel via `ai-feature-review` to assess higher-risk use-case treatment and required disclosures.
- **Auto-renewal subscription (High, blocking):** Route to consumer-protection counsel and run `terms-of-service-review` for auto-renewal disclosure and cancellation flow.
- **NorthStar AI vendor terms (Medium):** Route to commercial counsel and run `contract-risk-review` once vendor terms are provided.
- **Open-source library license (Medium):** Route to IP counsel once the library and its license are identified.
- **"SmartRoute AI" trademark (Medium):** Route to trademark counsel for clearance in US, Canada, and UK.

### 4. Go / Hold / Conditions Recommendation *(draft for attorney sign-off)*

**Draft recommendation: HOLD pending resolution of blocking issues — not a legal clearance.**

Five issues are currently marked blocking: (1) background location data privacy treatment, (2) the unqualified safety superlative, (3) AI output ownership and accuracy, (4) AI safety-affecting recommendations pending risk classification, and (5) auto-renewal subscription disclosures. The launch should not proceed on the August 14, 2026 date until these are resolved.

If the blocking issues are resolved, this could convert to a **CONDITIONS** recommendation, with launch permitted subject to: (a) an updated, approved privacy notice and consent flow for background location; (b) substantiated or revised marketing claims approved by advertising counsel; (c) AI disclaimers and output-ownership terms reviewed via `ai-feature-review`; (d) compliant auto-renewal disclosures and cancellation flow; and (e) confirmation that the existing terms of service are amended to cover the new functionality. This recommendation is a draft and must be reviewed and approved by responsible counsel before it is communicated to the launch team.

### 5. Assumptions and Open Items

1. **Assumption:** The current public versions of the Trailhead terms of service and privacy policy are the controlling documents. [CONFIRM: provide controlling versions.]
2. **Assumption:** SmartRoute AI is a general-audience feature not directed to or knowingly used by children. [CONFIRM.]
3. **Assumption:** The marketing landing-page copy provided is the final draft intended for launch. [CONFIRM: confirm final copy.]
4. [CONFIRM: identify the open-source elevation-data library and its license type.]
5. [CONFIRM: provide the NorthStar AI vendor / API terms for contract review.]
6. [CONFIRM: confirm whether the "fitness level" profile includes any health-related data that triggers heightened obligations.]
7. [CONFIRM: confirm the data retention period for background location data and the basis for that period.]
8. [ATTORNEY TO CONFIRM: which jurisdictions' consumer-protection and auto-renewal frameworks apply to the subscription tier across US, Canada, and UK — [verify jurisdiction].]
9. [ATTORNEY TO CONFIRM: whether AI-driven route recommendations affecting physical safety fall within any higher-risk regulatory classification in the launch markets.]
10. [CONFIRM: confirm whether expert guides referenced in marketing have a relationship with Trailhead Software, Inc. and the basis for the "trusted by" claim.]

### 6. Attorney Verification Checklist

- [ ] All required inputs have been received and are complete and accurate.
- [ ] The target markets and user populations are correctly identified and no additional jurisdictions apply.
- [ ] Every sensitive data category (including background location) has been identified and routed to privacy counsel.
- [ ] Marketing claims have been reviewed against substantiation requirements by counsel with advertising law expertise.
- [ ] Open-source and third-party license obligations have been reviewed by IP counsel.
- [ ] AI / algorithmic decision-making features have been reviewed using `ai-feature-review` or by counsel with AI law expertise.
- [ ] Regulated-industry exposure (consumer subscriptions, any health-adjacent data) has been routed to appropriate specialist counsel.
- [ ] The existing terms of service and privacy policy have been confirmed to cover the new functionality, or amendments have been drafted.
- [ ] No legal authority, statute, or regulation has been asserted without verification.
- [ ] All assumptions and `[CONFIRM: ...]` items have been resolved.
- [ ] The go / hold / conditions recommendation has been reviewed and approved by responsible counsel before it is communicated to the launch team.
- [ ] This document is labeled as a draft and is not shared with third parties or used as a compliance certification.
