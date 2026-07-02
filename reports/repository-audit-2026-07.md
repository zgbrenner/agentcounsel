# Repository Audit — July 2026

**Status:** Hand-maintained audit record. The "Addressed in this change" items landed
together with this report; the backlog in Section 5 is the recommended follow-up
sequence, in priority order.

**Scope:** the full library at the time of the audit — 191 skills across 23
directories under `skills/` (20 practice areas + 3 cross-cutting support groups),
plus every supporting layer (`core/`, `practice-profiles/`, `overlays/`,
`playbooks/`, `matter-packs/`, `review-panels/`, `matter-workspaces/`,
`connectors/`, `evals/`, `examples/`) and the index/documentation layer.

**Method:** four parallel review passes — (1) index/documentation consistency and
staleness, (2) skill quality in the 13 original practice areas, (3) skill quality
in the 9 newer areas plus `setup/`, (4) supporting-layer coverage — each
cross-checked against disk, followed by a synthesis and an implementation pass.
All three validation suites (`sync_plugin_skills.py --check`, `validate_repo.py`,
`check_evals.py`) passed before and after the changes.

---

## 1. Overall assessment

The library is in better shape than most of its documentation says it is. The
current-state index layer (`README.md`, `SKILLS_INDEX.md`, `WORKFLOW_ROUTER.md`,
`COMMANDS.md`, `metadata/index.json`, `docs/PRACTICE_AREAS.md`,
`reports/eval-coverage.md`) reconciled almost exactly with disk. Skill depth is
strong and safety discipline is largely uniform — genuinely thin skills are the
exception. The real problems were:

1. **Stale planning and standards documents** describing a 14-area, 66-skill
   repository and prescribing structure the repo has since contradicted.
2. **Undersized practice areas** — `financial-crime` (2 skills), `privacy` (4,
   with no breach-response workflow), `legal-ops` (3, with no intake/triage
   front door).
3. **Authoring-depth asymmetries** — a 2,150-line shared reference library in
   `contracts/` with nothing comparable elsewhere; six practice profiles that
   were stubs (one was 9 lines behind a 12-skill area); ten antitrust skills
   with byte-identical boilerplate headers; six skills missing the house
   citation-discipline rule.
4. **Structural safety gap** — the library ships individual-client areas
   (family-law, trusts-estates) but `core/` had no capacity / vulnerable-party
   operating rule; the guidance lived only in one practice profile.
5. **Supporting-layer lag** — router evals covered 8 of 23 directories; the
   deadline-critical and individual-client areas had no matter workspaces; three
   planned overlays and any securities-grade connector were missing.

## 2. What was addressed in this change

### Structural / safety

- **New core rule `core/capacity-and-vulnerable-parties.md`** — never assess
  capacity, undue influence, or abuse; immediate safety escalation; minors and
  unrepresented parties; no outcome predictions about people. Wired into
  `docs/SAFETY_MODEL.md`. This binds every skill, closing the biggest safety gap
  the audit found.
- **Boundary notes for the legal-methodology verification cluster** —
  `red-team-verifier`, `hallucination-red-team`, `citation-integrity-check`, and
  `source-validation` previously fired on the same triggers; each now states
  when to use it and when to use a sibling.
- **Safety-boilerplate standardization** — the bolded
  `core/source-and-citation-discipline.md` rule added to the six outliers (all
  four `product-legal` skills, `ai-governance/ai-use-case-intake`,
  `legal-methodology/hallucination-red-team`).

### Coverage — 7 new skills

- `financial-crime/transaction-monitoring-alert-triage` — fills the gap
  `kyc-onboarding-review` explicitly routed away.
- `financial-crime/aml-program-gap-review`
- `financial-crime/edd-file-review`
- `privacy/breach-response-workflow` — the most conspicuous single gap in the
  library; notification clocks are flagged, never computed.
- `privacy/cross-border-transfer-review`
- `privacy/vendor-privacy-diligence`
- `legal-ops/legal-intake-triage` — the legal front-door workflow.

Each ships with the standard eleven-field frontmatter, eight-section structure,
starter evals, and index/router/commands entries.

### Quality

- **Six practice profiles rewritten to the full template standard** (securities
  was a 9-line stub; antitrust, tax, bankruptcy, trusts-estates, insurance were
  thin scaffolds).
- **All 10 antitrust-competition skills de-boilerplated** — bespoke
  `description`, Purpose, and Use When per skill, plus skill-specific safety
  bullets (gun-jumping, algorithmic-pricing, cartel-indicator escalation).

### Supporting layers

- **Overlays:** `overlays/education-law/` and `overlays/environmental-esg/`
  (two of the three remaining planned overlays).
- **Connector:** `connectors/sec-edgar.md` for the securities/m-and-a/corporate
  verification surface.
- **Matter workspaces:** `bankruptcy-matter.md`, `family-law-matter.md`,
  `trusts-estates-matter.md` — the deadline-critical and individual-client
  areas, aligned with the new core rule.
- **Router evals:** extended from 14 cases / 8 areas to cover every practice
  area, plus cross-practice disambiguation cases.

### Documentation / staleness

- `reports/practice-area-expansion-plan.md` — re-labeled as substantially
  implemented, with an implementation-status table and superseded-passage
  annotations (the m-and-a fold, the `securities` naming, the insurance scope,
  the mission-fit question).
- `docs/SKILL_METADATA_STANDARD.md` — the seven missing practice areas added to
  the `practice_area` controlled list.
- `COMMANDS.md` cold-start count fix; `docs/PLATFORM_GAP_ANALYSIS.md` and
  `docs/IMPLEMENTATION_SEQUENCE.md` updated to reflect shipped work;
  `docs/PRACTICE_AREAS.md` release-name fix; `CONFIGURING.md` count fix;
  `practice-profiles/README.md` financial-crime contradiction fixed.

## 3. Verified healthy (no action needed)

- `README.md`, `SKILLS_INDEX.md`, `WORKFLOW_ROUTER.md` — all 191 pre-change
  skill paths present, zero dead entries, correct counts.
- `metadata/index.json` and the generated reports — in sync with disk.
- Eval coverage — every skill has an eval file; generated starter evals pull
  skill-specific content (not boilerplate); hand-authored evals (e.g.
  `nda-review`) are rich.
- Cold-start interviews — the per-area question banks are genuinely
  differentiated (39–41 area-specific questions each); the shared template
  around them is an intentional design.
- The m-and-a, real-estate, and deeper securities skills are at or near the
  `nda-review` gold standard; `legal-research` is among the strongest areas.
- `core/` deadline discipline is strong and consistent.

## 4. Divergences the library has accepted (now documented, not "wrong")

- `m-and-a` is a standalone top-level area rather than folded into `corporate`.
- The securities directory kept the long name `securities-capital-markets`.
- `insurance` shipped broader than the coverage-only scope the plan proposed.
- Individual-client practice (family-law, trusts-estates) is in scope; the
  safety obligations that come with it now live in
  `core/capacity-and-vulnerable-parties.md`.

## 5. Prioritized backlog (deferred — recommended order)

1. **Extend the shared reference-library model beyond `contracts/`.** Highest
   leverage in the repo. Build red-flag catalogs / negotiability-and-fallback
   references for the contract-review skills outside `contracts`
   (`ai-governance/ai-vendor-terms-review`, `privacy/dpa-review`,
   `product-legal/terms-of-service-review`, `employment/severance-review`), and
   grow the one-file `references/output-patterns.md` areas toward the
   six-file `contracts/references/` depth.
2. **Template extraction program.** Seven areas ship elaborate fixed output
   tables inline but zero `templates/` (ip, product-legal, ai-governance,
   regulatory, financial-crime, legal-ops, legal-methodology); several other
   areas have intra-area holes (`litigation/matter-intake`,
   `contracts/redline-summary`, `employment/severance-review`,
   `legal-research/case-brief`).
3. **Deepen the Tier-B workflows.** Bankruptcy and tax skills name the right
   concepts but collapse the analysis into single workflow bullets (e.g.
   `cash-collateral-dip-financing-issue-spotter` step 4,
   `tax-covenants-indemnities-review` step 3); explode them to the per-topic
   granularity of `m-and-a/purchase-agreement-issue-list`.
4. **"Explicitly carved-out sibling" skills.** Gaps that existing skills
   already point at: shareholder/member-meeting minutes (corporate),
   RIF/WARN + OWBPA group termination and standalone restrictive-covenant
   review (employment), regulatory examination/inquiry response (regulatory),
   citator / negative-treatment check (legal-research), discovery
   request/response and motion-opposition (litigation).
5. **Round out the newer areas:** real-estate loan/financing-document review
   (the clearest true coverage gap in the newer areas),
   securities equity-incentive-plan review, m-and-a R&W-insurance review.
6. **Differentiate the family-law review skills** with a shared
   `family-law/references/` issue catalog; add `real-estate/references/`.
7. **More connectors:** PACER/RECAP (litigation, bankruptcy), USPTO
   (the ip cluster), state-court/state-register aggregators.
8. **Examples for flagship older skills** (employment `termination-risk`,
   corporate `board-minutes`, ip `claim-chart`, regulatory
   `rule-change-summary`, legal-research `legal-research-memo`) — seven areas
   have no sample output.
9. **Individual-client / capacity review panel** pairing with the new core
   rule; a bankruptcy deadline-lens panel.
10. **Level the legal-methodology depth split** (seven ~100-line QC skills vs.
    four ~200-line siblings) or document the lean profile as intentional; and
    consider an orchestration entry (playbook or matter-pack) for the four
    areas that have neither (ip, ai-governance, product-legal — financial-crime
    gains skills in this change but still lacks a playbook).
11. **Benchmark eval expansion** — 13 areas have zero benchmark cases.
12. **Remaining expansion-plan items:** entertainment-media-sports overlay;
    government-contracts and immigration as candidate areas (run them through
    the plan's placement framework first).
13. **Maturity promotions:** the nine `experimental` areas mostly meet the
    definition of done except subject-matter-expert review (and, until this
    change, matter workspaces); decide promotion criteria and promote
    deliberately.

## 6. Maintenance notes

- The audit confirmed `validate_repo.py` derives `practice_area` from directory
  names, so the controlled list in `docs/SKILL_METADATA_STANDARD.md` can drift
  silently — consider a validator check that the doc lists every area.
- `reports/` mixes generated and hand-maintained files; each hand-maintained
  file (this one, the expansion plan) should carry an explicit status banner so
  staleness is visible, as both now do.
