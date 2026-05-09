# Cybersecurity Per-Seat Risk from AI Headcount Displacement — Investment Memo

**Date:** March 24, 2026 | **Theme:** SaaSpocalypse impact on cybersecurity per-seat pricing models

---

## 1. Executive Summary

### Investment Thesis

The "SaaSpocalypse" — the repricing of per-seat SaaS business models in response to AI-driven white-collar displacement — is a real and accelerating threat that is **not evenly distributed** across cybersecurity. The companies most exposed are those whose revenue is anchored to a count of human employees: Zscaler (100% per-user) faces an existential architecture challenge, and SentinelOne (majority endpoint, still user-heavy) faces a meaningful transition risk. CrowdStrike and Palo Alto Networks have bifurcated exposure with meaningful natural hedges. Fortinet, Cisco/Splunk, Elastic, and Rubrik are largely to entirely insulated by their pricing models. The key investment question is not whether per-seat revenue will compress — it will — but whether each company's hedge mechanisms (cloud workload expansion, AI agent identity repricin, autonomous AI security product value) mature quickly enough to offset.

**Bull case (per-seat-exposed names):** AI agent proliferation creates a new security attack surface larger than the human surface it replaces; companies that reprice quickly around NHI (non-human identity), cloud workload, and agentic AI security can grow total ARR even as human-seat ARR compresses. The net effect is mix shift, not revenue decline.

**Bear case:** Agent repricing arrives slowly due to competitive pressure and enterprise procurement resistance; human-seat attrition at 15–20% enterprise headcount reduction compresses ARR at ZS/S by $300–700M before offset mechanisms reach scale, driving NRR below 100% and multiple compression in 2026–2027.

**Target investor profile:** Growth investors long ZS or S need to specifically monitor NRR trend and pace of agent-tier product launches. Value investors considering CRWD or PANW should weight the cloud workload and NHI hedge as primary thesis support. ESTC and RBRK are relatively safe harbors within the theme.

---

## 2. Business Model & Unit Economics: Seat-Compression Sensitivity

### Revenue at Direct Risk by Company


| Company            | Ticker | ARR / Revenue Base        | Headcount-Linked Revenue Est.           | $ at Risk (15% headcount decline) | $ at Risk (30% headcount decline) |
| ------------------ | ------ | ------------------------- | --------------------------------------- | --------------------------------- | --------------------------------- |
| Zscaler            | ZS     | $3.36B ARR                | ~$3.36B (100%)                          | ~$500M                            | ~$1.0B                            |
| SentinelOne        | S      | ~$1.0B ARR                | ~$500–600M (50–60%)                     | ~$75–90M                          | ~$150–180M                        |
| CrowdStrike        | CRWD   | ~$4.9B ARR                | ~$1.5–2.0B (30–40%)                     | ~$225–300M                        | ~$450–600M                        |
| Palo Alto Networks | PANW   | ~$9.2B revenue            | ~$1.8–2.8B (20–30%)                     | ~$270–420M                        | ~$540–840M                        |
| Okta               | OKTA   | ~$3.0B ARR                | ~$1.95–2.1B (65–70% WIC)                | ~$290–315M                        | ~$585–630M                        |
| JFrog              | FROG   | ~$532M revenue            | ~$160–215M (30–40% per-developer seats) | ~$24–32M                          | ~$48–65M                          |
| Fortinet           | FTNT   | ~$6.8B revenue            | ~$340–680M (5–10%)                      | ~$50–100M                         | ~$100–200M                        |
| Cisco/Splunk       | CSCO   | ~$55B revenue             | ~$1.65–2.75B (3–5% security exposure)   | ~$250–415M                        | ~$500–825M                        |
| Elastic            | ESTC   | ~$1.48B revenue           | None material                           | None                              | None                              |
| Rubrik             | RBRK   | ~$1.26B subscription rev. | None                                    | None                              | None                              |
| Datadog            | DDOG   | ~$3.43B revenue           | ~$100–175M (~3–5% On-Call + CI Visibility per-committer) | ~$15–26M | ~$30–52M |


*Note: "Headcount-linked" estimated conservatively; actual exposure depends on endpoint mix, contract structure, and renewal timing.*

### The Agent Repricin Offset

At a 1:5 displacement ratio and 2× agent-tier pricing (realistic near-term assumption):

- Revenue retained from affected accounts: **~40%**
- Net ARR headwind (before new enterprise growth): $200–400M at ZS over a 2–3 year cycle

This analysis explains why ZS stock corrected despite reporting strong Q2 FY2026 numbers — the risk is embedded in future renewals, not current results.

### Operating Leverage Dynamics

Per-seat vendors have strong operating leverage *on the way up* (high incremental margins as seats add without proportional cost). The same lever operates in reverse: seat compression reduces revenue without meaningfully reducing fixed cost bases (engineering, cloud infrastructure, G&A). This implies **margin compression coincides with revenue compression** — a double pressure that is not offset by pure headcount reduction.

---

## 3. Competitive Position & The NHI Hedge Race

The most important strategic dynamic in this theme is the race to reprice around **non-human identity (NHI)** and AI agent security. The company that establishes itself as the go-to platform for securing AI agents gains a new billable surface that partially compensates for lost human-seat revenue.

### Agentic Product Readiness & Seat-Loss Mitigation Matrix

The following table scores each company's current readiness to offset seat attrition through agent/NHI pricing. Scores reflect product status as of March 24, 2026.


| Company                | Key Agentic Product(s)                                                            | Status                                                         | Architectural Fit | Mitigation Strength | Net Assessment                                                                      |
| ---------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------------- | ------------------- | ----------------------------------------------------------------------------------- |
| **Datadog**            | LLM Observability; Bits AI SRE Agent; TOTO time-series model; AI Security; MCP Server | All GA 2024–2025 | ★★★★★             | N/A (net positive)  | Consumption model grows with AI workload — every AI agent is a billable host; no repricing needed |
| **JFrog**              | JFrog Fly (agentic repo); MCP Server; MCP Registry                                | MCP Server: GA July 2025; Fly: GA early 2026                   | ★★★★★             | ★★★★★               | No repricing needed — consumption grows with agent code volume                      |
| **Okta**               | Okta for AI Agents; Auth0 for AI Agents; ISPM for NHI                             | GA April 30, 2026                                              | ★★★★★             | ★★★★                | Direct mechanism: NHI module on existing platform; 50:1 NHI ratio creates 10× TAM   |
| **CrowdStrike**        | Charlotte Agentic SOAR; Falcon for AI Workloads on AWS; FedRAMP High Charlotte AI | GA (all)                                                       | ★★★★              | ★★★★                | Falcon Flex redeployment + cloud workload growth + NHI identity extension           |
| **SentinelOne**        | Singularity Identity NHI (GA Feb 2026); Prompt AI Agent Security (RSAC 2026)      | GA                                                             | ★★★★              | ★★★                 | Identity-first NHI; behavioral validation approach is technically ahead of peers    |
| **Rubrik**             | SAGE (Semantic AI Governance Engine); Agent Cloud; Agent Rewind                   | SAGE: announced RSAC 2026; Agent Cloud: GA                     | ★★★★              | ★★                  | Core business already insulated; SAGE/Agent Cloud is TAM expansion not mitigation   |
| **Palo Alto Networks** | Cortex AgentiX (in XSIAM/Cloud); XSIAM NHI detection; AI Agent Discovery          | AgentiX: GA in XSIAM; standalone early 2026                    | ★★★               | ★★★                 | Real product in market but no separate NHI SKU yet; CyberArk integration pending    |
| **Elastic**            | Agent Builder; Elastic Skills library                                             | GA Jan 2026                                                    | ★★★               | N/A                 | Already insulated by volume pricing; agentic tools strengthen competitive position  |
| **Fortinet**           | FortiSOC (agentic SOC execution); FortiAI Application Intelligence                | FortiSOC: Preview                                              | ★★                | ★★                  | Uses agents in SOC; no NHI identity product; core business already mostly insulated |
| **Cisco/Splunk**       | Cisco AI Defense (model-layer); Splunk observability for AI pipelines             | AI Defense: GA; no unified NHI product                         | ★★                | N/A                 | Mostly insulated; no coherent NHI response; fragmented portfolio                    |
| **Zscaler**            | AI Security Suite (Asset Mgmt, MCP Gateway, AI Deception)                         | AI Security Suite: announced Jan 2026; MCP Gateway: no GA date | ★                 | ★                   | Most exposed; farthest from solution; MCP Gateway promising but unshipped           |


### Mitigation Sufficiency by Company

For seat-exposed companies, the critical question is whether agent revenue can **fully offset** projected human-seat losses by 2028. The following assessment combines the seat exposure estimates from Section 2 with the readiness scores above:


| Company            | ARR at Risk (15% HC decline) | Agent Revenue Offset by 2028 (est.)                                                                                                                                                       | Net ARR Impact                 | Confidence                                                                                                          |
| ------------------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Datadog            | ~$15–26M                     | AI workload consumption (LLM Observability, new hosts) adds $200–500M+ ARR by 2028; seat-exposed revenue is self-hedging | **Net strongly positive**      | Very High — pricing model already aligned with AI infra growth; no transition required |
| Okta               | ~$290–315M                   | ~$200–400M (NHI module at 20% human rate; early penetration)                                                                                                                              | **Neutral to positive**        | Medium — product just GA; adoption lag                                                                              |
| JFrog              | ~$24–32M                     | >$50M (consumption growth from AI artifact volume)                                                                                                                                        | **Net positive**               | High — no repricing needed                                                                                          |
| CrowdStrike        | ~$225–300M                   | ~$300–500M (cloud workload + NHI identity + NG-SIEM telemetry expansion)                                                                                                                  | **Net positive**               | High — already GA, Falcon Flex active                                                                               |
| SentinelOne        | ~$75–90M                     | ~$60–120M (NHI module + Purple AI expansion)                                                                                                                                              | **Near neutral**               | Medium — transition underway                                                                                        |
| Palo Alto Networks | ~$270–420M                   | ~$150–250M (AgentiX bundled; CyberArk NHI pending)                                                                                                                                        | **Partial gap remains**        | Medium — execution risk on CyberArk                                                                                 |
| Zscaler            | ~$500M                       | ~$30–80M from AI Asset Mgmt; metered usage (ZT Branch/Cloud, AI tokens) ~$100–200M by 2028; Z-Flex spend-envelope provides soft deferral (no formal seat-to-workload reallocation clause) | **Large gap — ~$300–420M net** | Low-to-medium — Z-Flex defers renewal cliff but no contractual seat swap; metered is real hedge but too small today |


**Key observation:** Non-human identities already outnumber human identities ~50:1 in the average enterprise. If this ratio becomes the new pricing basis, the TAM for NHI security is **50× the TAM** of human identity security — the displacement threat becomes the growth opportunity for vendors positioned correctly.

### Moat Assessment in the Agentic AI Transition


| Company | Moat in AI Agent Era                                                                    | Durability                                                           |
| ------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| ZS      | Weak — proxy architecture doesn't cover agent traffic                                   | **Weakening** — requires new product category                        |
| OKTA    | Strongest — identity IS the NHI control plane; no architectural change needed           | **Strengthening** — NHI is Okta's natural next market at 50× TAM     |
| CRWD    | Strong — Falcon Flex + cloud workload + Charlotte AI                                    | **Stable** — diversified endpoint definition insulates               |
| PANW    | Strong — CyberArk NHI + NGFW throughput insulation                                      | **Strengthening** — CyberArk is the strategic hedge                  |
| FROG    | Moderate — consumption pricing grows with AI code generation; ML model registry new TAM | **Stable-to-improving** — B2A strategy reduces human-seat dependency |
| S       | Moderate — Purple AI + cloud workload mix shift underway                                | **Improving** — pace of transition is key variable                   |
| FTNT    | Strong — hardware/throughput/OT base immune                                             | **Stable** — not exposed, not positioned in NHI                      |
| ESTC    | Strong — ingest-volume pricing benefits from AI telemetry                               | **Strengthening** — AI increases log volume                          |
| RBRK    | Strong — data-volume pricing; AI expands data surface                                   | **Strengthening** — AI data governance tailwind                      |
| DDOG    | Strongest structural alignment — consumption pricing grows with every AI host deployed  | **Strongly strengthening** — AI infra is Datadog's core TAM; no architectural transition required |


---

## 4. Top 3 Growth Drivers & Sensitivities

### Driver 1: Enterprise Headcount Reduction Pace (0–18 Months)

**Description:** The rate at which enterprises reduce white-collar headcount through AI automation determines the speed of seat attrition. Current estimates: 50K+ AI-attributed job cuts in 2025; multiple forecasters project 5M+ white-collar roles at risk by 2028. CHRO and CFO survey data shows most enterprises targeting 10–20% knowledge-work headcount reduction over 3 years.

**Sensitivity Table (impact on ZS ARR as proxy for maximum seat exposure):**


| Headcount Reduction Rate | Time Horizon | ZS ARR at Risk | ZS NRR Impact (no agent offset) |
| ------------------------ | ------------ | -------------- | ------------------------------- |
| 5% (slow adoption)       | 2 years      | ~$168M         | ~95% NRR                        |
| 15% (base case)          | 2–3 years    | ~$504M         | ~85% NRR                        |
| 30% (accelerated)        | 3 years      | ~$1.0B         | ~70% NRR                        |


**Milestones to watch:** Enterprise CHRO surveys on AI-driven headcount plans (Q2–Q3 2026); Zscaler management commentary on seat count trends in next earnings call (expected June 2026).

> **Z-Flex Watch:** Z-Flex TCV (~$650M cumulative, $290M in Q2 FY2026) provides a *soft, negotiated* hedge against seat attrition — not a structural one. There is **no formal reallocation clause** allowing customers to trade unused human seats for Workload or AI Guardrail credits mid-contract. The "module swap" flexibility in Z-Flex means customers can add or substitute security capability modules without a new procurement cycle, but seat counts are fixed at contract signing and mid-term reductions require renegotiation. The indirect benefit: Z-Flex's spend-envelope structure (committed dollars, not strictly committed seats) means customers that maintain flat security budgets despite headcount reduction can redirect committed spend toward Zero Trust Branch, Zero Trust Cloud, or AI Guard modules rather than losing it to lapsed seat capacity. This is case-by-case commercial flexibility, not a contractual right. The structural loss still crystallizes at renewal. The signal that matters is Zscaler's **non-seat metered ARR** (Zero Trust Branch, Zero Trust Cloud, AI token-based security): >25% of new ACV as of Q2 FY2026, growing 100%+ YoY. If metered usage reaches 35–40% of new ACV within four quarters, the structural transition is on track. If it stalls below 25%, Z-Flex renewals in 2028–2029 will face headcount-driven renegotiation with limited offset.

---

### Driver 2: Agent Repricin Speed and Market Acceptance (12–36 Months)

**Description:** Each cybersecurity vendor is building or planning product tiers that charge for securing AI agents as distinct identities or workloads. The speed at which these tiers reach GA, achieve market acceptance, and hit material revenue determines whether the seat compression is a permanent impairment or a temporary revenue gap.

**Probability-Weighted Scenarios:**


| Scenario | Description                                                                       | ZS Revenue by 2028                       | CRWD Revenue by 2028   |
| -------- | --------------------------------------------------------------------------------- | ---------------------------------------- | ---------------------- |
| Bear     | Agent products delayed 24+ months; seat attrition accelerates; pricing power weak | $3.0B (flat/down)                        | $7.5B (+modest growth) |
| Base     | Agent products GA in 12–18 months; 1.5× human pricing; ~40% revenue offset        | $3.5B (+modest growth despite attrition) | $8.5B (+solid growth)  |
| Bull     | Agent products GA in <12 months; 3× human pricing; 60%+ offset; NHI TAM expansion | $4.2B (continued growth)                 | $10B+ (acceleration)   |


---

### Driver 3: Non-Human Identity TAM Realization (24–60 Months)

**Description:** If the market prices NHI security at even a fraction of what human identity security commands, the TAM expansion from ~50 non-human identities per human identity is enormous. CyberArk/PANW, CrowdStrike, and SentinelOne are all positioned to capture this expansion. Zscaler must build a new product.

**TAM math:** Current identity security market ~$15–20B (human-focused). At 50:1 NHI ratio and even 0.2× per-NHI pricing vs. per-human pricing, NHI TAM = $150–200B theoretical ceiling. Realistically, 5–10% market penetration by 2030 = $7.5–20B addressable NHI security market.

**Milestone:** Watch CyberArk (PANW-integrated) NHI ARR disclosures; CrowdStrike Falcon Identity non-human account growth; PANW NHI-specific commentary at next investor day.

---

## 5. Risk Framework

### Top 5 Risks (Severity × Probability)


| Rank | Risk                                                                        | Trigger                                                                                                                                 | Company Most Affected                             | Severity                                                 |
| ---- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------- |
| 1    | **NRR inflects below 100% at ZS before agent repricin**                     | 2026–2027 renewals arrive as headcount has been reduced; agent products not yet GA                                                      | ZS                                                | Critical × High = **Critical**                           |
| 2    | **Endpoint vendors (CRWD, S) unable to reprice cloud workload fast enough** | AI infrastructure grows but customer contracts lock in old endpoint-only rates; Falcon Flex terms restrict redeployment                 | CRWD, S                                           | High × Medium = **High**                                 |
| 3    | **NHI market develops more slowly than expected**                           | Enterprises treat AI agent identity as an IT operations problem, not a security problem; procurement resists premium agent-tier pricing | PANW, CRWD, S                                     | High × Medium = **High**                                 |
| 4    | **Pricing compression across the board**                                    | ZS cuts prices to retain seat volume; cascades to CRWD/S as competitors; compresses ASPs industry-wide                                  | ZS, S, CRWD                                       | Medium × High = **High**                                 |
| 5    | **Regulatory mandate for AI agent security accelerates NHI market**         | EU AI Act, SEC disclosure requirements, or FedRAMP for AI agents mandate independent security auditing of NHI                           | ZS (benefits if builds it), PANW (strong benefit) | Medium × Medium = **Medium** (upside risk, not downside) |


### Pre-Mortem: If the Per-Seat Thesis Materializes Badly

*"If ZS or S see significant ARR contraction by 2028, the most likely sequence is:* Enterprise customers begin reducing Zscaler seat counts at 2026 renewals, citing AI-reduced headcount; ZS management initially attributes it to customer consolidation; by Q3 2026, NRR drops from ~120% to ~108%; by Q4 2026, it drops to ~100%; the agent-tier product launches in H1 2027 but enterprise procurement moves slowly; by Q4 2027, NRR is ~95% and multiples compress from 15× ARR to 8× ARR, erasing 40–50% of market cap."

### Key Assumptions for the Positive Scenario

1. Enterprise headcount reduction stays below 15% over 3 years (gradual, not abrupt)
2. AI agent security pricing achieves 2×–3× human-tier rates within 18 months of product GA
3. CrowdStrike Falcon Flex contracts allow mid-term license redeployment from user endpoints to cloud workloads without revenue loss
4. PANW CyberArk NHI integration accelerates rather than dilutes PANW's platformization narrative
5. Zscaler ships a credible AI agent access control product by H2 2026

---

## 6. 12-Month KPI Watch List


| #   | KPI                                             | Current Value                                          | Target (Positive)                                    | Red Flag Threshold                                                                                  | Source / Frequency                                                    |
| --- | ----------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1   | **Zscaler NRR**                                 | ~120% (FY2025 est.)                                    | Stays above 115%                                     | Falls below 110%                                                                                    | Zscaler quarterly earnings (next: ~June 2026)                         |
| 2   | **Zscaler Seat Count Trend**                    | Not disclosed explicitly                               | Management guides stable or growing seat counts      | Management discloses seat count pressure or removes seat-count commentary                           | Zscaler earnings call Q&A                                             |
| 3   | **ZS AI Agent Access Product GA**               | Pre-GA / roadmap                                       | GA announcement by Q3 2026                           | No mention in next two earnings calls                                                               | Zscaler product announcements / RSA 2026                              |
| 4   | **SentinelOne Cloud/Identity % of Bookings**    | ~50% of new bookings                                   | >60% by Q4 FY2027                                    | Drops back below 45%                                                                                | SentinelOne quarterly earnings (next: ~June 2026)                     |
| 5   | **CrowdStrike Cloud Security Module ARR**       | Part of $1.56B bundle                                  | Explicit cloud workload ARR disclosure >$500M        | No separate cloud disclosure; bundle growth decelerates                                             | CrowdStrike quarterly earnings (next: ~June 2026)                     |
| 6   | **PANW NHI / CyberArk ARR Post-Integration**    | Not yet broken out                                     | First NHI ARR disclosure at next investor day        | No NHI-specific disclosure by FY2027                                                                | PANW investor day / quarterly earnings                                |
| 7   | **Enterprise CHRO Headcount Survey Data**       | 10–20% 3-year reduction targets (survey data, Q1 2026) | Reduction pace stays at low end (<10% over 2 years)  | Surveys show acceleration to >25% reduction in 2 years                                              | SHRM / Gartner workforce surveys (quarterly)                          |
| 8   | **Per-Agent Pricing Tier Announcements**        | None publicly disclosed at scale                       | 2+ major vendors announce agent-tier SKUs by Q3 2026 | No agent-tier pricing by end of 2026 (implies product delays)                                       | Vendor product launches / RSA 2026 / AWS re:Inforce                   |
| 9   | **AI-Generated Telemetry Volume at Elastic**    | Not disclosed separately                               | Management notes AI-workload data as a growth driver | No AI-telemetry commentary; security ARR growth decelerates                                         | Elastic quarterly earnings (next: ~May 2026)                          |
| 10  | **ZS Stock vs. CRWD/PANW Relative Performance** | ZS already corrected double digits (Feb 2026)          | ZS outperforms after agent product announcement      | ZS underperforms CRWD by >20% over 6 months (signals market pricing in permanent NRR impairment)    | Daily market data                                                     |
| 11  | **Okta NRR Trend**                              | ~106% (Q4 FY2026)                                      | Stabilizes at 108%+ as NHI attach begins             | Falls below 103% (WIC seat attrition outpacing NHI gains)                                           | Okta quarterly earnings (next: ~June 2026)                            |
| 12  | **Okta for AI Agents Revenue Contribution**     | GA April 30, 2026; no revenue disclosed yet            | First material NHI ARR disclosure by Q3 FY2027       | No mention in next two earnings calls despite widespread agent adoption                             | Okta earnings calls / Showcase 2026                                   |
| 13  | **JFrog Cloud Revenue Growth Rate**             | +45% YoY ($243M, FY2025)                               | Sustains 30%+ growth; cloud becomes >50% of total    | Cloud growth decelerates below 25% YoY (signals CI/CD pipeline activity slowing)                    | JFrog quarterly earnings (next: ~May 2026)                            |
| 14  | **JFrog ML Model Registry Traction**            | Launched 2025; NVIDIA + Hugging Face partnerships      | First $100M ARR milestone from ML/model management   | No mention of ML registry customers or ARR contribution by end of 2026                              | JFrog earnings Q&A / SwampUP 2026 conference                          |
| 15  | **ZS Metered Usage % of New ACV**               | >25% of new ACV (Q2 FY2026); ARR +100%+ YoY            | Reaches 35–40% of new ACV within 4 quarters          | Stalls below 25% or management stops disclosing metric (signals structural seat dependence remains) | Zscaler quarterly earnings; mgmt commentary on Z-Flex vs. metered mix |


---

## Appendix: The Architectural Bypass Summary

The table below summarizes which security architectures are structurally bypassed by AI agent traffic — the deepest form of per-seat risk because it requires new product development, not just repricing.


| Security Product              | Human Traffic Pattern                       | AI Agent Traffic Pattern                                       | Bypassed?                                                                       | Remediation Required                                             |
| ----------------------------- | ------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Zscaler ZIA                   | Browser → proxy tunnel                      | SDK/API client → endpoint directly                             | **Yes — fully bypassed**                                                        | New API-gateway proxy product                                    |
| Zscaler ZPA                   | SSO/SAML login → app                        | Client credentials / service token → app                       | **Yes — fully bypassed**                                                        | New non-human ZTNA product                                       |
| CrowdStrike Falcon (endpoint) | Agent on managed laptop                     | Agent on cloud VM / container                                  | **Partially** — cloud agent deployed separately                                 | Falcon Cloud Security (already GA)                               |
| PANW Prisma Access            | User tunnels to apps                        | Service accounts call APIs                                     | **Yes for ZTNA**                                                                | AI ZTNA / NHI policy needed                                      |
| PANW NGFW                     | All traffic flows through firewall          | All traffic still flows through firewall                       | **No**                                                                          | No change needed                                                 |
| SentinelOne Endpoint          | Agent on managed laptop                     | Agent on cloud VM / container                                  | **Partially**                                                                   | Singularity Cloud (GA, growing)                                  |
| Fortinet FortiGate            | All traffic through appliance               | All traffic through appliance                                  | **No**                                                                          | No change needed                                                 |
| Splunk SIEM                   | Log events from user actions                | Log events from agent actions                                  | **No**                                                                          | Higher volume; same pricing                                      |
| Elastic SIEM                  | Log events from user actions                | Log events from agent actions                                  | **No**                                                                          | Higher volume; higher revenue                                    |
| Rubrik                        | Backup data from all systems                | Backup data from AI systems too                                | **No**                                                                          | More data; higher revenue                                        |
| Okta WIC/CIC                  | SSO/MFA for human employee logins           | OAuth2 client credentials; service tokens; API keys for agents | **Partially** — human SSO flows bypassed; agent auth uses different OAuth flows | Okta for AI Agents / NHI module (GA April 2026) extends coverage |
| JFrog Artifactory             | Human developers push artifacts via CLI/IDE | AI coding agents push artifacts via API/SDK; MCP integration   | **No** — API-first platform; consumption billing applies equally                | B2A (business-to-agent) via MCP server already in progress       |
| Datadog Agent (all products)  | DevOps/SRE teams deploy on managed hosts    | AI agents, LLM servers, GPU nodes all run on Datadog-monitored hosts | **No** — host-based billing applies to AI infra identically; LLM Obs adds new consumption layer | Already billed; AI telemetry density per host increases revenue per node |


---

*Sources: Financial Content SaaSpocalypse series (March 2026), Zscaler Q2 FY2026 earnings, CrowdStrike pricing documentation (CyCognito, Vendr), PANW Prisma Access licensing guide + PeerSpot mindshare data, SentinelOne NHI security blog, CyberArk NHI security blog + 2026 predictions, Help Net Security agentic AI enterprise surveys (February–March 2026), TokenRing agentic displacement report (December 2025), InvestorPlace AI job displacement analysis (February 2026), ALM Corp AI displacement statistics 2026. Extended: Okta Q4 FY2026 earnings (March 4, 2026) + Okta for AI Agents GA announcement + Okta NHI platform innovation press release + Futurum agentic identity positioning analysis; JFrog FY2025 full year results + Q4 2025 earnings call + JFrog Trusted AI 2026 Playbook + CloudRepo Artifactory pricing guide. Agentic readiness update (March 24, 2026): Okta Showcase 2026 + Okta for AI Agents launch details (SiliconANGLE, HyperFRAME Research, Walseth AI); CrowdStrike Charlotte Agentic SOAR + AWS Agentic AI Specialization + FedRAMP High announcement (BusinessWire); SentinelOne RSAC 2026 NHI + Prompt AI Agent Security launch (BusinessWire, Help Net Security, SecurityMEA); PANW Cortex AgentiX + AI Agent Discovery + NHI workload identity framework (Network World, SecurityInfoWatch); Rubrik SAGE + Agent Cloud + Agent Rewind (Help Net Security, BusinessWire, Security Boulevard); JFrog Fly + MCP Server + MCP Registry (JFrog press room, SiliconANGLE, ITBrief); Fortinet FortiAI Application Intelligence + FortiSOC agentic AI (Fortinet newsroom); Zscaler AI Security Suite + MCP Gateway (Zscaler IR, Help Net Security); Elastic Agent Builder + Elastic Skills (Help Net Security, GitHub).*