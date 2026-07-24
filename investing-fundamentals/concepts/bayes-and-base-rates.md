### Bayes and Base Rates

> A Bayesian framework to evaluate the plausibility of aggressive growth forecasts (e.g., for GenAI companies or capacity additions) by starting with a historical base rate (prior belief based on reference classes) and updating that belief in proportion to new, objective evidence.

---

### The Bayesian Updating Framework

The core insight of Bayesian forecasting is to hold beliefs lightly and update them in proportion to the weight of evidence:

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

1. **Establish the Prior ($P(A)$):** Use a **base rate** from a specific reference class (e.g., U.S. public companies of a similar starting revenue size over the last 75 years).
2. **Handle the Zero-Probability Problem:** If no historical company in the reference class has achieved the target growth rate, the math of Bayes' Theorem fails ($P(A) = 0$). To resolve this, planners use heuristics (such as Laplace smoothing or $3/N$), which typically yield an initial probability of **less than 0.1%** for unprecedented growth rates.
3. **Determine the Posterior ($P(A|B)$):** Adjust the prior probability upward or downward as new information (such as real-world revenue execution, adoption rates, or customer contract growth) is reported.

---

### Case Studies: AI Capex Projections (2025–2026)

#### 1. OpenAI Revenue Projections
*   **Forecast:** From **$3.7B in 2024** to **$145B in 2029** (a **108% 5-year CAGR**), and **$200B by 2030**.
*   **Prior (Base Rate):** A reference class of U.S. public companies with initial sales of $2–5B (18,900 firm-periods, 1950–2024).
    *   *Base Rate Result:* **No public company has grown this fast for five years in the last 75 years.** The average nominal 5-year CAGR is 7.0% (std dev 10.6%). OpenAI's forecast implies a **9.5 standard deviation outcome** under a normal approximation.
    *   *Roll-forward (2025–2030):* Projected CAGR of 72.7% from a starting point of $13B. In a reference class of companies starting with $10–15B in sales (3,700 firm-periods), **no company has ever achieved a 72.7% CAGR over 5 years**.
*   **Updating Factors:**
    *   *Positive:* ChatGPT reached 100M users in just 2 months (unprecedented diffusion speed). 2025 estimated sales of $13B shows strong near-term execution.
    *   *Negative:* Unprofitable growth with massive cash burn (negative FCF of -$9B in 2025, -$17B in 2026) requiring dilutive capital. Stock-Based Compensation (SBC) exceeded 45% of sales in 2025 ($1.5M/employee annual rate), which is 7x higher than any major technology startup in history prior to going public.

#### 2. Oracle Cloud Infrastructure (OCI)
*   **Forecast:** Cloud revenues growing from **$10B in FY2025** to **$166B in FY2030** (a **75% 5-year CAGR**).
*   **Prior (Base Rate):** Reference class of U.S. public companies with starting sales of $8–12B (4,400 observations).
    *   *Base Rate Result:* **No company with $10B+ in sales has ever grown this fast for five years in the past 75 years.** In fact, no company with $5.6B+ in sales has achieved that growth rate. The average CAGR is 5.7% (std dev 9.6%).
*   **Updating Factors:**
    *   *Positive:* Significant growth in Remaining Performance Obligations (RPO) from signed multi-billion dollar agreements.
    *   *Negative:* Capital requirements to build capacity, power grid bottlenecks, and counterparty risk if renting startups run out of capital before completing contract terms.

---

### Project Success Rates and Datacenter Buildouts

AI datacenter construction involves massive capital, specialized GPU hardware, high power density, and complex liquid cooling, making them high-risk capital projects.

*   **Project Success Base Rates (Bent Flyvbjerg's 16,000 projects):**
    *   *Completed on or under budget:* **< 50%**
    *   *Completed on budget AND on time:* **< 9%**
    *   *Completed on budget, on time, AND delivering anticipated benefits:* **0.5%**
*   **AI Infrastructure Bottlenecks:** Securing power/electricity grid connections (lead times stretch to 7–10 years in major metros) and securing key substation components like high-voltage transformers (lead times of 3–5 years).
*   **Mitigants:** Shifting to modular datacenter designs (which historically have higher success rates than unique designs) and applying a "think slow, act fast" planning methodology.

---

### Strategic Capacity Expansion and Preemption

AI infrastructure builds represent a **"preemptive strategy"** (under Michael Porter's capacity expansion framework) where a firm makes early, massive resource commitments to lock up key resources (land, power, chips) and deter competitors.

*   **Incumbents vs. Startups:** Preemption is highly risky for startups (OpenAI, Anthropic, xAI) that must continually raise dilutive capital. Well-capitalized incumbents (Google, Microsoft, Amazon, Meta) have substantial financial resources and cash flows to absorb expansion costs.
*   **The Risk of Overcapacity:** If the preemptive strategy fails to deter competitors, it historically leads to **industry overcapacity, price collapses, and corporate bankruptcies** (analogous to the fiber-optic telecom buildout bubble of 1999–2002).

---

### References

[Michael J. Mauboussin & Dan Callahan, CFA](https://www.morganstanley.com/im/publication/insights/articles/article_bayesandbaserates.pdf): "Bayes and Base Rates: How History Can Guide Our Assessment of the Future," *Consilient Observer*, Morgan Stanley Investment Management [2026-02-10]
