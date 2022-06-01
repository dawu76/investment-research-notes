### Module 1 TLDR

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
- Most quant techniques are good for modeling things in an environment where "the edge is self-evident". E.g. an options trader on the sell-side whose problem is all about managing risk while processing customer orders.
- Focus less on fancy techniques and more on understanding, "why do I get the trade? Why is the other side willing to trade at prices that seem cheap/attractive to me?"

### Questions

Question: "what happens when all RW students learn about these uncompetitive opportunities here, then go and implement them all at the same time... and some even open funds to manage $$ for other people. Don't those spaces get very competitive and disappear? How do avoid colliding with each other?"

Question: What is "liquidity"?

What is liquidity? Based on order book and the buy/sell orders there, we can buy or sell only a certain number of shares at a given point in time. If we try to offload more shares than there are open buy orders for, then we'll have to sell at lower prices.

Question: who would the 'motivated buyers' be in a down-trending market?

That would be highly context dependent. E.g. why would the current price not be as low as you think it should be? Perhaps the market is just digesting info more slowly because it doesn't recognize certain risks sufficiently. Or maybe you're selling to an over-leveraged trader who is trying to quickly cover their shorts.

Question: how does edge change in high versus low volatility environments?

Volatility can present opportunities to buy at discounts. It's essential to keep some dry powder to take advantage of these situations.

E.g. suppose an external shock causes an emerging market asset to fluctuate a lot more. Any holders who were leveraged will be forced to sell. Forced selling pushes prices lower, perhaps to discounted levels. If you have the capital, this can present opportunities to pick up assets at bargain prices. E.g. in March 2020, $LQD was selling at 9% below fair value due to heavy forced selling, letting us buy $100 of corporate bonds at $91 or so.

Re: fat tail trading - I wouldn't expect to get any edge from buying tail risk exposure.

Question: How would you quantify your edge?

In theory it would be the difference between your trade price and the expected value if you were to repeat the trade many times. But in practice accurately determining the true edge is quite difficult. This is especially true of longer-term positions. It also makes detecting a loss of edge difficult.

Question: How much of the course will be focused on Crypto?

There will be crypto examples but we won't be covering specific mechanics of the crypto markets or of any asset classes. The focus will be on useful generic trading skills as well as a few concrete systematic strategies.

Question: what level of edge decay have you experienced onchain if any?

Enormous. Initially the edges were so big we could screw up and still make money but now we need to execute well to be profitable. Eventually new edges appear.
