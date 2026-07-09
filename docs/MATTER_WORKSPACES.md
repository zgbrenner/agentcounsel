# Matter Workspaces

A **matter workspace** is a Markdown-native scaffold for organizing one legal
matter across multiple skills, documents, deadlines, sources, and review passes —
with no database, backend, login, or vendor dependency. A populated workspace is
**draft legal work product for attorney review**, not legal advice, and may be
privileged.

## Two formats

| Format | Location | Best for |
|---|---|---|
| Single-file workspace | `matter-workspaces/*-matter.md` | A focused matter handled in one or two sittings; quick to open and read. |
| Canonical multi-file template | `matter-workspaces/_template/` | A multi-step, document-heavy, source/citation-intensive, or long-running matter where facts, sources, assumptions, tasks, outputs, and quality checks each deserve their own tracked file. |

Pick the one that fits the matter. Do not maintain both for the same matter.

## When to use a workspace instead of a single skill

Create a workspace first when the task is any of:

- **multi-step** — it spans several skills;
- **document-heavy** — multiple source documents to track;
- **high-risk** — errors carry serious consequences;
- **ongoing** — it persists across sessions or weeks;
- **jurisdiction-sensitive** — governing law materially shapes the work;
- **deadline-sensitive** — one or more dates must be tracked and attorney-verified;
- **source/citation-heavy** — many statements must be traced to sources;
- likely to require **multiple quality checks**; or
- likely to require **attorney escalation**.

For a single, self-contained task (one document, one draft output), skip the
workspace and run the skill directly.

## The multi-file template

`matter-workspaces/_template/` contains:

```
matter_profile.md      Matter header: parties, jurisdiction, deadlines, posture,
                       privilege status, practice profile/pack/playbook, escalation triggers
facts.md               Established facts and disputed facts, each labeled by source
open_questions.md      Unresolved questions blocking or shaping the analysis
documents/             Source documents and a documents index
source_log.md          Every source consulted, with quality-layer classification
citation_map.md        Each drafted statement mapped to its supporting source
unsupported_claims.md  Statements with no adequate source — must be resolved
assumptions.md         Working assumptions and the effect if each is wrong
tasks.md               Open action items, owners, and verification status
skills_used.md         Which AgentCounsel skills were run, when, and on what
outputs/               Draft deliverables produced by skills
quality_checks/        Records of quality-layer passes run on the outputs
attorney_review.md     The attorney sign-off gate for the whole matter
matter_status.md       Current status, next steps, and a change log
```

`source_log.md`, `citation_map.md`, `unsupported_claims.md`, and `assumptions.md`
use the exact quality-layer classification vocabulary (see `docs/QUALITY_LAYER.md`
and `docs/SOURCE_VALIDATION.md`) so a quality pass maps cleanly onto the
workspace. These templates organize and label sources; they do **not** perform
automated legal verification. Verifying every authority and deadline remains an
attorney task.

## Initializing a workspace

**Script (recommended):**

```
python scripts/init_matter_workspace.py "Contoso MSA Review" --practice-area contracts
```

Options: `--jurisdiction`, `--pack matter-packs/m-and-a.md`, `--output-dir`,
`--force` (overwrite), `--dry-run`, `--list-templates`. The script copies the
template into a new, safely named directory under `matters/` (git-ignored),
seeds `matter_profile.md` with the matter name, practice area, jurisdiction, and
a next-steps block. It runs with the Python standard library only — no network,
no paid APIs.

**Manual:** copy `matter-workspaces/_template/` to a new location (for example
`matters/2026-contoso-msa-review/`) and work through the files in the order
listed in the template's `README.md`. Never edit the files inside `_template/`
itself — they are the reusable blank scaffold.

**The setup skill:** `skills/setup/create-matter-workspace/SKILL.md` recommends a
template for a matter and produces a populated draft.

## Relationship to other surfaces

- **Skills** produce the individual deliverables indexed in `skills_used.md`.
- **Playbooks** (`playbooks/`) are recipes for a recurring task type; a workspace
  records the outputs of running one.
- **Review panels** (`review-panels/`) run a draft through multiple supervised
  review passes; record the result in `quality_checks/`.
- **Matter packs** (`matter-packs/`) sequence skills for a matter type; a
  workspace organizes the outputs.
- **Practice profiles** (`practice-profiles/`) configure agent behavior; the
  workspace records which profile is in use.

See `WORKFLOW_ROUTER.md` for when to choose each surface.

## No backend, runtime, or vendor dependency

Every file is plain Markdown and works in any editor, AI assistant, or document
system. See `docs/LOCAL_PLATFORM_PATH.md` for the architecture-level path toward
a local or self-hosted matter-scoped experience built on this format.
