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

#### Questions

Question: ...

Answer: Near end of month, there will be marginally more buying pressure for $TLT from fund managers. Play with the window dressing app to understand how it works.

Question: why does the window dressing alpha persist?

Answer: The truth is the effect is fairly weak, noisy, and ties up capital, so it's not that attractive of an edge. It's not consistent to the point where it's present in every month, every year. It's not free money and it's not a large enough of alpha for fund managers to really spend a lot of energy on.

Question: How do we quantify our edges from these types of trades?

Answer: We'll cover this in more detail in Week 5.

Question: will we learn when to buy and sell?

Answer: Yes we'll cover this a bit in week 3 in the "Front Running Flows" and "Dispersing Dislocation" sections. Another approach is Positioning Imbalances, e.g. when traders are loaded up on one side of a trade and are feeling pain from certain moves in the market. There will be tons of examples in the Module 3 materials.

Question: Can you elaborate on pairs-trading strategies and statistical arbitrage?

Answer: we'll cover arbitrage -> pairs trading -> "one-legged" convergence trades where we aren't trading pairs of assets
- arbitrage: take advantage of minor price differences on different exchanges, buying on the cheaper exchange, selling it on the more expensive exchange; why is it not riskless: because it takes time and costs money to shift assets around
- pairs trading: a risky arbitrage trade where we do NOT ship assets across exchanges; instead we buy the asset on the cheaper exchange, sell on the more expensive one; the ideal outcome is that though we might have negative P&L on one exchange, we more than make it up on the other exchange; downside is higher transaction costs; this type of trade is riskier but more general in that it can work when the spread is volatile or the instruments are not fungible between different exchanges;
- statistical arbitrage: a more general version of pairs trading is where we deal with *correlated* assets on the same or different exchanges, not necessarily the same asset on different exchanges; here we expect the differences to converge but they won't necessarily
- examples: cross-venue pair trade, short basis arbitrage (long spot, short futures or vice versa), and equity pairs trades between correlated stocks or very similar instruments like ADRs; in all cases, go long the cheaper one, short the more expensive one
- "one-legged" convergence trades: can we avoid the transactions costs of trading two legs? we dealt with two legs to cancel out the market exposure; what if we do away with that, resulting in higher expected return but higher risk due to exposure to market movements; so these trades are exposed to two sources of return: expected convergence in the leg + variance from random market movements, which should cancel out over enough trades or over diverse enough assets
- to minimize variance we can do a lot of trades as in HFT or go broad, exposing ourselves to more markets
