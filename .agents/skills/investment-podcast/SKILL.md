---
name: investment-podcast
description: Guides the ingestion, summarization, and formatting of investment-related podcasts and interview overviews.
---

# Ingesting and Summarizing Investment Podcasts

Use this skill when the user requests to add a podcast episode, interview, or verbal discussion to the wiki. It ensures that the overview meets structural standards, is placed in the correct location, and is properly registered in the wiki index.

---

## 1. Raw Transcript Retrieval and Storage

Before synthesizing the podcast summary, retrieve the raw transcript from the video/audio source.

### **Acquisition and Formatting**
1. Fetch the transcript programmatically (e.g., using `youtube_transcript_api` in a temporary Python helper script).
2. Format the raw transcript with timestamp prefixes for every segment: `[MM:SS] Text...` (e.g., `[14:20] The Fed is likely to raise...`).
3. Save the formatted raw transcript to the `trading/interviews/` directory.
4. **File Name Format:** Use lowercase, hyphenated slugs:
   `YYYYMMDD-[guest-name]-[show-name]-transcript.md`
   *Example:* `trading/interviews/20260716-jack-schwager-excess-returns-transcript.md`

### **Cleanup**
* **Tidy Workspace:** Always delete any temporary download/fetch scripts (such as `fetch_transcript.py`) immediately after the raw transcript has been saved to prevent cluttering the repository.

---

## 2. Directory and File Naming Conventions for Summaries

All podcast overviews must be placed in a `podcasts/` subdirectory within the most relevant topic folder. Do not clutter the root of the topic directories.

- **Macro podcasts:** `investing-macro/podcasts/`
- **Options/Volatility podcasts:** `investing-options/podcasts/`
- **Fundamentals/Equity research podcasts:** `investing-fundamentals/podcasts/`
- **Crypto podcasts:** `investing-crypto/podcasts/`

### **File Name Structure**
Use lowercase, hyphenated slugs ending with the episode release date in `YYYYMMDD` format:
`[show-abbreviation]-[hyphenated-episode-title]-[YYYYMMDD].md`

*Example:* `tcaf-too-early-to-get-off-the-wave-20260626.md`

---

## 3. Page Frontmatter

Every podcast summary must include a standard frontmatter block:

```yaml
---
title: "Episode Title | Show Name [Episode/Episode Number]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept
tags: [macro, fed, rates, credit, etc. - must match SCHEMA.md taxonomy]
sources: [URL to video/audio, and/or path/to/raw/transcript.md if saved locally]
confidence: high
contested: false
---
```

---

## 4. Required Page Sections

Every overview page must be structured with the following sections to maintain a consistent reading experience:

### **I. Executive Summary**
A 2-3 sentence overview of the core macro or micro thesis presented, the sentiment of the speakers, and the overall conclusion.

### **II. Timestamps & Agenda**
Include chronological timestamps with brief bullet points describing each segment.

### **III. Detailed Key Takeaways**
Deep-dive paragraphs on the core themes discussed (e.g., Fed policy changes, supply chain choke points, market breadth). Each theme should:
*   Explain the macroeconomic or fundamental reasoning behind it.
*   Include **illustrative quotes** from the guests or hosts to ground the claims.

### **IV. Portfolio Positioning & Action Items**
Actionable steps for a personal portfolio based on the discussion:
*   How to adjust asset allocation (equities, cash, bonds, crypto, real estate).
*   Sectors/strategies to overweight or underweight.
*   Key indicators to monitor (e.g., credit spreads, 10-year yield, regional bank stocks).

### **V. Asset Class & Sector Breakdown Table**
A structured markdown table summarizing specific mentions:

| Asset Class / Sector | Stock / ETF | View | Rationale / Catalyst |
| :--- | :--- | :--- | :--- |
| *e.g., Semiconductors* | *Micron (MU)* | *Highly Bullish* | *Surging HBM demand, pricing power, Q3 blowout.* |

### **VI. Cross-References**
Include a bulleted list of `[[wikilinks]]` linking to at least 2 existing wiki pages (e.g., `[[valuations]]`, `[[yen-carry-trade-unwinding-2025]]`).

---

## 5. Wiki Registration Workflow

After writing the file, you must complete the following registration steps:

1.  **Index Entry:** Open [index.md](file:///Users/howardwu/dev/investment-research-notes/index.md) and list the page under its respective category.
    *   **Subfolder Indicator:** Append `(podcasts/)` next to the link to indicate its subfolder placement.
    *   **Chronological Order:** Insert the entry in reverse chronological order (newest date first) relative to other listings in that section.
    *   *Example:* `- [[tcaf-too-early-to-get-off-the-wave-20260626]] (podcasts/) — Podcast discussion...`
2.  **Log Entry:** Append an entry to the top of [log.md](file:///Users/howardwu/dev/investment-research-notes/log.md) recording the `ingest` action. Detail both the summary document and the raw transcript file.
    *   *Format:*
        ```markdown
        ## [YYYY-MM-DD] ingest | Show Name — Episode Title | Guest
        
        - Created: `path/to/summary-page.md` (Brief description)
        - Created: `path/to/raw-transcript-page.md` (Raw interview transcript with timestamps)
        - Updated: `index.md`
        - Updated: `log.md`
        ```
3.  **Wiki Count:** Increment the total pages count at the top of `index.md`.
