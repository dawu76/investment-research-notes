# RW Pro Discord — #data-analysis digest, April 2026

- **Period:** April 1–30, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Raw transcript:** [rw-pro-data-analysis-raw-20260401-20260430.md](./rw-pro-data-analysis-raw-20260401-20260430.md)
- **Volume:** 38 main-channel messages, tooling-heavy this month rather than strategy-heavy — the two biggest threads are both about research infrastructure (IDE choice, and getting off Colab onto a local environment) rather than a specific trading signal.

---

## 1. Positron: a new IDE gets early-adopter buzz

robotkris kicked off the month by flagging posit's new IDE **Positron** — a fork of VS Code built with data science in mind — specifically calling out its variable explorer, which auto-plots distribution and descriptive stats for any dataframe column in the notebook view, saving a lot of manual plotting.

- He's a long-time RStudio user and was skeptical going in, but after trying it said he's likely to switch.
- Several members chimed in with existing usage: Stefan uses it already and likes switching between R and Python plus using Claude in the terminal; Marco specifically likes the built-in "position assistant" for using an LLM inside a session; liz installed it on the spot ("looks beautiful"); andyw, a returning skeptic from a couple of years ago when RStudio-equivalent features weren't there yet, confirmed it's now functional.
- Ewan and Ben pointed out an alternative for non-R users: the VS Code **Data Wrangler** extension does something similar for those staying in Python.

**Sentiment:** Enthusiastic, low-friction tooling adoption — multiple independent confirmations within the same hour, no dissent.

**Pull quotes:**
- robotkris: *"This is genuinely useful - a variable explorer within the notebook view that plots the distribution and descriptive stats of each column if the variable is a dataframe. Saves a lot of plotting."*
- robotkris: *"I've been a long time R Studio enjoyor and I think I'm going to make the switch. I was very skeptical going in, but I really like it."*

## 2. Measuring how autocorrelation structure changes over time

Rachit proposed a method for tracking how a series's autocorrelation evolves: for a given lookback window and number of lags, compute the ACF at each period, then take the "area under the curve" of that ACF as a single time-varying summary statistic, and asked if this made sense or if there was a better approach.

robotkris's answer reframed the question rather than just validating the AUC idea: instead of (or alongside) a single AUC summary, look at the **significance levels of individual lags over time**, or track the **number of significant lags** at each point. His point was that each of these measurement choices captures a genuinely different angle on "how has autocorrelation changed" — there isn't one canonical answer.

**Sentiment:** Quick, substantive methodology exchange — one question, one thoughtful multi-angle answer.

**Pull quotes:**
- Rachit: *"for each period calculate ACF(w, L) ,\ncalculate 'area under the curve' of ACF calculated in previous step"*
- robotkris: *"Could also look at significance levels of individual lags over time. Or number of significant lags. Each way you measure it will give you a slightly different angle."*

## 3. Replicating the VX30/VIX3M "hurricane slayer" research

deal_me_in set out to independently reproduce the hurricane slayer research and hit an early data problem: how to calculate VX30 from Yahoo Finance data (or find a proxy via ^VIX3M or ETNs). He resolved it himself within a couple of hours using the `vix-utils` PyPI package, then posted a VX30/VIX3M mean-next-day-return-by-z-score-decile bar chart (image only, not captured in the text transcript) showing his early results, and opened a dedicated thread on 4/12 noting he was **getting different results versus the RW note** — the thread's in-thread replies weren't captured by this extraction (main-channel only), so the resolution of that discrepancy isn't reflected here.

**Sentiment:** Self-directed, resourceful — solved his own blocker before anyone else weighed in, then flagged a real discrepancy worth following up (see the linked thread for the actual thread discussion).

**Pull quotes:**
- deal_me_in: *"Im trying to calculate VX30. Does anyone know how to do this with yahoo finance data (or is that impossible)? Are there other proxies I can use (either with ^VIX3M or ETNs)?"*
- deal_me_in: *"Found it… vix-utils from pypi did the thing"*
- deal_me_in (thread title): *"im getting different results vs the RW note"*

## 4. Concretum's daily 15:45 OHLCV database, shared and side-eyed

MidKnight shared a link to Concretum Group's daily 15:45 OHLCV database, pitched as useful for reliable backtesting. TimExcellent replied with a linked tweet and a one-word reaction ("yikes..") that reads as skeptical of the product/claim, though no further discussion unpacked why. robotkris was more positive, calling it "really useful" without elaboration.

**Sentiment:** Mixed and unresolved — one skeptical reaction, one endorsement, no follow-up discussion to reconcile them.

**Pull quotes:**
- robotkris: *"This is really useful"*
- TimExcellent: *"yikes.."* (in reply, linking to a related tweet)

## 5. Getting off Colab: running Lab tooling (R, rsims) on a local environment

This was the month's largest and most substantive thread, running from 4/19 through 4/29.

**The problem:** Rachit asked whether there was a guide for connecting to the Lab and running R locally instead of in Colab. His frustration was concrete — frequent reauth/library-reload cycles, sessions disconnecting when switching contexts, and losing local LLM tooling every time he's back in Colab. MidKnight echoed the same want from the non-R side: getting Lab data into whatever local tools he prefers.

**Pointers to existing resources:**
- Ben pointed to a pinned guide in "the Forum" channel.
- robotkris linked a specific pinned resource, *"Clarifications Around Lab Data,"* covering how to get Lab data into a local session.
- Separately, whiplash asked robotkris directly for a documentation/webinar section on the Lab's backend infrastructure, referencing robotkris's past data-engineering course content — this went unanswered in-channel this month.

**robotkris's core technical answer**, given in detail after Rachit reported still hitting Colab RAM/timeout issues even after reading the pinned resource:
- Pointed to his own public blog post on **connecting Colab to a local Jupyter runtime** (robotwealth.com/how-to-connect-google-colab-to-a-local-jupyter-runtime/), which solves the RAM problem while keeping the Colab-native workflow.
- For a fully local (non-Colab-connected) setup matching the Lab's environment, he explained precisely what changes: skip the setup script that runs in the first cell of every Lab notebook (that script is Colab-specific — it provisions a fresh Ubuntu environment with libraries every session), and instead install packages once locally, then replace that first cell with direct `library()` calls. He gave the exact replacement code, including the `pacman::p_load_gh("RWLab/rwRtools", ...)` incantation for installing rsims and other GitHub-hosted packages — a one-time step in a persistent local environment vs. the every-session reinstall Colab requires.

**Resolution:** Rachit tried the local-runtime blog post first and got partway there — "impatient" with local package installation, he ended up buying Colab credits as a stopgap (4/27) — but with robotkris's follow-up local-library-call approach reported back two days later that he was **up and running locally**, and by 4/30 was reflecting positively on the switch to R itself for analysis work, separate from the tooling friction.

**Sentiment:** A real pain point resolved end-to-end thanks to robotkris's detailed, code-level walkthrough — worth bookmarking for anyone else fighting Colab session/RAM limits.

**Pull quotes:**
- Rachit: *"I keep having to reauth and load libs etc often bcs Ill move between things and the session will disconnect. Kills my flow. also all the llm stuff i've got on my local gets lost in colab."*
- robotkris: *"if you're connecting to a local jupyter runtime, you won't need to use the setup script that features in the first cell of every Lab notebook. That setup script is tailored specifically to the Colab environment... To run that stuff locally, I would just install the packages you need (you only need to do this once - whereas we do it every time we spin up a fresh Colab server), then comment out that first code block and replace with a bunch of library calls."*
- Rachit: *"this was super helpful tyvm Kris. pretty much up and running locally"*
- Rachit (closing reflection, 4/30): *"man I really am enjoying using R for analysis work... it feels like fewer layers of translation between thought and plot"*

## 6. Feather file version consistency in the Lab

MidKnight asked robotkris whether all feather files in the Lab use the same format version, noting multiple feather versions exist. robotkris confirmed they're **version 1** "from memory" — a legacy constraint from when the pipeline was built, since v1 was needed for compatibility with R's feather libraries at the time — and added that this is likely no longer a hard requirement, so a future move to v2 shouldn't be blocked technically.

**Sentiment:** Small factual clarification with an open-ended "we could probably upgrade this" note, not treated as urgent.

**Pull quotes:**
- robotkris: *"They should be version 1 from memory.... we started developing the pipeline at a time when you needed to use version 1 for compatibility with the feather libraries in R... there should be nothing stopping us switching over to v2."*

---

## Overall read

April's #data-analysis was dominated by infrastructure and tooling rather than trading signals — the Positron IDE thread and the Colab-to-local-environment thread together account for over half the month's messages. The throughline across both is a community-wide push toward faster, more persistent local research environments (whether that's a new IDE with better dataframe introspection, or getting off Colab's ephemeral sessions entirely), with robotkris doing the heavy lifting on the infrastructure side — both pointing to existing documentation and, when that wasn't enough, writing out the exact local-environment setup code. The one open technical thread worth following up is deal_me_in's VX30/VIX3M discrepancy versus the official RW note (in a sub-thread not captured here) — that's a concrete data-methodology gap rather than a tooling preference, and worth checking directly in Discord if it matters for anyone running hurricane-slayer-style research.
