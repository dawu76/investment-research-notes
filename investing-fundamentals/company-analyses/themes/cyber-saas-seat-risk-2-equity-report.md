# Cybersecurity Per-Seat Risk from AI Headcount Displacement — Equity Report
**Published:** March 24, 2026 | **Theme:** AI-driven white-collar automation and per-seat SaaS license attrition

---

## Executive Summary

The accelerating deployment of agentic AI tools across enterprise knowledge-work functions is creating a structural challenge for cybersecurity vendors whose revenue is priced on a per-human-user or per-human-endpoint basis. Labeled the "SaaSpocalypse" by analysts, this dynamic erased nearly $2 trillion in B2B software market cap in Q1 2026 as investors repriced the assumption of stable or growing human headcount underlying SaaS seat models.

For cybersecurity specifically, the threat operates through three concurrent channels: (1) direct seat attrition as white-collar workers are reduced and endpoint/user licenses lapse; (2) architectural bypass — AI agents typically call APIs directly, sidestepping proxy-based and browser-centric security products built for human traffic; and (3) pricing model mismatch — new AI agent workloads require security coverage but don't fit neatly into human-seat pricing tiers, creating a revenue gap before repricin catches up.

The critical analytical divide is **pricing metric, not product category**: vendors charging per human user face direct headcount attrition; vendors charging per data volume, per network throughput, or per cloud workload are structurally insulated — and may benefit from AI-generated telemetry expansion. A meaningful natural hedge exists for vendors whose platform already prices on cloud workloads and non-human identity, as AI agent infrastructure proliferates faster than human headcount shrinks.

**In plain English:** The companies at risk are those that assumed every employee is a billable unit. The companies insulated are those that bill the infrastructure, not the people using it.

---

## Macro Context: Seat Compression at Enterprise Scale

A "seat compression" wave documented through late 2025 and into Q1 2026 shows one AI agent replacing approximately **five human knowledge workers** at comparable output. At equal per-seat pricing, this implies:

- 2,500 workers replaced by 500 AI agents = **80% license revenue lost per account** before agent repricin
- For agent repricin to fully offset, agent-tier pricing must be **5× per-human rates** — unlikely near-term
- Realistic near-term offset: agent-tier pricing at 1×–2× human rates → **60–80% net revenue compression** per affected account

This math is severe for pure per-human-seat vendors. Companies that can charge on agent-infrastructure dimensions (workload count, API call volume, data processed) face a much smaller gap.

Data points:
- 50,000+ U.S. white-collar job cuts explicitly attributed to AI automation in 2025
- Anthropic CEO: ~50% of entry-level white-collar positions at risk within five years
- Microsoft data: 5 million white-collar jobs (management analysts, customer service, sales engineering) facing extinction
- Non-human identities already outnumber human identities ~50:1 in the average enterprise — the scale of agent infrastructure being secured is vastly larger than human workforce

---

## The Architectural Bypass Problem

Beyond pricing, several cybersecurity architectures face a deeper challenge: they were **physically built for human traffic patterns** and don't intercept AI agent traffic by design.

| Human User Behavior | AI Agent Behavior | Architectural Impact |
|--------------------|--------------------|---------------------|
| Browser → proxy tunnel → internet | SDK/HTTP client → API endpoint directly | Proxy-based security (ZIA) bypassed entirely |
| SSO login via identity provider | OAuth2 client credentials / API key auth | ZTNA (ZPA) never invoked for agent traffic |
| Managed laptop endpoint with agent installed | Containerized workload, serverless function | Endpoint agent not deployed; different tooling needed |
| Human-generated log events (login, file access) | Machine-speed events (thousands/sec per agent) | Log volume explosion; SIEM pricing models may diverge |
| Predictable 9-to-5 usage patterns | Always-on, variable, bursty | Behavioral analytics baselines invalidated |

---

## Company-by-Company Analysis

### 1. Zscaler (ZS) — SEAT RISK: CRITICAL

**Revenue Model:** ~100% per-human-user (ZIA at ~$6–10/user/month; ZPA at similar rates). No meaningful revenue from workload, throughput, or data-volume pricing.

**Direct Exposure:**
Every white-collar worker eliminated removes exactly one ZIA seat and one ZPA seat with no partial offsets. Zscaler's ~$3.36B ARR (Q2 FY2026, +25% YoY) is almost entirely a function of the count of human employees at enterprise customers. A sustained 15–20% enterprise headcount reduction over two to three years implies direct ARR headwind of ~$500M–670M at no change in customer count or pricing.

**The Architectural Problem:**
ZIA routes human *browser traffic* through Zscaler's cloud proxy — AI agents using SDKs or API clients bypass this entirely. ZPA authenticates human users through identity providers via SAML/OIDC — AI agents use client credentials flows, service account tokens, or API keys that ZPA never sees. Zscaler's architecture is not a software configuration issue; it is a fundamental product-design assumption. Building a ZIA/ZPA equivalent for AI agent traffic requires a new product, not a pricing tier update.

**Compensating Factors:**
- Zscaler raised prices ~35%+ on many SKUs (August 2025), buying short-term revenue resilience even with seat count compression
- DSPM (Data Security Posture Management) product is an early bet on non-human data security — not yet at material scale
- Q2 FY2026 results remained strong (+26% YoY) driven by platform upsell and ASP expansion — masking underlying seat-count risk
- ZS stock already corrected double-digits in February 2026 on seat-compression fears; some risk may be partially priced

**Z-Flex and Metered Usage — Structural Mitigation Assessment:**

Z-Flex is Zscaler's most-cited commercial response to seat-compression concerns, but the mechanism is widely misunderstood. **Z-Flex is a multi-module, multi-year commitment vehicle** (typically 3–5 year terms, average ~4 years), not a consumption-based or per-workload pricing model. Management has explicitly stated it "doesn't change model mechanics." The pricing is predefined at contract inception; customers commit to a seat count and a suite of modules, and the flexibility is in which modules they deploy — not whether seats are counted. Key metrics: ~$290M TCV booked in Q2 FY2026 (+65% QoQ), ~$650M cumulative; average deal is eight-figure TCV.

**What Z-Flex actually does and does not do:**

| Mechanism | Description | Seat-Loss Mitigation |
|-----------|-------------|---------------------|
| Z-Flex multi-year terms | Locks in today's committed spend for 3–5 years at fixed rates | **Low-to-moderate** — delays renewal cliff; spend envelope softens seat attrition (see below) |
| Z-Flex module swapping | Customers can add/swap security modules mid-contract without a new procurement cycle | **Soft hedge** — no formal reallocation clause; module redirects are negotiated case-by-case |
| Spend-envelope structure | Because Z-Flex commits dollars (not strictly seats), customers maintaining budget but losing headcount can redirect spend to non-seat modules | **Indirect and partial** — requires Zscaler cooperation; not a contractual right |
| Price increases (~35%, Aug 2025) | Higher per-seat ASP offsets volume compression | **Temporary** — masks compression; erodes competitiveness at renewal |
| Metered non-seat offerings | Zero Trust Branch, Zero Trust Cloud, AI token-based security | **Moderate and growing** — the real structural hedge |

**On the question of a formal seat-to-workload reallocation clause:** No such mechanism is publicly documented. There is no contractual provision allowing customers to formally "trade in" unused human seats for Workload or AI Guardrail credits at a defined exchange rate mid-contract. Management describes Z-Flex as allowing customers to "swap in and out of modules as business dynamics change" and to "redeploy committed spend across new modules without additional procurement cycles" — but this language refers to adding or substituting *security capability modules*, not converting seat-denominated capacity into workload/consumption capacity. Seat counts are fixed at contract signing; mid-term reductions require renegotiation.

The indirect mechanism that *does* exist: Z-Flex's spend-envelope structure means a customer that maintains flat security budget despite headcount reduction could redirect committed dollars toward Zero Trust Branch, Zero Trust Cloud, or AI Guard modules rather than leaving them unused in lapsed seat capacity. This is not a formal clause — it is an emergent commercial flexibility that Zscaler's account teams would facilitate. It provides a soft, negotiated hedge that is meaningfully better than pure per-seat annual contracts (where attrition hits NRR immediately) but is not a structural protection. The structural loss crystallizes at renewal when the new seat count anchors the next commitment.

**The distinction that matters: Z-Flex vs. metered usage.** The genuinely seat-decoupled revenue stream at Zscaler is its *non-seat metered offerings* — a separate product category from Z-Flex. These include Zero Trust Branch (per-branch/device), Zero Trust Cloud (per-cloud-workload), and AI Security products priced on AI transactions/tokens. As of Q2 FY2026, this metered category represented **>25% of new ACV**, with ARR growing **100%+ YoY**. Zscaler processed approximately 1 trillion AI transactions in calendar 2025, and management expects AI agent traffic (machine-to-machine, MCP request flows) to drive this category further. This is the actual seat-decoupled mechanism — and it is growing.

**Quantified mitigation gap:** If metered ARR is ~15–20% of total (~$500–670M), and the seat-exposed base at risk in a 15% headcount decline scenario is ~$500M, metered usage would need to roughly double its current base *just to offset the attrition* — requiring approximately 2–3 more years of 100%+ ARR growth at current trajectory. In the meantime, the gap is real and the duration risk is in multi-year Z-Flex deals: at renewal (years 4–5), if enterprise customers have 20% fewer employees, they negotiate proportionally smaller commitments.

**Bottom line on Z-Flex:** It is a **retention and upsell vehicle with a soft, negotiated hedge against seat attrition — but no formal reallocation clause**. The spend-envelope structure is better than annual per-seat contracts (attrition impact is deferred to renewal rather than immediate), but worse than a true consumption model. The metered usage category remains the correct structural signal to watch; its trajectory over the next 4–6 quarters is the leading indicator of whether Zscaler successfully transitions to a pricing model that survives the SaaSpocalypse.

**The key question for ZS investors:** Can Zscaler ship a credible AI agent access control product (essentially a Zero Trust layer for non-human API traffic) before NRR inflects downward on headcount-driven renewals? Current evidence suggests this product is 12–24 months from commercial readiness. Z-Flex buys time — metered usage buys structural insulation. Only the latter solves the problem.

---

### 2. SentinelOne (S) — SEAT RISK: HIGH (partially offsettable)

**Revenue Model:** Per-endpoint (Singularity Endpoint), per-cloud-workload (Singularity Cloud Security), per-identity credential (Singularity Identity). Mix is shifting: cloud/identity modules now ~50% of new bookings.

**Direct Exposure:**
The Singularity Endpoint business tracks closely with managed user laptop count. Each white-collar worker eliminated removes one endpoint license. Total ARR: ~$1.0B (FY2026); endpoint is still the majority of existing ARR despite the mix shift.

**Natural Hedge:**
- Cloud workload protection (containers, VMs, Kubernetes nodes) grows proportionally with AI infrastructure deployment — every AI agent cluster running in the cloud is a new Singularity Cloud workload
- Singularity Identity explicitly targets non-human identity (NHI) security, meaning AI agent credentials are a billable surface
- **Purple AI is the most important strategic hedge:** as SOC teams shrink due to AI automation of analyst tasks, Purple AI's autonomous threat detection and response grows in value per deployment, potentially increasing ARR per customer even as headcount falls

**Net Assessment:**
SentinelOne is in transition. The legacy endpoint book is headcount-exposed; the cloud/identity/AI-SIEM book is headcount-insulated. The speed of mix shift determines whether the hedge works. At current pace (~50% of new bookings in cloud/identity), the insulated portion reaches majority of total ARR in approximately 18–24 months.

---

### 3. CrowdStrike (CRWD) — SEAT RISK: LOW-MODERATE (strong natural hedge)

**Revenue Model:** Per-endpoint across a broad and expanding definition: user workstations, servers, cloud instances, containers, and increasingly AI inference infrastructure. Falcon Flex allows flexible redeployment of license capacity across endpoint types.

**Direct Exposure:**
User workstation licenses (Falcon Prevent/Insight) decline with white-collar headcount. This is real but bounded — user endpoint is now a minority of CrowdStrike's total endpoint universe.

**Natural Hedge — The Most Robust in the Cohort:**
- Falcon Cloud Security protects cloud workloads — AI compute infrastructure (GPU servers, model inference endpoints, agent orchestration clusters) is a growing category of protected workloads
- Falcon Identity Protection covers non-human service accounts and API credentials — each AI agent generates multiple new identities
- Falcon Flex's pooled licensing model lets customers redeploy shrinking user-endpoint allocation toward growing cloud-workload needs without incremental spend — a retention mechanism under headcount compression
- NG-SIEM (LogScale) charges on data ingestion volume — AI agents generate orders-of-magnitude more telemetry than humans, potentially growing NG-SIEM revenue even as headcount falls
- **Charlotte AI** mirrors Purple AI's strategic position: fewer human analysts increases the economic value of autonomous AI security operations, driving higher Charlotte AI attach rates

**Net Assessment:** CrowdStrike has the most naturally diversified pricing architecture against this risk of any endpoint-adjacent vendor. The company that makes AI compute workloads and agent identities new billable surfaces is simultaneously the most resilient to losing human endpoint seats.

---

### 4. Palo Alto Networks (PANW) — SEAT RISK: LOW-MODERATE (bifurcated)

**Revenue Model:** Highly mixed — NGFW hardware/software (per throughput/device), Prisma Access/SASE (per user), Cortex XDR/XSIAM (per endpoint/node), Prisma Cloud (per cloud workload/credit), and identity (per identity, post-CyberArk).

**Direct Exposure:**
Prisma Access (SASE/ZTNA) is explicitly per-user. Mindshare in SASE already declining (11.8%, down from 17.6% vs. prior year per PeerSpot). Cortex XDR on user endpoints has endpoint-count exposure similar to CrowdStrike.

**Natural Hedge:**
- NGFW hardware/subscription (estimated ~40–50% of total revenue) is completely immune — charges by network throughput tier, not user count
- Prisma Cloud (cloud workload/CNAPP) benefits from AI infrastructure expansion
- CyberArk acquisition (identity + privileged access + NHI) positions PANW as arguably the strongest platform play on AI agent identity security in the industry; NHI is CyberArk's fastest-growing segment
- AI Security (integrated into Prisma Cloud and Cortex) targets AI pipeline security — a nascent but growing category

**Net Assessment:** PANW's bifurcated model means the per-user exposure is real but bounded. The CyberArk NHI hedge is the most strategically decisive factor for PANW's positioning in the agentic AI era — it converts the threat (AI agents displacing human users) into a growth vector (securing those agents as identities).

---

### 5. Fortinet (FTNT) — SEAT RISK: LOW

**Revenue Model:** Predominantly hardware appliance + subscription (per throughput tier), with modest per-user components (FortiSASE, FortiClient EMS).

**Direct Exposure:**
FortiSASE and FortiClient EMS have per-user pricing, but these represent a small fraction of total Fortinet revenue. The core FortiGate business charges by firewall throughput and appliance tier — entirely independent of headcount.

**Structural Insulation:**
- SMB and OT/industrial customers (Fortinet's core base) are the least exposed to white-collar AI displacement. Manufacturing floor workers, plant operators, and retail staff are not being replaced by knowledge-work AI agents.
- FortiAnalyzer, FortiManager, and the broader operational technology (OT) security suite charge per device managed — not per employee
- FortiAI and FortiSOC's agentic AI capabilities position Fortinet to sell AI analyst automation *to* the shrinking security teams, growing revenue from fewer humans rather than losing it

**Net Assessment:** Fortinet's pricing architecture and customer base are structurally insulated from white-collar knowledge-worker displacement. The per-user exposure is a rounding error relative to hardware/throughput revenue.

---

### 6. Cisco / Splunk (CSCO) — SEAT RISK: LOW

**Revenue Model:** Splunk on data ingest volume; Cisco networking on hardware/subscription; Duo MFA and Umbrella DNS on per-user.

**Direct Exposure:**
Cisco Duo (multi-factor authentication) and Cisco Umbrella (DNS-layer security) are per-user products. These are meaningful but not disclosed separately; neither is a primary driver of Cisco's investment thesis. The far larger Splunk business charges per GB/day of data ingested — AI agents generate *more* log data, not less.

**Natural Hedge:**
- Splunk is architecturally insulated and potentially a beneficiary — AI agents produce high-frequency, machine-speed telemetry that increases log volumes substantially
- Cisco networking infrastructure is priced per device/port — not per employee
- ThousandEyes (network intelligence) charges per agent monitor, not per user

**Net Assessment:** Cisco is largely insulated. Duo seat compression is the primary exposure but it's modest relative to Cisco's $55B+ revenue base. Splunk may actually see a tailwind as AI-generated telemetry volume expands.

---

### 7. Elastic (ESTC) — SEAT RISK: MINIMAL

**Revenue Model:** Indexed data volume (GBs stored/processed per period). No per-user pricing in the security or observability products.

**Direct Exposure:** None direct. Fewer human workers means marginally fewer user-activity log events, but security telemetry is dominated by infrastructure, network, and application events — not human-generated data.

**Natural Hedge:**
AI agents generate extremely high-frequency, machine-speed log events. An enterprise deploying 500 AI agents may generate 10–50× the log volume of 2,500 human workers. Elastic's revenue model means this is **an expansion driver**, not a threat.

**Net Assessment:** Elastic is structurally positioned as a beneficiary of the agentic AI trend in terms of revenue model. The primary risk to Elastic is Databricks Lakewatch (a competing analytics platform), not headcount compression.

---

### 8. Rubrik (RBRK) — SEAT RISK: NONE

**Revenue Model:** Terabytes of data under protection (backup/recovery) plus cloud data management subscriptions. Entirely data-volume based.

**Direct Exposure:** None. Enterprise data volumes don't shrink with headcount — AI systems process and generate *more* data than the human workflows they replace. Rubrik's addressable data surface expands with AI adoption.

**Natural Hedge:**
- AI training data, model artifacts, agent memory stores, and inference logs all represent new data requiring protection and auditability
- The regulatory pressure around AI data governance (audit trails, explainability, data retention) increases Rubrik's value proposition in AI-heavy environments
- Rubrik Agent Cloud (AI agent governance/guardrails) is a direct bet on the AI agent security market

**Net Assessment:** Rubrik is the clearest beneficiary in the cohort. Its pricing is entirely decoupled from human headcount, and AI adoption expands the data it is paid to protect.

---

## Revenue Quality Assessment: Per-Seat Risk Summary

| Company | Ticker | Pricing Metric | Per-Seat Exposure | Natural Hedge Strength | Net Risk to ARR |
|---------|--------|---------------|-------------------|----------------------|-----------------|
| Zscaler | ZS | Per human user | **100% of ARR** | Weak — architecture bypassed by agents | **Critical** |
| SentinelOne | S | Per endpoint (user + cloud) | ~50–60% of ARR | Moderate — cloud/identity/Purple AI | **High, partially offset** |
| CrowdStrike | CRWD | Per endpoint (broad definition) | ~30–40% of ARR | Strong — Flex, cloud workloads, Charlotte AI | **Moderate, largely offset** |
| Palo Alto Networks | PANW | Mixed (per-user SASE + per-throughput NGFW) | ~20–30% of ARR | Strong — NGFW insulated; CyberArk NHI | **Low-Moderate, mostly offset** |
| Fortinet | FTNT | Per device/throughput (dominant); per-user (small) | ~5–10% of revenue | Very strong — hardware/OT/SMB core immune | **Low** |
| Cisco/Splunk | CSCO | Per-ingest (Splunk); per-device (networking); per-user (Duo/Umbrella small) | ~3–5% of revenue | Very strong — Splunk ingest-based; networking infra | **Low** |
| Elastic | ESTC | Per indexed data volume | None direct | Positive — AI telemetry volume expands revenue | **Net positive** |
| Rubrik | RBRK | Per data protected | None | Positive — AI data proliferates Rubrik coverage | **Net positive** |
| Okta | OKTA | Per human user/MAU | ~65–70% WIC (workforce) | Strong — NHI is identity's natural extension; "Okta for AI Agents" GA | **High risk, strongest offset** |
| JFrog | FROG | Hybrid: per-developer + per-GB consumption | ~30–40% per-developer seats | Strong — AI code generation grows consumption; ML model registry new TAM | **Moderate risk, partially offset** |
| Datadog | DDOG | Consumption: per-host, per-GB, per-events — NOT per-seat | ~3–5% (On-Call per responder; CI Visibility per committer) | Near-complete — AI workloads generate more telemetry; every AI agent runs on a billable host | **Net positive — structurally aligned with AI proliferation** |

---

### 9. Okta (OKTA) — SEAT RISK: HIGH (strongest natural hedge in cohort)

**Revenue Model:** Per-human-user for Workforce Identity Cloud (WIC) at $6–$17+/user/month annually; per-monthly-active-user (MAU) for Customer Identity Cloud (CIC, Auth0). WIC is estimated ~65–70% of total revenue.

**Scale:** FY2026 revenue $2.919B (+12% YoY); ARR ~$3.0B. NRR ~106% (Q4 FY2026) — down from 122% in FY2023, a 16-point decline over three years that already reflects early headcount-linked attrition pressure, even before the current agentic wave accelerates it.

**Direct Exposure:**
Every enterprise employee requires an Okta WIC license for SSO, MFA, and lifecycle management. At estimated ~65–70% of revenue tied to WIC, a sustained 15–20% enterprise headcount reduction represents ~$280–410M of annual ARR at direct risk. FY2027 guidance of $3.17–3.19B implies only 8–9% growth — decelerating despite expanding TAM, suggesting the market already partially discounts the seat-compression overhang. Okta stock corrected double-digits in February 2026 on the same SaaSpocalypse fears as Zscaler.

**Why Okta Has the Strongest NHI Hedge:**
Okta's existential advantage in this transition is that **identity is the natural control plane for both human and non-human actors** — there is no architectural bypass problem here. Okta doesn't need to build a different product; it needs to extend its existing platform to issue, manage, and revoke credentials for AI agents the same way it does for humans.

Key evidence that Okta is executing:
- "Okta for AI Agents" launched (GA April 30, 2026) — direct auth/authz for AI agent identities
- "Auth0 for AI Agents" — extends CIC to handle agent-to-agent authentication
- "New Okta Platform innovations extend Identity Security Fabric to non-human identities" (announced 2026)
- Blueprint for the Secure Agentic Enterprise (Showcase 2026) — positioning Okta as the governance layer for all agentic workflows
- Stock rose 11% after Q4 FY2026 earnings as market began pricing in the NHI TAM expansion

**The NHI Math Is Favorable:**
Non-human identities outnumber human identities ~50:1 in the average enterprise. If Okta captures NHI at even 20% of per-human pricing:
- 1,000 employees → 50,000 NHIs
- At $10/user/month human rate: $10K/month
- At $2/NHI/month (20% rate) × 50,000: $100K/month — **10× revenue expansion per enterprise**

Only 10% of organizations currently have a NHI strategy, and 91% already deploy AI agents — the gap between exposure and governance is Okta's TAM.

**Caveat:** NHI products are not yet assumed to be near-term revenue contributors per street commentary. FY2027 guidance is conservative and does not model NHI at material scale. The transition from "lost WIC seat" to "gained NHI license" involves a 2–3 year product adoption lag.

---

### 10. JFrog (FROG) — SEAT RISK: LOW-MODERATE (consumption model largely insulates)

**Revenue Model:** Hybrid — per-developer seats (e.g., Pro at $6K/10 users/year; Enterprise+ at ~$110K+) plus per-GB consumption (storage + data transfer, $0.75–$1.25/GB). Cloud revenue growing fastest (+45% YoY in FY2025).

**Scale:** FY2025 revenue $531.8M (+24% YoY); FY2026 guidance $623–628M (+17.5%). Cloud revenue $243.3M FY2025. $1M+ ARR customers: 74. Security (Advanced Security + Curation): >10% of ARR.

**Where Seat Risk Exists:**
JFrog serves software developers as its primary buyer. AI coding tools (GitHub Copilot, Cursor, Claude Code, Devin) are reducing the number of human developers needed to produce equivalent software output. If enterprise engineering headcount falls 20–30% over three to five years, JFrog loses per-developer seat licenses proportionally. Estimated ~30–40% of JFrog revenue is per-developer seat; a 20% developer headcount decline represents a ~$30–45M ARR headwind at current scale.

**Why the Consumption Model Largely Insulates:**
The critical structural insight for JFrog is that **AI coding agents generate dramatically more software artifacts than human developers, not fewer.** Every AI agent running a build:
- Stores compiled artifacts in Artifactory (more GB stored → more consumption revenue)
- Pulls dependencies at high frequency for every build run (more data transfer → more consumption revenue)
- Triggers JFrog Xray scans on every artifact (more security scans → more Advanced Security consumption)
- Creates more build versions, more container images, more package manifests

A 50-person developer team replaced by AI coding agents might generate 5–10× the CI/CD pipeline activity — and JFrog charges for that activity. The company itself notes that "teams with active CI/CD pipelines report actual costs 3–5× higher than base price."

**The ML Model Registry as New TAM:**
JFrog ML (released 2025), built in partnership with NVIDIA Enterprise AI Factory and Hugging Face, positions JFrog as the enterprise artifact registry for AI/ML assets:
- LLM model weights and checkpoints (multi-GB to multi-TB per model)
- Fine-tuned model variants (each enterprise fine-tune creates a new managed artifact)
- Training datasets and evaluation benchmarks
- Model governance and provenance tracking (analogous to software bill of materials)

This TAM is entirely decoupled from developer headcount and grows with AI adoption.

**The B2A Strategy (Business-to-Agent):**
JFrog has announced MCP server integration and "JFrog Fly" to enable AI coding agents to interact directly with the JFrog platform via API and Model Context Protocol. This is a forward-looking hedge: even if human developers decline as a buyer persona, AI coding agents become consumption-based customers of JFrog's artifact infrastructure directly.

**Net Assessment:** JFrog occupies a structurally advantaged position — it is the artifact registry and distribution layer for software output regardless of whether that output is produced by humans or AI agents. The per-developer seat component faces real pressure; the consumption + ML model registry + B2A components point toward net expansion.

---

### 11. Datadog (DDOG) — SEAT RISK: NEGLIGIBLE (consumption model is net positive from AI proliferation)

**Revenue Model:** Pure consumption-based SaaS — per host monitored, per GB of logs ingested, per APM trace, per session for RUM, per event for Cloud Security. **There is no per-user or per-seat component in any of Datadog's core products.** The sole exceptions are On-Call (per on-call responder, introduced 2024) and CI Visibility (per committer), which together represent an estimated ~3–5% of total ARR.

**Why Datadog is included in this analysis:** Datadog is not traditionally classified as a cybersecurity company, but it is a platform actively used by security teams (Cloud Security, Application Security Management) and faces the agentic AI transition as a *demand tailwind* rather than a threat. Including it here provides an important anchor: it represents the model that per-seat cybersecurity vendors are trying to migrate toward.

**Seat compression sensitivity:**

The ~3–5% of ARR tied to headcount (On-Call responders + CI committers) faces a small, real compression risk as enterprises reduce engineering headcount. However, this is nearly entirely self-hedged:
- Fewer on-call engineers → but AI-generated incidents and alerts increase per-host alerting volume
- Fewer human committers → but AI coding agents (Copilot, Cursor, Claude Code) generate dramatically more CI pipeline runs per team, increasing CI Visibility consumption

Empirically: a 20% developer headcount reduction in a team using AI coding tools typically results in *more* CI activity, not less, as AI agents iterate faster. The per-committer billing basis likely benefits from this dynamic.

**The structural advantage: AI workloads are net consumption positive.**

Every AI agent, LLM pipeline, GPU cluster, and agentic workflow must run on compute infrastructure. Datadog charges per host monitored — meaning:
- AI inference servers → billable hosts
- LLM orchestration containers → billable hosts
- AI agent runtime environments → billable hosts
- GPU nodes → billable hosts, with significantly higher telemetry density than CPU hosts

Datadog's Q4 FY2025 data supports this: 4,000+ customers used at least one AI integration (doubled YoY). LLM Observability — priced per GB of AI request/response data — is a new consumption category that scales directly with LLM usage, not headcount.

**Relevant agentic products:**

| Product | Description | Status |
|---------|-------------|--------|
| LLM Observability | Monitors AI pipeline inputs/outputs, token usage, latency, cost, toxicity per request | GA, 2024 |
| Bits AI SRE Agent | Autonomous site reliability engineer — investigates outages, executes remediation playbooks | GA, 2025 |
| TOTO (Time-Series Foundation Model) | Proprietary open-weight model for time-series anomaly detection; trains on Datadog's full telemetry corpus | GA, 2025 |
| AI Security | Detects prompt injection, model misuse, sensitive data leakage in LLM pipelines | GA, 2025 |
| Datadog MCP Server | Enables AI agents to interact with Datadog platform natively via Model Context Protocol | Available |

**Net Assessment:** Datadog is not exposed to the SaaSpocalypse — it is a *beneficiary* of it. Every AI agent deployed replaces a seat at a per-seat vendor while adding a billable host at Datadog. The 3–5% headcount-linked exposure (On-Call + CI Visibility) is marginal and partially self-hedged. The correct framing for DDOG is: it is the infrastructure layer that agentic AI workflows run *on top of*, generating consumption revenue independent of human headcount.

---

---

## Agentic Product Readiness Assessment

The following section scores each company on how far along they are in building products that secure or serve AI agents and machine identities — and to what extent those products can offset white-collar seat attrition. Each company is scored across four dimensions (1–5 scale):

- **Product Maturity:** How far along from roadmap → preview → GA → at-scale revenue
- **Architectural Fit:** How naturally the NHI/agent capability extends from existing architecture vs. requiring a rebuild
- **Revenue Upside from Agents:** The size and credibility of the agent-driven revenue opportunity
- **Seat Loss Mitigation:** The degree to which agent revenue directly compensates for lost human-seat licenses

---

### Readiness Scorecard

| Company | Product Maturity | Architectural Fit | Revenue Upside | Seat Loss Mitigation | **Overall** |
|---------|:----------------:|:-----------------:|:--------------:|:-------------------:|:-----------:|
| Datadog | ★★★★★ | ★★★★★ | ★★★★★ | N/A (net positive by design) | **★★★★★** |
| JFrog | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | **★★★★★** |
| Okta | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★ | **★★★★★** |
| CrowdStrike | ★★★★★ | ★★★★ | ★★★★ | ★★★★ | **★★★★** |
| SentinelOne | ★★★★★ | ★★★★ | ★★★★ | ★★★ | **★★★★** |
| Rubrik | ★★★★★ | ★★★★ | ★★★★ | ★★ | **★★★★** |
| Palo Alto Networks | ★★★★ | ★★★ | ★★★★ | ★★★ | **★★★** |
| Elastic | ★★★ | ★★★ | ★★★ | N/A (already insulated) | **★★★** |
| Fortinet | ★★★ | ★★ | ★★ | ★★ | **★★** |
| Cisco/Splunk | ★★ | ★★ | ★★★ | N/A (mostly insulated) | **★★** |
| Zscaler | ★★ | ★ | ★★ | ★ | **★★** |

---

### Per-Company Readiness Detail

#### Datadog (DDOG) — Readiness: ★★★★★ | Structurally Aligned — Not a Mitigation Story, a Tailwind Story

Datadog requires no mitigation because it has no meaningful seat-loss exposure. The correct framing is inverted: **AI agent proliferation is a direct consumption growth driver for Datadog**, not a threat to hedge against.

The agentic AI transition creates three reinforcing demand vectors for Datadog:

1. **More billable hosts:** Every AI agent, LLM inference server, and GPU cluster is a Datadog-monitored host. At $15–31/host/month, each new AI workload deployment adds directly to ARR. This is the same pricing model that drove Datadog's growth during the cloud migration era — AI infrastructure build-out is the next equivalent wave.

2. **Higher telemetry density per host:** GPU nodes running LLM inference generate significantly more traces, metrics, and logs per second than traditional CPU application servers. Datadog's per-GB log pricing and per-event custom metrics billing both benefit from this density increase — revenue per monitored host rises.

3. **New consumption categories (LLM Observability, AI Security):** LLM Observability monitors AI request/response pairs at a per-GB rate — a billable category that didn't exist three years ago and is growing rapidly. AI Security (prompt injection detection, model misuse monitoring) adds further per-event consumption. Both categories are priced by AI workload volume, not headcount.

The minimal seat-linked exposure (On-Call per responder; CI Visibility per committer — together ~3–5% of ARR) is discussed in §11. Even this small residual is partially self-hedged: AI coding agents run more CI pipeline builds than human developers, sustaining committer-count-based billing even as human developer headcount falls.

**Why this matters for the broader analysis:** Datadog serves as the benchmark for what "agentic AI readiness" looks like structurally. Its consumption model is what per-seat vendors (ZS, OKTA, S) are implicitly trying to replicate through metered usage, workload-based modules, and NHI repricing — attempting to convert their pricing basis from "per human" to "per workload," the model Datadog already has.

#### JFrog (FROG) — Readiness: ★★★★★ | Most Architecturally Positioned

JFrog's response to the agentic AI era is the most operationally mature of any company in this cohort, and uniquely, **it requires no repricing — just natural consumption growth**.

**What's shipping:**
- **JFrog MCP Server** (GA July 2025): Enables LLMs and AI coding agents to interact directly with the JFrog platform via Model Context Protocol from popular agentic IDEs (Cursor, GitHub Copilot, Claude Code). Enforces token-based authorization with scoped access per tenant and tool — every agent operation authenticated under end-user identity. Already in production.
- **JFrog MCP Registry** (GA): Central enterprise registry to store, manage, and control access to MCP servers from multiple vendors — a governance layer for how developers *and* agents connect to tooling. First enterprise-class MCP governance product.
- **JFrog Fly** (GA early 2026): Branded as "the world's first agentic artifact repository," Fly enables agentic releases — software delivery orchestrated entirely by autonomous AI agents using natural language and semantic cues. Integrates natively with Cursor, Copilot, and Claude Code via MCP.

**Why the mitigation is near-complete:** JFrog doesn't need to win a new pricing argument. Every AI coding agent that runs a build, pushes a package, or pulls a dependency generates consumption revenue (storage GB + transfer GB) on the same pricing model that human developers already use. Fewer human developers writing code, replaced by AI agents writing *more* code, *faster*, means artifact throughput likely *increases* even as per-developer seat count falls.

**Residual risk:** If enterprises consolidate entirely to GitHub-native artifact storage and away from JFrog, that's a displacement risk — but it predates the agentic AI transition and is unrelated to the seat-compression dynamic.

---

#### Okta (OKTA) — Readiness: ★★★★★ | Strongest Identity-Native Response

Okta's response to the agentic AI era is the most strategically coherent of any per-seat-exposed vendor: **the product that faces the threat (identity management for human users) is structurally identical to the product that captures the opportunity (identity management for AI agents)**.

**What's shipping:**
- **Okta for AI Agents** (GA April 30, 2026): End-to-end identity security for AI agents — discovery of AI agents in enterprise environments via ISPM, identity lifecycle management through Universal Directory, least-privilege access enforcement, automated policy enforcement. Integration partners at GA: Boomi, DataRobot, Google Vertex AI.
- **Auth0 for AI Agents**: Extends CIC to handle agent-to-agent authentication and OAuth2 client credentials flows for automated systems.
- **Identity Security Posture Management (ISPM) extended to NHI** (in platform): Scans for risky service accounts, API keys, OAuth tokens — the credential surface of AI agents — within the existing Okta platform.
- **Okta Showcase Blueprint (March 2026)**: Published a formal "Secure Agentic Enterprise" architecture blueprint, positioning Okta as the identity control plane for the full agentic stack.

**Market validation:** Only 22% of organizations currently treat AI agents as independent, identity-bearing entities requiring their own lifecycle management, yet 88% have already experienced suspected AI agent security incidents. This gap defines Okta's greenfield for NHI.

**Mitigation math:** At 50:1 NHI-to-human ratios and Okta's existing per-human pricing of ~$10/user/month, even 20% of per-human pricing per NHI yields 10× revenue per enterprise account. The question is price point and adoption speed — but the product architecture and the go-to-market motion (existing Okta customer → add NHI module) are both in place.

**Caveat:** FY2027 guidance ($3.17–3.19B; +8–9% growth) does not model NHI at material contribution. Street expectation is that NHI revenue is meaningful by FY2028, not FY2027.

---

#### CrowdStrike (CRWD) — Readiness: ★★★★★ | Most Comprehensive Agentic Security Platform

CrowdStrike has shipped the broadest portfolio of agentic AI security capabilities of any vendor in this cohort, operating simultaneously as a user of AI agents (Charlotte AI) and a securer of AI agent workloads (Falcon for AI infrastructure).

**What's shipping:**
- **Charlotte Agentic SOAR** (GA): Orchestrates AI-powered agents across the security lifecycle. Connects context and data so agents reason and act dynamically in real time under analyst command. Unites native, custom-built, and trusted third-party agents in a single coordinated system.
- **Charlotte AI Agentic Response + Agentic Workflows** (GA): Autonomous reasoning and action on first- and third-party security data — transcends ask-and-respond copilot to autonomous investigation and response.
- **Charlotte AI FedRAMP High Authorization** (November 2025): Cleared for public sector deployment — a moat that ZS, S, and others haven't matched.
- **Securing Agentic AI Workloads on AWS** (GA): CrowdStrike protects AI applications, LLMs, and agent services running on AWS — an inaugural partner in AWS Agentic AI Specialization. Secures the AI infrastructure itself (model endpoints, inference APIs, agent orchestration) as new billable workloads.
- **Falcon Identity Protection extended to NHI**: Service accounts and workload identities treated as first-class identity objects with the same detection and response capabilities as human accounts.

**The strategic compounding effect:** As enterprises adopt AI agents in production, they need both to (a) secure the agent infrastructure (CrowdStrike Falcon Cloud Security) and (b) defend against adversaries using AI agents to attack (Charlotte AI detects AI-driven attacks at machine speed). CrowdStrike is positioned on both sides of this dynamic.

**Mitigation strength:** High. Falcon Flex allows human endpoint licenses to be redeployed to cloud workload/AI infrastructure coverage mid-contract. Cloud security and identity ARR growth directly offsets user-endpoint attrition without requiring customer churn or new price negotiations.

---

#### SentinelOne (S) — Readiness: ★★★★★ | Most Aggressive RSAC 2026 NHI Launch

SentinelOne made the NHI transition one of its two central announcements at RSAC 2026 (March 23–24, 2026 — this week), indicating the company is treating agent identity as an immediate revenue priority, not a roadmap item.

**What's shipping:**
- **Singularity Identity extended to NHI** (GA, February 2026): First-class inventory of service accounts, workload identities, and AI agent credentials within Singularity Identity. Applies identity security policies, detections, and posture checks built specifically for NHI misconfigurations and behavioral anomalies. Covers endpoints, browsers, and AI workflows.
- **Prompt AI Agent Security** (announced RSAC 2026, March 24, 2026): New real-time discovery and governance control plane for AI agents and agentic workflows. Monitors, controls, and enforces policy on agent interactions at machine speed — purpose-built for the rate and scale of agent-to-system interactions that human-speed tooling can't handle.
- **Purple AI one-click Auto Investigation** (GA, RSAC 2026): Full agentic SOC investigation launched with a single click — gathers cross-stack evidence, synthesizes threat data, constructs complete attack timelines autonomously. Record 50%+ attach rate in Q4 FY2026 licenses.
- **Paradigm: behavioral validation over authorization**: SentinelOne's NHI framework focuses not just on whether an agent is *authorized* to act but on whether its *behavior* is consistent with its declared purpose — a more sophisticated approach than static policy enforcement.

**Mitigation strength:** Moderate-to-high. Singularity Identity NHI extends an existing platform module — no separate product sale needed. Purple AI at 50% attach and growing means autonomous security tools are already becoming the primary value proposition for new licenses, which is structurally different from (and less headcount-dependent than) protecting human-operated endpoints.

---

#### Rubrik (RBRK) — Readiness: ★★★★★ | Industry-First Semantic Governance Layer

Rubrik's agentic AI response is the most surprising of the cohort — a data protection company has shipped what it claims is the industry's first AI governance engine, positioned directly at the point where agents interact with enterprise data.

**What's shipping:**
- **Rubrik SAGE** (Semantic AI Governance Engine, announced RSAC 2026, March 23, 2026): Real-time AI governance for autonomous agents. Uses a custom Small Language Model (5× faster than GPT-5.2 in benchmarks) to interpret natural language policy intent (e.g., "Do not give financial advice") and enforce it as machine logic against agent interactions — dynamic semantic interpretation vs. static keyword filters.
- **Rubrik Agent Cloud** (GA): AI Agent Operations Platform — real-time command center for agentic operations. Includes SAGE, adaptive policy improvement (proactively refines ambiguous guardrails), and Agent Rewind (instantly undoes destructive agent actions and restores data integrity using Rubrik's backup infrastructure).
- **Agent Rewind**: The unique capability that only Rubrik can offer — because Rubrik already holds point-in-time snapshots of enterprise data, it can literally reverse what an agent did to data. No other vendor in this cohort can offer this.

**Strategic position:** Rubrik sits between agents and enterprise data at the governance layer. While Okta controls *who* the agent is, and CrowdStrike protects *where* the agent runs, Rubrik controls *what the agent can do with data* and *undoes mistakes when agents go wrong*. These are complementary, not competing, control surfaces.

**Mitigation note:** Rubrik's core business was already insulated from seat-loss risk (per-data-protected pricing). SAGE/Agent Cloud is a new product category that grows the TAM into governance, not a defensive response to pricing pressure. However, it meaningfully expands Rubrik's revenue potential per enterprise as agentic AI deployment scales.

---

#### Palo Alto Networks (PANW) — Readiness: ★★★★ | Strong Platform, Execution Risk

**What's shipping:**
- **Cortex AgentiX** (GA, embedded in XSIAM and Cortex Cloud; standalone platform in early 2026): Agentic AI platform for security operations, enabling autonomous reasoning, investigation, and response. Available now within existing XSIAM platform — customers don't need to buy a new product.
- **XSIAM extended with AI-driven identity threat detection and response** (GA): Detects and responds to threats using NHI credential data in real time — specifically built to handle live threat actors using stolen NHI credentials.
- **AI Agent Discovery in Cortex platform** (announced 2026): Cortex now inventories and assesses AI agents deployed in enterprise environments, applying security policies to agent identities as part of the unified identity platform vision.
- **Workload Identity framework**: Published detailed architecture for treating AI agent workload identities as distinct security objects requiring instantaneous revocation on anomalous behavior.

**Gap:** CyberArk integration (the most strategically important NHI asset) is still in progress. The market had expected CyberArk + PANW NHI capabilities to be announced in a more integrated form by now; unified platform delivery is the key execution risk.

**Mitigation strength:** Moderate. AgentiX and XSIAM NHI extensions are real and in market, but the pricing model for these capabilities is bundled into existing XSIAM ARR (no separate NHI SKU yet announced). The mitigation of Prisma Access per-user seat loss via agent-tier NHI pricing requires a pricing model announcement that hasn't materialized yet.

---

#### Elastic (ESTC) — Readiness: ★★★ | Building Tools, Not Monetizing Identity

**What's shipping:**
- **Elastic Agent Builder** (GA, January 2026): Platform for building production-ready AI agents on top of Elasticsearch — native data prep, retrieval, ranking, conversational experience, and agent observability. Targets enterprises building their own security AI agents.
- **Official Elastic Skills** (GitHub, active): Library of pre-built agent skills for security operations — SIEM queries, investigation templates, response playbooks as agent-callable tools.
- **Security Labs agentic SOC blog** (February 2026): Detailed architecture for an AI-native SOC using Elastic, positioning 2026 as the inflection point for agentic security operations at scale.

**Key distinction:** Elastic is building *tools for building AI agents* (developer platform) and using AI to improve its SIEM (internal product), not building a product that **secures AI agents as identities** or **prices on agent identities**. This is an important gap — Elastic's agentic AI work strengthens the platform's value to human security teams but doesn't create the NHI pricing mechanism needed to offset seat attrition.

**Mitigation note:** Irrelevant for Elastic's core thesis — its volume-based pricing model is already insulated from seat attrition. AI-generated telemetry naturally expands Elastic's revenue. The agentic tooling strengthens competitive positioning in the SIEM market rather than addressing a seat-compression risk.

---

#### Fortinet (FTNT) — Readiness: ★★★ | Using Agents, Not Securing Them as Identities

**What's shipping:**
- **FortiSOC** (Preview, announced March 23, 2026): Unified cloud SOC using agentic AI for triage, investigation, and response. Expands FortiAI across FortiAnalyzer, FortiSIEM, FortiSOAR for end-to-end agentic execution.
- **FortiAI Application Intelligence**: Detects and governs AI application communications — visibility into what AI applications are running on the network and what data they're sending/receiving. Reduces unsanctioned AI usage and data exposure.
- **FortiAI expanded across Security Fabric** (2025): FortiAI integrated as an AI analyst and automation layer across all major Fortinet products.

**Critical gap:** Fortinet's agentic AI work is focused on **using** AI agents to improve SOC efficiency, not on **securing** AI agents as distinct identities or workloads that enterprises deploy. FortiAI Application Intelligence provides some visibility into AI application behavior, but there's no NHI identity management product, no agent credential lifecycle management, and no workload identity security module. Fortinet's MCP support in FortiSOC enables agent orchestration within the SOC but doesn't address the broader enterprise agent identity problem.

**Mitigation strength:** Low. Fortinet's FortiAI shrinks the cost of running a human SOC team (positive operating leverage for customers), which may increase deal sizes for FortiSOC — but it doesn't generate a new pricing surface for the NHI transition. As noted elsewhere, Fortinet's core business is structurally insulated from seat loss regardless, so the lack of an NHI offset is less consequential than it would be for ZS or Okta.

---

#### Cisco / Splunk (CSCO) — Readiness: ★★ | Fragmented Response, No Unified NHI Story

**What's shipping:**
- **Cisco AI Defense** (announced FY2025): Designed to protect enterprise AI applications from model-layer attacks — prompt injection, data poisoning, model theft. This is about securing AI *models as infrastructure*, not about NHI identity management.
- **Splunk observability for AI pipelines**: Splunk's logging capabilities extend naturally to AI workload telemetry, but this is a passive capability (more data flowing to existing product), not an active NHI security offering.
- **Cisco Duo MFA for service accounts**: Existing capability, not a new NHI product.

**Gap:** Cisco lacks a coherent, announced NHI identity security product. The Splunk SIEM (the most valuable Cisco security asset) benefits passively from AI telemetry expansion but doesn't generate incremental pricing from agent adoption. Cisco's fragmented product portfolio (stitched together from acquisitions) makes a unified NHI narrative difficult to execute. No announced "Cisco for AI Agents" equivalent.

**Mitigation note:** Again, largely irrelevant — Cisco/Splunk is already mostly insulated from per-seat pressure at the corporate level. Duo seat compression is real but modest. The more important risk to Cisco is Databricks Lakewatch threatening Splunk's SIEM position (separate analysis).

---

#### Zscaler (ZS) — Readiness: ★★ | AI Security Suite Without Solving the Core Problem

**What's shipped:**
- **Zscaler AI Security Suite** (announced January 27, 2026): Includes AI Asset Management (inventory of AI apps, models, agents, usage), MCP Gateway (secure automation), and AI Deception (divert/neutralize model-based attacks). Provides visibility into what AI is running in the enterprise.
- **2026 AI Threat Report**: Documents the 91% YoY surge in enterprise AI activity creating governance gaps — importantly, Zscaler is diagnosing the problem it needs to solve.
- **Next-Gen ZTNA Platform**: Evolves ZTNA architecture to be more extensible, but the press release language focuses on human users on any device/location rather than non-human agent authentication.

**The unresolved architectural problem:** Zscaler's AI Security Suite gives enterprises *visibility* into what AI agents exist and what they're doing at the network layer — but it does not give enterprises *access control* over AI agents that bypass ZIA entirely. The MCP Gateway is the most promising component (it could intercept MCP-based agent tool calls and enforce policy), but it was only announced in January 2026 with no GA date disclosed.

**Honest assessment:** Zscaler is the most aware of the problem (its own threat reports document the risk in detail) but the furthest from a complete solution. The AI Security Suite is a monitoring and visibility product; what's needed is a full-stack agent identity and access control product that replaces ZIA's proxy architecture for machine-speed, API-native traffic. Building that requires restructuring Zscaler's core network topology — not just adding a new module.

**Mitigation strength:** Minimal to low. AI Asset Management generates no new pricing. MCP Gateway (if shipped) could become a meaningful new product, but timeline is unclear. The gap between Zscaler's existing business risk and its current product response is the widest in the cohort.

---

## The Agent Repricin Math

For per-seat vendors to fully neutralize the headcount compression risk, AI agent licenses must compensate for lost human seats. At a 1:5 displacement ratio:

| Agent Pricing vs. Human Pricing | Revenue Retained Per Account |
|----------------------------------|------------------------------|
| 0.5× (agents priced at half human rate) | 10% |
| 1× (equal pricing) | 20% |
| 2× (double human rate) | 40% |
| 5× (five times human rate) | 100% — full offset |
| 10× (ten times human rate) | 200% — expansion |

The realistic near-term range is 1×–3× for agent-tier pricing, implying **20–60% revenue retention** from affected account cohorts before new enterprise growth compensates. This math makes headcount compression a multi-year earnings headwind for seat-dependent vendors even if they eventually reprice successfully.

---

*Sources: Financial Content SaaSpocalypse series (March 2026), TokenRing agentic displacement report (December 2025), CyberArk NHI security blog (2026), Help Net Security agentic AI enterprise security surveys (February–March 2026), Zscaler Q2 FY2026 earnings, CrowdStrike pricing data (CyCognito, Vendr), PANW Prisma Access licensing guide, SentinelOne NHI blog, Fortinet FY2025 results, Elastic pricing documentation, Rubrik FY2026 results. Extended: Okta Q4 FY2026 earnings (March 2026) + Okta for AI Agents launch, Okta NRR trend (SaaStr), JFrog FY2025 full year results + Q4 2025 earnings call transcript, JFrog Artifactory pricing guide (CloudRepo), JFrog Trusted AI 2026 Playbook. Datadog: DDOG Q4 FY2025 earnings (February 10, 2026) + FY2024 10-K + Datadog investor presentation (February 2026, investors.datadoghq.com) + Datadog LLM Observability product page + Datadog Bits AI SRE Agent announcement + Datadog TOTO model announcement + FinancialContent Deep Dive DDOG AI Observability (February 27, 2026) + Vendr Datadog pricing guide 2026.*
