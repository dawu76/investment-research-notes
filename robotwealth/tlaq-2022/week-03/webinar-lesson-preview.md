### 2022-06-14 notes

---

#### Overview of week 3

Look for non-competitive trades
- best example of this is risk premia harvesting
- e.g. risk premia harvesting from owning VTI, which faces certain risks that other participants may not want to bear, such as liquidity risk, political risk, slowing economic growth, rising inflation, rising interest rates

"Win-lose" games you can compete in: most active trading isn't win-win but rather involves one party "winning," the other party "losing"
- e.g. who is buying (selling) below (above) fair value because they need to enter or exit a position for reasons other than fair value, maybe due to redemptions or investment mandates or different time-frames, macro vs. micro views, different scales of trades ('capacity'), or different forecasts; also known as price-insensitive buying or selling; in other words, you want to trade with a party who doesn't mind they're selling too low or buying too high relative to your criteria
- you want to identity why the party selling or buying at this price? why is it advantageous for them? don't assume you're smarter than they are
- "other incentives" for trading beyond just buying below fair value or selling above fair value include bond "window dressing" by investment managers at the end of each month

Consider why can you compete in these games?
- is the trade too small for large players to exploit?
- is it too capital intensive for most retail traders to take advantage of?
- too noisy or slow to converge?

Examples of edges & representative strategies: the hardest trades are those where you're not providing a service to other market participants, e.g. taking advantage of behavorial and structural effects. Easier to harder edges include the following.
- dispersin' dislocations
- front-running flows
- positioning imbalances
- speed advantages
- information advantages
- exploiting mistakes
- behaviorial / structural effects

---

#### Pairs Trading Setup

Sort pair candidates -> Trade: this is an iterative process
- which pairs are good? that's the hard part, while trade execution is easier
- how do we find which assets have lumpy flows that push them away from fair value, and which pairs of assets should move together over time? this is a mean reversion trade
- look at pairs sorted / scored by features: we'd expect pairs with higher ranks to have generally higher returns in a backtest
- which features that would explain how well two assets can be pairs? e.g. same industry, size, profitability, exposure to factors? how predictive has past behavior been of future activity, using different lookbacks?
- how do we trade pairs? execution is less important than selecting two candidates to trade; examples include: 20-day 2 standard deviation Bollinger Bands of these pairs, where we buy when the pair hits the bottom band, short when it hits the top band
- it's usually the simpler, blunter techniques that work best and don't require as much execution skill to be profitable; no need to feel quant anxiety

---

#### Broader statistical arbitrage

Looks more like the one-legged convergence trades.

Example: $CUBE/$EXR pairs trade - plot their ratio or log-difference to see how they're varying over time, shorting the more expensive one, buying the cheaper one in equal $ amounts as the ratio fluctuates around a long-term average. One of the legs of these trades is a market hedge to cancel out the risk from exposure to the industry. This entails costs as one of the legs typically is not profitable.

If you're trading a diverse enough book, you can do away with the two sides and just buy or sell one of the assets in the original pairs trade. Instead just associate features (price, volume, slope, order flow, fundamentals) with one of each leg and use them to determine the best candidates to trade. The assumption here is that trading the leg you "expect to converge" will have higher EV at the expense of higher variance (due to exposure to market risk).

---

#### Questions

##### Question: ...

Answer: Near end of month, there will be marginally more buying pressure for $TLT from fund managers. Play with the window dressing app to understand how it works.

##### Question: why does the window dressing alpha persist?

Answer: The truth is the effect is fairly weak, noisy, and ties up capital, so it's not that attractive of an edge. It's not consistent to the point where it's present in every month, every year. It's not free money and it's not a large enough of alpha for fund managers to really spend a lot of energy on.

##### Question: How do we quantify our edges from these types of trades?

Answer: We'll cover this in more detail in Week 5.

##### Question: will we learn when to buy and sell?

Answer: Yes we'll cover this a bit in week 3 in the "Front Running Flows" and "Dispersing Dislocation" sections. Another approach is Positioning Imbalances, e.g. when traders are loaded up on one side of a trade and are feeling pain from certain moves in the market. There will be tons of examples in the Module 3 materials.

##### Question: would shitcoins give us better opportunities due to greater inefficiencies?

Answer: Yes, it's more likely to see occasional examples of poor trade execution, which we can take advantage of via really low limit orders

##### Question: regarding crypto basis arbitrage trades, can we ever go long the future, short the spot?

Answer: yes but it's higher costs to borrow spot to short since there is less supply of this

#### Question: Is it possible to trade in a way that combines speed and diversification?

Yes but start with the easier problems and less competitive markets. Start with executing once per day trades. Don't put pressure on yourself to recreate RenTech's techniques. Get excited with the idea of building out a nice trading setup but don't overbuild, focus on what you actually need to make money and incrementally build off of that.

Focus on the methodology first before going into the executional details.

##### Question: Can you elaborate on pairs-trading strategies and statistical arbitrage?

Answer: we'll cover arbitrage -> pairs trading -> "one-legged" convergence trades where we aren't trading pairs of assets
- arbitrage: take advantage of minor price differences on different exchanges, buying on the cheaper exchange, selling it on the more expensive exchange; why is it not riskless: because it takes time and costs money to shift assets around
- pairs trading: a risky arbitrage trade where we do NOT ship assets across exchanges; instead we buy the asset on the cheaper exchange, sell on the more expensive one; the ideal outcome is that though we might have negative P&L on one exchange, we more than make it up on the other exchange; downside is higher transaction costs; this type of trade is riskier but more general in that it can work when the spread is volatile or the instruments are not fungible between different exchanges;
- statistical arbitrage: a more general version of pairs trading is where we deal with *correlated* assets on the same or different exchanges, not necessarily the same asset on different exchanges; here we expect the differences to converge but they won't necessarily
- examples: cross-venue pair trade, short basis arbitrage (long spot, short futures or vice versa), and equity pairs trades between correlated stocks or very similar instruments like ADRs; in all cases, go long the cheaper one, short the more expensive one
- "one-legged" convergence trades: can we avoid the transactions costs of trading two legs? we dealt with two legs to cancel out the market exposure; what if we do away with that, resulting in higher expected return but higher risk due to exposure to market movements; so these trades are exposed to two sources of return: expected convergence in the leg + variance from random market movements, which should cancel out over enough trades or over diverse enough assets
- to minimize variance we can do a lot of trades as in HFT or go broad, exposing ourselves to more markets

##### Question: can you provide an example of AMMs?

Answer: Futures traded against a virtual AMM, where buying makes the futures price exponentially more expensive, while selling makes it exponentially cheaper.

General idea is to push vAMM towards fair value of the futures, where fair value is based on prices of similar futures elsewhere.

##### Question: PEAD and FOMC announcement drift strategies?

Answer: The idea is that price tends to drift in the direction of the surprise for the next 3 months. The PEAD effect appears to have diminished recently.

When do prices drift in the direction of the general reaction, and when do they reverse the initial reaction?

##### Question: How much of your porftolio should be allocated to risk premia harvesting vs. active trading?

Start with more of your capital allocated to more robust, harder-to-screw up strategies like RPH and allocate less to active trading, depending on your experience and track record. This can also fluctuate depending on the opportunity set from the larger macro environment.

##### Question: What does the path to trading full time look like?

Answer: The problem is that you need money to make money, and it involves high variance.

Pulling out funds from your trading account for living expenses lowers your trading capital, which is worse during market drawdowns.

How do we deal with this? Need to find lower-volatility edges, i.e. minimizing the variance. This requires "grinding" and higher time commitment babysitting your positions and looking for opportunities.

So you ideally need other non-trading income streams. It's not realistic to expect to live off of your trading immediately. Don't quit your job and jump in without other sources of income. Start with the low-touch, robust approach and master it - you will learn a lot more from that than from delving into esoteric quant strategies.

###### Question: what academic degrees could help you get your foot in the door of a firm?

Credentials less important than track record for crypto firms. But need a PhD or Masters in FE for tradfi roles. Crypto has lowered the entry bar for trading as retail traders can use products offered by retail crypto firms; the same is not true of the products used by institutional traders.
