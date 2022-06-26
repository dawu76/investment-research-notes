### Content recap

#### Dispersing dislocations [01:20]
- Getting paid to disperse dislocations that cause asset prices to deviate from "fair value"
- Caused by unpredictable lumpy supply or demand overwhelming available liquidity, causing these deviations
- What service are we getting paid for? To step in and provide liquidity of last resort, pushing prices back toward equilibium
- More apparent in lower liquidity markets

#### Trend effects [01:23]
- An example of a behaviorial effect
- Why do they persist? Trend effects don't appear to be compensation for any useful service. So it seems to be a market anomaly caused by behavioral inefficiencies. Maybe participants are reacting too slow to new info, or there is a feedback effect.
- Traditionally most associated with commodities or crypto.
- Simple representative strategy: go long anything within 5 days of the past-20-day high. Go short anything that has not seen its past 20-day high since 15+ days ago. In other words, based on recency of its highs over a recent period.
- Elevator pitch: "What would cause inefficiency?" Not sure beyond 'behavioral or structural' reasons. "Why wouldn't it be fully absorbed?" Again not clear, other than feedback effects and delayed reaction. "How to harness the edge?" Use some variant of going long/short based on performance over a lookback period.


#### Define rules to take advantage of inefficiencies
- Next concepts: portfolio management, position sizing

---

#### Module 2 questions [01:30]

"How do we track margin usage in a crypto strategy?"
- Do we just record margin usage at start of trade and then track how it changes over the course of the trade?
- Example scenario: Suppose we have $1K USD collateral in crypto account. We have BTC-PERP or perpetual BTC futures trading at premium to spot BTC, and the "funding rate" on this perpetual futures is 20% p.a.
- This means if we put on a "short basis trade", i.e. go short BTC perpetual futures and go long BTC spot, we can earn 20%.
- Suppose we go long 0.008 BTC or $500 and short the equivalent amount in perpetual futures. How does this trade show up in your account balance page (e.g. on FTX)? The page will list your long 0.008 BTC position and a USD position equal to your $1K starting balance - long $BTC cost. This is because your futures position has no "carry value" and the P&L from your short BTC-PERP just gets added/subtracted from your USD account balance.
- The short BTC-PERP trade appears in the "positions" tab as a short trade with a "liquidation price," which means: if BTC price goes to that 'liquidation price', we'll be liquidated out of the position due to us exceeding our margin. But how would we get liquidated if we're long spot and short the equivalent in futures? Because (1) they are NOT guaranteed to move together and (2) only 97.5% of the BTC balance counts as collateral.
- If BTC goes up, our collateral will increase but our losses on the BTC-PERP will also increase. Eventually the losses on the BTC-PERP will exceed the collateral in your account (based on your USD + BTC holdings).
- So any increase in BTC collateral is "mostly" offset by the loss from the perpetual futures position but at a certain BTC price, that residual that is NOT offset will exceed your collateral.
