# RW Pro Discord — #tradfi-trading digest, March 2026

- **Period:** March 1–31, 2026 (channel was quiet March 1; content begins March 2)
- **Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
- **Raw transcript:** [rw-pro-tradfi-trading-raw-20260302-20260331.md](./rw-pro-tradfi-trading-raw-20260302-20260331.md)
- **Volume:** 378 messages — the busiest month in this digest series so far. The backdrop was an active Middle East war that kept crude, VIX and IV structurally elevated all month, against which robotkris and Euan ran a sustained multi-week research program (Treasury and commodity carry, UVXY-VXZ hedge mechanics) while the community traded earnings-season short-vol, debated multi-strategy portfolio construction, and worked through a long discretionary-vs-systematic trading exchange late in the month.

---

## 1. Middle East war jolts energy markets and keeps vol structurally bid

Early March opened with a large IG weekend gap (crude futures indicated +15% before Globex, settling to roughly +8% by the open) that traders spent the morning sanity-checking against actual futures prices.

- Dan and Rachit compared IG's indicative +15% number against the actual April CL open (~75, versus an IG "high" near 77) — concluding IG's weekend quote overstated the real gap, a recurring gap-quality lesson.
- The conflict widened beyond crude: Dutch TTF natural gas — normally uncorrelated with US NG — moved in sympathy, which Dan flagged as a specific risk for anyone short TTF given its known "widowmaker" reputation and 5-contract minimum size.
- By evening, Dan warned the situation "is accelerating" with European electricity bills likely to spike as a result.
- The elevated-vol backdrop persisted for weeks: by March 7, Rachit and 4D were sizing options trades against IV levels described as **"highest its been in 6y,"** with 4D pricing crude IV around 110% (vs. ~50% pre-war) and the term structure in clear backwardation.

**Sentiment:** A live geopolitical shock working through markets in real time, with the group doing useful due-diligence on which "shock" numbers (IG indicative quotes vs. actual futures prints) were reliable — and a vol regime that stayed elevated long enough to reshape several other threads this month (see #2 and #4 below).

**Pull quotes:**
- Dan: *"All eyes on oil but I had no idea Dutch Nat Gas could be affected, usually NG and TTF is uncorrelated. Glad I'm not short this time, TTF is known to be a widowmaker just as bad as NG."*
- 4D: *"imo, the term structure is clearly in backwardation and iv is around 110%, whereas it was around 50% before the war, I think it is high."*

## 2. Earnings-season short-vol trading: stats, live results, and open questions on execution

The month's most heavily-traded live edge: shorting options around earnings announcements.

- **Euan supplied the deepest quantitative grounding**, sharing stats on always-selling a 15-delta strangle (avg 6.4c edge, 85% win rate, worse in high-VIX/VVIX regimes) versus always-buying a straddle (average loss of 13c, 38% win rate) — concluding the ATM strikes are cheapest and the far-OTM puts most overpriced. He was candid about the gap in his own understanding: *"What I have no clue about is intraday management. take profits? stop losses? exit at a certain time etc."*
- 4D was running the trade live and reported concrete numbers: ~60 trades so far this earnings season, an in-progress Sharpe estimate of 13 with VIX>20, closing shorts "right after the market opens" rather than holding.
- MidKnight independently built a similar scanning approach — cross-sectional VRP screening via the Moontower real-vol display, entering near the close on earnings day and exiting the next close.
- **mm** joined the thread having run his first earnings season with the trade, noting he'd been taking both sides rather than 4D's short-only approach.
- SNP asked the group detailed implementation questions (stock selection for smaller accounts, bid-ask spread impact); 4D's answer — closing the underlying position upfront near |delta|>0.9 to avoid post-earnings-drift (PEAD) risk — drew a strong response from SNP ("That is really smart").
- **Euan supplied the key caveat that tempers the whole trade**: post-earnings, options were fairly priced in his own study, so the edge is earnings-day only — "after the market opens, the edge is gone" (as 4D paraphrased it) — meaning PEAD, if traded, needs to be treated as a fully separate, longer-horizon, delta-one strategy, not bundled with the vol trade.
- A cost-sensitivity check from blue664203 (testing on SPX to simplify close/expiration mechanics) found transaction fees eating into "a huge part of the edge."

**Sentiment:** A genuinely live, actively-traded seasonal edge with real position counts and Sharpe estimates being shared in real time — but Euan's fair-pricing finding is the load-bearing caveat: the edge window is narrow and doesn't extend past the open.

**Pull quotes:**
- Euan: *"If you always sell a 15-delta strangle, you make an average of 6.4 cents with a win rate of 85%... If you always buy a straddle, you lose an average of 13 cents with a win rate of 38%."*
- Euan: *"I did a study and post earnings the options were fairly priced. So I'd get out ASAP. [PEAD] will operate on a longer time scale and will be only delta one. I'd keep that separate."*
- 4D: *"it might be another best earning trading season, vix > 20, sharpe = 13 for now"*

## 3. robotkris and Euan's futures carry research program: Treasuries and oil

**robotkris ran the month's most substantial original-research thread**, posted as an explicit "Quick research update":

- Built a 30-day constant-maturity series for ZF and ZN to measure local curve slope without quarterly-roll noise, generating a carry signal from the 30-day-vs-29-day synthetic price difference — used to time a belly-vs-bond spread trade (short ZN / long ZB or UB).
- He was upfront that DV01-based hedging (vs. a simple regression hedge) improved the spread's behavior, but flagged the DV01 approach wasn't done carefully and could be refined further using FRED data.
- Extended the same idea to commodities: a short-front/long-third-month CL calendar spread, which he described as "obviously mean reverting, but very extreme" — profitable trading pure mean reversion on a one-day lag with no costs applied, but explicitly framed as early-stage ("Don't go trading this or anything").
- **William pushed back constructively**, noting the bond carry spread looked flat for a full decade — **robotkris's response reframed the finding rather than defending it**: normal variance for a single-effect spread, but the carry signal itself suggested flipping or flattening the trade for chunks of that decade, meaning a *better* carry signal (not the base spread) is likely where the real improvement lives. He and MidKnight also floated extending the idea cross-sectionally to a basket of G7 bonds.
- **Euan, working the same problem independently**, said he couldn't verify a specific chart reference from "Andrew's book" but was "going back to the idea with a clean sheet of paper approach" to see if he could beat the unconditional carry rules — a signal that this is an active, multi-person research line rather than a single finished result.
- Dan added a parallel, related idea: a symmetric absolute (not spread) carry measure applied to ICE Brent, and raised Corey Hoffstein's point that a long/short carry trade is arguably closer to mean-reversion than "carry" in the traditional sense.
- The thread connected to a second later find: bil mor surfaced an external basis-momentum paper that looked consistent with robotkris's CL first-vs-third-month finding, which robotkris flagged for further exploration, and mm separately noted he'd already planned to look into the same underlying paper that weekend.

**Sentiment:** The most rigorous, multi-week collaborative research thread of the month — robotkris driving concrete signal-construction work, Euan running an independent parallel check, and the group (William, MidKnight, Dan) contributing real pushback and extensions rather than just reactions.

**Pull quotes:**
- robotkris: *"Timely reminder that oil is one wild beast. Looking at commodity carry, this is a simple short front, long third month CL spread... it's obviously mean reverting, but very extreme."*
- robotkris: *"That said, the carry signal suggested flipping the spread or at least flattening for chunks of the last decade. There's almost certainly a better carry signal that could potentially flip the sign of the spread more effectively."*
- Euan: *"I'm going back to the idea with a clean sheet of paper approach just to see if I can find something better than unconditional rules."*

## 4. The UVXY-VXZ complex: borrow risk, term structure, and robotkris's ongoing hedge research

The month's longest-running single-strategy thread, touching operational risk, market structure, and an active model-improvement effort.

- **Operational risk surfaced early**: Dan had UVXY bought-in by IBKR mid-session on March 10 due to a short-borrow shortfall — distinct from a normal share recall, per IBKR's notice. He described the net effect (missing out on gains he'd have captured via VXX/VIXY instead) and said he'd change ETFs mainly to avoid the manual-correction hassle, not for the P&L hit. Multiple members (Sam, danielscapital) reported the same UVXY unavailability-to-borrow issue recurring several times a year, with **robotkris offering the practical workaround**: VIXY at 1.5x the dollar amount of UVXY replicates the calendar-spread effect (losing only the leverage-decay benefit).
- **MidKnight connected robotkris's live UVXY webinar to a VX futures-calendar insight**: the VX1-VX2 vs VX3-VX4 carry/tail-risk breakdown clarified why the constant-maturity hedge is still only a partial one. **robotkris validated the intuition directly**: "the 30day-ish region was the most crowded part of the trade," and floated that a "shock hedge" could in principle be derived for any two points on the curve, though not with precision.
- Dan pushed on hedge-ratio mechanics further (whether a sub-VX30 constant maturity is even achievable, given the front month starts at 30 DTE) and proposed keeping VXZ for the back-end hedge while replacing the front leg with outright futures — trading simplicity against added margin intensity (FullMetal37! flagged the offset loss vs. a pure-futures structure).
- **robotkris connected the whole trade family explicitly when AlanRE asked how to weigh UVXY-VXZ against the separately-run VIX basis trade**: both harvest overlapping vol-term-structure edges (UVXY-VXZ shorts front-curve vol hedged by back-curve vol; VIX basis predicts the *sign* of the VRP via a dynamic model) — meaning they'll be highly correlated in practice even though they're constructed differently. Ben reported running both at a modest 5% allocation each as a practical answer to the correlation question.
- **robotkris shipped a concrete model update**: the UVXY-VXZ simulation was rebuilt with a vix-aware hedge ratio (varying with VIX level rather than fixed), reporting the same trade-buffer setting remains optimal for IBKR's high-fee tier, and that after-cost Sharpe improved about 10% with the new hedge. He also published reusable tools (an R function and a matching Pine Script) so members can compute their own live hedge ratio.

**Sentiment:** A model genuinely being improved in public — from an operational near-miss (forced buy-in) through a mechanistic insight (VX calendar crowding) to a shipped, better-performing hedge — with robotkris driving each step and taking member questions (MidKnight, AlanRE, TheOriginal101) as prompts for further refinement rather than one-off answers.

**Pull quotes:**
- robotkris: *"In a pinch, you could use VIXY instead (1.5x the dollar amount of UVXY). You lose the leverage decay effect, but you'll get the same calendar spread effect."*
- robotkris: *"Mate I reckon you are on to something here... at least when we did that analysis, it seemed that the 30day-ish region was the most crowded part of the trade."*
- robotkris: *"I've updated the UVXY-VXZ simulation to include the vix-aware hedge we built last week... the after-cost Sharpe is about 10% higher using this vix-aware hedge."*

## 5. Market data costs, redistribution licensing, and a possible RW-wide data-sharing idea

A practical infrastructure thread sparked by a casual "what data do you use" question.

- Members compared notes across providers: CQG (MidKnight, for intraday tick data, cheaper now that brokers resell it), Norgate and Data Bento (robotkris — Data Bento praised as "a pleasure to work with" but pricier), CSI (Dan, for global breadth and roll-schedule customization), and Polygon/Massive (mm — fast, no rate limits, good delisted-ticker coverage, but recommends Sharadar/Quandl instead for historical equities).
- **robotkris surfaced the real structural cost driver**: it's not the data itself but exchange-set redistribution licenses — e.g. roughly $3k/month for CME alone — that make sharing a subscription across a VM genuinely expensive, with the exchanges (not the data provider) setting the price.
- This led robotkris to float a bigger idea directly to the group: *"if RW purchased the data under a redistribution license and shared the cost with members, it would work out much cheaper than everyone buying their own subscription. Current RW pricing doesn't support that for everything, and the user base's data needs may be too fragmented to make the economy of scale thing work. But it would be good to explore it at some pont."*
- MidKnight's half-joking "may as well get a Bloomberg terminal" suggestion turned into a real thread: robotkris confirmed a shared VM-hosted terminal login is plausible and likely within terms of service, and akhan separately clarified Bloomberg's actual licensing restriction (physical terminals can be shared within one org; VM/web logins can't).

**Sentiment:** Useful, concrete vendor comparison plus a genuinely proposed (if not yet committed) idea from robotkris for RW to pool data costs — worth tracking if it resurfaces as an actual initiative.

**Pull quotes:**
- robotkris: *"It's the redistribution licensing that gets expensive. It adds up to thousands per month. We should have a conversation about data at some point... it would be good to explore it at some pont."*
- robotkris: *"That's in addition to the data charges - there are monthly redistribution licenses that, as I understand it, are set by the exchanges rather than the data provider. eg CME alone is something like $3k/month."*

## 6. Community contribution: a portfolio-level stress-test tool

blue664203 (Discord tag KONG) shared a self-built risk management tool for stock & options portfolios, motivated directly by a gap Euan had raised in the vol book club: most risk simulation tools are built for single option positions and don't handle portfolio-level effects (positions moving in different directions and magnitudes under the same shock). The tool answers "what happens to my portfolio if SPY drops X% and VIX spikes Y%" and quantifies hedge effectiveness.

**robotkris responded with a specific improvement suggestion** rather than just praise: let users flex the beta assumption (e.g., push beta toward 1) to model correlations spiking as stocks crash — a scenario the default tool likely understates. MidKnight and TimExcellent both thanked the builder for the community spirit, with TimExcellent noting the practical alternative (booking time on a shared community terminal) would be far more cumbersome.

**Sentiment:** Genuine community reciprocity — a member built something in direct response to another member's (Euan's) stated gap, and got an actionable improvement idea back from robotkris rather than just thanks.

**Pull quote:**
- robotkris: *"One thing that would be cool is to be able to flex the beta assumptions - eg push beta towards 1 to see what might happen if correlations increase as stonks crash."*

## 7. SEC weighs scrapping the quarterly earnings report requirement

4D shared a WSJ report that the SEC is preparing a proposal letting companies report results twice a year instead of quarterly. Reaction split two ways:

- MidKnight and Rachit reacted with straightforward concern/resignation about losing "earning trading seasons" (the exact edge several members were actively trading — see #2 above).
- **-k offered the more interesting reframe**: rather than pure downside, this creates a *new* source of equities alpha — a company's choice to report quarterly (or to suddenly stop) would likely itself be predictive of forward returns, and cited an academic reference on forecasting earnings from alternative data as a related, if riskier, angle to consider.

**Sentiment:** Still a proposal, not a rule change, but worth flagging given how directly it threatens the group's most-traded live edge — and -k's alpha-in-the-disclosure-choice idea is a genuinely novel angle if it does go through.

**Pull quotes:**
- -k: *"on the bright side, there might be quite a bit of equities alpha in this! whether a company chooses to report quarterly earnings in general, or if they suddenly choose to not report one quarter, etc. would likely be predictive of forward returns."*
- 4D: *"maybe we don't have many earning trading seasons left...."*

## 8. Options-expiry mechanics: dealer gamma, the JPM collar, and VRP timing

Sam asked about the "biggest options expiry ever" chatter and whether dealer delta-buying created a tradeable pattern into the close.

- **Euan gave the grounded answer, pushing back on the popular narrative**: dealer-gamma stories have *some* truth but usually get overstated in importance — pre-2021 there was a real pattern of futures rallying overnight into AM expiration then reverting intraday, but it hasn't persisted since. He linked a more current paper on expiration effects as the better reference going forward.
- IrishJohnnie added the concrete calendar detail: that day combined the JPM collar roll and the QYLD roll (~2pm ET), with dealers trying to stay delta-neutral against parties actively front-running the flow — later correcting himself on the exact date (QOPEX + QYLD roll that day; the JPM collar itself lands March 31).
- **Euan's most generalizable point came a few days later**, explaining *why* VRP is realized specifically around monthly expiries: whichever month is currently expiring gets "used up," making the next month relatively rich — a structural, not one-off, effect that generalizes to any market with a known VRP.

**Sentiment:** A useful corrective on a popular-but-overstated market-structure narrative (dealer gamma), with Euan supplying the more durable structural insight (VRP concentration around expiries) that outlasts the specific expiry-day discussion.

**Pull quotes:**
- Euan: *"There is always some truth behind these dealer gamma ideas, but they usually overstate the importance. Up until about 2021, there was a pattern where futures would rally overnight into the AM expiration, then revert intraday. But it hasn't been there since."*
- Euan: *"the effect is that all of the VRP is realized around monthly expiries. So when march is expiring, april would be too expensive."*

## 9. Multi-strategy portfolio construction: accounts, signal netting, and live performance

A rich thread on the operational mechanics of running many strategies at once.

- Quarry614 explained IBKR's sub-account structure (one login, per-strategy accounts, no cross-margining between them) — a tradeoff William and Dan both probed, with **Dan making the case for merging into one portfolio** (net positions, shared margin, automatic daily rebalancing) against Quarry614's preference for simplicity via separation, especially past ~20 strategies.
- **Dan's own numbers anchored the thread**: 35 strategies, live Sharpe "about 2.7," managed via signal netting across ~120 markets — deliberately not fully optimizing strategy weights (giving extra room to capital-hungry strategies like futures trend-following) because marginal portfolio-Sharpe gains have flattened out, which he said was itself part of why he joined RW Pro.
- **llIHeroic supplied the important caveat on that Sharpe number**: at 2.7, if it's inclusive of tail risk, further gains become mostly a matter of levering up the portfolio and compounding into a capacity ceiling — not a free lunch.
- A parallel sub-thread (akhan, Dan, deal_me_in) worked through the mechanics of tracking strategy-level performance while netting positions at the broker: **Dan's rule of thumb — track strategies individually using EOD closes outside the broker; the broker-level net position is purely an execution detail and doesn't need to match strategy-level bookkeeping.** deal_me_in described his own solution in detail: nine real accounts (plus three paper), tracking *returns* rather than dollars at the strategy level, computed 10 minutes before close daily regardless of whether he trades that day — an approach he said took him "a long time to come up with... so elegantly simple."

**Sentiment:** A genuinely practical, experience-grounded exchange with real numbers on the table (35 strategies, Sharpe 2.7, nine accounts) — useful as a reference thread for anyone scaling past a handful of strategies.

**Pull quotes:**
- Dan: *"I've got 35 strategies, but now shave my head so I don't have that hair pulling issue anymore. Actually pretty easy to manage now, only problem is when I make changes and introduce a bug to the system."*
- llIHeroic: *"if sharpe is inclusive of tail risk then past a certain point it's just a matter of getting the portfolio vol up and coumpounding into the capacity ceiling"*
- deal_me_in: *"It took me a long time to come up with something so elegantly simple. I hope it works for you."*

## 10. Discretionary-to-systematic trading: order flow, footprint charts, and why the transition is hard

The month's longest single-day exchange, sparked by FullMetal37! asking MidKnight to explain his discretionary futures day-trading approach.

- **MidKnight described a market-profile-adjacent, purely intraday approach**: heavy scalping in the first 30 minutes when volatility is high, transitioning out as the opening "fight" resolves; fading light prints (works better in thinner markets like the Hang Seng than thicker ones); leaning on footprint charts and the DOM rather than a fixed rule like pure orderbook-imbalance fading.
- **mm, who made the reverse journey (discretionary crypto scalping to full systematic), gave the most detailed account of *why* he switched**: he used a delta footprint chart to spot buy/sell-taker imbalance at levels of interest (daily/weekly/monthly/quarterly/yearly VWAPs), looking for a down-candle-at-highs ("P shape") or up-candle-at-lows ("b shape") pattern to fade for a quick scalp — framed honestly as "trading off of 'trapped traders' buying a breakout which worked well in crypto, but maybe i just needed something to justify my trades." The actual reason he moved on: "eventually realized my systematic stuff in aggregate outperformed me sitting in front of a footprint chart for 8 hours a day scalping asia session shitcoins."
- MidKnight asked directly whether the transition was hard to accept; **mm's answer reframed the whole debate in economic rather than ideological terms**: "at the end of the day we're all trying to get paid in some way. if you're consistently doing well manually then that's just where you perform best for the time being" — and that withdrawing living expenses constantly creates a drag that either requires a large capital base or "responsible" use of margin to avoid diminishing portfolio growth.
- MidKnight, in turn, was candid about his own constraint: he estimated needing roughly a $400k account to make his limited systematic work pay enough to live on, and separately confirmed he'd tried to automate his discretionary edge a few years ago and found it "pretty difficult to break everything down into a rules based approach" — a struggle **mm confirmed from his own experience** building a VWAP-proximity scanner that worked without ever having a clean "reasoning" for why.
- Rachit, watching from the sidelines, admitted he gets lost trying to get too specific about "signals" whenever he explores this area and lacks a confident mental model — MidKnight's blunt response: no shortcuts, just "a lot of time and experience," and much of what actually works is contrary to what's taught on YouTube.

**Sentiment:** The most candid, personal thread of the month — two experienced discretionary traders (MidKnight, mm) openly discussing the economics and difficulty of systematizing intuition, without either claiming systematic is simply "better."

**Pull quotes:**
- mm: *"eventually realized my systematic stuff in aggregate outperformed me sitting in front of a footprint chart for 8 hours a day scalping asia session shitcoins so i tried leaning more into that"*
- mm: *"at the end of the day we're all trying to get paid in some way. if you're consistently doing well manually then that's just where you perform best for the time being"*
- MidKnight: *"Most of what works is contrary to what you will read about or see on youtube. Especially around the trade mgmt side. It takes a lot of screen time."*

## 11. Portfolio sizing under stress, and IBKR operational reliability

Two smaller but practically-relevant threads about running strategies through the month's elevated volatility.

- George asked how others running RP7 handle a realized-vol measure that had cut his sizing "by almost half" — specifically whether people set a floor on minimum exposure. **Yan's answer reframed RP7 as a long-term, largely hands-off holding**: he rebalances monthly to target weights and lets the vol-scaling do its job rather than overriding it. (A related, more technical RP7 question from George back on March 7 — how the API's adjusted weights, which sum to 100%, interact with per-asset vol budgeting — didn't get a captured answer in the channel.)
- Separately, akhan asked how to size across a full stable of strategies (EOM bond, EOM index balancing, stat arb, risk-premia harvesting, VXX/VXZ) at month-end. **robotkris pointed to Module 6 of Trade Like a Quant's volatility-targeting approach** as the practical framework, and flagged a recent webinar on portfolio sizing.
- On reliability: Dan hit two separate IBKR issues this month — a recurring Netliq bug briefly zeroing out account value right before order submission (March 20, eventually described as fixed), and a trade-busting incident on March 31 where an exchange-side price glitch triggered his stop into a bad fill, resolved within hours once IB confirmed the busted trade was actually an adjustment rather than a cancellation.

**Sentiment:** Practical, low-drama risk-management housekeeping — a reminder that even well-automated portfolios need human judgment calls on sizing floors and exchange-side operational hiccups.

**Pull quotes:**
- Yan: *"For me, RP7 is basically my long-term investment portfolio that I'll likely never cash out, so I just rebalance it monthly according to the target weights and let it ride"*
- robotkris: *"I would steer you towards the volatility targeting approach from Module 6 of Trade Like a Quant. It's practically very useful (prevents any single thing from dominating your portfolio)."*

---

## Overall read

March 2026 was the busiest and most research-dense month in this digest series, set against an active Middle East war that kept crude, VIX and IV structurally elevated all month (#1) — a backdrop that fed directly into the earnings-season short-vol trade several members ran live (#2). **robotkris's contributions were the backbone of the month**: he ran a genuine multi-week research program on futures carry (Treasuries and oil, #3) and shipped a concrete, improved UVXY-VXZ hedge model in response to member questions (#4), while also surfacing the month's most consequential infrastructure idea — a possible RW-wide data-cost-sharing arrangement (#5) — and pointing members to the right internal framework for portfolio sizing (#11). **Euan's contributions were equally load-bearing but more analytical**: his 0DTE/earnings strangle statistics (#2), his independent carry-research parallel track (#3), and his structural explanation of VRP concentration around expiries (#8) are all durable, reusable frameworks rather than one-off answers. If you're looking for the two most actionable threads to build on this quarter: the UVXY-VXZ vix-aware hedge (already shipped and measured, #4) and the commodity/Treasury carry signals (still early-stage but with real robotkris-built infrastructure behind them, #3). The discretionary-vs-systematic exchange between MidKnight and mm (#10) is worth reading in full even though it produced no trade idea — it's the most honest single account this month of *why* systematizing trading intuition is hard, and what the economic trade-off actually looks like once you're profitable either way.
