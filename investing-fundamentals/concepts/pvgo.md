---
title: Present Value of Growth Opportunities (PVGO)
created: 2026-06-26
updated: 2026-06-26
type: concept
tags: [valuation, framework, concept]
sources: [investing-fundamentals/concepts/valuations.md]
confidence: high
contested: false
---

# Present Value of Growth Opportunities (PVGO)

PVGO is a framework for decomposing a stock's price into two components: (1) the value of current earnings sustained indefinitely (steady-state value), and (2) the option value of future value-creating investments. It was coined by Stewart Myers (1977) and formalized by Miller & Modigliani (1961). A high PVGO% implies high expectations embedded in the price; a low PVGO% implies modest expectations.

Source: Mauboussin, Michael J. and Callahan, Dan. "Opportunities and Expectations: The Present Value of Growth Opportunities in Valuation." *Counterpoint Global Insights*, Morgan Stanley Investment Management, June 18, 2026.

---

## Core Framework

**Stock Price = Steady-State Value + PVGO**

- **Steady-state value** — current earnings capitalized as a perpetuity: `Steady-State P/E = 1 ÷ cost of equity`
- **PVGO** — residual: market price minus steady-state value; reflects the market's pricing of future value-creating investment opportunities
- **PVGO%** — PVGO as a share of total price; used as an expectations proxy

### Steady-State P/E Anchor

At an assumed cost of equity of 8.75%, the steady-state P/E = **11.4x** (= 1 ÷ 0.0875). Any market P/E above that implies either PVGO pricing, unsustainable earnings, or both. The S&P 500 P/E was 21.9x as of June 12, 2026 (consensus 2026 earnings).

See [[equity-risk-premium]] for cost of equity inputs (Damodaran ERP estimates used here).

---

## S&P 500 PVGO — Historical Context

- **1961–2025 average:** PVGO = 35% of price; steady-state = 65%
- **Near-zero PVGO periods:** 1974, 2011 (low expectations → subsequently strong returns)
- **Peak PVGO periods:** 1999–2001 (dot-com bubble)
- **End of 2025:** PVGO well above the long-run average

**Quartile signal:** PVGO% has modest timing utility — primarily at extremes:
- Lowest PVGO quartile → subsequent 10-yr CAGR: **11.6%**
- Highest PVGO quartile → subsequent 10-yr CAGR: **7.6%**
- Middle quartiles average ~11.2% (signal is weak between extremes)

---

## Company-Level PVGO Methodology

For individual companies, Mauboussin uses enterprise-value based approach (vs. equity perpetuity for the index):

1. **NOPAT** (trailing 12 months, adjusted for intangible investment)
2. **Steady-state enterprise value** = NOPAT ÷ WACC
3. **Steady-state equity value** = Steady-state EV − net debt
4. **PVGO** = Market cap − steady-state equity value
5. **PVGO%** = PVGO ÷ market cap

*Example:* NOPAT = $100, WACC = 8%, net debt = $250, market cap = $1,500 → steady-state equity = $1,000 → PVGO = $500 → PVGO% = 33%

### Quintile Returns (1990–2024, US companies ≥$1B market cap)

| PVGO Quintile | 5-yr Median TSR |
|---|---|
| Lowest (Q1) | 8.7% |
| Q2 (highest of all) | highest |
| Q3–Q4 | moderate |
| Highest (Q5) | 5.0% |

The measure is most useful at extremes. The low-vs-high half spread is positive in ~90% of years, averaging **+260 bps/year** (5-yr rolling, 1990–2024).

---

## PVGO vs. Value Factor (Fama-French HML)

Both PVGO% and the value factor (high-minus-low book-to-price) are expectations measures. High book-to-price = low expectations (value stocks); low book-to-price = high expectations (growth stocks).

The value factor has weakened since the early 2000s, partly due to the shift from tangible to intangible investment making book value less relevant (Lev & Srivastava, 2022).

**Finding:** PVGO% sorting outperforms the value factor by an average of **+230 bps** over 5-year periods (1990–2024), with more consistency year to year.

See [[equity-return-components]] for the broader decomposition of TSR that PVGO realization feeds into.

---

## Company PVGO Profiles (as of 2025)

| Company | Notable PVGO observation |
|---|---|
| **Nvidia** | PVGO% today similar to end of 2016 and below early-2000s average — earnings caught up with price |
| **Microsoft** | Went from 85% (1999) → −53% (2012) → strong rebound; still well below 1999 peak |
| **Amazon** | PVGO% at year-end 2025 = lowest since 1997 IPO; decades of earnings growth absorbed the expectations |
| **JPMorgan** | Peak ~40%; deeply negative post-GFC 2008–09; lower absolute PVGO% than tech peers throughout |

---

## Highlighted Passages

> You can think about the value of prospective cash flows in two parts. The first is the continuation of what a company is doing today. For instance, you might assume that a company earning $2 per share annually can sustain that level on a steady-state basis. The second part is the option to make investments in the future that create value. This part is called the "present value of growth opportunities" (PVGO), a term coined by Stewart Myers, a financial economist. "Growth" here refers to value creation, the ability to earn a return on investment higher than the opportunity cost of capital. "Opportunities" captures the idea that these investments are options, which confer the right but not the obligation to act.
>
> For the stocks of most companies, and for the market overall, some of the price is attributable to PVGO. The contributions of steady state and PVGO to total price are proxies for expectations. When the steady state is most of the stock price, expectations about future value creation are low (presuming the business is not cyclical or in secular decline). When the PVGO is a large percentage of the price, expectations about value creation are high.

---

> The steady-state assumes that the current level of earnings persists. As a result, we can value that part as a perpetuity, which capitalizes the earnings. Specifically, the P/E multiple should equal 1 ÷ the cost of equity capital. Assuming a cost of equity of 8.75 percent, the P/E multiple attributable to the steady-state value is 11.4 (11.4 = 1 ÷ 0.0875). A premium to the steady-state multiple implies that the market is attributing value to PVGO, current earnings are unsustainable, or a combination of the two.

---

> PVGO of Stock Market. Exhibit 1 shows the annual PVGO percentage for the S&P 500 from 1961 to 2025. We estimate the steady-state value by taking the operating earnings of the S&P 500 for the trailing four quarters and dividing them by an estimate of the cost of equity capital at year-end. The estimate for the equity risk premium comes from Aswath Damodaran, a professor of finance at the Stern School at New York University. We then subtract the steady-state price from the index price to assess the amount attributable to value creation. On average, the PVGO has been 35 percent of the price, and the steady-state value has been 65 percent. There have been periods when the price incorporated little or no future value creation (1974 and 2011) and other times when it reflected substantial future value creation (1999 and 2001). At the end of 2025, this measure was well above the average.

---

> PVGO of Companies. We now turn to the analysis of the stocks of companies. We use a different and more sophisticated method for this work. To estimate steady-state value for each company, we start with trailing 12-month net operating profit after taxes (NOPAT) and capitalize it by the weighted average cost of capital. We then subtract net debt, leaving us with a steady-state value for the equity. That allows us to estimate PVGO.
>
> For example, assume NOPAT is $100, the cost of capital is 8 percent, net debt is $250, and the market value of equity is $1,500. In this simple example, the steady-state equity value is $1,000 ($100 ÷ 0.08 = $1,250 − $250 = $1,000).
>
> Because total equity value equals steady-state value plus PVGO, we can solve for a PVGO percentage of 33 percent (PVGO = $1,500 – $1,000 = $500, and PVGO percentage = $500 ÷ $1,500 = 0.33).
>
> Exhibit 4 shows the five-year annualized TSRs, by quintile of PVGO percentage, for the stocks of U.S. public companies with market capitalizations of $1 billion or more in 2024 USD from 1990 to 2024. The five-year median TSR was 8.7 percent for the quintile with the lowest PVGO percentage and 5.0 percent for the quintile with the highest PVGO percentage. But the fact that the second quintile had the highest median TSR underscores that this measure is more useful at the extremes than it is between them.

---

> We picked a handful of companies we found to be interesting examples and measured PVGO percentages from the mid- to late-1990s to 2025. Here are some observations, none of which should be construed as investment advice:
>
> - **NVIDIA.** Despite now being the largest company in the world as measured by market capitalization, Nvidia's PVGO percentage is lower than it was, on average, in the early 2000s. The stock has performed extremely well in recent years, in large part mirroring rapid growth in earnings and cash flow. As a result, the PVGO percentage is today similar to what it was at the end of 2016.
> - **Microsoft.** Following the dot-com bust, Microsoft's stock was roughly flat for a decade, even though the company continued to grow sales and profits. As a result, its PVGO percentage went from 85 percent in 1999 to negative 53 percent in 2012. From there, the stock and PVGO percentage rebounded strongly. Still, the PVGO percentage remains well below the peak.
> - **Amazon.** Amazon's PVGO percentage was in excess of 100 percent in the late 1990s (through 2001), reflecting the fact that the company was losing money. But over time, the PVGO percentage has drifted lower even as the company's sales, profits, and stock price grew at a rapid rate. The PVGO percentage at year-end 2025 was the lowest year-end reading since the company went public in 1997.
> - **JPMorgan Chase.** This company followed the same pattern as some of the technology giants, including Nvidia and Microsoft, but the absolute levels of its PVGO percentages were substantially lower. Similar to other financial companies, JPMorgan's PVGO percentage peaked at around 40 percent and was substantially negative following the global financial crisis of 2008-2009.

---

> PVGO is a measure of expectations. So is the "value factor," which was popularized by Eugene Fama and Kenneth French, professors of finance. The value factor is calculated by sorting stocks based on book-to-price multiples, controlling for the size of the market capitalization. The factor is the average returns of the stocks with high book-to-price minus the average returns of those with low book-to-price.
>
> The multiple of book-to-price is the inverse of the more conventional price-to-book. So, a high book-to-price multiple often implies modest expectations and low book-to-price reflects high expectations. This factor is called "high-minus-low" (HML), or "value," in the finance literature. Fama and French show that the value factor helps explain stock returns beyond the predictions of the capital asset pricing model (CAPM) from 1927 to 2025.
>
> The value factor has been less effective since the early 2000s. One potential explanation has been the shift from tangible to intangible investment, which has made book value a less relevant financial measure.

---

> The value factor has been less effective since the early 2000s. One potential explanation has been the shift from tangible to intangible investment, which has made book value a less relevant financial measure. Here we explore whether PVGO can add any insight.
>
> Exhibit 7 compares the results of the sort based on low and high PVGO percentages (exhibit 5) to the value factor. The exhibit measures five-year annualized returns from 1990 through 2024. The PVGO percentage seems to provide higher, and more consistent, returns. The average five-year return is 230 basis points above those of the value factor.

---

## Related Pages

- [[valuations]] — General valuation methodology notes and market valuation reference
- [[equity-risk-premium]] — ERP framework; Damodaran estimates used as cost of equity input here
- [[equity-return-components]] — PVGO realization is a component of long-run TSR decomposition
- [[factor-strategies]] — Value factor (HML) context and factor investing evidence
