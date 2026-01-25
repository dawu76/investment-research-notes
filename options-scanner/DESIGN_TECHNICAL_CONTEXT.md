# Design: Price & Technical Context for Strike Selection

**Date:** 2026-01-25
**Status:** Proposed
**Goal:** Add technical analysis context to help identify put strikes slightly below key support levels while maintaining decent premium/strike ratios

---

## Table of Contents

1. [Overview](#overview)
2. [User Workflow](#user-workflow)
3. [Data Model](#data-model)
4. [Support Level Detection](#support-level-detection)
5. [Strike Selection Algorithm](#strike-selection-algorithm)
6. [Integration with Scanner](#integration-with-scanner)
7. [CLI Interface](#cli-interface)
8. [Output Format](#output-format)
9. [Implementation Plan](#implementation-plan)
10. [Testing Strategy](#testing-strategy)

---

## Overview

### Problem Statement

When selling puts conservatively, traders want strikes that:
1. Are **below key support levels** (reduces assignment risk)
2. Still offer **attractive premiums** relative to the strike price
3. Have acceptable **probability of profit** (low delta)

The current scanner selects strikes using a simple offset from ATM, which doesn't consider price structure or support/resistance levels.

### Solution

Add a `TechnicalContext` module that:
1. Fetches historical price data (6-12 months)
2. Calculates technical indicators (SMAs, 52-week range)
3. Identifies support levels using multiple methods
4. Enables strike selection relative to support levels
5. Displays technical context alongside options data

---

## User Workflow

### Before (Current)
```
User runs scanner → Gets strikes at fixed offset from ATM →
Must manually check charts for support levels → Decides on strike
```

### After (Proposed)
```
User runs scanner with --show-technicals →
Sees support levels for each symbol →
Scanner suggests strikes at/below support →
User sees premium % at support-based strikes →
Makes informed decision with full context
```

### Example Usage
```bash
# Show technical context and suggest strikes near support
python -m options_scanner \
  --symbols AAPL MSFT NVDA \
  --show-technicals \
  --strike-method support \
  --support-buffer 2.0 \    # 2% below support
  --min-annual 20
```

---

## Data Model

### New Class: `TechnicalContext`

```python
from dataclasses import dataclass
from typing import List, Optional
import numpy as np

@dataclass
class SupportLevel:
    """Represents a price support level."""
    price: float
    strength: str          # 'strong', 'moderate', 'weak'
    source: str            # 'swing_low', 'volume_profile', 'round_number', 'sma'
    touches: int           # Number of times price bounced from this level
    last_tested: str       # Date last tested (YYYY-MM-DD)
    distance_pct: float    # Current distance from price (%)


@dataclass
class TechnicalContext:
    """Technical analysis context for a symbol."""
    symbol: str
    current_price: float

    # 52-Week Range
    high_52w: float
    low_52w: float
    range_percentile: float    # 0-100, where in 52w range (0=at low, 100=at high)

    # Moving Averages
    sma_20: float
    sma_50: float
    sma_200: float
    price_vs_sma20: float      # % above/below SMA20
    price_vs_sma50: float      # % above/below SMA50
    price_vs_sma200: float     # % above/below SMA200

    # Volatility
    iv_rank: Optional[float]   # 0-100, current IV vs 52w range (if available)
    hv_20: float               # 20-day historical volatility (annualized %)
    atr_14: float              # 14-day Average True Range
    atr_percent: float         # ATR as % of price

    # Support Levels (sorted by proximity to current price)
    support_levels: List[SupportLevel]

    # Derived Metrics
    nearest_support: Optional[SupportLevel]
    suggested_put_strike: Optional[float]   # Strike at/below nearest support

    def to_dict(self) -> dict:
        """Convert to dictionary for DataFrame integration."""
        return {
            'symbol': self.symbol,
            'price': self.current_price,
            '52w_high': self.high_52w,
            '52w_low': self.low_52w,
            '52w_percentile': self.range_percentile,
            'sma_20': self.sma_20,
            'sma_50': self.sma_50,
            'sma_200': self.sma_200,
            'iv_rank': self.iv_rank,
            'hv_20': self.hv_20,
            'atr_pct': self.atr_percent,
            'nearest_support': self.nearest_support.price if self.nearest_support else None,
            'support_strength': self.nearest_support.strength if self.nearest_support else None,
            'suggested_strike': self.suggested_put_strike,
        }
```

---

## Support Level Detection

### Algorithm Overview

Support levels are identified using multiple complementary methods, then consolidated:

```
┌─────────────────────────────────────────────────────────────────┐
│                    SUPPORT DETECTION PIPELINE                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Historical Data (6-12 months)                                  │
│         │                                                       │
│         ▼                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Swing Lows   │  │ Volume       │  │ Round        │          │
│  │ Detection    │  │ Profile      │  │ Numbers      │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
│         │                 │                 │                   │
│         ▼                 ▼                 ▼                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ SMA Support  │  │ Fibonacci    │  │ Historical   │          │
│  │ (50/200)     │  │ Retracements │  │ Clusters     │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
│         │                 │                 │                   │
│         └────────────┬────┴─────────────────┘                   │
│                      ▼                                          │
│              ┌──────────────┐                                   │
│              │  Consolidate │                                   │
│              │  & Rank      │                                   │
│              └──────┬───────┘                                   │
│                     ▼                                           │
│              Final Support Levels                               │
│              (sorted by strength)                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Method 1: Swing Low Detection (Primary)

Identifies local price minima where price reversed upward.

```python
def find_swing_lows(df: pd.DataFrame, window: int = 5) -> List[dict]:
    """
    Find swing lows (local minima) in price data.

    A swing low is a candle whose low is lower than the lows of
    `window` candles on both sides.

    Args:
        df: DataFrame with 'Low', 'High', 'Close', 'Volume' columns
        window: Number of candles on each side to compare

    Returns:
        List of swing low dictionaries with price, date, strength
    """
    swing_lows = []
    lows = df['Low'].values

    for i in range(window, len(lows) - window):
        current_low = lows[i]

        # Check if this is a local minimum
        left_higher = all(lows[i-j] >= current_low for j in range(1, window+1))
        right_higher = all(lows[i+j] >= current_low for j in range(1, window+1))

        if left_higher and right_higher:
            # Calculate strength based on depth and volume
            depth = (df['High'].iloc[i-window:i+window].max() - current_low) / current_low
            volume_ratio = df['Volume'].iloc[i] / df['Volume'].iloc[i-window:i+window].mean()

            strength = 'weak'
            if depth > 0.05 and volume_ratio > 1.2:
                strength = 'strong'
            elif depth > 0.03 or volume_ratio > 1.0:
                strength = 'moderate'

            swing_lows.append({
                'price': round(current_low, 2),
                'date': df.index[i].strftime('%Y-%m-%d'),
                'strength': strength,
                'source': 'swing_low',
                'depth': depth,
            })

    return swing_lows
```

### Method 2: Support Clusters (Multiple Touches)

Groups nearby swing lows to find price levels tested multiple times.

```python
def cluster_support_levels(swing_lows: List[dict],
                          tolerance_pct: float = 1.5) -> List[SupportLevel]:
    """
    Cluster nearby swing lows into support zones.

    Args:
        swing_lows: List of swing low dictionaries
        tolerance_pct: Maximum % difference to consider same level

    Returns:
        Consolidated support levels with touch counts
    """
    if not swing_lows:
        return []

    # Sort by price
    sorted_lows = sorted(swing_lows, key=lambda x: x['price'])
    clusters = []
    current_cluster = [sorted_lows[0]]

    for low in sorted_lows[1:]:
        cluster_avg = np.mean([l['price'] for l in current_cluster])

        # Check if within tolerance of current cluster
        if abs(low['price'] - cluster_avg) / cluster_avg * 100 <= tolerance_pct:
            current_cluster.append(low)
        else:
            # Save current cluster and start new one
            clusters.append(current_cluster)
            current_cluster = [low]

    clusters.append(current_cluster)  # Don't forget last cluster

    # Convert clusters to SupportLevel objects
    support_levels = []
    for cluster in clusters:
        avg_price = np.mean([l['price'] for l in cluster])
        touches = len(cluster)

        # Strength based on number of touches
        if touches >= 3:
            strength = 'strong'
        elif touches >= 2:
            strength = 'moderate'
        else:
            strength = 'weak'

        # Find most recent test date
        last_tested = max(l['date'] for l in cluster)

        support_levels.append(SupportLevel(
            price=round(avg_price, 2),
            strength=strength,
            source='swing_low_cluster',
            touches=touches,
            last_tested=last_tested,
            distance_pct=0.0  # Will be calculated later
        ))

    return support_levels
```

### Method 3: Moving Average Support

SMAs often act as dynamic support during uptrends.

```python
def get_sma_support(current_price: float,
                    sma_50: float,
                    sma_200: float) -> List[SupportLevel]:
    """
    Identify SMAs that may act as support (when price is above them).
    """
    sma_supports = []

    # SMA 50 support (if price is above it)
    if current_price > sma_50:
        distance = (current_price - sma_50) / current_price * 100
        if distance < 15:  # Only relevant if within 15%
            sma_supports.append(SupportLevel(
                price=round(sma_50, 2),
                strength='moderate',
                source='sma_50',
                touches=0,  # N/A for dynamic support
                last_tested='dynamic',
                distance_pct=distance
            ))

    # SMA 200 support (if price is above it)
    if current_price > sma_200:
        distance = (current_price - sma_200) / current_price * 100
        if distance < 25:  # Only relevant if within 25%
            sma_supports.append(SupportLevel(
                price=round(sma_200, 2),
                strength='strong',  # 200 SMA is major support
                source='sma_200',
                touches=0,
                last_tested='dynamic',
                distance_pct=distance
            ))

    return sma_supports
```

### Method 4: Round Number Support

Psychological price levels (e.g., $100, $150, $200).

```python
def get_round_number_support(current_price: float,
                             lookback_pct: float = 15) -> List[SupportLevel]:
    """
    Identify round numbers below current price that may act as support.

    Round numbers: $10 intervals for <$100, $25 for $100-500, $50 for $500+
    """
    supports = []

    # Determine interval based on price
    if current_price < 100:
        interval = 10
    elif current_price < 500:
        interval = 25
    else:
        interval = 50

    # Find round numbers below current price
    lower_bound = current_price * (1 - lookback_pct / 100)
    round_num = (current_price // interval) * interval

    while round_num >= lower_bound:
        distance = (current_price - round_num) / current_price * 100

        # Stronger support at major round numbers
        is_major = (round_num % 100 == 0) or (round_num % 50 == 0 and current_price >= 200)

        supports.append(SupportLevel(
            price=round_num,
            strength='moderate' if is_major else 'weak',
            source='round_number',
            touches=0,
            last_tested='psychological',
            distance_pct=distance
        ))

        round_num -= interval

    return supports
```

### Consolidation: Merge All Support Levels

```python
def consolidate_support_levels(
    swing_supports: List[SupportLevel],
    sma_supports: List[SupportLevel],
    round_supports: List[SupportLevel],
    current_price: float,
    max_distance_pct: float = 15
) -> List[SupportLevel]:
    """
    Merge support levels from all sources, remove duplicates,
    and rank by relevance.
    """
    all_supports = swing_supports + sma_supports + round_supports

    # Update distance_pct for all
    for support in all_supports:
        support.distance_pct = (current_price - support.price) / current_price * 100

    # Filter: only supports below current price and within max distance
    valid_supports = [
        s for s in all_supports
        if 0 < s.distance_pct <= max_distance_pct
    ]

    # Remove duplicates (within 1% of each other)
    consolidated = []
    for support in sorted(valid_supports, key=lambda x: x.distance_pct):
        is_duplicate = any(
            abs(support.price - existing.price) / existing.price * 100 < 1
            for existing in consolidated
        )
        if not is_duplicate:
            consolidated.append(support)

    # Sort by proximity (nearest first)
    consolidated.sort(key=lambda x: x.distance_pct)

    # Boost strength if multiple sources agree
    # (implementation: check for nearby levels from different sources)

    return consolidated[:5]  # Return top 5 most relevant
```

---

## Strike Selection Algorithm

### Mode 1: Support-Based Strike Selection (New Default for Put Selling)

```python
def select_put_strike_near_support(
    available_strikes: List[float],
    support_levels: List[SupportLevel],
    current_price: float,
    buffer_pct: float = 2.0,           # How far below support
    min_premium_pct: float = 0.5,      # Minimum premium as % of strike
    options_chain: pd.DataFrame = None  # For premium lookup
) -> dict:
    """
    Select optimal put strike based on support levels.

    Strategy: Find strike at or slightly below nearest strong support
    that still offers acceptable premium.

    Args:
        available_strikes: List of available put strikes
        support_levels: Sorted support levels (nearest first)
        current_price: Current stock price
        buffer_pct: Desired % below support level
        min_premium_pct: Minimum acceptable premium/strike ratio
        options_chain: Put options data for premium lookup

    Returns:
        Dictionary with selected strike and reasoning
    """
    if not support_levels:
        return {'strike': None, 'reason': 'No support levels identified'}

    for support in support_levels:
        # Calculate target price (buffer below support)
        target_price = support.price * (1 - buffer_pct / 100)

        # Find closest available strike at or below target
        valid_strikes = [s for s in available_strikes if s <= target_price]

        if not valid_strikes:
            continue

        selected_strike = max(valid_strikes)  # Highest strike below target

        # Check premium if options chain provided
        if options_chain is not None:
            strike_data = options_chain[options_chain['strike'] == selected_strike]
            if not strike_data.empty:
                bid = strike_data['bid'].iloc[0]
                if pd.isna(bid) or bid == 0:
                    bid = strike_data['lastPrice'].iloc[0]

                premium_pct = (bid / selected_strike) * 100

                if premium_pct < min_premium_pct:
                    continue  # Skip if premium too low

        # Calculate how far strike is from current price
        otm_pct = (current_price - selected_strike) / current_price * 100

        return {
            'strike': selected_strike,
            'support_level': support.price,
            'support_strength': support.strength,
            'support_source': support.source,
            'buffer_from_support': round((support.price - selected_strike) / support.price * 100, 2),
            'otm_pct': round(otm_pct, 2),
            'reason': f"Strike ${selected_strike} is {buffer_pct:.1f}% below {support.strength} "
                      f"support at ${support.price} ({support.source})"
        }

    return {'strike': None, 'reason': 'No suitable strike found near support levels'}
```

### Mode 2: Multi-Criteria Strike Selection

For users who want to optimize across multiple factors:

```python
def score_put_strike(
    strike: float,
    current_price: float,
    premium: float,
    delta: Optional[float],
    nearest_support: Optional[SupportLevel],
    weights: dict = None
) -> float:
    """
    Score a strike based on multiple criteria.

    Default weights optimize for conservative put selling:
    - Premium yield (higher is better, up to a point)
    - Distance from support (closer is better)
    - OTM percentage (more OTM is safer)
    - Delta (lower is better for probability)

    Returns:
        Score from 0-100 (higher is better)
    """
    if weights is None:
        weights = {
            'premium': 0.30,      # Premium attractiveness
            'support': 0.35,      # Proximity to support
            'safety': 0.25,       # OTM distance
            'probability': 0.10,  # Delta-based probability
        }

    scores = {}

    # Premium score: 0.5% to 2% is ideal range
    premium_pct = (premium / strike) * 100
    if premium_pct < 0.3:
        scores['premium'] = 20
    elif premium_pct < 0.5:
        scores['premium'] = 50
    elif premium_pct <= 1.5:
        scores['premium'] = 100  # Sweet spot
    elif premium_pct <= 2.5:
        scores['premium'] = 80
    else:
        scores['premium'] = 60  # High premium often means high risk

    # Support score: being near/below support is good
    if nearest_support:
        support_distance = (nearest_support.price - strike) / nearest_support.price * 100
        if support_distance >= 0:  # At or below support
            if support_distance <= 3:
                scores['support'] = 100  # Ideal: just below support
            elif support_distance <= 5:
                scores['support'] = 80
            else:
                scores['support'] = 60
        else:  # Above support (riskier)
            scores['support'] = max(0, 50 + support_distance * 10)
    else:
        scores['support'] = 50  # Neutral if no support data

    # Safety score: more OTM is safer
    otm_pct = (current_price - strike) / current_price * 100
    if otm_pct >= 10:
        scores['safety'] = 100
    elif otm_pct >= 5:
        scores['safety'] = 80
    elif otm_pct >= 3:
        scores['safety'] = 60
    else:
        scores['safety'] = 40

    # Probability score: lower delta is better
    if delta is not None:
        prob_profit = (1 - delta) * 100
        scores['probability'] = min(100, prob_profit)
    else:
        scores['probability'] = 50  # Neutral if no delta

    # Weighted total
    total = sum(scores[k] * weights[k] for k in weights)

    return round(total, 1)
```

---

## Integration with Scanner

### Modified `OptionsPremiumScanner` Class

```python
class OptionsPremiumScanner:
    def __init__(self, symbols, min_annual_return=0, max_delta=1.0,
                 min_volume=0, min_open_interest=0,
                 min_dte=0, max_dte=365,
                 # New technical context parameters
                 show_technicals=False,
                 strike_method='offset',      # 'offset', 'support', 'delta', 'otm_pct'
                 support_buffer_pct=2.0,      # Buffer below support
                 target_delta=None,           # For delta-based selection
                 target_otm_pct=None,         # For OTM%-based selection
                 min_premium_pct=0.3):        # Minimum premium/strike %

        # Existing attributes...
        self.symbols = symbols
        self.min_annual_return = min_annual_return
        # ... etc

        # New attributes
        self.show_technicals = show_technicals
        self.strike_method = strike_method
        self.support_buffer_pct = support_buffer_pct
        self.target_delta = target_delta
        self.target_otm_pct = target_otm_pct
        self.min_premium_pct = min_premium_pct

        # Cache for technical context
        self._technical_cache: Dict[str, TechnicalContext] = {}

    def get_technical_context(self, symbol: str) -> TechnicalContext:
        """
        Fetch and calculate technical context for a symbol.
        Results are cached to avoid redundant API calls.
        """
        if symbol in self._technical_cache:
            return self._technical_cache[symbol]

        ticker = yf.Ticker(symbol)

        # Get historical data (1 year)
        hist = ticker.history(period="1y")

        if hist.empty:
            return None

        current_price = self.get_stock_price(symbol)

        # Calculate 52-week range
        high_52w = hist['High'].max()
        low_52w = hist['Low'].min()
        range_percentile = (current_price - low_52w) / (high_52w - low_52w) * 100

        # Calculate SMAs
        sma_20 = hist['Close'].rolling(20).mean().iloc[-1]
        sma_50 = hist['Close'].rolling(50).mean().iloc[-1]
        sma_200 = hist['Close'].rolling(200).mean().iloc[-1] if len(hist) >= 200 else None

        # Calculate historical volatility
        returns = hist['Close'].pct_change().dropna()
        hv_20 = returns.tail(20).std() * np.sqrt(252) * 100

        # Calculate ATR
        tr = pd.concat([
            hist['High'] - hist['Low'],
            abs(hist['High'] - hist['Close'].shift()),
            abs(hist['Low'] - hist['Close'].shift())
        ], axis=1).max(axis=1)
        atr_14 = tr.rolling(14).mean().iloc[-1]
        atr_percent = (atr_14 / current_price) * 100

        # Detect support levels
        swing_lows = find_swing_lows(hist)
        swing_supports = cluster_support_levels(swing_lows)
        sma_supports = get_sma_support(current_price, sma_50, sma_200 or sma_50)
        round_supports = get_round_number_support(current_price)

        support_levels = consolidate_support_levels(
            swing_supports, sma_supports, round_supports,
            current_price
        )

        # Try to get IV rank (may not be available from yfinance)
        iv_rank = None  # Placeholder - would need options data

        context = TechnicalContext(
            symbol=symbol,
            current_price=current_price,
            high_52w=high_52w,
            low_52w=low_52w,
            range_percentile=range_percentile,
            sma_20=sma_20,
            sma_50=sma_50,
            sma_200=sma_200,
            price_vs_sma20=(current_price - sma_20) / sma_20 * 100,
            price_vs_sma50=(current_price - sma_50) / sma_50 * 100,
            price_vs_sma200=(current_price - sma_200) / sma_200 * 100 if sma_200 else None,
            iv_rank=iv_rank,
            hv_20=hv_20,
            atr_14=atr_14,
            atr_percent=atr_percent,
            support_levels=support_levels,
            nearest_support=support_levels[0] if support_levels else None,
            suggested_put_strike=None  # Set during strike selection
        )

        self._technical_cache[symbol] = context
        return context
```

### Modified `scan_symbol` Method

```python
def scan_symbol(self, symbol, strike_offset=0):
    """Enhanced scan with technical context support."""

    # Get technical context if enabled
    tech_context = None
    if self.show_technicals or self.strike_method == 'support':
        tech_context = self.get_technical_context(symbol)

    # ... existing code to get ticker, price, expirations ...

    for exp_date in expirations[:8]:
        # ... existing code to get options chain ...

        # NEW: Select put strike based on method
        if self.strike_method == 'support' and tech_context:
            put_selection = select_put_strike_near_support(
                available_strikes=put_strikes,
                support_levels=tech_context.support_levels,
                current_price=current_price,
                buffer_pct=self.support_buffer_pct,
                min_premium_pct=self.min_premium_pct,
                options_chain=puts
            )
            put_strike = put_selection.get('strike') or put_strikes[put_strike_idx]

        elif self.strike_method == 'delta' and self.target_delta:
            # Find strike closest to target delta
            put_strike = select_strike_by_delta(puts, self.target_delta)

        elif self.strike_method == 'otm_pct' and self.target_otm_pct:
            # Find strike at target % OTM
            target_price = current_price * (1 - self.target_otm_pct / 100)
            put_strike = min(put_strikes, key=lambda x: abs(x - target_price))

        else:
            # Default: use offset method (existing behavior)
            put_strike = put_strikes[put_strike_idx]

        # ... existing code to get put data and calculate metrics ...

        # NEW: Add technical context to results
        if tech_context:
            result['52W Percentile'] = tech_context.range_percentile
            result['SMA 50'] = tech_context.sma_50
            result['SMA 200'] = tech_context.sma_200
            result['HV 20'] = tech_context.hv_20
            result['Nearest Support'] = tech_context.nearest_support.price if tech_context.nearest_support else None
            result['Support Strength'] = tech_context.nearest_support.strength if tech_context.nearest_support else None
            result['Distance to Support'] = tech_context.nearest_support.distance_pct if tech_context.nearest_support else None

        self.results.append(result)
```

---

## CLI Interface

### New Command-Line Arguments

```python
def parse_arguments():
    parser = argparse.ArgumentParser(...)

    # Existing arguments...

    # === NEW: Technical Context Arguments ===

    tech_group = parser.add_argument_group('Technical Analysis')

    tech_group.add_argument(
        '--show-technicals', '-t',
        action='store_true',
        help='Display technical context (52W range, SMAs, support levels)'
    )

    tech_group.add_argument(
        '--strike-method',
        choices=['offset', 'support', 'delta', 'otm_pct'],
        default='offset',
        help='''Strike selection method:
            offset: Fixed offset from ATM (default)
            support: Select strikes near support levels
            delta: Select by target delta
            otm_pct: Select by target OTM percentage'''
    )

    tech_group.add_argument(
        '--support-buffer',
        type=float,
        default=2.0,
        metavar='PCT',
        help='Percent below support level for strike selection (default: 2.0)'
    )

    tech_group.add_argument(
        '--target-delta',
        type=float,
        metavar='DELTA',
        help='Target delta for strike selection (e.g., 0.20 for 20 delta)'
    )

    tech_group.add_argument(
        '--target-otm',
        type=float,
        metavar='PCT',
        help='Target OTM percentage for strike selection (e.g., 5 for 5%% OTM)'
    )

    tech_group.add_argument(
        '--min-premium-pct',
        type=float,
        default=0.3,
        metavar='PCT',
        help='Minimum premium as %% of strike (default: 0.3)'
    )

    tech_group.add_argument(
        '--support-lookback',
        type=int,
        default=15,
        metavar='PCT',
        help='How far below current price to look for support (default: 15%%)'
    )

    return parser.parse_args()
```

### Example Commands

```bash
# Basic usage with technical context display
python -m options_scanner --symbols AAPL MSFT --show-technicals

# Support-based strike selection (your use case)
python -m options_scanner \
  --symbols AAPL MSFT NVDA GOOGL \
  --strike-method support \
  --support-buffer 2.0 \
  --min-premium-pct 0.5 \
  --min-annual 20 \
  --min-dte 30 \
  --max-dte 45

# Delta-based selection
python -m options_scanner \
  --symbols AAPL MSFT \
  --strike-method delta \
  --target-delta 0.20

# OTM percentage selection
python -m options_scanner \
  --symbols AAPL MSFT \
  --strike-method otm_pct \
  --target-otm 5

# Conservative preset with support
python -m options_scanner \
  --conservative \
  --strike-method support
```

---

## Output Format

### Enhanced Console Output

```
================================================================================
                         OPTIONS PREMIUM SCANNER
================================================================================
Markets are OPEN - using live bid prices

================================================================================
                         TECHNICAL CONTEXT SUMMARY
================================================================================

Symbol   Price    52W Range       %ile   SMA50   SMA200   HV20   Support Levels
--------------------------------------------------------------------------------
  AAPL  187.50   164.07-199.62    72%   182.40   176.20   22.5%  $180(S), $175(M)
  MSFT  378.25   309.00-420.82    62%   370.50   355.80   19.8%  $365(S), $350(M)
  NVDA  495.80   403.25-502.50    96%   475.00   420.50   35.2%  $480(M), $450(S)

Legend: (S)=Strong, (M)=Moderate, (W)=Weak support

================================================================================
                    CASH-SECURED PUTS - SUPPORT-BASED STRIKES
================================================================================

Filter: Strike Method = Support, Buffer = 2.0% below support

Expiration: 2026-02-21 (27 DTE)
--------------------------------------------------------------------------------
                                    Support                           Risk
Symbol  Strike    Bid  %OTM  Delta   Level  Buffer  Premium%  Annual%  Score
--------------------------------------------------------------------------------
  AAPL  175.00   1.85   6.7%  0.18  $178.50  1.9%     1.06%    14.3%    82
  MSFT  360.00   3.50   4.8%  0.22  $365.00  1.4%     0.97%    13.1%    78
  NVDA  470.00   8.20   5.2%  0.25  $480.00  2.1%     1.74%    23.6%    75

Strike Reasoning:
  AAPL: $175 is 1.9% below STRONG support at $178.50 (swing_low_cluster, 3 touches)
  MSFT: $360 is 1.4% below STRONG support at $365.00 (sma_50)
  NVDA: $470 is 2.1% below MODERATE support at $480.00 (swing_low_cluster, 2 touches)

================================================================================
```

### Enhanced CSV Export

New columns added to CSV output:

```csv
Symbol,Price,52W_High,52W_Low,52W_Percentile,SMA_50,SMA_200,HV_20,Nearest_Support,Support_Strength,Support_Source,Support_Touches,Expiration,DTE,Put_Strike,Put_Bid,Put_Delta,Put_OTM_Pct,Put_Premium_Pct,Put_Annual_Pct,Buffer_From_Support,Risk_Score
AAPL,187.50,199.62,164.07,72.0,182.40,176.20,22.5,178.50,strong,swing_low_cluster,3,2026-02-21,27,175.00,1.85,0.18,6.7,1.06,14.3,1.9,82
```

---

## Implementation Plan

### Phase 1: Core Technical Context (Week 1)
- [ ] Create `TechnicalContext` dataclass
- [ ] Implement 52-week range calculation
- [ ] Implement SMA calculations (20, 50, 200)
- [ ] Implement historical volatility (HV20)
- [ ] Add `--show-technicals` flag
- [ ] Unit tests for calculations

### Phase 2: Support Detection (Week 2)
- [ ] Implement swing low detection
- [ ] Implement support clustering
- [ ] Implement SMA support identification
- [ ] Implement round number support
- [ ] Implement consolidation algorithm
- [ ] Unit tests for support detection

### Phase 3: Strike Selection (Week 3)
- [ ] Implement `--strike-method support`
- [ ] Implement support buffer logic
- [ ] Implement minimum premium filter
- [ ] Add strike reasoning to output
- [ ] Implement risk scoring
- [ ] Integration tests

### Phase 4: Polish & Documentation (Week 4)
- [ ] Enhanced console output formatting
- [ ] CSV export with new columns
- [ ] Update README with examples
- [ ] Performance optimization (caching)
- [ ] End-to-end testing

---

## Testing Strategy

### Unit Tests

```python
class TestTechnicalContext(unittest.TestCase):

    def test_52w_percentile_at_high(self):
        """Price at 52W high should be 100%."""
        # current=200, low=150, high=200 → 100%
        pct = calculate_range_percentile(200, 150, 200)
        self.assertEqual(pct, 100.0)

    def test_52w_percentile_at_low(self):
        """Price at 52W low should be 0%."""
        pct = calculate_range_percentile(150, 150, 200)
        self.assertEqual(pct, 0.0)

    def test_52w_percentile_midpoint(self):
        """Price at midpoint should be 50%."""
        pct = calculate_range_percentile(175, 150, 200)
        self.assertEqual(pct, 50.0)


class TestSupportDetection(unittest.TestCase):

    def test_swing_low_detection(self):
        """Should identify local minima in price data."""
        # Create test data with known swing lows
        ...

    def test_support_clustering(self):
        """Nearby swing lows should cluster together."""
        swing_lows = [
            {'price': 100.0, 'date': '2025-01-01'},
            {'price': 100.5, 'date': '2025-02-01'},
            {'price': 101.0, 'date': '2025-03-01'},
            {'price': 95.0, 'date': '2025-04-01'},
        ]
        clusters = cluster_support_levels(swing_lows, tolerance_pct=1.5)
        self.assertEqual(len(clusters), 2)  # $100 cluster and $95

    def test_round_number_support(self):
        """Should identify round numbers below price."""
        supports = get_round_number_support(187.50)
        prices = [s.price for s in supports]
        self.assertIn(175.0, prices)
        self.assertIn(180.0, prices)


class TestStrikeSelection(unittest.TestCase):

    def test_strike_below_support(self):
        """Selected strike should be below support with buffer."""
        strikes = [170, 175, 180, 185, 190]
        support = SupportLevel(price=180, strength='strong', ...)
        result = select_put_strike_near_support(
            strikes, [support], current_price=190, buffer_pct=2.0
        )
        # 2% below 180 = 176.4, so should pick 175
        self.assertEqual(result['strike'], 175)

    def test_no_valid_strike_below_support(self):
        """Should return None if no strikes below support-buffer."""
        strikes = [185, 190, 195]
        support = SupportLevel(price=180, strength='strong', ...)
        result = select_put_strike_near_support(
            strikes, [support], current_price=190, buffer_pct=2.0
        )
        self.assertIsNone(result['strike'])
```

### Integration Tests

```python
def test_full_scan_with_technicals():
    """End-to-end test with technical context enabled."""
    scanner = OptionsPremiumScanner(
        symbols=['AAPL'],
        show_technicals=True,
        strike_method='support',
        support_buffer_pct=2.0
    )
    results = scanner.scan_all()

    # Verify technical columns present
    assert '52W Percentile' in results.columns
    assert 'Nearest Support' in results.columns

    # Verify strikes are reasonable
    for _, row in results.iterrows():
        assert row['Put Strike'] < row['Current Price']
        if row['Nearest Support']:
            assert row['Put Strike'] <= row['Nearest Support']
```

---

## Appendix: IV Rank Calculation

If IV data becomes available (via paid API or options chain):

```python
def calculate_iv_rank(current_iv: float, iv_history: List[float]) -> float:
    """
    Calculate IV Rank (percentile of current IV vs 52-week range).

    IV Rank = (Current IV - 52W Low IV) / (52W High IV - 52W Low IV) × 100

    Higher IV Rank = premiums are elevated = better for sellers
    """
    iv_high = max(iv_history)
    iv_low = min(iv_history)

    if iv_high == iv_low:
        return 50.0

    return (current_iv - iv_low) / (iv_high - iv_low) * 100
```

---

## Summary

This design adds comprehensive technical context to the options scanner, enabling:

1. **Support-aware strike selection** - Automatically pick strikes below key support
2. **Visual technical context** - See 52W range, SMAs, and support levels at a glance
3. **Multiple selection methods** - Support-based, delta-based, or OTM%-based
4. **Risk scoring** - Quantify how well a strike fits conservative criteria
5. **Backward compatibility** - Default behavior unchanged; new features opt-in

The key differentiator for your use case is the `--strike-method support` mode, which finds strikes slightly below identified support levels while ensuring acceptable premium/strike ratios.
