# Lakewatch SIEM Competitive Threat — Equity Analyst Report
**Published:** March 24, 2026 | **Event:** Databricks Lakewatch Launch + Antimatter & SiftD Acquisitions

---

## Executive Summary

On March 24, 2026, Databricks launched **Lakewatch** — an open, agentic SIEM built on its Data + AI Lakehouse platform — and simultaneously announced acquisitions of two security startups: **SiftD** (founded by Splunk's SPL inventor and lead architects) and **Antimatter** (UC Berkeley researchers focused on AI agent authentication). The product is in Private Preview and powered by Anthropic Claude models. Databricks claims up to 80% lower TCO vs. incumbent SIEMs, charges by "work performed" rather than data ingested, and is backed by a formal Open Security Lakehouse Ecosystem including Palo Alto Networks, Zscaler, Okta, and Cribl as partners.

This is not a minor product extension — it is a full-stack assault on the fastest-growing segment in enterprise security, using structural cost advantages from the Lakehouse platform, talent from the very companies it threatens, and AI-native architecture to challenge vendors whose most critical near-term growth vectors all sit in the SIEM/security-analytics category. The launch also coincides with the April 14, 2026 EOL of IBM QRadar SaaS, creating an active customer displacement wave that Databricks can intercept.

**In plain English:** Databricks just turned years of enterprises storing security logs on its platform into a go-to-market beachhead, and hired the people who built Splunk's search engine to weaponize it.

---

## What Lakewatch Sells and Who Buys It

### Core Product
Lakewatch is a SIEM — it ingests, normalizes, correlates, and analyzes security telemetry across an enterprise to detect threats and drive response. Its differentiators vs. incumbents:

| Feature | Lakewatch | Traditional SIEM |
|---------|-----------|-----------------|
| **Data architecture** | Open lakehouse (Delta Lake/Apache Iceberg) | Proprietary/closed |
| **Pricing model** | By compute/work performed | By data ingested (GB/day) |
| **Data retention** | Petabyte-scale, years | Expensive beyond 90 days |
| **AI layer** | Anthropic Claude, custom Agent Bricks | Bolt-on ML models |
| **Multi-modal data** | Security + IT + business data unified | Security data only |
| **Agent capability** | Build, optimize, deploy custom security agents | Limited/none |
| **Vendor lock-in** | Open formats, open ecosystem | Proprietary formats |

### Target Customer
- Enterprises already running Databricks for data/AI workloads (immediate upsell path)
- Security teams with large log volumes chafing against Splunk/CrowdStrike ingest pricing
- SOC teams looking to run AI-driven detection at scale
- Organizations migrating off IBM QRadar SaaS (EOL April 14, 2026)
- Federal/regulated environments that need petabyte retention + auditability

### Core Need Driving Purchases
Two simultaneous pressures: (1) security teams need to ingest and analyze orders-of-magnitude more data due to agentic AI threat surface expansion; (2) existing SIEM pricing models make comprehensive data retention economically impossible. Lakewatch offers to solve both simultaneously.

---

## How They Make Money

Databricks is private but reported $2.4B revenue for FY2025 (ending January 2025) growing ~50% YoY, with annualized revenue estimated at $3.0–3.5B by end of 2025. Lakewatch will be priced by compute consumption on the Databricks platform rather than data ingestion volume — aligning pricing to value delivered rather than penalizing data richness.

This matters strategically: incumbents are locked into data-ingestion pricing models that create customer resentment. Databricks' compute-consumption model both undercuts incumbents and aligns incentives with customers, since customers benefit from storing *more* data rather than being penalized for it.

---

## Competitive Threat Map: Affected Public Companies

### 1. Cisco (CSCO) via Splunk — THREAT LEVEL: CRITICAL

**The SiftD Dimension:** SiftD was founded by the *creator of Splunk's Search Processing Language (SPL)* and the *lead architects of Splunk's search stack*. Their combined 39 years of Splunk experience means Databricks now employs the people who understand Splunk's deepest architectural constraints, performance ceilings, and pricing triggers. This is not coincidental talent acquisition — it is targeted extraction of Splunk's most sensitive institutional knowledge.

**Revenue Exposure:**
- Splunk was acquired by Cisco for $28B in March 2024
- Security segment revenue: $8.09B in FY2025 (+59% YoY), representing ~19.5% of Cisco's total revenue
- Without Splunk, Cisco total revenue would have declined ~14% in the reported period
- Splunk's core product — Splunk Enterprise Security — is the market-share leader in SIEM and the product most directly targeted by Lakewatch

**Structural Vulnerability:**
- Splunk's pricing model (data ingest GB/day) is the most-cited customer complaint in the security market
- Splunk requires expensive per-node compute to run at scale; Databricks runs on cloud compute already deployed in customer environments
- Splunk's SPL is a proprietary query language with steep learning curves; Lakewatch aims for SQL + natural language (via Claude) — far lower friction
- Cisco's Splunk integration is incomplete; SIEM customers are mid-migration, creating instability

**Near-Term Catalyst:** IBM QRadar SaaS EOL (April 14, 2026) creates a pool of enterprise customers who are actively evaluating alternatives right now. Cisco/Splunk was previously the obvious migration target; Lakewatch now directly competes for these accounts.

**Margin Relevance:** Splunk software carries ~80%+ gross margins. Any revenue at risk here is extremely high-margin revenue. Even 5-10% share erosion over 3 years would be material to Cisco's profitability profile.

---

### 2. CrowdStrike (CRWD) — THREAT LEVEL: HIGH

**SIEM as the Next Growth Engine:**
CrowdStrike's Next-Gen SIEM (LogScale) has been the company's fastest-growing product module:
- Q2 FY2026 SIEM ARR: >$430M (+95% YoY)
- Q3 FY2026 SIEM ARR: >$585M (estimated; 100%+ YoY growth)
- SIEM ARR as % of total (~$4.9B ARR): ~12% and growing rapidly
- Cloud + Identity + SIEM bundle: $1.56B ARR total, +40% YoY

CrowdStrike entered the 2025 Gartner Magic Quadrant for SIEM for the **first time** (as a Visionary), signaling the product is still early in enterprise adoption. This is its most promising growth driver at risk.

**Structural Vulnerability:**
- LogScale (formerly Humio) was acquired in 2021 and is still being integrated; it's not yet native Falcon architecture
- CrowdStrike's SIEM pricing (like Splunk) is volume-based ingest — the exact model Databricks is attacking
- CrowdStrike's core value proposition is data gravity in the Falcon platform; Databricks' value proposition is data gravity in the Lakehouse — these are directly competing

**Offset / Moat:** CrowdStrike's endpoint telemetry is proprietary and uniquely high-fidelity. Security teams running CrowdStrike Falcon will continue to need to ingest Falcon data. The question is *where* — in Falcon NG-SIEM or in Lakewatch. Databricks has explicitly shown how to ingest CrowdStrike Falcon events into its platform (a 2021 blog post pre-dates Lakewatch by 5 years; this was planned).

**Margin Relevance:** Platform modules beyond endpoint carry higher incremental margins than endpoint (no hardware/agent costs). SIEM ARR growth at 100%+ is the most important near-term growth vector for CRWD's multiple. Multiple compression risk if Lakewatch disrupts the trajectory.

---

### 3. Palo Alto Networks (PANW) — THREAT LEVEL: MODERATE-HIGH (complex partner/competitor dynamic)

**XSIAM as PANW's Platformization Anchor:**
- XSIAM: ~400 customers as of FY2025, average ARR >$1M per customer → ~$400M+ ARR implied
- FY2025 Revenue: $9.17B; FY2026 guidance: $10.5B (+14% YoY)
- XSIAM and security operations are the central pillar of PANW's "platformization" strategy — the key narrative driving premium multiple

**Complicated Relationship:** PANW is *simultaneously* a partner and a threatened competitor:
- PANW is listed in Databricks' Open Security Lakehouse Ecosystem
- PANW acquired IBM QRadar and is EOL'ing QRadar SaaS (April 14, 2026) — these customers are exactly who Databricks is targeting
- PANW could benefit from Lakewatch if it reduces SOC complexity for joint customers
- But if Lakewatch takes the SOC analytics layer, XSIAM's differentiation and pricing power weakens

**IBM QRadar Factor:** PANW paid for and is now sunsetting QRadar SaaS, intending customers to migrate to XSIAM. Lakewatch intercepts that migration. The PANW-to-XSIAM migration thesis just became more competitive.

**Margin Relevance:** Security ops revenue at PANW carries high margins and is structurally important to the multiple. XSIAM momentum has been the most-cited bull case for the stock. Disruption of XSIAM's ramp would be a significant catalyst for multiple compression.

---

### 4. SentinelOne (S) — THREAT LEVEL: MODERATE

**Singularity AI SIEM is Early But Growing:**
- FY2026 total revenue: $1.0B (+22% YoY); total ARR: ~$1.0B
- Non-endpoint modules (Cloud, Identity, SIEM/Data Lake) now ~50% of new quarterly bookings
- Singularity AI SIEM listed on AWS Marketplace (June 2025)
- Purple AI (generative AI security analyst): 40%+ attach rate on new licenses; >50% inclusion rate in Q4 FY2026 bookings

**Structural Vulnerability:**
- SentinelOne is still building out its SIEM; it lacks the distribution, brand, and enterprise credibility of Splunk/PANW/CRWD in security operations
- Its AI SIEM is genuinely competitive on technology but faces the same pricing model risk (Singularity Data Lake charges on data volume)
- Purple AI is its most important differentiator — but Lakewatch/Claude is also positioning as AI-native

**Relative Resilience:** SentinelOne's Singularity SIEM is less entrenched in enterprise commitments, meaning less displacement risk *currently*, but also less installed base to defend. It's more of a greenfield TAM threat than an installed base churn threat.

---

### 5. Elastic (ESTC) — THREAT LEVEL: MODERATE

**SIEM as a Key Security Use Case:**
- FY2025 revenue: $1.483B (+~17% YoY); FY2026 guidance: ~$1.72B
- Recognized as **Gartner SIEM Visionary** (2025 Magic Quadrant)
- Signed $26M CISA contract for unified SIEM-as-a-service (federal validation)
- Recently added native SOAR workflows to eliminate the "SOAR automation tax"

**Structural Vulnerability:**
- Elastic's SIEM is built on its search platform, which itself competes with Databricks for analytical workloads
- No explicit SIEM revenue disclosure makes % at risk harder to quantify but likely meaningful (~25-35% of security segment estimated)
- Elastic's pricing (indexed data volume) is also the ingest-based model Databricks attacks

**Relative Resilience:** Elastic has a strong open-source community, deeply embedded in security workflows through ECS (Elastic Common Schema) and a large base of self-managed deployments. Its CISA win suggests government/regulated verticals where Databricks may face compliance hurdles in the near term.

---

### 6. Fortinet (FTNT) — THREAT LEVEL: MODERATE

**FortiSOC Launched One Day Before Lakewatch — Both in Preview:**
On March 23, 2026 — the day before Lakewatch — Fortinet announced FortiSOC, a unified cloud-delivered SOC consolidating FortiAnalyzer + FortiSIEM + FortiSOAR + FortiTIP into a single service with agentic AI capabilities and MCP (Model Context Protocol) support. The simultaneous emergence of two competing agentic SOC platforms in preview is not coincidence — it reflects the market converging on the same next-generation architecture from different starting points.

- FY2025 revenue: $6.80B; FY2026 guidance: $7.50–7.70B
- Security Operations ARR: ~$434M (Q1 2025, +30.3% YoY) → estimated ~$550M+ by end of 2025
- SecOps as % of total revenue: ~8%

**Structural Vulnerability:**
- FortiSOC and Lakewatch are direct competitors in unified agentic SOC analytics — both in preview simultaneously
- Fortinet's SecOps revenue (~8% of total) is its fastest-growing product category; Lakewatch competes for the same enterprise buyers
- FortiSOC ingests third-party telemetry (not just Fortinet-native), which means it competes with Lakewatch for the analytics layer even at multi-vendor accounts

**Relative Resilience:** Fortinet's go-to-market is dominant in SMB, mid-market, and OT/industrial (SCADA/ICS) — segments where Databricks Lakehouse has almost no penetration. The FortiGate firewall installed base creates tight product bundling that Lakewatch cannot displace via pricing alone. Price-sensitive buyers who chose Fortinet over Splunk will not migrate to a Databricks-infrastructure-dependent platform.

---

### 7. Zscaler (ZS) — THREAT LEVEL: MINIMAL / NET POSITIVE

**Named Partner, Not Competitor — With One Long-Term Watch Item:**
Zscaler is explicitly listed in Databricks' Open Security Lakehouse Ecosystem, and Lakeflow Connect natively ingests Zscaler telemetry as a standard data source. Zscaler has no SIEM product. Its revenue ($2.67B FY2025; ARR $3.36B+ in Q2 FY2026, +25% YoY) comes entirely from Zero Trust access (ZIA, ZPA), AI Security, and Data Security (DSPM/DLP). None of these are directly threatened by Lakewatch.

- Being a named Lakewatch data source *increases* Zscaler's telemetry value proposition — customers running both platforms have an integration that validates ZS log quality as market-standard
- Near-to-medium term, Lakewatch is a **mild positive** for ZS: drives adoption of ZS at accounts that adopt Lakewatch, since Lakewatch needs ZS telemetry

**Long-Term Watch: Antimatter Scope Creep.** Antimatter's focus on provably secure authentication and authorization for AI agents is architecturally adjacent to Zscaler's Zero Trust for AI/machine identity roadmap. If Databricks extends Antimatter beyond SOC into a full AI agent access policy product, that competes with where ZS is growing. This is a 3–5 year horizon risk, not a near-term one.

---

### 8. Rubrik (RBRK) — THREAT LEVEL: LOW

**Different Layer, One Emerging Overlap:**
Rubrik operates in cyber resilience — backup, ransomware recovery, and DSPM (via its Laminar acquisition). Its FY2026 subscription revenue was $1.26B (+53% YoY) with subscription ARR of $1.46B (+34% YoY) and 80.1% gross margins. This is a fundamentally different market from SIEM: Rubrik protects data *at rest* and enables recovery *after* a breach; Lakewatch detects threats *in flight* from telemetry.

**Where overlap is emerging:** Rubrik's **Agent Cloud** (launched 2026) monitors agentic AI actions, enforces guardrails, and audits agent changes across enterprise data. Databricks' **Antimatter** acquisition targets provably secure auth/authz for AI agents within the SOC. Both are staking a claim to "who governs AI agents' access to sensitive data" — different framing, converging use case. This is nascent but worth monitoring as agentic AI adoption accelerates.

Rubrik's core business (backup telemetry, ransomware detection on snapshots) is insulated because it uses a unique data source no SIEM can access and charges per data protected — not per log ingested. The Lakewatch pricing disruption doesn't touch Rubrik's model.

---

## Revenue Quality Assessment by Company

| Company | Ticker | SIEM/SecOps ARR (est.) | % of Total Revenue | Pricing Model at Risk | Revenue Predictability |
|---------|--------|------------------------|--------------------|-----------------------|----------------------|
| Cisco/Splunk | CSCO | ~$3.5–4.0B (Splunk ES) | ~9–10% Cisco total | Data ingest (GB/day) | High — multi-year contracts |
| CrowdStrike | CRWD | ~$585M NG-SIEM ARR | ~12% of total ARR | Data ingest + platform | High — platform lock-in |
| Palo Alto Networks | PANW | ~$400M XSIAM ARR | ~4–5% of total | Per-node + data | High — platformization deals |
| SentinelOne | S | ~$150–200M est. | ~15–20% of ARR | Data lake ingest | Medium — still ramping |
| Elastic | ESTC | ~$400–500M est. | ~27–34% of revenue | Indexed data volume | High — subscriptions |
| Fortinet | FTNT | ~$550M+ SecOps ARR | ~8% of revenue | Bundled firewall contract | High — hardware renewal cycles |
| Zscaler | ZS | None (no SIEM product) | 0% direct exposure | Per-user/seat (not ingest) | **Net positive** — ecosystem partner |
| Rubrik | RBRK | None (different market) | 0% direct exposure | Per-data-protected | Insulated — backup model unaffected |

---

## Cost Structure and Margin Implications

The structural issue is that SIEM/security-analytics software carries **the highest gross margins in each company's portfolio** (typically 75–85% gross margin) because it is pure software with no hardware dependency. This means:

1. Any dollar of SIEM revenue lost to Databricks represents the **most profitable revenue** being displaced
2. Pricing competition initiated by Lakewatch's 80%-lower-TCO claim will compress ASPs even in accounts Databricks does not win
3. The pricing pressure effect arrives faster than the displacement effect — expect ASP compression in SIEM renewals beginning H2 2026

---

## Competitive Edge Assessment: Who Has What to Defend

| Company | Primary Moat in SIEM | Moat Durability vs. Lakewatch |
|---------|---------------------|-------------------------------|
| Cisco/Splunk | SPL ecosystem, detection content library, 20 years of enterprise trust | **Weakening** — SiftD acquisition puts SPL architects at Databricks |
| CrowdStrike | Endpoint data gravity, Falcon single-agent architecture | **Moderate** — endpoint moat is strong; SIEM moat less so |
| Palo Alto | XSIAM workflow integration with Cortex, QRadar migration program | **Moderate-Weak** — partner overlap with Databricks complicates response |
| SentinelOne | AI-native architecture, Purple AI brand | **Moderate** — youngest platform, most malleable to compete or partner |
| Elastic | Open-source community, ECS standard, developer adoption | **Moderate** — open-source nature may enable Lakewatch interoperability rather than displacement |
| Fortinet | FortiGate firewall install base, SMB/OT dominance, bundled pricing | **Moderate** — enterprise SecOps at risk; SMB/OT base structurally insulated |
| Zscaler | Zero Trust platform, per-user pricing, named Lakewatch ecosystem partner | **Strong** — partner status and non-ingest pricing model insulate from disruption |
| Rubrik | Backup data moat (unique telemetry), per-data-protected pricing, Laminar DSPM | **Strong** — different market layer; only Antimatter/agent-governance overlap is nascent |

---

## Growth Driver Impact Analysis

**Near-Term (0–12 months):**
- All five SIEM-exposed companies (CSCO, CRWD, PANW, S, ESTC) are in active QRadar-displacement cycles. Lakewatch is now a fourth option in those deals.
- SIEM deal cycles elongate as buyers introduce Lakewatch as a negotiating tool, even if Databricks doesn't win.
- Pricing pressure accelerates. Expect ASP compression on CrowdStrike NG-SIEM and XSIAM renewals.
- Fortinet's FortiSOC (launched same week as Lakewatch, also in Preview) now competes directly with Lakewatch in enterprise SOC evaluations — the agentic SOC market just got two new entrants simultaneously.
- Zscaler benefits: named partner status and ZS telemetry ingestion by Lakewatch is a mild positive for ZS customer stickiness.

**Medium-Term (12–36 months):**
- Enterprises already running Databricks (majority of Fortune 500) face a natural consolidation pull to add Lakewatch rather than operate a separate SIEM.
- The "data platform + SIEM" bundled pitch mirrors how AWS/Azure won back observability workloads from Datadog/New Relic/Splunk in 2021–2023.
- SiftD's team enables rapid SPL-compatible migration paths — reducing the #1 switching cost from Splunk.

**Long-Term (36+ months):**
- If agentic security becomes the dominant paradigm, native AI-agent platforms (Databricks + Anthropic) may have a structurally superior position to security-native vendors bolting on AI.
- The "security data lake as SIEM" architecture that was previously a niche pattern (Anvilogic, Panther) is now being productized at Databricks scale.

---

*Sources: Databricks press releases (March 24, 2026), CrowdStrike Q3 FY2026 results (December 2025), PANW FY2025 earnings, SentinelOne FY2026 results, Elastic Q1 FY2026 results, 2025 Gartner Magic Quadrant for SIEM, CNBC. Extended analysis: Fortinet FY2025 full year results + FortiSOC launch (March 23, 2026), Zscaler Q2 FY2026 results, Rubrik Q3/FY2026 results, Rubrik DSPM product documentation.*
