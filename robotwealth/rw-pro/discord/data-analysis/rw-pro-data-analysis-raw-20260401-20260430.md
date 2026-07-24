# RW Pro Discord — #data-analysis raw transcript

- **Period:** April 1–30, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Message count:** 38
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:data-analysis after:2026-03-31 before:2026-05-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact April boundaries. Two Discord threads are noted below at their start points but their in-thread replies are not captured by this extraction method (main-channel messages only): "Thread on VX30 / VIX3M hurricane slayer data analysis..." (started 4/12/26 by deal_me_in, 10 messages) and "@Rachit this has some info about" (started 4/27/26 by Matt G, referencing an earlier robotkris message about Lab data access). One image-only message (a VX30/VIX3M mean-return-by-decile bar chart posted by deal_me_in on 4/11/26, 9:28 PM, with no accompanying text) is also not captured by this text-based extraction.

---

4/1/26, 3:37 PM | robotkris: Anyone used posit's new IDE "positron"? It's quite different to R Studio - it's a fork of VS Code designed with data science in mind. This is genuinely useful - a variable explorer within the notebook view that plots the distribution and descriptive stats of each column if the variable is a dataframe. Saves a lot of plotting.
---
4/1/26, 3:38 PM | Stefan: yea ive been using it, its great if you switch a lot between R and python + nice with claude in the terminal
---
4/1/26, 3:47 PM | robotkris: I've been a long time R Studio enjoyor and I think I'm going to make the switch. I was very skeptical going in, but I really like it.
---
4/1/26, 3:49 PM | Ewan [reply]: I think the Data Wrangler plugin for vscode does the same thing, not sure what using R is like in vscode though
---
4/1/26, 3:51 PM | robotkris: Oh right, I will have to check that out
---
4/1/26, 4:05 PM | Ben [reply]: Love Data Wrangler!
---
4/2/26, 10:18 PM | Marco: I like the position assistant, you can use an LLM inside your session
---
4/3/26, 8:46 AM | liz [reply]: just installed it. looks beautiful. excited to give it a shot
---
4/4/26, 7:07 PM | andyw: Blimey! That's changed massively - I tried it a couple of years ago and a lot of the stuff I value in RStudio just wasn't functional then. But is now. Thx
---
4/6/26, 10:06 AM | Rachit: I'm trying to assess how autocorrelation of a series is changing over time, currently doing the following:


given a lookback window w;  and # lags L
,
for each period calculate ACF(w, L)
,
calculate 'area under the curve' of ACF calculated in previous step
,

does this make sense? is there a better way of doing this?
---
4/7/26, 8:47 AM | robotkris [reply]: Could also look at significance levels of individual lags over time. Or number of significant lags. Each way you measure it will give you a slightly different angle.
---
4/11/26, 8:06 PM | deal_me_in: Hi all. Im interested in doing the hurricane slayer research myself. Im trying to calculate VX30. Does anyone know how to do this with yahoo finance data (or is that impossible)? Are there other proxies I can use (either with ^VIX3M or ETNs)? Thanks!
---
4/11/26, 9:16 PM | deal_me_in [reply]: Found it… vix-utils from pypi did the thing
---
4/12/26, 8:21 PM | deal_me_in: deal_me_in
 started a thread: Thread on VX30 / VIX3M hurricane slayer data analysis... im getting different results vs the RW note. See all threads.
 — 
4/12/26, 8:21 PM
Sunday, April 12, 2026 at 8:21 PM
---
4/17/26, 9:01 AM | MidKnight: I thought this was pretty interesting and maybe people here would find it useful:
---
4/17/26, 9:01 AM | MidKnight: https://concretumgroup.com/daily-1545-ohlcv-database-for-reliable-backtesting/
---
4/17/26, 11:18 AM | TimExcellent [reply]: https://x.com/concretumr/status/2044705248481013830?s=46&t=N-bRxq_vUy3zqgpzvnA6zA yikes..
---
4/17/26, 11:24 AM | robotkris [reply]: This is really useful
---
4/19/26, 5:30 AM | Rachit: was there a guide somewhere on getting  connected to the lab and R on a local env ?
---
4/19/26, 7:53 AM | MidKnight: I can't say I've seen anything on it @Rachit . I would love to be able to get data from the lab but apply it easily to my non R preferred tools.
---
4/19/26, 7:59 AM | Rachit: I kinda like the R stuff and would like to use the tools that Kris has built on it, like rsims. Just would like to be using my local ide over colab. I keep having to reauth and load libs etc often bcs Ill move between things and the session will disconnect. Kills my flow. also all the llm stuff i've got on my local gets lost in colab
---
4/19/26, 8:40 AM | Ben [reply]: It is pinned to the top of one of the channels
---
4/19/26, 8:41 AM | Ben: Found it, the Forum
---
4/19/26, 2:56 PM | whiplash: Hey @robotkris ,
With the new refresh of the RW infra, I was wondering if you could give us some insight into the backend? Would be really insightful for the maniacs and autists to get a feel for how to build robust infrastructure. It can be a section in the upcoming webinars or even some documentation of the data infrastructure and how they all tie in.
You had tackled some elements in the data engineering course as well, I and perhaps others in the group are  quite curious to see how things are evolved since then, practically speaking.

Cheers brother
---
4/19/26, 2:58 PM | whiplash [reply]: Looks really cool !
Came across an extension by Vscode called data wrangler that's pretty similar as well ( for the stubborn python users in the house  )
---
4/20/26, 12:05 PM | robotkris [reply]: Yeah really happy to!
---
4/20/26, 12:05 PM | robotkris [reply]: @Rachit this has some info about getting The Lab data into a local session: ⁠Clarifications Around Lab Data…
---
4/20/26, 7:50 PM | Rachit [reply]: thx for that. Was hoping there was a way to preserve the colab env so that my work could translate easily between the lab and my local env. Basically I want to adhere to the spirit of keeping research in the lab but I keep running into issues with colab (e.g. yesterday i did a bunch of stuff in the morning which worked fine initially, but then the env kept blowing up on lack of ram. I was able to resolve that by just running fewer cells but then the runtime inexplicably kept timing out and i couldn't make much progress for the rest of the day).

it probably pilot error. I'll try to get R running locally with the rwlab tools when i muster the patience again. I'm really warming up to R over py for research work, just gotta get over some of these env humps.
---
4/20/26, 8:29 PM | robotkris: @Rachit  One option is to connect colab to a local runtime. I wrote a post about this on the public blog ages ago - it should still work: https://robotwealth.com/how-to-connect-google-colab-to-a-local-jupyter-runtime/

That will solve the RAM issue. To get the same environment was we're running in Colab, you could spin up a container and install the packages the same way we do in our Colab sessions with this setup script: https://github.com/RWLab/rwRtools/blob/master/examples/colab/load_libraries.R
---
4/20/26, 8:31 PM | Rachit [reply]: ah of course there is a blog post about it  !! tyvm much appreciated as always, i will give this a try
---
4/20/26, 9:58 PM | robotkris [reply]: Keen to hear how it goes (and whether that blog post is now out of date...)
---
4/23/26, 8:29 AM | MidKnight: @robotkris I note there are different versions of the feather format possible. By chance, are all the feather files in the lab the same version and also what version are they using?
---
4/23/26, 8:42 AM | robotkris [reply]: They should be version 1 from memory.... we started developing the pipeline at a time when you needed to use version 1 for compatibility with the feather libraries in R. Things would have moved on since then and there should be nothing stopping us switching over to v2.
---
4/27/26, 12:18 AM | robotkris: Matt G
 started a thread: @Rachit this has some info about. See all threads.
 — 
4/27/26, 12:18 AM
Monday, April 27, 2026 at 12:18 AM
---
4/27/26, 12:21 AM | Rachit [reply]: blog post worked to setup and run a local runtime. I got hung up on getting the packages installed locally. I got a bit impatient trying to getting some research to a satisfactory point/conclusion and ended up just getting some colab credits  lol
---
4/27/26, 11:37 AM | robotkris [reply]: Fair enough! I should have mentioned that if you're connecting to a local jupyter runtime, you won't need to use the setup script that features in the first cell of every Lab notebook. That setup script is tailored specifically to the Colab environment (running Ubuntu with some useful libraries already installed).

To run that stuff locally, I would just install the packages you need (you only need to do this once - whereas we do it every time we spin up a fresh Colab server), then comment out that first code block and replace with a bunch of library calls. Example:


### COMMENT OUT SETUP SCRIPT ###

# snippet: rw load rwRtools v0.8
# source("https://raw.githubusercontent.com/RWLab/rwRtools/master/examples/colab/load_libraries.R")
# debug_msg <- load_libraries(load_rsims = TRUE, extra_libraries = c("roll", "here", "glue", "scales", "arrow"), extra_dependencies = c())

# cat(debug_msg)

### REPLACE WITH library CALLS ###

library(tidyverse)  # loaded by default in the setup script
library(roll)  # this and below are from the extra_libraries argument from load_libraries above
library(here)
library(glue)
library(scales)
library(arrow)

# Set chart options
options(repr.plot.width = 14, repr.plot.height=7)
theme_set(theme_bw())
theme_update(text = element_text(size = 20))


You can install most libraries with install.packages("package name").

You can install rsims (and other packages hosted on github) with either devtools or pacman (I prefer pacman):
 pacman::p_load_gh("RWLab/rwRtools", dependencies = FALSE, update = FALSE)`

And you only have to do that once in your local environment
---
4/29/26, 9:09 AM | Rachit [reply]: this was super helpful tyvm Kris. pretty much up and running locally
---
4/30/26, 10:27 AM | Rachit: man I really am enjoying using R for analysis work

i'm still a bit slow and doing some mental rewiring after spending so long with Python but it feels like fewer layers of translation between thought and plot
