# Plugin Bundle Sync

The Claude Code plugin adapter (`adapters/claude-code-plugin/`) ships a curated starter bundle of AgentCounsel skills. That bundle is **generated** from the canonical library — it is not maintained by hand.

## `/skills` is canonical

The `/skills` directory is the single source of truth for every AgentCounsel skill. The plugin bundle under `adapters/claude-code-plugin/skills/` contains **generated copies** of a curated subset.

Do not edit the plugin copies directly. Edit the canonical skill under `/skills`, then regenerate the bundle with the sync script.

## The curated bundle

`scripts/sync_plugin_skills.py` copies these eight skills — and their templates — from `/skills` into the plugin bundle:

- `legal-research-memo`
- `nda-review`
- `contract-risk-review`
- `demand-letter`
- `litigation-chronology`
- `termination-risk`
- `dpa-review`
- `ai-use-case-intake`

The curated list lives in `scripts/sync_plugin_skills.py` as `CURATED_BUNDLE`. To add or remove a bundled skill, edit that list and re-run the script.

### `legal-core` is hand-maintained

One additional plugin skill, **`legal-core`**, is **not** generated from `/skills`. It is a summary of the `/core` operating rules, maintained by hand. The sync script preserves it and never overwrites it.

If you change the `/core` rules, update `adapters/claude-code-plugin/skills/legal-core/SKILL.md` by hand to keep it accurate.

## Templates

Where a curated skill has a `templates/` folder, the sync script copies the template files into the plugin skill's own `templates/` folder, so the bundle is self-contained and the relative `templates/...` references in each `SKILL.md` resolve. (`ai-use-case-intake` has no template.)

## Running the sync

```
python scripts/sync_plugin_skills.py
```

The script uses the Python standard library only. It is idempotent: it writes only the files that are missing or out of date, removes plugin files that no longer exist in canonical, preserves `legal-core`, and prints exactly what changed.

## When to run it

- After editing any canonical skill in the curated bundle, or any of its templates.
- Before any release or packaging of the Claude Code plugin bundle.
- Whenever `python scripts/validate_repo.py` reports plugin bundle drift.

## Drift detection

`scripts/validate_repo.py` checks the plugin bundle on every run and fails if:

- an expected plugin skill is missing (the eight curated skills, plus `legal-core`); or
- a curated plugin skill — its `SKILL.md` or any template — does not match its canonical source in `/skills`.

When the validator reports drift, run `python scripts/sync_plugin_skills.py` and commit the result. See `VALIDATION.md`.

## Known limitations

- `legal-core` is hand-maintained, not generated; the sync script cannot detect whether it has fallen behind `/core`. Review it manually when `/core` changes.
- The sync script manages only the curated skill folders. It does not remove an unexpected extra folder placed in the plugin `skills/` directory; the validator reports such a folder as a warning.
