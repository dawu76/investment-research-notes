---
title: Individual Bonds vs. Bond Funds — Mark-to-Market, Real Returns, and the Annuity Math
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [bonds, rates, inflation, concept, retirement-planning]
sources: []
confidence: medium
contested: false
---

## The core claim being evaluated

A common financial-planning argument: bond funds like TLT (20+yr Treasury ETF) or IEF
(7-10yr) have no maturity date, so a mark-to-market price decline (e.g. TLT down ~43%
over 2021-2026) is a permanent-feeling loss. An individual Treasury bond, by contrast,
returns 100% of face value at a known maturity date (zero credit risk), so — the
argument goes — someone who bought individual long bonds at 2021's near-zero yields
"would not be down 43%, because you get 100% of your money back at the end."

**This is true and important structurally, but incomplete/misleading if read as "so
individual long bonds didn't really lose money."** See [[bond-supply-tsunami-2026]]
section 4 ("Duration Risk Is the Primary P&L Problem") for the underlying duration
math that drives both instruments' price moves.

## What's correct

- Bond funds like TLT/IEF continuously roll their holdings to maintain a target
  maturity band — there is no mechanism by which a dollar in the fund ever "pulls to
  par." NAV just reflects the current market price of the underlying bonds, indefinitely.
- An individual Treasury bond has a hard contractual maturity date at which the U.S.
  government returns 100% of face value, with effectively zero credit risk.
- Coupon payments on an individual bond are contractually fixed; fund distributions
  fluctuate with the changing composition of current holdings.

## What the claim glosses over

### 1. Mark-to-market loss is nearly identical in the interim

A 30-year Treasury bought in 2021 at ~1.9% and now marked at ~4.5-4.8% yields has lost
roughly as much *today* as TLT has (~40-45%, modified duration ~16-18yr × ~2.7-3.0pt
yield rise). The only difference is the individual bond is contractually guaranteed to
amortize that loss back to zero by its maturity date; the fund has no such mechanism
because it never stops rolling into new bonds at whatever the prevailing rate is.

### 2. "100% of your money back" is nominal, not real

This is the biggest omission. Locking in a sub-2% coupon for 30 years while inflation
runs at or above that rate for the holding period guarantees a **real** loss of
purchasing power, even though the nominal principal is fully intact at maturity. See
worked example below, and [[tips-how-they-work]] for the TIPS-based alternative that
avoids this specific problem by indexing principal to CPI.

### 3. The comparison assumes a matched holding horizon

The "you get 100% back" framing only holds if you never need to sell before the bond's
final maturity. Retirees who need to rebalance or draw on the position before maturity
realize close to the same mark-to-market loss as a fund holder would. The real fix is
matching bond maturities to actual spending/rebalancing horizons (see
[[retirement-planning-strategy]]), not concluding individual bonds are loss-proof.

## Worked example: real loss including coupons

Setup: $100,000 face value, 1.9% coupon (bought at par, so nominal YTM = coupon rate),
30-year maturity from 2021, constant 3%/year inflation for the full holding period.
(Simplified to annual coupons rather than the actual semiannual UST convention.)

**Real yield-to-maturity (exact, not approximate, given constant inflation):**

$$r_{real} = \frac{1+y_{nominal}}{1+i} - 1 = \frac{1.019}{1.03} - 1 \approx -1.07\%\text{/year}$$

Compounded over 30 years: $(1 - 0.0107)^{30} \approx 0.725$ — i.e. $100,000 of 2021
purchasing power becomes the equivalent of **~$72,500** of 2021 purchasing power by
2051 if coupons are reinvested at that same real rate. **Cumulative real loss: ~27.5%.**

**Alternative — spend each coupon as received, no reinvestment:** deflate each cash
flow back to 2021 dollars and sum, without further compounding:

- Coupons: $1,900/year × annuity factor (see below, ≈19.60) ≈ **$37,240** (2021 dollars)
- Principal: $100,000 × $(1.03)^{-30} \approx 0.412$ ≈ **$41,200** (2021 dollars)
- Total real value received ≈ **$78,440** vs. $100,000 invested → **~22% real loss**

Either way — whether coupons are reinvested at the (negative) real rate or simply spent
as received — a 30-year Treasury bought at 1.9% with 3% inflation over the holding
period delivers a real loss on the order of **20-30% of original purchasing power**,
arriving smoothly as underpaid coupons rather than as a visible drawdown.

## The present-value annuity factor

Used above to value the coupon stream. Instead of discounting 30 separate coupon
payments one at a time, the present value of $1/year for $n$ years at rate $i$ has a
closed-form sum (geometric series):

$$PV = \frac{1 - (1+i)^{-n}}{i}$$

For $i = 3\%$, $n = 30$: $(1.03)^{30} \approx 2.4273$, so $(1.03)^{-30} \approx 0.4120$.
Annuity factor $= \frac{1 - 0.4120}{0.03} \approx 19.60$.

Interpretation: a stream of $1/year for 30 years, deflated at 3%/year, is worth $19.60
today — not $30 — because later payments are worth much less in present-value terms.
As $n \to \infty$, the factor converges to $1/i$ (here, $1/0.03 \approx 33.3$, the
value of a perpetuity); at 30 years you're already at 19.60 of that 33.3 ceiling,
meaning far-out payments (year 25-30) contribute very little to the total.

## Bottom line

The genuinely useful takeaway isn't "individual bonds don't lose money" — it's
**duration-matching**: judge a bond you intend to hold to maturity by its terminal
(nominal) outcome, not its interim mark-to-market price, but don't mistake nominal
principal preservation for real value preservation, and don't assume a 20-30yr
maturity is the right instrument unless your actual spending/rebalancing horizon
is that long. See [[bond-supply-tsunami-2026]] for the supply-side forces currently
pushing long yields higher, and [[sequence-of-returns-risk]] for why retirees'
actual horizons are usually much shorter than a bond's stated maturity would suggest.
