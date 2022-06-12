### Intro to Forward Contracts and Futures

What purpose do they play?
- producers and buyers of a given asset want to lock in the price they'll get or pay for that asset in N months; so producers and buyers enter into a **forward contract** to lock in the price at which they can buy & sell the asset; the producer agrees to deliver that asset in N months in return for a fixed price; the buyer agrees to take delivery of the asset, paying a fixed price for the asset
- forward contracts expose both sides of the trade to **counterparty risk**, where one side cannot fulfill the terms of the contract; e.g. the counterparty risk for the producer is that the buyer doesn't have the cash in N months to purchase the asset, while the risk for the buyer is that the producer isn't able to deliver the asset in N months (e.g. because of problems growing the crop or extracting the resource)
- forward contracts are also a less flexible, less scalable arrangement for both sides, as it's difficult to get out of the contract even if plans change
- Futures contracts are an evolution of forward contracts: these contracts trade on exchange, which takes a small cut of each transaction in return for the added convenience. Instead of entering into forward contracts with a specific producer or buyer, producers and buyers can instead trade futures contracts on the exchange to hedge their exposure to the asset. Futures contracts let both sides enter and exit their hedges as needed based on their desired exposure levels.
- How do futures exchanges manage the counterparty risk, i.e. the risk that buyers/sellers of contracts don't fulfill their end of the agreement? Through margin requirements that change as the contract's P&L fluctuates. E.g. a producer sells a contract to deliver `X` amount of an asset for `$K` in `D` days, and the buyer of the contract agrees to take delivery of `X` amount of the asset for `$K` in `D` days. The futures exchange will require that both sides of the trade post an 'initial margin' amount, e.g. 10% of the `$K` notional contract value, to their margin accounts at the exchange. This is caled 'initial' margin because the margin amount will fluctuate over time.
- What if the market for the asset changes significantly before contract expiration to the point that it makes sense for one of the parties to renege on the contract, e.g. the producer no longer wants to deliver the asset for `$K` because the asset's price has risen, or the buyer no longer wants to purchase at `$K` because the asset's price has fallen. How does the exchange prevent either side from reneging? By requiring the trade to be settled every day based on the futures contracts price fluctuations, with changes in the P&L of the contract position getting posted to the margin accounts of both parties. For example, if the price of the futures contract falls (because supply of the underlying is expected to increase), then the contract seller (usually the producer) sees a profit, while the contract buyer seller sees a loss. If the price of the contract rises, then the contract buyer sees a gain while the seller sees a loss.
- These gains/losses are realized each day and are posted to their respective margin accounts, with funds going from the account of the day's loser into the that of the day's winner. If this results in the margin account of the day's loser dipping below the minimum margin requirement, then that party has to post additional margin.

---

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
- regarding the persistence of this edge: why does the crypto futures vs. spot premium persist? Because there are limitations on how much spot can be purchased and how much the futures can be shorted. It takes a lot of capital to go long the spot crypto, and it doesn't make sense to buy it on leverage since that would require borrowing stablecoins at a higher interest rate. On the other side of the trade, shorting the crypto futures may require going on margin, which means traders need to manage their margin requirements closely. Arbitrageurs also need to aware of "basis risk" where the basis actually increases for a period of time.

![image](https://user-images.githubusercontent.com/1627180/173246935-4bd49524-6917-4af1-a59b-02a57102101c.png)

Key considerations for the crypto basis arbitrage trade

![image](https://user-images.githubusercontent.com/1627180/173248010-f5b9d2d7-5f11-4222-b150-a974f56ce832.png)

---

### References

TLAQ Week 2 [lecture](https://robotwealth.com/courses/trade-like-a-quant-bootcamp/lessons/2-stonkingly-obvious-high-probability-edges/topic/crypto-stablecoin-lending-and-other-yield-plays/): Crytpo Stablecoin Lending & Other Yield Plays

TLAQ Week 2 [lecture](https://robotwealth.com/courses/trade-like-a-quant-bootcamp/lessons/2-stonkingly-obvious-high-probability-edges/topic/crypto-basis-arbitrage-an-introduction-to-forward-contracts-and-futures/): Intro to Crypto Forward Contracts and Futures
