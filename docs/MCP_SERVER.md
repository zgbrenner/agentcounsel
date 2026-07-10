# AgentCounsel MCP Server

AgentCounsel can be exposed to MCP-compatible AI clients through the lightweight server in [`mcp_server.py`](../mcp_server.py).

The server keeps the Markdown skill library as the source of truth. It does not duplicate the 209 skills as 209 individual MCP tools. Instead, it provides a small discovery and retrieval interface so clients can identify the narrowest relevant workflow and load its complete instructions only when needed.

## Available tools

| Tool | Purpose |
|---|---|
| `list_practice_areas` | List practice areas and skill counts. |
| `search_skills` | Search skills by task, keyword, title, description, practice area, or full content. |
| `route_legal_task` | Recommend the most relevant skills for a plain-language legal task. |
| `get_skill` | Retrieve the complete Markdown workflow for one skill. |
| `get_core_rules` | Retrieve AgentCounsel's global operating and legal-safety rules. |

The server also exposes the read-only resource `agentcounsel://catalog`, which contains a compact catalog of all available skills.

## Legal-safety model

AgentCounsel supplies structured workflows for draft legal work product. It does not provide legal advice or create an attorney-client relationship. Outputs must be reviewed and adopted by a qualified licensed attorney before reliance.

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
2. Select the narrowest recommended workflow.
3. Call `get_skill` with the returned skill ID or path.
4. Follow the skill's required-input, workflow, output-format, and attorney-verification sections.
5. Use `get_core_rules` when the client has not already loaded AgentCounsel's global safety rules.
