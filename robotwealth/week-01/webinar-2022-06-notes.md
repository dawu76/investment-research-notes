### Module 1 TLDR

---

Market is efficient due to competition
- so we typically end up near expected fair value
- hard to be profitable but also harder to pay far from fair value

Avoid losing $ due to the usual reasons of: overtrading, trading too big, doing "heroic things".
- e.g. if you have a directional POV, consider just buying the underlying instead of overpaying for options.
- don't take on huge trades as it's mathematically assured you'll eventually blow up
- don't try to predict the direction of very volatile assets

Goal: "get paid doing useful stuff in an uncompetitive environment" (just like in any other business)
- look for simple robust strategies, avoid trades requiring very sophisticated analyses
- strong programming skills are 'neither necessary nor sufficient' for trading success

The most important mistake to avoid: trading too big
- a sequence of returns of -X%, +X% results in a loss
- lose 50%, need to gain 100% to get back to even

Being profitable in your trading requires a plan
- understand what types of edges you'll pursue
- don't start trading creative, marginal effects, go for the most obvious, reliable trades

Realistic expectations: developing intuition based on simulations
- simulate the experience of holding a volatile asset with certain performance characteristics
- based on initial capital, tweak the Sharpe Ratio, annual drift %, annual volatility %
- compare the performance over a 5-year period: this is hard even with a decent edge!
- gives us an idea of the high variability in the results, even in the presence of a strong edge; and in the worst case, we didn't even make money for 4 years

Executing your edge
- To go from merely having ideas in your head to executing your edge via analytics/technology, start simple and focus on basic robust techniques. Don't try to over-engineer your techniques and tech stack at the outset.
- Avoid building technology you may not need. That represents time spent not making money. Focus on incremental improvements as they are needed.
- Concentrate on making money NOW. Don't build for a future that will never come.

Start with the simple and obvious
- simple, mostly systematic strategies
- exploit big high-probability edges
- can be executed manually or minimum automation 

Question: is there a reliable way to predict market direction beyond big events like central bank activity, pandemics, etc?

Not easily. There are weak indicators of return such as:
- counter-cyclical valuation timing
- short-term reversals
- medium term trend effects
- FOMC announcement drift
- seasonal regularities: turn of month; sell in May & go away; January effect;
- buying when there's "blood in the street"

But because stocks tend to go up over time, it's tough to beat that drift, as any attempt to time the market involves being flat, short, or under-invested.
- If your signal is actually useless and it leaves you out of the market 30% of the time, then your expected returns will be 30% lower.
- Can you consistently predict direction well enough to beat buy & hold?

Illustration: Hull Tactical's market timing signals
- they take a reasonable approach here, but they've under-performed the market due to their lower exposure

Question: how do we effectively leverage our analytical skills in trading?
- Most quant techniques are good for modeling things in an environment where "the edge is self-evident". They're focused on scalable techniques executed with precision. E.g. an options trader on the buy-side whose problem is all about managing risk while processing customer orders.
- Focus less on fancy techniques and more on understanding, "why do I get the trade? Why is the other side willing to trade at prices that seem cheap/attractive to me?"
- Focus on a simple-enough implementation that gets your 80% of the way there.

Question: with multiple assets, since volatility is sub-addivitive, the combined basket will have lower volatility than their simple sum.
- "Yes". So prefer uncorrelated stuff.

On the persistence of edges
- edges will disappear, new ones will appear

Question: risk premium vs. inefficiency
- inefficency = highly competitive mis-pricing, will disappear over time due to competition
- risk premium = many know that it pays but it persists because it involves taking on risks others don't want to bear
- more like a spectrum: ERP may include market-making, FX carry seeking, business hour effects; inefficiency includes momentum, FOMC drift, latency arbitrage
- our focus will be more on the ERP side, which is less competitive

Question: how are options order books constructed
- just like order books for standard assets
- spread is often larger due to many types of contracts for one underlying asset

Question: what do you think about stop losses?
- they aren't a magic way to cut losses out of your trades; they also change the shape of the trade distribution, sometimes in an unfavorable way;
- you may not just cut out the unprofitable trades, but also the eventually profitable trades; so your distribution of gain/loss ends up with a spike at the stop loss level while the area under the curve for positive trades is reduced
- but we use stop losses ourselves; sometimes we need a way to exit a trade based on an external signal;
- another way to manage losses is to manage to a drawdown (DD) limit: aggressively cut position size as you approach your DD limit in a perfect way; but in practice, this requires more active management

Question: better to trade different markets or to focus on a single one first?
- Trading is a generic discipline. Going broad is the easiest way to build a decently performing portfolio.
- But it's easiest to learn the discipline via concentration in one market/asset class because there is less market-specific parochial knowledge to learn.
- Unpredictable external events will affect our positions, it's bound to happen;

---

### Questions

**Question**: "what happens when all RW students learn about these uncompetitive opportunities here, then go and implement them all at the same time... and some even open funds to manage $$ for other people. Don't those spaces get very competitive and disappear? How do avoid colliding with each other?"

**Question**: what is a Sharpe Ratio?

A measure of risk-adjusted return, i.e. E(return) / STDEV(return)

**Question**: What is "liquidity"?

What is liquidity? Based on order book and the buy/sell orders there, we can buy or sell only a certain number of shares at a given point in time. If we try to offload more shares than there are open buy orders for, then we'll have to sell at lower prices.

**Question**: what is meant by path depedency?

The realized return at the end of a period depends on the sequence of returns that are randomly realized in a given run of the simulation (or a given run of "real life"). A given distribution can be used to generate many possible paths of returns.

**Question**: who would the 'motivated buyers' be in a down-trending market?

That would be highly context dependent. E.g. why would the current price not be as low as you think it should be? Perhaps the market is just digesting info more slowly because it doesn't recognize certain risks sufficiently. Or maybe you're selling to an over-leveraged trader who is trying to quickly cover their shorts.

**Question**: how does edge change in high versus low volatility environments?

Volatility can present opportunities to buy at discounts. It's essential to keep some dry powder to take advantage of these situations.

E.g. suppose an external shock causes an emerging market asset to fluctuate a lot more. Any holders who were leveraged will be forced to sell. Forced selling pushes prices lower, perhaps to discounted levels. If you have the capital, this can present opportunities to pick up assets at bargain prices. E.g. in March 2020, $LQD was selling at 9% below fair value due to heavy forced selling, letting us buy $100 of corporate bonds at $91 or so.

Re: fat tail trading - I wouldn't expect to get any edge from buying tail risk exposure.

**Question**: How would you quantify your edge?

In theory it would be the difference between your trade price and the expected value if you were to repeat the trade many times. But in practice accurately determining the true edge is quite difficult. This is especially true of longer-term positions. It also makes detecting a loss of edge difficult.

**Question**: What is your process for quantifying different possible sources of edge?

Via a mental model of why it would work and supporting analysis, followed by ongoing analysis of trade performance over time. But we'll never know for sure the extent of the edge due to the noise and unpredictability of the market. It's not a clean engineering problem.

**Question**: how do you confirm your edge is statistically significant?

The answer is you can't ever be sure due to data limitations. We observe the effect over time and see if it seems to behave as expected, weighing different possibilities.

**Question**: does finding an edge require backtesting on past data?

No, for certain types of trades and edges, we can't get our hands on the right type of data to effectively backtest it.

**Question**: is the content geared towards "fast" or "slow" trading?

Nearly everything we discuss in more detail requires no more than 1X/day trading.

**Question**: should we park our assets in VTI?

Yes, some of it. We should all have long exposure to a broad basket of assets.

Question: what do you think of WorldQuant's paper of 101 sources of alpha?

I've never seen anyone actually implementing this seemingly random list of possible edges.

**Question**: How much of the course will be focused on Crypto?

There will be crypto examples but we won't be covering specific mechanics of the crypto markets or of any asset classes. The focus will be on useful generic trading skills as well as a few concrete systematic strategies.

**Question**: what level of edge decay have you experienced onchain if any?

Enormous. Initially the edges were so big we could screw up and still make money but now we need to execute well to be profitable. Eventually new edges appear.

**Question**: will we discuss commodity trading techniques?

Only at a high level, not the implementation details.

**Question**: is there a programming language we should start to use?

Just start with MS Excel. A few examples in Module 5 will involve usage of R, though Python is also possible.

**Question**: Part-time vs. full-time trader distinction?

What can be feasibly managed without making it a full job? Certain analyses are impossible part-time, e.g. HFT or 24-hour crypto bots, day-trading SPY futures. The course is focused on trades that cna be managed with much less time investment.
