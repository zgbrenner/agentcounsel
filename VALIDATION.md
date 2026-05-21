# Repository Validation

AgentCounsel ships a lightweight validation script, `scripts/validate_repo.py`, that checks the repository for structural and consistency problems. It uses only the Python standard library — no dependencies, no package manager, no build tooling.

## Running it

```
python scripts/validate_repo.py
```

Run it from anywhere; the script locates the repository root relative to its own location. It prints a report and exits with status `0` if all checks pass, or `1` if any error is found. Warnings are advisory and do not affect the exit code.

## What it checks

**Structure**

- The directories the library is organized around exist: `core/`, `skills/`, `adapters/`, `practice-profiles/`, `matter-workspaces/`, `skills/setup/`, `skills/legal-methodology/`, and `skills/contracts/references/`.
- Every canonical skill folder under `skills/` contains a `SKILL.md`. A `references/` folder under a practice area is treated as shared reference material, not a skill.
- Every plugin skill folder under `adapters/claude-code-plugin/skills/` contains a `SKILL.md`.
- Every `SKILL.md` has valid YAML frontmatter (an opening and a closing `---`).
- Every `SKILL.md` frontmatter has a non-empty `name` and `description`.
- Every `SKILL.md` has an H1 title.
- Every canonical skill under `skills/` contains all eight required sections, in order: Purpose, Use When, Required Inputs, Do Not Use When, Legal Safety Rules, Workflow, Output Format, Attorney Verification Checklist.

**Safety and content**

- No file describes AgentCounsel as providing legal advice. Outputs must be described as draft legal work product for attorney review.
- Every `SKILL.md` references the source/citation discipline core rule (`core/source-and-citation-discipline.md`) or carries equivalent language against inventing legal authority or citations.
- No file contains the forbidden framing that this project is a ChatGPT Project instructions or package repository.
- No substantive file contains a leftover placeholder marker (such as a TODO or FIXME note, or lorem ipsum filler text).

**Links and paths**

- Every relative Markdown link resolves to a file that exists.
- Every skill path referenced in `SKILLS_INDEX.md`, `WORKFLOW_ROUTER.md`, and `COMMANDS.md` points to a real `SKILL.md`.
- Adapter index files point back to the canonical root files.
- `adapters/claude-code-plugin/plugin.json` is valid JSON and has `name`, `version`, and `description`.

**Plugin bundle**

- Every expected plugin skill is present — the eight curated skills plus the hand-maintained `legal-core`.
- Each curated plugin skill under `adapters/claude-code-plugin/skills/` matches its canonical source in `/skills`, including templates. If they differ, the validator reports drift; run `python scripts/sync_plugin_skills.py` to regenerate the bundle. See `PLUGIN_SYNC.md`.

**Warnings (advisory)**

- A canonical skill that is not listed in `SKILLS_INDEX.md`.
- An index file with no skill paths to validate.
- A plugin skill folder that is not part of the curated bundle or the maintained set.

## What it does not check

The script validates structure and consistency — not legal accuracy. It cannot tell whether a skill's workflow is sound, whether its content is correct, or whether its legal framing is appropriate for a given matter. Substantive review by a qualified, licensed legal professional, together with each skill's Attorney Verification Checklist, remains essential. See `CONTRIBUTING.md` and the `core/` operating rules.

## When to run it

- Before opening or updating a pull request.
- After adding, renaming, or moving a skill, template, or adapter file.
- After editing `SKILLS_INDEX.md` or `WORKFLOW_ROUTER.md`.
- After running `python scripts/sync_plugin_skills.py` to regenerate the plugin bundle (see `PLUGIN_SYNC.md`).

## Note

`scripts/validate_repo.py` and this file (`VALIDATION.md`) are excluded from the forbidden-phrase scans, because they necessarily describe the phrases being checked for.

Generated build output is not validated as repository source: the scan skips `dist/` (platform install packs from `scripts/build_platform_packs.py`) and `node_modules/`. `scripts/build_platform_packs.py` performs its own build-time validation of the packs it generates.
