# RW Pro Discord — #vol-book-club-chat digest, May 2026

- **Period:** May 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1387280068182540390
- **Raw transcript:** [rw-pro-vol-book-club-chat-raw-20260501-20260531.md](./rw-pro-vol-book-club-chat-raw-20260501-20260531.md)
- **Volume:** 129 messages — a much busier month than June (40 messages), dominated by two things: Euan fielding a steady stream of VRP-mechanics questions, and Ben running a genuinely substantial multi-week quantitative research project on the pre-earnings long-vol straddle trade.

---

## 1. VRP harvesting fundamentals: the wheel, covered calls, and "buying at a discount" framing

The month opened with shashinsho asking whether the "wheel strategy" (selling cash-secured puts, then covered calls if assigned, repeat) is a sound way to get long SPY exposure "at a cheaper price."

Euan's answer reframed the entire question, and is worth internalizing as a general principle:
- The wheel is nothing more than a covered call and a cash-secured put synthetically combined — they're the same position via put/call parity. Branding it as a distinct "strategy" mostly just doubles the ways to get it wrong.
- The actual edge is the variance risk premium (VRP), not "getting paid to wait" or "buying at a discount." Euan explicitly pushed back on both framings as the same category of wrong thinking as a covered call "giving income" — in every case it's just a long-delta position augmented with the variance premium, full stop.
- Practically: make sure the strikes you choose actually carry a variance premium (ATM captures it cleanly; far OTM puts still have some VRP but won't match the delta exposure of an ATM position).

This framing recurred throughout the month as the lens through which nearly every other VRP question got answered (see sections 2, 3, 7).

**Sentiment:** Foundational and slightly corrective — Euan is actively steering the group away from popular-but-imprecise framings (income, discounts) toward the more rigorous delta + VRP decomposition.

**Pull quotes:**
- Euan: *"the wheel is just a succession of covered calls (if you have the stock) and cash secured puts (if you don't) which are synthetically both the same... The extra edge in the idea is just the variance premium."*
- Euan: *"I'd push back a bit against the 'buying for a discount' thing. That is a similar wrong framing to a covered call 'giving income'. In both cases it is just a long delta position augmented with the variance premium."*

## 2. Where VRP is (and isn't) worth harvesting: commodities, gold, and stock selection heuristics

Two related threads, a few weeks apart, on where to actually deploy VRP-selling capital.

aditya asked about VRP trades in gold specifically. Euan's answer was a clear "smaller or skip it," for a well-reasoned informational-asymmetry reason: gold's VRP is statistically high and persistent, similar to indices, **but** commodities markets have genuine insiders (suppliers, industrial users, market makers with privileged flow) in a way equity indices largely don't — professional stock pickers don't reliably beat random, but professional commodity participants actually know things retail traders don't. Gold compounds this further by being an incoherent mix of industrial, jewelry/vanity, inflation-hedge, and risk-on demand depending on the day. His conclusion: stick to indices, where "nothing is knowable to anyone" — a genuinely level playing field.

Later in the month, Euan extended this into a concrete single-stock selection heuristic when the topic of individual-name vol-selling came up: favor "shitty companies" as short-vol candidates — high P/E, low return on assets, high leverage, high vol, high implied vol, high historical VRP, clear jump risk. He was careful to caveat this with the regime risk it carries: this heuristic would have hurt badly during the dotcom bubble, and "the MAG7 would have hurt recently" (i.e., high-multiple mega-caps have NOT behaved like the "shitty company" archetype despite superficially fitting a "richly valued" description) — a reminder that these are statistical tilts, not guarantees.

**Sentiment:** Pragmatic risk-scoping — Euan draws a clear line between markets with a level informational playing field (favorable for systematic VRP harvesting) and markets with structural information asymmetry (avoid or size down).

**Pull quotes:**
- Euan: *"in commodities most of the big participants know stuff. Suppliers and users are both informed... You, the retail traders, will always be totally ignorant... I stay away from commodities because I don't need the extra risk."*
- Euan: *"a useful rule of thumb is to sell vol on shitty companies: high PE, low return on assets, high leverage, high vol, high implied vol, high historical VRP, anything with clear jump risk. This would have been bad during the dotcom bubble and the MAG7 would have hurt recently, but it is generally the way to go."*

## 3. VIX options mechanics: European settlement, delta selection, and settlement risk

MidKnight flagged something that looked like a data error on the VIX option chain — with VIX at 17.4, he expected the 50-delta strike near that level, but IB showed the 50-delta put at 21.5. Euan's explanation is a genuinely useful mechanical point for anyone trading VIX options: because they're European-style, the true underlying is the **forward** value of the index, not spot — so when the futures curve is upward-sloping (as it typically is), the effective ATM strike sits meaningfully above the cash VIX print. He also relaxed the precision requirement: exact 50-delta isn't necessary, anywhere from 40–60 delta captures the variance premium adequately.

This opened into a deeper settlement-risk discussion:
- **Edux** asked whether Euan closes VIX positions before expiration specifically to avoid Special Opening Quotation (SOQ) risk, and raised the documented history of traders placing orders in OTM SPX options right before settlement specifically to manipulate the SOQ print (which drew SEC/CFTC scrutiny).
- **Euan's answer was unusually candid about market structure**: settlement manipulation genuinely happens, and it's not fringe behavior — "a strategy the big firms do, not just a rogue trader or two." He noted the practice is less blatant than 4-5 years ago purely because of negative press, not because the underlying incentive or mechanism was fixed — "it would be easy to fix the process so it couldn't happen but why would you offend your biggest customers?"
- On his own practice: he holds VIX option exposure between roughly 2 weeks and 2 months, not on a strict system but based on how closely he can pay attention — shorter-dated has more edge but proportionally more variance and rebalancing burden.

**Sentiment:** Candid and slightly cynical about market structure, but practically actionable — clear guidance on both the mechanical (forward-based strikes) and structural (settlement risk, tenor selection) dimensions of trading VIX options.

**Pull quotes:**
- Euan: *"Because they are European options, the true underlying is the forward value of the index. So the atm strike will currently be above the cash index because the futures curve is going up."*
- Euan: *"Manipulation of the settlement def happens. It is a strategy the big firms do, not just a rogue trader or two... It would be easy to fix the process so it couldn't happen but why would you offend your biggest customers?"*

## 4. Short-vol-around-macro-events: early testing and holding-period guidance

The precursor to what became a much bigger thread in June (see June's digest, sections 2–3). Sam asked the practical execution question directly: when shorting VIX futures ahead of NFP, should the trade be closed immediately after the release, or held longer since VIX futures often keep drifting down post-print? Euan's answer: give it time — he typically holds 15–30 minutes post-release rather than exiting immediately.

Jack asked whether anyone had real performance stats on this class of trade. Euan supplied a genuinely useful, appropriately-hedged answer from his own testing: selling 1DTE options overnight ahead of these numbers was positive but underwhelming — his conclusion was that the effect is real, but mostly just a modest boost on top of the baseline edge from unconditionally selling overnight vol (which is itself profitable but "nothing exciting"), rather than a standout standalone strategy. He explicitly noted he hadn't tested this specifically on VIX.

He also added useful macro context that ties directly into this month's later Fed-related content: the "important" economic number that moves markets **changes across regimes** — money supply in the early 90s, then NFP (a genuinely massive effect for a long stretch), and now inflation prints dominate. This is a useful caution against assuming today's highest-signal release will remain the highest-signal release indefinitely.

**Sentiment:** Grounded, appropriately modest — Euan's own results describe a real but small edge, not a standout trade, which is a useful expectation-setting data point ahead of June's much livelier real-time test of a closely related FOMC trade.

**Pull quotes:**
- Euan: *"I tested selling 1DTE overnight before these numbers and the results were positive but underwhelming... the effect is real but probably not huge."*
- Euan: *"it is worth noting that the 'important' number changes over time. in the early 90s it was money supply. then NFP (which was a massive effect) and now it is all about inflation."*

## 5. Ben's pre-earnings long-vol straddle research project (the month's biggest thread)

Spanning May 13–24, this was the most substantial original research produced in the channel all month — a genuine multi-iteration quantitative project, not a one-off post.

- **Sizing groundwork (May 13).** Yan asked Euan for a rough annualized-vol estimate for a typical pre-earnings long-vol book. Sam worked through an explicit back-of-envelope calc using the "Volatility Trading" textbook formula (equation 7.10): for a 50%-vol pre-earnings stock, ~1-week option duration, 20 concurrent positions, $100 average stock price → ~$5.50 straddle price, ~$110 portfolio notional, and a position-level volatility of roughly $22/day assuming uncorrelated positions. Euan's honest response: this really calls for a Monte Carlo rather than a closed-form estimate, since the question depends on exactly what you want to know.
- **First pass (May 18, weekly options).** Ben shared a full ORATS-based backtest (July 2015–May 2026) of the long straddle trade entered 10 or 15 trading days before earnings. Key findings: a clear IV ramp into earnings in both scenarios; VRP-at-entry was **not** predictive of which straddles perform better; IV decile showed no clean filtering pattern either; higher-priced stocks and (weakly) the bottom price decile looked more favorable; market cap alone showed no clear pattern. He shared explicit cost assumptions ($0.65/contract, $0.005/share, 5bps hedge slippage, and multiple spread-friction scenarios from 0% to 4% half-spread) and flagged uncertainty about whether those spread assumptions were realistic, having personally hit an 8% spread trying to close a position.
- **robotkris and Euan on expected quality.** Asked for a gut-feel Sharpe on the strategy, robotkris estimated **0.5–0.8 depending on scope** — and stressed that even at the low end this is valuable specifically because it's (1) positive-EV long-vol exposure and (2) largely uncorrelated with the rest of a typical portfolio. Euan added an important statistical caveat: Sharpe ratios on long-vol strategies tend to understate the "in a good way" — the payoff has significant positive skew, so a Sharpe-based comparison against normally-distributed strategies is somewhat misleading in the strategy's favor.
- **Monthly-options extension (May 19).** Ben reran the same analysis on monthly rather than weekly options. The IV ramp persisted but was less pronounced. More interestingly, the **lower implied-move decile earned dramatically more than the highest decile — 7.8% mean return vs. 0.7%, an 11× spread** — i.e., stocks where the options market wasn't pricing in much of a move going into earnings were the better long-vol candidates, not the ones with the largest priced-in moves. Higher market cap also correlated with better returns (plus tighter spreads as a side benefit).
- **The hedging mechanism debate.** Ben noted hedged variations underperformed on monthlies specifically, and ran the question past Claude before posting it to the channel. **Euan's correction is the most technically important single message of the thread**: Claude had the *mechanism* right but the *cause* wrong — monthlies do have less theta, but theta isn't actually where the edge comes from. The edge lives in vol mispricing, which gets realized daily via theta exceeding the gamma P&L; monthly options simply have less exposure to that daily-realized vol edge because they're further from the earnings-vol mispricing event. This is a subtle but important distinction between "the option Greek that changes" and "the actual source of the return."
- **Deeper filtering pass (May 24).** After finding and fixing a data-quality bug (corrupted stock splits in FMP data inflating market-cap and implied-move readings — switched to Norgate), Ben re-confirmed the core finding held: delta-hedged beats unhedged. His best-performing configuration was **entering the monthly contract 10 trading days before announcement, delta-hedged at 0.35** ("2M-H-0.35"). Drawdown analysis showed a pattern: the worst drawdowns clustered around broader market stress events (e.g., the tariff shock) where IV was already elevated at entry — leading him to propose a new filter (skip trades where entry IV exceeds the 90th percentile of that symbol's own historical IV distribution), though he noted this filter didn't show clean improvement with the data volume he had at the time.

**Sentiment:** This is the channel operating at its research best — a member running a genuine, iterative, cost-aware, bug-caught-and-fixed quantitative study, with robotkris and Euan providing calibration checks (expected Sharpe range, skew caveat) and a key mechanistic correction along the way.

**Pull quotes:**
- Euan: *"I think claude is right about the option mechanism but wrong about the cause... theta isn't the edge. the edge is in the vol mispricing which is realized daily by theta being bigger than the gamma PL. and monthlies just have less exposure to the vol edge which is caused by the earnings vol being mispriced."*
- robotkris: *"gut feel it would go at about 0.5-0.8 depending on how broadly you could do it. But that's a very useful 0.5-0.8 because (1) it gets you positive EV long vol exposure, and (2) it will be uncorrelated with most everything else."*
- Ben: *"Decile 1 (lowest IM) earns 7.8% mean vs Decile 10 earns 0.7% — an 11× spread."*

## 6. Restriking and delta management for the earnings straddle/strangle

A follow-on practical thread once Ben's research established the strategy's shape. Sam asked how to handle position sizing when a straddle premium feels uncomfortably large — Euan's answer: switch to a strangle, which preserves the same vega exposure and average profit per unit of vega, at the cost of a lower win rate (a genuine risk/reward tradeoff, not a free lunch).

On restriking mechanics specifically, Euan clarified the reasoning behind his "35-delta" restrike rule mentioned in an earlier webinar: it's the point where the original 50-delta legs have moved meaningfully out of range (into the low-30s/high-60s delta territory), at which point restriking a 10-delta strangle more frequently becomes worthwhile — with the caution "don't go crazy" about over-restriking. When Marco asked how close to earnings it's still worth restriking, Euan's answer reframed the question again in his preferred terms: he doesn't think about it as a days-to-earnings cutoff at all, just as maintaining vega exposure while limiting delta exposure, with the price-move threshold that triggers restriking naturally varying as the event approaches.

**Sentiment:** Practical mechanics, consistent with Euan's overall philosophy (section 1) of keeping the framing anchored to vega/delta rather than calendar-time or "rules of thumb" that don't generalize.

**Pull quotes:**
- Euan: *"A strangle will give exposure to the thing you want. The win rate will be lower but the average profit (per unit of Vega) should be the same"*
- Euan: *"i always just try to have vega exposure and limited delta exposure. the price moves that cause re-striking will vary as we get closer to the event, but my aim is still the same"*

## 7. VRP harvesting mechanics, precisely: vega, gamma, and calendar spreads

Rob asked a long, careful, well-researched question directly citing Euan's own book (*Option Trading*, pages 90–91) — pointing out an apparent tension between two statements: that harvesting VRP requires being "short gamma" (per the book) versus always wanting vega exposure and restriking to maintain it (per the book club discussions). Isn't short vega actually a bet on *implied* vol falling, distinct from harvesting the realized-vs-implied spread?

Euan's answer is the clearest single technical explanation of VRP mechanics in the month's transcript: **every option has vega and gamma of the same sign**, so for any simple single-leg or straddle/strangle position, being short vega necessarily means being short gamma too — they can't be decoupled in a simple position. Compound structures (calendars, skew trades) *can* locally decouple them, but even then, whichever part of the vol surface you're short-vega on is the part actually collecting the VRP. His concrete example: long a short-dated straddle + short a long-dated straddle nets you long gamma / short vega overall — but the VRP is being collected specifically in the long-tenor leg, while it's simultaneously being *paid away* in the short-tenor leg. This resolves the apparent contradiction Rob identified: there's no tension, just two properties of the same short-vega exposure that happen to move together in simple positions and can be examined separately in compound ones.

**Sentiment:** A genuinely clarifying, textbook-quality explanation — the kind of answer that resolves real confusion rather than restating the question in different words.

**Pull quotes:**
- Euan: *"Every option has vega and gamma of the same sign, so for a single option or straddle or strangle, whenever you are short vega you will also be short gamma... if you are long a short dated straddle and short a long dated straddle you will be long gamma and short vega. But you will only be collecting VRP in the long tenor. You will be paying the VRP in the short tenor."*

## 8. Portfolio construction: rebalancing cadence and capital allocation for VRP strategies

akhan asked three follow-up questions after a portfolio-construction session: how often to reassess portfolio weights, what to do if realized volatility undershoots the target (10% actual vs. 20% expected after 3 months — increase leverage, or wait?), and how to think about capital allocation for VRP strategies that consume margin rather than actual capital.

Euan's answer, consistent with his generally low-friction, non-dogmatic style seen elsewhere this month: rebalance no more than quarterly unless something material changes (a component gets delisted, a venue gets hacked, or the strategy itself gets abandoned) — the same logic applies to re-leveraging decisions, not just weight rebalancing. On capital allocation for margin-based strategies specifically, his answer was refreshingly unconcerned with precision: he doesn't track capital basis at all, just allocates by the proportion of total P&L he wants each strategy contributing — e.g., sizing stat arb up until it's expected to deliver ~40% of total P&L — which he calls the practical advantage of a "vibes"-based allocation approach that works even when the underlying capital basis differs across strategies.

**Sentiment:** Pragmatic and deliberately anti-precision — a useful counterpoint for anyone over-engineering rebalancing rules or capital-allocation formulas.

**Pull quotes:**
- Euan: *"You won't find much benefit in doing this more than quarterly. UNLESS something materially changes... I rebalance once a quarter or whenever I change a model. No need to be dogmatic."*
- Euan: *"I don't worry about capital at all. i just allocate to get the proportion of pl per strategy where I want it... this is one of the great advantages of the 'vibes' approach. you can allocate on 'goodness' even if the capital basis is different."*

## 9. PEAD candidates and live earnings-season trade results

Closing out the month, a live, informal thread on post-earnings-announcement-drift (PEAD) trading and how the earnings-vol season was actually going for members running it live:
- hast reported a real loss on SNOW — a pre-profit, hypergrowth, high-short-interest name with a large earnings surprise that hurt the short-vega leg of his long-vol-into-earnings/short-vol-through-earnings trade — and asked whether requiring a positive P/E might be a useful filter to avoid this profile of stock going forward.
- **Euan's response is a notably humble and useful piece of guidance**: he's already tested essentially every "good stock / bad stock" categorization scheme he could think of for this exact purpose and never found one that reliably worked, despite genuinely trying. His practical advice instead: trade as many names as possible with equal dollar premium per position, and let the law of large numbers do the filtering work that a stock-characteristic filter can't reliably do.
- FullMetal37! and nxtrador shared real-time, mixed live results — FullMetal37! roughly flat on the season overall but negative specifically on DELL; nxtrador's dry joke about being assigned DELL ("Dude you're getting a DELL") got a laugh. Sam and Ben separately floated SNOW and DELL as PEAD candidates for their own models, with Sam noting SNOW's options "don't extend up enough" to make the PEAD trade work well.
- Euan closed the month with a one-line theoretical note that PEAD is likely best understood as "a pure delta one effect" rather than genuine vol mispricing — i.e., he's not aware of research showing options are actually cheap or mispriced around the drift, which tempers how much of an *options-specific* edge (versus a plain directional-stock edge) PEAD trading around earnings surprises really offers.

**Sentiment:** Realistic and appropriately humbling — a good counterweight to section 5's successful research thread, showing that even a well-understood strategy (long vol into earnings) produces real, sometimes large individual losses (SNOW), and that the intuitive fix (filter by company quality) has already been tried by the group's most experienced member without success.

**Pull quotes:**
- Euan: *"I've tested almost everything I could think of to find 'good' and 'bad' stocks and really never came up with anything... My advice would be just to do as many as possible and equal dollar premium. That way the law of large numbers will help."*
- Euan: *"I think it is a pure delta one effect. I don't know of any studies that show vol is cheap or options being underpriced."*

---

## Overall read

May was #vol-book-club-chat's most substantive month of the two covered so far (129 messages vs. June's 40), and the standout contribution is **Ben's multi-week pre-earnings long-vol straddle research project (section 5)** — a genuine iterative quant study complete with a caught-and-fixed data bug, cost modeling, and a decile-based finding (lower implied-move stocks outperforming higher implied-move stocks 11×) that's directly actionable for anyone running this trade.

1. **Euan's mechanistic correction of Ben's Claude-assisted theta/vega analysis (section 5) is the single most technically valuable exchange of the month** — a reminder that even a well-informed AI-assisted analysis can get the *mechanism* right while getting the *causal story* wrong, and that this distinction matters for how a strategy should be adapted going forward.
2. **VRP harvesting has a consistent theoretical throughline across nearly every thread this month**: it's fundamentally a short-vega (and, in simple positions, necessarily short-gamma) exposure, not "income" or "buying at a discount" — Euan restated and refined this framing in sections 1, 6, and 7 in response to different member questions, suggesting it's the single most important mental model this channel keeps returning to.
3. **The "filter for good/bad stocks" instinct (section 9) has already been thoroughly tried by Euan and found not to work** — worth remembering before any member proposes a new stock-quality filter for the earnings-vol trade; the more promising filtering signal so far is Ben's implied-move decile finding (section 5), not fundamental quality screens.
4. **VIX and event-driven vol trades (sections 3–4) both carry real structural/settlement risks worth respecting** — European-style forward-based strikes, documented SOQ manipulation by large players, and only a modest (not standout) edge from short-vol-around-macro-events per Euan's own backtesting — useful context heading into June's live FOMC trade test (see June's digest).
