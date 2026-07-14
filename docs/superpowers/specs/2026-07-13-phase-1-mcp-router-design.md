# Phase 1 MCP Router and Repository Metrics Design

## Status

Approved for implementation on July 13, 2026 through the user's instruction to start Phase 1.

## Goal

Make AgentCounsel's existing MCP surface and maintainer reports use the canonical generated metadata, produce reliable and compact routing results, and expose measurable context and skill-readiness signals without changing any canonical legal skill body.

## Scope

This change implements the first Phase 1 slice:

1. Replace the MCP server's independent parser and full-text frequency router with a standard-library service that consumes `metadata/index.json` and `metadata/router.json`.
2. Use stable skill IDs (`<practice-area>/<slug>`) across MCP tools.
3. Return structured routing results with confidence, alternatives, missing inputs, gates, quality checks, and escalation signals.
4. Add unit tests and CI coverage for the MCP service.
5. Generate per-skill and per-pack context-size metrics.
6. Generate a per-skill maintainability/readiness scorecard that does not claim legal correctness.
7. Remove stale hardcoded skill counts and stale comments encountered in the touched surfaces.

## Non-goals

- Do not edit the substance of any file under `skills/`.
- Do not add model calls, embeddings, a vector database, or network search.
- Do not make the MCP runtime responsible for legal conclusions.
- Do not calculate legal deadlines.
- Do not replace Markdown as AgentCounsel's canonical source of truth.
- Do not add a second hand-maintained router.

## Architecture

### Pure service layer

Create `agentcounsel_mcp.py`, a standard-library-only module that can be imported and tested without installing the MCP package. `CatalogService` loads generated metadata once, validates required top-level shapes, and serves compact skill records, weighted search, exact retrieval, and structured routing.

The service reads canonical generated artifacts rather than reparsing YAML frontmatter. It reads a skill body only when full content is explicitly requested.

### Thin MCP adapter

Keep `mcp_server.py` as the FastMCP transport adapter. Each MCP tool delegates to one `CatalogService` instance. The adapter contains no independent routing or parsing logic.

### Routing

Search weighting favors fields designed for discovery:

1. Stable ID and exact title match.
2. Description and `use_when` triggers.
3. Tags, practice area, required inputs, and expected outputs.
4. Skill body is not part of default ranking, preventing repeated safety boilerplate from distorting results.

`route_task` returns:

- primary route;
- confidence and score;
- alternative routes;
- reason for selection;
- required inputs that must be gathered;
- jurisdiction, deadline, and attorney-review gates;
- recommended quality checks;
- escalation requirement derived from risk;
- route type, including workspace routing when canonical workspace triggers are present.

When nothing matches, it returns `status: no_match` instead of inventing a route.

### Context metrics

Create `scripts/generate_context_metrics.py` to generate:

- `metadata/context_metrics.json`;
- `reports/context-metrics.md`.

Metrics use a deterministic approximation of one token per four characters and include characters, estimated tokens, output-section count, reference/template link count, and pack aggregate size. These metrics are planning signals, not provider billing measurements.

### Skill health scorecard

Create `scripts/generate_skill_health_report.py` to generate:

- `metadata/skill_health.json`;
- `reports/skill-health.md`.

The report measures repository readiness signals only: eval-case depth, scored candidate status, example coverage, template coverage, routing metadata, and context-size pressure. It must prominently state that it does not measure legal correctness or attorney approval.

## Error handling

- Missing or malformed generated metadata raises a descriptive `CatalogLoadError` during service creation.
- Invalid limits and empty queries raise `ValueError`.
- Unknown stable IDs raise `KeyError`.
- Generators support `--check` and exit nonzero on drift.
- Generated reports contain no client information and make no legal-quality claims.

## Testing

Use standard-library `unittest` and temporary fixture repositories.

Required tests:

- metadata is loaded once and list-valued fields remain intact;
- stable IDs are returned;
- trigger-rich metadata outranks body boilerplate;
- exact title and ID matches rank first;
- practice-area filtering works;
- structured routing contains missing inputs, quality checks, gates, alternatives, and escalation;
- no-match behavior is explicit;
- full content is omitted from compact cards;
- context metrics are deterministic;
- health-report signals are generated without legal-correctness claims;
- `--check` drift behavior is covered through generator functions.

## Compatibility

Existing MCP tool names remain available. `get_skill` accepts stable IDs, folder slugs, titles, and canonical paths for backward compatibility, but all returned records use stable IDs. A new `get_skill_card` tool provides compact retrieval.
