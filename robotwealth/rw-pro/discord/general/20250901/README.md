## Discord notes for 2025 September

I hope some of you could help me clarify something in regards to position sizing dynamics in a "dollar-neutral" portfolio. Specifically I am having some troubles determining the effective position size for short positions. And I might be overcomplicating it.

Lets assume we have traded into two assets, with both starting price at 100. We are long 1 unit, and short 1 unit.  At the start of the trade, everything looks like this:
- Long: 100 USD
- Short: -100 USD
- Portfolio: 0

Now lets say the long asset increases to 110, and the short asset decreases to 90. In both scenarios we have gained +10USD, and a total of +20 USD. The portfolio from my broker now looks like this:
- Long: 110 USD
- Short: -90 USD
- Portfolio: +20 USD (which reflects the gains)

If I were to rebalance now (lets say I always want to rebalance to 100 USD for all positions for simplicity's sake), I would have to take OFF 10 USD risk of the long asset, but for the short asset I would add on risk by shorting more, such that;
- Long: 100 USD
- Short: -100 USD
- Portfolio: 0

This is what is causing me to be a bit unsure. Because the long position value reflects the gains, but the short position just reflects what the position is worth when we buy it back at a lower price, but it does not take into account the gains. This in turn led me to start toying around with a "effective position size" for the short position which would be: -Position size - 2xPNL. In this scenario, this would look like:
- Long: 110 USD
- Short: -90 USD - 2*10 = -110 USD
- Portfolio: 0

Basically a dollar-neutral portfolio which reflects equal USD size gains on both legs. In this scenario I take off risk on both legs when the trade goes "my way", and I add on risk on both legs if both go "against me".

... I might have explained myself improperly, because I was unsure about the "correct" way to rebalance a short position compared to a long position as the rebalancing becomes inverse of what you would do to a long position. When a long position increases in value, I will reduce risk when it reaches my upper rebalancing band. However, for a short position, which makes money, decreases in value, and I will have to add on risk to rebalance it. A long position directly has the P&L included in the position value, whereas the short position does not unless I account for the unrealized P&L. If I instead account for the unrealized P&L, I will take off risk from the position when it goes my way. Treating it similar to a long position.

However, after some more thought on this, it now makes sense as to why I would increase risk on the short position when it makes money to rebalance it correctly. Assuming this is a portfolio of funding carry for example, the funding will be based on the actual position value, and by accounting for the unrealized P&L I will be reducing the funding received from the short position by accounting for the unrealized P&L in the position value calculation, reducing the "edge" from funding itself, if that's what one is trading.

What was causing my confusion was this "inverse logic" for long/short positions. Lets just assume that we are fully informed traders, and the fair value for two assets are $100. We long one asset which is priced at 99, and short another which is priced at 101, expecting to receive +1 USD from both legs. Instead the long position increases in price to 110, and the short position decreases in price to 90. Given that the fair value for both assets is 100, we know the prices will converge to that. Lets assume in this hypothetical world that we are constrained to have these trades on, but are allowed to rebalance. We would rebalance the long position by taking risk off, as we have made more money than what was expected, keeping more gains when the asset converges to fair value. But for the short position, we would increase our short exposure in base units to rebalance. In this made-up scenario, when the asset converges back to the fair value, we would end up losing more as we have increase the risk exposure.

Again, I apologize for my absolute garbage explanations. I went down a rabbit hole and have probably overcomplicated something very simple 

Euan: "I briefly talked about this on Tuesday. Longs and shorts behave differently. Longs get bigger as they make money, but shorts get smaller. You just need to rebalance."
- But in terms of rebalancing, Is it incorrect to rebalance accounting for the P&L (the "effective" position size I mentioned above), or should I just rebalance in terms of what the actual position size is displaying? Basically taking off risk on longs and adding risk to shorts when the positions make money. The advantage for the short position in this case is that I will be taking off risk when the position goes against me (other way around for longs), but that also goes against the theoretical "If I short at price 100, and price goes to 110, E[R] increases and the short should be more lucrative, given that my "thesis" is correct".
- The overriding priority is to always have exposure where you want it. When it isn't, make it so. But where you want it, is a function of edge. In many risk premia trades you won't have an idea of edge beyond "it has some". So here we just keep exposure to the _original proportion of the account_. All we know is risk, so we just adjust based on risk.
- In some situations you know something about your edge. And it could be that edge increases as you lose money. This happens in **mean reversion** trades. Here you need to rebalance back to your desired edge/risk relationship (maybe Kelly or maybe mean/ volatility). To do this you need a model for edge.
- In the UVXY trade, as you lose money your account drops, so purely on a risk basis you need to reduce. If you have an edge model you can take that into account. I didn't get into the idea of making an edge model. It isn't trivial. But in my experience, _even with a decent model the risk change due to account depletion will dominate._
- Kris: Your exposures are a function of your model of edge and your desired risk. In the YOLO trade for example, your target weights change every day as the factor values change and the underlying assets get more or less volatile. In the risk premia change, your target weights really only change as the underlying volatilities change (assuming you're doing inverse vol sizing).

Kris: You really want to be treating rebalancing purely as the process that brings your exposures into line with what you want. 
- > If I short at price 100, and price goes to 110, E[R] increases and the short should be more lucrative, given that my "thesis" is correct"
- The problem with this is that if you have an edge, your thesis will be correct on average. In the short-term, you'll have times when it's wrong and times when it's right. You almost always have no way to predict when you're more or less likely to be wrong. Your edge plays out on average over the long run.
- _So if you take a bigger position at a certain time, you're essentially letting the results from that decision dominate your overall results_. And since you have no way of knowing if there's anything special about that result, you're introducing a source of luck. It's just as likely to deliver a big loss as it is to deliver a big win. But since you have an edge, it doesn't make sense to rely on luck. You should rely on that edge working out in the long run. And to do that, it makes sense to prevent any one result from dominating your overall results. That's the essence of rebalancing.
- I'm not sure what you mean by "accounting for the unrealised P&L." Your P&L is your P&L whether you've realised it or not. I think you might be confusing yourself by **thinking about rebalancing in terms of expected return rather than risk control**. It's all about keeping your risk in line with what you want.

---

Could you elaborate more on the rule of thumb for volatility when you were mentioning options of the VIX etf ( along the lines of 'only 25% of the skew is fairly priced')?
- Euan: The implied skew tells us how the option market expects implied vol to move as the stock moves around. It is displayed as vol(X) but that can be translated into vol(S). That translation is one of those simple but confusing things that I probably shouldn't attempt in a few lines. I'll do it in a webinar when one of the books gets to that point. Anyway, if you look at how vol actually moves when the stock moves, you will find it is much lower than the move implied by the skew. Typically only about 25% as high.
- So there should be a skew premium. But it isn't as high as the option market says. This is why a hedged risk reversal makes money: the skew premium. And this premium is a lot more reliable than the ATM VRP.
