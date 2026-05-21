# AgentCounsel — Static Skill Catalog

A static, browser-readable catalog of the AgentCounsel skill library. It is
generated from the canonical `skills/` directory so humans and browser-based
LLM agents can read, navigate, and copy from the library without a checkout.

The generator has **no runtime dependencies** — it is a single Node script
that uses the standard library only. This keeps the catalog consistent with
AgentCounsel's no-build-system, Markdown-first philosophy. There is no
backend, no login, and no browser extension.

## Build and preview

From this `site/` directory:

```
npm run build      generate the static site into site/public/
npm run serve      preview it at http://localhost:8080
npm run dev        build, then serve
```

`npm install` is not required — there are no dependencies to install.

## What it generates

Everything is written to `site/public/`:

- `index.html` — homepage: what AgentCounsel is, the attorney-review model, and quick links.
- `skill-index.html` — every skill in one list, grouped by practice area.
- `practice-areas/` — one page per practice area, listing its skills.
- `skills/<area>/<skill>.html` — one page per skill: the agent trigger description, all eight `SKILL.md` sections, the full raw `SKILL.md`, and **Copy Full Skill** / **Copy One-Off Prompt** buttons.
- `platforms/` — setup guides for ChatGPT Projects, Claude Projects, Gemini Notebooks, Codex / repo agents, and one-off prompt use.
- `llms.txt` and `llms-full.txt` — machine-readable summaries for LLM agents.
- `style.css` and `app.js` — one stylesheet and a small copy-to-clipboard script.

## Deploy

Serve the contents of `site/public/` with any static host — GitHub Pages,
Netlify, Vercel, an object store, or a plain file server. `llms.txt` is
written at the root of that directory so it is served at `/llms.txt`.

## Keeping it current

The catalog is generated, not hand-edited. After adding or changing a skill
under `skills/`, run `npm run build` again. Source files for the generator:

- `generate.mjs` — reads `skills/` and writes the site.
- `serve.mjs` — the local preview server.
- `assets/style.css`, `assets/app.js` — copied into the build output.
