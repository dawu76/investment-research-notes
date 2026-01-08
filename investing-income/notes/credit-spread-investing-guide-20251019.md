# Credit Spread Investing Guide

**A Complete Actionable Guide to Trading Credit Spreads**

---

## Table of Contents

1. [Quick Start Summary](#quick-start-summary)
2. [What Are Credit Spreads?](#what-are-credit-spreads)
3. [The Beginner Strategy](#the-beginner-strategy)
4. [Risk Management Rules](#risk-management-rules)
5. [Managing Active Trades](#managing-active-trades)
6. [Advanced Techniques](#advanced-techniques)
7. [Trading Psychology](#trading-psychology)
8. [Getting Started](#getting-started)

---

## Quick Start Summary

### The Core Strategy

**Trade Setup:**
- Sell options 30-40 days to expiration
- Target 70-80% probability of profit
- Use the shortest width possible (typically 5 points)
- Trade stocks with 30-55% IV and 100K+ option volume

**Risk Management:**
- Never use more than 20% of your account
- Risk no more than 2.5% per trade
- Set stop loss at 50-100% of credit collected
- Take losses immediately when hit

**Expected Results:**
- Win rate: 70-80%+
- Average return: 20-40% per trade
- Monthly compounding potential

---

## What Are Credit Spreads?

### Definition

A credit spread is selling one option and buying another option at a different strike price on the same stock with the same expiration date. You receive money upfront (the "credit") and have defined maximum profit and loss.

### Two Types

#### Put Credit Spread (Bullish)
**When to use:** You think the stock will stay flat or go up

**How it works:**
1. Sell a put option below current price (collect premium)
2. Buy a put option further below (protection)
3. Keep the difference as your credit

**Example:** Microsoft trading at $510
- Sell the $505 put → collect $455
- Buy the $500 put → pay $320
- **Net credit: $135** (you keep this if stock stays above $505)

#### Call Credit Spread (Bearish)
**When to use:** You think the stock will stay flat or go down

**How it works:**
1. Sell a call option above current price (collect premium)
2. Buy a call option further above (protection)
3. Keep the difference as your credit

**Example:** Microsoft trading at $510
- Sell the $515 call → collect $625
- Buy the $520 call → pay $420
- **Net credit: $205** (you keep this if stock stays below $515)

### Calculating Max Profit & Loss

**Max Profit:**
```
Max Profit = Total Credit Collected
```
This is what you keep if the stock stays outside your short strike.

**Max Loss:**
```
Max Loss = (Strike Width × 100) - Credit Collected

Example:
5-point spread, $120 credit collected
Max Loss = ($5 × 100) - $120 = $500 - $120 = $380
```

**Break-Even Point:**
```
Put Spread: Short Strike - (Credit ÷ 100)
Call Spread: Short Strike + (Credit ÷ 100)
```

---

## The Beginner Strategy

Follow these four variables to set up high-probability trades.

### Variable #1: Days to Expiration (DTE)

**RULE: Sell options 30-40 days to expiration**

**Why this matters:**
- Options decay faster in the 30-45 day window (theta acceleration)
- You can sell TWO 30-day spreads and collect more premium than ONE 70-day spread
- Don't waste time on longer-dated options

**Action:** When opening a trade, select the expiration date 30-40 days out.

---

### Variable #2: Strike Price Selection

**RULE: Target 70-80% Probability of Profit (POP)**

**How to find it:**
- Look at your broker's "Probability of Profit" or "Delta" column
- Select strikes that show 70-80% (or 0.70-0.80 delta)
- This represents about 1 standard deviation out-of-the-money

**The Trade-off:**

| Strike Distance | POP | Credit | Risk |
|----------------|-----|--------|------|
| Closer to stock price | 60% | Higher ($160) | Higher |
| Medium distance | 70% | Medium ($115) | Medium |
| Further away | 80% | Lower ($76) | Lower |

**Action:** Use 70-80% POP as your baseline. This balances probability of winning with meaningful premium.

---

### Variable #3: Width Between Strikes

**RULE: Use the shortest width available**

**Why shorter is better:**
- Better return on investment (ROI)
- Example comparison:
  - 5-point spread: $76 credit / $424 risk = **18% ROI**
  - 10-point spread: $104 credit / $896 risk = **11.6% ROI**

**Strategy:** Sell two 5-point spreads instead of one 10-point spread to double your return.

**Action:** Start with 5-point spreads ($5 difference between your strikes). As you gain experience, you can adjust.

---

### Variable #4: Stock Selection

**RULE: Find liquid stocks with moderate volatility**

**Two Key Criteria:**

1. **High Liquidity**
   - Option volume: 100K+ daily
   - Ensures you can enter and exit easily
   - Tighter bid-ask spreads

2. **Moderate Implied Volatility (IV)**
   - Sweet spot: 30-55% IV
   - Below 30%: Not worth the time (premiums too low)
   - Above 55%: Too volatile, hard to manage emotionally

**How to Screen:**
- Use your broker's stock screener
- Set filters:
  - Option IV: 30-55% (or 0.30-0.55)
  - Option volume: 100,000+
- Look for stable, predictable companies

**Good Examples:**
- S&P 500 index (SPY/SPX)
- Microsoft
- Meta
- Nvidia (when trending)
- Taiwan Semiconductor (TSMC)

**Stocks to Avoid:**
- Tesla (too erratic)
- AMD (high whipsaw)
- Anything with "roller coaster" moving averages

---

### Opening Your First Trade (Step-by-Step)

**Example: Opening a Put Credit Spread**

1. **Find a stock** using your screener (30-55% IV, 100K+ volume)
   - Example: Nvidia

2. **Go to the options chain**

3. **Select expiration date** 30-32 days out

4. **Find your strike prices:**
   - Look for 70-80% POP in the delta/probability column
   - Example: $170 put shows 76% POP

5. **Build the spread:**
   - Sell the $170 put (higher strike)
   - Buy the $165 put (lower strike, protection)
   - This creates a 5-point spread

6. **Check the credit:**
   - Look at bid ($98) and ask ($106)
   - Aim for mid-price (~$102)

7. **Enter your order:**
   - Select "Buy" (even though it's a credit, the order type is "buy")
   - Set quantity (start small: 1-5 contracts)
   - Set limit price at mid-point
   - Submit order

8. **Verify you received credit:**
   - You should immediately receive money in your account
   - Example: $102 per spread × contracts

**Outcome:**
- If Nvidia stays above $170 on expiration → Keep full $102 credit
- If Nvidia falls below $165 → Max loss of $398
- Break-even: $168.98 ($170 - $1.02)

---

## Risk Management Rules

These rules are **non-negotiable**. They protect you from catastrophic losses.

### Rule #1: Account Allocation

**NEVER use more than 20% of your account for credit spreads**

**Why:**
- Using 100% = emotional disaster
- Account swings cause fear and greed to take over
- You won't follow your rules under extreme stress

**Action:**
```
Maximum Allowance = Total Account × 20%

Example:
$10,000 account → $2,000 max for credit spreads
$50,000 account → $10,000 max
```

**Conservative approach:** Start with 5-10% of your account.

---

### Rule #2: Risk Per Trade

**NEVER risk more than 2.5% of your allowance per trade**

**Why:**
- You can lose 40 trades in a row before depleting your allowance
- Prevents single-trade wipeout
- Builds cushion for learning

**Action:**
```
Max Risk Per Trade = Allowance × 2.5%

Example:
$10,000 allowance → $250 max risk per trade
$2,000 allowance → $50 max risk per trade
```

**What this means:**
- If you collect $100 credit with 100% stop loss, your max risk = $100
- This means you can only open trades where credit × 2 ≤ max risk per trade

---

### Rule #3: Set Stop Losses Immediately

**NEVER risk more than you can make**

**The 100% Stop Loss Rule:**
- If you collect $100 credit, exit when the spread reaches $200 value
- Your loss: $200 - $100 initial credit = $100 max loss
- Risk = Reward (minimum 1:1 ratio)

**Example:**
- Opened spread, collected $120 credit
- Stop loss: Exit when spread value hits $240
- Final loss: $240 - $120 = $120

**Action:** Set price alerts or good-til-cancelled (GTC) orders at your stop loss level immediately after opening.

---

## Managing Active Trades

Once your trade is open, active management determines your success.

### Dynamic Stop Loss System

As your trade becomes profitable, move your stop loss to lock in gains.

**Progression:**

| Your Profit | Spread Value | New Stop Loss | Locked Profit |
|-------------|--------------|---------------|---------------|
| 0% | $100 (initial) | $200 | -$100 to $0 |
| 50% | $50 | $100 | $0 (break-even) |
| 75% | $25 | $50 | $50 |
| 87.5% | $12.50 | $25 | $75 |

**How it works:**

**At 50% profit:**
- You're up $50 (spread now worth $50 vs $100 initial)
- Move stop loss to break-even ($100)
- If trade reverses to $100, you exit with $0 loss
- Protects you from turning a winner into a loser

**At 75% profit:**
- You're up $75 (spread now worth $25)
- Move stop to $50
- Locks in minimum $50 profit

**At 87.5% profit:**
- You're up $87.50 (spread worth $12.50)
- Move stop to $25
- Locks in minimum $75 profit

**Why this works:**
- Continuously protects gains
- Gives room for minor reversals (doesn't stop you out too early)
- Automates decisions (removes emotion)
- Some trades will reverse and stop out (acceptable trade-off)

---

### The Two Critical Rules

**Rule #1: Never Let a Winner Become a Loser**

**The problem:**
- Trade is up $50 (winning)
- You feel great (euphoria)
- Market reverses, spread back to $100 (break-even)
- You think: "It was winning before, it'll come back"
- You refuse to exit
- Eventually take a large loss

**The solution:**
- When you reach 50% profit → Move stop to break-even
- If it hits break-even → Exit, no exceptions
- You protected yourself from losing money on a winning trade

---

**Rule #2: Never Risk More Than You Can Make**

**The problem:**
- Collect $100 credit
- Trade goes against you
- Spread now worth $300
- You're down $200
- "Maybe it'll reverse..." (it often doesn't)
- End up with max loss of $400

**The solution:**
- Set initial stop at 100% of credit
- If spread reaches $200 → Exit immediately
- Your loss = $100 (same as your potential gain)
- 1:1 risk-reward minimum

---

### When to Close or Roll Trades

#### Taking Profits: The Checkpoint System

**Checkpoint #1: 50% Time Remaining**
- Example: Opened 4-week spread, now 2 weeks left
- Question: Am I up 75%+ profit?
  - **YES** → Consider rolling out to collect more premium
  - **NO** → Keep holding (theta accelerates in final 2 weeks)

**Checkpoint #2: 25% Time Remaining**
- Example: Opened 4-week spread, now 1 week left
- Question: Am I up 90%+ profit?
  - **YES** → Consider rolling out
  - **NO** → Let it ride to expiration

**Why these checkpoints:**
- 50% time left but only 25% profit = inefficient (wasting time)
- 75% profit already collected = risking a lot for little remaining gain
- Better to roll out and start fresh theta decay

---

#### How to Roll a Trade

**Rolling Out (Extend Time):**
1. Close your current spread
2. Open a new spread at a later expiration date
3. Collect additional credit (more time = more premium)

**Example:**
- Current: TSMC 260/265 put, 14 days left, up 70%
- Roll to: Same 260/265 put, 28 days out
- Collect: ~$25 additional credit

**Rolling Up (Adjust Strike - For Profitable Trades):**
1. Close current spread
2. Open new spread at higher strikes (stock moved favorably)
3. Collect credit (closer to money + more time)

**Example:**
- Stock moved from $510 to $530
- Roll from 260/265 to 270/275
- Collect $65 credit

**CRITICAL RULE: Never roll if you have to pay a debit**

If rolling requires paying money, close the trade instead. Don't reduce your profit potential chasing a losing position.

---

#### How to Close a Trade

**Steps:**
1. Find your position in your broker platform
2. Click "Close Position"
3. You're doing the reverse:
   - Buy back the option you sold
   - Sell the option you bought
4. Check the bid-ask spread
5. Aim for mid-price
6. Submit order

**When to close:**
- Stop loss hit (exit immediately)
- Target profit reached
- Week before earnings (if holding a spread)
- Short leg goes in-the-money (avoid assignment)

---

## Advanced Techniques

### Using Technical Analysis

Technical analysis increases your win rate beyond the baseline 70-80%.

#### Finding Predictable Stocks

**What to look for:**
- **Smooth moving averages** (not roller coasters)
- **Clear trends** (obvious upswings and downswings)
- **Respects support/resistance** (predictable bounces)

**Moving Average Setup:**
- 20-period MA (short-term trend)
- 50-period MA (medium-term trend)
- 200-period MA (long-term support/resistance)

**Good stock characteristics:**
- Moving averages have stable, consistent slopes
- 200 MA trends upward over time
- Price respects these levels

**Examples of predictable stocks:**
- S&P 500 (SPY)
- Microsoft
- Lockheed Martin
- TSMC

**Examples of unpredictable stocks to avoid:**
- Tesla (erratic movements)
- AMD (frequent whipsaws)

---

#### Selling at Support Levels

**The Strategy:**
Sell put credit spreads when stock touches major support.

**Key support levels:**
- 200-period moving average (strongest)
- 50-period moving average
- Historical price support zones
- Major psychological levels

**Why this works:**
- Buyers historically step in at support
- Your directional bet (up or flat) has better odds
- IV often spikes at support (more premium for you)

**Action:**
1. Identify stock with clean moving averages
2. Wait for price to touch 200 MA support
3. Confirm bounce is starting (don't catch falling knife)
4. Sell put credit spread with 30-40 DTE
5. Ride the bounce upward

---

#### Implied Volatility (IV) Crush Strategy

**The Concept:**
- IV = Market's expectation of future movement
- When stock reaches support/resistance → IV spikes (uncertainty)
- When stock moves away from that level → IV drops
- You profit from BOTH the directional move AND the IV drop

**How to execute:**

1. **Identify IV spike zones:**
   - Support levels
   - Resistance levels
   - Major moving averages
   - Earnings announcements

2. **Wait for stock to enter the zone:**
   - IV will be elevated (options priced higher)
   - More uncertainty = more premium

3. **Sell your credit spread:**
   - Collect elevated premium
   - Target your normal 70-80% POP

4. **Profit from two factors:**
   - Stock moves away from the zone (directional profit)
   - IV contracts (volatility profit)

**Real Example: Microsoft August 5**
- Stock fell to $394 (support level)
- IV spiked to 38% (normally 18%)
- Sold 395/390 put spread for $250 (very high premium)
- Next day: Stock at $404, IV dropped to 29%
- Spread value: $162
- **Profit: $88 in one day (35% gain)**

---

### Earnings Trading Strategy

**The Opportunity:**
- IV spikes dramatically before earnings
- Market tends to OVERESTIMATE the move
- Can collect massive premiums

**The Rule:**
- **OPEN spreads** the week of earnings (sell 4 weeks out before announcement)
- **CLOSE spreads** the week before earnings (if already holding)

**Ideal Setup:**
1. Stock at major support level (e.g., 200 MA)
2. Earnings approaching (IV elevated)
3. Technical structure suggests buyers will step in

**Why this works:**
- Technical edge (support likely holds)
- IV edge (market overestimates move)
- Even if earnings disappoint, support absorbs selling

**Action:** Only trade earnings when you have BOTH technical support AND elevated IV.

---

### Call Credit Spreads (Use Sparingly)

**The Reality:**
- Market trends up most of the time
- Call spreads fight the natural trend
- Market underprices call risk (you get less reward for more risk)

**When to use (only 10-20% of trades):**

**Situation #1: Confirmed Downtrend**

Requirements:
- Identify clear trend reversal
- Look for bearish patterns:
  - Bearish engulfing candle
  - Evening star pattern
  - Break below major support
- Enter quickly, exit quickly (downtrends move faster)

**Situation #2: Iron Condors** (see below)

**Key Difference:**
- Put spreads: Can hold longer, ride extended uptrends
- Call spreads: Take profit quickly, don't overstay

**Recommendation:** Focus 80-90% of your trades on put credit spreads.

---

### Iron Condors

**Definition:**
Selling BOTH a put spread and call spread on the same stock, same expiration.

**Traditional Approach (NOT Recommended):**
- Open both spreads simultaneously
- Problem: If in uptrend, call spread likely loses, cutting your profit in half

**Recommended Sequential Approach:**

**Step 1:** Open put spread first
- Example: Stock at $185
- Sell 185/180 put spread
- Collect $100

**Step 2:** Wait for favorable movement
- 14 days pass
- Stock moves to $220
- Put spread mostly decayed (nearly max profit)

**Step 3:** Now sell call spread
- With 14 days left
- Sell 230/235 call spread (far out-of-the-money)
- Collect $50 additional

**Step 4:** If market reverses
- Stock comes back to $208
- **Win on BOTH sides:**
  - Put spread: $100
  - Call spread: $50
  - **Total: $150** (50% more than put alone)

**Why this works:**
- Put spread already nearly guaranteed to win
- Can sell call spread much higher (more room for error)
- Conservative call spread = high probability both win

---

## Trading Psychology

Your emotional control determines your success more than strategy knowledge.

### The Three Psychological Traps

#### Trap #1: Loss Aversion

**The Research:**
- Humans feel pain of loss 2X MORE than joy of winning
- $100 loss hurts 2X more than $100 gain feels good
- Option sellers are often more risk-averse (loss hits harder)

**How it affects you:**
- Hit stop loss on a trade
- Don't want to accept the loss
- Keep rolling out, hoping for recovery
- Small loss becomes catastrophic

**The Solution:**
- Accept that losses are part of trading
- Set stop loss before opening trade
- When hit → Exit immediately, no negotiation
- Move on to next opportunity

---

#### Trap #2: Disposition Effect

**The Pattern:**
- Hold losing trades too long (don't want to realize loss)
- Cut winning trades too early (fear of losing unrealized gains)

**Example:**
- Trade is losing, down 50%
- "I don't want to take the loss, maybe it'll recover"
- Keep holding, ends up max loss
- Trade is winning, up 75%
- "Better take profit now before it reverses"
- Exit early, miss remaining gains

**The Solution:**
- Use systematic stop losses (removes emotion)
- Use profit checkpoints (removes emotion)
- Follow your rules, not your feelings

---

#### Trap #3: The Winning Streak Trap

**The Pattern:**
1. Win 7 trades in a row (70-80% win rate working)
2. Feel invincible, "on a hot streak"
3. Size up next trade: 2.5% → 10%
4. That trade loses
5. Wipes out multiple previous wins

**The Solution:**
- **Never** increase position size due to winning streak
- Stick to 2.5% risk per trade always
- Past wins don't predict future wins
- Consistency beats home runs

---

### The Best Losers Are the Best Winners

**Key Insight:**
"The main difference between me now and four years ago: I am now a much better loser."

**What separates good traders:**
- Not better technical knowledge
- Not better stock picking
- **Ability to take losses and move on**

**The Mindset:**
- Losses are data points, not personal failures
- Cut losses quickly (they're just numbers)
- Move to next trade with clear head
- Focus on process, not individual outcomes

**Action:** Practice taking losses in paper trading until it becomes mechanical, not emotional.

---

### Profit vs Risk Math

Understanding win rate vs loss size:

**Bad Trader (70% Win Rate):**
- Win: $100 × 7 times = $700
- Lose: $400 × 3 times = -$1,200
- **Net: -$500 (LOSING despite 70% win rate!)**

**Beginner Strategy (80% Win Rate):**
- Win: $120 × 4 times = $480
- Lose: $380 × 1 time = -$380
- **Net: +$100 (barely profitable)**

**Elite Trader (70% Win Rate + Loss Management):**
- Win: $120 × 7 times = $840
- Lose: $60 × 3 times = -$180 (exit at 50% stop)
- **Net: +$660 (THIS IS THE GOAL)**

**The Lesson:** Managing losers matters MORE than maximizing winners.

---

### Practical Mindset Tips

**1. Don't Compare Yourself to Others**
- Everyone at different life stage
- Different capital, experience, circumstances
- "Comparison is the thief of joy"
- Only compare yourself to yourself

**2. Set Realistic Expectations**
- Average 20% per trade is EXCELLENT
- 30-40% annualized returns = better than most hedge funds
- Don't reach for unrealistic gains

**3. Journal Your Trades**
- Record all trades (entry, exit, P&L)
- Note what you learned
- Note emotional state during trade
- Review monthly to identify patterns

**4. Be Kind to Yourself**
- Credit spreads are complicated
- You WILL make mistakes
- Mistakes are part of learning
- Celebrate progress, not perfection

---

## Getting Started

### Step 1: Get Options Approval

**Check your brokerage requirements:**

**Fidelity:**
- Need **Tier 2** options approval
- Allows spreads (up to 4 legs)

**Interactive Brokers (IBKR):**
- Need **Level 3**
- Covers short call spreads + short put spreads

**Robinhood:**
- Need **margin account**
- Need **Level 3 options trading**

**Action:** Apply for appropriate options level in your broker settings.

---

### Step 2: Paper Trade First

**CRITICAL: Do NOT skip paper trading**

**Why paper trading matters:**
- Credit spreads are complex
- Need to understand mechanics
- Most important: Practice emotional control

**How to paper trade correctly:**
- **Trade like it's real money**
- Track every trade seriously
- Feel the emotions (wins/losses)
- Follow your rules strictly
- Practice taking losses (this is the hardest part)

**Duration:** Paper trade until you:
- Understand all mechanics
- Can follow rules without exception
- Can take losses without emotional reaction
- Have 20+ trades recorded

---

### Step 3: Start Small with Real Money

**Your first real trades:**
- Start with 1-2 contracts maximum
- Use 5% of your account (even if you allow 20%)
- Follow the beginner strategy exactly:
  - 30-40 DTE
  - 70-80% POP
  - 5-point spreads
  - 100% stop loss

**Expect emotional difference:**
- Real money feels VERY different than paper trading
- You will feel fear and greed more strongly
- This is normal
- Stick to your rules even more strictly

---

### Step 4: Build Your Stock Watchlist

**Create a screener:**
- IV: 30-55%
- Option volume: 100K+
- Focus on stable, predictable stocks

**Analyze charts:**
- Look for smooth moving averages
- Identify support levels (especially 200 MA)
- Avoid erratic stocks

**Build a list of 10-15 stocks you'll trade regularly**

---

### Step 5: Develop Your Routine

**Weekly:**
- Review stock watchlist
- Identify stocks at support levels
- Check IV levels
- Look for setup opportunities

**Daily:**
- Check open positions
- Monitor stop loss levels
- Adjust stops if profit targets hit
- Look for new opportunities

**After each trade:**
- Journal the trade
- Note what worked/didn't work
- Update your statistics (win rate, avg win/loss)
- Identify lessons learned

---

## Quick Reference Guide

### The Beginner Checklist

**Before Opening a Trade:**
- [ ] Stock IV between 30-55%
- [ ] Option volume >100K
- [ ] Chart shows clean, predictable trend
- [ ] At or near support level (for puts)
- [ ] DTE set to 30-40 days
- [ ] Strike selected for 70-80% POP
- [ ] Using 5-point width
- [ ] Risk ≤2.5% of allowance
- [ ] Total allocation ≤20% of account

**After Opening:**
- [ ] Set stop loss at 100% of credit
- [ ] Document trade in journal
- [ ] Set price alerts

**Active Management:**
- [ ] Check daily
- [ ] At 50% profit → Move stop to break-even
- [ ] At 75% profit → Move stop to 50% credit
- [ ] At 50% time remaining → Check if 75% profit
- [ ] At 25% time remaining → Check if 90% profit
- [ ] Week before earnings → Close position

**At Exit:**
- [ ] Record final P&L
- [ ] Journal lessons learned
- [ ] Update statistics

---

### Key Formulas

**Max Profit:**
```
Max Profit = Total Credit Collected
```

**Max Loss:**
```
Max Loss = (Strike Width × 100) - Total Credit
Example: ($5 × 100) - $120 = $380
```

**Break-Even (Put Spread):**
```
Break-Even = Short Strike - (Credit ÷ 100)
Example: $505 - ($120 ÷ 100) = $503.80
```

**Break-Even (Call Spread):**
```
Break-Even = Short Strike + (Credit ÷ 100)
Example: $515 + ($190 ÷ 100) = $516.90
```

**Return on Risk:**
```
ROI = Credit ÷ Max Loss
Example: $100 ÷ $400 = 25%
```

**Max Risk Per Trade:**
```
Max Risk = Allowance × 2.5%
Example: $10,000 × 0.025 = $250
```

---

### Common Mistakes to Avoid

1. Using too much of your account (>20%)
2. Risking too much per trade (>2.5%)
3. Not setting stop losses
4. Refusing to take losses (hoping for recovery)
5. Rolling for a debit (paying to roll)
6. Holding through earnings
7. Trading volatile, unpredictable stocks
8. Not paper trading first
9. Sizing up after wins
10. Not journaling trades

---

## Final Wisdom

### The Core Principles

**1. Trade to Risk, Not to Profit**
- Don't think: "I can make $10,000!"
- Think: "Can I afford to lose $2,000?"
- Risk management comes first, always

**2. Managing Losers > Maximizing Winners**
- Taking small losses protects your capital
- One large loss can wipe out many wins
- Exit at your stop loss, no exceptions

**3. Consistency Beats Home Runs**
- 20% per trade is excellent
- Compound consistently over time
- Don't overreach for unrealistic gains

**4. Emotional Control Is Everything**
- "Fear and greed will dictate your actions"
- Set rules when calm, follow when stressed
- The best losers are the best winners

**5. Simple and Repeatable**
- Complex strategies are hard to follow
- Simple rules are easier to maintain
- Consistency requires repeatability

---

### Your Path Forward

**Month 1-2: Learning**
- Paper trade extensively
- Learn mechanics
- Practice taking losses
- Build emotional tolerance

**Month 3-4: Small Real Trades**
- Start with 1-2 contracts
- Follow beginner strategy exactly
- Journal everything
- Focus on process, not results

**Month 5-6: Building Confidence**
- Gradually increase size (within 2.5% rule)
- Develop your watchlist
- Refine your entries with technical analysis
- Track your statistics

**Month 7+: Developing Your Style**
- Adapt strategies to your personality
- Find what works for you
- Stay within risk management rules
- Continuously improve through journaling

---

### Remember

"Credit spreads allowed me to compound wealth while working 9-to-5 and enabled early retirement. Without learning credit spreads, I probably wouldn't have been able to quit my job."

**You can do this.**
- Start small
- Follow the rules
- Take losses quickly
- Stay consistent
- Let compounding work

Good luck on your credit spread journey.

---

*This guide is based on real trading experience and represents one successful approach to credit spreads. Always do your own research, understand the risks, and never trade with money you can't afford to lose. Past performance doesn't guarantee future results.*