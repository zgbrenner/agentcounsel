# Practice-Area Expansion Plan

**Status:** Substantially implemented. Most of what this document proposed has
since been built — see the Implementation status section below for what
shipped, what diverged, and what remains open. The document is retained for
the four-tier taxonomy model and the rationale behind each placement decision,
which continue to govern how new areas and overlays are added.

> Current totals (practice areas, skill counts) are tracked in [`metadata/index.json`](../metadata/index.json) and summarized in [`README.md`](../README.md). Any specific figures below reflect the state at the time of writing.

**Purpose:** Audit AgentCounsel's current practice-area taxonomy and propose a
disciplined model for expanding it — adding the practice areas the library is
missing without making the repository messy, duplicative, or inconsistent.

---

## Implementation status

Where each recommendation in this plan stands as of this update. Where the
implementation diverged from the plan, the divergence is stated plainly.

| Recommendation | Current state |
|---|---|
| Wave 0 — overlay infrastructure (`overlays/` scaffold, `OVERLAY.md` template, `docs/PRACTICE_AREAS.md` registry) | Done. |
| Wave 0 — fold `m-and-a` into `corporate` | **Diverged:** `m-and-a` was built as a standalone top-level area (10 skills) instead of being folded into `corporate`. |
| Wave 0 — fold `consumer-protection` into `product-legal`; fold `personal-injury` into `litigation` | Open — the fold-in skills have not been added. |
| Wave 1 — `real-estate` | Done (9 skills). |
| Wave 2 — `insurance` | Done as a top-level area (12 skills). **Diverged on scope:** shipped broader than the coverage-only scope proposed here, including `insurance-requirements-contract-review`. |
| Wave 2 — `tax` | Done (10 skills). |
| Wave 2 — `bankruptcy-restructuring` | Done (12 skills). |
| Wave 2 — `securities-capital-markets` | Done (12 skills). **Diverged on naming:** the directory kept the long name `securities-capital-markets` rather than the shorter `securities` suggested in Section 11. |
| Wave 2 — `antitrust-competition` | Done (10 skills). |
| Wave 2 — `government-contracts` | Open. |
| Overlays — `healthcare`, `fintech-payments` | Done, under `overlays/`. |
| Overlays — environmental & ESG, education | Being added in the current update. |
| Overlay — `entertainment-media-sports` | Open. |
| Wave 3 — mission-fit decision (Section 11) | Resolved in favor of covering individual-client work; the core operating rule `core/capacity-and-vulnerable-parties.md` now carries the vulnerable-party safety obligations. |
| Wave 3 — `trusts-estates` | Done (12 skills). |
| Wave 3 — `family-law` | Done (12 skills). |
| Wave 3 — `immigration` | Open. |

---

## 1. Audit of the current taxonomy

AgentCounsel has 14 directories under `skills/`:

`ai-governance`, `contracts`, `corporate`, `employment`, `financial-crime`,
`ip`, `legal-methodology`, `legal-ops`, `legal-research`, `litigation`,
`privacy`, `product-legal`, `regulatory`, `setup` — 66 skills in total.

*(Historical: 14 areas and 66 skills were the totals at the time of writing.
As of this update, `skills/` holds 23 directories and 191 skills — see
Implementation status.)*

Classified into the four-tier model proposed in Section 2:

| Tier | Current areas |
|---|---|
| 1 — Core legal practice areas | `contracts`, `corporate`, `employment`, `ip`, `litigation`, `legal-research`, `privacy` |
| 2 — Advanced / specialized | `product-legal`, `regulatory`, `ai-governance`, `financial-crime` |
| 3 — Industry / regulatory overlays | *(none)* |
| 4 — Cross-cutting support groups | `legal-methodology`, `legal-ops`, `setup` |

### Findings

1. **The taxonomy is real but undocumented.** The 14 areas are sound, but the
   library has never written down which tier each belongs to or what the tiers
   mean. New contributors have no rule for where a new area belongs.
2. **The overlay tier is empty, and there is no overlay mechanism.** The
   library has no way to express "healthcare work" or "fintech work" except by
   creating a new top-level area. That is the single largest duplication risk:
   without an overlay mechanism, every sector becomes a parallel skill tree.
3. **Supporting layers already lag behind the areas.** Only 9 of 12 practice
   areas have a practice profile (`financial-crime` and `legal-ops` have
   none); only 4 cold-start interviews exist; only 8 of 66 skills have evals;
   only 6 matter-workspaces exist. Adding areas without a "definition of done"
   will widen these gaps.
4. **`legal-ops` is shelved with the practice areas but is cross-cutting
   support.** `ai-governance` and `financial-crime` also sit on the border
   between a practice area and an overlay. The directory layout does not encode
   the distinction.
5. **`practice_area` is validated against directory names** (`docs/SKILL_METADATA_STANDARD.md`,
   `scripts/validate_repo.py`) — a good gate — but the *tier* and *maturity* of
   an area are recorded nowhere.
6. **The candidate list has naming problems.** `m-and-a` is awkward as a
   directory; `environmental-energy-esg` bundles three different things;
   `securities-capital-markets` is long. These are addressed in Section 9.

---

## 2. The four-tier taxonomy model

Every area in the library should be classified into exactly one tier. The tier
determines how the area is built and where it lives.

### Tier 1 — Core legal practice areas

The foundational areas almost every legal team touches. Broad, document- and
matter-centric, generally jurisdiction-light at the workflow level. They live
under `skills/` as top-level directories and are the most heavily resourced
(profiles, cold-start interviews, matter-workspaces, evals).

### Tier 2 — Advanced / specialized legal practice areas

Narrower, self-contained bodies of legal doctrine that require specialist
expertise and generate document or matter types not covered by a Core area.
Also top-level directories under `skills/`, but typically higher `risk_level`,
stricter safety language, and a hard requirement for evals before they are
marked stable.

### Tier 3 — Industry or regulatory overlays

**Not bodies of law — sectors, industries, or client types.** Legal work in a
sector (healthcare, fintech, energy) cuts across many practice areas; the
"specialness" is regulatory and contextual coloring, not a new set of document
types. Overlays are **not** top-level `skills/` directories. They are
implemented as a profile plus a reference pack that *modifies how existing
skills run* (see Section 4). This tier is the library's defense against
duplication.

### Tier 4 — Cross-cutting support groups

Not legal practice at all — groups that support the library or the user's
process: `setup` (configuration), `legal-methodology` (analytical disciplines),
`legal-ops` (legal-operations workflows). They live under `skills/` but are
labeled clearly as support, not practice areas, in `README.md` and
`SKILLS_INDEX.md`.

---

## 3. Placement decision framework

Before a candidate is added, run it through this test. It produces one of four
outcomes: **new top-level area**, **fold into an existing area**, **overlay**,
or **decline**.

**Make it a new top-level practice area only if ALL of these hold:**

- It has a substantial, self-contained body of legal doctrine distinct from
  every existing area.
- It generates document or matter types that no existing area's skills handle.
- At least 3 viable starter skills can be written that are genuinely new
  workflows, not re-skins of existing skills.
- It is a body of law, not primarily a sector or client type.

**Fold it into an existing area if:**

- A majority of its work is already covered by an existing area's skills, and
  the difference is sub-specialty flavor.
- Making it standalone would duplicate skills the library already has (another
  "contract review," another "intake," another "chronology").

**Make it an overlay if:**

- It is a sector, industry, or client type rather than a body of doctrine.
- Its legal work spans several existing practice areas.
- Making it an area would force per-sector duplicates of core skills.

**Decline (or defer pending a maintainer decision) if:**

- It does not fit the library's mission (e.g., a shift from commercial /
  in-house work to individual-client representation), or
- It cannot be built safely within the skill model.

A candidate that is close to the line should default to **fold** or **overlay**
— the conservative choice — and be promoted to a top-level area later only if
demand is demonstrated.

---

## 4. The overlay mechanism (the anti-duplication device)

This is the most important structural recommendation. Without it, every sector
in the candidate list becomes a new area and the repository doubles in size
with near-duplicate skills.

**An overlay does not contain skills.** It contains:

- An `OVERLAY.md` — what the sector is, which core skills it modifies, the
  sector's escalation gates and safety triggers, key regulators and
  terminology, and an explicit statement of what it does *not* change.
- An overlay **profile** — the sector equivalent of a `practice-profiles/`
  file: sector-specific gates, standard positions, prohibited assumptions.
- An optional **reference pack** — sector red-flag catalogs and checklists,
  modeled on `skills/contracts/references/`.

**How it is used:** the user runs the normal skill (e.g.,
`contract-risk-review`) and *also* loads the overlay. The overlay sharpens the
skill for the sector; it never replaces it.

**Proposed location:** a new top-level `overlays/` directory, one folder per
overlay. Keeping overlays out of `skills/` is deliberate — it stops a sector
from masquerading as a practice area. (A lighter alternative is
`practice-profiles/overlays/`; either works, but a visible top-level directory
is clearer.) Implementing the overlay tier requires a small amount of
infrastructure — a directory convention, an `OVERLAY.md` template, and a
`validate_repo.py` update so `overlays/` is not scanned as skills. This
infrastructure is **Wave 0** work and must land before the first overlay.

**The one exception:** if a sector genuinely needs a workflow that no existing
skill covers (for example, a clinical-trial-agreement review), that *single*
skill is added to the most relevant existing practice area — never a new
sector directory. The overlay still carries the profile and references.

---

## 5. Maturity model — `experimental` to `stable`

A new area should not appear in the catalog as if it were as battle-tested as
`contracts`. Introduce a lightweight, area-level maturity status.

- **`experimental`** — the area exists, has at least one skill, and validation
  passes, but it is not yet fully resourced or reviewed. It is labeled
  `experimental` in `README.md` and `SKILLS_INDEX.md` and in a new
  `docs/PRACTICE_AREAS.md` registry.
- **`stable`** — the area has met every item in the Section 6 definition of
  done, including evals and subject-matter-expert review.

Record tier and maturity in a single new registry file, `docs/PRACTICE_AREAS.md`
(area, tier, maturity, profile?, cold-start?, eval coverage). This keeps the
taxonomy in one auditable place without changing the per-skill frontmatter
standard. Optionally, an area-level `status` could later be added to skill
frontmatter, but the registry file is the lighter first step.

---

## 6. Definition of done for a new top-level practice area

A new area is not "done" — and cannot be marked `stable` — until all of this is
true. This checklist is the contract that keeps expansion from creating mess.

1. The candidate passed the Section 3 test as a genuine top-level area.
2. `skills/<area>/` contains 3–6 skills, each with the full eleven-field
   frontmatter, the eight required sections, and source/citation-discipline
   language (`scripts/validate_repo.py` passes).
3. `<area>` is added to the `practice_area` controlled list in
   `docs/SKILL_METADATA_STANDARD.md`.
4. The area is listed in `README.md`, `SKILLS_INDEX.md`, `WORKFLOW_ROUTER.md`,
   and `COMMANDS.md`, with consistent naming and counts.
5. A practice profile exists at `practice-profiles/<area>.md`.
6. `metadata/index.json` is regenerated (`scripts/build_skill_index.py`).
7. `scripts/validate_repo.py` and `scripts/check_evals.py` pass; the plugin
   bundle is synced if the area contributes a bundled skill.
8. At least one eval exists per skill (or an agreed minimum eval set);
   high-risk areas have evals **before** the area is announced, not merely
   before `stable`.
9. A matter-workspace exists if the area is matter-centric.
10. A cold-start interview skill exists under `skills/setup/`.
11. Every skill has had subject-matter-expert / attorney review.
12. `CHANGELOG.md` and `docs/PRACTICE_AREAS.md` are updated.

Items 1–7 are required to merge an `experimental` area. Items 8–12 are required
to mark it `stable`.

---

## 7. Candidate analysis — fold into an existing area

These three candidates must **not** become top-level areas: they would
duplicate skills the library already has. They are added as sub-specialty
skills inside an existing area.

### m-and-a → fold into `corporate`

*(Superseded: `m-and-a` was ultimately built as a standalone top-level area
with 10 skills — see Implementation status.)*

- **Recommendation:** Fold into `corporate`. Keep the directory name
  `corporate`; broaden its display name to "Corporate & M&A" in `README.md`
  and `SKILLS_INDEX.md`. Do not rename the directory (it would break paths,
  frontmatter, the plugin bundle, and the site).
- **Rationale:** `corporate` already holds `closing-checklist`,
  `diligence-issue-extraction`, and `material-contract-schedule` — all
  M&A-centric. A separate `m-and-a` area would duplicate them. M&A is the
  flagship sub-specialty of corporate work, not a separate doctrine.
- **Starter skills (add to `corporate/`):** `merger-agreement-review`;
  `disclosure-schedule-builder`; `reps-and-warranties-review`;
  `purchase-price-mechanism-review` (earn-outs, escrows, adjustments);
  `m-and-a-diligence-summary` (or extend `diligence-issue-extraction`).
- **Unique safety restrictions:** none beyond `corporate`'s; reinforce that
  deal economics and price mechanics are organized, never computed.
- **Practice profile:** no new profile — extend `practice-profiles/corporate.md`
  with M&A sections.
- **Cold-start interview:** no — `corporate-cold-start-interview` covers it;
  add M&A questions to it.
- **Evals before stable:** yes — add evals for each new M&A skill.

### consumer-protection → fold into `product-legal`

- **Recommendation:** Fold into `product-legal`. Broaden its display name to
  "Product & Consumer" if desired.
- **Rationale:** `product-legal` already covers `marketing-claims-review` and
  `terms-of-service-review` — the core of consumer-protection work. Advertising,
  disclosures, dark patterns, and consumer-contract fairness are the same
  practice. A separate area would split one body of work in two.
- **Starter skills (add to `product-legal/`):** `advertising-substantiation-review`;
  `disclosure-adequacy-review`; `dark-pattern-review`;
  `auto-renewal-and-cancellation-review`; `consumer-contract-fairness-review`.
- **Unique safety restrictions:** unfair/deceptive-practice standards are
  highly jurisdiction-specific — never assert that a practice "is" or "is not"
  deceptive; flag for attorney verification.
- **Practice profile:** extend `practice-profiles/product-legal.md`.
- **Cold-start interview:** none new.
- **Evals before stable:** yes for the new skills.

### personal-injury → fold into `litigation`

- **Recommendation:** Fold into `litigation` as a sub-specialty; optionally
  also publish a "personal injury" overlay later if plaintiff vs. defense
  workflows diverge enough.
- **Rationale:** `litigation` already has `matter-intake`,
  `litigation-chronology`, `demand-letter`, and `deposition-prep` — directly
  usable for PI. PI is tort litigation, not a separate doctrine. A standalone
  area would duplicate the litigation toolkit.
- **Starter skills (add to `litigation/`):** `injury-claim-intake`;
  `medical-records-chronology` (a medical-record-focused variant of the
  chronology skill); `damages-summary` (special and general damages);
  `settlement-evaluation-organizer`.
- **Unique safety restrictions:** medical records are highly sensitive
  personal data — reinforce confidentiality; statutes of limitation are
  outcome-determinative — never compute, always flag; never state a claim's
  settlement value as a figure, only organize the inputs.
- **Practice profile:** extend `practice-profiles/litigation.md`.
- **Cold-start interview:** none new — `litigation-cold-start-interview`.
- **Evals before stable:** yes for the new skills.

---

## 8. Candidate analysis — new top-level practice areas

Ten candidates qualify as genuine new areas. None should be created "now," in
the same window as a v0.1.0 release; they are sequenced into waves in Section
10. Each entry below states the recommended wave.

### real-estate — Tier 2 — Wave 1 (first new area)

- **Recommendation:** New top-level area. The cleanest, lowest-risk first new
  area — document-centric, high demand, fits the skill model exactly. Use it
  to prove the new-area process.
- **Starter skills:** `commercial-lease-review`;
  `purchase-and-sale-agreement-review`; `lease-abstract`;
  `title-and-survey-review`; `estoppel-and-snda-review`;
  `land-use-and-zoning-triage`.
- **Unique safety restrictions:** never confirm title status, marketability,
  or that liens are cleared; recording, option, and notice deadlines are
  flagged, never computed; property law is intensely local — `[verify
  jurisdiction]` on every substantive point.
- **Practice profile:** yes — `practice-profiles/real-estate.md`.
- **Cold-start interview:** yes, at the `stable` milestone.
- **Evals before stable:** yes.

### insurance (coverage) — Tier 2 — Wave 2

- **Recommendation:** New top-level area, scoped to **insurance coverage**
  (policyholder-side policy review and coverage analysis). The
  insurer-as-regulated-industry angle is a separate, later **overlay**, not
  part of this area. Note the boundary: contract *insurance requirements* (an
  insurance clause in a commercial agreement) stay in `contracts` — they are
  already covered by the contracts red-flag catalog.
- **Starter skills:** `policy-coverage-review`; `claim-coverage-analysis`;
  `reservation-of-rights-review`; `additional-insured-analysis`;
  `coverage-position-summary`.
- **Unique safety restrictions:** never opine that a claim "is covered" or
  "is denied" — organize the coverage analysis for an attorney; coverage turns
  on policy wording and jurisdiction; notice and proof-of-loss deadlines are
  flagged, never computed.
- **Practice profile:** yes.
- **Cold-start interview:** yes, at `stable`.
- **Evals before stable:** yes.

### tax — Tier 2 — Wave 2 (narrow scope)

- **Recommendation:** New top-level area, but **deliberately narrow** —
  structural issue-spotting only. Tax is numeric, jurisdiction-specific, and
  advice-heavy; an over-broad tax area is unsafe.
- **Starter skills:** `transaction-tax-issue-spotting`;
  `contract-tax-clause-review` (gross-up, withholding, tax indemnity);
  `entity-classification-triage`; `withholding-and-reporting-triage`.
- **Unique safety restrictions:** **never compute tax liability, rates, or
  amounts**; never produce a tax opinion or state a position as correct;
  never state a filing deadline; every output is an issue list for a tax
  attorney or accountant. `risk_level: high`.
- **Practice profile:** yes.
- **Cold-start interview:** yes, at `stable`.
- **Evals before stable:** yes — and evals should exist **before announcement**
  given the failure modes.

### bankruptcy-restructuring — Tier 2 — Wave 2 (deadline-critical)

- **Recommendation:** New top-level area.
- **Starter skills:** `automatic-stay-analysis`; `proof-of-claim-triage`;
  `executory-contract-review` (assumption / rejection);
  `preference-and-avoidance-triage`; `restructuring-options-summary`;
  `creditor-and-claims-review`.
- **Unique safety restrictions:** bar dates and bankruptcy deadlines are
  unforgiving and often non-extendable — **never compute any date**, always
  `[deadline verification required]`; the automatic stay is critical and
  acting in violation is sanctionable — treat stay scope as attorney
  judgment. `risk_level: high` (some skills `critical`).
- **Practice profile:** yes.
- **Cold-start interview:** yes, at `stable`.
- **Evals before stable:** yes — required before announcement.

### securities-capital-markets — Tier 2 — Wave 2

- **Recommendation:** New top-level area. Consider the shorter directory name
  `securities`.
- **Starter skills:** `disclosure-document-review`; `risk-factor-review`;
  `periodic-report-review`; `securities-filing-triage`;
  `insider-trading-policy-review`; `equity-incentive-plan-review`.
- **Unique safety restrictions:** securities law is heavily regulated and
  disclosure liability is severe — never conclude that a disclosure is
  "adequate" or that an exemption "applies"; never confirm filing deadlines or
  exemptions; jurisdiction- and regime-specific. `risk_level: high`.
- **Practice profile:** yes.
- **Cold-start interview:** yes, at `stable`.
- **Evals before stable:** yes — required before announcement.

### antitrust-competition — Tier 2 — Wave 2

- **Recommendation:** New top-level area.
- **Starter skills:** `merger-notification-triage`;
  `competitor-collaboration-review`;
  `distribution-and-pricing-restriction-review`;
  `information-exchange-risk-review`; `antitrust-risk-triage`.
- **Unique safety restrictions:** never confirm merger-filing thresholds or
  deadlines; never conclude conduct is "lawful" or "unlawful"; hardcore
  conduct (cartel, bid-rigging) carries criminal exposure — include an
  escalation gate that stops the workflow and routes to counsel.
- **Practice profile:** yes.
- **Cold-start interview:** yes, at `stable`.
- **Evals before stable:** yes.

### government-contracts — Tier 2 — Wave 2 (or overlay if low demand)

- **Recommendation:** New top-level area if the user base does government
  contracting; otherwise an overlay on `contracts` + `regulatory`. It is a
  hybrid — its own clause/compliance doctrine, but also a sector.
- **Starter skills:** `solicitation-review`; `clause-flowdown-review`;
  `compliance-obligation-tracker`; `bid-protest-triage`;
  `subcontract-flowdown-review`.
- **Unique safety restrictions:** bid-protest windows are extremely short —
  never compute, always flag; certifications carry false-claims exposure —
  escalation gate on any certification question; regime-specific.
- **Practice profile:** yes (if an area).
- **Cold-start interview:** yes, at `stable` (if an area).
- **Evals before stable:** yes.

### immigration — Tier 2 — Wave 3 (deadline-critical, individual-client)

- **Recommendation:** New top-level area — but only if the library extends to
  individual-client work (see the mission-fit note in Section 11).
- **Starter skills:** `visa-and-status-option-triage`; `petition-intake`;
  `document-checklist-builder`; `rfe-response-triage`;
  `status-and-deadline-tracker`.
- **Unique safety restrictions:** status expiry and filing deadlines are
  critical and consequences irreversible — never compute; eligibility is never
  asserted, only organized; country-specific; immigration consequences of
  criminal or other matters trigger escalation. `risk_level: high`.
- **Practice profile:** yes.
- **Cold-start interview:** yes, at `stable`.
- **Evals before stable:** yes — required before announcement.

### trusts-estates — Tier 2 — Wave 3 (individual-client)

- **Recommendation:** New top-level area, subject to the mission-fit decision.
- **Starter skills:** `estate-planning-intake`; `will-review`;
  `trust-document-review`; `estate-administration-checklist`;
  `fiduciary-duty-triage`.
- **Unique safety restrictions:** testamentary capacity and execution
  formalities are formal and intensely jurisdiction-specific — never confirm
  validity; individual clients may be elderly or vulnerable — capacity and
  undue-influence cautions; probate and tax deadlines flagged, never computed.
- **Practice profile:** yes.
- **Cold-start interview:** yes, at `stable`.
- **Evals before stable:** yes.

### family-law — Tier 2 — Wave 3 (lowest priority; mission-fit decision first)

- **Recommendation:** Defer pending a maintainer decision. It is the candidate
  furthest from the library's commercial / in-house lean, and the most
  sensitive. If adopted, it is a genuine new area.
- **Starter skills:** `family-law-intake`; `asset-and-debt-inventory`;
  `custody-factor-organizer`; `support-factor-organizer`;
  `separation-agreement-review`.
- **Unique safety restrictions:** emotionally sensitive matters with
  vulnerable parties; domestic-violence and child-safety indicators trigger an
  immediate escalation gate; never give relationship or strategic advice;
  conflicts-of-interest screening; jurisdiction-specific.
- **Practice profile:** yes.
- **Cold-start interview:** yes, at `stable`.
- **Evals before stable:** yes.

---

## 9. Candidate analysis — industry / regulatory overlays

These five candidates must **not** become top-level areas. Each is a sector
whose legal work spans existing practice areas. They are built with the
overlay mechanism from Section 4: a profile and a reference pack, not a skill
tree. Overlays do not get a cold-start interview skill (a fill-in profile
template is enough). Any genuinely sector-unique skill is hosted in the
relevant existing area, not in the overlay.

### healthcare-life-sciences — overlay

- **Recommendation:** Overlay over `privacy`, `contracts`, `regulatory`,
  `employment`, and `product-legal`.
- **Rationale:** A life-sciences company's legal work *is* contracts,
  privacy, regulatory, and employment work — colored by health-data
  sensitivity and sectoral regulation. A standalone area would clone those
  skills.
- **Sector-specific skills (only if needed, hosted in the parent area):**
  `clinical-trial-agreement-review` (in `contracts`);
  `business-associate-agreement-review` (in `privacy`);
  `regulatory-pathway-triage` (in `regulatory`).
- **Unique safety restrictions:** health data is high-sensitivity personal
  data; sectoral privacy/security regimes overlay general privacy law; never
  give a regulatory-pathway or clinical conclusion.
- **Practice profile:** an overlay profile.
- **Evals before stable:** yes for any sector-specific skills.

### fintech-payments — overlay

- **Recommendation:** Overlay over `financial-crime`, `regulatory`,
  `privacy`, and `contracts`.
- **Rationale:** AML/KYC is already in `financial-crime`; the rest of fintech
  work is regulatory, privacy, and contract work. The sector is an overlay.
- **Sector-specific skills (only if needed):**
  `payment-services-agreement-review` (in `contracts`);
  `money-transmission-licensing-triage` (in `regulatory`).
- **Unique safety restrictions:** licensing and money-transmission rules are
  jurisdiction-specific; never confirm licensing status or that an activity is
  exempt.
- **Practice profile:** an overlay profile.
- **Evals before stable:** yes for any sector-specific skills.

### environmental-energy-esg — split; start as one overlay, do not ship as one area

- **Recommendation:** Do **not** create a single `environmental-energy-esg`
  area — the name bundles three different things. Start as a single
  **environmental & ESG overlay** over `regulatory`, `corporate`, and
  `product-legal`. Revisit a standalone `environmental` Tier-2 area in a later
  wave only if demand is real. Treat "energy" as an industry overlay of its
  own if needed.
- **Sector-specific skills (only if needed):** `esg-disclosure-review`;
  `supply-chain-diligence-review` (hosted in `regulatory` or `corporate`).
- **Unique safety restrictions:** environmental and ESG-disclosure regimes are
  jurisdiction-specific and fast-moving; never assert a compliance conclusion.
- **Practice profile:** an overlay profile.
- **Evals before stable:** yes for any sector-specific skills.

### entertainment-media-sports — overlay

- **Recommendation:** Overlay over `contracts` and `ip`.
- **Rationale:** This sector is overwhelmingly contracts and IP/licensing
  work. A standalone area would duplicate both.
- **Sector-specific skills (only if needed):** `talent-agreement-review`;
  `rights-and-licensing-review`; `clearance-triage`;
  `name-image-likeness-review` (hosted in `contracts` or `ip`).
- **Unique safety restrictions:** rights chains and clearances are
  fact-specific — never confirm that rights are cleared; publicity/likeness
  law is jurisdiction-specific.
- **Practice profile:** an overlay profile.
- **Evals before stable:** yes for any sector-specific skills.

### education-law — overlay (low priority)

- **Recommendation:** Overlay over `employment`, `privacy` (student records),
  `regulatory`, and `contracts`. Low priority — likely a profile only, with no
  dedicated skills initially.
- **Unique safety restrictions:** student records are sensitive; minors are
  involved; sector-specific regimes overlay privacy and employment law.
- **Practice profile:** an overlay profile.
- **Evals before stable:** not applicable unless dedicated skills are added.

---

## 10. Recommended sequencing

Expansion is sequenced into waves so the repository is never destabilized.
Each wave fully completes (Section 6 definition of done) before the next
begins.

**Wave 0 — folds and overlay infrastructure (do first; lowest risk).**
No new top-level directories. (a) Fold `m-and-a` into `corporate`,
`consumer-protection` into `product-legal`, and `personal-injury` into
`litigation` by adding the sub-specialty skills listed in Section 7. (b) Build
the overlay infrastructure from Section 4: the `overlays/` convention, the
`OVERLAY.md` template, an overlay profile template, and the `validate_repo.py`
update. (c) Add `docs/PRACTICE_AREAS.md` (the tier/maturity registry). This
wave adds real value immediately and creates the anti-duplication machinery.

**Wave 1 — the first new top-level area: `real-estate`.** A clean,
document-centric, low-risk area used to exercise and prove the Section 6
process end to end.

**Wave 2 — the specialized, high-doctrine areas.** `tax`,
`bankruptcy-restructuring`, `securities-capital-markets`,
`antitrust-competition`, `government-contracts`, and `insurance` (coverage).
Sequence within the wave by user demand. Each is higher-risk; evals are
required before announcement, not merely before `stable`. Add overlays
(`healthcare-life-sciences`, `fintech-payments`,
`environmental & ESG`, `entertainment-media-sports`) on a parallel track once
Wave 0 infrastructure exists.

**Wave 3 — individual-client areas.** `immigration`, `trusts-estates`, and —
only on an explicit maintainer decision — `family-law`. These require the
mission-fit decision in Section 11 first.

Recommended count discipline: no more than two new top-level areas in flight
at once, and never a new area in the same release as a tooling or
infrastructure change.

---

## 11. Naming conventions, corrections, and the mission-fit question

- **`m-and-a`** — never created as a directory; folded into `corporate`.
  *(Superseded: `skills/m-and-a/` was created as a standalone top-level area —
  see Implementation status.)*
- **`securities-capital-markets`** — if created, use the shorter directory
  name `securities`; "capital markets" can be the display name. *(Superseded:
  the directory shipped under the long name `securities-capital-markets` —
  see Implementation status.)*
- **`environmental-energy-esg`** — do not ship as one directory. Split per
  Section 9.
- **`insurance`** — scope the directory to insurance *coverage*; document the
  boundary with the existing contract insurance-requirement content.
- **Directory names** stay lowercase and hyphenated to match the
  `practice_area` validation rule. Display names (with "&", capitalization)
  live in `README.md` and `SKILLS_INDEX.md` only.
- **Tier-4 labeling** — `README.md` and `SKILLS_INDEX.md` should explicitly
  mark `setup`, `legal-methodology`, and `legal-ops` as cross-cutting support,
  not practice areas, so counts stay honest.

**Mission-fit question (for maintainers).** AgentCounsel today leans toward
commercial and in-house legal work. `immigration`, `trusts-estates`,
`family-law`, and `personal-injury` are wholly or partly **individual-client**
practice. Adding them is reasonable, but it is a deliberate scope expansion
that brings new safety obligations (capacity, vulnerable parties,
unauthorized-practice exposure, conflicts). Decide this explicitly before
Wave 3, rather than letting it happen skill by skill. *(Superseded: the
decision was made in favor of covering individual-client work;
`core/capacity-and-vulnerable-parties.md` now carries the resulting
vulnerable-party safety obligations — see Implementation status.)*

---

## 12. Risks and anti-patterns to avoid

- **Sector-as-area duplication.** Creating `healthcare`, `fintech`, etc. as
  top-level areas, each with its own `contract-review` skill. The overlay
  mechanism exists to prevent exactly this.
- **Skeleton areas.** Merging an area with one skill and no profile, evals, or
  review, then leaving it. The maturity model and definition of done prevent
  this; an unfinished area stays `experimental` and visibly so.
- **Deadline computation creep.** Every deadline-sensitive new area (bankruptcy,
  immigration, government-contracts, securities, tax, real-estate, litigation)
  must inherit the core rule: deadlines are flagged, never computed.
- **Big-bang expansion.** Adding many areas at once. The wave model caps
  in-flight areas at two.
- **Taxonomy drift.** Areas added without a recorded tier. `docs/PRACTICE_AREAS.md`
  is the single source of truth for tier and maturity.
- **Individual-client safety gaps.** Treating individual-client areas like
  commercial ones. They need capacity, vulnerable-party, and
  unauthorized-practice language the commercial areas do not.

---

## 13. Summary table

| Candidate | Tier | Recommendation | Wave | Profile | Cold-start | Evals before stable |
|---|---|---|---|---|---|---|
| m-and-a | Core (sub-specialty) | Fold into `corporate` | 0 | Extend corporate | Extend corporate's | Yes (new skills) |
| consumer-protection | Advanced (sub-specialty) | Fold into `product-legal` | 0 | Extend product-legal | None new | Yes (new skills) |
| personal-injury | Core (sub-specialty) | Fold into `litigation` | 0 | Extend litigation | None new | Yes (new skills) |
| real-estate | Specialized | New top-level area | 1 | Yes | Yes (at stable) | Yes |
| insurance (coverage) | Specialized | New top-level area | 2 | Yes | Yes (at stable) | Yes |
| tax | Specialized | New top-level area (narrow) | 2 | Yes | Yes (at stable) | Yes (before announce) |
| bankruptcy-restructuring | Specialized | New top-level area | 2 | Yes | Yes (at stable) | Yes (before announce) |
| securities-capital-markets | Specialized | New top-level area | 2 | Yes | Yes (at stable) | Yes (before announce) |
| antitrust-competition | Specialized | New top-level area | 2 | Yes | Yes (at stable) | Yes |
| government-contracts | Specialized / hybrid | New top-level area, or overlay if low demand | 2 | Yes | Yes (at stable) | Yes |
| healthcare-life-sciences | Industry overlay | Overlay | 2+ | Overlay profile | No | Yes (sector skills) |
| fintech-payments | Industry overlay | Overlay | 2+ | Overlay profile | No | Yes (sector skills) |
| environmental-energy-esg | Mixed | Split; one overlay first; do not ship as one area | 2+ | Overlay profile | No | Yes (sector skills) |
| entertainment-media-sports | Industry overlay | Overlay | 2+ | Overlay profile | No | Yes (sector skills) |
| education-law | Industry overlay | Overlay (low priority) | 3+ | Overlay profile | No | N/A unless skills added |
| immigration | Specialized | New top-level area | 3 | Yes | Yes (at stable) | Yes (before announce) |
| trusts-estates | Specialized | New top-level area | 3 | Yes | Yes (at stable) | Yes |
| family-law | Specialized | Defer; maintainer decision, then new area | 3 | Yes | Yes (at stable) | Yes |

**Net effect on the taxonomy:** of the 18 candidates, 3 fold into existing
areas, 5 become overlays, and 10 become new top-level areas added across three
waves — never duplicating an existing skill, and never adding an area without
the resourcing the definition of done requires.

---

## 14. Open questions for maintainers

1. **Mission fit:** does AgentCounsel expand into individual-client practice
   (`immigration`, `trusts-estates`, `family-law`, plaintiff-side
   `personal-injury`)? This gates Wave 3.
2. **Overlay location:** a top-level `overlays/` directory (recommended) or
   `practice-profiles/overlays/`?
3. **Maturity tracking:** the `docs/PRACTICE_AREAS.md` registry alone
   (recommended first step), or also an area-level `status` field in skill
   frontmatter?
4. **Demand signal:** which Wave 2 specialized areas does the user base
   actually need first? That ordering is a product decision, not a structural
   one.
5. **Government contracts:** area or overlay? Decide based on how central
   government contracting is to the intended users.
