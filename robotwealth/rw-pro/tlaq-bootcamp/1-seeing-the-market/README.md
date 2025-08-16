### TLAQ > 1: Seeing the Market As It Really Is > The Problems of Non-Stationarity and Adverse Selection

Let’s say you’re looking at doing a systematic trade. You think you’re making the same trade each time, give or take.

So you run a simulation, take the P&L of the simulated trades and plot them as a histogram like this. In this case, the returns are negatively skewed (I drew it that way), there’s a chance of occasional big losses.

The expectation (the mean of the trade returns) is positive. And the results are variable, cos who knows why things happen in the market day to day…

Now, you might think this histogram represents your edge. You might think that the uncertainty in market outcomes is represented by the spread of the histogram. And, you might think that, if you take enough bets, all the luck nets out and you’ll realize the expected returns.

You might think that, when you take a trade, you’re basically pulling a result out of a hat which returns distributed like above. Nearly right, but actually very not. When you group up all your trades like this, you’ve assumed that your edge was the same for each trade. And that all the variance you observe was purely a result of unforecastable market noise.

But that’s the best case scenario. Sometimes you are just wrong. However good we think this trade might be, sometimes we’re going to be taking predictably bad trades.

There’s certainly going to be predictable stuff that we haven’t modellled. So, our variance isn’t solely due to chance. Sometimes we take good trades and sometimes we take bad trades. And when we take bad trades, we’re more likely to lose money. Refer to histograms of P&L for 'good' trades vs. 'bad' trades.

Ok, so now you start trading this thing and you find your live trading results are worse than your simulation results over the same period.

<img width="700" height="350" alt="image" src="https://github.com/user-attachments/assets/ce00e07a-25f1-4ad5-97cc-766e9bfe757c" />

Well, assuming you haven’t’ done anything dumb this is likely because bad trades are easier to get into than good trades. So you’re likely either **missing good trades** or **getting bad prices on good trades**. 

In your simulation you assumed you got everything at some price in your data feed. In reality, there’s more competition for price than that, depending on your approach you might end up missing some trades or chasing as they trade away.
- If you miss some trade, you’ll find that they’re nearly all the good ones, the competitive ones.
- And you’ll find you take nearly all the bad trades. The uncompetitive ones.

So the 'bad' trades end up making up a larger proportion of your overall trades, while the 'good' trades make up a smaller proportion. This impacts you in all kinds of ways that we’ll discuss throughout the course – but one obvious takeaway is “don’t be a dick for a tick”. If you’re doing a systematic trade then _missing trades tends to be more damaging than worrying about buying within the spread to save a little bit on the entry price_.

Just know that the highly competitive market environment impacts you in many ways, some of them not obvious. Little things like missing the odd trade to try to finesse price can hurt you in serious ways.
