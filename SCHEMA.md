# Wiki Schema

## Domain

Personal investment research — US public equities (tech, security, cloud, fintech focus),
macro analysis, options strategy, crypto, and real estate. Personal portfolio, not
institutional. Emphasis on fundamental analysis with macro and quantitative overlay.

## Structure

This wiki predates the hermes llm-wiki skill. The existing directory layout serves as the
wiki layer — **do not create parallel `raw/`, `entities/`, `concepts/` directories**.

### Layer 1 — Raw / Immutable Sources

Source material that should never be edited. Read from; synthesize into wiki pages.

| Location | Contains |
|---|---|
| `investing-fundamentals/company-analyses/*-1-document-sources.md` | Source docs for each company analysis |
| `investing-fundamentals/README.md` | Curated reading list: papers, blog posts |
| `investing-macro/README.md` | Macro reference library (Fed/QE, RRP, reserves, etc.) |
| `investing-guidelines/principles.md` | Sourced investment philosophy excerpts (Oaktree, Klarman, etc.) |
| `trading/interviews/` | Interview transcripts |
| `reading-list/transcripts.md` | Podcast/interview transcripts |
| `investing-books/` | Book notes (rise-of-carry, smart-portfolios) |

### Layer 2 — Wiki Pages (Agent-maintained)

Synthesized, cross-referenced pages. These are the living knowledge layer.

| Location | Type | Contains |
|---|---|---|
| `investing-fundamentals/company-analyses/*-2-equity-report.md` | entity | Equity analysis for each company |
| `investing-fundamentals/company-analyses/*-3-investment-memo.md` | entity | Investment thesis and decision |
| `investing-fundamentals/company-analyses/*-4-stress-test.md` | entity | Bull/bear stress test |
| `investing-fundamentals/concepts/` | concept | Financial concepts (ERP, valuation, return components) |
| `investing-fundamentals/comparisons/` | comparison | Side-by-side company or strategy comparisons |
| `investing-guidelines/wealth-preservation.md` | concept | Personal wealth preservation framework |
| `investing-macro/bond-supply-tsunami-2026.md` | concept | 2026 bond supply thesis |
| `investing-macro/hormuz-closure-scenarios-2026.md` | concept | Geopolitical risk scenarios |
| `investing-options/` | concept | Options strategy notes |
| `investing-crypto/` | entity/concept | Crypto company analyses and concepts |
| `investing-real-estate/` | concept | Real estate strategy notes |
| `galactic-macro/` | concept | Speculative macro / geopolitical research |
| `[topic]/podcasts/` | concept | Synthesized podcast/interview detailed takeaways & quotes |

## Company Analysis Pipeline

Each company follows a numbered pipeline. Files are named `[ticker]-N-[type].md`:

1. `*-1-document-sources.md` — Raw source collection. **Immutable.** Never edit after creation.
2. `*-2-equity-report.md` — Equity research synthesis.
3. `*-3-investment-memo.md` — Investment thesis and conviction level.
4. `*-4-stress-test.md` — Bull/bear stress test (when present).

Not all companies have all four stages. When adding a new company, start with `-1-document-sources.md`.

## Conventions

- **File names:** lowercase ticker or hyphenated slug, no spaces (e.g., `crwd-3-investment-memo.md`, `equity-risk-premium.md`)
- **Podcasts & Verbal Media:** Store detailed summaries and syntheses of podcasts/interviews in a `podcasts/` subfolder inside the relevant topic directory (e.g., `investing-macro/podcasts/`). Use a hyphenated filename ending with the release date (`YYYYMMDD`). When indexing in `index.md`, append `(podcasts/)` next to the wiki link.
- **Cross-references:** Use `[[wikilinks]]` to link between pages. Every new wiki page should link to at least 2 other pages.
- **Existing files:** Files that predate this wiki schema do not have YAML frontmatter. Add frontmatter only to newly created pages.
- **New pages:** Use the frontmatter below.
- **Updates:** When updating an existing page, bump the `updated` date in frontmatter if it has one.
- **Provenance:** On pages synthesizing 3+ sources, append `^[path/to/source.md]` markers to paragraphs whose claims come from a specific source.
- **Google Workspace operations:** Always use the GWS CLI (`gws`) via `run_command` instead of using any Google Workspace MCP tools. This avoids manual browser OAuth prompts and keeps execution clean.

### Frontmatter for New Pages

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from taxonomy below]
sources: [path/to/source-file.md]
confidence: high | medium | low
contested: false
---
```

### Raw Source Frontmatter

New `-1-document-sources.md` files should include:

```yaml
---
ticker: CRWD
ingested: YYYY-MM-DD
sha256: <hex digest of body content>
---
```

The `sha256` enables re-ingest drift detection. Compute over body content only (after the closing `---`).

## Tag Taxonomy

Add new tags to this section before using them. All tags on any page must appear here.

**Companies & Sectors**
- `company` — individual stock or company page
- `cybersecurity` — endpoint, network, identity, cloud security
- `fintech` — financial technology, brokerage, payments
- `cloud` — cloud infrastructure, SaaS, DevOps
- `infrastructure` — chips, networking, storage, data center
- `crypto` — cryptocurrency, stablecoins, DeFi, web3
- `saas` — software-as-a-service business model
- `ecommerce` — online retail and merchant services

**Macro & Markets**
- `macro` — macroeconomic analysis
- `fed` — Federal Reserve policy
- `rates` — interest rates, yield curve
- `liquidity` — market liquidity, bank reserves, RRP, TGA
- `inflation` — inflation dynamics
- `bonds` — fixed income, Treasuries
- `credit` — credit markets, spreads
- `geopolitical` — geopolitical risk scenarios

**Analysis & Strategy**
- `thesis` — investment thesis page
- `catalyst` — near-term catalyst analysis
- `risk` — risk factor analysis
- `valuation` — valuation methodology or model
- `earnings` — earnings analysis
- `options` — options strategy
- `volatility` — VIX, implied volatility, gamma
- `real-estate` — real estate investment
- `positioning` — market structure, short interest, crowding, and positioning dynamics

**Meta**
- `framework` — investment framework or principle
- `comparison` — side-by-side analysis
- `concept` — financial or economic concept
- `speculation` — low-confidence or speculative content

## Page Thresholds

- **Create a company page** when doing a full analysis (3+ sources). Use the numbered pipeline.
- **Create a concept page** when a concept appears in 2+ company analyses or macro notes.
- **Create a comparison page** when directly comparing 2+ companies or strategies.
- **Don't create a page** for passing mentions or single-source details.
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links.

## Update Policy

When new information conflicts with an existing page:
1. Check dates — newer sources generally supersede older ones.
2. If genuinely contradictory, note both positions with dates and sources.
3. Mark `contested: true` in frontmatter and add `contradictions: [page-slug]`.
4. Flag for review in the next lint report.

## Obsidian Compatibility

This wiki directory works as an Obsidian vault. `[[wikilinks]]` render as clickable links.
Graph View will visualize cross-references across company analyses and macro themes.
