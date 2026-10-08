---
name: investment-analyst
description: Executes a complete 3-step fundamental equity research analysis for a specified public company (1-document-sources, 2-equity-report, 3-investment-memo) following the wiki pipeline.
---

# Investment Analyst Workflow

Use this skill when the user requests an equity research analysis on a specific company (e.g. `/investment-analyst [company/ticker]`).

Execute the following three-step analysis automatically and in sequence. Save each output as a separate Markdown file in `investing-fundamentals/company-analyses/` (or the target directory). Complete each step fully before proceeding to the next.

## File Naming Conventions

Use the standard pipeline naming convention:
- `[company]-1-document-sources.md`
- `[company]-2-equity-report.md`
- `[company]-3-investment-memo.md`

Replace `[company]` with the lowercase ticker or hyphenated company slug (e.g. `crwd`, `ftnt`, `panw`, `tesla`, `berkshire-hathaway`).

---

## STEP 1: DOCUMENT SOURCES (`*-1-document-sources.md`)

Use `search_web` and `read_url_content` extensively to find official investor relations filings and documents for the target company.

### A) Annual Reports & Filings (Primary Task)
- Search for Annual Reports, Form 10-K, or Universal Registration Documents for the **past 5 years** (prioritize the most recent year first — e.g. FY2025/FY2026 filings).
- Sources must be official: company investor relations website, SEC.gov EDGAR, AMF-France.org, Companies House, or equivalent regulators.
- Exclude aggregators, press releases, CSR/ESG reports, or third-party presentations.
- If both English and another language exist for the same year, keep English only (else original language).
- If the company changed names or tickers, search prior corporate names for older filings.
- Return verified direct PDF or filing URLs in chronological order.

Output a clean Markdown table:

| Year | Document Title | Direct PDF / Filing URL | Source Domain |
|:-----|:---------------|:------------------------|:--------------|

### B) Capital Markets Day / Investor Day (Secondary Task)
- Search for Capital Markets Day (CMD) or Investor Day presentation decks and transcripts within the past 5 years.
- Sources must be official (company IR site or regulatory portal).
- Exclude media articles and third-party summaries.

Output a separate table titled "Capital Markets Day / Investor Day Materials":

| Event Year | Event Name / Title | Direct PDF / Web URL | Source Domain |
|:-----------|:-------------------|:---------------------|:--------------|

### Frontmatter for Document Sources
Follow `SCHEMA.md` raw source frontmatter:
```yaml
---
ticker: [TICKER]
ingested: YYYY-MM-DD
sha256: <hex digest of body content>
---
```

Save this output as `investing-fundamentals/company-analyses/[company]-1-document-sources.md`. Note: this file is an immutable raw source record.

---

## STEP 2: EQUITY ANALYST REPORT (`*-2-equity-report.md`)

Based on the primary filings identified in Step 1, supplemented by web research on the company's financial model, product segments, and competitive landscape, create a comprehensive equity analyst report.

**Tone:** Highly analytical, factual, rigorous, and concise.

### Frontmatter
```yaml
---
title: "[Company Name] Equity Research Report"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [company, [sector-tags from SCHEMA.md], valuation, earnings]
sources: [investing-fundamentals/company-analyses/[company]-1-document-sources.md]
confidence: high
contested: false
---
```

### Report Structure:

#### Executive Summary (150–200 words)
Explain how the company makes money, the quality of its economics, and its key competitive advantages and risks. End with a one-sentence synthesis in plain English.

#### What They Sell and Who Buys
Summarize the core products or services and customer profile (enterprise tiers, SMB, consumer segments, geographical split). Clarify the core business need or ROI driving customer procurement.

#### How They Make Money
Explain the revenue model (recurring SaaS, consumption/token-based, transaction/take rate, upfront hardware/licensing, hybrid). Detail key revenue segments and their relative size ($ and % of revenue).

#### Revenue Quality & Retention
Evaluate predictability and revenue diversification. Break down ARR/subscription revenue vs. professional services/one-off exposure, Net Retention Rate (NRR/NDR), Gross Retention Rate (GRR), and customer concentration risks (e.g. top 10 customers % of revenue).

#### Cost Structure & Unit Economics
Outline major cost components: COGS (hosting/infrastructure/compute), R&D, Sales & Marketing (CAC payback), and G&A. Note GAAP and non-GAAP Gross Margins, Operating Margins, and operating leverage potential.

#### Capital Intensity & Cash Flow Dynamics
Describe balance sheet asset intensity, CapEx requirements (maintenance vs. growth), working capital cycle, stock-based compensation (SBC) dilution impact, and Free Cash Flow conversion (FCF / Operating Cash Flow).

#### Growth Drivers
Identify the primary levers of top-line expansion (pricing power, seat/usage expansion, cross-sell/multi-product adoption, international expansion, M&A). Distinguish structural secular tailwinds from cyclical fluctuations.

#### Competitive Edge & Moat Assessment
Detail what protects the company's economics: high switching costs, network effects, brand/reputation, proprietary IP/data loops, scale/cost advantages, or regulatory barriers. Quantify moat durability using return on invested capital (ROIC), gross margin stability, and pricing resilience.

Save this output as `investing-fundamentals/company-analyses/[company]-2-equity-report.md`.

---

## STEP 3: INVESTMENT MEMO (`*-3-investment-memo.md`)

Synthesize the findings from Steps 1 and 2 into an actionable investment memo with strict risk frameworks, sensitivity scenarios, and measurable KPI watchlists.

### Frontmatter
```yaml
---
title: "[Company Name] Investment Memo"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity
tags: [company, thesis, valuation, risk, [sector-tags]]
sources: [investing-fundamentals/company-analyses/[company]-1-document-sources.md, investing-fundamentals/company-analyses/[company]-2-equity-report.md]
confidence: high
contested: false
---
```

### Memo Structure:

#### 1. Executive Summary & Thesis
- Core investment thesis in 1 concise paragraph.
- Bull Case (1–2 sentences with target upside / multiple).
- Bear Case (1–2 sentences with downside floor / multiple).
- Target investor profile (growth at reasonable price [GARP], deep value, compounder, special situation).

#### 2. Business Model & Unit Economics
- Revenue breakdown by segment and geography.
- Key unit economics (LTV/CAC, Magic Number, Rule of 40, ARPU, gross margin per unit).
- Operating leverage trajectory and incremental operating margins.
- Working capital efficiency and FCF conversion.

#### 3. Competitive Position & Moat Durability
- Industry market share data and ranking against direct peers.
- Moat classification (switching costs, network effects, cost advantages, scale).
- Moat durability score and competitive differentiation matrix.

#### 4. Top 3 Growth Drivers & Sensitivities
- For each of the top 3 drivers: description, TAM impact, and catalyst timeline.
- **Sensitivity Matrix:** Table modeling Base / Bull / Bear scenarios across revenue growth, operating margin, EPS/FCF per share, and valuation multiple (EV/Sales, EV/FCF, or P/E).

| Scenario | 3-Yr Revenue CAGR | Terminal Op Margin | FY28 FCF/Share | Target Multiple | Target Price | Implied IRR |
|:---------|:------------------|:-------------------|:---------------|:----------------|:-------------|:------------|
| **Bear** | ...               | ...                | ...            | ...             | ...          | ...         |
| **Base** | ...               | ...                | ...            | ...             | ...          | ...         |
| **Bull** | ...               | ...                | ...            | ...             | ...          | ...         |

#### 5. Risk Framework & Pre-Mortem Failure Modes
- Top 5 fundamental risks ranked by `Severity x Probability`.
- For each risk: trigger event, business impact, and company mitigation.
- **Pre-Mortem:** *"If this investment loses >50% of its value over the next 3 years, the most likely cause will be..."*
- Core load-bearing assumptions that must hold true for the thesis to succeed.

#### 6. 12-Month KPI Watch List
- 8–10 specific, measurable operating and financial metrics to monitor quarterly.
- Structured table with target range and explicit red-flag breach thresholds.

| KPI / Metric | Current Baseline | 12-Month Target | Red-Flag Threshold | Data Source | Frequency |
|:-------------|:-----------------|:----------------|:-------------------|:------------|:----------|

Save this output as `investing-fundamentals/company-analyses/[company]-3-investment-memo.md`.

---

## STEP 4: WIKI REGISTRATION & CROSS-LINKING

After creating all three files:
1. **Update `index.md`:** Add the company analysis files under `## Fundamental Analysis` -> `### Company Analyses` in `index.md`.
2. **Update `log.md`:** Add an entry recording the creation of the analysis pipeline:
   ```markdown
   ## [YYYY-MM-DD] create | [ticker] company analysis pipeline

   - Created: `investing-fundamentals/company-analyses/[company]-1-document-sources.md`
   - Created: `investing-fundamentals/company-analyses/[company]-2-equity-report.md`
   - Created: `investing-fundamentals/company-analyses/[company]-3-investment-memo.md`
   - Updated: `index.md`
   - Updated: `log.md`
   ```
3. **Cross-References:** Ensure `*-2-equity-report.md` and `*-3-investment-memo.md` include `[[wikilinks]]` to at least 2 relevant concepts or theme pages (e.g. `[[valuations]]`, `[[ai-inference-costs-accounting]]`, `[[pvgo]]`).
