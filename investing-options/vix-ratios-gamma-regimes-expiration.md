# VIX Ratios, Gamma Regimes, and Expiration Mechanics

## Background: The Volatility Stack

### What is Implied Volatility (IV)?

When options are priced, the market embeds a forward-looking estimate of how much an underlying will move. This is *implied volatility* — the IV you back out from an option price using Black-Scholes. Higher IV = more expensive options = market expects larger swings.

IV is not one number — it exists at every layer of the market simultaneously.

---

## The Three Measures

### VIX — S&P 500 Index Level

The CBOE VIX measures the 30-day implied volatility of SPX (S&P 500 index) options directly. It is constructed from a wide strip of SPX calls and puts across strikes, weighted to reflect the market's aggregate expectation of index-level volatility. It is the "fear gauge" of the whole index as one instrument.

### VIXEQ — Constituent-Level Volatility

VIXEQ represents the *median implied volatility across the individual S&P 500 member stocks*. Rather than looking at the index option market, it looks at the options on each of the 500 companies individually. This measures how volatile each stock is expected to be on its own terms — its *idiosyncratic* or single-name volatility.

### VOLI — ETF-Layer Volatility

VOLI measures implied volatility derived from SPY (the SPDR S&P 500 ETF) options, weighted toward shorter tenors and including zero-days-to-expiration (0DTE) options. SPY options are the dominant venue for retail and institutional intraday hedging. Because SPY is extremely liquid at short tenors, VOLI tends to reflect the *immediate, tactical hedging layer* of the market — what's happening in the next few hours to days.

### Why Three Layers?

| Layer | Instrument | Typical User | Tenor |
|-------|-----------|-------------|-------|
| VIX / SPX options | SPX index | Macro funds, portfolio hedgers, vol funds | Weeks–months |
| VIXEQ / single-name options | Individual stocks | Equity traders, dispersion desks, stock pickers | Days–weeks |
| VOLI / SPY 0DTE options | SPY ETF | Retail, tactical day-traders, intraday hedgers | Hours–days |

Under *normal* conditions, these layers move together. When something breaks in their relationship, it tells you *where* stress is originating and *what kind* of hedging demand is driving it.

---

## The Ratios: VIX/VIXEQ and VIX/VOLI

### VIX/VIXEQ — Index Vol vs Single-Name Vol

This ratio tells you whether the market is pricing the *index* as more dangerous than the *sum of its parts*.

In a perfectly efficient world, index volatility should be *lower* than the average constituent volatility, because stocks don't all move together (correlation < 1 means diversification reduces index vol):

```
σ_index ≈ √( Σ wᵢ² σᵢ² + Σᵢ≠ⱼ wᵢwⱼ σᵢσⱼ ρᵢⱼ )
```

When correlation (ρ) rises toward 1, individual stocks lose their independence and the index behaves as a single, undiversified instrument.

- **VIX/VIXEQ rising** → index vol increasing faster than single-name vol → market is repricing *correlation higher*. Stocks are increasingly moving together. The index is becoming more dangerous per unit of constituent risk.
- **VIX/VIXEQ falling** → index is calm but individual stocks are volatile → dispersion is high, single names are doing their own thing.

### VIX/VOLI — SPX Vol vs SPY ETF Vol

This ratio tells you whether the deeper institutional SPX options market is more agitated than the liquid SPY ETF market.

- **VIX/VOLI rising** → institutional-grade SPX hedging demand is outpacing ETF-layer hedging → people are bypassing intraday SPY noise and going straight to SPX puts for protection. Signals *size* and *urgency* — large portfolio managers, not day-traders.

When both ratios spike simultaneously: sophisticated, macro-scale hedging demand is moving into SPX index options, correlation is rising, and the market is losing the diversification buffer that normally dampens index-level moves.

---

## Dispersion, Correlation, and the Dealer Book

### Dispersion Trading

Dealers and sophisticated vol desks run *dispersion trades*: sell index volatility (expensive) and buy single-name volatility (cheaper), profiting from the fact that VIX historically trades at a premium to VIXEQ. This works because stocks don't all move together perfectly.

When VIX/VIXEQ spikes, the spread the dispersion trader was harvesting widens — but the correlation assumption embedded in the position is breaking down. If correlation unexpectedly rises toward 1, losses on the short-index-vol leg aren't offset by gains on the long-single-name-vol leg.

### The Idiosyncratic Cushion

Dealers who sell SPX options hedge their vanna exposure (how delta changes as IV changes) using a combination of:
1. Single-name options (cheaper, idiosyncratic, offset each other)
2. ETF options (liquid, low-cost intraday)
3. Other index options

When VIXEQ is high and stocks are volatile on their own terms, dealers have room to maneuver — they can hedge across many names and positions net out. When VIX/VIXEQ rises (VIXEQ not keeping up), that idiosyncratic cushion erodes. Dealers are forced to hedge more directly in the SPX book, which is deep but *less flexible* — large block trades move it more than the combined ETF/single-name market.

---

## Gamma Regimes: Positive vs Negative

### Options Greeks: Delta and Gamma

**Delta** — how much an option's price changes per $1 move in the underlying. A call with delta 0.5 gains $0.50 for every $1 the index rises.

A put option as an instrument always has a **negative delta** (between −1 and 0) — its value rises as the stock falls. But the sign of your *position* delta depends on whether you are long or short the option:

- **Long put (buyer):** your position delta = the option's delta → **negative**. Your position gains as stock falls.
- **Short put (seller):** your position delta = the negation of the option's delta → **positive**. Your position gains as stock rises, loses as stock falls — economically equivalent to a partial long position in the stock.

As the stock falls toward the put's strike, the option's own delta moves from near 0 (far OTM) toward −0.5 (at the money) toward −1 (deep ITM). The consequences for each side:

| | Long put (buyer) | Short put (seller) |
|--|--|--|
| Position delta | Negative (−1 to 0) | Positive (0 to +1) |
| As stock falls | Delta becomes more negative → position gains | Delta becomes more positive → exposure increases |
| At expiration, deep ITM | Delta = −1 (full short-stock equivalent) | Delta = +1 (full long-stock equivalent, obligated to buy at strike) |

The put seller's increasing positive delta is exactly the intuition you would expect: as the stock falls toward the strike, the seller is becoming more and more obligated to buy the stock at the strike price. Full delta of +1 at expiration means they are fully exposed — economically indistinguishable from owning the stock outright.

**Gamma** — how fast delta changes as the stock price moves. The put option itself has **positive gamma**: as stock falls, the option's delta becomes more negative; as stock rises, less negative.

The **short put position** has **negative gamma** — the negation of the option's gamma. Because of this sign flip, the short put seller's positive delta moves *with* the falling price rather than against it:

```
Stock falls → short put delta increases toward +1  (more exposed, more long-like)
Stock rises → short put delta decreases toward  0  (less exposed, less long-like)
```

Negative gamma means your delta moves in the opposite direction to price changes. This has a critical implication for anyone hedging a short put position: when the stock falls and your delta increases (you are getting longer), you must *sell* stock to stay neutral. When the stock rises and your delta decreases (you are getting shorter), you must *buy* stock. You are always chasing the move — selling into weakness, buying into strength. This is why short gamma is destabilizing.

**Vanna** — how much delta changes as implied volatility changes (cross-derivative of delta with respect to IV). Relevant when both price and vol are moving simultaneously, which is almost always the case in stress events.

**Theta** — how much an option loses in value per day from the passage of time alone. Sellers collect theta; buyers pay it.

### Who Holds What: The Dealer/Client Divide

The options market is a zero-sum game between two sides:

**Non-dealer participants** — retail traders, hedge funds, portfolio managers, and institutional investors — are the *customers*. They buy options primarily to:
- Hedge existing equity exposure (buy puts to protect against drawdowns)
- Speculate on direction or volatility (buy calls or puts outright)
- Generate income (sell covered calls or cash-secured puts)

**Dealers** — market makers and bank trading desks — are the *intermediaries*. They take the other side of whatever customers do. They don't have a directional view; their job is to quote markets, fill orders, and hedge away the risk they accumulate. They are *reactive*, not predictive.

This means **the dealer's book is the mirror image of aggregate customer sentiment**:

| What customers are doing | What dealers end up holding | Dealer position delta | Dealer gamma |
|--------------------------|----------------------------|-----------------------|-------------|
| Buying puts (bearish hedging, fear) | Long puts | Negative (gains as market falls) | Positive → stabilizing |
| Selling puts (income generation, complacency) | Short puts | Positive (gains as market rises) | Negative → destabilizing |
| Buying calls (bullish speculation) | Long calls | Positive (gains as market rises) | Positive → stabilizing |
| Selling calls (covered call writing) | Short calls | Negative (gains as market falls) | Negative → destabilizing |

When the market is broadly fearful and buying puts, dealers accumulate net long gamma. When the market is complacent and selling options for income, dealers accumulate net short gamma. **Dealer gamma is therefore a direct readout of aggregate customer positioning and sentiment.**

### Dealer Gamma Sign and Hedging Behavior

**When dealers are net LONG gamma** (customers are net buyers of options — typically fearful or hedging):

Dealers are long puts (negative delta, positive gamma). As the stock falls, the delta on their long puts becomes more negative — they are getting shorter. To stay delta-neutral, they must *buy* stock. As the stock rises, delta becomes less negative — they are getting longer. They must *sell* stock. This is countercyclical:

- Stock falls → dealer buys → **stabilizing**
- Stock rises → dealer sells → **stabilizing**
- Sentiment context: customers are already hedged or defensive; the options market is pricing in risk

**When dealers are net SHORT gamma** (customers are net sellers of options — typically complacent or income-seeking):

Dealers are short puts (positive delta, negative gamma). As the stock falls, the delta on their short puts becomes more positive — they are getting longer. To stay delta-neutral, they must *sell* stock. As the stock rises, delta becomes less positive — they are getting shorter. They must *buy* stock. This is procyclical:

- Stock falls → dealer sells → **destabilizing**
- Stock rises → dealer buys → **destabilizing**
- Sentiment context: customers have been selling protection, assuming calm; the options market is underpricing risk

A **negative gamma regime** means dealers are net short gamma across the index — customers have collectively sold enough options that dealers are now on the long side of every position, forced to chase price rather than fade it. Every move forces them to add fuel to that move via hedging flows rather than absorbing it.

A **positive gamma regime** is the opposite: customers have bought enough options (hedges) that dealers are absorbing volatility. The market has a natural damping mechanism.

### Vanna Flows and the Vol-Price Feedback Loop

Vanna becomes important when implied volatility and price are moving simultaneously — which is the norm during selloffs. When IV spikes during a market decline:

- Puts' deltas become more negative (they're gaining intrinsic value *and* gaining sensitivity)
- Dealers who are short puts (net short gamma) must buy even more of the underlying to stay hedged
- This is the **vanna feedback loop**: falling prices → rising IV → larger delta on puts → more forced buying (or less selling) required

In a negative gamma + rising vanna environment, these two effects compound: the dealer is chasing price moves *and* simultaneously adjusting for vol moves. This is why stress events can produce nonlinear, seemingly disproportionate moves — it's not just sentiment, it's mechanical.

### Why Rising VIX/VIXEQ Deepens Negative Gamma

When more hedging flows concentrate in SPX options and customers are buying SPX puts, dealers are selling them — becoming *more* short gamma at the index level. The negative gamma condition deepens as the ratio rises. Simultaneously, vanna exposure increases because dealers are now short more puts that become more sensitive as IV rises alongside falling prices.

---

## Large Strike Open Interest: Gamma Pin Mechanics

### What is a Large Short Put Position at a Strike?

When a major market participant sells a large number of put options struck at a specific level (e.g., SPX 6475 expiring March 31), the dealer on the other side *bought* those puts — they are *long* the puts at 6475, meaning they are long gamma near that strike.

This is the opposite of the bearish hedging case. Here, the *customer* is the put seller — likely a fund or structured product desk generating income by selling downside protection. Their sentiment is complacent or neutral: they are betting the market won't fall to 6475. The *dealer* ends up long the put, which locally creates stabilizing (positive-gamma) behavior near that strike, even while the broader book may be net short gamma everywhere else. One large positioned seller can temporarily impart positive-gamma mechanics to a specific strike zone within an otherwise negative-gamma market.

### Support From Above: SPX Falling Toward the Strike

In this scenario the dealer is the **long put holder** (because the customer sold the put). The dealer's position delta is negative and becomes more negative as the stock falls — the dealer is getting shorter, so they must buy to stay neutral. This is the stabilizing, positive-gamma case.

As SPX falls from above toward 6475:

1. The dealer's long put delta becomes more negative (approaching −1 as the put moves toward ATM)
2. To stay delta-neutral, the dealer *buys* SPX futures/stock as the market falls toward 6475
3. This buying creates a mechanical support cushion
4. The closer to expiration, the larger the gamma (gamma peaks near ATM at expiration)
5. IV at nearby strikes may *compress* temporarily because dealers' mechanical buying absorbs selling pressure
6. The market experiences a "cushioned," slower decline near the pin

**From above, the 6475 strike acts like a floor with a speed bump — it slows the descent and may produce a bounce.**

### Resistance From Below: SPX Rallying Toward the Strike

If the market has already fallen through 6475 and is approaching from below:

1. The 6475 put is now in-the-money — dealers are short delta on their long put
2. As the market rallies toward 6475, their delta becomes less negative (they need to sell futures to stay neutral)
3. This selling pressure creates resistance at 6475 from below
4. The pin works in both directions — 6475 becomes resistance on the way up too

### Summary of Price and Vol Behavior Near the Strike

| Scenario | Direction | Vol Behavior | Price Behavior |
|----------|-----------|-------------|---------------|
| SPX above 6475, falling toward it | From above | IV may dampen slightly (mechanical buying absorbs selling) | Slower, cushioned decline |
| SPX at 6475 | At strike | Maximum gamma (peaks at ATM near expiry) | Choppy, high-frequency oscillation |
| SPX below 6475, rallying toward it | From below | IV stays elevated (put buyers still nervous) | Capped rally, mechanical resistance |
| SPX well below 6475 | Deep ITM put | Vol can spike violently | Accelerated downside, no more support |

---

## What Happens at Expiration

### The Pin Disappears

When the March 31 options expire, all gamma tied to the 6475 strike *evaporates overnight*. The mechanical hedging flows that were creating support and resistance are gone.

**Consequences:**
1. The "cushion" slowing the decline from above is removed — next support may be far lower
2. If SPX was being held near 6475 by gamma gravity, it may gap away from that level
3. Dealers no longer need to buy dips near 6475 → removal of support bid
4. The gamma regime can shift abruptly — the next large open interest strike (possibly much lower) becomes the new pin zone

### Vol Behavior After Expiration

- **Vol crush scenario**: If expiration passes without a breakdown, near-term IV often falls sharply (the theta event resolves, uncertainty dissipates)
- **Vol expansion scenario**: If the market was being artificially suppressed by pin dynamics and now breaks lower, realized volatility spikes and VIX jumps sharply
- The 0DTE gamma that was stabilizing intraday moves is reset — new strikes become relevant for the next expiration cycle

### The Vulnerability Window

The transition is dangerous when all of the following are simultaneously true:

1. Already in a negative gamma regime (fragile, procyclical hedging flows)
2. Temporarily supported by pin mechanics at a specific strike (artificial floor)
3. Rising VIX/VIXEQ and VIX/VOLI (growing index-level hedging demand)
4. Renewed bid for far-OTM puts (tail risk buying, skew steepening)

When the support strike expires and rolls off, the mechanical bid disappears, no new large near-term strike immediately replaces it, and dealers who were long gamma near that level suddenly have flat books. Any macro event or sentiment shift can now move the market more freely — and in a negative gamma environment, those moves will be amplified rather than absorbed.

---

## Far-OTM Put Bid and Skew

Far out-of-the-money puts are *tail hedges* — they only pay off in a crash scenario (e.g., SPX drops 10–20%+). They are expensive per unit of coverage, so buying them signals genuine fear of a non-linear downside scenario, not just a normal pullback hedge.

A renewed bid for far-OTM puts:
- Pushes the *skew* steeper (put skew = how much more expensive OTM puts are vs OTM calls)
- Signals large players are paying up for protection *past* the near-term pin
- Means the market is pricing in a scenario where the mechanical support *fails* post-expiration

---

## Synthesis: Reading the Full Signal

| Signal | What It Measures | Customer Sentiment Implication | Market Mechanics |
|--------|-----------------|-------------------------------|-----------------|
| VIX/VIXEQ rising | Index vol vs single-name vol | Institutional fear concentrated at index level; customers hedging portfolios, not single names | Correlation rising, diversification failing, hedging centralizing in SPX book |
| VIX/VOLI rising | SPX vol vs SPY ETF vol | Large players bypassing retail/intraday ETF layer; urgency of institutional hedging | Dealer SPX book absorbing size; less flexible than ETF market |
| Negative gamma regime | Dealer net gamma position (mirror of customer positioning) | Customers are net option *sellers* (complacent) or dealers absorbed heavy put-buying and are now short gamma | Every move amplified rather than absorbed; procyclical hedging flows |
| Positive gamma regime | Dealer net gamma position | Customers are net option *buyers* (fearful, defensive) | Every move dampened; dealers buy dips and sell rips naturally |
| Large OI at nearby strike (short put by customer) | Dealer is long the put (mirror of customer's short) | Customer sold puts for income/yield; dealer bought them and is now long gamma at that strike | Mechanical support from above, resistance from below — until expiration |
| Far-OTM put bid | Tail risk demand / skew | Customers paying up for crash protection; genuine fear of non-linear downside | Skew steepens; dealers short more OTM puts, deepening net short gamma further out |

When all five flash simultaneously, the market is walking on a floor that expires on a known date. The signals above that floor suggest the buyers holding it up are already paying for protection in case it gives way.
