# RW Pro Discord — #data-analysis raw transcript

- **Period:** June 1–30, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Message count:** 25
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:data-analysis after:2026-05-31 before:2026-07-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact June boundaries. Channel activity was sparse this month — no messages appear before June 10 or after June 28 within the range. A Discord thread ("Impact of volatility drag," started 6/17/26 by deal_me_in, 9 messages) is noted below at its start point but its in-thread replies are not captured by this extraction method (main-channel messages only); the related discussion that continued back in the main channel on 6/26–6/28 is captured in full. Some individual messages are capped at 250 characters by the extraction tooling; these are marked `[capped]` below where the cutoff is mid-sentence.

---

6/10/26, 9:44 PM | deal_me_in: Hey all. In my automated trading system I have added a risk model that prevents trading of any asset with a wide spread. Im currently using the Corwin–Schultz model to estimate the spread using daily highs and lows since that data is easily available.

Anyone have any real world experience using this model?
https://users.nber.org/~confer/2009/mms09/Corwin_Schultz.pdf
---
6/10/26, 11:19 PM | Euan: kind of...
once upon a time i did a lot of work on spreads and market impact. i read this paper but didn't implement it because i found the rule "spread = k*sqrt($trade volume) worked pretty well. but you need a different k for each stock so you can go a bit further and convert it into something which has volatility in it. pg 111 of "volatility trading".
i've never felt the need to revisit the problem (it could be an entire career)
---
6/11/26, 1:11 AM | deal_me_in: Ty. I'll check pg 111!
---
6/11/26, 1:21 AM | deal_me_in: Uh, what's K in that equation?
---
6/11/26, 3:25 AM | Euan: scaling constant. you need to calibrate that to historical data. which is why i use the vol version in the book
---
6/11/26, 5:33 AM | deal_me_in: Pardon my ignorance, but assumedly you're using that to calculate the spread on options prices. Would that work for ETF in Stocks too?
---
6/11/26, (edited) | deal_me_in: Also you talking about equation 4.18? On my kindle that's on page 109
---
6/11/26, 8:06 AM | Euan: Sorry I didn't know kindle was so far off the hard copy in page numbers.

Don't have it with me but it is towards the end of chapter 6. There is a section on estimating transaction costs.

It was meant to be used for stocks and ETFs
---
6/11/26, 8:27 AM | deal_me_in: Oh yeah, 6.22 makes more sense
---
6/17/26, 7:22 PM | deal_me_in started a thread: "Impact of volatility drag" (9 messages — thread replies not captured by this extraction; see note above)
---
6/23/26, 9:46 PM | Rachit: i've been digging through the vix basis and slayer stuff last few days. both of them result in a signal that is a binary on/off switch for going long or short vol (pls correct me if im wrong!).

I did a simple ensemble of both, which somewhat improv [capped]
---
6/23/26, 9:55 PM | robotkris [reply]: This is a hard problem Rachit...

those vol explosions happen infrequently enough that anything that sidesteps one of them can make the performance look a lot better, but beceause the number of observations is small, it's very hard to infer whether [capped]
---
6/23/26, 10:01 PM | Rachit [reply]: ty! ill heed the advice on keeping the position sized relatively small and just eat the variance
---
6/23/26, 10:15 PM | robotkris: I think that sometimes that's as good as it gets. Recognising that is important
---
6/25/26, 8:53 PM | Andre [reply]: I also do this kind of ensemble, trying to combine both signals. I think it does help to smooth the returns. What I think helps as well is to have a flat threshold for the slayer, instead of flipping directly from short to long and vice versa
---
6/25/26, 9:12 PM | Rachit [reply]: Thanks, Andre. Would you mind expanding on the flat threshold? i'm not sure i understand what that means
---
6/25/26, 9:16 PM | Andre [reply]: When you trade the slayer, you choose a certain z-score threshold at which to flip from long to short, like 1.75. You could add a flat range to this: for example, from 1.0 to 1.75 you're not short anymore, you're flat. Make sense?
---
6/25/26, 9:16 PM | Rachit [reply]: ah right on that makes sense. ty!
---
6/26/26, 12:30 AM | deal_me_in: Hey @Euan you mention that shorting UXVY gives you the vol drag edge. I did some analysis that says maybe not? Im probably wrong here but here's what I found...
---
6/26/26, 12:33 AM | deal_me_in: Basically, the "annualized_drag" column attempts to quantify the annualized returns lost to vol drag... so UPRO costs you like 200% a year in vol drag.

If annualized_drag is negative, then the vol drag is actually a vol tailwind. Thats the case f [capped]
---
6/26/26, 12:34 AM | deal_me_in: you can read about this study in the thread above...
---
6/26/26, 8:15 PM | deal_me_in: Ok i figured out how to ask this question… @Euan how would you estimate the annualized returns lost to vol drag for an asset? I can just try it your way and compare it to Claude's way that I used above.
---
6/26/26, 9:04 PM | Euan: I don't know how claude got its ideal return. the way to see the drag is to look at the return on the base product and compare that to the return on the leveraged version. So a 3x ETF should have 3 time the return of the unleveraged. Any underperform [capped]
---
6/26/26, 9:42 PM | robotkris: There's also a good lesson in TLQ Module 1 that goes through volatility drag - I think it's a good one for building up the intuition. But really, it's as simple as Euan suggested - if something goes up then down, the leveraged version will have a mor [capped]
---
6/28/26, 9:06 PM | deal_me_in: OK ok. im gonna stop trying to be smart about it lol. ill just calculate vol drag as variance / 2 and be done with it.

My initial hypothesis, which Euan does mathematically prove in the leveraged etf chapter in vol trading (not that i understand it) is that vol drag won't always make everything go to zero. Things that trend can benefit from vol drag (TMF for example).

What I wanted to see, was if vol drag helped UXVY, which kinda trends down as it incinerates money to zero. But i realize that's dumb.... its trending down, so its just gonna incinerate more money and vol drag is gonna increaee that loss.
