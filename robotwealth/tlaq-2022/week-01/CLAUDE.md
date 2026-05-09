# Discord Channel Summary Instructions

## Overview

This directory contains scripts for scraping Discord channel messages and organizing them into structured markdown documents. Use these instructions when the user requests a Discord channel summary.

## Prerequisites

- Chrome must be running with remote debugging enabled
- User must have the Discord channel open in Chrome

### Starting Chrome with Remote Debugging

```bash
# Quit Chrome completely first (Cmd+Q on Mac)
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
```

**Note:** The `--user-data-dir` option is required to avoid errors when starting Chrome in debugging mode. This creates a separate profile directory for the debug session.

## File Structure

### Required Scripts
- `scrape-discord.js` - Collects messages from Discord
- `process-messages.js` - Processes and organizes into markdown

### Generated Files (can be deleted, will be recreated)
- `discord-messages-raw.json` - Raw scraped data (intermediate output)
- `module-1-discussion-notes.md` - Final organized markdown

### Not Needed
- `console-scraper.js` - Alternative browser console approach (fallback, can be deleted)

## Data Flow

```
scrape-discord.js → discord-messages-raw.json → process-messages.js → module-1-discussion-notes.md
```

The `discord-messages-raw.json` file stores intermediate data between the two processing steps. Keeping it allows re-running `process-messages.js` with different theme categorizations or formatting without re-scraping Discord.

## Scripts

### 1. `scrape-discord.js` - Message Collection

Connects to Chrome via Puppeteer and scrapes all messages from the currently open Discord channel.

**Features:**
- Scrolls to top of channel first
- Scrolls down collecting messages until no new messages load
- Extracts username, timestamp, content, and reply context
- Deduplicates messages by ID
- Outputs to `discord-messages-raw.json`

**Usage:**
```bash
node scrape-discord.js
```

### 2. `process-messages.js` - Message Processing & Organization

Processes raw messages into a themed, organized markdown document.

**Features:**
- Extracts original dates from archived/imported messages (format: "Original date: DD/MM/YYYY at HH:MM AM/PM UTC")
- Separates username from content using known username list
- Categorizes messages into themed sections
- Marks high-signal users with ⭐ (therobotjames, robotkris)
- Filters out short filler messages
- Generates table of contents

**Usage:**
```bash
node process-messages.js
```

**Output:** `module-1-discussion-notes.md`

## Workflow

1. User opens Discord channel in Chrome (with remote debugging)
2. Run `node scrape-discord.js` to collect messages
3. Run `node process-messages.js` to generate organized markdown

## Customization Points

### Adding New High-Signal Users

In `process-messages.js`, update the `highSignalUsers` array:
```javascript
const highSignalUsers = ['therobotjames', 'robotkris', 'robotkris.'];
```

### Adding New Known Usernames

In `process-messages.js`, add to the `knownUsers` array (sorted by length descending for proper matching):
```javascript
const knownUsers = ['namitchopra_20013', 'jovial_panda_70993', ...];
```

### Modifying Theme Categories

In `process-messages.js`, update the `themes` object and `themeKeywords` to add/modify categories:
```javascript
const themes = {
  'Module 1 Overview and Core Philosophy': [],
  'Position Sizing and Volatility': [],
  // ... add more themes
};

const themeKeywords = {
  'Module 1 Overview and Core Philosophy': ['module 1', 'main point', 'competitive', ...],
  // ... add keywords for categorization
};
```

### Adjusting Scroll Behavior

In `scrape-discord.js`:
- `noNewMessages < 20` - Number of scrolls with no new messages before stopping
- `await new Promise(r => setTimeout(r, 300))` - Delay between scrolls (ms)

## Output Format

The generated markdown includes:

1. **Header** - Channel name, scrape date, message count
2. **Table of Contents** - Links to themed sections with message counts
3. **Themed Sections** - Messages organized by topic
   - Each bullet: `⭐ **username** (YYYY-MM-DD): message content`
   - High-signal users marked with ⭐ and bold
   - Multi-line content indented under bullet
4. **Key Takeaways** - Summary of insights from high-signal users

## Handling Archived/Imported Messages

Many channels contain messages imported from other servers. These have metadata like:
```
(Archived from: Trade Like a Quant, #channel-name. Original date: 26/10/2023 at 12:11 AM UTC)
```

The script:
- Extracts the original date (DD/MM/YYYY) and uses it instead of import date
- Strips the archive metadata from displayed content
- Maintains chronological order based on original dates

## Dependencies

```json
{
  "dependencies": {
    "puppeteer-core": "^latest"
  }
}
```

Install with: `npm install`
