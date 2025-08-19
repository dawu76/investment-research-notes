## The mistakes that traders make

### Is Trading a Game We Can Lose?

Losing at games of pure skill vs. luck
- Is it actually possible to lose money on purpose trading? And if so, what is the best strategy? It’s very easy to lose at chess because chess is a deterministic game of skill. There is no external random element. There’s no roll of the dice. There are well-defined rules. It’s just you versus the opposition. And, whilst it might be hard to identify really good moves in chess, it’s easy to identify bad moves.
- So you can lose at chess. On the other extreme, snakes and ladders is entirely a game of chance. Luck is the only factor. There is no skill involved. So it’s impossible to lose on purpose at snakes and ladders, unless you cheated somehow.
- In the middle is poker. Poker involves both skill and luck. In the short-term, luck dominates, but over the long run, all that luck averages out, and the best player will win and the worst player will lose. I think it’s clear to everyone that trading is more like poker than any of the other games here. Markets are highly unpredictable and short-term outcomes are dominated by chance. But that doesn’t necessarily mean that long-run outcomes are dominated by skill. It doesn’t mean we can necessarily win but, given what we know about the market, we can definitely lose.

Retail traders often do things that almost guarantee that they will lose money. 
- You might think that retail traders lose money because they are taking the wrong trades. You might think that they are buying when they should be selling and selling when they should be buying.
- And that if they did the opposite of what their instincts told them to do, maybe they’d make money?
- But that’s not it - these traders aren’t incredible “negative alpha” generating machines making lousy buy and sell decisions. 

There are three dominant strategies for losing money. I call them the mortal sins. They’re losing money because they are doing one or many of these three things: 
- They are trading **too often** – opening and closing positions without edge and paying lots of transaction costs. Trading is an expensive business. If you do it in a careless way, you’ll die from papercuts. If you’re trading to get an edge, you want to save it for times when you’re pretty sure you have a large mispricing, at least on average.
- They are trading **too big** – sizing too big and losing lots of money, which is very bad because you need money to make more money.
- They are **trying to be heroes** – they’re taking heroic or highly specific bets.

### Every time you trade you lose money

Every time you trade you lose money. It’s an expensive business!
- You pay a commission and a bunch of other fees.
- You pay a spread on the entry and exit price of each trade – it costs more to buy than you get for selling; you have to tip your market maker.
- Your trades will tend to push price against you if they are large. Your buying will make the asset you are trying to buy more expensive.

The most reliable way to lose money as a trader is to instantaneously open and close positions.
- Open and close, open and close, open and close. On every one of these trades, you’re going to take a loss.
- The loss you take will increase with the number of trades you take. It’s going to be a reliable grind down until you have no money left to trade.
- So trading decisions require a balancing act. You have to trade to make money of course. But you only want to do it when it’s worth the cost to do so. It’s a balancing act between **uncertain gains and certain losses**.

**Example**: Take an instrument trading on an exchange. There’s a limit order book where people post orders they are prepared to buy and sell at. We’ll assume you’re a very small trader so I can keep the example neat and we don’t have to worry about market impact, which is another important cost if you’re trading large. Now if we want to trade straight away, we can buy and sell at the prices in this image.
- And we might say that the middle point represents a short-term view of market fair value – the price where we think that a roughly equal amount of buying and selling would occur.
- It costs us more to buy than it does to sell – and that’s because the people who are quoting are providing us a useful service – they are providing us the ability to buy or sell instantly which is valuable and risky for them, so they expect to be compensated for it if they do it well. (They are buying cheap, selling rich, accepting and managing risk)
- Let’s say our total fees to trade this thing are 5bp and the bid/ask spread (the difference between the price we can buy and sell) is also 10bp. A basis point is 1/100 of 1%. So 5 basis points is 0.05%
- Now, let’s say that the market is pricing this instrument right. What would we expect to make if we bought the instrument, held it for a bit, and then sold it? The future is highly unpredictable. We can have random good news, we can have random bad news. But we can’t predict any of those things, so we expect staying the same to be the most likely outcome.
- We might visualize the expected fair value of this instrument in the future as a probability distribution like below, with the peak at the current price. (

<img width="750" height="400" alt="image" src="https://github.com/user-attachments/assets/286a68b9-af4d-4e55-b9d3-c720eb4647af" />

Now how much do we expect to make on the trade? Assuming we have no edge, we expect to lose 20 basis points on each round trip transaction. (By round-trip I mean opening and closing the position in full).
- We’ll start with the buy transaction. We bought at the green arrow but the fair value of it was the yellow dashed line half the spread lower than our buy price. So on buying, we expect to incur an immediate loss of 5bps (marked against the midprice) plus another 5bp we paid in commissions and fees. So we’re down 10 basis points on the entry. 
- Then on the exit, we’re selling something for 5 basis points less than it’s worth, and paying another 5 basis points in commissions. In total, we expect to lose 20 basis points on this transaction.
- So just to break even, we need the instrument to be mispriced by at least 20 basis points (assuming we’re closing it when it is fairly priced). We need to believe the market has mispriced this by 20 basis points, or 2*(fees + spread), simply to break even on the trade.
- To actually take this trade, you would also need the asset to be mis-valued by an additional hurdle to make it worth the while to take the risk (and because you’re wrong sometimes). So to buy this asset, you need to think it was undervalued by at least: 2x the fees + bid/ask spread + hurdle to make it worth the while to take the risk (and because you’re wrong sometimes).

**Lesson**: Be conservative. Do the bare minimum amount of trading to harness the edge you observe. 
- Restrict your trading to times when you’re relatively confident there’s a large mispricing or when you need to reduce risk. Minimizing your costs, through trading less often and avoiding marginal bets, is nearly always the correct move for the individual trader. In the tradeoff between 'uncertain benefit' and 'certain costs', lean towards reducing the latter.
- Note: We’re not always explicitly making a forecast of the fair value of an asset every time we trade. Often we’re just saying something like “on average at times like this in the past, this has tended to be underpriced by a significant amount.”
