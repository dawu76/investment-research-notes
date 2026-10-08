---
title: "Brookings: Financing the AI Buildout (Van Nieuwerburgh, Sept 2026) - Takeaways, Data Checks and Historical Comparisons"
created: 2026-09-30
updated: 2026-10-02
type: concept
tags: [credit, bonds, infrastructure, cloud, risk, thesis, valuation, comparison]
sources:
  - https://www.brookings.edu/wp-content/uploads/2026/09/4c_Van-Nieuwerburgh.pdf
  - https://www.brookings.edu/articles/financing-the-ai-buildout/
  - investing-fundamentals/company-analyses/themes/ubp-financing-ai-build-out-2026-09.md
  - investing-fundamentals/company-analyses/themes/burry-ai-capital-cycle-oracle-jupiter-2026-09.md
  - reading-list/notes/market-newsletter-digest-2026-09-24.md
confidence: high
contested: false
---

# Brookings: Financing the AI Buildout (Van Nieuwerburgh, September 2026)

Author: Stijn Van Nieuwerburgh, Columbia Business School. Brookings Papers on Economic Activity (BPEA), Fall 2026 conference draft, title-page draft date September 4, 2026, presented at the BPEA conference September 24-25, 2026. Full 28-page PDF read directly (text extracted via `pdftotext`, not a secondhand summary). An academic paper, not sell-side research: no rating, no trade recommendation, and the author discloses no conflicts of interest. ^[brookings]

See [[ubp-financing-ai-build-out-2026-09]] for a detailed comparison against UBP's identically-titled fixed-income note published eight days earlier; this page covers the Brookings paper on its own terms.

## The argument in five lines

1. The AI buildout is a physical capital investment cycle, not just a software story: a 1GW AI campus costs about $41B, and a 183GW U.S. buildout completed by 2032 requires annual investment averaging 3.63% of GDP over 2025-2032, larger relative to the economy than the canal, railroad, electrification, highway, or telecom booms.
2. Hyperscaler capex ($800.5B projected 2026) is for the first time exceeding the five firms' combined operating cash flow ($707.1B), forcing a shift from internal funding toward leases, joint ventures, project debt, private credit, securitization, and special-purpose vehicles (SPVs).
3. This shift expands funding capacity but raises asset-level leverage, obscures contingent obligations, and concentrates exposure in tenant credit, technological obsolescence, and execution risk, illustrated in detail through Meta's Hyperion/Beignet financing structure.
4. The paper computes, rather than assumes, what the buildout needs to work: at a 10% unlevered return and a 50% operating margin, the 2025-2032 buildout requires $3.725 trillion in mature annual revenue by 2032, equivalent to roughly 80%/year revenue growth for OpenAI and Anthropic combined, from their current ~$100B base.
5. The paper does not call a bust. Its explicit conclusion is that it would be "premature to conclude that AI infrastructure already poses systemic risk," and its main policy recommendation is better measurement and disclosure of off-balance-sheet exposure while the capital structure is still forming.

## Key data points

| Item | Figure |
|---|---|
| Total AI buildout investment, 2025-2032 | $10.3T ($10,279B), averaging 3.63%/year of GDP |
| Representative 200MW AI campus cost | $8.2B: 26.8% facility ($2.2B), 4.9% incremental power infrastructure ($0.4B), 68.4% IT equipment ($5.6B, incl. GPU racks at $4.0M each) |
| Cost basis | $41M per MW in 2025, growing 4%/year, alongside 4%/year nominal GDP growth assumption |
| US data center pipeline (Cleanview database, accessed July 2026) | 57GW operating; 509GW planned/announced pipeline; 2,933 operational-or-planned projects (566GW) tracked in total |
| Capacity realization scenario, 2025-2032 (the paper's central scenario, not a forecast) | 182.7GW completed by 2032; 117.2GW completed after 2032; 226.9GW never completed (44.5GW/kW-equivalent realization rate on the pipeline) |
| Hyperscaler capex, 5 firms (Oracle, Microsoft, Amazon, Meta, Alphabet) | $96.8B (2020) -> $400B+ (2025) -> $800.5B (2026E) |
| Hyperscaler operating cash flow, same 5 firms | $707.1B (2026E), first year capex exceeds OCF |
| Morgan Stanley's financing-split estimate, 2025-2028 incremental compute needs | $2.9T total, ~60/40 equity/debt; within debt: ~$800B private credit, ~$200B corporate debt, ~$150B structured finance |
| Off-balance-sheet obligations (WSJ tally, cited by Brookings; 4 firms, ex-Oracle) | $2.4T: $904B future lease commitments + $1.52T future purchase commitments (mostly chips), vs. $604B on-balance-sheet ($356B long-term debt + $248B current lease obligations), only ~1/5 of $3T total datacenter-related obligations currently recognized on balance sheet |
| Moody's lease-commitment estimate (hyperscalers) | ~$970B total lease commitments, of which ~$660B not yet reflected on balance sheet |
| Meta Hyperion/Beignet JV with Blue Owl | 2.0GW, ~$30B total investment; Meta sold an 80% equity stake to Blue Owl for ~$2.5B; Beignet raised $27B of debt (Oct 2025), rated A+ (one notch below Meta's own corporate rating), the largest individual investment-grade corporate debt issuance in U.S. history; ~90% debt-to-asset ratio; debt-service coverage ratio only 1.12x; priced at 6.58%, >100bp above what Meta's own unsecured debt would likely have cost, implying >$5B of additional interest expense over the financing's life |
| Sopaipilla JV (Meta/BlackRock, El Paso TX) | 960MW; $12.3B of A+-rated bonds issued July 2026, following a nearly identical structure to Beignet |
| $500B NVIDIA-backstopped credit facility (Aug 2026) | Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs, and KKR fund NVIDIA chip purchases; NVIDIA provides a 25% residual value guarantee, exposing it to up to $125B of backstops. A similar Google/Broadcom arrangement finances TPU acquisition |
| Data center REIT beta vs. S&P 500 | Risen from ~0.5 to ~1 since 2018 (36-month rolling window); exposure to the non-AI component of the S&P 500 is now comparable to exposure to AI stocks, data centers behave less like a diversifying/defensive asset and more like part of the broader systematic-risk complex |
| Revenue required to "pencil out" (Appendix D, central case) | $3.725T mature annual revenue by 2032 (9.2% of 2032 GDP), at a 10% required unlevered return and a 50% operating cash-flow margin; capital base at commissioning for the 182.7GW buildout is $9.61T (vs. $8.54T raw construction cost, reflecting a 1.126x adjustment for return during construction) |
| Revenue requirement sensitivity | $2.29T at 5% required return / 67% margin, up to $6.72T at 15% required return / 33% margin; rises to $6.0T (14.8% of 2032 GDP) if IT equipment's economic life is 3 years instead of the central 6-year assumption |
| Implied GPU-hour pricing (central case) | $5.5/GPU-hour at 100% utilization, $6.9/GPU-hour at 80% utilization, $7.9/GPU-hour at 70% utilization, against current market pricing of roughly $6-10+/hour for on-demand frontier GPU capacity |
| Historical U.S. capex booms, % of GDP (paper's Table 1) | Canals 1836-41: 0.66%; Railroads 1870-90: 2.24%; Electrification 1905-25: 0.50%; Highways 1956-73: 1.13%; Telecom/fiber 1996-2003: 1.10%; AI buildout 2025-32: 3.63% |

## Takeaways for investors

1. **The buildout's economic validity rests on one explicit, falsifiable bar.** OpenAI and Anthropic's combined revenue needs to compound at roughly 80%/year, sustained to 2032, from today's ~$100B base, to clear the paper's central required-revenue estimate. This is trackable every quarter against actual ARR disclosures and is a sharper test than qualitative "is AI demand real" framing.
2. **The Hyperion/Beignet structure is becoming a template, and each instance carries a visible risk premium.** Sopaipilla already replicates it. The >100bp spread Beignet pays over what Meta's own unsecured debt would cost is a market-observable price for moving the asset off Meta's balance sheet, watch whether that spread widens or compresses as more of these deals price.
3. **Reported hyperscaler leverage is the wrong leverage metric.** Off-balance-sheet obligations run roughly 3-4x on-balance-sheet debt (consistent with UBP's independent 3.3x estimate), and the ratio itself (not just the absolute dollar figure) is the thing worth tracking quarter over quarter as a proxy for how fast risk is migrating off GAAP balance sheets.
4. **The GPU economic-life assumption drives much of the result.** Moving from a 6-year to a 3-year assumption for IT equipment nearly doubles the GDP share of required revenue (9.2% -> 14.8%). Any shift in disclosed depreciation schedules, consensus useful-life assumptions, or realized GPU resale values is a direct, mechanical input into whether the buildout's economics improve or deteriorate, more informative than headline capex growth rates alone.
5. **Data center REITs no longer diversify AI exposure.** With beta to the broad market converged to ~1 and non-AI/AI stock exposure now comparable, treating data center REITs as a lower-correlation "picks and shovels" way to play the buildout is no longer supported by the paper's own return data.
6. **The NVIDIA-backstopped facility is a vendor-financing circularity worth watching the way Cisco/Lucent/Nortel vendor financing was watched in 2000-01.** A chip supplier guaranteeing 25% of the residual value on its own product, up to $125B, is a tell about how much balance-sheet support the supplier itself believes its customers' purchases need.
7. **The paper's own restraint is itself a data point.** This is the most methodologically rigorous model-based treatment of AI-buildout financing risk available, and it explicitly declines to call systemic risk "yet." That absence of alarm, from a source with no commercial incentive either way, is worth weighing against noisier bearish newsletter calls (e.g., QTR's Fringe Finance and MacroEdge Research in [[market-newsletter-digest-2026-09-24]]) that assume an imminent unwind without a comparable quantitative basis.

## Checking the claims

### Internal arithmetic

Every reported total in the paper was independently recomputed and checks out cleanly, a sharp contrast to the UBP note (see below), which had a cumulative-capex transposition error and an overstated Oracle index-cap buffer.

- **Table 5 (annual investment) sums correctly.** The eight annual investment figures (1,153 + 1,432 + 1,399 + 1,098 + 791 + 940 + 1,408 + 2,058) sum to $10,279B, matching the quoted $10.3T. The eight nominal-GDP figures sum to $283,448B. The ratio (10,279/283,448 = 3.627%) matches the quoted 3.63%, and the simple average of the eight annual investment/GDP ratios (3.75, 4.48, 4.20, 3.17, 2.20, 2.51, 3.62, 5.08) also averages to 3.63%, confirming the paper's claim that both methods agree.
- **Table 6 (capital and required revenue by cohort) sums correctly.** GW (182.6 vs. stated 182.7), cost ($8,537.9B vs. stated $8,538.0B), capital required ($9,613.7B vs. stated $9,613.8B), profit/required operating cash flow ($1,862.4B, exact match), and required revenue ($3,724.7B vs. stated $3,724.8B) all reconcile to within rounding.
- **The construction-period capital multiplier checks out.** φ = 0.10(1.1)³ + 0.25(1.1)² + 0.40(1.1) + 0.25 = 0.1331 + 0.3025 + 0.44 + 0.25 = 1.1256, matching the paper's stated 1.126x adjustment from raw cost ($8.54T) to capital base at commissioning ($9.61T).
- **The capital-recovery-factor math checks out.** At r=10%: a(10%, 6-year) = 0.10(1.1)⁶/[(1.1)⁶-1] = 0.1772/0.7716 = 22.96% (exact match); a(10%, 20-year) = 0.10(1.1)²⁰/[(1.1)²⁰-1] = 0.6728/5.7275 = 11.75% (exact match). The weighted charge, 0.68 × 22.96% + 0.32 × 11.75% = 19.37%, matches exactly.

No arithmetic or reconciliation issues were found anywhere in the paper during this check.

### Against other data in the wiki

- **Parekh's digest citation matches exactly.** [[market-newsletter-digest-2026-09-24]] §4 cites Michael Parekh citing this paper's "$10.3 trillion... about 3.6% of US GDP per year for eight years" figure, this matches the paper's own $10.3T / 3.63% precisely, confirming accurate secondhand transmission.
- **Off-balance-sheet obligation estimates triangulate loosely across three independent sources now in this wiki**, despite different firm counts and category definitions: Brookings/WSJ tally $2.4T (4 firms, ex-Oracle; leases + purchase commitments only), UBP $2.9T (5 firms; leases + purchase commitments + Meta/Alphabet guarantees; see [[ubp-financing-ai-build-out-2026-09]]), and Burry's ~$3T (5 firms; broader categories including construction-in-progress; see [[burry-ai-capital-cycle-oracle-jupiter-2026-09]]). All three land in the same $2.4-3T zone. This is a useful cross-check rather than a coincidence: the paper's own Section VI explicitly calls for "triangulating multiple data sources" to address this measurement gap, citing a forthcoming companion paper (Van Nieuwerburgh and Sun, 2026, "Clouds of Credit: Mapping the Financial Web Behind AI Compute") and private data providers such as Atrium.ai as efforts in the same direction.
- **Moody's lease-commitment figure is narrower in scope than UBP's.** Brookings cites Moody's ~$970B total lease commitments (~$660B not yet on balance sheet); UBP's "$1.16T leases signed not commenced" is a related but not identical category. The mismatch is not a contradiction. It illustrates the paper's core measurement-gap argument: "off-balance-sheet lease commitments" does not yet have one settled definition across sources.
- **McKinsey's prior estimate has been overtaken.** The paper cites McKinsey's April 2025 estimate of a "$7 trillion race to scale data centers" as a prior comparable projection, about 30% below Brookings' own $10.3T figure derived roughly a year and a half later. The direction of revision across outside estimates has been consistently upward.
- **Oracle's Jupiter force majeure postdates the paper and is not discussed in it**, but is a live instance of exactly the execution-risk category (grid interconnection, permitting, hardware delays) the paper's Section V and abstract flag as a vulnerability. See [[burry-ai-capital-cycle-oracle-jupiter-2026-09]] and [[market-newsletter-digest-2026-09-24]] §3.

### Methodological points

- **The revenue-required model holds required return and operating margin constant across the full forecast horizon.** It does not separately model declining per-unit GPU cost or pricing (a Jevons-paradox-style volume response) over time, nor margin compression from rising hyperscaler/neocloud competition, either could move the required $/GPU-hour away from the paper's central $5.5-7.9 range without the paper's framework capturing which direction dominates.
- **The $10.3T / $3.7T figures are already the paper's central (not worst) case.** The 182.7GW realized out of a 509GW announced pipeline (a 44.5% out of total addressable realization, net of the "never completed" 226.9GW) is a judgment call built into the scenario, not a conservative floor, meaning the revenue-required bar is not an upper-bound stress case, it's the base case.
- **The model is explicitly unlevered.** The 10% required return is an unlevered cost of capital; actual project financing is highly levered in practice (Beignet at ~90% debt-to-asset per Section IV). The paper does not translate its revenue-required framework into implied equity IRRs under realistic leverage, leaving the amplified volatility of actual equity outcomes (much more sensitive to revenue shortfalls than the unlevered 10% hurdle suggests) as an exercise for the reader.
- **The $10.3T estimate excludes future hardware refresh cycles.** The paper explicitly notes that 2025-26 vintage GPU capacity will likely need substantial replacement by around 2030, even though buildings and power infrastructure remain usable, meaning cumulative gross investment through the full useful life of this capacity, not just its initial build, is higher than the headline figure.

## Historical comparisons (paper's Table 1, with its own caveats)

| Episode | Period | Size (% of GDP) |
|---|---|---|
| Canals | 1836-1841 | 0.66% |
| Railroads | 1870-1890 | 2.24% |
| Electrification | 1905-1925 | 0.50% |
| Highways | 1956-1973 | 1.13% |
| Telecom and fiber | 1996-2003 | 1.10% |
| AI buildout | 2025-2032 | 3.63% |

The paper's own caveat on this table matters as much as the numbers: historical comparisons based on gross investment require caution because the created assets have very different economic lives. Canals, railroads, and fiber often delivered service for decades; GPUs may become economically obsolete within three to six years. The AI buildout therefore generates less net capital formation per dollar of gross investment than most of the historical comparisons in the table, even though it is nominally the largest of the six as a share of GDP, a nuance that a bare comparison to the railroad or telecom booms (as several newsletters covered in this wiki's digests tend to make) elides.

## Verdict

This is the most rigorous model-based treatment of AI-buildout financing economics in the wiki to date: every reported arithmetic result reconciles exactly on independent recomputation, the capacity and investment estimates are built from a disclosed project-level database with a documented econometric methodology (not assumed top-down), and the central contribution (a formal answer to "what revenue does this need to generate to earn a normal return") is something no other source in this wiki's AI-financing coverage (UBP, Burry, the newsletter digests) attempts to compute directly. Its conclusion is appropriately narrow: it defines the revenue bar (~80%/year growth, ~$3.7T by 2032) rather than forecasting whether it will be cleared, and explicitly declines to call systemic risk premature. Two caveats on status: it is a conference draft (title-page draft dated September 4, 2026, presented September 24-25) rather than a published, peer-reviewed paper, and as an academic exercise in scenario construction it carries real sensitivity to its own realization-rate and economic-life assumptions, which the paper is transparent about but does not resolve.

## Cross-References

- [[ubp-financing-ai-build-out-2026-09]]: the identically-titled UBP credit note; full comparison of overlap and divergence lives there
- [[burry-ai-capital-cycle-oracle-jupiter-2026-09]]: Burry's ~$3T aggregate off-balance-sheet estimate, which triangulates with this paper's $2.4T WSJ-tallied figure
- [[market-newsletter-digest-2026-09-24]]: Michael Parekh's citation of this paper's $10.3T/3.6%-of-GDP estimate (§4), alongside Burry's independent capital-cycle data in the same section
- [[ai-compute-commencement-wall-and-refinancing-trap]]: commencement-timing and off-balance-sheet framework this paper's Sections III-V extend with original modeling
- [[ai-inference-costs-accounting]]: GPU-hour pricing and inference-cost economics relevant to the paper's required-revenue-per-GPU-hour calculation
- [[sage-road-ai-trade-2026-09]]: Sage Road Research's "market rupture" thesis, assessed against this paper's "premature to conclude systemic risk" finding
