# Third-Party Notices

AgentCounsel itself is licensed under the MIT License (see `LICENSE`).

Some AgentCounsel skills incorporate legal-workflow ideas adapted from prior
open-source projects licensed under the Apache License, Version 2.0. Those
projects' license terms continue to apply to the material adapted from them,
and Apache-2.0 §4 requires that the following attributions be preserved in
derivative distributions:

- **agnostic-skills-for-legal** — https://github.com/foolish-bandit/agnostic-skills-for-legal
  (Apache-2.0)

  That project is itself derived from, and carries attribution to:

  - **claude-for-legal** — Anthropic — https://github.com/anthropics/claude-for-legal (Apache-2.0)
  - **claude-for-legal-web** — veronica-builds — https://github.com/veronica-builds/claude-for-legal-web (Apache-2.0)

- **financial-services** — Anthropic — https://github.com/anthropics/financial-services (Apache-2.0)

- **knowledge-work-plugins** — Anthropic — https://github.com/anthropics/knowledge-work-plugins (Apache-2.0)

AgentCounsel also adapts organizational taxonomies and template shapes from
the following CC-BY-4.0, BSD-2-Clause, and MIT/CC0 sources. In each case,
AgentCounsel reuses only category names, factual classifications, or a
lightweight document shape — never the source project's prose, dataset
examples, or template clause text, which are rewritten independently. See
`docs/OSS_BORROWING_MAP.md` for the reuse classification of each source.

- **CUAD (Contract Understanding Atticus Dataset)** — The Atticus Project —
  https://www.atticusprojectai.org/cuad
  License: CC-BY-4.0
  Material used: the dataset's contract clause category taxonomy (category
  names and grouping only)
  Affected AgentCounsel files: `skills/contracts/references/clause-category-checklist.md`
  Use type: adapted
  Notes: category names and taxonomy are reused; all one-line descriptions of
  what to check and why are independently written for AgentCounsel.

- **eyecite** — Free Law Project —
  https://github.com/freelawproject/eyecite
  License: BSD-2-Clause
  Material used: the library's citation-type classification scheme (full
  case citation, short-form, supra, id., statutory, regulation, law-journal,
  unknown/partial)
  Affected AgentCounsel files: `skills/legal-research/references/citation-type-taxonomy.md`
  Use type: adapted
  Notes: the classification categories are reused; descriptions of each
  type, verification needs, and hallucination-risk notes are independently
  written and are not eyecite's code, docstrings, or documentation text.

- **reporters-db and courts-db** — Free Law Project —
  https://github.com/freelawproject/reporters-db and
  https://github.com/freelawproject/courts-db
  License: BSD-2-Clause
  Material used: the fact that these datasets catalog case-law reporter
  abbreviations and court names/abbreviations, described as a verification
  resource
  Affected AgentCounsel files: `connectors/reporters-and-courts.md`,
  `connectors/README.md`
  Use type: adapted
  Notes: no dataset content is redistributed; the connector documents how a
  skill may consult the datasets, and describes their scope and limits in
  AgentCounsel's own words.

- **oneNDA, Bonterms, and Common Paper** — respective publishers of each
  open standard commercial agreement template
  License: CC-BY-4.0 (each project)
  Material used: a short, independently written description of each
  standard's scope, used solely as a labeled comparison baseline
  Affected AgentCounsel files: `skills/contracts/references/market-standard-baselines.md`
  Use type: adapted
  Notes: no template clause text is reproduced; descriptions are original
  and each standard is identified by name as the source of any baseline
  comparison.

- **MADR (Markdown Any Decision Records)** —
  https://github.com/adr/madr
  License: MIT / CC0-1.0
  Material used: the lightweight Status/Context/Decision/Consequences record
  shape
  Affected AgentCounsel files: `docs/decisions/README.md` and the records
  under `docs/decisions/`
  Use type: adapted
  Notes: AgentCounsel's records are a shortened, independently written
  adaptation of MADR's structure, not a copy of its template file or example
  content.

- **Federal Plain Language Guidelines** — plainlanguage.gov, a U.S. government
  interagency initiative —
  https://www.plainlanguage.gov/guidelines/
  License: U.S. government public domain / CC0
  Material used: sentence-level plain-language techniques, distilled into a
  checklist
  Affected AgentCounsel files: `skills/legal-methodology/references/plain-language-checklist.md`
  Use type: adapted
  Notes: rewritten in AgentCounsel's own words and explicitly scoped to
  client- and business-stakeholder-facing prose only, never to legal
  drafting itself; attribution is noted here though not legally required for
  public-domain material.

- **CISA Cybersecurity Tabletop Exercise Program (CTEP)** — Cybersecurity and
  Infrastructure Security Agency —
  https://www.cisa.gov/resources-tools/services/cybersecurity-tabletop-exercise-program-ctep
  License: U.S. government public domain
  Material used: the tabletop-exercise structure (a scenario walked through
  with mid-run "injects")
  Affected AgentCounsel files: `docs/tutorials/practice-matter.md`
  Use type: adapted
  Notes: only the exercise-structure concept is reused; the scenario, facts,
  and injects in the tutorial are original and fictional, and attribution is
  noted here though not legally required for public-domain material.

- **Citation File Format (CFF)** —
  https://citation-file-format.github.io/
  License: CC-BY-4.0 (specification)
  Material used: the `cff-version` schema and standard field names for
  software citation metadata
  Affected AgentCounsel files: `CITATION.cff`
  Use type: spec usage note
  Notes: only the public schema's field names and structure are used to
  describe this repository's own metadata; no specification prose is
  reproduced.

A further round of adaptations, evaluated against the sources recorded in
`docs/OSS_BORROWING_MAP.md`'s third round of evaluations, is attributed below.
As above, only category names, factual conventions, or a lightweight
structural shape are reused — never the source project's own prose, code, or
examples.

- **claude-for-legal** — Anthropic —
  https://github.com/anthropics/claude-for-legal
  License: Apache-2.0
  Material used: the provenance-tagging convention (labeling drafted content
  by where it came from)
  Affected AgentCounsel files: `skills/legal-methodology/references/citation-confidence-tiers.md`,
  `matter-workspaces/_template/documents/README.md` (Document Map provenance
  field)
  Use type: adapted
  Notes: this is a separate, additional borrow from the same project already
  noted in the Apache-2.0 lineage list above (via `agnostic-skills-for-legal`);
  only the tagging convention is reused, not any skill text, prompt, or
  installer logic.

- **agent-governance-toolkit** — Microsoft —
  https://github.com/microsoft/agent-governance-toolkit
  License: MIT
  Material used: the compliance-mapping shape (mapping a requirement to a
  control, a status, and an evidence pointer)
  Affected AgentCounsel files: `skills/regulatory/compliance-gap-matrix/SKILL.md`,
  `skills/regulatory/compliance-program-tracker/SKILL.md`
  Use type: adapted
  Notes: AgentCounsel's compliance gap matrix already organized requirements,
  controls, status, severity, remediation, and an attorney note as a shared
  organizing shape; this entry formally records that shape as also informed
  by this toolkit's convention. No governance-toolkit code, policy content, or
  automated-enforcement logic is used.

- **VectifyAI/PageIndex** — https://github.com/VectifyAI/PageIndex
  License: MIT
  Material used: the hierarchical tree-index idea — a per-document outline of
  sections and headings, used for navigation rather than requiring a full
  re-read of the source
  Affected AgentCounsel files: `matter-workspaces/_template/documents/README.md`
  (Document Map), `docs/MATTER_WORKSPACES.md`
  Use type: adapted

- **thedotmack/claude-mem** — https://github.com/thedotmack/claude-mem
  License: Apache-2.0
  Material used: the capture-compress-resurface session-memory lifecycle
  (record what happened, compress it to what matters, resurface it at the
  start of the next session)
  Affected AgentCounsel files: `matter-workspaces/_template/matter_status.md`
  (Session Notes), `docs/MATTER_WORKSPACES.md`
  Use type: adapted
  Notes: PageIndex and claude-mem are recorded together because both feed the
  same round of matter-workspace template additions — the Document Map (from
  PageIndex) and Session Notes (from claude-mem). Neither project's code,
  storage backend, or coding-agent-specific content is used; both conventions
  are translated to plain, append-only Markdown with no runtime, database, or
  automatic compression. Session Notes are explicitly labeled as drafting
  context for continuity between sessions, not work product — the Attorney
  Verification Checklist discipline applies to the outputs the notes
  reference, never to the notes themselves.

- **AnttiHero/lavern** — https://github.com/AnttiHero/lavern
  License: Apache-2.0
  Material used: the mechanical grounding-check step — sorting each claim
  into supported / needs-citation / unsupported before any other review
  proceeds
  Affected AgentCounsel files: `skills/legal-methodology/red-team-verifier/SKILL.md`
  (source-support audit step)
  Use type: adapted
  Notes: this is one specific, narrow borrow from lavern's broader review
  workflow; lavern's human-gate and evidence-backed-debate concepts more
  generally remain a use-later item in `docs/OSS_BORROWING_MAP.md` and are not
  otherwise adopted here. No lavern agent personas, prompts, or legal content
  are used.

AgentCounsel is an independent open-source project. It is not affiliated with,
endorsed by, or sponsored by Anthropic, OpenAI, or Google.
