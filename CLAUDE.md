# investment-research-notes

Personal investment research notes and tools for a personal portfolio. Mostly
markdown research notes organized by topic, plus one real Python project.

## Structure

- `investing-fundamentals/` — fundamental analysis notes and company analyses
- `investing-guidelines/` — personal investment rules and frameworks
- `investing-macro/` — macro research notes and scripts
- `investing-options/` — options strategy notes; `investing-options/scanner/` is
  a real Python package (see its own CLAUDE.md)
- `investing-quant/` — quantitative research notes
- `investing-real-estate/` — real estate research
- `investing-books/`, `reading-list/` — book notes
- `investing-crypto/` — crypto research notes
- `galactic-macro/` — macro framework notes
- `personal-finance/` — personal finance notes
- `trading/` — trading notes and interview transcripts
- `robotwealth/` — RobotWealth course notes and scripts

## Key distinction

Everything except `investing-options/scanner/` is notes/markdown. Only the
scanner has tests, a package structure, and code conventions worth enforcing.

## Wiki

WIKI_PATH for this project: /Users/howardwu/dev/investment-research-notes

This directory uses the hermes llm-wiki skill. At the start of any session,
orient by reading SCHEMA.md → index.md → last 20 lines of log.md before
ingesting, querying, or linting.

## Google Workspace Operations

For all Google Workspace related operations (including Gmail, Calendar, Docs, Sheets, etc.), **always use the GWS CLI (`gws`)** instead of Google Workspace MCP tools. The MCP tools require manual OAuth in the browser and produce excessively verbose output. 

Use GWS CLI commands within an unsandboxed shell via `run_command` by passing the active profile's token via `GOOGLE_WORKSPACE_CLI_TOKEN` and pointing `GOOGLE_WORKSPACE_CLI_CONFIG_DIR` to the empty config path (`/Users/howardwu/.gemini/antigravity-cli/scratch/empty_gws_config`).
