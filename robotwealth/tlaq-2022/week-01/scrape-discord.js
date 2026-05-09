const puppeteer = require('puppeteer-core');

async function scrapeDiscord() {
  console.log('Connecting to Chrome...');

  // Connect to existing Chrome instance with remote debugging
  const browser = await puppeteer.connect({
    browserURL: 'http://127.0.0.1:9222',
    defaultViewport: null
  });

  // Get all pages and find the Discord tab
  const pages = await browser.pages();
  let discordPage = null;

  for (const page of pages) {
    const url = await page.url();
    if (url.includes('discord.com')) {
      discordPage = page;
      break;
    }
  }

  if (!discordPage) {
    console.error('No Discord tab found. Please make sure Discord is open in Chrome.');
    await browser.disconnect();
    return;
  }

  console.log('Found Discord tab, starting message collection...');

  // Collect messages while scrolling through the entire channel
  const allMessageIds = new Set();
  const allMessages = [];

  // First scroll to top to start from beginning
  console.log('Scrolling to top of channel...');
  let atTop = false;
  let topScrollCount = 0;
  while (!atTop && topScrollCount < 500) {
    const scrolledToTop = await discordPage.evaluate(() => {
      const messagesContainer = document.querySelector('[class*="messagesWrapper"]');
      if (messagesContainer) {
        const scroller = messagesContainer.querySelector('[class*="scroller"]');
        if (scroller) {
          const wasAtTop = scroller.scrollTop === 0;
          scroller.scrollTop = 0;
          return wasAtTop;
        }
      }
      return false;
    });

    if (scrolledToTop) {
      atTop = true;
    }

    await new Promise(r => setTimeout(r, 200));
    topScrollCount++;

    if (topScrollCount % 50 === 0) {
      console.log(`  Still scrolling to top... (${topScrollCount} scrolls)`);
    }
  }
  console.log(`Reached top after ${topScrollCount} scrolls`);

  // Now scroll down and collect all messages until end of channel
  console.log('Collecting messages while scrolling down to end of channel...');
  let noNewMessages = 0;
  let scrollCount = 0;
  let latestDate = new Date(0);

  while (noNewMessages < 20) {
    // Extract current messages
    const currentMessages = await discordPage.evaluate(() => {
      const messageElements = document.querySelectorAll('[id^="chat-messages-"]');
      const msgs = [];

      messageElements.forEach(msgEl => {
        const msgId = msgEl.id;
        let username = '';
        const usernameEl = msgEl.querySelector('[class*="username"]');
        if (usernameEl) {
          username = usernameEl.textContent.trim();
        }

        let timestamp = '';
        const timeEl = msgEl.querySelector('time');
        if (timeEl) {
          timestamp = timeEl.getAttribute('datetime') || timeEl.textContent.trim();
        }

        let content = '';
        const contentEl = msgEl.querySelector('[id^="message-content-"]');
        if (contentEl) {
          content = contentEl.textContent.trim();
        }

        const accessoriesEl = msgEl.querySelector('[id^="message-accessories-"]');
        if (accessoriesEl && accessoriesEl.textContent.trim()) {
          const accessoryText = accessoriesEl.textContent.trim();
          if (accessoryText && accessoryText !== content) {
            content += '\n[Attachment/Embed]: ' + accessoryText;
          }
        }

        let replyTo = '';
        const replyEl = msgEl.querySelector('[class*="repliedMessage"]');
        if (replyEl) {
          replyTo = replyEl.textContent.trim();
        }

        if (content || username) {
          msgs.push({
            id: msgId,
            username: username || '[continued]',
            timestamp: timestamp,
            content: content,
            replyTo: replyTo
          });
        }
      });

      return msgs;
    });

    // Add new messages
    let newCount = 0;
    for (const msg of currentMessages) {
      if (!allMessageIds.has(msg.id)) {
        allMessageIds.add(msg.id);
        allMessages.push(msg);
        newCount++;

        // Track latest date
        if (msg.timestamp) {
          const msgDate = new Date(msg.timestamp);
          if (msgDate > latestDate) {
            latestDate = msgDate;
          }
        }
      }
    }

    if (newCount === 0) {
      noNewMessages++;
    } else {
      noNewMessages = 0;
    }


    // Scroll down
    await discordPage.evaluate(() => {
      const messagesContainer = document.querySelector('[class*="messagesWrapper"]');
      if (messagesContainer) {
        const scroller = messagesContainer.querySelector('[class*="scroller"]');
        if (scroller) {
          scroller.scrollTop = scroller.scrollHeight;
        }
      }
    });

    await new Promise(r => setTimeout(r, 300));
    scrollCount++;

    if (scrollCount % 50 === 0) {
      const dateStr = latestDate.getTime() > 0 ? latestDate.toISOString().split('T')[0] : 'unknown';
      console.log(`  Collected ${allMessages.length} messages so far (latest: ${dateStr})...`);
    }
  }

  console.log(`Finished collecting. Total unique messages: ${allMessages.length}`);

  // Sort by timestamp
  allMessages.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));

  // Use collected messages
  const messages = allMessages.map(m => ({
    username: m.username,
    timestamp: m.timestamp,
    content: m.content,
    replyTo: m.replyTo
  }));

  console.log(`Total messages to save: ${messages.length}`);

  // Get channel name
  const channelName = await discordPage.evaluate(() => {
    const channelHeader = document.querySelector('[class*="title-"][class*="themed-"]');
    return channelHeader ? channelHeader.textContent.trim() : 'discord-channel';
  });

  // Format output
  const output = {
    channelName: channelName,
    scrapedAt: new Date().toISOString(),
    messageCount: messages.length,
    messages: messages
  };

  // Save to JSON file
  const fs = require('fs');
  const outputPath = './discord-messages-raw.json';
  fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));
  console.log(`Saved raw messages to ${outputPath}`);

  await browser.disconnect();
  console.log('Done!');
}

scrapeDiscord().catch(console.error);
