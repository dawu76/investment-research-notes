# Raw message log — #tradfi-trading (Robot Wealth Community)

**Period:** 2026-06-01 to 2026-06-30 (no activity on Jun 1; first message Jun 2)
**Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
**Message count:** 151
**Extraction method:** Browser automation (Claude in Chrome) — Discord search (`in:tradfi-trading after:2026-05-31 before:2026-07-01`) to locate the range start, then DOM scroll-and-extract to pull message text, author, and timestamp directly from the rendered page. See `rw-pro-tradfi-trading-20260601-20260630.md` for the thematic summary.

Format: `timestamp | author [reply]: message text`. `[reply]` marks a threaded reply to an earlier message. Long messages may be truncated at ~250 characters at source.

---

6/2/26, 6:45 PM | NP [reply]: Forced to eat garbage
---
6/3/26, 4:02 AM | Matt G: Love this chart.
---
6/3/26, 7:50 AM | MidKnight: unbelievable
---
6/3/26, 8:01 AM | Rachit: thats a pretty big number
---
6/4/26, 11:08 PM | robotkris: @here Quick update on the FX stat arb stuff we looked at in the last webinar... We applied the triangulated stat arb approach to fx using a dense web of currency baskets. Sharpe 1.3 before costs, 1.5 combined with the sparse version. I flagged at t[runcated]
---
6/4/26, 11:13 PM | Rachit [reply]: really interesting how you used correlations to figure out there was a data issue! suppose layering costs on top of this would further degrade the sharpe?
---
6/4/26, 11:13 PM | robotkris [reply]: I was thinking 0.7-0.9 after costs... might be optimistic.... I probably shouldn't anchor these things without doing the actual analysis!
---
6/5/26, 4:08 AM | mm: i was banging my head against a wall for a day or two trying to figure out how you were able to get that over 1[truncated]
---
6/5/26, 4:08 AM | mm: but your new findings are more in line with what i found and what i would expect from markets with billions in capacity
---
6/5/26, 7:41 AM | Dan [reply]: Hi Kris, Regarding "FX is one of the deepest markets" - for this reason I was trying to get setup to trade FX on IBKR. i.e. Real FX not CFDs. However even with all the permissions enabled, it seems IB restrict Australians to only 5 currencies or so
---
6/5/26, 7:42 AM | llIHeroic: Looked at this years ago and in the US IBKR still gouged you on the rate spreads trading spot
---
6/5/26, 7:43 AM | llIHeroic: The cme futures were the only viable option iirc
---
6/5/26, 8:09 AM | MidKnight [reply]: Yeah its true the futures have a better spread just looking at best bid/offer, but you can bid/offer between the spread with the IDEALPRO at increments at 0.00001
---
6/5/26, 8:13 AM | MidKnight: in some products like the euro, it is mostly a 0.00001 spread vs the futures at 0.00005
---
6/5/26, 8:22 AM | llIHeroic: The problem at least at the time was let's say LIRA/USD was +7% on net rate and you'd only get forwarded like 3.8% it was awful
---
6/5/26, 8:25 AM | llIHeroic: The proper forwards are embedded into the futures so it isn't an issue there
---
6/5/26, 8:26 AM | MidKnight: yeah, ok your statement could be more consistent with more exotic rates. I've never looked at the Lira seriously. The yield is good but the risk profile of it never appealed to me
---
6/5/26, 8:29 AM | llIHeroic: Yeah, it was a long time ago so take it with a grain of salt. Even on major currencies though if they withhold 1% of the notional carry that's a lot of units of sharpe; esp. considering fx vol is usually low. 5-10y ago I don't know if it's different
---
6/5/26, 8:29 AM | MidKnight: 2.7 cent spread on TRY right now on idealpro
---
6/5/26, 8:32 AM | llIHeroic: Yeah it's still crazy: https://www.interactivebrokers.com/en/accounts/fees/pricing-interest-rates.php — IBKR gives you 5% for long TRY positions and the actual short rate is like 30%. IBKR still collecting huge carry off their customer's risk positions
---
6/5/26, 8:33 AM | MidKnight: yeah that perspective sucks and now I see your point vs the futures more clearly. Thanks for highlighting that. I guess its another one of those tradeoffs one has to make with respect to sizing granularity given desired exposure vs more profits
---
6/5/26, 8:34 AM | MidKnight: every fx brokers slants the yield in their favour
---
6/5/26, 8:36 AM | MidKnight: i love the granularity you can have in FX, but I be honest in that is a bloody hard group of markets to squeak out much gain from
---
6/5/26, 3:35 PM | Dan [reply]: oh I have all the futures already, the reason I was looking for FX was to get more markets - particularly the crosses. Most of the liquid forex futures are long or short USD, which makes them all fairly correlated and not too additive to the portfolio
---
6/5/26, 3:37 PM | Dan [reply]: I agree that FX is hard to trade though, one of the most efficient markets and I don't understand why so many "gurus" push beginners into trading FX & CFDs.. I want it for diversification and lower correlations, but my stuff doesn't do that well on FX
---
6/5/26, 6:34 PM | alvin [reply]: Suspect it has to do with the insane leverage FX has (comparatively) and also shady brokers that gives affiliates a cut of their customers trading activity
---
6/6/26, 4:31 AM | Dan [reply]: Yeah, and no PDT rule I think? So these furus can attract people that want to trade with only $1k which widens their net for the grift.
---
6/6/26, 6:51 AM | Sam: Better cash management with the CFDs though. Also my CFD broker will pay interest of 29% on short USD/TRY, to give an example. Is that better than IBRK?
---
6/6/26, 7:00 AM | Dan [reply]: Interesting thanks didn't know that about cash usage on forex. TRY is turkish lira? that would've been a fun one to trade, but looks like IB is not listing it. https://www.interactivebrokers.com.au/en/trading/ibkr-forex-cfds.php Can you see these rates without the IB site trying to flip you to another country? ps does your CFD broker have a good API?
---
6/6/26, 7:18 AM | Sam: The net annualized rate you will earn is approximately 31.5% to 34.5%, depending on real-time market swap spreads. This net annualized yield is determined by subtracting the US borrowing rate from the Turkish Lira interbank lending rate, adjusted for [broker markup]
---
6/6/26, 7:18 AM | Sam: so IBKR has better rate than my CFD broker.
---
6/6/26, 7:19 AM | MidKnight [reply]: IB lists it in the idealpro exchange. USD.TRY
---
6/6/26, 7:20 AM | MidKnight: its your classic carry style trade the Lira, big yield, big negative tails
---
6/6/26, 7:22 AM | Dan [reply]: ahh yep, seems like Aussies can't trade idealpro except for the 5 main currencies that we're allowed.
---
6/6/26, 7:37 AM | Sam: Try CMC Australia
---
6/6/26, 9:25 AM | alvin [reply]: Think so yeah. Fx isn't centralised so there's a bit of a Wild Wild West (albeit better now)
---
6/6/26, 1:20 PM | Matt G: And so the insanity begins. I have no idea what will happen with the IPO and that feels like speculation to me so I am not planning on joining the IPO, but I've been wondering how to trade that need for the passive funds to buy into Space X on the day it is included in the various indices. Being long a few days before and selling on the inclusion date might be a sensible trade? I believe NASDAQ inculsion is July but S&P much later. Has anyone experience of trading stocks that enter indices? Is it a sensible or reliable trade?
---
6/7/26, 1:51 AM | FullMetal37!: I think the easier trade is to short the IPO after a few days/weeks. but probably borrowing costs would be high for something like SpaceX
---
6/7/26, 4:17 AM | Quarry614 [VBT]: Don't forget that because SpaceX's float will only be 4-5% and guaranted adding to the NASDAQ 100 in 2 weeks (ok, not guaranteed, buyt they did change the rule specifically for SpaceX, so yea) would mean that its affect on the index would be negligible. Therefore, they are going to weight it with a 3x multiplier (!) so that its weighting counts for 12-15% of its total valuation. In 2 weeks there is going to be massive index fund buying for an overweighted position. I would like to know if Index funds are going to be buying early (which might mess up thier tracking) or if they have to wait, which will be an almight squeeze?
---
6/7/26, 6:35 AM | llIHeroic: I think big front runners have made the edge close to zero post announcement
---
6/7/26, 6:36 AM | llIHeroic: Heard it mentioned modeling and predicting inclusions pre-announcement is where the edge shifted too and similar to Euan heard naive index inclusion has been dead for a long long time
---
6/8/26, 12:04 AM | Sam: CRSP index trackers will be buying probably at the get go.
---
6/8/26, 12:07 AM | Sam: SpaceX IPO is priced at $1.77 trillion. The London grey markets are pricing SpaceX about $2.1 trillion. Clearly an arbitrage type situation...if you can buy IPO shares.
---
6/8/26, 12:08 AM | Sam: FWIW, i intend to apply for IPO stock
---
6/8/26, 2:48 PM | marco [reply]: how does the allocation work? is it pro rata or FCFS? because for sure it will be oversubscribed, they size it for that too happen so it pops on day1 and they can call it a success
---
6/8/26, 2:49 PM | marco: i doubt it will a mid-long term good deal though, the economics don't look so good
---
6/8/26, 8:56 PM | Sam: It's going to be scaled down since SpaceX will be massively oversubscribed. I reckon an allocation of 10% of whatever you apply for
---
6/9/26, 12:27 AM | Sam: Beware IBKR flipping policy...if you sell IPO shares within 30days?..you can't apply for any more IPOS for a period of 60 days
---
6/9/26, 12:28 AM | Sam: Anthropic probably not coming to market till Oct and Open AI might be Dec
---
6/9/26, 12:38 AM | Alex [reply]: Where does one find out about these kind of policies? I think about doing the IPO with a regional (german) broker and now wonder about policies like that applying.
---
6/9/26, 2:45 AM | Sam: Ask Grok/Gemini etc
---
6/9/26, 2:46 AM | Sam: Or ask your broker!
---
6/9/26, 3:16 AM | marco [reply]: oh wow i am surprised you even get that. i suppose antrophic will be insane.. i thought so many times to long it on ventuals but didn't really trust the market (and it's not so liquid)
---
6/9/26, 3:17 AM | marco: it's trading at 1.6T now lol
---
6/9/26, 5:00 AM | M4TZEHDF [reply]: German brokers normally don't let you participate in US IPOs, SpaceX is the first exception. So I guess there is no such policy.
---
6/9/26, 5:02 AM | Alex: I thought they do, but just very very rarely unless you're with Deutsche Bank. I guess I'm gonna ask them and otherwise just wing it.
---
6/9/26, 5:04 AM | Alex: Also think its kinda suspect how they not only changed many of the index inclusion rules for spacex and others but now its also available for many german retail brokers? Sounds to me like retail customers and etf holders are supposed to be exit liquidity
---
6/9/26, 5:11 AM | M4TZEHDF: No way, of course everybody in finance wants the best for retail
---
6/9/26, 5:13 AM | Rachit: they are going to be mining space asteroids with robots the shares are literally going to the moon (and surroundings)
---
6/9/26, 6:46 AM | Sam: I would check how much your German brokers charge in FX fees. And any other fees for that matter.
---
6/9/26, 6:58 AM | Sam: https://www.lsegissuerservices.com/spark-insights/ifr-the-syndicate-episode-two/episode-two-the-disastrous-1987-bp-share-sale
---
6/9/26, 2:17 PM | Alex [reply]: Well yea you're right that this is usually the case. But seems worse this time.
---
6/9/26, 2:19 PM | Alex [reply]: Yes sure. I'm on top of that. Usually I trade in an USD account where I got no fx fees. But doing IPO's I think I'll have to do that in EUR and that would be 0.3%. Pretty bad for active trading but for a single trade it's alright.
---
6/10/26, 9:10 PM | Sam: Saudi, Kuwait, said to place $1b-$5b each in orders re SpaceX
---
6/10/26, 9:22 PM | Rachit: lmao
---
6/11/26, 2:38 AM | Rachit: 4x oversubscribed
---
6/11/26, 6:06 PM | Dan: IBKR Internalization - good or bad? I don't want to end up as PFOF (payment for order flow). Various forums say not to do it, but the way IB write the blurb sounds ok?
---
6/11/26, 8:04 PM | Euan: I'm going to talk a bit about this tonight. Basic conclusion is that it probably doesn't matter much for most people
---
6/11/26, 9:50 PM | Dan [reply]: There was 2 reasons I'm considering it: a) I had a MOC order that went unfilled (expired at 16:30), and it was because another strategy was making a LOC order on the same stock that day that did get filled (LOC was buying, MOC was selling). Rare, and I can handle that with orders, but I had read that internalization can get around self-match protection. b) On tiered commissions, the commissions are cheaper but the exchange fees pass through. I'm wondering if we get enough fills internally it's going to save on the fees part of commissions. Probably end up being a rounding error though, there's not much info out there on this.
---
6/11/26, 10:00 PM | Euan: i do applaud the focus on costs though
---
6/14/26, 9:45 PM | Dan: Some VRP via ETP stuff from Concretum guys. Requires executing at the close. https://concretumgroup.substack.com/p/automating-a-volatility-strategy
---
6/16/26, 6:46 PM | deal_me_in [reply]: Is this just an unhedged version of the vix carry strategy? That's also missing exposure to the volatility drag effect from shorting svxy?
---
6/16/26, 8:11 PM | Dan [reply]: Possibly, I can't say as I'm not running the RW version but thought it was interesting - particularly how often code is provided these days. Maybe due to LLMs making code fairly easy now we'll see that more often.
---
6/16/26, 8:12 PM | Dan: I decided I'm not going to run with this one, it's too similar to my other VIX stuff.
---
6/16/26, 8:23 PM | deal_me_in: What other Vix stuff are you running?
---
6/16/26, 8:39 PM | Dan [reply]: Futures in my normal carry portfolio, and for VXX some hedging strats, and a short strategy that uses a combination of things like Contango, and S&P measurements.
---
6/16/26, 8:41 PM | Dan: Noticed something interesting when looking at this though - the Margin is way higher to be long SVIX than it is to be short VXX. I'm guessing it's the special status of SVIX as an inverse or leveraged ETF. I always thought SVIX might be preferable to some because the max you can lose is to go to 0, but VXX's max single-day spike is only 40% or something - so far that is 😉
---
6/16/26, 8:43 PM | deal_me_in: Interesting that you have a carry portfolio. What kind of strategies are in it?
---
6/17/26, 7:33 AM | Dan [reply]: Just one, Carry. Or carry long & carry short if you separate them. Diversified futures, runs on anything that gets a strong contango or backwardation in the curve.
---
6/17/26, 7:42 AM | MidKnight [reply]: Yeah the volatility drag isn't there under this structure, but neither is the large borrow costs you can get periodically from shorting these VIX ETFs. UVXY has exceeded 40% borrow costs in the past. Not to mention there is also no risk of having sha[res called away]
---
6/17/26, 7:47 AM | 4D [reply]: yeah, i just trade vix futures
---
6/17/26, 8:21 AM | Dan [reply]: UVXY is bad, got a few rejections in the past.
---
6/17/26, 8:23 AM | Dan: VXX on the other hand I've never been rejected, borrow cost is 2.98% today and I have a little thing on my UI showing costs on positions. I don't see it diverge far above that often.
---
6/17/26, 8:24 AM | MidKnight: you can check it out historically in the short borrow costs data file from RW, VXX has exceeded 20% in the past
---
6/17/26, 8:25 AM | Dan [reply]: I got annoyed at some timing luck with the rolls, I'm sure it's fine long term I was just annoyed lol. The ETPs are smooth because of the VX30 thing. I still have short VIX futures for carry, but I'm avoiding the front month now just doing M2 onwards
---
6/17/26, 8:25 AM | Dan [reply]: Nice thanks, wasn't sure where to get that.
---
6/17/26, 8:26 AM | MidKnight: at the moment I am exploring a weekly rebalance back to the 30D maturity
---
6/17/26, 8:26 AM | Dan: I've wondered in the past, at live execution time if there's a borrow level that we should just skip the trade. For stock-shorting, it's said that high borrow rates predict a risky or potentially unprofitable trade and I know some people do skip them. But I don't like not having data for the backtest on it.
---
6/17/26, 8:26 AM | MidKnight: i'm further conducting a study on switching the constant maturity duration based on the regieme
---
6/17/26, 8:27 AM | MidKnight: you can get periods of almost 3 months with vix in backwardation
---
6/17/26, 8:27 AM | 4D [reply]: me too. I am now on July August and September
---
6/17/26, 8:28 AM | 4D: Targeting 50 and 80 days maturity
---
6/17/26, 8:29 AM | Dan [reply]: Sounds like a smoother way to do it
---
6/17/26, 8:30 AM | MidKnight [reply]: I'm curious if you are doing just the short part or did you calendarize it?
---
6/17/26, 8:30 AM | MidKnight: because the margin is a lot lower if its a calendar
---
6/17/26, 8:30 AM | 4D [reply]: Calendar, but I make a schedule to roll one spread every couple of days
---
6/17/26, 8:32 AM | MidKnight: have you guys also looked at doing the same thing with the V Stoxx futures?
---
6/17/26, 8:32 AM | MidKnight: I've been paper trading it a bit and seems pretty similar, but maybe too similar
---
6/17/26, 8:32 AM | MidKnight: IB ticker is V2TX
---
6/17/26, 8:34 AM | Dan [reply]: High correlation, and higher trading costs (less liquid). But I'm not sure how high correlation, I haven't done the work on it..
---
6/17/26, 8:34 AM | 4D: for example, suppose I want to have 8 spreads today. To make 50 and 80 days maturity, I need front: [0. 4. 4. 0. 0. 0.] back: [0. 0. 3. 5. 0. 0.] the first 0 means 0 position for June, 4 positions for July, and so on then I subtract the back array from front array to be [0, -4, -1, 5]. that's what I want, short 4 vx of July, 1 vx of Aug, and long 5 of Sep. if you want to do 30 spreads, you need to roll one spread everyday.
---
6/17/26, 8:35 AM | Dan: Also VSTOXX is only micros I think, which is another trading costs thing.
---
6/17/26, 8:35 AM | MidKnight [reply]: i'd think of it as a mini, its 100 euro / pt
---
6/17/26, 8:36 AM | MidKnight: vxm is 100 USD / pt
---
6/17/26, 9:40 AM | llIHeroic: I think the sharpe of the 40-60ish dte is a little better than short 30day or inside
---
6/17/26, 9:41 AM | llIHeroic (edited): The decay is higher (per unit) but var/jump risk also scales faster
---
6/17/26, 8:22 PM | deal_me_in [reply]: I havent done anything with futures so please excuse my ignorance... are you simply finding futures with in backwardation and going long; and finding futures in contango and shorting them?
---
6/17/26, 8:58 PM | Dan [reply]: It's a bit more complicated, as I'm trading different parts of the curve. E.g. with Nat gas there could be part of it that I'm long, and another part that I'm short. Carry is fun that there are so many different types of carry to consider as well, it's a big decision tree of choices to come to your final strategy, or ensemble of strategies.
---
6/17/26, 8:59 PM | Dan [reply]: A very basic demo that got me interested and led me down the path to what ended up being my most difficult and time consuming strategy to develop, was the demo strategy Clenow describes in his book and in this video https://www.youtube.com/watch
---
6/17/26, 9:00 PM | Dan: If you want more detail on various more professional/quanty (robust) ways to build it - see the papers and webinar put out by Resolve Asset management. They've done a few and some go right into how to calculate and vol-adjust them.
---
6/17/26, 9:18 PM | deal_me_in: TY! My backlog is so long lol.
---
6/18/26, 4:07 AM | Andre [reply]: I've always wanted to study his Term Structure strategy from when I read the book. IIRC it was the best strategy he presented. How is it performing for you?
---
6/18/26, 8:03 AM | Dan [reply]: Started that one in June 2025, so only 1 year live and since Carry goes through long cycles it's been an interesting period that does not match the long term behaviour - I say that because shorts have dominated performance which is the reverse of the [long-run expectation]
---
6/18/26, 8:03 AM | Dan: It's quite different to Clenow's as I use vol-adjusted carry whereas he uses simple percentages. I also sector-weight things for potential correlation benefit/risk, and have a bigger universe.
---
6/18/26, 8:05 AM | Rachit: fuck me that looks like a hell of a ride
---
6/18/26, 8:08 AM | Dan [reply]: Not at all, it's combined with Trend, Skew, MR, and Seasonal signals in the same account. The carry curves are just if I separate it out. For all 5 futures signals combined it looks like this. But yeah I wouldn't want to run carry by itself, like T[rend alone would be...]
---
6/18/26, 8:08 AM | Rachit: ahhh right that seems a lot more reasonable!
---
6/18/26, 8:11 AM | Dan: Check out RSSY where CoreyH combined carry with stocks, has that 6 month drawdown I talked about but it's more muted by the equity component, though you can def see liberation effect on that. Doesn't have a long history but from other carry funds you [can extrapolate...]
---
6/18/26, 11:13 PM | Andre [reply]: Thanks for sharing!!
---
6/23/26, 6:28 PM | Stefan: am i tripping or did these trades actually print in premarket spy today?
---
6/23/26, 9:56 PM | Dan [reply]: Ha, tradingview has a weird 6pt candle too, not exactly the same but who knows.. With intraday data each vendor can disagree sometimes, and I have not heard good things about IBs data.
---
6/23/26, 10:05 PM | Stefan [reply]: since i didnt get filled im just gonna assume it was buggy
---
6/23/26, 10:11 PM | Rachit: looks like a buncha stops being triggered on the gap?
---
6/24/26, 7:00 PM | Sam: https://www.cnbc.com/2026/06/23/alphabet-verizon-dow-djia.html
---
6/24/26, 7:00 PM | Sam: Dunno if anything can be done with this info.
---
6/25/26, 6:44 AM | ASlan: Stocks tend to have a 1-2% outsized return for one year relative to their peers when dropped from indexes like spy and russell. But dont know if that would hold true for DOW and honestly not that big of a return bump relative to what we get up to
---
6/30/26, 1:31 AM | deal_me_in: My broker (alpaca) always considers VXX and UVXY hard to borrow. Is that true for IB too?
---
6/30/26, 1:32 AM | deal_me_in: I'm trying the VIX carry strategy but forced to use SVIX
---
6/30/26, 1:38 AM | 4D [reply]: nope, easy to borrow uvxy now
---
6/30/26, 2:56 AM | Robert K [reply]: I'm extreamly new to the group here, I don't know what tradfi trading even is. But for VXX the most economical way to short it is via synthetic options. Get you a leap where you buy the at the money put and sell that at the money call. This will equ[ate to a synthetic short]
---
6/30/26, 2:56 AM | Robert K: I usually make adjustments or add to the position each time VXX pops up.
---
6/30/26, 3:57 AM | Rachit: anyone by chance looked at the moc rebalance trade but on the semis?
---
6/30/26, 4:05 AM | emsin44 [reply]: Tradfi is just short for traditional finance as compared to crypto
---
6/30/26, 4:16 AM | Robert K [reply]: ahhhh, thanks for letting me know!
---
6/30/26, 5:41 AM | deal_me_in [reply]: I'm definitely lost a to how this expresses the carry trade equivalent to shorting vxx
---
6/30/26, 5:48 AM | Rachit: yeah same ....also, wouldn't the borrow be factored into the price of the options?
---
6/30/26, 5:49 AM | llIHeroic: Long put + short call same strike is the synthetic equivalent to short shares. As in the PnL distributions of each position are the same as each other
---
6/30/26, 5:50 AM | llIHeroic: And yes there is an implied borrow rate for the duration priced into the long put + short call. If you have duration you will actually see a decent change in marks as this fluctuates
---
6/30/26, 6:45 AM | Robert K: Yeah you're right, the borrow rate is factored in isn't it. Well I have never had issues getting filled by doing the synthetic. Also easy to roll one of the legs to adjust the risk graph over time. Example here, over time you can offset the drawdown
---
6/30/26, 6:46 AM | Robert K: Old example I had for the VXX trade
---
6/30/26, 9:03 AM | Euan: this is a rough cut/paste of something i wrote about leveraged ETFs and how to factor in borrow. "XXXX" was a placeholder for the 4x ticker which i couldn't find at the time. I think it was SPYU but that isn't really important.
---
6/30/26, 9:03 AM | Euan: should this get a webinar?
---
6/30/26, 11:11 AM | Dan [reply]: Interesting. Maybe not intended but just given me an idea that for one of my long strategy maybe I should be using SSO instead of UPRO for less decay, looks like it has longer history too. A bit less $turnover but still liquid enough for me
---
6/30/26, 4:56 PM | Matt G [reply]: This is a very interesting read. Thanks.
---
6/30/26, 6:02 PM | akhan [reply]: I would like that. If possible may be also shed some light on why sometimes they have huge spreads. For example ITM UVXY 24.5 strike call expiring 2nd July has bid/ask of 1.02/1.60 roughly 36%. To me this looks quite a lot.
---
6/30/26, 6:47 PM | Robert K [reply]: Were these the spreads with the market closed? I'd think they'd tighten up once the market opens.
---
6/30/26, 9:34 PM | akhan: It's 1/1.74 right now. At least on IBKR.
---
6/30/26, 11:20 PM | Sam: Shorting near expiry ITM calls should lead to a short position in $UVXY if you are having problems in borrowing the stock.
---
6/30/26, 11:55 PM | Sam: @Euan end of month/quarter today...calendar effects? Long index futures half hr before close?
