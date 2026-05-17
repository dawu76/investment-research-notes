# US Tax Interaction: Property Sale vs. Other Investment Income

*Research date: May 2026 | Related documents: tax-research-plan.md, tax-research-tw-gains.md*

---

## Motivating Questions

1. For a representative unit in the 觀海極品 condo community (30坪 baseline), the US federal and state taxes on the property capital gain appear to be quite low as a percentage of the overall sale price — and much lower than the taxes owed to the Taiwanese government. To what extent would the US taxes be affected by non-real estate income in the same year as the property sale — specifically income from short-term vs. long-term stock and options gains, US Treasuries, and municipal bonds?

2. If the property is likely to sell in August of a given year, should investment strategies in the time leading up to that date be adjusted to favor more income from long-term capital gains and tax-exempt bonds/bond funds? Or would it not make much of a difference?

---

## Short Answer

The composition of other US investment income in the sale year **matters very little** for the property-specific US tax exposure, and restructuring a portfolio specifically around the property sale is not worth the effort. The Taiwan tax (~$21K–$38K USD depending on regime) is the dominant liability; the total US exposure on the property gain is ~$1,500–$2,400, and it is not materially moved by investment composition choices.

---

## Why Other Income Barely Affects the Property's US Tax Exposure

### Layer 1: Federal Income Tax on the Capital Gain → FTC Eliminates It Regardless

The inherited property gain is automatically long-term (IRC §1223(11)), so it is taxed at 0%/15%/20% depending on total taxable income. At the gain levels for a 30坪 unit ($0–$14K USD, per the exchange rate sensitivity analysis in tax-research-tw-gains.md), the maximum federal income tax is:

- At 15% rate: ~$2,087
- At 20% rate: ~$2,782

The Foreign Tax Credit (FTC) from Taiwan taxes (Old System: ~$20,700; HSTT: ~$37,500) is **10–18× that amount**. Even in a worst-case FTC limitation scenario — where high domestic income shrinks the passive basket percentage on Form 1116 — the FTC still covers $2–3K of income tax with ease.

Whether other income pushes the property gain from the 15% to the 20% bracket is a $695 question that the FTC absorbs regardless.

**Practical implication:** Do not optimize investment income for LTCG bracket management in the sale year — it is irrelevant once the FTC is applied.

**Legislative note (May 2026):** The *United States-Taiwan Expedited Double-Tax Relief Act* (H.R. 33) passed the House in early 2026 but explicitly excludes real estate capital gains. The FTC remains the sole mechanism for double taxation relief on this transaction — this legislation does not change the analysis.

**FTC carryforward note:** If Taiwan taxes generate FTC credits in excess of the Form 1116 limitation in the sale year, excess credits carry forward **10 years** (and back 1 year). If high-income years with foreign income are expected in the following decade, excess FTC is valuable and does not go to waste. Conversely, if income is expected to be low in those years, the carryforward may expire unused. This is a reason to discuss the sale timing with a US CPA relative to Form 1116 limitation capacity — but it is not a portfolio restructuring question.

**Timing caution — cash-basis FTC mismatch:** Most individuals claim FTC in the year the foreign tax is **paid** (cash basis, IRC §905(b)). If the sale closes in late December 2026 but Taiwan tax is not remitted until January 2027, US income tax on the 2026 gain will be owed on the 2026 return with no credit to offset it — the credit would only appear on the 2027 return. Practical fix: ensure Taiwan taxes are paid before December 31 of the closing year. Alternatively, the **Accrual Election (IRC §905(a))** allows claiming FTC in the year the liability arises rather than the year paid, but this election is irrevocable for all future years and requires discussion with a CPA before making it.

---

### Layer 2: NIIT (3.8%) → Almost Certainly Triggered Already by Other Income

NIIT applies if MAGI > $200K (single) / $250K (MFJ). With significant stock, options, and bond income, the threshold is almost certainly already exceeded in any year, with or without the property sale.

The NIIT on the property gain itself is at most **$529** (3.8% × $13,910 maximum gain). More importantly, the NIIT threshold is a **cliff, not a slope** — if MAGI is already above $200K/$250K, other investment income is already being taxed at 3.8%, and the property gain simply adds $529 to the pile.

The only scenario where restructuring would make sense for NIIT purposes is if MAGI would be *just below* $200K/$250K without the property gain — which is unlikely given the described income profile.

**Municipal bond note:** Municipal bond interest is excluded from Net Investment Income (NII) under IRC §1411 — it reduces both MAGI and the NII base, directly reducing NIIT on all NII. But the NIIT savings specifically attributable to the property gain is $529 maximum; munis would need to reduce MAGI below the $200K/$250K threshold to matter meaningfully for the property-related exposure.

---

### Layer 3: California State Tax → Real Exposure, but Small and Not Sensitive to Income Composition

California taxes the property gain as ordinary income at up to 13.3%, with no preferential LTCG rate and no foreign tax credit for Taiwan taxes paid. This is the one layer where other income genuinely interacts with the property — higher total California income pushes the marginal rate on the property gain upward:

| CA taxable income | Marginal rate | Tax on $13,910 gain |
|---|---|---|
| ~$100K–$300K | 9.3% | $1,294 |
| ~$300K–$500K | 10.3% | $1,433 |
| ~$500K–$1M | 11.3% | $1,572 |
| >$1M | 13.3% | $1,850 |

The range across all income levels is **$1,294–$1,850** on the property gain — a spread of only ~$556 between the lowest and highest marginal rate. That does not justify restructuring a portfolio. The same conclusion applies to the choice of sale year: moving the property sale to a lower-income California year produces the same ~$556 swing and similarly does not justify timing the sale for California income-level reasons. Of the three US tax layers, California is the only one that is income-level-sensitive — federal income tax is neutralized by the FTC regardless of bracket, and NIIT is effectively a cliff that is already triggered for the described income profile.

*Note: if the sale produces a USD loss (2026 exchange rate ≥ NT$30/USD, which the sensitivity analysis shows is a meaningful probability), California tax on the property gain is $0 regardless.*

---

## Analysis by Income Type

| Income type | Effect on property sale's US tax |
|---|---|
| **Long-term stock/options gains** | Fills LTCG brackets alongside the property — but FTC covers the income tax regardless; marginal impact is zero |
| **Short-term stock/options gains** | Taxed as ordinary income; fills lower brackets, potentially pushing property gain from 15% to 20% bracket — FTC covers the ~$695 rate difference |
| **US Treasuries** | Ordinary income; adds to MAGI and NII, slightly increases NIIT on other income. Not material to the property-specific exposure |
| **Municipal bonds** | Excluded from NII (IRC §1411); reduces MAGI and NIIT base. Genuinely beneficial for NIIT across the overall portfolio, but incremental benefit attributable to the property gain specifically is $529 maximum |

---

## Should Investment Strategy Be Adjusted in the Year of the Sale?

**No, not specifically for the property sale.** The total US tax exposure from this transaction (~$1,500–$2,400 for NIIT + California combined) is too small to justify portfolio decisions. The Taiwan HSTT or Old System tax is 15–25× larger.

### Two Genuine Exceptions Worth Discussing With a US CPA

**1. If MAGI is close to the NIIT threshold**
If MAGI would be near $200K/$250K without the property gain, shifting to muni bonds in the sale year reduces the 3.8% hit on *all* NII — not just the $529 on the property. This is the one scenario where investment composition in the sale year has amplified impact. Given the described income profile (substantial stock/options/bond income), this scenario seems unlikely.

**2. FTC carryforward capacity**
If the Form 1116 passive basket limitation in the sale year is expected to be low (high domestic income relative to foreign income), a larger fraction of Taiwan taxes will generate excess FTC credits rather than current-year offsets. If future years are expected to have foreign income against which to use excess credits, this is fine. If not, consider whether the sale can be timed to a year with higher foreign passive income (e.g., a year with foreign dividend income or a year with lower domestic income), which would allow more of the Taiwan FTC to be used currently rather than carried forward.

---

## Where to Actually Focus Planning Energy

The property sale's US tax exposure is fixed and small regardless of investment choices. The decisions that move the needle materially are:

1. **Confirm the original purchase date** — approximate month confirmed as **April 2012** (exact day TBD via title deed search at the local 地政事務所). Pre-Jan 2016 → Old System applies (~$20,700 vs. ~$38,000 under HSTT). Nothing in the US investment portfolio comes close to this lever.

2. **Confirm the actual registered area (登記面積)** from the 謄本 or 房屋稅籍證明書. The market value estimates span NT$3–4M depending on unit size; this is the largest single unknown in the total tax estimate.

3. **Commission the 不動產估價師 retroactive appraisal** now (effective date May 2022) to lock in the highest defensible US stepped-up basis before the property is sold and memories fade.

4. **Monitor the TWD/USD rate** as the sale approaches. The breakeven rate is approximately NT$30/USD (unit only). If the rate is above NT$30 at closing, the sale produces a USD loss and the US income tax exposure on the property is zero. This is a larger lever than any investment portfolio adjustment.

---

*All estimates based on 30坪 baseline and central 2026 price assumption of NT$42万/坪. See tax-research-tw-gains.md for full sensitivity analysis and assumptions. Confirm all tax positions with a US CPA and Taiwan CPA before the sale.*

