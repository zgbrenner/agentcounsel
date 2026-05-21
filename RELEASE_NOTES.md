# AgentCounsel v0.1.0 — First Public Release

**Release date:** 2026-05-21
**License:** Apache-2.0

AgentCounsel v0.1.0 is the first public release of an open, Markdown-native library of **legal skills** for AI agents and the legal professionals who supervise them. A skill is a structured workflow that helps an AI agent — or a lawyer — produce **draft legal work product for attorney review**.

> AgentCounsel does not provide legal advice. Every output is a draft that a qualified, licensed legal professional must review before it is relied upon. Using the library does not create an attorney–client relationship.

This document is the curated summary of the release. The granular development history is in [`CHANGELOG.md`](CHANGELOG.md).

## What's in the release

### A complete skill library

**66 skills** — 57 across **12 practice areas**, plus 9 cross-cutting skills in two supporting groups:

- **Legal Research** — structured, verifiable research memos.
- **Litigation** — matter intake, chronologies, demand letters, subpoena triage, deposition prep, legal holds, privilege-log review, claim charts, brief drafting.
- **Contracts** — NDA review, contract risk review, redline summaries, SOW review, vendor agreement status.
- **Corporate** — board minutes, written consents, closing checklists, diligence issue extraction, material-contract schedules, entity compliance.
- **Employment** — termination risk, worker classification, hiring review, wage-and-hour triage, internal investigations, protected leave, severance, policy review.
- **Privacy** — DPA review, data subject requests, privacy-policy gap review, privacy impact assessments.
- **Product Legal** — launch review, marketing-claims review, terms-of-service review, AI-feature review.
- **Regulatory** — enforcement-risk memos, rule-change summaries, compliance-gap matrices, compliance-program tracking.
- **AI Governance** — AI use-case intake, AI vendor terms review, model-risk triage, employee AI policy.
- **Intellectual Property** — trademark triage, infringement triage, cease-and-desist response, patent FTO triage, invention intake, DMCA, open-source licensing.
- **Financial Crime / AML** — KYC onboarding review, sanctions / PEP / adverse-media screening review.
- **Legal Operations** — templated legal responses, meeting briefings, signature routing.

Two cross-cutting groups support every practice area: **Setup** (cold-start interviews and a matter-workspace builder) and **Legal Methodology** (red-team verification, statutory interpretation, risk assessment, source validation).

Every skill follows the same structure — Purpose, Use When, Required Inputs, Do Not Use When, Legal Safety Rules, Workflow, Output Format, Attorney Verification Checklist — and carries standardized, agent-readable YAML frontmatter.

### A safety-first design

Every skill inherits the operating rules in [`core/`](core/): draft work product only, attorney review always required, never invent legal authority or deadlines, separate facts from analysis, preserve confidentiality, and flag uncertainty with visible placeholders. The full design is documented in [`docs/SAFETY_MODEL.md`](docs/SAFETY_MODEL.md).

### Works on every major surface

AgentCounsel is plain Markdown, so it runs anywhere an agent or person can read a file. The release includes adapters and build tooling for **ChatGPT, Claude, Gemini, Codex and other repo agents, Cursor**, and generic Markdown workflows. `scripts/build_platform_packs.py` generates ready-to-install packs per platform.

### Team configuration layers

Optional, plain-Markdown layers let a legal team adapt the library without changing any skill: **practice profiles** (`practice-profiles/`) capture a practice group's jurisdictions and standard positions, and **matter workspaces** (`matter-workspaces/`) organize a single matter end to end.

### Documentation and onboarding

This release adds a rewritten [`README.md`](README.md), a [`QUICKSTART.md`](QUICKSTART.md) walkthrough, a [`docs/FAQ.md`](docs/FAQ.md), a [`docs/SAFETY_MODEL.md`](docs/SAFETY_MODEL.md), and an [`examples/`](examples/) directory of illustrative sample outputs (with entirely fictional facts) for contract review, litigation chronology, DPA review, product launch review, and red-team verification.

### Quality tooling

- `scripts/validate_repo.py` — structural, metadata, link, and safety-framing validation (standard library only).
- `scripts/build_skill_index.py` — generates the machine-readable `metadata/index.json`.
- `scripts/sync_plugin_skills.py` — regenerates the Claude Code plugin bundle.
- `scripts/build_platform_packs.py` — generates per-platform install packs.
- A lightweight eval framework in `evals/`.
- GitHub Actions CI runs the full validation suite on every change.

## Getting started

1. Read [`QUICKSTART.md`](QUICKSTART.md) — your first skill run in about five minutes.
2. Skim [`README.md`](README.md) for what the library is and how it is organized.
3. Read [`docs/SAFETY_MODEL.md`](docs/SAFETY_MODEL.md) before using it on real work.
4. Browse [`examples/`](examples/) to see what a finished draft looks like.

## Known limitations

AgentCounsel is **pre-1.0**. Content and structure may still change between releases.

- Skills supply **process and structure, not the law of any jurisdiction**. You must supply current law and verify it.
- Skills do not compute or assert deadlines — they flag them for attorney verification.
- The validator checks structure and consistency, not legal accuracy.
- Every output is a draft. **Attorney review is mandatory and is not optional.**

## Reporting issues

Bugs and skill requests: open an issue using a template in `.github/ISSUE_TEMPLATE/`. Security or safety concerns: follow [`SECURITY.md`](SECURITY.md) — privately, and without confidential or real client data.

## License and attribution

Apache License 2.0 — see [`LICENSE`](LICENSE). AgentCounsel adapts legal-workflow ideas from prior Apache-2.0 open-source work; attribution is recorded in [`NOTICE`](NOTICE). AgentCounsel is an independent project and is not affiliated with, endorsed by, or sponsored by any AI vendor.
