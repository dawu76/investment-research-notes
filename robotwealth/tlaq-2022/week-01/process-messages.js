const fs = require('fs');

// Read the raw messages
const data = JSON.parse(fs.readFileSync('./discord-messages-raw.json', 'utf8'));

// High-signal users to preserve
const highSignalUsers = ['therobotjames', 'robotkris', 'robotkris.'];

// Clean up message content - remove filler and extract actual content
function cleanContent(content) {
  // Remove the archive metadata prefix
  let cleaned = content.replace(/\n?\[Attachment\/Embed\]: /, '');

  // Extract username, content, and original date from archived format
  // Format: "usernameContent text (Archived from: ..., Original date: DD/MM/YYYY at HH:MM AM/PM UTC)"
  const archiveMatch = cleaned.match(/^([\s\S]*?)\(Archived from:.*?Original date: (\d{1,2}\/\d{1,2}\/\d{4}) at (\d{1,2}:\d{2} [AP]M) UTC\)$/);
  if (archiveMatch) {
    const fullStart = archiveMatch[1];
    let username = '';
    let content = fullStart;

    // Known usernames to check (sorted by length descending to match longest first)
    const knownUsers = ['namitchopra_20013', 'jovial_panda_70993', '.ianforcements', 'satorinakamoto',
                        'dawongandonly', 'vincentfreeman', 'therobotjames', 'tlaq_importer',
                        'timexcellent', 'orlando8826', 'kevinw7235', 'zdenekjanda', 'zapgambles',
                        'robotkris.', 'n.kemalure', 'marco01983', 'kairos.ess', 'egonomics',
                        '.meatfish', 'robotkris', 'quarry614', 'werewitt', 'zane2526',
                        'faz3723', 'welcap', 'lkc673'];

    for (const user of knownUsers) {
      if (fullStart.startsWith(user)) {
        username = user;
        content = fullStart.substring(user.length);
        break;
      }
    }

    if (!username) {
      // Fallback: find first uppercase letter as content start
      const upperMatch = fullStart.match(/^([a-z0-9_.]+)([A-Z@'].*)$/s);
      if (upperMatch) {
        username = upperMatch[1];
        content = upperMatch[2];
      } else {
        // Last resort: assume all lowercase before first space is username
        const spaceIdx = fullStart.indexOf(' ');
        if (spaceIdx > 0) {
          username = fullStart.substring(0, spaceIdx);
          content = fullStart.substring(spaceIdx + 1);
        } else {
          username = fullStart;
          content = '';
        }
      }
    }

    // Parse the original date (DD/MM/YYYY format)
    const dateParts = archiveMatch[2].split('/');
    const originalDateStr = `${dateParts[2]}-${dateParts[1].padStart(2, '0')}-${dateParts[0].padStart(2, '0')}`;

    return {
      extractedUser: username,
      content: content.trim(),
      originalDate: originalDateStr
    };
  }

  // Check for archived format without original date extraction
  const simpleMatch = cleaned.match(/^([a-zA-Z0-9_.]+)([\s\S]*?)\(Archived from:.*?\)$/);
  if (simpleMatch) {
    let extractedContent = simpleMatch[2].trim();
    extractedContent = extractedContent.replace(/^[,.:;!?]\s*/, '');
    return {
      extractedUser: simpleMatch[1],
      content: extractedContent,
      originalDate: null
    };
  }

  return {
    extractedUser: null,
    content: cleaned.trim(),
    originalDate: null
  };
}

// Process messages
const processedMessages = [];
for (const msg of data.messages) {
  const cleaned = cleanContent(msg.content);
  if (!cleaned.content) continue;

  // Skip very short filler messages
  const lowerContent = cleaned.content.toLowerCase();
  if (cleaned.content.length < 10 &&
      !highSignalUsers.includes(cleaned.extractedUser) &&
      (lowerContent.includes('thanks') ||
       lowerContent.includes('got it') ||
       lowerContent === 'image.png' ||
       lowerContent.match(/^:.*:$/))) {
    continue;
  }

  // Use original date if available, otherwise use message timestamp
  let displayDate;
  if (cleaned.originalDate) {
    displayDate = cleaned.originalDate;
  } else {
    displayDate = new Date(msg.timestamp).toISOString().split('T')[0];
  }

  processedMessages.push({
    username: cleaned.extractedUser || msg.username,
    timestamp: msg.timestamp,
    displayDate: displayDate,
    content: cleaned.content,
    isHighSignal: highSignalUsers.includes(cleaned.extractedUser)
  });
}

// Group messages by theme/topic
const themes = {
  'Module 1 Overview and Core Philosophy': [],
  'Position Sizing and Volatility': [],
  'Trading Too Often and Transaction Costs': [],
  'Market Efficiency and Competition': [],
  'Finding Edges and Opportunities': [],
  'Constrained Markets and Forced Selling': [],
  'Auction Mechanics and Price Discovery': [],
  'Practical Questions and Broker Recommendations': [],
  'Course Structure and Content': []
};

// Keywords for categorization
const themeKeywords = {
  'Module 1 Overview and Core Philosophy': ['module 1', 'main point', 'competitive', 'don\'t be a dick', 'discipline', 'dumb shit', 'plan'],
  'Position Sizing and Volatility': ['sizing', 'volatility', 'position size', 'too big', 'blow up', 'returns per unit', 'rebalancing', 'double the size'],
  'Trading Too Often and Transaction Costs': ['trading too often', 'transaction cost', 'basis points', 'fees', 'turnover'],
  'Market Efficiency and Competition': ['efficient', 'mispriced', 'equilibrium', 'fair value', 'competitive', 'unpredictable', 'randomness'],
  'Finding Edges and Opportunities': ['edge', 'alpha', 'opportunity', 'profitable', 'exploit', 'where do we find', 'trade idea'],
  'Constrained Markets and Forced Selling': ['constrained', 'forced', 'march 2020', 'vix', 'TLT', 'NAV', 'discount', 'stressed', 'limit down'],
  'Auction Mechanics and Price Discovery': ['auction', 'opening', 'supply and demand', 'order book', 'price discovery', 'gap'],
  'Practical Questions and Broker Recommendations': ['broker', 'interactive brokers', 'UK', 'ETF', 'futures', 'crypto'],
  'Course Structure and Content': ['module 2', 'module 3', 'webinar', 'video', 'exercise', 'spreadsheet', 'course']
};

// Categorize each message
for (const msg of processedMessages) {
  const contentLower = msg.content.toLowerCase();
  let assigned = false;

  // Priority assignment for high-signal users with substantial content
  if (msg.isHighSignal && msg.content.length > 200) {
    // These are usually comprehensive explanations - categorize carefully
    for (const [theme, keywords] of Object.entries(themeKeywords)) {
      const matchCount = keywords.filter(kw => contentLower.includes(kw.toLowerCase())).length;
      if (matchCount >= 2) {
        themes[theme].push(msg);
        assigned = true;
        break;
      }
    }
  }

  if (!assigned) {
    // Standard categorization
    for (const [theme, keywords] of Object.entries(themeKeywords)) {
      if (keywords.some(kw => contentLower.includes(kw.toLowerCase()))) {
        themes[theme].push(msg);
        assigned = true;
        break;
      }
    }
  }

  // Default to overview if not categorized
  if (!assigned && msg.content.length > 50) {
    themes['Module 1 Overview and Core Philosophy'].push(msg);
  }
}

// Generate markdown
let markdown = `# Trade Like a Quant - Module 1 Discussion Notes

**Channel:** ${data.channelName}
**Scraped:** ${new Date(data.scrapedAt).toLocaleDateString()}
**Total Messages Processed:** ${processedMessages.length}

---

## Table of Contents

`;

// Generate TOC
const orderedThemes = [
  'Module 1 Overview and Core Philosophy',
  'Position Sizing and Volatility',
  'Trading Too Often and Transaction Costs',
  'Market Efficiency and Competition',
  'Finding Edges and Opportunities',
  'Constrained Markets and Forced Selling',
  'Auction Mechanics and Price Discovery',
  'Practical Questions and Broker Recommendations',
  'Course Structure and Content'
];

for (const theme of orderedThemes) {
  if (themes[theme].length > 0) {
    const anchor = theme.toLowerCase().replace(/[^a-z0-9]+/g, '-');
    markdown += `- [${theme}](#${anchor}) (${themes[theme].length} messages)\n`;
  }
}

markdown += '\n---\n\n';

// Generate content for each theme
for (const theme of orderedThemes) {
  const messages = themes[theme];
  if (messages.length === 0) continue;

  markdown += `## ${theme}\n\n`;

  // Sort by date (using displayDate for proper chronological order)
  messages.sort((a, b) => {
    return new Date(a.displayDate) - new Date(b.displayDate);
  });

  for (const msg of messages) {
    const userPrefix = msg.isHighSignal ? '**' : '';
    const userSuffix = msg.isHighSignal ? '**' : '';

    // Format content - handle multi-line content, indent continuation lines
    let formattedContent = msg.content
      .split('\n')
      .map(line => line.trim())
      .filter(line => line)
      .join('\n  ');

    // Format: bullet with username + date + content on same line (no line break)
    const marker = msg.isHighSignal ? '⭐ ' : '';
    markdown += `- ${marker}${userPrefix}${msg.username}${userSuffix} (${msg.displayDate}): ${formattedContent}\n\n`;
  }

  markdown += '---\n\n';
}

// Add key insights summary at the end
markdown += `## Key Takeaways (High-Signal User Insights)

### From therobotjames:

`;

const jamesInsights = processedMessages
  .filter(m => m.username === 'therobotjames' && m.content.length > 200)
  .sort((a, b) => b.content.length - a.content.length)
  .slice(0, 5);

for (const insight of jamesInsights) {
  // Get first meaningful paragraph
  const paragraphs = insight.content.split('\n').filter(p => p.trim().length > 50);
  const preview = paragraphs[0] ? paragraphs[0].substring(0, 400) + (paragraphs[0].length > 400 ? '...' : '') : insight.content.substring(0, 400);
  markdown += `- ${preview}\n\n`;
}

markdown += `### From robotkris:

`;

const krisInsights = processedMessages
  .filter(m => m.username === 'robotkris.' && m.content.length > 150)
  .sort((a, b) => b.content.length - a.content.length)
  .slice(0, 5);

for (const insight of krisInsights) {
  const paragraphs = insight.content.split('\n').filter(p => p.trim().length > 50);
  const preview = paragraphs[0] ? paragraphs[0].substring(0, 400) + (paragraphs[0].length > 400 ? '...' : '') : insight.content.substring(0, 400);
  markdown += `- ${preview}\n\n`;
}

// Write output
fs.writeFileSync('./module-1-discussion-notes.md', markdown);
console.log('Generated module-1-discussion-notes.md');
console.log(`Processed ${processedMessages.length} messages into ${orderedThemes.filter(t => themes[t].length > 0).length} themes`);
