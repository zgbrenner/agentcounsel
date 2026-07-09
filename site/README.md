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
npm run build      generate the static site into site/public/ (gitignored)
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

## Search

The home page and the skill index embed a [Pagefind](https://pagefind.app)
(MIT) search box (`<div id="search">`, `data-pagefind-body` scopes indexing to
each page's `<main>` so nav/footer boilerplate doesn't pollute results).
Pagefind's own assets (`pagefind/pagefind-ui.{css,js}`) are **not** produced by
`generate.mjs` — the deploy workflow indexes the built site with
`npx pagefind@1 --site site/public` after the `node site/generate.mjs` step.
In a local `npm run build` preview, those assets don't exist yet, so the
search box shows a muted fallback message instead of erroring; it only comes
alive on the deployed Pages site.

## Deploy

The site is built and deployed automatically by GitHub Actions on every
push to `main` — see `.github/workflows/deploy-pages.yml`, which builds the
site, then runs Pagefind over `site/public` to generate the search index
before uploading the Pages artifact. The generated `site/public/` directory
is gitignored; pull requests verify that the generator still runs cleanly but
do not deploy. `llms.txt` is written at the root of the output so it is
served at `/llms.txt`.

## Keeping it current

The catalog is generated, not hand-edited. After adding or changing a skill
under `skills/`, run `npm run build` again. Source files for the generator:

- `generate.mjs` — reads `skills/` and writes the site.
- `serve.mjs` — the local preview server (run after `npm run build`).
- `assets/style.css`, `assets/app.js` — copied into the build output.
