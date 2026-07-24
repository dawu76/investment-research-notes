# How to Extract a Full Transcript from a Vimeo Video

## Prerequisites

The video must have captions or subtitles available (auto-generated or manual). You can confirm this by the presence of a **CC button** in the player controls or a **Transcript panel** visible on the side.

---

## Scenario A: Video on its Own Vimeo Page

This applies when the URL in your browser is something like `vimeo.com/123456789` or `player.vimeo.com/video/123456789`.

### Step 1: Open the Developer Console

Press **Cmd + Option + J** (Mac) or **Ctrl + Shift + J** (Windows/Linux). The Chrome DevTools panel opens with the Console tab active. You'll see a `>` prompt at the bottom.

> If Chrome shows a warning saying *"Don't paste code you don't trust"*, type `allow pasting`, press Enter, then paste again.

### Step 2: Paste and Run the Script

Click the console input, paste the following, then press **Enter**:

`````javascript
const video = document.querySelector('video');
const track = video.textTracks[0];
track.mode = 'hidden';
const transcript = Array.from(track.cues).map(c =>
  `[${Math.floor(c.startTime/60)}:${String(Math.floor(c.startTime%60)).padStart(2,'0')}] ${c.text.replace(/<[^>]*>/g,'')}`
).join('\n');
copy(transcript);
```

### Step 3: Paste the Result

The full transcript is now in your clipboard. Press **Cmd + V** to paste it into any text editor, Google Doc, Notion, etc.

---

## Scenario B: Video Embedded in Another Webpage

This applies when the Vimeo player appears as a video window inside someone else's website (a blog post, a course platform, a membership site, etc.). The player is loaded inside an `<iframe>` pointing to `player.vimeo.com`, which means the standard console cannot reach it directly due to browser security rules.

You have two options:

### Option B1: Switch the Console Context to the Iframe (Quickest)

#### Step 1: Open the Developer Console

Press **Cmd + Option + J** (Mac) or **Ctrl + Shift + J** (Windows/Linux) while on the page containing the embedded video.

#### Step 2: Switch the Console Context to the Vimeo Frame

At the top of the Console panel, there is a dropdown that reads `top`. Click it — a list of all frames loaded on the page appears. Look for one that shows `player.vimeo.com` and select it. The dropdown will now display that frame's URL instead of `top`.

Your console commands now execute inside the Vimeo iframe's context, giving you direct access to the video element.

#### Step 3: Paste and Run the Script

Paste the same script as above and press **Enter**:

````javascript
const video = document.querySelector('video');
const track = video.textTracks[0];
track.mode = 'hidden';
const transcript = Array.from(track.cues).map(c =>
  `[${Math.floor(c.startTime/60)}:${String(Math.floor(c.startTime%60)).padStart(2,'0')}] ${c.text.replace(/<[^>]*>/g,'')}`
).join('\n');
copy(transcript);
```

#### Step 4: Paste the Result

The transcript is in your clipboard. Press **Cmd + V** to paste it wherever you need it.

---

### Option B2: Open the Vimeo Player URL Directly (Cleaner)

#### Step 1: Find the Iframe's Source URL

Right-click on the embedded video and choose **Inspect** from the context menu. In the DevTools Elements panel, look at the highlighted element — it should be an `<iframe>` tag with a `src` attribute that looks like `https://player.vimeo.com/video/123456789?...`. Copy that full URL.

> Alternatively, right-click the video and if the option **"Open frame in new tab"** appears, click it — this skips the URL-finding step entirely.

#### Step 2: Open the URL in a New Tab

Paste the copied URL into a new browser tab and navigate to it. You now have the Vimeo player on its own page, which is equivalent to Scenario A.

#### Step 3: Follow Scenario A Steps

Open the console with **Cmd + Option + J**, paste and run the script, then paste your clipboard result wherever you need it.

---

## The Extraction Script (Quick Reference)

```javascript
const video = document.querySelector('video');
const track = video.textTracks[0];
track.mode = 'hidden';
const transcript = Array.from(track.cues).map(c =>
  `[${Math.floor(c.startTime/60)}:${String(Math.floor(c.startTime%60)).padStart(2,'0')}] ${c.text.replace(/<[^>]*>/g,'')}`
).join('\n');
copy(transcript);
```

---

## Troubleshooting

**Chrome shows "Don't paste code you don't trust"**
Type `allow pasting` in the console and press Enter, then paste the script again.

**`track.cues` is null**
Try `track.mode = 'showing'` instead of `'hidden'`. This displays captions on screen but forces all cues to load. Run the rest of the script after that line.

**`video.textTracks` has length 0**
The video has no captions at all. There is no way to extract a transcript programmatically in this case.

**Multiple text tracks (multiple languages)**
Change `textTracks[0]` to the appropriate index (e.g., `textTracks[1]` for the second language option).

**The frame dropdown doesn't show a `player.vimeo.com` entry**
The site may be loading the iframe lazily. Click on the video to interact with it first, then reopen DevTools and check the dropdown again.

**`copy()` is not defined**
This function only works in Chrome and Edge consoles. In Firefox, use `console.log(transcript)` instead and manually select and copy the output from the console.
