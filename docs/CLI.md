# CLI reference

AgentCounsel ships a small set of helper scripts. They are **Python standard
library only** (run with `py` on Windows or `python3` elsewhere) plus one Node
script for the static site. There are no third-party dependencies, no network
calls, and no API keys. The canonical source of truth is always `skills/` and
`core/`; most scripts either **validate** the repository or **regenerate** a
derived artifact from the canonical files.

> Convention: scripts that generate a file usually also accept `--check`, which
> regenerates in memory and compares against what is committed — exiting non-zero
> if they differ, without writing. CI uses the `--check` forms so a stale
> generated file fails the build.

## Quick map

| Script | Mutates files? | Key flags |
|---|---|---|
| `scripts/validate_repo.py` | No | — |
| `scripts/build_skill_index.py` | Yes (writes metadata) | `--check` |
| `scripts/build_platform_packs.py` | Yes (writes `dist/`, `metadata/packs.json`) | `--check` |
| `scripts/check_evals.py` | No | — |
| `scripts/run_evals.py` | No | `--strict`, `--quiet`, `--markdown-report`, `<slug>` |
| `scripts/generate_eval_report.py` | Yes (writes report) | `--check` |
| `scripts/sync_plugin_skills.py` | Yes (writes plugin bundle) | `--check` |
| `scripts/generate_skill_improvement_prompts.py` | Yes (writes reports) | `--check` |
| `scripts/generate_cold_start_interviews.py` | Yes (writes setup skills) | `--check`, `--list` |
| `scripts/init_matter_workspace.py` | Yes (writes a new matter under `matters/`) | `--practice-area`, `--jurisdiction`, `--pack`, `--output-dir`, `--force`, `--dry-run`, `--list-templates` |
| `site/generate.mjs` | Yes (writes `site/public/`) | — |

---

## scripts/validate_repo.py

**Purpose.** Full structural and consistency validation: every skill's frontmatter
and eight required sections, relative-link resolution, safety framing, index
coverage, generated-metadata freshness, pack-registry integrity, and the
matter-workspace / playbook / review-panel integrity checks.

**Example.** `py scripts/validate_repo.py`

**Mutates files?** No. Read-only.

**Common failure modes.** A new skill missing a required section; a broken
relative link; a generated file (`metadata/index.json`, `router.json`,
`packs.json`) out of date — re-run the matching builder; a playbook/review-panel
missing a required section; a workspace template file missing.

---

## scripts/build_skill_index.py

**Purpose.** Regenerate `metadata/index.json` and `metadata/router.json` from the
canonical skills' frontmatter.

**Example.** `py scripts/build_skill_index.py` (write) · `py scripts/build_skill_index.py --check` (verify only)

**Mutates files?** Yes, without `--check`.

**Common failure modes.** `--check` reports "out of date" after you edit a skill's
frontmatter — re-run without `--check` and commit the regenerated metadata.
Invalid frontmatter (unknown quality check, bad risk level) blocks the build.

---

## scripts/build_platform_packs.py

**Purpose.** Regenerate the per-platform packs in `dist/` and the pack manifest
`metadata/packs.json`, discovering each area's skills, templates, quality checks,
matter packs, matter workspaces, playbooks, and review panels.

**Example.** `py scripts/build_platform_packs.py` · `py scripts/build_platform_packs.py --check`

**Mutates files?** Yes, without `--check`.

**Common failure modes.** A pack references a file that does not exist (the
builder validates every path); `metadata/packs.json` stale after a skill or
playbook change — rebuild.

---

## scripts/check_evals.py

**Purpose.** Schema-validate every `*.eval.yaml` under `evals/` (skill, router,
benchmark, and static evals) and run the deterministic metadata-integrity checks.

**Example.** `py scripts/check_evals.py`

**Mutates files?** No.

**Common failure modes.** A new eval file with a missing required key, a
`skill`/filename mismatch, an `expected_primary_skill` that is not a real skill
ID, or an invalid `eval_status`.

---

## scripts/run_evals.py

**Purpose.** Static, non-LLM heuristic runner that scores candidate skill outputs
in `evals/outputs/<slug>/<case-id>.md` against the shared safety assertions. It
does **not** call any model and does **not** judge legal correctness.

**Example.** `py scripts/run_evals.py --strict --quiet` · `py scripts/run_evals.py contracts/nda-review`

**Mutates files?** No.

**Flags.** `<slug>` runs one skill; `--strict` requires every case under the
required slugs to have a passing candidate; `--quiet` prints only the rollup;
`--markdown-report` emits a Markdown summary.

**Common failure modes.** `--strict` fails when a required candidate output is
missing or an assertion regex does not match.

---

## scripts/generate_eval_report.py

**Purpose.** Regenerate `reports/eval-coverage.md` from the eval files and
metadata.

**Example.** `py scripts/generate_eval_report.py` · `py scripts/generate_eval_report.py --check`

**Mutates files?** Yes, without `--check`.

**Common failure modes.** `--check` reports the report is out of date after you
add or change eval cases — regenerate and commit.

---

## scripts/sync_plugin_skills.py

**Purpose.** Regenerate the Claude Code plugin bundle under
`adapters/claude-code-plugin/skills/` from the canonical skills it curates.

**Example.** `py scripts/sync_plugin_skills.py` · `py scripts/sync_plugin_skills.py --check`

**Mutates files?** Yes, without `--check`.

**Common failure modes.** `--check` reports the bundle is out of sync after you
edit a bundled skill — re-run to resync. See `PLUGIN_SYNC.md`.

---

## scripts/generate_skill_improvement_prompts.py

**Purpose.** Regenerate `reports/skill-improvement-prompts.md` and
`reports/skill-quality-checklist.md`.

**Example.** `py scripts/generate_skill_improvement_prompts.py --check`

**Mutates files?** Yes, without `--check`.

**Common failure modes.** Reports out of date after skills change — regenerate.

---

## scripts/generate_cold_start_interviews.py

**Purpose.** Regenerate the 14 generated cold-start interview skills under
`skills/setup/` from the embedded per-area question banks. The four
hand-authored interviews are off-limits to the generator.

**Example.** `py scripts/generate_cold_start_interviews.py --check` · `py scripts/generate_cold_start_interviews.py --list`

**Mutates files?** Yes, without `--check`. `--list` only lists, `--check` only verifies.

**Common failure modes.** `--check` reports drift after the data block changes —
regenerate and commit.

---

## scripts/init_matter_workspace.py

**Purpose.** Create a new matter workspace from the canonical multi-file template
(`matter-workspaces/_template/`) under `matters/` (which is git-ignored).

**Example.** `py scripts/init_matter_workspace.py "Contoso MSA Review" --practice-area contracts --jurisdiction "New York"`

**Mutates files?** Yes — creates a new workspace directory. Refuses to overwrite an
existing one unless `--force`.

**Flags.** `--practice-area`, `--jurisdiction`, `--pack <matter-pack path>`,
`--output-dir`, `--force`, `--dry-run` (show what would be created, write
nothing), `--list-templates` (list the template and known practice areas).

**Common failure modes.** Destination already exists without `--force`; the
template directory is missing. See `docs/MATTER_WORKSPACES.md`.

---

## site/generate.mjs

**Purpose.** Generate the static HTML catalog into `site/public/` from `skills/`,
the examples, and the generated metadata.

**Example.** `node site/generate.mjs`

**Mutates files?** Yes — rewrites `site/public/` (preserving a pre-existing
`site/public/packs/` that CI populates from `dist/`). `site/public/` is
git-ignored.

**Common failure modes.** Run after regenerating `metadata/` so the site reflects
current skills, packs, and quality checks.

---

See `docs/AGENT_COMMANDS.md` for the recommended order to run these after editing
different parts of the repository, and `VALIDATION.md` for the full list of
checks `validate_repo.py` performs.
