---
name: Children's Privacy Review
description: "Use when reviewing a product or service that may attract minors to organize audience-analysis facts, age-gating and parental-consent mechanics, data-minimization and profiling facts, and cross-jurisdiction age-threshold divergence for attorney review."
practice_area: privacy
task_type: review
jurisdictions: []
risk_level: critical
requires_attorney_review: true
inputs:
  - "A description of the product or service: what it does, who it is marketed to, and how it is accessed"
  - "Audience-analysis facts: content, marketing, design, and usage signals bearing on whether minors are a likely or actual audience"
  - "The age-gating mechanics as implemented or designed (age screen, self-declaration, verification method, if any)"
  - "The parental-consent flow, if one exists, as implemented or designed"
  - "The data collected from users, defaults applied, and any profiling, personalization, or advertising practices"
  - "Whether the product is offered in or to a school or educational (edtech) context"
  - "Optional: any known instance of actual knowledge of underage use inconsistent with the stated audience or age gate"
outputs:
  - "Audience-analysis fact table (directed-to-children signals)"
  - "Age-gating mechanics summary, described not endorsed"
  - "Parental-consent flow fact table"
  - "Data-minimization, defaults, profiling, and advertising fact table"
  - "School/edtech context flag"
  - "Cross-jurisdiction age-threshold divergence note"
  - "Prominent escalation flag for any actual-knowledge indicator"
related_skills:
  - skills/privacy/pia-generation/SKILL.md
  - skills/product-legal/launch-review/SKILL.md
  - skills/privacy/privacy-policy-gap-review/SKILL.md
  - skills/ai-governance/ai-use-case-intake/SKILL.md
  - skills/product-legal/marketing-claims-review/SKILL.md
tags:
  - privacy
  - childrens-privacy
  - age-gating
  - parental-consent
  - data-minimization
  - edtech
---

# Children's Privacy Review

## Purpose

Organize the facts a reviewing attorney needs to assess whether a product or service attracts, is directed to, or is used by minors, and how it currently handles that population. The skill inventories audience-analysis signals, describes age-gating and parental-consent mechanics as implemented, records data-minimization, default, profiling, and advertising practices as facts, flags school/edtech context, and preserves cross-jurisdiction divergence rather than stating any age threshold as settled. It produces draft legal work product for attorney review — not legal advice.

This skill never concludes that a product "is directed to children," that an age gate or consent flow "is compliant," or that any specific age threshold applies. Those are attorney determinations that depend on jurisdiction, sector, and the totality of the facts. The skill's job is to organize the facts so counsel can make that determination — not to make it.

## Use When

- A product, app, game, or online service is being reviewed for whether children's-privacy obligations may apply.
- A product team is designing or has implemented an age gate, age-assurance mechanism, or parental-consent flow and wants the mechanics organized for legal review.
- A launch review, feature review, or marketing-claims review has surfaced signals that minors may be part of the actual or likely audience.
- The organization operates or is evaluating a school-facing or edtech product and needs the school/education context flagged for specialized review.
- A vendor, partner, or internal team raises a concern that underage users may be present despite the stated age gate or terms of service.
- The organization needs a periodic children's-privacy fact review as part of a broader privacy or product-legal audit.

## Required Inputs

- **A description of the product or service** — its functionality, how it is accessed (web, app, in-person, school-issued device), and its stated intended audience.
- **Audience-analysis facts** — content, subject matter, visual design, marketing channels, user testimonials or reviews, app-store category, influencer or ambassador programs, and any usage or analytics data bearing on the actual or apparent audience. Provide these as facts; do not ask the skill to infer an audience from a bare product name.
- **The age-gating mechanics** as implemented or designed — whether there is an age screen, self-declaration, neutral age screen, or a technical age-verification or age-estimation method, and how it behaves (e.g., what happens on a "too young" answer).
- **The parental-consent flow**, if any — how it is triggered, what is collected from the parent, how consent is verified, and what happens if consent is withheld or not obtained.
- **Data practices** — what personal data is collected from users, what the default settings are (visibility, sharing, notifications, geolocation), and whether profiling, personalization, recommendation systems, or targeted/behavioral advertising are used and whether minors are excluded from them.
- **School/edtech context** — whether the product is offered directly to consumers, through a school or district, under an operator/school agreement, or as an instructional tool, and who is understood to be the contracting party.
- Optional: **any known instance of actual knowledge of underage use** inconsistent with the stated audience or age gate — for example, a support ticket, a parent complaint, or internal data suggesting users below the stated minimum age.
- Optional: the practice group's `practice-profiles/privacy.md` if populated and loaded alongside this skill. If present, use its Standard Positions and Escalation Thresholds to benchmark the review; if absent, proceed without profile benchmarking.

If the product description and audience-analysis facts are not provided, stop and request them. Do not infer audience, age-gating behavior, or data practices from assumption or model background knowledge of similar products.

## Do Not Use When

- The task is to draft or finalize the age-gating or parental-consent flow itself — this skill organizes facts about an existing or proposed design; drafting the actual flow or consent language is an attorney/product task.
- The task is a general product launch review with no children's-audience signal present (use `skills/product-legal/launch-review/SKILL.md`, and route to this skill only if a signal surfaces).
- The task is a general data-processing impact assessment with no minors-specific question (use `skills/privacy/pia-generation/SKILL.md`).
- There is **actual knowledge that the product is being used by underage users in a manner inconsistent with its data practices or consent flow** and no attorney has yet been looped in — stop, do not proceed with the standard review, and escalate immediately per the Legal Safety Rules below.
- The task is to determine which children's-privacy law applies or what a specific age threshold is under a named law — that is always an attorney-verification item this skill flags, never resolves.

## Legal Safety Rules

- **Source and citation discipline.** Follow `core/source-and-citation-discipline.md`. Never invent legal authority, citations, quotations, statutes, cases, regulations, filing deadlines, or procedural rules. Label what is a provided source, a user-provided fact, an assumption, a legal inference, or an item requiring attorney verification, and use a citation placeholder such as `[Attorney to insert authority]` when no source is available.
- Produce draft legal work product for attorney review. This is not legal advice.
- **Never state an age threshold as settled.** Children's-privacy age thresholds (for consent, for the definition of a minor, for heightened protections) differ by jurisdiction, sector, and sometimes by specific right. Every reference to an age threshold in the output must be flagged `[verify jurisdiction]` and never presented as a fixed, universal number.
- **Never conclude that the product "is directed to children."** Whether a product is directed to, targeted at, or mixed-audience with respect to children is a legal and factual determination for counsel. Organize the audience-analysis signals; do not weigh them into a conclusion.
- **Never bless an age-gating or parental-consent mechanism as sufficient.** Describe the mechanics exactly as implemented or designed. Do not characterize an age screen, self-declaration, or verification method as "adequate," "compliant," or "sufficient" — flag adequacy as `[ATTORNEY TO CONFIRM]`.
- **Escalate actual knowledge immediately and prominently.** If the inputs indicate the organization has actual knowledge that underage users are present and are being mishandled relative to the product's stated consent flow, data practices, or age gate — do not proceed with the standard review as a routine matter. Post a prominent escalation banner at the top of the output: `[ATTORNEY TO CONFIRM: actual-knowledge escalation — possible ongoing children's-privacy exposure; route to counsel immediately, do not treat as a routine review]`. Continue to organize the available facts, but do not soften, minimize, or bury this signal inside a routine gap table.
- Record audience-analysis, age-gating, consent-flow, and data-practice facts **as facts described**, never as legal conclusions. Distinguish what the product does from what any law requires.
- Do not compute or assert any deadline (for example, a data-deletion or consent-renewal deadline). Mark every such reference `[deadline verification required]`.
- Flag the school/edtech context prominently — school-facing products commonly carry a distinct consent and contracting model (school-as-agent, operator agreements) that a consumer-facing children's-privacy analysis does not capture; do not analyze a school-facing product using consumer-facing assumptions.
- Preserve confidentiality: keep product-specific and organization-specific facts out of reusable templates; the review is a matter record.
- Flag every gap with a placeholder rather than resolving it silently.
- **Profile reference is optional, not authoritative.** Where `practice-profiles/privacy.md` is loaded, its Standard Positions and Escalation Thresholds inform the draft but never substitute for attorney judgment; if the profile conflicts with the matter facts or the supervising attorney's conclusions, the attorney prevails.

## Workflow

1. **Confirm inputs and screen for actual knowledge first.** Before anything else, check whether the inputs indicate actual knowledge of underage users being mishandled. If so, post the prominent escalation banner (see Legal Safety Rules) at the top of the working output and continue the remaining steps to organize supporting facts, without treating the review as routine.

2. **Record the product description.** Summarize the product or service, how it is accessed, and its stated intended audience, each attributed to its source (user-stated, provided document, or product materials).

3. **Build the audience-analysis fact table.** Record directed-to-children signals as facts: subject matter and content, visual/design style, marketing channels and messaging, app-store category and rating, influencer or ambassador programs, testimonials or reviews suggesting a young audience, and any usage/analytics data on actual age distribution. Note the source of each signal. Do not weigh the signals into an audience conclusion.

4. **Describe the age-gating mechanics.** Record, as implemented or designed and without endorsement: the type of gate (neutral age screen, self-declaration, technical verification/estimation, none), what happens on a "too young" response, whether the gate can be circumvented by re-entry, and whether the gate is applied at signup only or at other points (e.g., feature-specific).

5. **Describe the parental-consent flow, if any.** Record: how consent is triggered, what is collected from the parent (and whether that collection itself is minimized), the verification method used, what access or features are gated pending consent, and what happens if consent is withheld, revoked, or never obtained.

6. **Record data-minimization facts.** List the data collected from users at signup and in ordinary use, and whether collection appears scoped to what the product needs to function. Do not characterize the scope as minimized or excessive — record it as a fact for attorney assessment.

7. **Record defaults, profiling, and advertising facts.** Record the default privacy and visibility settings, whether profiling, personalization, or recommendation systems are applied to minors (or to all users without age-based distinction), and whether targeted or behavioral advertising is served to minors or to the general user base without exclusion.

8. **Flag school/edtech context.** If the product is offered through a school, district, or educational context, record: the contracting party (school, district, or the end user directly), whether an operator/school agreement or equivalent exists, and how consent is structured in that context (e.g., school-as-agent for consent, if stated). Flag this context prominently and note that it requires a distinct analytical track from a consumer-facing product `[ATTORNEY TO CONFIRM: school/edtech consent framework]`.

9. **Note cross-jurisdiction divergence.** Wherever an age threshold, consent requirement, or heightened-protection category is referenced by the product's own materials or by the user, record it as stated but flag: `[verify jurisdiction]` — age thresholds and consent triggers differ by jurisdiction and sector and must never be treated as settled or universal.

10. **Compile escalation items.** Flag prominently: the actual-knowledge banner (if triggered), any school/edtech context, any indication that age-gating can be trivially circumvented, any profiling or targeted advertising directed at a population that includes or likely includes minors, and any data collection from minors that appears to exceed what the product needs to function.

11. **Assemble the output** using `templates/childrens-privacy-facts-table.md`, and label it as draft legal work product for attorney review.

## Output Format

Deliver the following, in order:

1. **Actual-Knowledge Escalation Banner** — if triggered, the prominent `[ATTORNEY TO CONFIRM: actual-knowledge escalation ...]` flag at the very top; if not triggered, a brief statement that no actual-knowledge indicator was present in the inputs provided.
2. **Summary** — 3-5 sentences: the product, its stated audience, and the overall posture of the review (facts organized, not a compliance conclusion).
3. **Audience-Analysis Fact Table** — using `templates/childrens-privacy-facts-table.md`: signal | description | source. No audience conclusion drawn.
4. **Age-Gating Mechanics** — described as implemented, with adequacy flagged `[ATTORNEY TO CONFIRM]`.
5. **Parental-Consent Flow Facts** — trigger, data collected from parent, verification method, consequence of no/withheld consent.
6. **Data-Minimization Facts** — data collected, scoped to function or not, as a fact for attorney assessment.
7. **Defaults, Profiling, and Advertising Facts** — default settings, profiling/personalization exposure, targeted-advertising exposure to minors.
8. **School/Edtech Context Flag** — present or absent; if present, contracting party and consent structure, flagged `[ATTORNEY TO CONFIRM: school/edtech consent framework]`.
9. **Cross-Jurisdiction Divergence Notes** — every age threshold or consent-trigger reference, each `[verify jurisdiction]`.
10. **Escalation Items** — factors requiring immediate attorney attention.
11. **Attorney Verification Items and Assumptions** — every placeholder gathered in one list, followed by every assumption made.

### Optional: Business Stakeholder Summary

When the output will brief a non-lawyer stakeholder (a product owner, trust-and-safety lead, or executive sponsor), add a **Business Stakeholder Summary** as a clearly separated section following `core/business-stakeholder-communication.md` — Business Summary, Decision Needed, Recommended Ask, Fallback Position, and Escalation Needed? — produced only on request or for a plainly business audience, always in addition to the deliverable above and never a substitute for attorney review.

## Attorney Verification Checklist

- [ ] Any actual-knowledge escalation has been reviewed by counsel and addressed before the product continues its current practices.
- [ ] Whether the product is directed to, targeted at, or a mixed audience including children has been determined by counsel — not by this draft.
- [ ] Every age threshold or consent-trigger reference has been confirmed under the applicable jurisdiction and sector. `[verify jurisdiction]`
- [ ] The age-gating mechanism has been assessed by counsel for adequacy, including its resistance to circumvention.
- [ ] The parental-consent flow (if any) has been assessed by counsel for adequacy, including the verification method used.
- [ ] Data-minimization practices for minors have been reviewed and confirmed proportionate.
- [ ] Profiling, personalization, and targeted/behavioral advertising exposure to minors has been reviewed and addressed.
- [ ] If a school/edtech context is present, the applicable consent framework and contracting structure have been confirmed by counsel.
- [ ] All `[CONFIRM: ...]`, `[ATTORNEY TO CONFIRM: ...]`, `[verify jurisdiction]`, and `[deadline verification required]` placeholders have been resolved before this draft is relied upon.
- [ ] If a practice profile was loaded: every applicable Standard Position and Escalation Threshold has been surfaced and deviations flagged; if none was loaded, no standing-position framing was assumed.
