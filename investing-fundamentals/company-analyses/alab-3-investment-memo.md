# Astera Labs Inc. (NASDAQ: ALAB) — Investment Memo
**Date:** April 6, 2026 | **Exchange:** NASDAQ | **Sector:** Semiconductors / AI Infrastructure Connectivity

---

## 1. Executive Summary

### Investment Thesis

Astera Labs has built the most comprehensive portfolio of semiconductor connectivity solutions for AI data center infrastructure, spanning PCIe/CXL signal integrity (Aries), Ethernet scale-out fabric (Taurus), memory expansion (Leo), and PCIe/scale-up fabric switching (Scorpio). In an era where the bottleneck in AI infrastructure has shifted from compute to connectivity, Astera's purpose-built silicon and COSMOS software platform provide hyperscalers with an integrated, standards-agnostic solution that is increasingly difficult to displace once designed into a platform. The company delivered $852.5M in revenue and ~39% non-GAAP operating margins in FY2025, demonstrating strong unit economics even while investing aggressively in next-generation silicon and optical connectivity. With a $6.5B warrant-linked commitment from Amazon and expanding design wins across multiple hyperscalers, the revenue ramp has a credible multi-year runway.

The thesis rests on three pillars: (1) PCIe 6 and CXL 3 content-per-server expansion driving Aries retimer revenue; (2) Ethernet-based scale-out fabric adoption driving Taurus AEC volume at 400G/800G; and (3) Scorpio fabric switch penetration of the emerging merchant scale-up switch market (projected $20B by 2030). Against these tailwinds, investors must weigh the central structural risk: a faster-than-expected transition from copper AEC to optical fiber in AI data center scale-out fabric, which would compress Taurus revenue before Astera's optical products (aiXscale-based) are ready to compensate.

### Bull Case
AI infrastructure CapEx sustains at $400B+ globally through 2027; Scorpio X-Series wins scale-up market share from NVIDIA NVLink proprietary fabric; Taurus extends copper AEC dominance through 800G-per-lane; and Leo drives a new CXL memory expansion revenue cycle post-2026 as LLM inference memory demand grows. Revenue reaches $2B+ by FY2027 with non-GAAP operating margins expanding to 42-45%.

### Bear Case
The optical transition in AI data centers accelerates to 2026-2027, compressing Taurus AEC revenue before optical products are available; a single hyperscaler (Amazon) delays or reduces purchase commitments; Broadcom and Marvell compete aggressively in PCIe switches and CXL memory, eroding Aries and Leo pricing; and Scorpio X-Series faces qualification delays. Revenue growth slows to 20-30% with margin compression from elevated R&D spend.

### Target Investor Profile
**High-growth technology investors** with 3-5 year horizons and tolerance for single-stock semiconductor concentration risk. Astera is not a value play (premium multiple) or income investment. Suitable for investors who have conviction in sustained AI CapEx growth and believe Astera can successfully navigate the copper-to-optical transition.

---

## 2. Business Model & Unit Economics

### Revenue Summary

| Metric | FY2023 | FY2024 | FY2025 | Q1 2026 Guidance |
|--------|--------|--------|--------|------------------|
| Revenue | $115M (est.) | $396.3M | $852.5M | $286-297M |
| YoY Growth | — | +242% | +115% | ~34-40% YoY |
| GAAP Gross Margin | — | ~74-76% | 75.7% | ~74% |
| Non-GAAP Operating Margin | — | ~32% | 39.2% | ~39-40% |
| GAAP Operating Income | — | — | $173.4M | — |
| Non-GAAP EPS | — | ~$0.60 | $1.84 | $0.53-$0.54 |
| Operating Cash Flow | — | — | $319.3M | — |

### Revenue Breakdown by Product (Estimated, FY2025)

Astera does not publicly disclose per-product revenue. The following is derived from management commentary:

| Product | FY2025 Growth | Est. % of Revenue | Est. FY2025 Revenue |
|---------|--------------|-------------------|---------------------|
| Aries PCIe/CXL Retimers | ~70% YoY | ~40-45% | ~$340-385M |
| Taurus Ethernet AECs | >300% (4x+) YoY | ~30-35% | ~$255-300M |
| Scorpio Fabric Switches | N/A (first full year) | ~15% (~$125M+) | ~$125-130M |
| Leo CXL Memory | Early ramp | ~5-10% | ~$40-85M |

### Key Unit Economics

| Metric | Value | Notes |
|--------|-------|-------|
| Gross Margin | 75.7% (GAAP, FY2025) | Reflects mix of retimer silicon (~85%+ GM) and cable module hardware (~60-65% GM) |
| Non-GAAP Operating Margin | 39.2% (FY2025) | FCF-generating; SBC is the primary GAAP/non-GAAP delta |
| R&D as % Revenue | ~30-35% (est.) | Reflects multi-generational silicon investment |
| Customer concentration | ~80% from 3 hyperscalers (FY2024) | Improving but still highly concentrated |
| Amazon framework | $6.5B over multiple years | Warrant-linked; provides long-term revenue floor |
| Design cycle | 12-24 months from qualification to volume | Creates revenue lag but also lock-in |

### Operating Leverage Dynamics

Astera exhibits strong theoretical operating leverage: once a chip generation is taped out (high fixed cost), incremental volume ships at ~75% gross margin. However, the company continuously invests in next-generation silicon (PCIe 7, optical retimers, Scorpio X-Series), preventing operating margins from compressing R&D rapidly. Near-term non-GAAP operating margin of ~39-40% should expand gradually to 42-45% as Scorpio revenue scales, as switches carry higher ASPs with similar gross margins to retimers.

### Working Capital & Cash Conversion

As a fabless business, Astera builds inventory ahead of customer ramps (creating short-term cash usage) and collects payment upon shipment (no subscription float). The positive FCF at $319M operating cash flow in FY2025 demonstrates that growth is self-funding. Key working capital risk: obsolete inventory writedowns at product generation transitions (e.g., PCIe 5 → PCIe 6).

---

## 3. Competitive Position & Moat

### Market Position

| Market | Astera Position | Est. Market Size (2025-2026) | Key Rivals |
|--------|----------------|------------------------------|------------|
| PCIe/CXL Retimers | **#1 in AI data center** | ~$530M+ (2025) | Marvell, Parade, Montage, Microchip |
| Ethernet Scale-Out AECs (AI) | **Leading position** | Growing rapidly with 400G/800G rollout | Credo (CRDO), InPhi/Marvell |
| PCIe Fabric Switches | **Emerging leader** (first mover) | $2-5B+ by 2028 | Broadcom (incumbent), Microchip |
| Scale-Up Fabric Switches | **Challenger** (Scorpio X in development) | $5-20B by 2030 | NVIDIA (proprietary NVLink), Broadcom |
| CXL Memory Controllers | **Pioneer** | $200M+ (2025-2026, early stage) | Marvell (Structera), Samsung |

### Moat Classification: **Proprietary IP + Platform Switching Costs + Ecosystem Positioning**

**1. Purpose-Built AI Silicon Architecture**
Aries DSP retimers were designed from inception for GPU-to-GPU PCIe/CXL traffic — not repurposed from storage or telecom silicon. This results in measurably better signal integrity performance at lower power in AI traffic patterns. Competitors have announced competing retimer products (Marvell, Microchip) but have not displaced Astera at the hyperscaler accounts.

**2. COSMOS Software Platform — the "Invisible Moat"**
COSMOS is Astera's unified software layer providing telemetry, predictive failure analytics, and connectivity management across all four product families. Once a hyperscaler integrates COSMOS into its infrastructure management stack (automation scripts, monitoring dashboards, operations runbooks), switching to a competing silicon vendor requires rebuilding the entire software integration. This creates 12-24 months of inertia per account per generation transition. This is the most underappreciated element of Astera's competitive positioning.

**3. Protocol Agnosticism and Multi-Standard Coverage**
- NVLink Fusion ecosystem partner (NVIDIA)
- Founding member of UALink Consortium (AMD, Google, Microsoft, Meta)
- PCIe 6 / CXL 3 leadership
- 400G/800G Ethernet scale-out support
- Photonics (aiXscale) for future optical scale-up

Astera is the only vendor positioned across all major AI fabric standards simultaneously, allowing it to win regardless of which interconnect standard wins the "protocol war" between NVIDIA's proprietary stack and the open consortium approach.

**4. Design-In Lock-In with 12-24 Month Qualification Cycles**
Hyperscaler qualification of a new silicon vendor takes 12-18 months. Once Aries is qualified into NVIDIA Blackwell HGX, it remains the designed-in solution for the platform lifetime (typically 24-36 months before the next generation). This creates revenue visibility and switching costs even without explicit long-term contracts.

### Moat Durability Assessment: **High (2026-2027) → Medium (2028-2030)**

The moat is strong through the PCIe 6 / Ethernet 800G cycle (2026-2027). The durability question for 2028-2030 hinges on whether:
1. Co-packaged optics (CPO) eliminates the need for discrete retimers by integrating optics directly at the switch ASIC — removing the PCB-trace signal integrity problem Aries solves
2. Scale-up fabric transitions from copper to optical faster than Astera's aiXscale-based product roadmap can respond

### Key Competitors

| Competitor | Overlap Area | Threat Level | Assessment |
|------------|-------------|-------------|------------|
| **Marvell Technology** | CXL memory (Structera), PCIe retimers | HIGH | Well-funded, strong hyperscaler relationships; primary long-term competitor |
| **Broadcom** | PCIe fabric switches, Ethernet | HIGH | Incumbent scale; Broadcom's PCIe switch response to Scorpio is accelerating |
| **Credo Technology (CRDO)** | Ethernet AECs (SerDes) | MEDIUM | Direct Taurus competitor; less software differentiation |
| **Parade Technologies** | PCIe/CXL retimers | MEDIUM-LOW | Less AI-focused; strong in PC/consumer |
| **Montage Technology** | PCIe retimers | LOW | China-focused; limited hyperscaler access |
| **NVIDIA (NVLink proprietary)** | Scale-up fabric | MEDIUM | Proprietary NVLink competes with Scorpio X; NVLink Fusion creates both risk and opportunity |

---

## 4. Top 3 Growth Drivers & Sensitivities

### Driver 1: PCIe 6 / Aries Retimer Revenue Ramp (FY2025-FY2027)

**Description**: Every NVIDIA Blackwell and next-gen AI server platform deploying PCIe 6 requires updated Aries 6 retimers for each PCIe slot. Content-per-server increases as GPU configurations grow (8→16→32 GPUs per rack) and PCIe 6 lanes per device double. Management announced PCIe 6 connectivity portfolio entering production in May 2025.

**TAM Impact**: The PCIe retimer market is estimated at $530M+ in 2025, growing to $1.0-1.5B by 2027 as PCIe 6 volumes ramp. Astera's leading market share (~50%+ in AI data centers) implies $500-750M in Aries revenue at full cycle penetration.

**Scenarios:**

| Scenario | Assumption | Aries Revenue FY2027 |
|----------|------------|---------------------|
| Bull | PCIe 6 ramps at all 5 major hyperscalers; GPU count per rack doubles | $600-750M |
| Base | PCIe 6 ramps at 3 hyperscalers; normal GPU density growth | $450-550M |
| Bear | PCIe 6 qualification delays; Marvell wins 1-2 hyperscaler accounts | $300-400M |

**Milestones**: Track PCIe 6 qualification announcements at AWS, Google, Meta, Microsoft, Oracle through mid-2026.

---

### Driver 2: Taurus Ethernet AEC Expansion — and the Copper-to-Optical Risk (FY2025-FY2027)

**Description**: Taurus Ethernet Smart Cable Modules are the cornerstone of the scale-out AI Ethernet fabric at hyperscalers. As Ethernet-based GPU interconnect (at 400G and 800G per port) displaces InfiniBand, AECs become the preferred short-reach (<7m) cable solution due to 25-50% lower power consumption vs. optical and no latency penalty from full DSP processing.

**TAM Impact**: The scale-out Ethernet interconnect market for AI data centers is enormous. Hyperscalers deploying tens of thousands of GPU ports each, at 2-4 cables per GPU port, represent hundreds of millions of cable modules annually. Taurus grew 4x+ in FY2025, implying from ~$50-60M to ~$250-300M in one year.

**The Copper vs. Optical Transition — Detailed Analysis:**

This is the most important structural risk for Taurus specifically:

**What Taurus does**: Taurus SCMs embed Astera's SerDes/DSP silicon inside a copper AEC cable connector. The cable itself is thin-gauge copper (30/32/34 AWG); the Astera chip inside provides signal conditioning, gearboxing (rate conversion), diagnostics, and management telemetry. This allows thin, power-efficient copper cables to run at 100G, 200G, and 400G per lane over up to 3-7 meters.

**Why copper AECs are currently preferred for short-reach AI fabric (<7m)**:
- Power: AECs consume 25-50% less power than AOCs (no optical transceiver, no laser diodes)
- Latency: No optical serialization/deserialization overhead
- Cost: Copper AECs are significantly cheaper than optical at equivalent speeds
- Reliability: No fiber handling, less complex connector management in high-density racks

**Where optical wins today**:
- Beyond 7-10 meters (copper AECs cannot maintain signal integrity)
- Scale-up (GPU-to-GPU within a training cluster) over multi-rack distances (>10m)
- Spine-to-spine connections in multi-pod data center architectures

**The transition risk**:
As speeds scale beyond 200G/lane (approaching 400G/lane), copper becomes increasingly difficult to drive at even short distances due to signal attenuation. At 400G-per-lane speeds, the viable copper reach shrinks from 7m to potentially 3m or less. If rack designs physically separate GPUs from ToR switches beyond copper reach, or if co-packaged optics eliminates the need for external cables entirely, Taurus AECs face obsolescence.

Astera's own published technical analysis (the "400G Per-Lane Inflection Point" white paper) acknowledges this dynamic: copper AECs will serve the market through approximately 200G-per-lane (current); at 400G-per-lane, optical becomes necessary for many use cases. Management estimates scale-out optical revenue reaches material scale "earliest 2028-2029."

**Astera's optical response for Taurus**:
- As of Q1 2026, **Astera does NOT have a shipping optical Taurus product**
- aiXscale Photonics acquisition (Nov 2025) provides fiber-chip coupling technology primarily targeting scale-up optical (Scorpio X-Series use case), not Taurus scale-out
- Aries optical module ("PCIe over Optics") demonstrates Astera's DSP can work in optical settings, but this is not the same as an optical Ethernet SCM
- The gap: Astera has a copper Taurus product that is at peak revenue growth *now*, but no optical Taurus product ready. Competitors (Credo, optical transceiver vendors) are better positioned if optical transitions sooner

**Scenarios:**

| Scenario | Assumption | Taurus Revenue FY2027 |
|----------|------------|----------------------|
| Bull | Copper AECs maintain dominance through 200G/lane cycle; hyperscalers standardize AECs for 800G scale-out at <7m | $500-700M |
| Base | Mixed adoption: AECs for server-level, AOCs for pod-to-pod; Taurus grows but at slower pace | $350-500M |
| Bear | Optical transitions faster; co-packaged optics reduces cable count; Credo wins optical AEC design-ins | $150-250M |

**Key milestones to watch**:
- Hyperscaler public statements on 800G/lane AEC vs. AOC adoption at OFC 2026 conference
- Credo Technology quarterly earnings for Taurus competitive commentary
- Whether Astera announces an optical Ethernet SCM product or OEM partnership

---

### Driver 3: Scorpio Fabric Switch Market Creation (FY2026-FY2030)

**Description**: Scorpio is Astera's newest and fastest-growing product family, crossing 15% of revenue (~$125M+) in its first full year of production. The P-Series targets the PCIe scale-out switch market (GPU-to-NIC-to-storage disaggregation); the X-Series targets the scale-up GPU cluster fabric (competing with NVIDIA NVLink and the emerging UALink standard). Management sees the merchant scale-up switching market reaching $20B by 2030.

**The strategic optionality**: Scorpio X-Series, combined with aiXscale photonic technology and UALink membership, is Astera's largest and most speculative growth opportunity. If hyperscalers adopt open-standard scale-up fabrics (UALink, Ultra Accelerator Link) to reduce NVIDIA NVLink dependency, Astera is one of the only merchant silicon vendors positioned to provide the fabric switch.

**Scenarios:**

| Scenario | Assumption | Scorpio Revenue FY2027 |
|----------|------------|------------------------|
| Bull | Scorpio X-Series enters production at 2 hyperscalers; UALink consortium drives open fabric adoption | $400-600M |
| Base | Scorpio P-Series grows; X-Series at early production; 1 hyperscaler at scale | $250-350M |
| Bear | NVIDIA NVLink retains dominance; Broadcom wins PCIe switch wars; Scorpio X delayed | $100-150M |

---

## 5. Risk Framework with Failure Modes

### Top 5 Risks

| # | Risk | Severity | Probability | Expected Impact |
|---|------|----------|-------------|-----------------|
| 1 | Optical transition compresses Taurus AEC revenue (2027-2028) | Very High | Medium | Taurus revenue flat or declining; ~$200-400M revenue at risk |
| 2 | Hyperscaler CapEx pause / program delay | High | Medium | Revenue miss of 20-30% in the affected quarter |
| 3 | Customer concentration (Amazon/Google anchor) | High | Low-Medium | Single-customer delay = 15-30% revenue impact |
| 4 | Competitive displacement by Marvell/Broadcom in PCIe switches and CXL | High | Medium | Aries and Leo pricing pressure; share loss |
| 5 | TSMC / Taiwan supply chain disruption | Very High | Low | Catastrophic short-term; no fallback fab for advanced nodes |

---

### Risk Detail

**Risk 1: Optical Transition Accelerates Beyond Taurus AEC Addressable Market**
- **Trigger**: Hyperscalers standardize on 400G/800G AOC (Active Optical Cables) or integrate co-packaged optics directly into GPU/switch chipsets, eliminating the cable-module form factor
- **Impact**: Taurus revenue growth stops. At an estimated ~$250-300M FY2025 Taurus revenue growing to $350-500M by FY2027 in base case, a full stall would cost ~$200-400M in projected revenue
- **Mitigation**: (a) AEC power/cost/latency advantages sustain copper through the 200G/lane cycle (2026-2027); (b) Astera's aiXscale acquisition positions it for optical scale-up; (c) Scorpio X-Series includes photonic links
- **Gap**: Astera has NO shipping optical Ethernet SCM product as of Q1 2026. If optical transition comes before 2028, the revenue gap is real and unhedged
- **Specific products at risk**: Taurus Ethernet SCMs (~30-35% of FY2025 revenue est.); potentially Aries Smart Cable Modules
- **Products that are NOT at risk**: Aries PCIe/CXL Retimers (bus-level, not fabric-level), Leo CXL Controllers, Scorpio P-Series (being adapted for optical)

**Risk 2: Hyperscaler CapEx Pause or Program Delay**
- **Trigger**: Macroeconomic deterioration, AI capex rationalization, or specific platform delay (e.g., next NVIDIA GPU gen delayed)
- **Impact**: Revenue misses of 20-30%; management guidance cuts; multiple compression in a high-growth narrative stock
- **Mitigation**: Amazon $6.5B warrant framework provides revenue floor; multiple customer diversification improving in FY2025-2026
- **Precedent**: Q4 2022 – Q2 2023 saw broad hyperscaler capex pauses; semiconductor companies with 80%+ customer concentration suffered severe drawdowns

**Risk 3: Customer Concentration (Amazon/Google)**
- **Trigger**: Single large hyperscaler delays deployment, shifts architecture (e.g., adopts NVLink for all scale-up, uses optical), or qualifies alternative vendor
- **Impact**: 15-30% quarterly revenue impact for a single customer event; possible earnings guidance cut
- **Mitigation**: Diversification actively underway; Scorpio P-Series crossing 15% at one customer in first year with two more US hyperscalers in qualification; Microsoft CXL win adds third anchor customer

**Risk 4: Competitive Displacement by Marvell and Broadcom**
- **Trigger**: Marvell wins PCIe/CXL retimer qualification at a key hyperscaler; Broadcom wins PCIe fabric switch at scale
- **Impact**: Pricing pressure; ASP compression of 15-25%; potential market share loss in next platform cycle
- **Mitigation**: COSMOS software switching costs; first-mover qualification advantage; Aries 6 production-proven in Blackwell
- **Timeline**: PCIe 7 cycle (2027-2028) is the first major design-in competition point

**Risk 5: TSMC Taiwan Supply Chain**
- **Trigger**: Taiwan conflict, US-China export control escalation affecting TSMC advanced node access
- **Impact**: Catastrophic short-term; no second-source fab for cutting-edge 3-5nm AI silicon
- **Mitigation**: None available near-term; TSMC Arizona ramp (2025+) provides partial mitigation only for mature nodes
- **Industry-wide**: This risk affects all US fabless AI semiconductor companies equally (NVIDIA, AMD, Broadcom, Marvell)

---

### Pre-Mortem: Why Would This Investment Fail in 3 Years?

*"If we look back from April 2029 and Astera Labs was a poor investment, the most likely reason is: the copper-to-optical transition in AI data center scale-out Ethernet fabric arrived 18-24 months earlier than management's 2028-2029 timeline, driven by co-packaged optics integration directly into next-generation switch ASICs. This made the Taurus AEC form factor obsolete before Astera's optical product suite (aiXscale-based) was ready to ship at scale. Simultaneously, Scorpio X-Series faced qualification delays against incumbent Broadcom PCIe switches, causing Scorpio revenue to disappoint. The result was that Astera's two highest-growth products (Taurus, Scorpio X) underperformed, leaving the company as primarily an Aries retimer business growing at 15-20% instead of the 50%+ compound platform story the market priced in at the time of investment."*

---

### Key Assumptions That Must Hold for the Thesis to Work

1. Copper AECs (Taurus) remain the preferred solution for scale-out Ethernet at <7m through 2027
2. Scorpio X-Series enters production at ≥1 major hyperscaler in FY2026
3. PCIe 6 qualifications proceed on schedule at Amazon, Google, Microsoft
4. aiXscale optical technology matures into shippable product by 2028-2029
5. Astera wins ≥1 UALink-based scale-up design win before NVIDIA NVLink fully dominates open fabric market
6. TSMC manufacturing access remains uninterrupted at advanced nodes

---

## 6. 12-Month KPI Watch List (April 2026 – April 2027)

| # | KPI | Current Value | Target / Bull Range | Red Flag Threshold | Source / Frequency |
|---|-----|---------------|---------------------|---------------------|-------------------|
| 1 | **Total Revenue (Quarterly)** | $270.6M (Q4 2025) / guided $286-297M (Q1 2026) | $300-320M by Q3 2026 | <$260M any quarter | Quarterly earnings |
| 2 | **Taurus Revenue Growth (YoY)** | >300% (FY2025, est.) | >80% YoY (decelerating from 300% but still high) | <30% YoY growth = optical risk signal | Quarterly earnings (inferred from commentary) |
| 3 | **Scorpio % of Total Revenue** | ~15% (FY2025) | 20-25% by end FY2026 | <15% = X-Series delay | Quarterly earnings commentary |
| 4 | **New Hyperscaler Design Wins** | 2-3 US hyperscalers in qualification (commentary) | ≥2 new design wins confirmed in earnings calls | Zero new qualifications announced for 6+ months | Earnings call commentary |
| 5 | **Gross Margin (GAAP)** | 75.7% (FY2025) | 75-77% | <73% = product mix degradation or pricing pressure | Quarterly earnings |
| 6 | **Non-GAAP Operating Margin** | 39.2% (FY2025) | 39-43% | <35% = R&D overrun or revenue miss | Quarterly earnings |
| 7 | **Optical Product Announcement** | No shipping optical AEC product (Q1 2026) | Optical Ethernet SCM product announcement by Q3 2026 | No announcement by end of 2026 = 2028-2029 gap unaddressed | Press releases / OFC 2026 |
| 8 | **Scorpio X-Series Qualification Updates** | Announced expanded roadmap; X-Series for high-volume production 2026 | First production shipment confirmed by Q3 2026 | X-Series delay to 2027 | Earnings calls |
| 9 | **Leo CXL Revenue Ramp** | Small contribution FY2025; Microsoft Azure deployment live | Leo crosses 10% of total revenue by FY2026 | Leo remains <5% of revenue by Q4 2026 = CXL adoption slower than expected | Earnings commentary |
| 10 | **Customer Concentration** | ~80% from 3 hyperscalers (FY2024) | <65% from top 3 by end FY2026 | Top customer rises above 60% alone | Annual 10-K disclosure |

### Monitoring Notes

- **Copper vs. Optical Inflection Point — Key Conference**: The Optical Fiber Communications (OFC) Conference (typically March each year) is the most important external signal on timing. If hyperscaler network architects present papers on AEC-to-AOC transition timelines at OFC 2027, adjust Taurus forward estimates immediately.
- **Credo Technology (CRDO) as a Proxy**: Credo's Ethernet AEC/SerDes business overlaps directly with Taurus. Monitor CRDO quarterly results for commentary on copper vs. optical competitive dynamics and win rates vs. AOC alternatives.
- **NVIDIA GTC**: Annual NVIDIA GPU Technology Conference (March each year) reveals the next-generation AI platform architecture. Scorpio X-Series qualification success or failure will often be telegraphed here.
- **aiXscale Product Milestones**: Watch for any Astera press releases on optical transceiver or co-packaged optics demonstration events. A working demo by OFC 2027 would significantly de-risk the optical transition concern.

---

*Memo prepared based on FY2025 annual results (reported February 10, 2026), Q1 2026 guidance, and public filings through Q3 2025. All product characterizations cross-referenced against Astera Labs' official technical documentation and earnings call transcripts. Financial estimates for per-product revenue are analyst-derived from management commentary; Astera does not publicly disclose product-level revenue breakdown.*
