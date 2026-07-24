---
title: AI Inference Costs Accounting: R&D vs. COGS
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [saas, cloud, concept, valuation]
sources: [investing-macro/market-newsletter-digest-2026-07-09.md]
confidence: high
contested: false
---

# AI Inference Costs Accounting: R&D vs. COGS

The classification of artificial intelligence (AI) inference and compute costs is one of the most critical and heavily debated topics in modern tech finance. As software companies transition from legacy SaaS architectures to AI-native architectures, the classification of these costs has direct implications for corporate [[valuations]], gross margins, and audited financial statements under U.S. GAAP and IFRS.

---

## 1. Executive Summary
The accounting treatment of AI costs depends primarily on the **nature and purpose** of the activity rather than the technology itself. The industry has converged on a clear standard:
*   **Production Inference Costs** (delivering customer-facing services) must be categorized under **Cost of Goods Sold (COGS)** (or Cost of Revenue).
*   **Model Training, Fine-Tuning, and Dev/Test Inference** are categorized under **Research & Development (R&D)** operating expenses (OpEx), unless they qualify for capitalization.

While this principle is simple, the execution remains complex, and the debate has shifted from "where should these costs go?" to "how do we operationalize, measure, and optimize these costs?"

---

## 2. Core Accounting Frameworks (U.S. GAAP)

Auditors (including the Big 4) evaluate AI compute costs under two main standards:

### ASC 730: Research and Development
*   **Application:** Covers the discovery of new knowledge or translation of research findings into a product or process.
*   **Treatment:** Costs associated with initial model training, experimentation, evaluating alternative model architectures, and testing new prompts/fine-tuning in a pre-production environment must be expensed as incurred under R&D.

### ASC 350-40: Internal-Use Software
*   **Application:** Governs capitalization of software developed or obtained for internal use or delivered as a cloud service (SaaS).
*   **Treatment:** While ongoing usage fees for hosting/APIs are expensed, certain internal model development or integration costs during the "application development stage" may be eligible for capitalization.
*   **Modernization (ASU 2025-06):** In late 2025, the FASB modernized ASC 350-40, replacing the rigid three-stage framework with a principles-based model centered on **development uncertainty**. Under this update, costs can only be capitalized once it is probable that the software project will be completed and will perform its intended function, which is particularly relevant to the highly unpredictable nature of training large neural networks.

---

## 3. Which Approach Has the Most Acceptance?

The clear consensus among auditors, CFOs, and financial analysts is that **production inference costs belong in COGS**.

### The Rationale for COGS
Production inference is the variable cost incurred to deliver a product to a customer. When a customer uses an AI-powered feature (e.g., generating text, analyzing an image, or executing an agentic workflow), each query represents a direct API call (e.g., to OpenAI, Anthropic) or a GPU compute cycle (on AWS, Azure, GCP). Because these costs scale dynamically with customer usage and are required to fulfill the service, they are direct costs of revenue.

### The Impact: Gross Margin Compression
The strict classification of production inference under COGS has forced a structural shift in software unit economics:
*   **Legacy SaaS:** Historically enjoyed gross margins of **70% to 80%+** because serving code and database queries was cheap (see [[ddog]] or [[now]] for examples of high-margin legacy architectures).
*   **AI-Native SaaS:** Typically operates at gross margins of **50% to 60%** (and sometimes lower) due to the significant variable costs of running LLM inference. Failing to put these costs in COGS artificially inflates gross margin and distorts the true profitability of the software.

---

## 4. How the Debate Has Evolved Over Time

The debate around AI costs has moved through three distinct phases:

### Phase 1 (2022–2023): Hype and Hiding in R&D
*   **Context:** The ChatGPT-led boom meant companies were racing to ship AI features. Most of these features were labeled "beta" or "experimental."
*   **Accounting Behavior:** Finance teams routinely categorized almost all AI compute and API spend under R&D (OpEx). 
*   **Strategic Motive:** Because venture capitalists were still funding growth at all costs, startups wanted to maintain their high "SaaS gross margins" (80%+). Pushing inference into R&D hid the high marginal cost of AI features. Auditors generally allowed this because the features were not yet stable, core revenue drivers.

### Phase 2 (2024–2025): Auditor Scrutiny and the Profitability Pivot
*   **Context:** AI features matured into permanent, default product offerings. At the same time, venture capital and public markets pivoted, demanding paths to profitability and clear unit economics rather than pure user growth.
*   **Accounting Behavior:** Audit firms (such as Deloitte, PwC, EY, and KPMG) began enforcing strict boundaries. If an LLM call was required to deliver a feature that a paying customer relied on, it could no longer be classified as R&D. It had to move to COGS.
*   **The Shock:** Many companies experienced sudden, severe gross margin compression as their true cost of delivery was unmasked. This forced CFOs to re-evaluate pricing strategies, moving away from flat-rate unlimited pricing toward usage-based or tiered models.

### Phase 3 (2026+): Operational Cost Attribution and Efficiency
*   **Context:** The debate over *where* the costs belong is largely resolved. The challenge now is *how* to accurately separate and optimize them.
*   **Accounting Behavior:** Companies are implementing strict infrastructure segregation. If developers run training scripts or test prompts on the same cloud accounts or API keys used by the production app, the blended bill is highly vulnerable to audit failure. CFOs are mandating separate cloud accounts, API workspaces, and granular cost tagging.
*   **Efficiency Metrics:** The focus has shifted to the **Inference Efficiency Ratio (IER)** and per-customer cost attribution. Product engineering teams are now measured on their ability to optimize inference (e.g., through model routing, prompt optimization, quantization, and caching) to protect the corporate gross margin.

---

## 5. Key Nuances and Controversial Areas

Even with consensus, several gray areas persist:

1.  **Shared API Keys and Accounts:** Startups often use a single OpenAI or Anthropic corporate account. If the engineering team is using the same API keys for training/evaluating models as the app is using to serve customers, separating R&D from COGS is a manual guessing game. Auditors frequently default to putting the entire bill in COGS if a clean split cannot be proven, which penalizes the gross margin.
2.  **Free Trials and PoCs:** When prospects run inference during sales pilots, should those costs go to Sales & Marketing (S&M) or COGS? Standard practice suggests allocating free-tier compute to S&M, but tracking this accurately is technically challenging.
3.  **Internal-Use Productivity Tools:** If a company builds an internal AI agent to help its customer support team, the inference costs are typically categorized under Customer Support (COGS). If they build one for the sales team, it belongs in S&M. If it's a general company-wide assistant, it is General & Administrative (G&A). This requires department-level tagging of AI usage.
4.  **Foundation Model Training vs. Fine-Tuning:** Training a brand-new foundation model from scratch is clearly R&D (and sometimes capitalized as an intangible asset). However, continuous fine-tuning on live user data to keep a production system relevant blurs the line between R&D and operational maintenance.

---

## 6. Actionable Recommendations for Tech Finance Teams

To ensure audit readiness and protect financial integrity, companies should adopt the following best practices:

*   **Implement Cloud Account Segregation:** Never mix production and development workloads on the same accounts or API workspaces. Use distinct API keys and cloud resource groups for production (COGS) and R&D/testing (OpEx).
*   **Establish a Dedicated "AI COGS" Line Item:** Instead of burying AI costs in general "Hosting" or "Infrastructure," create a distinct line item on the P&L. This shows the board and investors exactly how AI usage scales relative to revenue.
*   **Deploy Granular Cost Tagging:** Tag every model invocation or cloud compute instance by customer ID or feature. This allows for real-time monitoring of customer profitability and prevents high-volume users from eroding margins.
*   **Document Accounting Policies Early:** Work with auditors to establish a clear policy document defining when a model transitions from "development" (R&D) to "production" (COGS), especially in continuous deployment environments.
