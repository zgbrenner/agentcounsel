---
name: Cookie Consent Review
description: "Use when reviewing a website or app's cookie and tracking consent implementation to inventory trackers against disclosure, describe consent-banner mechanics, record consent-record facts, and flag dark-pattern and cross-border divergence issues for attorney review."
practice_area: privacy
task_type: review
jurisdictions: []
risk_level: high
requires_attorney_review: true
inputs:
  - "The site or app's cookie/tracker inventory or a scan output listing trackers actually present"
  - "The cookie/tracking disclosure text (cookie notice, cookie policy, or privacy policy tracking section)"
  - "A description or screenshots of the consent banner and its behavior (timing, choices offered, layout)"
  - "Facts about consent-record keeping: what is logged, where, and for how long"
  - "Optional: whether a consent management platform (CMP) or IAB TCF-style framework is in use"
  - "Optional: the geographies/markets where the site or app operates"
outputs:
  - "Tracker inventory vs. disclosure comparison table"
  - "Consent-banner mechanics summary, described not endorsed"
  - "Consent-record fact table"
  - "Dark-pattern red-flag list, named neutrally"
  - "CMP/TCF-framework presence note"
  - "Cross-border divergence flags"
related_skills:
  - skills/privacy/privacy-policy-gap-review/SKILL.md
  - skills/privacy/cross-border-transfer-review/SKILL.md
  - skills/privacy/vendor-privacy-diligence/SKILL.md
  - skills/product-legal/marketing-claims-review/SKILL.md
  - skills/privacy/dpa-review/SKILL.md
tags:
  - privacy
  - cookies
  - tracking-technologies
  - consent-management
  - dark-patterns
  - adtech
---

# Cookie Consent Review

## Purpose

Organize a review of a website or app's cookie and tracking-technology consent implementation into an attorney-ready fact record. The skill inventories the trackers actually present against what the site or app discloses, describes the consent-banner mechanics as implemented, records consent-record-keeping facts, names dark-pattern indicators neutrally, notes the presence of a consent management platform (CMP) or IAB TCF-style framework as a fact (not an endorsement), and flags cross-border divergence. It produces draft legal work product for attorney review — not legal advice.

This skill never concludes that a consent implementation "is compliant," that a banner design "is" or "is not" a dark pattern, or that a given consent record satisfies any law's evidentiary requirements. Those are attorney determinations that vary by jurisdiction, regulator guidance, and the totality of the implementation. The skill organizes the facts so counsel can make that determination.

## Use When

- A website or app's cookie banner, tracker inventory, or consent flow needs a first-pass legal/compliance read.
- A privacy or marketing team has run a tracker scan and needs the results compared against the cookie notice or privacy policy.
- The organization is evaluating or has just deployed a consent management platform (CMP) and wants its configuration facts organized for review.
- A regulator inquiry, complaint, or internal audit has raised a question about whether disclosed and actual tracking match, or whether the consent flow gives users a genuine choice.
- The organization operates across multiple markets and needs the site's consent mechanics checked for jurisdiction-specific divergence (for example, prior-consent vs. opt-out models, or reject-parity requirements).
- A redesign of the cookie banner or consent flow is proposed and the current-state facts need to be captured before changes are made.

## Required Inputs

- **The tracker inventory or scan output** — a list of cookies, pixels, SDKs, and other tracking technologies actually present on the site or app, ideally from a scan tool or manual audit, including the technology name, vendor, and stated category (essential, functional, analytics, advertising, etc.), if categorized. Do not proceed on a description of "we use some cookies" alone.
- **The cookie/tracking disclosure text** — the cookie notice, cookie policy, or the tracking section of the privacy policy, in full.
- **A description or screenshots of the consent banner** — its timing (does tracking occur before a choice is made), the choices actually offered (accept all, reject all, customize, close/dismiss), the visual layout and prominence of each choice, and any pre-checked boxes or pre-selected categories.
- **Consent-record-keeping facts** — what the organization logs when a user makes a choice (timestamp, choice made, banner version, user/device identifier), where the record is stored, and the stated retention period for consent records.
- Optional: whether a **CMP or IAB TCF-style framework** is in use, and which one.
- Optional: the **geographies/markets** where the site or app operates, so cross-border divergence can be flagged against the actual footprint rather than assumed.
- Optional: the practice group's `practice-profiles/privacy.md` if populated and loaded alongside this skill. If present, use its Standard Positions and Escalation Thresholds to benchmark the review; if absent, proceed without profile benchmarking.

If the tracker inventory and the disclosure text are not both provided, stop and request them. Do not infer the tracker inventory from the disclosure text, or vice versa — comparing the two is the point of the review.

## Do Not Use When

- The task is to draft new cookie-notice or banner language — this skill organizes facts about the current implementation; drafting replacement language is an attorney/product task.
- No tracker inventory or scan is available and none can be obtained — a review built only on the disclosure text cannot compare disclosure against actual practice, which is the review's core function; note the gap and consider whether a scan should be run first.
- The task is a general privacy-policy gap review with no cookie/tracking-specific focus (use `skills/privacy/privacy-policy-gap-review/SKILL.md`).
- The task is a cross-border data-transfer mechanism review untethered to the cookie/consent banner itself (use `skills/privacy/cross-border-transfer-review/SKILL.md`).
- The task is vendor diligence on an adtech or CMP vendor's own practices in isolation (use `skills/privacy/vendor-privacy-diligence/SKILL.md`).

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- **Never conclude that the consent implementation is compliant, adequate, or lawful.** Consent requirements (prior consent vs. opt-out models, what counts as "granular," what a valid "reject" option must look like) vary by jurisdiction and by tracker category. Flag every such question `[verify jurisdiction]` and `[ATTORNEY TO CONFIRM]`.
- **Name dark-pattern indicators neutrally, as described design facts — never as a legal or ethical conclusion.** Record what the design does (for example: "Reject option requires more clicks than Accept," "Accept button uses higher-contrast color than Reject," "Categories are pre-checked by default," "Banner reappears until Accept is selected") without labeling it "manipulative," "deceptive," or "unlawful." Flag it for attorney assessment.
- **Record CMP/TCF-style framework presence as a fact, never as an endorsement or compliance signal.** Using a recognized framework does not itself establish that a specific configuration is lawful; note the framework's presence and version if known, and flag configuration-specific questions for attorney review.
- Compare the tracker inventory against the disclosure **only using what is actually provided.** Do not assume a tracker is disclosed because it fits a disclosed category name unless the disclosure text actually lists or clearly covers it — flag ambiguous coverage rather than resolving it.
- Record consent-record facts (what is logged, where, for how long) as facts. Do not conclude that the record-keeping satisfies any evidentiary or accountability requirement — flag adequacy `[ATTORNEY TO CONFIRM]`.
- Do not compute or assert any deadline (for example, a consent-renewal or re-consent interval). Mark every such reference `[deadline verification required]`.
- Flag cross-border divergence wherever the site or app's footprint spans multiple markets: prior-consent vs. opt-out consent models, "reject" parity requirements, and granularity requirements differ by jurisdiction — `[verify jurisdiction]` throughout, and never state that one jurisdiction's rule applies to the whole footprint.
- Preserve confidentiality: keep site-specific vendor lists and organization-specific facts out of reusable templates; the review is a matter record.
- Flag every gap with a placeholder rather than resolving it silently.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/privacy.md` is loaded, its Standard Positions and Escalation Thresholds inform the draft but never substitute for attorney judgment; if the profile conflicts with the matter facts or the supervising attorney's conclusions, the attorney prevails.

## Workflow

1. **Confirm inputs.** Verify the tracker inventory and the disclosure text are both provided. Note whether banner description/screenshots, consent-record facts, CMP/TCF information, and market footprint are available; record absences as scoping limitations.

2. **Build the tracker-vs-disclosure comparison.** For each tracker in the inventory, record: name, vendor, stated category (if categorized), and whether the disclosure text lists it by name, lists its category generically, or does not address it. Flag any tracker present but not clearly covered by the disclosure as a disclosure gap. Flag any category named in the disclosure with no corresponding tracker found as a possible stale disclosure entry.

3. **Describe the consent-banner mechanics as implemented.** Record: whether any tracking occurs before a choice is made (prior-consent vs. tracking-then-choice), the choices actually offered and their labels, whether "reject" and "accept" are presented with comparable prominence ("reject parity"), whether categories can be selected/deselected individually ("granularity"), and whether any category is pre-checked by default. Describe exactly what is implemented — do not characterize it as compliant or non-compliant.

4. **Record consent-record facts.** Record what is logged at the moment of choice (timestamp, choice made, banner/policy version in effect, identifier used), where the record is stored, and the stated retention period. Flag any gap (for example, no logged banner version, making it hard to reconstruct what a user actually agreed to) without concluding it is inadequate — flag `[ATTORNEY TO CONFIRM]`.

5. **Name dark-pattern indicators neutrally.** Using the banner-mechanics facts from step 3, list each design choice that is a commonly discussed dark-pattern indicator (asymmetric visual weighting of accept/reject, extra steps to reject, pre-checked boxes, repeated re-prompting after rejection, confirmshaming language, no persistent way to withdraw consent) as a described fact with a citation to what was observed. Do not label any indicator "a dark pattern" as a conclusion — name it neutrally and flag it for attorney assessment.

6. **Record CMP/TCF-style framework presence.** If a CMP or IAB TCF-style (or equivalent) framework is in use, record which one, and any configuration details provided (categories exposed, vendor list length, default settings). State plainly that the framework's presence is a fact, not a compliance signal, and flag configuration-specific questions `[ATTORNEY TO CONFIRM]`.

7. **Flag cross-border divergence.** If the site or app operates in more than one market, or the market footprint is unstated, flag that consent-model requirements (prior consent vs. opt-out, reject-parity, granularity) diverge by jurisdiction and that the current implementation may need to vary by user location. Do not assume a single jurisdiction's rule governs the whole footprint. `[verify jurisdiction]`

8. **Compile escalation items.** Flag prominently: any tracker actively firing that is not covered by the disclosure at all (not merely under-specified), any consent flow where tracking occurs with no choice presented first in a market where prior consent is commonly required, any dark-pattern indicator combination that appears to make rejection materially harder than acceptance, and any indication that consent records cannot be reconstructed for a given user or period.

9. **Assemble the output** using `templates/cookie-consent-review-table.md`, and label it as draft legal work product for attorney review.

## Output Format

Deliver the following, in order:

1. **Summary** — 3-5 sentences: what was reviewed, the site/app's stated footprint, and the overall posture (facts organized, not a compliance conclusion).
2. **Tracker-vs-Disclosure Table** — using `templates/cookie-consent-review-table.md`: Tracker | Vendor | Category | Disclosure Coverage (named / generic-category / not addressed).
3. **Consent-Banner Mechanics** — described as implemented: prior-consent vs. tracking-before-choice, choices offered, reject-parity observation, granularity, default/pre-checked state — no compliance conclusion.
4. **Consent-Record Facts** — what is logged, where, retention period, and any reconstruction gap.
5. **Dark-Pattern Indicators (Named Neutrally)** — each observed indicator described as a design fact, flagged for attorney assessment — no "dark pattern" conclusion.
6. **CMP/TCF-Framework Presence Note** — framework in use (if any), configuration facts provided, and the express caveat that this is not a compliance signal.
7. **Cross-Border Divergence Flags** — every consent-model question flagged `[verify jurisdiction]`, tied to the stated market footprint.
8. **Escalation Items** — factors requiring immediate attorney attention.
9. **Attorney Verification Items and Assumptions** — every placeholder gathered in one list, followed by every assumption made.

### Optional: Business Stakeholder Summary

When the output will brief a non-lawyer stakeholder (a marketing lead, product owner, or executive sponsor), add a **Business Stakeholder Summary** as a clearly separated section following `core/business-stakeholder-communication.md` — Business Summary, Decision Needed, Recommended Ask, Fallback Position, and Escalation Needed? — produced only on request or for a plainly business audience, always in addition to the deliverable above and never a substitute for attorney review.

## Attorney Verification Checklist

- [ ] The tracker inventory reviewed reflects trackers actually present, current as of the scan or audit date.
- [ ] Every tracker's disclosure coverage has been confirmed adequate under applicable law by counsel. `[verify jurisdiction]`
- [ ] The consent-banner mechanics (prior consent, reject parity, granularity, defaults) have been assessed by counsel against the applicable consent model for each relevant market.
- [ ] Consent-record-keeping has been assessed for evidentiary adequacy; any reconstruction gap has been addressed.
- [ ] Every named dark-pattern indicator has been assessed by counsel; none has been treated as resolved by this draft.
- [ ] Any CMP/TCF-style framework configuration has been reviewed on its own terms — its presence was not treated as a compliance conclusion.
- [ ] Cross-border divergence has been resolved market-by-market by counsel; no single jurisdiction's rule was assumed to govern the whole footprint.
- [ ] All `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and `[deadline verification required]` placeholders have been resolved before this draft is relied upon.
- [ ] If a practice profile was loaded: every applicable Standard Position and Escalation Threshold has been surfaced and deviations flagged; if none was loaded, no standing-position framing was assumed.
