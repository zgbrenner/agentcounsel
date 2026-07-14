# AgentCounsel MCP Server

AgentCounsel can be exposed to MCP-compatible AI clients through the lightweight server in [`mcp_server.py`](../mcp_server.py).

The server keeps the Markdown skill library as the source of truth and uses the generated catalog in `metadata/index.json` and `metadata/router.json` for discovery. It does not duplicate each skill as an individual MCP tool. Instead, it provides a compact routing and retrieval interface so clients can identify the narrowest relevant workflow, gather its missing inputs, apply the required gates, and load the complete instructions only when needed.

The standard-library service in [`agentcounsel_mcp.py`](../agentcounsel_mcp.py) contains all catalog and routing logic. `mcp_server.py` is only the FastMCP transport adapter.

## Available tools

| Tool | Purpose |
|---|---|
| `list_practice_areas` | List practice areas and generated skill counts. |
| `search_skills` | Search compact skill cards using stable IDs, titles, descriptions, use-when triggers, tags, inputs, and outputs. |
| `route_legal_task` | Return a structured primary route, alternatives, confidence, missing inputs, gates, quality checks, and escalation signal. |
| `get_skill_card` | Retrieve compact metadata for one skill without loading the Markdown body. |
| `get_skill` | Retrieve the complete Markdown workflow for one skill. |
| `get_core_rules` | Retrieve AgentCounsel's global operating and legal-safety rules. |

The server also exposes the read-only resource `agentcounsel://catalog`, which contains a compact catalog of all available skills.

## Stable identifiers and compatibility

Canonical skill IDs use the generated `<practice-area>/<skill-slug>` format, such as `contracts/nda-review`. `get_skill` and `get_skill_card` also accept a unique folder slug, title, or canonical repository path for backward compatibility. Returned records always use the stable generated ID.

## Structured routing response

`route_legal_task` returns:

- `status`: `matched` or `no_match`;
- `route_type`: normally `one-off skill`, or `matter workspace` when canonical workspace triggers are present;
- `confidence`: `high`, `medium`, `low`, or `none`;
- `primary_route` and `alternative_routes` as compact skill cards;
- `why_selected` with the matched metadata fields and deterministic score;
- `missing_required_inputs` from the selected skill metadata;
- `mandatory_quality_checks` from the generated quality-check mapping;
- `gates` for jurisdiction, deadlines, and attorney review;
- `escalation_required`, derived conservatively from the skill's risk level.

The router uses metadata fields designed for discovery. It does not rank skills by counting repeated words in complete skill bodies, so common safety boilerplate cannot dominate task-specific routing signals.

## Legal-safety model

AgentCounsel supplies structured workflows for draft legal work product. It does not provide legal advice or create an attorney-client relationship. Outputs must be reviewed and adopted by a qualified licensed attorney before reliance. A routing confidence score measures metadata fit only; it does not measure legal correctness.

## Run locally

Requires Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python mcp_server.py
```

The remote Streamable HTTP MCP endpoint is served at:

```text
http://localhost:8000/mcp
```

Set `PORT` to use a different port.

## Manufact deployment settings

Use these settings when deploying the repository to Manufact Cloud:

```text
Repository: zgbrenner/agentcounsel
Branch: main
Build command: pip install -r requirements.txt
Start command: python mcp_server.py
Port: 8000
Region: US
```

The Manufact GitHub App must have access to the repository before the initial deployment can be created.

## Example client flow

1. Call `route_legal_task` with a task such as `Review a mutual NDA for a software vendor relationship`.
2. Inspect the primary route, alternatives, missing inputs, gates, and quality checks.
3. Call `get_skill_card` when only compact metadata is needed.
4. Call `get_skill` with the returned stable skill ID when the full workflow is required.
5. Follow the skill's required-input, workflow, output-format, and attorney-verification sections.
6. Use `get_core_rules` when the client has not already loaded AgentCounsel's global safety rules.
