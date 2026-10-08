---
name: investment-stress-test
description: Run an adversarial bull/bear/arbitrator investment stress-test on a company that already has research documents (company-1-document-sources.md, company-2-equity-report.md, company-3-investment-memo.md). Use when the user wants to stress-test, pressure-test, or challenge an investment thesis; explore bull and bear cases; or get a structured arbitrated assessment with KPIs to monitor. Outputs to company-4-stress-test.md. Companion skill to investment-analyst.
---

## Overview

Runs a 3-agent adversarial stress-test on a researched company. Requires `[company]-3-investment-memo.md` to exist. Output: `[company]-4-stress-test.md`.

## Step 1: Pre-Flight — Read Existing Docs

Read `[company]-3-investment-memo.md` in full. Extract:

- **"Data as of" date** — scopes the web search window in Step 2
- **Risk framework** (Section 5) — top risks by severity × probability score become the bear analyst's focus areas
- **Investment thesis + bull/bear case** (Section 1) — the bull analyst's structural pillars
- **Top 3 growth drivers** (Section 4) — bull analyst's forward-looking arguments
- **KPI watch list** (Section 6) — baseline for the arbitrator's KPI proposals

Also read `[company]-2-equity-report.md` for competitive position, moat analysis, and key financial metrics.

## Step 2: Web Search — Recent Developments

**This step is mandatory. Never skip it.** Search for developments since the memo's "data as of" date. Run these searches in parallel:

1. `[Company] [ticker] earnings results [most recent quarter] [year]`
2. `[Company] [ticker] latest news [current month] [year]`
3. `[Company] [top competitor from memo] competitive update [year]`
4. `[Company] [top risk from memo] update [year]`

Synthesize findings into a bullet-point "Recent Developments" summary to inject into all three agent prompts. If no material developments exist, state that explicitly — do not omit the search.

## Step 3: Spawn Bull and Bear Analysts in Parallel

Dispatch both agents simultaneously with `run_in_background: true`. Each agent receives:

- All key financial metrics from the investment memo (paste the exact numbers)
- The recent developments from Step 2
- Their specific focus areas (derived from the memo, not invented)

**Bull analyst — 4 focus areas:**
1. Secular TAM and structural market position argument
2. Revenue quality metrics (NRR, RPO, gross margins, FCF — whichever apply)
3. Platform or product expansion signals from the most recent quarter
4. Why the most-feared bear scenario (identify it from the risk matrix) actually *strengthens* the bull case

**Bear analyst — 4 focus areas:**
1. The #1 structural risk from the risk matrix (highest severity × probability score)
2. Competitive bundling, displacement, or pricing pressure
3. Any inorganic revenue (M&A, acqui-hires) potentially masking organic deceleration — strip it out and show the math
4. Multiple compression math: what the valuation looks like if growth decelerates below the threshold that justifies the current multiple

**Required output format for both analysts:**
- 4 sections, one per focus area
- 3–5 bullet points per section, each backed by a specific number from the docs or web search
- Close with a 3–4 sentence summary paragraph
- Total: ~600–800 words

## Step 4: Spawn Arbitrator

Wait until **both** analysts return. Then dispatch a single arbitrator agent with both full reports included verbatim in the prompt.

**Arbitrator must produce exactly these 3 sections:**

### Section 1: Factual Common Ground
4–5 facts that both analysts accept as true but interpret differently. For each:
- State the fact
- Bull interpretation
- Bear interpretation

These must be genuine divergences on the same fact, not one side's unique claims.

### Section 2: The 3 Critical Divergence Assumptions
For each of 3 assumptions:
- **Name** — short label
- **Bull version** — the world where the bull wins on this assumption
- **Bear version** — the world where the bear wins
- **Why it's the crux** — 1–2 sentences on why this assumption dominates the outcome
- **Verdict weight** — which side has better *current* evidence from the data provided. Must be one of: *Lean bull [margin]*, *Lean bear [margin]*, or *Too close to call*. "Both sides have merit" is not acceptable.

### Section 3: KPI Monitor Proposals
For each of the 3 assumptions, 1–2 KPIs:
- **Metric name and definition** (precise enough to calculate from earnings releases)
- **Green signal** (value or trend that confirms the bull case)
- **Red flag** (value or trend that confirms the bear case)
- **Data source** (quarterly press release, 10-K, earnings call, etc.)

**Closing paragraph (3–4 sentences):** What is the single most important thing an investor must be right about to own this stock? What does that imply for portfolio sizing and conviction level?

## Step 5: Write Output File

Write `[company]-4-stress-test.md` with this structure:

```
# [Company] ([Ticker]) — Bull/Bear Stress-Test

**Format:** Adversarial debate — independent bull analyst, independent bear analyst, arbitrator
**Data as of:** [memo's data-as-of date]
**Recent developments through:** [today's date]
**Companion file:** [company]-3-investment-memo.md

---

## Recent Developments
[Bullet list from Step 2 web search]

---

## Bull Case
[4 sections + summary paragraph]

---

## Bear Case
[4 sections + summary paragraph]

---

## Arbitrator Assessment

### Shared Facts, Divergent Interpretations
[Table: Fact | Bull Interpretation | Bear Interpretation]

### The 3 Critical Divergence Assumptions
[3 assumptions with verdict weights]

### KPI Watch List
[Table: Assumption | KPI | Green Signal | Red Flag | Source]

### Closing Assessment
[3–4 sentence paragraph on single most important assumption + sizing implication]
```

## Hard Rules

1. **Web search always runs before agent dispatch** — mandatory even if you believe you know the recent news
2. **Bull and bear run in parallel** — always `run_in_background: true`; never sequentially
3. **Arbitrator must commit to a verdict** on each assumption — specific evidence required; equivocation is a failure mode
4. **Every analyst claim cites a number** — qualitative-only arguments are not acceptable
5. **Do not write the stress-test yourself** — the 3-agent structure exists to create adversarial independence; a single-agent summary defeats the purpose
6. **Focus areas come from the memo** — derive them from the existing risk matrix and investment thesis, not from generic playbooks
