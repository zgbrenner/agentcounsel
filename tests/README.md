# tests/

Unit tests for the repository's Python tooling under `scripts/`. Standard
library only (`unittest`) — no third-party packages, no network, consistent
with the rest of the tooling.

Run from the repository root:

```
python -m unittest discover -s tests
```

CI runs the same command in `.github/workflows/validate.yml`.

## Scope

These tests cover the **pure, shared functions** that the validation and build
scripts depend on — currently `scripts/_shared.py`: the SKILL.md frontmatter
parser (in its three return shapes), the restricted eval-YAML parser, and the
schema constants (`REQUIRED_SECTIONS`, `REQUIRED_FIELDS`). A change that
silently altered how skills are parsed would break these tests.

This is a starter harness focused on the highest-value, lowest-coupling
targets. Add a `test_<module>.py` per script as more pure logic is extracted
into testable functions.
