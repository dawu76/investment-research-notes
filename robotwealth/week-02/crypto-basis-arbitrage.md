### Intro to Crypto Stablecoin Lending and Basis Arbitrage

Key questions to ask yourself as you're structuring a trade
- what useful service am I providing? E.g. taking the other side of price-insensitive traders who want to quickly enter or exit their positions
- what risk am I exposing myself to? E.g. exposure to large market moves; increases in margin requirements in arbitrage or basis trades; credit risk from lending my assets to borrowers
- how do I properly execute the trade? E.g. how do I size it appropriately given the risk, how do I manage my collateral as the margin requirements change?
- ancillary question: how competitive is this trade? if it's not competitive, do we expect it to stay that way?

The two main sides in crypto trades are:
1. speculators who want leveraged exposure to crypto price movements
2. those who are willing to lend out their crypto or take on a 'basis arbitrage' trade in order to earn a certain yield on their assets

Speculators who want leveraged exposure do so via two main avenues:
1. buying stablecoins like USDT and then using them to buy BTC on margin via the BTC/USDT exchange rate
2. buying BTC futures, which require collateral in the form of cash or crypto coins at an exchange

Method (1) results in supply & demand for stablecoins
- demand comes from traders who want leveraged exposure to BTC, ETH, or other crypto assets; these speculators are willing to borrow the stablecoins at a certain interest rate in order to buy BTC, ETH, etc.
- supply comes from those who own stablecoins and are willing to lend them out to speculators at a given yield
- if demand > supply, then the cost to borrow the stablecoins, i.e. the interest paid by speculators or the yield earned by lenders, will be fairly high; this is especially the case when the crypto market is hot; when the crypto market cools down, however, the demand to borrow stablecoins drops, resulting in a lower yield earned by lenders. The relative demand & supply also depends on the types of traders attracted to a market like crypto; e.g. in the early days of a market, there may be more YOLO speculators who want leverage, but as the market matures, more conservative investors and larger institutions move in, reducing the relative demand for leveraged trades
- Why are lenders of stablecoins earning these yields (interest on their loan of stablecoins)? They are providing a useful service to speculators in search of leverage. They are also taking on various types of risk: credit risk from lending, market risk from the possibility of the stablecoin losing its value.

Method (2) can result in crypto futures and spot prices diverging, resulting in arbitrage opportunities
- if there are a lot of traders looking for leveraged exposure to BTC, they will push the BTC futures price above the BTC spot price; e.g. the 3M futures price may be 10% - 20% higher than the spot price
- as the futures contract's expiry approaches, the futures & spot prices will converge; just as in the commodity carry trade possible in the 1980s, traders can bet on this convergence. In the commodity carry trade, there was an excess supply of commodity futures from producers trying to lock in the price they would get for their goods, driving the futures price below spot. In this crypto futures trade, the imbalance is on the other side, with excess demand for futures coming from leveraged speculators and driving the futures price above spot.
- in the commodity carry trade, traders would buy the depressed futures contract in the hopes that it would converge up towards the spot price; in this crypto basis arbitrage trade, traders would buy the spot asset and short the futures in the hopes that the two would converge as expiration approaches
- this difference between spot and futures prices is called the "basis" and this convergence trade is known as "basis arbitrage"; since the convergence trade is betting that the basis will go to zero, this is a "short basis arbitrage" trade
- as more traders try to take advantage of this short basis arbitrage trade, the demand for the spot crypto will increase, as will the amount of crypto futures being shorted; this will drive the "basis" lower, reducing the return from this trade
- regarding the persistence of this edge: why does the crypto futures vs. spot premium persist? Because there are limitations on how much spot can be purchased and how much the futures can be shorted.

![image](https://user-images.githubusercontent.com/1627180/173246935-4bd49524-6917-4af1-a59b-02a57102101c.png)

Key considerations for the crypto basis arbitrage trade

![image](https://user-images.githubusercontent.com/1627180/173248010-f5b9d2d7-5f11-4222-b150-a974f56ce832.png)

---

### References

TLAQ Week 2 [lecture](https://robotwealth.com/courses/trade-like-a-quant-bootcamp/lessons/2-stonkingly-obvious-high-probability-edges/topic/crypto-stablecoin-lending-and-other-yield-plays/): Crytpo Stablecoin Lending & Other Yield Plays
