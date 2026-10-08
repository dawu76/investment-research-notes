# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete, init

## [2026-10-04] create | HTML companion for the 2026-09-25 newsletter digest

- Created: `investing-macro/market-newsletter-digest-2026-09-25.html` (reading version of the .md digest: ten key-reading tiles showing each figure against the prior digests, a watch-levels panel, a source-conflicts panel, a section index, all 12 themes with their text, numbers, quotes and sources kept, tables for the credit spread ladder, payroll breakeven, Muse metrics, SaaS multiples and regional datacenter capacity, and the related-page links pointed at the .md files).
- Everything in the HTML comes from the .md digest; nothing new was added. The .md file stays the source of record.
- 2026-10-07: reworked for skimming. Each of the 60 points is now a collapsible headline plus a one-line key-number gist, with the full original text (sources kept) in the expanded body split into short paragraphs. Added a 12-line Bottom line list linking to each theme, Expand all / Collapse all buttons, "Why it matters" and "Vs. prior digests" tags on sub-points, and a collapsed conflicts panel. A word-level check against the previous version confirmed no text was dropped.
- 2026-10-07: added 10 bar charts and 6 new tables. Charts are inline HTML/CSS bars on theme tokens (light and dark), each with hover/focus tooltips. Section-level charts sit under the takeaway: MOVE with Mar 2026 and Oct 2023 reference lines, payroll breakeven vs. actual, credit spreads by rating, token prices plus frontier share of spend, and datacenter capacity by region. Point-level charts: daily curve change, HYG vs. HYGH, Chinese hyperscaler capex, and Alibaba segment growth. Tables: auctions, fiscal items, productivity, enterprise cost before/after, crypto market-value shares, and the conflicts panel. Every value comes from the .md; three tables the charts replaced were removed, with the sentence text kept. Series colors were checked for colorblind separation in both themes.
- HTML pages are not wiki pages, so `index.md` is unchanged.

## [2026-10-04] ingest | Investment newsletter digest for 2026-09-25

- Retrieved 71 Gmail messages matching investment/newsletter keywords for 2026-09-25 (haroldwu account, GWS CLI); used about 47 after excluding promos, AI-engineering podcasts, general tech and culture pieces, Readwise, a duplicate ChinaTalk send and paywalled stubs with no data.
- Created: `investing-macro/market-newsletter-digest-2026-09-25.md` (12 sections): long-end selloff (10Y 5.18-5.23%, 30Y 5.47-5.5%, 7Y auction at 5.085%, highest since 1993) decomposed as a real-yield move (TIP and IEF fell together), MOVE 78.6 to 104.6; Fed hawks (Williams, Hammack, Paulson) vs. the Paulson/Tom Lee dovish case and the September 30 core PCE test; D'Agostino's sub-10K payroll breakeven and record-low labor share; CCC-only credit stress (Ree's HYG vs. HYGH split, Slok's refinancing-wall mechanism); new Project Jupiter details and the Akamai-Anthropic deal; Open Insights on paper vs. physical oil and JPMorgan's "no baseline view"; breadth at a March 2000 extreme vs. Wintersberger's rotation thesis; Ramp's frontier-share drop (53% to 45%), Muse's usage and revenue data, the "consumer inertia" selloff and Clouded Judgement multiples; FUNDA's enterprise AI survey; SemiAnalysis China datacenter model and Alibaba FY1Q27; Adyen, AMD, Costco and smaller single-stock notes; Tom Lee ETH ladder and Zcash.
- Data conflicts flagged inline rather than resolved: 10Y level by source and time, Muse download counts, UMich inflation expectations (4.6% prelim vs. "above 7%" from Noble/Dayan), Oracle rent deferral (three-year delay vs. owes rent regardless), two different oil crack-spread measures, and a price mismatch inside the VersaBank pitch.
- Updated: `index.md` (indexed under Macro; page count 228; last-updated date 2026-10-04).
- Updated: `log.md`

## [2026-10-02] create | HTML companion for the Sage Road "The AI Trade" note

- Created: `investing-fundamentals/company-analyses/themes/sage-road-ai-trade-2026-09.html` (visual version of `sage-road-ai-trade-2026-09.md`: verdict up front, thesis, the argument as a six-link chain with a strength rating per link, charts for the capex revisions, FCF collapse, off-balance-sheet estimates across sources, lab share of cloud revenue and the BIS boom comparison, the full fact-check table with verdicts, Sage Road's single-block view vs UBP's five-tier ranking, the timing mismatch as a timeline, strengths, how to use it).
- The BIS chart comparison labels come from the summary's chart image (canal mania peaked ~4x at year 5; dotcom stayed under 2x); the .md note only says AI rose faster than the other episodes.
- HTML pages are not wiki pages, so `index.md` is unchanged.

## [2026-10-02] create | HTML companions for the UBP and Brookings AI-financing notes

- Created: `investing-fundamentals/company-analyses/themes/ubp-financing-ai-build-out-2026-09.html` (visual version of the UBP note: four-line argument, capex vs cash flow, off-balance-sheet breakdown, per-company leverage/capex/backlog charts, lab exposure, bond-market signals, tenant-pricing table, commencement timeline, fragility ladder, all fact checks, history, Brookings comparison, verdict).
- Created: `investing-fundamentals/company-analyses/themes/brookings-financing-ai-buildout-van-nieuwerburgh-2026-09.html` (visual version of the Brookings note: five-line argument, Table 5 by year, campus cost split, pipeline scenario, funding mix, Beignet case, required-revenue walk and sensitivities, REIT beta, NVIDIA backstop, history, takeaways, all fact checks, verdict).
- Also logging `ai-buildout-financing-ubp-vs-brookings-2026-09.html` (combined side-by-side page, created 2026-10-01).
- Both new pages flag two inconsistencies in the source notes rather than repeating them: the UBP note's "~80%/year for ~8 years" (37x in 6 years is ~83%/yr; over 8 years it is ~57%/yr) and the Brookings note's "44.5%" realization rate (182.7/509 is ~36%; the three buckets sum to 526.8GW, not 509GW). The .md notes are unchanged.
- HTML pages are not wiki pages, so `index.md` is unchanged.

## [2026-10-02] ingest | Sage Road Research: The AI Trade (Sept 2026)

- Source: Sage Road Research, "The AI Trade" by Trevor Noren (September 2026), https://sageroadresearch.com/products/the-ai-trade. Full report is paywalled; the public 7-page executive summary was read from both the page images and the text version at /pages/the-ai-trade-executive-summary.
- Created: `investing-fundamentals/company-analyses/themes/sage-road-ai-trade-2026-09.md` (thesis, table of every cited data point with its source, claim checks against UBP/Brookings/Burry and the Jun 29, Jul 13, Jul 19, Jul 26 and Sep 18 digests, weaknesses and strengths, how to use it). Main findings: capex, FCF, issuance and open-weight data hold up; the $1.65T off-balance-sheet figure is below every other wiki estimate ($2.4-3T); the Meta "OCF 96% lower with SBC" claim is likely misquoted, and the SBC/deferred-tax mechanics are wrong; the contagion conclusion goes beyond the evidence because the summary does not separate Oracle and neoclouds from the AA hyperscalers.
- Updated: `investing-fundamentals/company-analyses/themes/ubp-financing-ai-build-out-2026-09.md` and `brookings-financing-ai-buildout-van-nieuwerburgh-2026-09.md` (backlinks added; `updated` bumped to 2026-10-02).
- Updated: `index.md` (indexed under Themes; page count 227; last-updated date bumped to 2026-10-02).
- Updated: `log.md`

## [2026-10-01] update | Style cleanup of pages written this session

- Applied the global writing style rules (no em dashes, no banned filler words such as "load-bearing" and "genuine") to text written in this session only: `investing-macro/market-newsletter-digest-2026-09-24.md`, `investing-fundamentals/company-analyses/themes/brookings-financing-ai-buildout-van-nieuwerburgh-2026-09.md`, the Wells Fargo and Edgewater rows in `investing-fundamentals/company-analyses/app-1-document-sources.md`, the Brookings comparison section in `investing-fundamentals/company-analyses/themes/ubp-financing-ai-build-out-2026-09.md`, and the new `index.md` and `log.md` entries. Also rewrote two "isn't X, it's Y" sentences. Pre-existing text from earlier sessions was left unchanged.
- Updated: `investing-fundamentals/company-analyses/app-1-document-sources.md` (sha256 recomputed after the edit: `fbf47e1d746b1760c0c4d23a0347ed86193e9b66b3ba9e1d9e98911d4dd92e60`; supersedes the hash in the earlier 2026-09-30 APP entry).
- Updated: `index.md`, `log.md`

## [2026-10-01] update | Alpha Exchange, Brij Khurana: corrections after re-reading the transcript

- Updated: `investing-macro/podcasts/ax-brij-khurana-wellington-ai-capex-crowding-out-bonds-20261001.md` (full rewrite after a line-by-line re-check against the timed transcript). Conclusions changed: (1) Khurana expects the Fed to LOWER bank capital charges on NDFI loans (he thinks they should raise them); the first version had this reversed. (2) His ~100bp "too high" gap is on the 10y10y forward (~6.2% vs. ~5-5.25% fair value), not spot 10Y, which sits inside his fair-value range per the wiki digests; the "cautious on long USTs" rating was replaced with "no explicit view; mixed." (3) The "~4% inflation" figure was the host's, not Khurana's; his own figure was ~2% core ex-shelter over three years, and the TIPS carry case is conditional ("if we keep realizing these levels of inflation"). (4) "Highest-conviction" TIPS was softened to "first of three unranked areas of excitement, close to the top of the list." Added: a growth-headwinds theme (tight policy plus oil shock, real wages ex transfers negative, nominal growth peak, November divided-government catalyst), hedged-to-USD yield point, the disputed JPMAM crowding-out chart, and a transcript-caveats block (garbled Australia/NZ hike size, host vs. guest attribution, claims without cited sources). Fixed an EM local quote that merged two sentences (the 18% is 2025), corrected ~8 timestamps, and corrected cross-reference descriptions (yen page is a Dec 2025 Fed-BOJ swing analysis; TIPS page covers auction mechanics only; Brookings uses a 10% hurdle, not 30-40% ROIC).
- Updated: `index.md` (entry text), `log.md`

## [2026-10-01] ingest | Alpha Exchange: Brij Khurana (Wellington), AI Capex Crowding Out Bonds

- Source: Alpha Exchange podcast (host Dean Curnutt), guest Brij Khurana, Fixed Income Portfolio Manager at Wellington Management. Released October 1, 2026 (https://youtu.be/zYAYoBNwg1Y). Full transcript pulled directly via YouTube's caption API (youtube-transcript-api, already installed), not a secondhand summary.
- Created: `investing-macro/podcasts/ax-brij-khurana-wellington-ai-capex-crowding-out-bonds-20261001.md`: Khurana's "low rates rot" thesis (investment has decoupled from rates since the dot-com crash, driving financialization instead); the QE balance-sheet channel running backward (QE raises yields by triggering debt-monetization fears, not lowering them); current inflation reframed as wealth-effect-driven sticky services inflation rather than labor-market inflation; the back-end Treasury selloff read as a Fed/AI-growth repricing rather than a supply story (~100bp above his nominal-growth fair-value estimate); AI capex financing's "circular" structure and ~$1T growth in bank lending to non-depository financial institutions; two distinct bond crowding-out mechanisms (hyperscaler issuance pressuring other IG borrowers; AI capex's rate-insensitivity raising stock-bond correlation and eroding bonds' hedge value); global rate-hike "mistakes" priced into Australia/NZ; the yen carry trade now flowing into US equities rather than EM, and Bessent's push to end the "one-way trade"; UK gilts vs. France's OAT-Bund spread; and TIPS as his highest-conviction trade given ~2.3% breakevens against real yields near 1990s-launch-era highs. Ten detailed-takeaway themes with illustrative quotes, a timestamped agenda, 8 portfolio-positioning action items, a 10-row asset class breakdown table, and 6 cross-references into existing wiki pages (bond supply, UBP/Brookings AI financing pages, yen carry trade page, TIPS mechanics page, Sept 24 digest).
- Updated: `index.md` (indexed under Macro with `(podcasts/)` tag; page count 226; last-updated date bumped to 2026-10-01).
- Updated: `log.md`

## [2026-09-30] create | Brookings "Financing the AI Buildout" (Van Nieuwerburgh, Sept 2026)

- Source: Brookings Papers on Economic Activity (BPEA) Fall 2026 conference draft by Stijn Van Nieuwerburgh (Columbia Business School), full 28-page PDF read directly via pdftotext (installed poppler for extraction; WebFetch could not parse the binary PDF).
- Created: `investing-fundamentals/company-analyses/themes/brookings-financing-ai-buildout-van-nieuwerburgh-2026-09.md` ($10.3T/3.63%-of-GDP buildout estimate from a Cleanview project-level capacity model with documented econometric imputation; Meta Hyperion/Beignet SPV case study with $27B debt at 90% debt-to-asset and 1.12x DSCR; off-balance-sheet obligations of $2.4T [WSJ tally, 4 firms] vs $604B on-balance-sheet; data-center REIT beta risen from ~0.5 to ~1 since 2018; a formal revenue-required-to-pencil-out calculation [Appendix D] showing $3.725T mature annual revenue needed by 2032 at a 10% unlevered return/50% margin, implying ~80%/year revenue growth from OpenAI+Anthropic's ~$100B base, with sensitivity $2.29-6.72T; historical comparison table showing the AI buildout at 3.63% of GDP vs canals 0.66%, railroads 2.24%, electrification 0.50%, highways 1.13%, telecom/fiber 1.10%). Independently re-verified every reported arithmetic total (Table 5, Table 6, capital-recovery-factor math, construction-period multiplier) -- all reconciled exactly, no errors found. Cross-checked off-balance-sheet figures against UBP's $2.9T and Burry's ~$3T estimates (triangulating in the same zone despite different firm counts/categories) and confirmed Michael Parekh's digest citation of this paper matches exactly.
- Updated: `index.md` (indexed under Themes; page count 225; last-updated date bumped to 2026-09-30).
- Updated: `log.md`

## [2026-09-30] update | UBP "Financing the AI Build-out" vs. Brookings/Van Nieuwerburgh comparison

- Updated: `investing-fundamentals/company-analyses/themes/ubp-financing-ai-build-out-2026-09.md` (added "Comparison to Brookings' 'Financing the AI Buildout' (Van Nieuwerburgh, Sept 2026)" section after reading the full Brookings BPEA conference-draft PDF directly, not a secondhand summary. Same title as the UBP note but a different genre: Brookings is an academic paper with an original capacity-pipeline model (Cleanview project database, ridge-regression imputation) and a formal revenue-required-to-pencil-out calculation (Appendix D: $9.61T capital base, 10% unlevered return, 6yr IT life / 20yr non-IT life assumptions -> 19.37% annual capital charge -> $1.86T required operating cash flow -> $3.725T required mature annual revenue by 2032 at a 50% margin, i.e. ~80%/year revenue growth from OpenAI+Anthropic's ~$100B base, sensitivity $2.29-6.72T); UBP is a sell-side-style credit note with no equivalent calculation. Documented where the two corroborate (same Hyperion/Beignet Meta-Blue Owl deal as central case study with near-identical figures, same 2026 capex-exceeds-OCF crossover, same ~3-4x off-balance-sheet-to-on-balance-sheet multiple, same railway-mania/telecom-fiber analogies) and where they diverge (Brookings' data-center-REIT-beta-rising-to-1 finding, the $500B NVIDIA-backstopped credit facility circularity point, and GPU-refresh-cycle exclusion all absent from UBP; UBP's company-level granularity absent from Brookings; flagged that the wiki's own prior 2.6%-of-GDP figure for UBP was this wiki's estimate, not UBP's own claim, and is not comparable to Brookings' 3.63% multi-year full-buildout figure). Added Brookings PDF to sources and cross-referenced `market-newsletter-digest-2026-09-24.md`.

## [2026-09-30] update | AppLovin (APP) company analysis pipeline (Wells Fargo eComm pixel adoption note, Edgewater Research channel checks)

- Updated: `investing-fundamentals/company-analyses/app-1-document-sources.md` (added Section E entry for Wells Fargo's September 30, 2026 note "Acceleration in eComm Pixel Adoption Driven by No / Low Traffic Sites; Appears To Be a False Start": argues the recent pixel-install spike is an APAC low/no-traffic Shopify-storefront artifact rather than genuine customer acquisition, with traffic-weighted additions flat in September vs. 1H:26; sees e-commerce customer growth inflection as unlikely before 2027. Added Section E entry for Edgewater Research's September 23, 2026 channel checks (analyst Joe Wittine, via public news coverage: Yahoo Finance, GuruFocus, Benzinga, Investing.com) finding APP's MAX ad network approaching a functional share ceiling, Q4 2026 sequential revenue growth guided to 8-9% (essentially flat vs. the 7-8.6% implied by Q3 guidance, read as a stall since Q4 is seasonally ad-tech's strongest quarter), and Unity Software compressing net revenue spreads; calls APP "a show-me story" and expects 2026/2027 sell-side estimates to move lower. Corrected an initial mischaracterization of the Q4-vs-Q3 growth comparison as "down from" when the ranges actually overlap/are roughly flat. Recomputed sha256 `cab268361ed558097e5018e844d42f5ac3fa6b841a90f5b3f7d066361b5f0b1c`).

## [2026-09-29] ingest | Investment newsletter digest for 2026-09-24

- Retrieved 82 Gmail messages matching investment/newsletter keywords for 2026-09-24; curated to 40 genuine investment/macro/crypto/options/single-stock newsletters after excluding general AI/tech news unrelated to markets, off-topic culture/politics pieces, pure marketing sends, and duplicate broadcast threads (SixSigmaCapital, Interconnected).
- Created: `investing-macro/market-newsletter-digest-2026-09-24.md`: 10Y Treasury clearing its last cap since 2007 (5.11-5.14%) on a five-year-high flash PMI and a tailed 5Y auction with October hike odds at 71%; Oracle's force majeure notice on the 2.45GW Project Jupiter data center and AI CDS widening (Oracle ~224bp, CoreWeave >850bp per The Alethea Narrative); Brent/WTI divergence with the refining crack spread at the 99.8th percentile since 2006 (Lance Roberts); Michael Parekh's $10.3T/8-year AI buildout estimate vs. Michael Burry's dot-com-matching capex/GDP capital-cycle data; DeepSeek's $1B ARR and $75B raise; Meta's Muse monetization disclosure and Cloudflare's agent-traffic-exceeds-human-traffic Q2 results; Broadcom/Micron multiple-gap thesis and Intuitive Surgical's Medtronic/J&J competitive-threat compression; Baiguan's 25-case US/China regulatory-blowup framework; and Lead-Lag's NMZ/FSK closed-end-fund/BDC income screen.
- Updated: `index.md` (indexed under Macro; page count 225).
- Updated: `log.md`

## [2026-09-29] query | Multifamily credit stress claim and REM downside

- Sources: Trepp via Multifamily Dive (Aug 2026 CMBS; CRED iQ/FDIC bank data), MBA debt outstanding (Q3 2025), CRE Daily on Arbor modifications, Apartments.com supply/vacancy outlook, Henry Hub futures reporting, stockanalysis.com REM holdings (Sept 25), Yahoo Finance chart API for REM/holdings prices and drawdowns, wiki digests for rates and MOVE.
- Created: `investing-real-estate/multifamily-credit-stress-and-rem-2026-09.md` (claim-by-claim table, REM holdings grouped by exposure, 1-year returns, historical drawdowns, scenario math, watch list).
- Updated: `index.md` (Real Estate; page count 224).
- Updated: `log.md`

## [2026-09-29] query | Uber as robotaxi beneficiary (BNP Paribas thesis)

- Sources: Benzinga on BNP Paribas (Nick Jones, Sept 29; read in Chrome after WebFetch 403; underlying BNP note not seen), Yahoo Finance (Sept 24; Q2 figures, insider buys, BofA Sept 22 note), TechCrunch AV deal tracker (Aug 1), CNBC/Bloomberg on Waymo ending Austin/Atlanta exclusivity (July 24), Seeking Alpha (Durant, Sept 29; paywalled, summary only), InsideEVs on Tesla Cybercab.
- Created: `investing-fundamentals/company-analyses/themes/uber-robotaxi-aggregator-thesis-2026-09.md` (BNP cost table with depreciation sanity check, bull and bear cases, utilization-vs-platform-fee arithmetic, verdict, watch list). `confidence: medium`, `contested: true`.
- Updated: `index.md` (Themes; page count 223).
- Updated: `log.md`

## [2026-09-28] ingest | UBP "Financing the AI Build-out" (Sept 16, 2026)

- Source: UBP Headlines, Filipe Alves da Silva. Full 27-page PDF read (web page is a summary). Historical data from Odlyzko (railway mania), AllianceBernstein and Econlib (2000-02 HY defaults), Brookfield PSG (sector default cycles), Fabricated Knowledge and CACM (telecom capex, dark fiber).
- Created: `investing-fundamentals/company-analyses/themes/ubp-financing-ai-build-out-2026-09.md` (key data table, investor takeaways, internal arithmetic checks, cross-checks against wiki digests and the Burry page, historical comparison table, verdict). Found: cumulative 2026-30 capex stated as both $6.5T and $5.6T; Oracle 1.5% index-cap headroom likely ~$35-40B rather than $60B; guarantees undercounted vs FT's $300B RVG figure; backlog-to-lease coverage omits chip costs.
- Updated: `investing-macro/macro-frameworks/ai-compute-commencement-wall-and-refinancing-trap.md` (dated reconciliation note: $2.3T = four clouds' RPO, ~$1.25T = labs' commitments; cross-reference). Addresses review trigger (c).
- Updated: `investing-fundamentals/company-analyses/themes/burry-ai-capital-cycle-oracle-jupiter-2026-09.md` (cross-reference).
- Updated: `index.md` (Themes; page count 222).
- Updated: `log.md`

## [2026-09-28] ingest | Burry AI capital cycle warning and Oracle Project Jupiter force majeure (4 articles)

- Sources: Yahoo Finance/GuruFocus (Sept 25), TheStreet (Sept 27), Morningstar Equity Research (Sept 24), Economic Times (Burry "Trump cannot afford to let AI boom fail"). Economic Times could not be opened directly (403 via fetch, blocked in browser); its claims were taken from the Yahoo/Stocktwits syndicated copy of the same story and a search snippet. Burry's original Substack posts were not read. TheStreet and Morningstar were read through Chrome after WebFetch returned 403.
- Created: `investing-fundamentals/company-analyses/themes/burry-ai-capital-cycle-oracle-jupiter-2026-09.md` (Burry's net investment/GDP and capital cycle argument, per-hyperscaler commitment estimates, Oracle ASC 606 prepayment critique and lease/contract duration mismatch, Jupiter force majeure with Morningstar's $25B+ revenue-at-risk read, disclosed shorts, source-disagreement table, watch list). `confidence: medium`, `contested: true`.
- Updated: `investing-macro/macro-frameworks/ai-compute-commencement-wall-and-refinancing-trap.md` (added cross-reference to the new page under Cross-References).
- Updated: `index.md` (indexed under Themes; page count 221).
- Updated: `log.md`

## [2026-09-28] ingest | Market and Investment Newsletter Digest (September 23, 2026)

- Ingested & Synthesized: `investing-macro/market-newsletter-digest-2026-09-23.md` (Synthesis of ~45 investment newsletters received on September 23, 2026, filtered from 73 keyword-matched messages: (1) Rates: the 58.4 flash PMI [five-year high] sent the 10Y to its highest close since July 2007 and the $70B 5Y auction to its highest yield since June 2006, Barr/Barkin/Goolsbee hawkish, October hike odds ~54% to ~70%, 30Y at ~5.35% through a multi-decade cap [Against All Odds], Alethea's rate-insulated vs. rate-sensitive bifurcation, Howell's 10Y-to-6% and 80% refinancing call, ECB ~100bp of hikes priced, VIX ~14.2 and MOVE 78.6 still suppressed, SMH normalized to 0.03σ while IGV is most stretched [Pinebrook]; (2) Energy: Trump diesel export ban talk at a $6.52 record [~2M bpd refinery cut risk], Brent back above $100 after Iran talks faded, China withholding ~3.5M bpd of seaborne imports, MacroEdge's $80-82 WTI floor; (3) Consumer Inertia selloff after Meta's Muse [Goldman 55-name basket, XLF lowest since July 1, Schwab -6.1%, PLNT -9.5%, Micron +5% on $31.5B turnover], Levine on "latent cash," JPM's O'Dwyer on a positioning unwind, Amazon opening seller tools to Claude [$46.8B seller fees > AWS revenue]; (4) Model price war: Opus 5.5 at $4/$20 [-20% list, ~40% cheaper per task at medium, no saving at max effort per Artificial Analysis] vs. GPT-6 Sol $2/$10 and Luna $0.10/$0.50, DeepSeek V4.1 Flash #1 on OpenRouter [+170% w/w], Citadel Securities Jevons evidence, Nvidia NVLink Fusion; (5) Buildout financing: SixSigma CoreWeave teardown [$103.7B RPO, $46.07B net debt, $640M quarterly interest, $10.6B due by 2027, DDTL 4.0 at SOFR+225/A3 vs. B+ corporate, Microsoft walked from $12B option], SemiAnalysis ClusterMAX 3.0 [Nebius to Platinum, Nvidia "Balance Sheet Is The Moat," 100% prepays], FT/Tooze on $300B of Big Tech residual value guarantees, SoftBank bonds at up to 9.875%, $575B AI debt YTD, AWS insiders on a $500B backlog, 5GW-to-2GW Anthropic ramp, 12-15 month enterprise pilots and 4-5 year AI server paybacks, NVDA under 17x forward; (6) China: Alibaba 20GW by 2032 as a T-Head bet [Goldman 5-6GW today, T-Head 10% to ~50%], Xi visit [Gewirtz "flipped script," Triolo on the thin AI hotline], Wuttke on overcapacity [1 container out per 4 in, EUR 1B/day deficit], Baiguan on Hefei; (7) Market structure: Kalshi Klear margin filing for event contracts, a16z on $117.3B/month RWA perps [44x YoY, 86% onchain, equities 48%], NEAR Intents, Howell on Bitcoin liquidity, ETHA spot-vol correlation +0.39; (8) Company notes: PSKY/WBD [$110B EV at 12.5x EBITDA], Berkshire into Lennar vs. KB Home warning, Rocket Lab bear case, Quanta organic backlog, AppLovin buyback math, EBITDA adjustments and AI-enabled AP fraud).
- Updated: `index.md` (Cataloged `market-newsletter-digest-2026-09-23.md`, bumped page count to 220, updated date to 2026-09-28).
- Updated: `log.md`

## [2026-09-27] create | Diversified Portfolio Backtests (1972-2025)

- Created: `investing-quant/strategies/balanced-portfolios/diversified-portfolio-backtests-1972-2025.md` (Write-up of the three-layer backtest in `investing-quant/backtests/`: P1 20 gold / 20 10y Treasury / 60 US stocks led on return in every window with real data [10.54% 1972-2025, 8.92% 2001-2025]; the Golden Butterfly led on risk [worst year -8.9%, only positive real return in CPI > 6% years]; international tilts cost about 1 point a year since 1972 and 1.7 since 2001; trend-following helped in every version but the real CTA index added only 0.5 points a year; TIPS lost to T-bills in inflation years and deepened P1's 2008 loss to -21.6%; returns fell 1.6-2.4 points from the 1972 to the 2001 window because of lower inflation, lower starting yields, and high starting valuations).
- Updated: `index.md` (Cataloged under Quant > Strategies, bumped page count to 219, updated date to 2026-09-27).
- Updated: `log.md`

## [2026-09-23] ingest | Market and Investment Newsletter Digest (September 22, 2026)

- Ingested & Synthesized: `investing-macro/market-newsletter-digest-2026-09-22.md` (Comprehensive institutional synthesis of ~68 market and technology newsletters received on September 22, 2026, filtered from 83 keyword-matched messages: (1) The Fed's Second Act: Copper's Record Chase & a Framework Losing Its Risk-On Majority: The Lead-Lag Report on the Fed's 25bp hike to 3.75-4.00% [12-0, Warsh] confirmed by copper's 11th weekly advance in 12 [within 1.1% of the $14,875 record] and a 14.81 VIX, plus its separate Weekly Signals framework flipping to a risk-off composite [-18] for the first time since July as Treasury Rotation flipped defensive [TLT +0.73% vs IEF +0.12% in August] and Lumber/Gold hit a 19.38-point spread, alongside Callum Thomas's dot-com-echo tech-vs-defensive valuation chart and Morningstar on Fed-hike headwinds for PE exits; (2) The AI Data-Center Overbuild Debate: Ed Zitron's forensic argument that under 50% of $1.2T+ hyperscaler capex since 2022 has become operational AI capacity [$390B+ uninstalled, Microsoft's "12GW total / 2GW AI-specific" discrepancy, NVIDIA/Broadcom's $561.5B in sold AI silicon roughly half warehoused] versus Michael Parekh's AI-RTZ #1217 gigawatt/token-loop economics [$47B/GW Vera Rubin, 100T tokens/day], plus The Diligence Stack's power-reliability interview and Klement on Investing's chip-ban efficacy data [China's global semiconductor share up 18% 2017-2023 despite US export bans]; (3) Nscale's $35B IPO: Mostly Metrics's S-1 breakdown [$103.4B contracted value vs $2.6B live, Microsoft/Anthropic 85% of backlog, negative gross margins, NVIDIA vendor-financing loop, CoreWeave comp at ~90x run-rate]; (4) Agentic Commerce's First Turf War: Amazon blocking Meta's Muse from shopping [The Neuron, Michael Parekh's ARD #168 on Xi's low-CEO-count Washington visit & GPT-6 Sol/Opus 5.5 same-day launch] and Citrini's "Agentic Reality" disintermediation framework [beneficiaries/pairs/losers since its Feb 2026 thesis]; (5) Tokenization as Monetary Plumbing: Jordi Visser's "Wealth Becomes Money" M×V=P×Y liquidity-supply thesis against $195.9T household net worth, and Coin Metrics on the SEC's September 17 Innovation Exemption for tokenized stocks [Binance bStocks $3.7B monthly volume, Kraken xStocks $3B onchain cap]; (6) Corporate Governance Under Strain: Matt Levine on Silver Lake's bid to eliminate Delaware appraisal rights in the Endeavor/TKO buyout [TKO stake alone worth more than the entire $27.50/share deal price by closing] and the Steak 'n Shake index-fund broadside; (7) Geopolitics: Doomberg's "Escalation Clauses" on Ukrainian strikes across 1M+ bpd of Russian refining capacity amid record $10.50/gallon French diesel and Merz's CDU historic-worst regional election result).
- Updated: `index.md` (Cataloged `market-newsletter-digest-2026-09-22.md`, bumped page count to 218, updated date to 2026-09-22).
- Updated: `log.md`

## [2026-09-22] ingest | Market and Investment Newsletter Digest (September 21, 2026)

- Ingested & Synthesized: `investing-macro/market-newsletter-digest-2026-09-21.md` (Comprehensive institutional synthesis of 61 market and technology newsletters received on September 21, 2026, filtered from 81 keyword-matched messages: (1) Lehman-Era Real Yields: Auction Stress & the Buyer Base: TSCS Research dissecting the 16 September 10Y TIPS real yield at 2.68% [5.01% nominal = 2.68% real + 2.33% breakeven] via record-weak Treasury auctions [30-year dealer share of 2.2%, lowest in 14 years; 20-year dealers holding 17% vs. 11% average; MOVE index at 81 vs. 135 in Oct 2023 at the same yield] and buyer-base forensics showing Japan's $135B Treasury runoff was mostly cash paydown not duration selling while insurers added $119B→$152B, alongside The Lead-Lag Report's XLK/SPY +2.65σ vs. XLU/SPY -3.01σ dispersion confirming the Fed's 25bp hike to 3.75-4.00% [12-0] and BOJ's hike to 1.25% [31-year high], and Charlie Bilello's direct Warsh quote on 5+ years of above-target inflation; (2) AI Lab Economics: Safety Narrative, Captive Insurance & the Four Overhangs: Arthur Hayes on Anthropic/OpenAI/SpaceX's "Safety First" pivot as compute-demand-destruction cover for >$1T of AI-backing debt, detailing a $1.54T captive-reinsurance "Affil Reins" scam [Apollo/KKR/Brookfield insurers, Vermont-domiciled reinsurers, Terra/Luna parallel] with a Bitcoin-bullish bailout-or-buyer-of-last-resort thesis, and Ben Thompson's Stratechery "Frontier Overhangs" framework [Capability, Product, Pricing, Capital Overhangs] independently reaching the same skepticism via Anthropic's Fable data-retention reversal, Meta Muse's stickiness threat, and the Jay Cooke/Northern Pacific 1870 financing parallel; (3) AI Infrastructure: CPU:GPU Ratios & Optical Disputes: The Diligence Stack's "Secret Agent CPU" scale-up domain thesis [GB200 NVL72's 36:72 baseline, Nvidia Vera CPU Rack, Arm AGI CPU], Irrational Analysis's ECOC-timed teardown alleging Coherent's CPO/NPO laser fails the 1MHz effective-linewidth spec and Cerebras's waveguide link-budget is unworkable, and SemiAnalysis's four-regime [prefill/midfill/decode-attention/decode-experts] inference-serving mechanics; (4) The Dollar as Portfolio Currency: Adam Tooze/Chartbook on the 2000-2015 reserve-accumulation era as historically exceptional, Brad Setser's finding that foreign dollar-asset purchases have shifted toward funding corporate America since the early 2020s, and JPMorgan's Cembalest on no near-term reserve-currency rival; (5) Forensic Audits: Babylon Burns's CENTCOM "1 billion barrel" Hormuz-oil-flow math [implying an implausible 31.8M bbl/day, 150% of prewar throughput] and Michael Burry's cryptic copper-signal "Trading Post" allegory amid the AI melt-up; (6) Company Deep Dives: Expanse Stocks's "Palantir as enterprise operating system" thesis, In Practise's Meta Reality Labs insider account of organizational silos and a 40% smart-glasses underperformance, Verdad Capital's TSE Value-Up reform data [sub-0.7x P/B universe share falling 31%→16% in four years], and Tanay Jaipuria's Agility Robotics SPAC financials [$1.8M 2025 revenue vs. $140M operating loss, $2.5B pre-money via Churchill Capital XI]; (7) Crypto: The Block's Zcash Ironwood shielded-pool migration [3.9M ZEC, 80% share] tied to Hayes's AI-debt-to-Bitcoin transmission thesis).
- Updated: `index.md` (Cataloged `market-newsletter-digest-2026-09-21.md`, bumped page count to 217, updated date to 2026-09-21).
- Updated: `log.md`

## [2026-09-21] ingest | Market and Investment Newsletter Digest (September 20, 2026)

- Ingested & Synthesized: `investing-macro/market-newsletter-digest-2026-09-20.md` (Comprehensive institutional synthesis of 55 market and technology newsletters received on September 20, 2026: (1) Lehman-Era Real Yields & The Refinancing Machine: TSCS Research on 10-year TIPS real yields touching 2.68% [highest since Nov 26, 2008 post-Lehman] with nominal 10Y Treasuries at 5.01% [2.68% real + 2.33% breakeven], Michael Howell on 70–80% of capital markets being pure debt refinancing with 77% collateral backing, and The Lead-Lag Report on XLK/SPY surging to +2.65 sigma while XLU/SPY collapses to -3.01 sigma; (2) Physical Commodity Bottlenecks: Apollo Chief Economist Torsten Slok on zero major copper discoveries in 2025 and an 18-year discovery-to-production lag creating a severe 2040s supply mismatch against 2-to-3 year datacenter cycles, and SpotGamma on WTI >$100 / record $6.31/gal diesel with suppressed OVX and heavy short call positioning on COP/XOM/CVX; (3) AI-Native Revenue Velocity & Software Multiple Spreads: OnlyCFO on ICONIQ Pacesetter Index top-decile AI startups scaling to $100M ARR in quarters [rendering T2D3 obsolete], public software multiple spreads reaching 3.4x for high-growth vs slower peers, and Mercury challenging QuickBooks in general ledgers; (4) Agent Swarms, Navier-Stokes & Crypto Ghost Rails: Jordi Visser on 10,000 parallel agents solving century-old Navier-Stokes in 88 hours, negative ex-healthcare US hiring for 20 straight months vs 30% S&P profit growth, and autonomous agents filling blockchain rails for programmatic micro-settlement; (5) Forensic Audits & Big Tech Assets: Edwin Dorsey's Bear Cave #344 covering Hub Group, Raiffeisen Russia trade, Astrana Health, and Jackson Financial, alongside Alphabet's $205B capex anchored by YouTube $40B+ ad run-rate, Waymo, and SpaceX $94.1B stake).
- Updated: `index.md` (Cataloged `market-newsletter-digest-2026-09-20.md`, bumped page count to 216, updated date to 2026-09-20).
- Updated: `log.md`

## [2026-09-21] ingest | Market and Investment Newsletter Digest (September 19, 2026)

- Ingested & Synthesized: `investing-macro/market-newsletter-digest-2026-09-19.md` (Deep institutional synthesis of 43 market and technology newsletters received on September 19, 2026: (1) Hyperscaler Semiconductor Bifurcation: Tech Investments analysis showing SpaceX deploying 16GW by 2028 as Nvidia's anchor customer (~35% of revenue, zero discounts, Austin Terafab) vs Broadcom's massive guidance sandbagging [17–19GW across Anthropic TPU v8i, OpenAI Jalapeno, and Meta MTIA yielding $425B–$475B potential revenue vs guided $230B]; (2) Frontier Lab Financials & Governance: OpenAI burn revised from $180B to $278B by 2030, Anthropic posting operating profit ex-SBC but delaying IPO past November elections, The Information on Amodei's tabloid era with NY Post attacks and Trump calling pacing a "SICK conspiracy", and GPT-6 Astra dominating Claude Fabel 5.1 in coding; (3) Chinese Optical Packaging & Memory Walls: Huawei Ascend 960 supernode eliminating 48,000 800G transceivers for 5,500 proprietary NPO engines entering volume production, and Michael Parekh on multi-turn context compaction as the modern "640K" limit; (4) The Warsh Monetary Doctrine: Chairman Kevin Warsh orchestrating a unanimous 12-0 FOMC vote to raise rates by 25 bps six weeks before midterms, ending 40 years of Fed forward-guidance spoon-feeding as the Fed follows market rates; (5) Capital Flow Euphoria & Blockchain Law: Callum Thomas on Tech ETFs capturing 50% of sector ETF AUM alongside margin debt warnings, and a16z crypto legal teardown showing BSA/AML does not mandate bank private blockchains).
- Updated: `index.md` (Cataloged `market-newsletter-digest-2026-09-19.md`, bumped page count to 215, updated date to 2026-09-19).
- Updated: `log.md`

## [2026-09-20] ingest | Market and Investment Newsletter Digest (September 18, 2026)

- Ingested & Synthesized: `investing-macro/market-newsletter-digest-2026-09-18.md` (Comprehensive institutional synthesis of 53 market and technology newsletters received on September 18, 2026: (1) Frontier AI Pacing, Recursive Self-Improvement, and the "AI Three Mile Island" governance dilemma: Dario Amodei, Sam Altman, Elon Musk, and Demis Hassabis alignment on pacing, METR investigation into the OpenAI–Hugging Face 1,200-agent cluster breach, evaluation failure modes (Noam Brown), Jamin Ball on IAEA embedded evaluators vs. the 1979 Three Mile Island 40-year nuclear freeze, Anthropic disclosing 26% of AI R&D led by Claude, OpenAI 3.1:1 agent-to-human workdays, pacing as a non-compressible time constraint, and open-weight margin compression eroding closed labs' 60% price premium and 90%+ revenue share; (2) Specialized Hardware Codesign & Memory Hierarchy: SemiAnalysis DeepSeek V4.1 Flash Day 7 serving benchmarks, Nvidia CUDA Day 0 zero-issue support vs AMD ROCm 23-hour delay and 14.8x–42x worse perf/dollar, host DRAM UVA offload unlocking B300 TP4-to-TP2 transition (+1.6x Pareto gain), SSD offload economic failure (52M vs 121M tokens/$), 4-hi HBM bandwidth sweet spot toward 0Hi stacks, TSMC Kaohsiung "Baipu Plan" CoWoS validation line, and Beth Kindig on Micron's structural AI memory supercycle; (3) Energy & Geopolitical Bottlenecks: SemiAnalysis tracking 75GW of firm binding orders for Behind-the-Meter (BTM) on-site power (20GW in Q2 2026 alone), AWS datacenter drone strikes in Bahrain/UAE causing permanent data loss, Gulf SWFs representing 25% of global AI capital facing oil export contraction, and Brent at $103/bbl alongside record diesel prices and Strait of Hormuz chokepoint constraints; (4) Macro Rates & Sovereign Debt Plumbing: 10-year Treasury testing 4.90%–5.00%, Michael Howell on normal bond cycle repricing driven by strong nominal GDP, Andy Constan dismantling the $1.5T hedge fund Treasury basis trade panic, and QTR/ZeroHedge analysis of monetizing statutory U.S. gold reserves [$1.3T–$2.6T at $5k–$10k/oz] via Fed gold certificates; (5) Cloud Software & Corporate Governance: Jamin Ball SaaS benchmarks [4.2x median EV/NTM Rev, 21% FCF margin], Meta Muse browser agent vs Benchmark-backed Instinct [$10B valuation], BlackRock Jay Jacobs on $IBIT financialization/borrowing mechanics, and Warren Buffett stepping down after 56 years at Berkshire Hathaway).
- Updated: `index.md` (Cataloged `market-newsletter-digest-2026-09-18.md`, updated page count to 214, updated date to 2026-09-18).
- Updated: `log.md`

## [2026-08-27] create | DAVE Interactive HTML Research Suite

- Created: `investing-fundamentals/company-analyses/dave-investment-research.html` (Interactive dark-mode institutional research and stress-test application consolidating Stages 1–4 for Dave Inc.: (1) Multi-tab navigation across Executive Dashboard, Business Model & $37 FCF Waterfall, Investment Memo & 2-Year Valuation Explorer, Adversarial Stress-Test & 6 Iceberg Risks, 6-Column KPI Watch List & Sizing, and Verified Sources; (2) Interactive scenario switchers for Bear/Base/Bull IRR and Downside Stress-Test flow-through; (3) Client-side quick search filter, collapsible deep dives, and print-ready CSS).
- Updated: `index.md` (Cataloged `dave-investment-research.html`, updated page count to 210).
- Updated: `log.md`

## [2026-08-27] create | SEZL Interactive HTML Research Suite

- Created: `investing-fundamentals/company-analyses/sezl-investment-research.html` (Interactive dark-mode institutional research and stress-test application consolidating Stages 1–4 for Sezzle Inc.: (1) Multi-tab navigation across Executive Dashboard, Business Model & $41 FCF Waterfall, Investment Memo & 3-Year Valuation Explorer, Adversarial Stress-Test & 6 Iceberg Risks, 6-Column KPI Watch List & Sizing, and Verified Sources; (2) Interactive scenario switchers for Bear/Base/Bull IRR and Downside Stress-Test flow-through; (3) Client-side quick search filter, collapsible deep dives, and print-ready CSS).
- Updated: `index.md` (Cataloged `sezl-investment-research.html`, updated page count to 209).
- Updated: `log.md`

## [2026-08-27] create | DAVE Stage 4 Bull/Bear Stress-Test & Adversarial Audit

- Created & Audited: `investing-fundamentals/company-analyses/dave-4-stress-test.md` (Stage 4 Adversarial Institutional Debate and Iceberg Risk Audit: (1) Added "The 6 Iceberg Risks of Dave ($DAVE)" matrix to Executive Summary; (2) Detailed legal & regulatory analysis covering TILA Regulation Z § 1026.4(a), FTC/DOJ federal complaint (Case No. 2:24-cv-09419, C.D. Cal. naming Jason Wilk individually), Baltimore 33% usury lawsuit under MCLL, state safe-harbor statutes [MO, NV, KS, WI] vs hostile states [CA, NY, CT, MD], and Section 27 FDIA interest rate preemption via Coastal Community Bank; (3) Audited Multi-Factor Downside Stress-Test financial statement flow-through with ASC 326 CECL reserve mechanics, reconciling 2-Yr stagnation bear target [$105–$112] with acute stress scenarios [Scenario A: $84.00; Scenario B: $32.50]; (4) 6-column KPI Watch List and 2.5%–4.0% Portfolio Sizing Framework with explicit de-risk triggers).
- Updated: `investing-fundamentals/company-analyses/dave-3-investment-memo.md` (Cross-referenced Stage 4 stress-test).
- Updated: `index.md` (Cataloged $DAVE stages 1–4, updated page count to 208).
- Updated: `log.md`

## [2026-08-27] init | Install investment-stress-test skill for Gemini / Antigravity

- Installed: `.agents/skills/investment-stress-test/SKILL.md` (Extracted from `investing-fundamentals/company-analyses/investment-stress-test.skill` into the active workspace skill discovery path `.agents/skills/investment-stress-test/`, enabling Gemini and Antigravity CLI agents to discover and run adversarial 3-agent bull/bear/arbitrator stress-tests).
- Updated: `log.md`

## [2026-08-27] create | SEZL Stage 4 Bull/Bear Stress-Test & Iceberg Risk Audit

- Created & Audited: `investing-fundamentals/company-analyses/sezl-4-stress-test.md` (Stage 4 Adversarial Institutional Debate and Iceberg Risk Audit: (1) In-depth 4-section Bull Case vs 4-section Bear Case with Arbitrator Shared Facts / 3 Crux Assumptions framework; (2) Detailed legal & regulatory analysis covering TILA Regulation Z § 1026.4(a), California DFPI 2019-2020 consent order ($582k penalty), NY DFS usury limits (16% civil / 25% criminal), RISA merchant sale vs direct loan distinctions, Dodd-Frank § 1075 Durbin debit exemption under WebBank, and OCC Tier 1 Leverage (8%–10%) / Total Capital (12%–14% on 100% RWA) capital lockup ($150M–$250M) causing ROTE to drop from >55% to 15%–18%; (3) Audited Multi-Factor Downside Stress-Test financial statement flow-through across Scenario A Credit Shock [$53.12 PT] and Scenario B Compound Stress [$27.44 PT]; (4) 6-column KPI Watch List and Portfolio Sizing Framework).
- Updated: `investing-fundamentals/company-analyses/sezl-3-investment-memo.md` (Cross-referenced Stage 4 stress-test).
- Updated: `index.md` (Cataloged $SEZL stages 1–4, updated page count to 207).
- Updated: `log.md`

## [2026-08-26] create | SEZL company analysis pipeline

- Created: `investing-fundamentals/company-analyses/sezl-1-document-sources.md` (Complete SEC EDGAR 10-K/10-Q filing directory, CIK 0001662991, shareholder briefing history, WebBank sponsorship details, and OCC National Bank charter application roadmap with SHA256 verification).
- Created: `investing-fundamentals/company-analyses/sezl-2-equity-report.md` (Comprehensive equity research report evaluating Sezzle's hybrid subscription-gated BNPL model, $183M recurring ARR, 854k Sezzle Anywhere subscribers, 50.0% Adjusted EBITDA margin, 85.0% Rule of 40 score, ~14x capital velocity, $41 FCF per $100 revenue unit economics, and full historical volatility decomposition with top 5 market-moving operational metrics).
- Created: `investing-fundamentals/company-analyses/sezl-3-investment-memo.md` (Institutional investment memo establishing a BUY/LONG thesis with a $235.00 target price (+88% upside), 3-year valuation sensitivity matrix, Pre-Mortem failure mode framework, 12-month KPI watch list, and guidance-treadmill volatility mechanics).
- Updated: `investing-fundamentals/company-analyses/comparisons/fintech-business-models-dave-vs-peers.html` (Added Sezzle historical volatility and market-moving metrics callout).
- Updated: `index.md` (Cataloged $SEZL under Companies, updated page count to 206).
- Updated: `log.md`

## [2026-08-25] create | Consumer FinTech Business Model, Valuation, Solvency & Cash Flow Architecture ($DAVE vs Peers)

- Created & Enhanced: `investing-fundamentals/company-analyses/comparisons/fintech-business-models-dave-vs-peers.html` (Comprehensive institutional equity research and UI/UX dashboard comparing Dave Inc. ($DAVE) against $SEZL (Sezzle), $AFRM (Affirm), $XYZ (Block / Cash App), $SOFI (SoFi), $CHYM (Chime), $KLAR (Klarna), $BFH (Bread Financial), and $ML (MoneyLion). Fully audited & enhanced via dual-pass Claude Code review: (1) 100% peer representation across all sections including 9 dedicated deep-dive cards in Section 3, 9-ticker coverage in Section 2, Section 6, and Section 8, and balanced cash conversion waterfalls in Section 7 contrasting high-velocity advances vs revolving store card banks ($BFH); (2) Solvency Architecture benchmarking Tangible Common Equity (TCE/TA), CET1 ratios, total liquidity ($260M for Dave, $1.85B for Affirm, $23B deposits for SoFi), net cash/debt, loss reserve coverage (ACL), and Loss Absorption Factors (Dave 3.55x, Sezzle 3.81x, Affirm 2.45x, BFH 1.07x); (3) Synchronized JavaScript visualization engine rendering normalized 9-ticker bars across Forward GAAP P/E, EV/EBITDA, Rule of 40 (Dave 88.8%, Sezzle 85.0%), and Loss Absorption Factors; (4) Institutional UI/UX polish featuring 2D sticky table headers/first-columns, WCAG AA dark-mode contrast (5.5:1 to 17.5:1), and WAI-ARIA tab navigation with URL hash routing).
- Updated: `index.md`
- Updated: `log.md`

## [2026-08-24] ingest | Market and Investment Newsletter Digest (August 20, 2026)

- Ingested & Synthesized: `investing-macro/market-newsletter-digest-2026-08-20.md` (Exhaustive synthesis of 54 substantive newsletters and research reports received on August 20, 2026: (1) Groundbreaker & Simon Taylor on the 2/28 ARM compute reset wall, >$2.3T in contracted cloud RPO, 24–36 month construction teasers, OpenAI's >200% revenue coverage deficit, Nvidia's $6B Poolside licensing backstop / $12B valuation, Stripe acquiring OpenRouter, and CFTC AI compute futures; (2) Unitree Robotics' STAR Market IPO surging +460% to $50B (1,190x P/E), founder Wang Xingxing resetting the commercial "ChatGPT moment" to 3–5 years, FCC foreign advanced robotics bans, and WisdomTree WDRN physical AI fund launch; (3) U.S. national debt surpassing $40.0 Trillion ($8.6B/day), Michael Howell on "Treasury QE" and "Bills Are The Pills" vs Fed rate transmission, Treasury Secretary Bessent doubling long-end buybacks to >$4B/operation following 30-year yields touching 5.34%, David Cervantes on the July 27 term-premium regime break, and Torsten Slok on structural rate insensitivity; (4) The Bear Cave on Guggenheim CEO Mark Walter's $17B insurer probe and Guggenheim Strategic Opportunities Fund's ($GOF) 125-month above-NAV ATM share issuance machine shutdown under Section 23 of the 1940 Act, Sharpe Two on UVIX short-vol roll decay, Moderna's +177% Phase 3 mRNA cancer vaccine breakthrough, TSOH on Roblox's bookings normalization, and Meta's engineering brain drain retainer equity counteroffers).
- Updated: `index.md`
- Updated: `log.md`

## [2026-08-21] update | CRCL company analysis pipeline (Claude Code reviewed & enriched)

- Updated: `investing-fundamentals/company-analyses/crcl-2-equity-report.md` (Incorporated Claude Code review feedback: reconciled FY26E revenue model and H2 Arc platform ramp, updated realized reserve yield series ~3.63%, clarified native USDC gas mechanics with zero unbacked tokens, refined OCC Trust Charter scope and Fed master account access nuance, accurate statutory placement of stablecoin yield restrictions under GENIUS Act §4(a)(11), and expanded competitive matrix with bank deposit tokens and Stripe/Bridge).
- Updated: `investing-fundamentals/company-analyses/crcl-3-investment-memo.md` (Restated 3-year valuation framework incorporating explicit tax, SBC dilution, and calibrated shares ~270M -> 285M FY28: $100.80 Base / $192.50 Bull / $21.60 Bear price targets, probability-weighted expected value $107.89 (+50.9% return), added Depeg/Run risk & Tokenized-MMF substitution to Risk Matrix, and updated 12-month KPI watch list).
- Refactored: `investing-fundamentals/company-analyses/CRCL.md` (Converted into a clean, concise routing hub with YAML frontmatter, eliminating duplicated/divergent legacy metrics).
- Updated: `log.md`

## [2026-08-21] ingest | Market and Investment Newsletter Digest (August 19, 2026)

- Ingested & Synthesized: `investing-macro/market-newsletter-digest-2026-08-19.md` (Deep synthesis of 14 key newsletters and institutional research reports received on August 19, 2026: (1) Ben Thompson & Michael Parekh on AI capital curve exhaustion, Nvidia $500B Wall Street AI Infrastructure Consortium, OpenAI $7B self-tender at $852B valuation, Anthropic $9.1B–$16.1B Riot compute deal, and developer software deflation; (2) U.S. Treasury doubling long-end buybacks to $4B/operation, George Noble & Andy Constan on the "Bessent-put" / short US Treasuries steepener, Arthur Hayes on sovereign debt monetization, and $1.44B crypto short squeeze; (3) Custom AI Silicon & Optical Infrastructure: Google $120B Marvell co-design deal with 59M share warrant, Broadcom gross margin compression, FUNDA 6D Torus 4x optical uplift, Cerebras CS-4 3nm wafer-scale processor launch, and 500% memory price spike "RAMageddon"; (4) Alexander Stahel on China as the new crude oil swing producer and QTR on BNPL/subprime consumer liquidity exhaustion)
- Updated: `index.md`
- Updated: `log.md`

## [2026-08-21] create | DAVE company analysis pipeline (Claude Code reviewed & enriched)

- Created & Updated: `investing-fundamentals/company-analyses/dave-1-document-sources.md` (Ingested FY2021-FY2025 10-Ks, Form S-4/A SPAC merger proxy, FY2026 10-Qs, Investor Day presentations, Coastal Community Bank sponsorship agreement, Victory Park Capital $150M credit facility, FTX $100M note settlement, and sell-side consensus baselines; computed sha256 `0b539d3fd1f121c19c411ac1d061f8180585c660833c721e3c23797bea05c7a4`)
- Created & Updated: `investing-fundamentals/company-analyses/dave-2-equity-report.md` (Full fundamental equity research synthesis: $730M revenue run-rate, $320M Adj EBITDA / 44% margin, 3.08M MTMs, $9.2B ExtraCash origination run-rate, dual take-rate metrics 4.80% service / 7.43% platform, CashAI v6.0 underwriting precision, $19 CAC with <35 day payback, Coastal Community Bank depository sponsor architecture, FTC inquiry resolution, comprehensive 5-segment competitive landscape breakdown, and >35x annual capital turnover)
- Created & Updated: `investing-fundamentals/company-analyses/dave-3-investment-memo.md` (High-conviction BUY / High-Velocity FinTech Compounder memo at ~$335.00: 2-year Sensitivity Matrix modeling $550.00 Base (+28.1% 2-Yr IRR) / $850.00 Bull / $112.00 Bear price targets, probability-weighted expected value of $522.40 (+55.9% expected return), multi-method valuation triangulation, granular competitive benchmarking matrix (EarnIn, Brigit, MoneyLion, Chime, Cash App, DailyPay, Legacy Banks), 5-factor risk scoring matrix, pre-mortem failure mode, and 12-month KPI watch list with data sources)
- Updated: `index.md`
- Updated: `log.md`

## [2026-08-21] create | AFRM company analysis pipeline (Claude Code reviewed & enriched)

- Created & Updated: `investing-fundamentals/company-analyses/afrm-1-document-sources.md` (Ingested FY2021-FY2025 10-Ks, Form S-1/A, FY2026 10-Qs, Investor Day presentations, Apple Pay, Shopify, Amazon commercial partnerships, industrial bank partner origination agreements (Cross River Bank, Celtic Bank), ABS Fitch rating actions, and Wall Street sell-side consensus baselines; computed sha256 `9de5ecea351ee5cf0d141f035c75ec7b86c02fa82fce93fdab9a9f0713b8372b`)
- Created & Updated: `investing-fundamentals/company-analyses/afrm-2-equity-report.md` (Full fundamental equity research synthesis: $48B GMV run-rate, $4.25B revenue, 24.1M active users, RLTC unit economics ~3.75-4.0% of GMV / 42.4% of revenue, Affirm Card +159% YoY acceleration, Apple Pay native iOS distribution, bank partner FDIA Section 27 rate exportation, $28.2B capital marketplace decomposition, interest rate repricing gap asymmetry, comprehensive credit metrics with measurement bases (2.1% NCOs, 6.1% ACL coverage), reciprocal link to Dave velocity contrast, and proprietary SKU-level underwriting moat)
- Created & Updated: `investing-fundamentals/company-analyses/afrm-3-investment-memo.md` (High-conviction GARP/Compounder investment memo at ~$76.50: 2-year Sensitivity Matrix modeling $130.00 Base (+30.4% 2-Yr IRR) / $240.00 Bull price targets (+77.1% 2-Yr IRR), dual GAAP P/E & ROTE valuation framework, peer benchmarking matrix (Klarna, Block, PayPal, Synchrony), corporate EV bridge with SBC share dilution, 5-factor risk scoring matrix, pre-mortem failure mode, August 27, 2026 earnings catalyst execution strategy, and enhanced 12-month KPI watch list with data sources)
- Updated: `index.md`
- Updated: `log.md`

## [2026-08-14] create | CRCL company analysis pipeline (Q2 2026 results, Arc L1 launch, GENIUS Act & MiCA)

- Created: `investing-fundamentals/company-analyses/crcl-1-document-sources.md` (Ingested IPO Form S-1/A, FY2025 10-K, Q1 & Q2 2026 10-Qs, OCC National Trust charter, EU MiCA EMI license, BlackRock USDXX audit attestations, and Coinbase renewal agreement; computed sha256 `53ff5f1ca17ffee43f2c1cc966e82b8ffaab0720db27c589adb000fe06d9f1c3`)
- Created: `investing-fundamentals/company-analyses/crcl-2-equity-report.md` (Full equity research synthesis: $73.3B USDC circulation, $14.8T quarterly on-chain volume, Q2 2026 financials $701M rev / $143M Adj EBITDA, Arc Blockchain institutional L1 launch on Sept 16, 2026, GENIUS Act and MiCA regulatory moat, Coinbase revenue-share mechanics, and competitive benchmarking vs Tether, Stripe Bridge, and USDG)
- Created: `investing-fundamentals/company-analyses/crcl-3-investment-memo.md` (High-conviction BUY investment memo at ~$71.50: 3-year Sensitivity Matrix modeling $116.80 Base / $261.00 Bull price targets, Interest Rate Easing and Coinbase dependency risk framework, Pre-Mortem failure mode, and 12-month KPI watch list)
- Updated: `index.md`
- Updated: `log.md`

## [2026-08-14] update | APP company analysis pipeline (JPMorgan initiation & Q2 2026 results)

- Updated: `investing-fundamentals/company-analyses/app-1-document-sources.md` (Ingested JPMorgan Aug 14, 2026 coverage assumption report, Q2 2026 10-Q, 8-K regulatory disclosure, and verified filing links; computed sha256 `dc2534791c47fd16d14fe52204578233eac360a76e717abdf8b312abf7ca975a`)
- Updated: `investing-fundamentals/company-analyses/app-2-equity-report.md` (Integrated JPMorgan institutional market share validations: >70% MAX mediation share, >40% DSP share; detailed consumer/e-commerce ad model: 9% of Q2 spend, $777M in 2026E, $1.4B in 2027E; Unity Vector & Meta competitive analysis; Q2 financials $1.92B rev / 84% EBITDA margin / $5.2B 2026E FCF; SEC investigation formal closure)
- Updated: `investing-fundamentals/company-analyses/app-3-investment-memo.md` (Updated high-conviction GARP/Compounder thesis contrasting our $638 Base / $1,178 Bull price targets against JPMorgan's $400 Dec 2027 PT / 18x 2028 EPS $22.42; integrated Unity Vector & Meta threat analysis, $1.8B buyback authorization, and updated 12-month KPI watch list)
- Updated: `investing-fundamentals/company-analyses/app-4-stress-test.md` (Annotated JPMorgan's Neutral initiation, gaming durability questions, and consumer revenue benchmarks)
- Updated: `index.md`
- Updated: `log.md`

## [2026-08-14] ingest | Market and Investment Newsletter Digest — August 14, 2026

- Created: `investing-macro/market-newsletter-digest-2026-08-14.md` (Digest of key themes: Bob Elliott on the AI "expectations mania", post-WWII record 25% annual earnings growth assumption, margin expansion paradox and 8% productivity impossibility, $5T circular vendor loop vs. $130B–$150B real AI revenues, 2008 banking contagion parallel, the "Kellogg's" real-economy test, -15% household savings math, and portfolio defense across TIPS, gold, European/Japanese value, and biotech)
- Updated: `index.md`
- Updated: `log.md`

## [2026-08-13] ingest | Market and Investment Newsletter Digest — August 13, 2026

- Created: `investing-macro/market-newsletter-digest-2026-08-13.md` (Digest of key themes: Robotti & Company Advisors Q2 2026 Letter on real assets vs. AI digital mania, atoms vs. bits bottleneck, public replacement-cost discounts, Subsea 7/Saipem merger, North American stranded natural gas, and Builders FirstSource housing reset; MacroVoices #545 with Michael Howell on the 65-month liquidity cycle rollover into 2027, 2-year yield vs SOFR rate hike signals with 85% accuracy, 6% 10-year Treasury yield trajectory, China's $4,000+ gold floor, $135–$200/bbl oil ratio, GLD 3:1 call spread setup, and Black Sea wheat short squeeze)
- Created: `trading/interviews/20260813-michael-howell-macrovoices-transcript.md` (Raw interview and market desk transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-08-13] ingest | Market and Investment Newsletter Digest — July 28, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-28.md` (Digest of key themes: Torsten Slok on $275B+ hyperscaler CapEx consensus revisions and Big Tech FCF margin compression, off-balance-sheet GPU debt financing, John Hwang on why Nvidia and Microsoft back open-weights to counter Anthropic and AWS/GCP custom chips, Moonshot Kimi K3 $20M revenue sharing licensing, Kospi 11% circuit-breaker flash crash and semiconductor memory bullwhip, Cadence Design Systems record $6.2B backlog, pre-FOMC FCI looseness vs. Kevin Warsh rate hike risks, Palantir 2Q26 AIP growth momentum, DoorDash $82B local commerce moat, Netflix ad-tier unit economics, a16z on physical AI simulation moats, AI Street on $200M multi-agent quant portfolios, and Adam Tooze on compute dollar hegemony)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-28] ingest | Market and Investment Newsletter Digest — July 27, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-27.md` (Digest of key themes: $250B+ hyperscaler CapEx scrutiny vs 1990s telecom overbuild, circular vendor financing, OpenAI autonomous coding agents, MSFT Q2 Copilot preview, and Bitcoin miner power pivot)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-28] ingest | Market and Investment Newsletter Digest — July 26, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-26.md` (Digest of key themes: July FOMC collision & 4.70% 10-year Treasury yield spikes, Esther Yang macro analysis, sector rotation into value, Nvidia/Microsoft open-source alliance, and SaaS unit economics compression)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-28] ingest | Market and Investment Newsletter Digest — July 25, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-25.md` (Digest of key themes: "AI is Oil Not God" resource commoditization, open-source AI lobbying wars, tokenized stocks 5x boom, Indium-Phosphide substrate bottlenecks, and Tech Schism 22x MSFT options carry positioning)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-28] ingest | Market and Investment Newsletter Digest — July 24, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-24.md` (Digest of key themes: bond yield signals, George Noble rate warnings, TPW Advisory investment era discernment, oil supply revenge, Claude Opus 5 vibe checks, and Schiff vs Pomp gold/BTC bets)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-28] ingest | Market and Investment Newsletter Digest — July 23, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-23.md` (Digest of key themes: Google Cloud 36% margins, enterprise AI control layer, energy war premiums, and earnings volatility shorting)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-28] ingest | Monetary Matters — Next Financial Crisis Unlikely To Start in Private Markets | Nicholas Brooks

- Created: `investing-macro/podcasts/mv-next-financial-crisis-unlikely-to-start-in-private-markets-20260723.md` (Detailed summary of Nicholas Brooks on private credit fundamentals, conservative 40-50% LTVs, $1.2T+ PE sponsor dry powder, absence of mark-to-market bank run risks, and senior direct lending allocation)
- Created: `trading/interviews/20260723-nicholas-brooks-monetary-matters-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-27] ingest | Financial Sense — Jim Welsh on Gold's Next Leg, Oil, and Climbing Bond Yields | Jim Welsh

- Created: `investing-macro/podcasts/fs-golds-next-leg-oil-and-climbing-bond-yields-20260724.md` (Detailed summary of Jim Welsh on gold Elliott Wave 4 consolidation, Wave 5 upside targets, 10-year Treasury yields climbing past 5.0%+, and oil price second-wave inflation risks)
- Created: `trading/interviews/20260724-jim-welsh-financial-sense-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-27] ingest | Excess Returns — It Only Happens at Bottoms | Andy Constan

- Created: `investing-options/podcasts/er-options-extreme-at-the-highs-20260718.md` (Detailed summary of Andy Constan on options market skew extremes at all-time highs, short dealer gamma squeezes, the "Size of the Pie" macro limit, and zero-cost collar hedging)
- Created: `trading/interviews/20260718-andy-constan-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-27] ingest | 22V Research — AI’s Speed Crash: The Structural Bull Market Isn’t Over | Jordi Visser

- Created: `investing-macro/podcasts/22v-ais-speed-crash-structural-bull-market-20260725.md` (Detailed summary of Jordi Visser on algorithmic speed crashes, systematic volatility de-leveraging, ~16% S&P 500 earnings beat rates, credit spread stability, and long-term HBM memory scarcity through 2030)
- Created: `trading/interviews/20260725-jordi-visser-22v-research-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-27] ingest | Excess Returns — We Asked the Man Who Mapped the AI Economy If the Boom Is Real | Kai Wu & Azeem Azhar

- Created: `investing-macro/podcasts/er-we-asked-the-man-who-mapped-the-ai-economy-20260721.md` (Detailed summary of Kai Wu & Azeem Azhar on mapping the AI value chain, hardware profit concentration, hyperscaler ROIC compression, open-source LLM price deflation, and enterprise productivity lag)
- Created: `trading/interviews/20260721-azeem-azhar-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-27] ingest | RiskReversal Media — This Is How the AI Bubble Actually Pops | Dan Nathan & Guy Adami

- Created: `investing-macro/podcasts/rr-this-is-how-the-ai-bubble-actually-pops-20260724.md` (Detailed summary of Dan Nathan & Guy Adami on hyperscaler CapEx prisoner's dilemma, semiconductor bullwhip effect, memory market volatility, and Nifty Fifty historical bubble parallels)
- Created: `trading/interviews/20260724-dan-nathan-guy-adami-riskreversal-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-27] ingest | Basis Points — Google CRUSHES Earnings, CapEx Debate & Tesla Q2 | Steven Fiorillo & Amit

- Created: `investing-fundamentals/podcasts/bp-google-crushes-earnings-capex-debate-20260724.md` (Detailed summary of Steven Fiorillo & Amit on Google Q2 earnings blowout, GCP 36% margins, SpaceX GPU compute rental, Tesla Q2 margin collapse to 1.4%, and Microsoft FY27 $220B–$240B CapEx guide)
- Created: `trading/interviews/20260724-steven-fiorillo-amit-basis-points-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-27] ingest | 22V Research — Short-Term AI Fear, Long-Term Compute Scarcity | Jordi Visser

- Created: `investing-macro/podcasts/jv-short-term-ai-fear-long-term-compute-scarcity-20260726.md` (Detailed summary of Jordi Visser on S&P earnings beats and 14.4% net margins, China's $9B state equity support, Jevons paradox in compute demand, Vera Rubin optical step-functions, and agentic AI memory)
- Created: `trading/interviews/20260726-jordi-visser-22v-research-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-27] ingest | What's Next For Markets — Software's AI Reckoning | Billy Fitzsimmons

- Created: `investing-fundamentals/podcasts/wnfm-softwares-ai-reckoning-20260726.md` (Detailed summary of Billy Fitzsimmons on enterprise software valuation compression, seat-based SaaS vs vibe coding disruption, hyperscaler CapEx wars, and OpenAI/Anthropic IPO catalysts)
- Created: `trading/interviews/20260726-billy-fitzsimmons-whats-next-for-markets-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-23] ingest | Market Newsletter Digest — July 23, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-23.md` (Detailed digest of macro and fundamental themes from July 23, 2026 newsletters, covering Brent crude re-breaching $100/bbl following Houthi attacks on Saudi tankers near Bab al-Mandeb; TSCS Research midstream primer on sticky risk premiums in war insurance, freight rates, and grade differentials; Alphabet's $205B FY2026 Capex guidance confirmation, -6.79% stock drop, and $94.1B SpaceX equity stake valuation disclosure; Swerve Insights' analysis of the $3.2T AI Capex gap requiring $701B annual OCF vs $577B current hyperscaler cash flow, and 89% compute vs 11% lab revenue split; Michael Burry's reference to the BIS report on AI circular vendor financing and long Tencent position at HK$448.60; Applied Intuition founders Qasar Younis and Peter Ludwig launching Dana agentic platform, predicting Physical AI will out-earn Digital AI in 25 years with 70% non-automotive revenue mix; 10-year Treasury yield hitting highest intraday level since Jan 2025; ECB holding rates at 2.25% with September hike risk; and Matt Levine's analysis on Anthropic's pre-IPO 10b5-1 stock plans adapting to non-financial model breakthrough MNPI)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-22] ingest | Market Newsletter Digest — July 22, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-22.md` (Detailed digest of macro and fundamental themes from July 22, 2026 newsletters, covering Alphabet's Q2 earnings ($119.8B rev, $24.8B GCP rev +82%), Q2 Capex surge to $44.9B, full-year Capex raised to $195B-$205B, first negative FCF quarter -$5.855B, and specialized third-party AI cloud partner reliance; SemiAnalysis report on Nvidia Kyber NVL144 12-month delay to 2028 vs Nvidia IR rebuttal; Mark Cuban's "Count the Humans" metric and VC bubble risk assessment; Robinhood Chain Arbitrum L2 traction ($200M ETH bridged, 130M transactions, 89% net fee margin); Tim Culpan's token economics framing of US-China AI competition; and Brent crude $93/bbl / WTI $88/bbl energy shock alongside Pentagon $87.6B war supplemental funding request)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-21] ingest | Market Newsletter Digest — July 21, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-21.md` (Detailed digest of macro and fundamental themes from July 21, 2026 newsletters, covering Gavin Baker and MBI Deep Dives' framework on open-weight models shifting value accrual downstream to compute/power/harnesses; Vercel CEO Guillermo Rauch's stealth cybersecurity evals for Kimi K3 and Sol; Convequity's rebalance into 800V DC power electronics via Enphase/SolarEdge paired allocation and Navitas GaN pure-play; rotation out of Lumentum into Tower Semiconductor for CPO hybrid bonding; Tae Kim's Google secular short thesis vs Rebound Capital's bull case; IBM's record -25% single-day crash on DRAM/HBM memory chipflation hardware delays; and Michael Howell's liquidity cycle rollover warning)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-20] ingest | Market Newsletter Digest — July 20, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-20.md` (Detailed digest of macro and fundamental themes from July 20, 2026 newsletters, covering Ben Thompson's analysis on AI inference COGS vs fixed R&D and unit cost of intelligence; Premier Xi Jinping's WAIC open-source AI geopolitical strategy; Moonshot AI's $30B+ Hong Kong IPO plans and DeepSeek's $51.82B valuation; IREN's $2.8B AI cloud contract expansion and ARR target upgrade to >$4.0B; TSMC Q2 record net margin (49.9%) and valuation disconnect; Brent crude breaking above $90/bbl on Strait of Hormuz VLCC zero-traffic choke; Philadelphia Semiconductor Index SOX entering a technical bear market down 20.2% from peak; and Bill Bonner's Dow/Gold ratio 13x framework)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 19, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-19.md` (Detailed digest of macro and fundamental themes from July 19, 2026 newsletters, covering Stripe and Advent's $53B+ buyout offer for PayPal; Moonshot AI's 2.8T Kimi K3 MoE release knocking Google Gemini out of top-3 and inferring SaaS-beating closed model API unit economics; NAND KV cache offloading; Jim Chanos's warning on hyperscaler ROIIC dropping to 10% and Micron failing the NVIDIA ceiling rule; Nebius's asset-light pivot and CoreWeave hedging; ASML and TSMC beat-and-raise guidance vs SOXX selloff; DTCC live tokenized stock trading launch for October 2026; Jenoptik AG's micro-optics explosion; ATI's SpaceX Starship superalloy chokepoint; Kalshi GPU compute forward curves; and US power grid deficit analysis)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 18, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-18.md` (Detailed digest of macro and fundamental themes from July 18, 2026 newsletters, covering the Moonshot Kimi K3 2.8T MoE launch; AI price wars undercutting frontier margins; extreme RPO concentration in hyperscaler backlogs; Jim Chanos's ROIC warnings and neocloud pivot to asset-light; Ray Dalio's 75% bubble gauge reading; Kevin Warsh's Congressional trilemma; Strait of Hormuz conflict and Brent crude rising above $85/bbl; TSMC's capex raise and pricing caution; SpaceX share slumps; and Netflix's Q2 earnings and multiple realignment)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 12, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-12.md` (Detailed digest of macro and fundamental themes from July 12, 2026 newsletters, covering the Yen carry recompression trade setup; equity repo market leverage stress and dealers charging +150bps over SOFR; Tom Lee's S&P 8,000 year-end target and H2 correction risk; combined free cash flow rollover of major tech hyperscalers; TSMC's grating coupler failures causing Nvidia to shift to Tower Semiconductor's silicon photonics NPO; local data center environmental backlash; China's MIIT banning Claude Code; SiliconFlow's token economics; SpaceX's exit liquidity lockup expiration; Jersey Mike's $12B franchise S1 model; and Fannie/Freddie housing capital reforms)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 11, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-11.md` (Detailed digest of macro and fundamental themes from July 11, 2026 newsletters, covering the BOJ's reserve losses and reverse carry trade dynamics on JGB 30-year 4% coupons; Kevin Warsh's hawkish Fed hold with dot plot suggesting 3.8% year-end rates; SK Hynix's $26.5B IPO Nasdaq debut; Oracle's S&P credit downgrade to one notch above junk on $42B cash burn and OpenAI reliance; Math & Markets' software-to-silicon margin transfer mechanism and favouring of ADBE/INTU over SNOW/DDOG/ZS; Meta's Muse Spark 1.1 model launch priced 4-8x cheaper than Anthropic; Sovereign AI push via Magna AI; California's upcoming 7.25%+ sales tax on SaaS; and the Strait of Hormuz crisis oil and rates dynamics)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 5, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-05.md` (Detailed digest of macro and fundamental themes from July 5, 2026 newsletters, covering TSCS Research's 1987 Gulf tanker-war parallel showing how crisis costs migrate into insurance/labor markets rather than the headline oil price; SpotGamma's options-flow confirmation of the semis-to-software rotation; Robinhood's decentralized-prime-broker ambitions behind its 7% Earn yield product; an institutional research roundup covering $8.6T of unicorns and 1999-level margin debt; James Lavish on Warsh's hawkish Sintra rhetoric masking a dovish inflation-measurement pivot; MacroVisor's half-time oil-oversupply call following the UAE's OPEC+ exit; Etched's and Beacon's founder profiles; and quick hits on liquidity-over-valuation and America's 250th as polycrisis)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 4, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-04.md` (Detailed digest of macro and fundamental themes from July 4, 2026 newsletters — a lighter, holiday-shortened day — covering the real-time semiconductor/memory sell-off triggered by Meta's compute-resale news alongside a soft June jobs report and Korea's third trading halt in three weeks; Nvidia's newly-named vendor-financing "backstop" program for neoclouds amid hyperscalers becoming chip competitors; a rigorous statistical rebuttal of the SMH/IGV correlation trade; Ironsides' H1 2026 macro recap and case for September/December rate cuts; a CDO-to-IPO structural parallel drawn from SpaceX's record $75B offering; a record week of European defense contract awards (Saab, BAE, KNDS's IPO postponement); and quick hits on small-cap positioning and tariff-vs-war market impact)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 3, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-03.md` (Detailed digest of macro and fundamental themes from July 3, 2026 newsletters, covering the bear/bull debate over Meta's compute-resale plan (George Noble vs. Clouded Judgement); Bonner Private Research's "AI Sovereignty" thesis built on Alex Karp's attack on subscription AI; the widening memory shortage (DRAM antitrust suits, the Apple-Micron public feud, Qualcomm's HBC workaround); Broadcom's custom AI accelerator deep dive (Google/Anthropic/OpenAI XPU deals); Doomberg on sanctions backfiring via Huawei's EUV-free chip roadmap; James Wang's data on America's 250th-anniversary business-formation boom; Michael Gayed's CLO ETF pick built for a higher-for-longer Fed; Shopee's multi-platform defense against TikTok Shop in Southeast Asia; and quick hits from TSOH and Torsten Slok on middle-market rate stress)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 2, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-02.md` (Detailed digest of macro and fundamental themes from July 2, 2026 newsletters, covering Sintra's coordinated retirement of Fed forward guidance ahead of June payrolls; Michael Gayed's Q3-open recap of gold's worst quarter since 2013 against the SOX's best quarter ever and a 40-year yen low; Charlie Bilello's consumer-facing "hundred-year flood" memory chipflation data; SemiAnalysis and Big Technology dissecting Meta's neocloud compute-resale pivot alongside Karp's frontier-lab attack; Arm CEO Rene Haas on agentic AI's CPU core-count economics; Matt Levine on Unicode homoglyph stock manipulation and universal basic AI; the OpenAI advertising "Devil's Triangle" of contradictory monetization pressures; Nicolas Colin's local-model thesis on the coming Big AI unwind; and Jimmy's Journal on Amazon's logistics moat as an agentic-commerce moat)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 1, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-01.md` (Detailed digest of macro and fundamental themes from July 1, 2026 newsletters, covering Fed Chair Warsh's Sintra debut amid a split desk read on Iran-Doha talks; Matt Levine's "Egg Libor" benchmark-manipulation piece; Michael Gayed's 50-year survey showing every equity crisis was a currency crisis first; the AI chipflation story confirmed by Apple's DRAM-driven price hikes and Korea's $576B chip investment; Meta's compute release-valve monetization strategy; Rebound Capital's Amazon robotics/advertising deep dive; Chris Dover on OpenAI's private-market strategy versus SpaceX's IPO, the YC token investment, and the Jalapeño chip; Adam Tooze on China's capital-controlled wealth disconnect from the AI boom; EPB Research on the structural decline in American housing investment; and a speculative Greenspan/AI-monetary-policy piece)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — June 30, 2026

- Created: `investing-macro/market-newsletter-digest-2026-06-30.md` (Detailed digest of macro and fundamental themes from June 30, 2026 newsletters, covering the Q2 quarter-end close with historic single-stock dispersion, yen at 1986 lows, and the Supreme Court's Fed-independence ruling on Governor Cook; Matt Levine on Susquehanna's insider-trading suit; the AI ROI runway debate between Torsten Slok's margin warning and SemiAnalysis's token-budgeting field data; Part II of the memory supercycle covering failed US export controls and Korea's $880B-$3.1T AI investment plan; Netflix's re-rating thesis alongside Comcast's NBCUniversal spinoff; the Q2 crypto wrap and Bitcoin-bailout speculation around Strategy's capital framework; Ed Zitron and the BIS on AI systemic financial risk; Michael Gayed's extreme healthcare-vs-tech defensive rotation signal; Stripe Sessions' agentic commerce demos and cloud-agent adoption at OpenAI/Anthropic/Cursor; and Danielle DiMartino Booth on the K-shaped economy cracking)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — June 29, 2026

- Created: `investing-macro/market-newsletter-digest-2026-06-29.md` (Detailed digest of macro and fundamental themes from June 29, 2026 newsletters, covering the Iran ceasefire's fragile weekend collapse-and-reversal ahead of Fed Chair Warsh's Sintra debut and June NFP, Matt Levine on record stock market leverage, SpearPoint's K-shaped mid-year AI-capex read, the memory/HBM supercycle and DDR price spikes, the hyperscaler "tollbooth" token-optimization thesis and The Diff's agent-minute measurement problem, BTC ETF's 7th straight outflow week and Strategy's mNAV compression, Axon Enterprise and Cloudflare's agentic-internet thesis, the private equity consensus-trade unwind, China-EU relations and China's hydropower/chip dominance, Topdown Charts' bullish ex-US/small-cap positioning, and email security's shift to an identity-graph architecture)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 17, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-17.md` (Detailed digest of macro and fundamental themes from July 17, 2026 newsletters, covering Moonshot's Kimi K3 2.8T parameters release, the AI model price crash, OpenAI compute chief tenancy model, data center GW boom and PJM 6.5GW power deficit, the circular RPO backlog loop, Kospi 25% correction, the SOX entering a bear market, Netflix Q2 earnings drop, and Kevin Warsh's testimony vs the Strait of Hormuz oil shock)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 16, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-16.md` (Detailed digest of macro and fundamental themes from July 16, 2026 newsletters, covering TSMC's Q2 earnings and $100B Arizona expansion, ASML's Q2 gross margin beat and High-NA 18A qualification, the $638B AI capex debt supercycle, GPU-to-power bottleneck shift, Menlo Ventures' Anthropic SPV, SpaceX IPO short selling dynamics, the SOX breaking $12,000, Howard Marks on AI autonomy and the 2008 meltdown playbook, June PPI, and Bank of Japan's reverse carry trade lessons)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 15, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-15.md` (Detailed digest of macro and fundamental themes from July 15, 2026 newsletters, covering Stripe and PE Advent's $53.4B buyout offer for PayPal, IBM's historic 26% single-day crash and budget pivots to hardware, Bill Ackman's PSUS discount and HHH insurance float plays, U.S.-Iran naval blockade and Strait of Hormuz transit drop, June CPI disinflation vs core PPI, Eli Lilly's talks to acquire AtaiBeckley in a psychedelic arms race, and Aswath Damodaran's Aa1 mature mature market ERP framework)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-19] ingest | Market Newsletter Digest — July 14, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-14.md` (Detailed digest of macro and fundamental themes from July 14, 2026 newsletters, covering Strait of Hormuz tolling proposals and crude price targets, Russian refinery throughput collapse and low-sulfur diesel shortages, Apple's IP theft lawsuit against OpenAI, Meta capex increases vs Fred Hickey bubble warning, SK Hynix Nasdaq listing and GraniteShares leveraged ETFs, Kevin Warsh's hawkish Fed testimony, and ATI as a space-era specialty superalloy chokepoint)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | Market Newsletter Digest — July 13, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-13.md` (Detailed digest of macro and fundamental themes from July 13, 2026 newsletters, covering the Maradona Theory of Interest Rates, AI Tokens per Watt optimization, Upstream/Downstream supply chain divergence, and Texas Stock Exchange)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Compound and Friends #251 — You're About to See the Real AI Winners Stand Up | Jonathan Thomas

- Created: `investing-macro/podcasts/tcaf-real-ai-winners-stand-up-20260717.md` (Detailed summary of TCAF episode 251 with Jonathan Thomas on the active ETF structural tailwind, the shift from AI creators to adopters, capex bubble lessons, and American Century's philanthropic model)
- Created: `trading/interviews/20260717-jonathan-thomas-tcaf-transcript.md` (Raw transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Compound and Friends #250 — The Real Ticking Time Bomb | Michael Cembalest

- Created: `investing-macro/podcasts/tcaf-the-real-ticking-time-bomb-20260710.md` (Detailed summary of TCAF episode 250 with Michael Cembalest on the 2031-2032 crossover point, capex margins, custom ASICs TCO improvements, and cybersecurity vulnerabilities)
- Created: `trading/interviews/20260710-michael-cembalest-tcaf-transcript.md` (Raw transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Compound and Friends #249 — Brian Belski Returns! | Brian Belski

- Created: `investing-macro/podcasts/tcaf-brian-belski-returns-20260703.md` (Detailed summary of TCAF episode 249 with Brian Belski on the S&P 7,000 target, secular bull market parameters, small-cap earnings acceleration, and regional bank M&A)
- Created: `trading/interviews/20260703-brian-belski-tcaf-transcript.md` (Raw transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Julia La Roche Show #391 — The Wrap: Bank Earnings and Oil Prices Soar | Chris Whalen

- Created: `investing-macro/podcasts/jlr-wrap-bank-earnings-and-oil-prices-soar-20260718.md` (Detailed summary of Chris Whalen's wrap on bank earnings disconnect, private credit systemic risks, and diesel shortages)
- Created: `trading/interviews/20260718-chris-whalen-la-roche-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Julia La Roche Show — Not A Normal Market | Ted Oakley

- Created: `investing-macro/podcasts/jlr-not-a-normal-market-20260716.md` (Detailed summary of Ted Oakley's macro perspectives on standard deviation equity metrics, capital preservation, and energy/gold miners)
- Created: `trading/interviews/20260716-ted-oakley-la-roche-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Julia La Roche Show — Market Rotten to the Core | Larry McDonald

- Created: `investing-macro/podcasts/jlr-market-rotten-to-the-core-20260714.md` (Detailed summary of Larry McDonald's interview on AI/data center capex rotations, commercial real estate credit risks, stablecoin policies, and the $6,500 gold target)
- Created: `trading/interviews/20260714-larry-mcdonald-la-roche-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Julia La Roche Show — No Rate Hike Coming | Danielle DiMartino Booth

- Created: `investing-macro/podcasts/jlr-no-rate-hike-coming-20260709.md` (Detailed summary of Danielle DiMartino Booth's interview on labor market participation declines, consumer credit contraction, and Federal Reserve leadership transition)
- Created: `trading/interviews/20260709-danielle-dimartino-booth-la-roche-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Julia La Roche Show — Economic Statecraft Changed Everything | Michael Every

- Created: `investing-macro/podcasts/jlr-economic-statecraft-changed-everything-20260707.md` (Detailed summary of Michael Every's interview on the global shift toward economic statecraft, central bank models breakdown, and reshoring interest rate pressures)
- Created: `trading/interviews/20260707-michael-every-la-roche-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Julia La Roche Show — A Recession Signal Just Triggered | Henrik Zeberg

- Created: `investing-macro/podcasts/jlr-a-recession-signal-just-triggered-20260702.md` (Detailed summary of Henrik Zeberg's interview on labor market indicators, swissblock recession frameworks, and the final equity melt-up to blow-off top)
- Created: `trading/interviews/20260702-henrik-zeberg-la-roche-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | The Julia La Roche Show #383 — Andrew Pancholi: Smart Money Is Quietly Exiting Stocks | Andrew Pancholi

- Created: `investing-macro/podcasts/jlr-smart-money-exiting-stocks-20260630.md` (Detailed summary of The Julia La Roche Show interview with Andrew Pancholi on mathematical macro cycles, smart money outflows in Dow futures, $183 oil targets, and $6,900 gold by March 2027)
- Created: `trading/interviews/20260630-andrew-pancholi-la-roche-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | MacroVoices #541 — Dr. Anas Alhajji: Bab el-Mandeb: The Next Oil Chokepoint Nobody's Watching | Dr. Anas Alhajji

- Created: `investing-macro/podcasts/mv-bab-el-mandeb-the-next-oil-chokepoint-20260716.md` (Detailed summary of MacroVoices interview with Dr. Anas Alhajji on Bab el-Mandeb chokepoints, the U.S.-Iran MOU collapse, Qatari helium semiconductor bottlenecks, and the fallacy of the SPR refill case)
- Created: `trading/interviews/20260716-anas-alhajji-macrovoices-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | MacroVoices #540 — Adam Parker: Beyond the AI Bubble | Adam Parker

- Created: `investing-macro/podcasts/mv-beyond-the-ai-bubble-20260709.md` (Detailed summary of MacroVoices interview with Adam Parker on equity earnings durability, energy tech-diversification, six AI revenue buckets, and quantitative pod microstructure)
- Created: `trading/interviews/20260709-adam-parker-macrovoices-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | MacroVoices #539 — Rory Johnston: Hormuz Crisis, is it Really Over? | Rory Johnston

- Created: `investing-macro/podcasts/mv-hormuz-crisis-is-it-really-over-20260702.md` (Detailed summary of MacroVoices interview with Rory Johnston on Middle East oil jailbreaks, China's 5M b/d import cut, refining bottlenecks, and WTI spec short positioning)
- Created: `trading/interviews/20260702-rory-johnson-macrovoices-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | MacroVoices #538 — Lyn Alden: Is The War Really Over and What's Next For Markets? | Lyn Alden

- Created: `investing-macro/podcasts/mv-is-the-war-really-over-20260625.md` (Detailed summary of MacroVoices interview with Lyn Alden on persistent deficits, stablecoin networks, AI energy bottlenecks, and the hawkish transition of the Fed under Kevin Warsh)
- Created: `trading/interviews/20260625-lyn-alden-macrovoices-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | MacroVoices #537 — Brent Johnson: There's No Turning Back | Brent Johnson

- Created: `investing-macro/podcasts/mv-theres-no-turning-back-20260618.md` (Detailed summary of MacroVoices interview with Brent Johnson on stablecoin hegemony, the imperial transition of the U.S., DXY milkshake dynamics, and agricultural fertilizer yield shocks)
- Created: `trading/interviews/20260618-brent-johnson-macrovoices-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | MacroVoices #536 — Larry McDonald: The Migration is Upon us | Larry McDonald

- Created: `investing-macro/podcasts/mv-the-migration-is-upon-us-20260611.md` (Detailed summary of MacroVoices interview with Larry McDonald on super core CPI inflation, the $3T tech lockup overhang, and rotations into value, healthcare, and energy)
- Created: `trading/interviews/20260611-larry-mcdonald-macrovoices-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | Excess Returns — Jack Schwager on Timeless Lessons from the New Wave of Elite Traders | Jack Schwager

- Created: `investing-macro/podcasts/er-lessons-from-new-wave-of-elite-traders-20260716.md` (Detailed summary of Excess Returns interview with Jack Schwager on video game reflexes, Sharpe critiques, and risk rules of modern Market Wizards)
- Created: `trading/interviews/20260716-jack-schwager-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | Excess Returns — He Found 2.5 Million Missing Workers | Eric Pachman

- Created: `investing-macro/podcasts/er-he-found-2-5-million-missing-workers-20260714.md` (Detailed summary of Excess Returns interview with Eric Pachman on survey response failures, Medicaid Care Economy tail risks, OER/Core CPI structural issues, and refining crack spreads)
- Created: `trading/interviews/20260714-eric-pachman-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | Excess Returns — 33 Charts that Show Why a Market Correction May Be Coming | Jim Paulsen

- Created: `investing-macro/podcasts/er-33-charts-market-correction-coming-20260710.md` (Detailed summary of Excess Returns interview with Jim Paulsen on stagnation in job growth indicators, Quasi Policy Index contraction, and rotation into Old Era equities)
- Created: `trading/interviews/20260710-jim-paulsen-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | Excess Returns — Big Uptrend. Tech Momentum Cracking | Katie Stockton

- Created: `investing-macro/podcasts/er-big-uptrend-tech-momentum-cracking-20260708.md` (Detailed summary of Excess Returns interview with Katie Stockton on short-term momentum consolidations, overbought stochastic sell signals, NYSE breadth, and the TAC ETF)
- Created: `trading/interviews/20260708-katie-stockton-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-18] ingest | Excess Returns — We Asked a $1 Billion Quant Manager Why Concentration Isn't a Warning | Matt Zenz

- Created: `investing-macro/podcasts/er-we-asked-a-1-billion-quant-manager-20260707.md` (Detailed summary of Excess Returns interview with Matt Zenz on market concentration, filtering small cap junk, the AI capex factor impact, and fixed income tax drag)
- Created: `trading/interviews/20260707-matt-zenz-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-17] ingest | Excess Returns — We Asked a 20-Year Bond Manager Why AI CapEx Is a Fragile Loop | Jeff Klingelhofer

- Created: `investing-macro/podcasts/er-we-asked-a-20-year-bond-manager-20260706.md` (Detailed summary of Excess Returns interview with Jeff Klingelhofer on the AI capex wealth effect loop, the Fed's three mandates, and public vs. private credit quality)
- Created: `trading/interviews/20260706-jeff-klingelhofer-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-17] ingest | Excess Returns — The $400 Billion Gap | Warren Pies

- Created: `investing-macro/podcasts/er-the-400-billion-gap-20260702.md` (Detailed summary of Excess Returns interview with Warren Pies on the $400B gap (tech capex vs. housing), OpenRouter token demand, GPU availability, and semiconductor blow-off screens)
- Created: `trading/interviews/20260702-warren-pies-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-16] ingest | Excess Returns — He Wrote the Book on Why Moats Fail | Ritavan

- Created: `investing-macro/podcasts/er-he-wrote-the-book-on-why-moats-fail-20260701.md` (Detailed summary of Excess Returns interview with Ritavan on the System Gambit framework, self-improving loops, path dependence, and why checklists fail when causal models change)
- Created: `trading/interviews/20260701-ritavan-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-16] ingest | Excess Returns — He Wrote the Book on 100-Baggers | Chris Mayer

- Created: `investing-macro/podcasts/er-he-wrote-the-book-on-100-baggers-20260626.md` (Detailed summary of Excess Returns interview with Chris Mayer on SpaceX's $2.6T valuation, S1 governance, the "early is overrated" fallacy, and the statistical reality of 100x outcomes)
- Created: `trading/interviews/20260626-chris-mayer-excess-returns-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-16] ingest | Thoughtful Money — Sky-High Earnings Expectations Courting Disaster?

- Created: `investing-macro/podcasts/tm-sky-high-earnings-expectations-20260703.md` (Detailed summary of Thoughtful Money Weekly Market Recap with Lance Roberts on sky-high forward earnings expectations, the "sandwich generation" planning crisis, factor rotation model rebalancing, and Blackstone's Virginia zoning failure)
- Created: `trading/interviews/20260703-lance-roberts-thoughtful-money-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-16] ingest | Thoughtful Money — Growing Risk Of Semiconductors Rolling Over & Dragging The Market Down With Them

- Created: `investing-macro/podcasts/tm-growing-risk-of-semiconductors-rolling-over-20260710.md` (Detailed summary of Thoughtful Money Weekly Market Recap with Lance Roberts on technical head-and-shoulders in semiconductors, real-time margin changes, AI capex GDP multipliers, and public-private utility partnerships)
- Created: `trading/interviews/20260710-lance-roberts-thoughtful-money-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-16] ingest | Thoughtful Money — There's Going To Be One Hell Of A Hangover When The Market Party Ends

- Created: `investing-macro/podcasts/tm-theres-going-to-be-one-hell-of-a-hangover-20260628.md` (Detailed summary of Thoughtful Money interview with Louis Gave on the 4-quadrant macro framework, bank relative strength, JPY repatriation risks, and the 60/20/20 portfolio)
- Created: `trading/interviews/20260628-louis-gav-thoughtful-money-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-16] ingest | Thoughtful Money — Longtime Bull Warns 'High' Risk Of Market Correction Soon

- Created: `investing-macro/podcasts/tm-longtime-bull-warns-high-risk-of-market-correction-soon-20260702.md` (Detailed summary of Thoughtful Money interview with Darius Dale on 1998-style correction risks, Kevin Warsh's 5 task forces, bank financial repression, and the E-shaped economy)
- Created: `trading/interviews/20260702-darius-dale-thoughtful-money-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-16] ingest | Thoughtful Money — Fourth Turning To Turn The Dollar Into A Wrecking Ball?

- Created: `investing-macro/podcasts/tm-fourth-turning-to-turn-the-dollar-into-a-wrecking-ball-20260702.md` (Detailed summary of Thoughtful Money interview with George Gammon on the Eurodollar liability system, currency cross-rate depreciation, private credit redemption halts, and pairs trading)
- Created: `trading/interviews/20260702-george-gammon-thoughtful-money-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-16] ingest | Thoughtful Money — The Equity Markets Are Insane Right Now

- Created: `investing-macro/podcasts/tm-the-equity-markets-are-insane-right-now-20260706.md` (Detailed summary of Thoughtful Money interview with Jan Van Eck on tech profit growth, BDC private credit opportunities, single-LLM headwinds, and long-term asset positioning)
- Created: `trading/interviews/20260706-jan-van-eck-thoughtful-money-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-16] ingest | Thoughtful Money — We're In The Greatest Stock & Earnings Bubble In US History

- Created: `investing-macro/podcasts/tm-greatest-stock-and-earnings-bubble-in-us-history-20260712.md` (Detailed summary of Thoughtful Money interview with Fred Hickey on AI overcapacity, hyperscaler accounting mismatch, and capital preservation in gold and short-term cash)
- Created: `trading/interviews/20260716-fred-hickey-thoughtful-money-transcript.md` (Raw interview transcript with timestamps)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-15] create | portfolio-secured-puts-interview-20260715-notes page

- Created: `investing-options/income/portfolio-secured-puts-interview-20260715-notes.md` (Accompanying strategy guide for Portfolio-Secured Puts, detailing duration parameters, SPAV ratios, reinvestment, and valuation guidelines)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-15] ingest | YouTube Interview Transcript - Portfolio Secured Puts with Brandon (2026-07-15)

- Created: `investing-options/income/portfolio-secured-puts-interview-20260715-transcript.md` (Cleaned and formatted complete transcript of the YouTube interview with Brandon Arnett on portfolio-secured puts, margin mechanics, covered calls, and valuation investing)
- Updated: `log.md`

## [2026-07-15] create | cpo-and-npo-optics theme page

- Created: `investing-fundamentals/company-analyses/themes/cpo-and-npo-optics.md` (Synthesizes CPO/NPO differences, Nvidia's shift from TSMC to Tower, UHP laser landscape Lumentum vs Coherent, and VCSEL CPO packaging; moved from concepts to themes)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-14] ingest | Market and Investment Newsletter Digest - July 10, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-10.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-11] create | ai-inference-costs-accounting concept page

- Created: `investing-fundamentals/concepts/ai-inference-costs-accounting.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-10] create | semianalysis-research-2026-06 concept page

- Created: `investing-macro/semianalysis-research-2026-06.md` (Synthesis of SemiAnalysis June 2026 research: US datacenter delays, hardware-software co-design, and Nvidia multipolar strategy)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-10] update | rename semianalysis-research-july-2026 to semianalysis-research-2026-07

- Renamed: `investing-macro/semianalysis-research-july-2026.md` to `investing-macro/semianalysis-research-2026-07.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-10] create | semianalysis-research-july-2026 concept page

- Created: `investing-macro/semianalysis-research-july-2026.md` (Synthesis of SemiAnalysis July 2026 research: Nvidia debt backstop, Anthropic Q3 profitability and IPO, Claude Code SaaS threat)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-10] ingest | Market and Investment Newsletter Digest - July 9, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-09.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-10] ingest | Market and Investment Newsletter Digest - July 8, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-08.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-10] ingest | Market and Investment Newsletter Digest - July 7, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-07.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-08] ingest | Market and Investment Newsletter Digest - July 6, 2026

- Created: `investing-macro/market-newsletter-digest-2026-07-06.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-07] create | bayes-and-base-rates concept page

- Created: `investing-fundamentals/concepts/bayes-and-base-rates.md` (Summarizes the Bayesian updating framework, reference-class forecasting, case studies of AI Capex/RPOs, and project success rates for datacenter buildouts)
- Updated: `index.md`
- Updated: `log.md`

## [2026-07-07] ingest | TCI Conference: $MSFT and $SPGI Investment Theses

- Updated: `investing-macro/market-newsletter-digest-2026-06-18.md` (Updated Section 6 to document arguments for/against $MSFT and $SPGI based on Moats & Multiples Substack)
- Updated: `investing-fundamentals/company-analyses/README.md` (Added $MSFT and $SPGI sections summarizing TCI's theses and counterarguments)
- Updated: `log.md`

## [2026-07-03] create | funding-short-squeeze concept page

- Created: `investing-fundamentals/concepts/funding-short-squeeze.md`
- Covers: funding short definition, pairs trade mechanics, squeeze unwind cascade, and
  a data-driven assessment methodology (correlation structure, short interest, borrow rates,
  options flow, intraday microstructure, 13F positioning, GS Most Short basket)
- Includes the June 2026 SaaS vs. semis anti-correlation observation as a concrete case study
- Added `positioning` tag to SCHEMA.md tag taxonomy
- Updated: `index.md` (total pages: 130)
> Rotate when this file exceeds 500 entries: rename to `log-YYYY.md`, start fresh.

---

## [2026-06-27] ingest | TCAF 248 — Too Early to Get Off the Wave

- Created: `investing-macro/podcasts/tcaf-too-early-to-get-off-the-wave-20260626.md`
- Source: The Compound and Friends, Episode 248 (June 26, 2026) featuring Ryan Detrick and Sonu Varghese
- Cross-links: [[yen-carry-trade-unwinding-2025]], [[valuations]], [[bond-supply-tsunami-2026]], [[market-newsletter-digest-2026-06-24]]
- Updated: `index.md` (total pages: 129)
- Updated: `log.md`

## [2026-06-26] ingest | Mauboussin & Callahan — Opportunities and Expectations (PVGO)

- Created: `investing-fundamentals/concepts/pvgo.md`
- Source: Counterpoint Global Insights, Morgan Stanley Investment Management, June 18, 2026
- Includes full text of 7 Readwise notebook highlights as illustrative quotes
- Cross-links: [[valuations]], [[equity-risk-premium]], [[equity-return-components]], [[factor-strategies]]
- Updated: `index.md` (total pages: 128)
- Updated: `log.md`

## [2026-06-25] ingest | Market and Investment Newsletter Digest - June 24, 2026

- Created: `investing-macro/market-newsletter-digest-2026-06-24.md`
- Updated: `investing-macro/hormuz-closure-scenarios-2026.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-06-18] ingest | Market and Investment Newsletter Digest - June 18, 2026

- Created: `investing-macro/market-newsletter-digest-2026-06-18.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-06-19] ingest | Market and Investment Newsletter Digest - June 19, 2026

- Created: `investing-macro/market-newsletter-digest-2026-06-19.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-06-21] ingest | Market and Investment Newsletter Digest - June 21, 2026

- Created: `investing-macro/market-newsletter-digest-2026-06-21.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-06-20] ingest | Market and Investment Newsletter Digest - June 20, 2026

- Created: `investing-macro/market-newsletter-digest-2026-06-20.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-06-02] ingest | Market and Investment Newsletter Digest - June 2, 2026

- Created: `investing-macro/market-newsletter-digest-2026-06-02.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-06-03] ingest | Market and Investment Newsletter Digest - June 3, 2026

- Created: `investing-macro/market-newsletter-digest-2026-06-03.md`
- Updated: `index.md`
- Updated: `log.md`

## [2026-05-25] lint | 4 issue categories found, index rebuilt

- Ran 12-point lint on 126 wiki-layer pages
- **FIXED:** Index rebuilt — was missing 115/126 pages; two entire sections absent (investing-quant, personal-finance)
- **CRITICAL:** Zero [[wikilinks]] exist anywhere — wiki is a flat collection, not a network; cross-linking is the main ongoing improvement opportunity
- **HIGH:** 52 pages exceed 200-line threshold; worst offenders: yen-carry-trade-unwinding-2025.md (1,189 lines), 2026-plan-comparisons-claude.md (1,170), stock-valuation-tool-plan.md (1,102), credit-spread-notes (1,046)
- **MEDIUM:** Two options transcript files reclassified as raw in index (put-options-selling-guide, credit-spread-transcript)
- No broken wikilinks (none exist yet), no contested pages, no sha256 drift, log rotation not needed

## [2026-05-24] init | Wiki bootstrapped

- Initialized hermes llm-wiki structure on existing investment-research-notes directory
- Created: SCHEMA.md, index.md, log.md
- Catalogued 17 company analyses, 3 financial concepts, 2 macro theses, 2 frameworks,
  1 crypto analysis, 2 real estate pages, 2 book notes
- Existing files predate this schema and do not have YAML frontmatter; new pages should use it
- Wiki path: /Users/howardwu/dev/investment-research-notes

## [2026-07-27] create | Individual Bonds vs. Bond Funds — Mark-to-Market, Real Returns, and the Annuity Math

- Created: `investing-quant/concepts/individual-bonds-vs-bond-funds.md`
- Filed from a conversation evaluating a financial-planning blog claim about TLT/IEF
  mark-to-market losses vs. individual Treasuries held to maturity; covers real vs.
  nominal YTM, the present-value annuity factor derivation, and a worked real-loss
  example ($100k, 1.9% coupon, 30yr, 3% inflation).
- Updated: `investing-macro/bond-supply-tsunami-2026.md` (added cross-link in section 4, individual long-bond holders)
- Updated: `index.md` (new page listed under Quant > Concepts; page count 178 → 179)
- Updated: `log.md`

## [2026-08-18] create | Global Liquidity Framework — The Asynchronous Business Cycle and Asset Allocation

- Created: `investing-macro/macro-frameworks/global-liquidity-framework.md`
- Synthesized Michael Howell's Global Liquidity Framework: the two circulations of money (financial vs. real economy), the 15–18 month asynchronous business cycle lag, momentum vs. level dynamics, and late-cycle asset allocation (commodities and defensives vs. high-multiple tech and long bonds).
- Included rigorous empirical assessment for institutional investors (Marshallian $k$, $300T+ debt refinancing mechanics, BIS research, monetary transmission lags, historical late-cycle precedents from 2000 and 2007–2008, plus structural limitations: fiscal dominance, measurement ambiguity, and non-linear crash risk).
- Updated: `investing-macro/macro-frameworks/README.md` (added cross-link under Michael Howell section)
- Updated: `index.md` (indexed under Macro section)
- Updated: `log.md`

## [2026-08-19] ingest | Market and Investment Newsletter Digest — August 19, 2026

- Created / Updated: `investing-macro/market-newsletter-digest-2026-08-19.md`
- Synthesized Michael Parekh's *AI: Reset to Zero #138* ("‘Gaming the System’ for AI: Nvidia, OpenAI & Anthropic"): Nvidia's $500B Wall Street financing consortium (Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, KKR), OpenAI's $7B self-funded pre-IPO tender offer ($852B valuation), Anthropic's $9.1B–$16.1B compute agreement with Riot Platforms, and historical parallels to the 1870s transcontinental railroad capital buildout.
- Added analysis of the August 19 crypto market surge (BTC >$68k, ETH, SOL, crypto equities): U.S. Treasury's announcement doubling long-end debt buybacks ($2B to $4B+ per operation), the SEC's proposed "Regulation Crypto Assets" safe harbor rules, and the cascading $1.44B short squeeze.
- Updated: `index.md` (indexed under Macro section)
- Updated: `log.md`

## [2026-08-19] update | CRCL company analysis pipeline (CLARITY Act Senate vote, Arc L1 revenue models, SEC safe harbor)

- Updated: `investing-fundamentals/company-analyses/crcl-2-equity-report.md` (incorporated the September 15 Senate CLARITY Act cloture vote, SEC Regulation Crypto Assets safe harbor rules, U.S. Treasury long-end buyback doubling, and multi-year Arc L1 platform revenue modeling: $310M–$330M FY26, $550M–$700M FY27, $800M–$1.0B+ FY28 with 80%+ contribution margin).
- Updated: `investing-fundamentals/company-analyses/crcl-3-investment-memo.md` (highlighted the mid-September dual catalyst window—Sept 15 CLARITY Act vote and Sept 16 Arc mainnet launch; updated scenario matrix, KPI watch list, and bank deposit-flight yield restriction risks).
- Updated: `investing-fundamentals/company-analyses/CRCL.md` (refreshed overview and fundamental analysis with latest Arc and legislative developments).
- Updated: `log.md`

## [2026-08-19] create | Custom AI Silicon & Optical Networking: Google-Marvell $120B Deal, Broadcom Impact, and Optical Supply Chain Matrix

- Created: `investing-fundamentals/company-analyses/comparisons/google-marvell-broadcom-optical-20260819.md`
- Synthesized the Google–Marvell ($MRVL) $120B lifetime custom AI silicon agreement (custom inference accelerators, custom TPU NICs, storage/memory controllers, and the 59M share / $12.2B performance equity warrant structure).
- Documented supply chain disruption across Broadcom ($AVGO) (breaking the sole-source TPU monopoly, margin compression, AMD TPU v10 co-design leaks, VMware CVE-2026-59310 zero-day, and XPV financing credit risks), Astera Labs ($ALAB) (custom controller IC substitution), and Nvidia ($NVDA) (internal inference workload displacement).
- Analyzed the optical networking selloff following Fabrinet's ($FN) Q1 FY27 guidance deceleration (-20% drop), mapping direct vs. indirect exposure across pluggable module assemblers ($AAOI — high risk) vs. upstream laser and physical materials leaders ($LITE, $COHR — indispensable InP/EML/CW laser moats).
- Updated: `investing-macro/market-newsletter-digest-2026-08-19.md` (added Section 3 covering custom AI silicon and optical transceiver selloff)
- Updated: `index.md` (indexed comparison document and updated August 19 digest description)
- Updated: `log.md`

## [2026-08-21] create | Treasury Financial Repression: SLR Bank Deregulation, Stablecoins as T-Bill Sinks, and Shadow Yield Curve Control

- Created: `investing-macro/macro-frameworks/treasury-financial-repression-slr-stablecoins.md`
- Synthesized the Treasury's market-based financial repression framework: using bank deregulation (SLR/eSLR exemptions, Basel III capital relief) to expand primary dealer warehousing capacity and eliminate the 5–25 bps illiquidity penalty across the 95% of the Treasury curve that is off-the-run.
- Detailed the regulatory rulemaking roadmap (Q4 2026 Fed/FDIC/OCC final joint rule vote, SEC FICC mandatory clearing harmonization, and 2027 implementation).
- Documented stablecoins as a captive $500B–$1T+ T-bill sink (GENIUS/CLARITY Acts), enabling the Treasury to twist issuance to the front end, reduce 10Y/30Y coupon auction sizes, run debt buybacks, and suppress the long-term term premium.
- Analyzed systemic downsides and risks: G-SIB duration/solvency traps, 50x hedge fund cash-futures basis trade fragility, credit crowding-out of the real economy, de-peg fire sales, and unchecked fiscal profligacy.
- Mapped the asymmetric banking impact and lobbying dynamics: existential deposit flight / NIM collapse for Regional Banks vs. fee/deposit-monopoly defense by TBTF Mega-Banks (BPI/ABA lobbying for anti-yield rules and proprietary deposit tokens).
- Updated: `investing-macro/macro-frameworks/README.md` (cross-link added)
- Updated: `investing-macro/bond-supply-tsunami-2026.md` (cross-link and policy response note added)
- Updated: `index.md` (indexed under Macro frameworks)
- Updated: `log.md`

## [2026-08-21] update | AppLovin (APP) company analysis pipeline (Wall Street consensus shift, Piper Sandler PT cut, AXON compute cost dynamics)

- Updated: `investing-fundamentals/company-analyses/app-1-document-sources.md` (completed Section E equity research coverage table incorporating Piper Sandler's August 21 PT cut from $385 to $325, JPMorgan's Neutral $350–$400 target, Bank of America's downgrade to $400, Morgan Stanley's $650 Overweight target, and BTIG's $410 Buy rating).
- Updated: `investing-fundamentals/company-analyses/app-2-equity-report.md` (expanded Moat Vulnerabilities to detail AXON algorithmic yield deceleration, diminishing returns in mobile gaming optimization, and rising AI compute/GPU infrastructure outlays dragging EBITDA margins).
- Updated: `investing-fundamentals/company-analyses/app-3-investment-memo.md` (updated valuation asymmetry box with Street consensus target range of $325–$650; incorporated compute cost inflation and model maturation into Risk #4).
- Updated: `log.md`

## [2026-09-01] create | AI Compute Commencement Wall, Take-or-Pay Liabilities, and the 2027–2028 Payment Shock

- Created: `investing-macro/macro-frameworks/ai-compute-commencement-wall-and-refinancing-trap.md`
- Synthesized structural financial assessment evaluating claims on OpenAI's $1.2T compute origination spree, the $636B supplier market cap multiplier, 200% revenue coverage deficit models, and hyperscaler ROIC inversion / refinancing traps.
- Documented the 24–36 month construction "teaser lag" vs. binding commencement date obligations, take-or-pay contractual structures, and circular vendor equity dynamics.
- Detailed the 4 transmission channels: GPU collateral/private ABS debt impairment, hyperscaler server D&A useful life revisions, semiconductor order cancellation bullwhip, and utility/nuclear PPA stranding.
- Mapped 3 equity market paths: (1) "Telecom 2000" Capital Overhang & Downside Unwind (30% probability), (2) Managed Restructuring / "Cloud Ingestion & Sovereign Bailout" (50% probability), and (3) Autonomous Productivity Monetization Surge (20% probability), alongside leading monitoring indicators (spot GPU rental rates, private secondary discounts, depreciation revisions).
- Updated: `investing-macro/macro-frameworks/README.md` (cross-linked under AI Infrastructure & Capital Cycles section)
- Updated: `investing-macro/market-newsletter-digest-2026-08-20.md` (cross-linked to framework)
- Updated: `index.md` (indexed under Macro frameworks; total pages bumped to 211)
- Updated: `log.md`

## [2026-09-01] update | AI Compute Commencement Wall — critical re-assessment, verdict re-grading, and gray-area flagging

- Updated: `investing-macro/macro-frameworks/ai-compute-commencement-wall-and-refinancing-trap.md`
- **Frontmatter corrected:** `confidence: high → medium`, `contested: false → true`, added `contradictions: [market-newsletter-digest-2026-08-20]` (source digest cites >$2.3T across all labs vs. this page's ~$1.2T single-lab figure). Added digest 2026-08-19 to `sources`.
- **Added prominent "Bottom Line — Conclusions as of 2026-09-01"** block at page top: 7 numbered conclusions surfacing what the statement-by-statement structure had buried.
- **Verdicts re-graded** against the evidence the page itself supplies, with a stated verdict scale:
  - Statement 2 ($636B market cap multiplier): `HIGHLY ACCURATE` → `MECHANISM ACCURATE / FIGURE UNVERIFIED`. No independent verification was performed; single-day moves lack a beta counterfactual and sit inside Nvidia's ordinary daily variance.
  - Statement 3 (200% coverage deficit): `SUBSTANTIVELY ACCURATE` → `PARTIALLY ACCURATE`. Added explicit 3×3 coverage-ratio matrix showing the supported range is **120%–333%**, not ">200%"; only 4 of 9 cells clear 200%. The page's own Path 3 (ARR $40–60B) implies 50–125% coverage, falsifying the "all four scenarios" universality claim.
  - Statement 4 (refinancing trap): retained but added the under-stated hyperscaler channel — **RPO quality re-rating precedes impairment**; Microsoft counterparty concentration noted alongside Oracle.
- **Added Statement 5 — Vendor-Financed Circularity (`UNASSESSED GAP`):** the "Nvidia as Fannie Mae for compute" mechanism present in the source digest but never assessed. Determines *when* the wall arrives; circular financing defers and enlarges rather than cancels it.
- **Added five `⬖ Gray area` callouts** on genuinely contested interpretations rather than overwriting: (1) where "binding" stops being binary in take-or-pay; (2) whether an attributable event study is feasible at all; (3) three definitional choices (exit ARR vs. GAAP, gross vs. net of credits, commenced vs. signed) that swing the coverage ratio more than the bear/bull spread; (4) cluster fungibility assumed not demonstrated; (5) vendor backstop vs. ordinary market-development spend.
- **Added Transmission Channel 5 — Renegotiation & Absorption:** take-or-pay against a distressed sole anchor tenant restructures rather than defaults; resolves the binary framing in §1/§3 that contradicted the page's own Path 2 base case. Loss changes form (revenue quality, RPO discount) rather than disappearing.
- **Surfaced the obscured conclusion:** Paths 1+2 carry ~80% of probability mass and *both* involve significant multiple compression; Path 2's "managed restructuring" label embeds a ~35% derate. Flagged the 30/50/20 split as an underived judgmental prior.
- **Indicators expanded 4 → 6** and converted to a threshold table: added **RPO counterparty concentration** (highest signal, tracks Statement 4's real channel) and **commencement slippage**; flagged indicators 2 and 4 as weakly specified.
- **Added §5 Portfolio Implications:** derating protection over crash protection; separating the neocloud solvency trade from the hyperscaler multiple trade; indicator-linked rather than date-linked sizing.
- **Fixed broken wikilink** `[[cyber-saas-seat-risk]]` → `[[cyber-saas-seat-risk-2-equity-report]]`; converted the misaligned ASCII transmission matrix to a markdown table; added a Review Triggers section.
- Updated: `index.md` (re-assessment noted on the entry)
- Updated: `investing-macro/macro-frameworks/README.md` (noted the accuracy audit and gray-area flags)
- Updated: `log.md`

## [2026-09-01] create & update | FinTech Regulatory & Usury Risk: TILA Reg Z, True Lender Exposure, and Company Pipeline Audits ($DAVE, $SEZL)

- Created: `investing-fundamentals/company-analyses/comparisons/fintech-usury-tila-regulatory-exposure-2026.md`
  - Synthesized the consumer fintech regulatory and usury risk spectrum comparing High Risk ($DAVE, $SEZL, $ML, private EWA), Moderate Risk ($AFRM, $KLAR, $XYZ), and Structurally Immune ($SOFI).
  - Deconstructed the legal mechanics: FDIA Section 27 "True Lender" rent-a-charter vulnerabilities vs. TILA Regulation Z (12 CFR § 1026.4) disguised finance charges (subscriptions, express delivery fees, tipping).
  - Modeled quantitative downside valuation bridges: $DAVE down -78% to -84% ($55–$75) and $SEZL down -81% to -88% ($16–$25) under adverse court injunctions and mandatory fee unbundling.
- Updated: `investing-fundamentals/company-analyses/sezl-2-equity-report.md` (added Accounting Policies & Internal Controls section detailing March 2026 PwC auditor transition, open ICFR material weakness on notes receivable cash flows, ASC 606 vs. ASC 310 revenue recognition tension, and Hindenburg Dec 2024 mitigation scorecard; cross-linked to comparison).
- Updated: `investing-fundamentals/company-analyses/sezl-3-investment-memo.md` (added regulatory reclassification downside valuation bridge of $16.00–$25.00 / -80% to -86% drawdown to Risk section; cross-linked to comparison).
- Updated: `investing-fundamentals/company-analyses/sezl-4-stress-test.md` (cross-linked to comparison).
- Updated: `investing-fundamentals/company-analyses/dave-2-equity-report.md` (deepened legal & regulatory risk analysis with details on FTC + DOJ federal lawsuit Case No. 2:24-cv-09419 in C.D. Cal. naming CEO Jason Wilk individually, City of Baltimore predatory lending suit, and ROSCA $1/mo subscriptions; cross-linked to comparison).
- Updated: `investing-fundamentals/company-analyses/dave-3-investment-memo.md` (added FTC/DOJ adverse ruling valuation bridge of $55.00–$75.00 / -78% to -84% drawdown to Risk #1; cross-linked to comparison).
- Updated: `investing-fundamentals/company-analyses/dave-investment-research.html` (synchronized interactive HTML suite: updated Iceberg Risks table with Case No. 2:24-cv-09419 docket specifics; added dedicated Legal & Regulatory Litigation card in Tab 2; incorporated the $55–$75 regulatory downside valuation bridge in Tab 3; expanded Tab 6 source table with Cross-FinTech Usury Framework link; and added Risk Audit & Litigation section in Tab 7 Complete Dossier).
- Updated: `investing-fundamentals/company-analyses/sezl-investment-research.html` (synchronized interactive HTML suite: updated Iceberg Risks table with TILA Reg Z usury reclassification and OCC bank capital trapped drag; added dedicated Accounting Policies, PwC Auditor Transition & ICFR Material Weakness card in Tab 2; added Hindenburg Dec 2024 Resolution Scorecard in Tab 2; incorporated the $16–$25 regulatory/bank capital downside valuation bridge in Tab 3; expanded Tab 6 source table with PwC 8-K, CFPB docket, and Cross-FinTech Usury Framework links; and added Accounting Governance & Regulatory Downside section in Tab 7 Complete Dossier).
- Updated: `index.md` (indexed new comparison document under Comparisons; bumped total pages to 212).
- Updated: `log.md`

## [2026-09-10] create | DeepSeek V4.1 Flash: Memory Architecture, AI Bottlenecks, and Semiconductor Value Chain Impact

- Created: `investing-fundamentals/company-analyses/themes/deepseek-v4-1-flash-memory-bottlenecks.md`
  - Synthesized comprehensive architectural analysis of DeepSeek V4.1 Flash launched September 10, 2026.
  - Deconstructed core innovations: Causal Encoder-Decoder (CED) with single projected KV cache from 20-layer encoder, Compressed Sparse Attention 2 (CSA2) with Full/Reindex/Reuse modes, FP4 (E2M1) KV quantization, 196B Engram host-prefetched parameter tier, and SWA Bounded Replay.
  - Detailed the **890 bytes/token** global KV cache breakthrough (4× reduction vs. V4-Flash, 437× vs. MHA baseline), demonstrating sub-1GB VRAM requirements for 1M-token context windows and 350+ concurrent stream capacity on 8×H100 nodes.
  - Resolved four foundational bottlenecks: memory bandwidth decode wall, agent multi-turn VRAM capacity wall, prefill/decode asymmetric compute allocation, and storage I/O paging stalls.
  - Mapped equity winners and losers across hardware memory tiers:
    - Enterprise NAND/SSD ($WDC, Kioxia, Solidigm, Samsung/Micron NAND): Critical structural headwind as SWA Bounded Replay eliminates KV cache SSD paging.
    - HBM Pure-Plays (SK Hynix 000660.KS, Samsung 005930.KS): Multiple normalization and pricing power softening as context is decoupled from HBM gigabytes.
    - Server Host DRAM & CXL ($MU, 005930.KS, $ALAB): Major structural tailwind from 196B Engram conditional parameters residing in host DDR5/CXL memory pools (highlighted by Micron CEO attendance).
    - GPU Accelerators ($NVDA, $AMD): High-VRAM markup pricing power softens, but unit volume preserved by 552B MoE footprint and Jevons paradox.
    - Inter-GPU Fabric ($AVGO, $ANET, $MRVL): MoE 552B parameter routing preserves intense All-to-All network demand.
    - Enterprise Software/SaaS ($NOW, $CRM, $PLTR): Restores 75–80%+ gross margins for agentic products by dropping token COGS toward nominal levels.
- Updated: `index.md` (indexed under Themes; bumped total pages to 213; updated date to 2026-09-10).
- Updated: `investing-fundamentals/concepts/ai-inference-costs-accounting.md` (bumped date to 2026-09-10; added cross-reference).
- Updated: `investing-macro/macro-frameworks/ai-compute-commencement-wall-and-refinancing-trap.md` (added cross-reference).
- Updated: `investing-fundamentals/company-analyses/themes/deepseek-v4-1-flash-memory-bottlenecks.md` (expanded Section 2 with technical breakdowns of how CED global KV projection, CSA2 tri-mode attention, native FP4 micro-scaling, Engram deterministic prefetching, SWA Bounded Replay local recomputation, and DSpark speculative decoding function under the hood; integrated the "Alexander the Great" multi-token concept problem and early-layer FLOP savings; added Section 5.G on the geopolitical driver bypassing Western HBM/CoWoS sanctions for Huawei Ascend and Chinese labs).
- Updated: `log.md`

