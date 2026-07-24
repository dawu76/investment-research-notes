[00:02] You're watching Excess Returns, the
[00:04] channel that makes complex investing
[00:05] ideas simple enough to actually use,
[00:08] where better questions lead to better
[00:10] decisions. I'm Matt Ziggler, and today's
[00:12] guest is the author and data nerd at
[00:14] Data for the People, like it says on his
[00:17] shirt, Eric Pacman. Welcome back to
[00:19] Access Returns.
[00:20] >> Thank Thanks for having me. Great to be
[00:22] back.
[00:22] >> You came on last call this past month.
[00:25] You did a segment on what the Fed is
[00:28] looking at when they're talking about
[00:30] employment and inflation. I promised we
[00:32] would do this episode to go deeper into
[00:34] each because the stuff you've been
[00:36] writing at Data for the People has been
[00:37] just on fire lately. So, we're going to
[00:40] do the deep dive today. You said though,
[00:42] right before we recorded, you wanted to
[00:44] say thank you. You got a bunch of
[00:45] traffic, a bunch of people checking out
[00:46] the site.
[00:48] >> Yeah, it was almost kind of shocking. I
[00:50] was getting these like anomaly reports
[00:51] from Google and everything that the
[00:54] search traffic like you know we're a
[00:56] sleepy little site um building all
[00:58] organically all word of mouth um you
[01:02] know bare bones to zero funding at this
[01:05] point in time just doing the work
[01:06] because we love it and uh yeah I mean I
[01:09] I was just on the tail end of of your
[01:12] last podcast like your weekly recap type
[01:14] thing and um I all of a sudden it's like
[01:18] you know 60 people signed up for my
[01:20] distribution list and you know
[01:22] distribution list that's a heavy lift
[01:24] right like you have to actually go to
[01:25] the site read the site click a button
[01:27] put your email address in I get it like
[01:30] I that that takes some some commitment
[01:33] and uh and you are
[01:34] >> we have a listener base with gumption
[01:36] we've got some gumption out there and
[01:38] I'm telling you
[01:39] >> very grateful [laughter]
[01:40] >> I'm telling you dear listener at home
[01:42] make the man grateful and you want this
[01:44] data because this this is where I'm
[01:46] starting us we talked about the Fed the
[01:49] way the Fed's looking at the numbers.
[01:50] Eric thinks there are flaws and
[01:53] problems, not just with the numbers
[01:55] they're looking at at the top level, but
[01:57] then as we drill down into their
[01:58] component parts. So, drawing on public
[02:01] data sets like BLS data and other
[02:02] places, he'll give us sources as we go
[02:04] through these. This is not the
[02:07] arrangement that they're looking at this
[02:09] data lens through. So, if you're running
[02:11] money, if you're handling stuff with
[02:13] clients, you want to see data for the
[02:15] people and what he's doing. So I'm going
[02:16] to ask you very very high level right
[02:19] now. I want to lead with employment. I
[02:21] want to lead with labor.
[02:23] >> Yeah.
[02:23] >> The the employment trend in the US right
[02:25] now is is employment running up, down,
[02:29] sideways. What direction does it look
[02:31] like we're heading?
[02:33] >> Yeah. So I I think that um that's
[02:36] actually you phrase that question in
[02:39] exactly the right way and we have a
[02:42] dashboard for that.
[02:44] So if you go to data for the people, we
[02:47] just released a brand new dashboard
[02:50] where we take the current population
[02:52] statistics data. So this is the
[02:53] household survey. So just a little bit
[02:56] like little aside here. Um you know we
[02:59] get the employment report every month
[03:01] moves the market one way or another. Um
[03:04] there are two surveys that are published
[03:07] here. Hopefully most people know this.
[03:09] the CES that is the uh institutional
[03:12] survey that is where the non-farm
[03:14] payroll comes from and the CPS that is
[03:16] the household survey that is where the
[03:18] unemployment rate comes from. So um
[03:21] those are separate they they sometimes
[03:24] will tell completely different stories
[03:26] because they're totally different
[03:27] surveys. One is serving people, the
[03:28] other one is surving businesses, right?
[03:30] Both the response rates are falling off
[03:32] a cliff right now. So there's that, but
[03:34] that's a whole another discussion. So
[03:35] how much we trust them, I don't know.
[03:37] But they're the best data that we have.
[03:39] So when I was with Ban Creek, an asset
[03:43] manager before I started data for the
[03:44] people, we created a really good I mean
[03:48] it was a it's called the tree map and go
[03:50] to banrete.com, you can look at it and
[03:52] you can drill down into the non-farm
[03:54] payroll data. So if you see like I don't
[03:56] know what last month was, it was like
[03:57] 50,000 of change or whatever. Um that's
[04:00] what is called at the BLS hierarchy
[04:02] level zero, highest level. And then when
[04:05] the number gets higher, you go down to
[04:07] more granular levels until you get to
[04:09] like sewing machine fabricators or
[04:11] whatever down at level seven. So So you
[04:13] can see a lot of detail on all the
[04:15] industries that's already there at B
[04:17] Creek. That's the CES. That's the um
[04:21] survey of businesses, right? Non-farm
[04:23] payroll data. So the problem with the
[04:26] CPS data and again sorry for all detail
[04:29] but I think this is really important
[04:31] >> this is really important because these
[04:33] surveys how the surveys are being
[04:35] responded to how the information is
[04:36] being captured is not the headline
[04:38] number and that's why I wanted to unpack
[04:40] this.
[04:41] >> No no and and so and it will also like
[04:44] if you can see this data which this is
[04:47] the challenge like the BLS look I'm not
[04:50] trying to hate on them but their job is
[04:52] not to make you see the data. If you
[04:54] look at the the release from the BLS
[04:57] from last month, the press release, it's
[04:59] like unemployment unchanged,
[05:01] unemployment for black people,
[05:02] unemployment for this, unchanged. It's
[05:04] like great. Your entire story is that
[05:06] there's no story. And then it's like,
[05:08] oh, and by the way, the labor force
[05:10] participation rate fell to 61.5%.
[05:13] That was down point4 points. And I'm
[05:16] like, what the?
[05:19] And then you're just like moving on. and
[05:21] you're just like, "Whoa, whoa, whoa,
[05:23] time out." Like, I'm a storyteller. You
[05:27] lead with the crisis in the labor force
[05:30] participation rate first rather than
[05:32] like there's no change in the
[05:33] unemployment rate, but this is the issue
[05:36] with the BLS right now. And this is the
[05:37] issue with the Fed. It's like you have
[05:40] to go back and like look, ask Claude,
[05:42] you go back and study the history of how
[05:45] these different benchmarks came into
[05:46] place.
[05:48] And there was a comment on that last
[05:50] video. So, I want to address this
[05:51] comment. Um, it was like,
[05:55] you're you're not you're telling me that
[05:57] the Fed doesn't have access to all these
[05:59] tools. Of course, they have access to
[06:00] all these tools. They know all the the
[06:02] minut detail. But they can't all of a
[06:05] sudden come out and say like, for the
[06:07] last 30 years, we've been focusing on
[06:09] the unemployment rate, and guess what?
[06:10] That no longer works. The world has
[06:12] changed. like they've just kind of
[06:14] painted themselves into a corner to say
[06:17] the unemployment rate is the one ring
[06:20] that rules them all. And right now I can
[06:23] tell you investor person that cares
[06:27] about America, you will not see the
[06:30] recession coming with the unemployment
[06:32] rate. It's already in the data. The
[06:35] depression, the recession, the the the
[06:37] crisis, let's call it the labor crisis.
[06:39] It could be like it's an inflationary
[06:42] surge because we just don't have enough
[06:43] people to work. But if you go to data
[06:45] for the people and you look at our
[06:47] latest data visualization which takes
[06:50] almost all the data in the CPS survey
[06:53] and creates a drill down tool to where
[06:55] you can look at every dimension. Forget
[06:57] about the unemployment rate that's in
[06:58] there too for you to look at it and see
[06:59] that nothing's happening. Go look at the
[07:02] people that are not in the labor force
[07:03] right now. You can actually see, and we
[07:06] just wrote about this, the revisions
[07:08] that are happening as the BLS improves
[07:11] their model and the census improves
[07:12] their model and you can see the number
[07:14] of people that are working age people
[07:16] just disappear. And so you're just like,
[07:20] well, wait a second, where are they
[07:21] going? Well, they're they're 75 plus
[07:22] now. And it's like, well, the actual age
[07:25] of people didn't change, but the whole
[07:27] BLS and the whole census runs on models.
[07:29] And we just wrote this. There's this
[07:31] great quote, "All models are wrong, some
[07:33] are useful." Well, they just made their
[07:35] model a little use more useful. Still
[07:38] wrong, but now all of our projections
[07:41] going forward have less working people
[07:43] to pay taxes, to pay into social
[07:45] security, to pay into Medicare. This
[07:48] goes way beyond investing. And I'm not
[07:51] here to tell you like what to believe in
[07:53] it. I'm here to tell you the tool is
[07:55] there. And so you want to answer your
[07:57] question on the number employed people,
[07:59] just go select the series that says
[08:02] employed and you'll see it. And then
[08:04] select it by race, select it by
[08:06] ethnicity, Hispano, uh or Hispanic,
[08:09] Latino, um select it by sex, select it
[08:13] by veteran status. Do it all. I mean,
[08:16] it's all there. By the way, the veterans
[08:17] one is crazy. Like the veterans are
[08:19] falling off a cliff. Like we're just
[08:21] we're not I mean, this is this is well
[08:23] known, but I just learned it. It's like,
[08:24] oh, wow. You know, clearly a lot of the
[08:27] Vietnam era, Gulf War era, they're all
[08:29] dying off and retiring out, but they're
[08:32] not being replaced.
[08:34] So, it's like, where are all the people
[08:35] that are fighting for our country?
[08:37] They're not there anymore. Anyway,
[08:38] that's an aside, but like all the data
[08:40] is there.
[08:41] >> Can we get a slide up for let's look at
[08:43] beyond the employ unemployment rate
[08:45] because this is part of what we're
[08:46] dancing around now. So, let's talk about
[08:48] this. What's going on here?
[08:50] >> Yeah. So, okay. when you pull it up, it
[08:53] will come up to age 16 years and o and
[08:56] over civilian labor force. So I think
[08:59] it's very very important if you
[09:01] understand how cities work to focus on
[09:04] the civilian labor force because that is
[09:06] the number of bodies that create tax
[09:08] revenue. that is the number of bodies
[09:10] that can actually go out and shop for
[09:12] things, support businesses until we
[09:16] come up with a a mechanism to tax bots,
[09:19] AI, and massively tax big tech, which
[09:22] like I'm not holding my breath. Like
[09:24] this is the business model of the US,
[09:26] right? We need people to work. And so
[09:28] that's why you have to look at the labor
[09:29] force. So right now, you see this
[09:31] long-term trend going all the way back
[09:32] to 1950s for 16 years and over. But now
[09:36] just go through and like there there are
[09:37] literally 30 different dimensions and
[09:39] cuts that you can look at in here. You
[09:41] got to spend a little bit of time with
[09:42] this and really have the desire to be
[09:44] educated here. So just go in and look at
[09:46] I'm going to look at the number of 45
[09:48] years and over people. Okay. Then that
[09:50] pulls up what's called a nonseasonally
[09:52] adjusted chart with the 12-month average
[09:54] on that in the civilian labor force.
[09:56] Well, now what if I'm concerned about or
[09:58] if I'm interested in the 45 years and
[10:00] over but just the labor force
[10:02] participation rate? Then you're like,
[10:04] "Uhoh, wait, what happened here?" So, in
[10:07] 2009, that was at 55.9%.
[10:11] And now the 12-month average is down to
[10:14] 50.7
[10:16] and it is falling off a cliff. And by
[10:18] the way, I haven't even looked at this
[10:19] chart before. There are too many
[10:20] dimensions in here to look at, but now
[10:22] all of a sudden, since what happened in
[10:24] January was this whole like
[10:25] reshuffleling of the models, the labor
[10:27] force participation rate is really,
[10:29] really dropping fast for the 45 years
[10:31] and over. It's down to 49.6%.
[10:34] So then you could say, but what about
[10:36] men? Oh well, so men, oh boy, that chart
[10:39] is death. So men is down to 54.7%.
[10:42] The lowest level by far on record, the
[10:46] prior minimum was back in the 1990s
[10:48] where it was 57.5. It went all the way
[10:50] up to 62.9.
[10:52] Women, well, they're much better, which
[10:55] this actually jives with the piece that
[10:56] we just worked about. Women are the
[10:58] driver of our labor force. We have have
[11:00] to thank them. If you're a man, go out
[11:03] and thank the next woman that you see
[11:04] for supporting this labor force and
[11:06] helping it to grow. [laughter] And if
[11:08] you don't believe me, spend even five
[11:10] minutes working through this database to
[11:11] see that men are not participating at an
[11:13] increasing rate and women are
[11:14] participating increasing rate, which we
[11:16] can go into that has a lot to do with
[11:18] which industries are the driver of um
[11:21] our labor force expansion and employment
[11:24] just in general.
[11:24] >> So let's let's take it there. Next,
[11:26] another part that's been fascinating is
[11:29] as we look at those jobs that are coming
[11:30] out, many of which in the 45 plus crowd.
[11:33] So these are the people, you know, these
[11:35] are these are my brethren. These are my
[11:37] peers. These are the ones who are making
[11:39] >> the six figure salary doing some job.
[11:42] Those are the ones that are going away
[11:43] right now. The weird part that's
[11:45] stabilizing the number in employment
[11:47] right now is the other jobs that are
[11:49] being added and they're not that six
[11:51] figure white collar go out and do
[11:53] something because you're 45 with a
[11:54] college degree job. They're coming in
[11:57] >> from what you're calling the Medicaid
[11:59] care economy. And you've got some insane
[12:01] charts explaining why because you've
[12:03] been talking about this for two years.
[12:05] >> Healthcare is the driving place and this
[12:07] Medicaid part of it is huge. Let's let's
[12:09] get some more charts up.
[12:11] >> Yeah. So, um I wish I remembered all
[12:14] these stats right off the top of my
[12:15] head, but you can uh you can go to well,
[12:18] let me let me step back. So, this is
[12:20] about been about a year and a half in
[12:22] the making. So, there there is a
[12:24] visualization on our website called
[12:26] Medicaid Care Economy concentration of
[12:28] state growth, state job growth. So, back
[12:31] when I was at Ban Creek, you know, I my
[12:34] background is in healthcare and and and
[12:36] so I'm looking at these healthcare job
[12:38] growth numbers and it's like 60% of
[12:39] total payroll, 70%, 80%. By the time we
[12:43] got to the end of 2025, it was like I
[12:46] don't know, the numbers are in my
[12:47] reports, but it was something like two,
[12:49] three, 400% of all job growth was coming
[12:51] in healthcare. Everything else was
[12:52] contracting. Wall Street Journal covered
[12:54] this. Everybody knew it by that point in
[12:56] time. But what they didn't know because
[12:58] people don't tend to drill down like we
[13:00] do is they didn't know where those jobs
[13:03] were coming from. And so people like are
[13:05] very confused about well is this all
[13:08] administrative oversight because of how
[13:10] inefficient our care economy is? Is it
[13:13] is it actual doctors by the way? No,
[13:15] it's not doctor growth. Is it nurses?
[13:17] Yes, it's nurses growth. We can show you
[13:18] that in a visualization we have. But
[13:20] overwhelmingly
[13:22] this growth is coming from what's called
[13:24] social assistance. And within that
[13:26] individual and family services and
[13:28] within that services for the elderly and
[13:31] disabled
[13:32] and home healthcare aids and so what is
[13:36] that? That is you know um I have an
[13:40] elderly parent or grandparent. They
[13:42] don't need to be institutionalized yet
[13:44] which would be very costly for me and
[13:46] the state andor the state. And so you
[13:48] can drop them off at an elderly daycare
[13:50] facility. They can you know keep track
[13:52] of their meds. They'll have
[13:53] socialization. you can work your job.
[13:55] It's a win-win, right? Um or what we
[13:58] more commonly know is you can hire
[14:00] someone to come into your home to take
[14:02] care of your parent well or your
[14:04] grandparent. Um those people, by the
[14:06] way, we have another data visualization
[14:08] which hopefully you'll put up which
[14:09] shows you what everybody makes 830
[14:12] professions across this country by city.
[14:14] If you go and explore that, you'll see
[14:16] that these are some of the most
[14:17] underpaid people in um really in the
[14:21] entire economy and is the engine of job
[14:24] growth. We wrote another piece on that
[14:26] um which I'll give to you to put in the
[14:28] show notes, but it basically is like
[14:29] we've created a couple million jobs in
[14:32] this over the past like decade or so.
[14:33] And so our aging of the economy, which I
[14:37] think most people know the boomers sort
[14:38] of rolled over into the 65 plus like in
[14:41] the middle of the 2010s, that has
[14:43] created huge demand for people to take
[14:46] care of them. By the way, most of them
[14:47] are women. I think it's like 80% are
[14:50] women, something like that. And about 30
[14:52] to 40% depending on the study, are
[14:54] immigrants. So there's another issue
[14:57] there with maybe a potential supply
[14:59] crunch with the people to take care of
[15:00] them. Anyway, all that said, I'm staring
[15:03] at this for like a year and I was like,
[15:06] then the one big beautiful bill hit,
[15:08] right? So, what's that going to do?
[15:09] Well, it's cutting Medicaid by a
[15:11] trillion dollars over 10 years. And as
[15:14] putting my investor hat on, I'm like,
[15:16] okay, we need jobs to keep growing. We
[15:18] need people to take care of old people
[15:20] to keep growing those jobs. So, the Fed
[15:23] says, "Oh, the the job growth is is
[15:25] healthy." And by the way, what I happen
[15:28] to know is that most of the home
[15:30] healthcare aids, the primary funer for
[15:31] them is Medicaid. And then, you know,
[15:34] Trump in his infinite wisdom, and I'm
[15:36] not being like political here. I'm just
[15:38] saying that he probably doesn't
[15:39] understand the way this works. Um, he
[15:43] decided to cut this or the the the
[15:45] administration decided to cut funding
[15:47] for this, which is basically the major
[15:50] growth driver of our jobs in in our and
[15:52] look, be probably not advised very well.
[15:55] Um, but Medicaid is a state-based
[15:57] program and so you can't really
[16:00] understand what's going to happen unless
[16:02] you drill down into the state. And so
[16:03] that's what I did. I went down into
[16:05] what's called the quarterly census
[16:06] employment wages data. That is, by the
[16:10] way, one of the most valuable databases
[16:12] if you want to understand anything about
[16:14] job growth. It is based on unemployment
[16:17] insurance claims or unemployment
[16:18] insurance reports from states. It covers
[16:20] 98% of all W2 employees. It is not a
[16:24] model. is the only real source of data
[16:27] that we really have at the BLS. It comes
[16:30] out like six to nine months in a rears.
[16:32] So, a lot of investors don't use it, but
[16:34] my gosh, like you can actually get the
[16:36] individual industry down to the
[16:38] individual
[16:40] county. And so, I've used this database
[16:42] for a lot of things, for a lot of the
[16:44] stories of America that I tell, but as
[16:46] an investor, especially with AI, there's
[16:48] no excuse you should be using this
[16:50] database as well or at least reading my
[16:51] stuff because I use it a lot. Um, so
[16:54] that's where this data visualization
[16:55] came from. You can basically look over
[16:57] time and you can actually press this
[16:59] little play button in the window end
[17:01] quarter and then just see how much um
[17:05] job growth came from what's called the
[17:07] Medicaid care economy. So this includes
[17:09] assisted living facilities, it includes
[17:11] nursing homes, that kind of stuff. How
[17:14] much job growth as a percentage of all
[17:15] the job growth in that state over a
[17:17] one-year period, a two-year period, and
[17:19] a three-year period. And what you'll
[17:20] find is that that map gets increasingly
[17:23] more red. And now we're at a point where
[17:26] through the end of 2025, which is all
[17:27] the data we have in that one-year
[17:29] period, like I think it's like 32 33
[17:32] states would have had negative job
[17:34] growth if it wasn't for Medicaid care
[17:36] economy. And then think of that setting
[17:39] up into the beginning of 2027 is when
[17:42] most of those cuts start in Medicaid.
[17:45] And so this is something that every
[17:46] investor needs to at least have on the
[17:48] back of their mind as like this is a
[17:50] major tail risk. Now maybe it's a tail
[17:54] risk to the upside because if all of a
[17:55] sudden we have no jobs then people just
[17:58] care about rates getting cut and then
[17:59] everyone gets really excited about more
[18:01] speculation. I can't tell you which way
[18:03] the market's going to go. All this helps
[18:05] is saying that there's a major tail risk
[18:07] that's out there and I helped you
[18:08] quantify it with this that is going to
[18:11] impact the real job market. And if you
[18:13] have a parent or a grandparent that
[18:15] relies in any way on home health care
[18:17] aid, you better figure this out right
[18:19] now and figure out where all the money
[18:22] is coming, what staffing agency it's
[18:23] coming through, because that could all
[18:25] of a sudden just disappear depending on
[18:27] what state you live in.
[18:29] >> It all ties back to consumption. It all
[18:32] ties back to real growth in the economy.
[18:34] I want to hit one more part on
[18:35] employment before we start getting into
[18:37] the cost side of this and talking about
[18:38] inflation. I want to talk about the wage
[18:41] ledger because I think this is another
[18:43] fantastic data series.
[18:45] >> Yeah. Um, so this one, if you actually
[18:48] go to the wage le ledger, I'd love if
[18:50] you do that because I am the most proud
[18:53] of this one. Not because it is the most
[18:55] um involved, the most complicated. In
[18:58] fact, there is a spreadsheet that lives
[19:01] out on the BLS website. It's called
[19:02] OEWS, occupation, employment, wage
[19:05] statistics. Everybody should look at it
[19:07] if you care about, you know, how much
[19:09] people make. You know, I'm sure that
[19:11] there's some investing thesis for
[19:13] knowing that kind of stuff and how
[19:14] that's changed over time. The problem is
[19:16] is the spreadsheet is like largely
[19:18] unusable in Excel. It crashes. It's hard
[19:21] to filter. And so all we did here was
[19:24] take that and put it into an interactive
[19:26] data visualization. So you can um you
[19:29] know, sort through that and sift through
[19:30] it and learn from it. And um not only
[19:33] that, but the main reason I'm proud
[19:35] about it is that you'll see the author
[19:36] of this is is a is a a gentleman by the
[19:39] name of Jonathan Pickkins. He is a
[19:41] rising senior in high school. And so I
[19:45] am uh working with him. He's one of my
[19:47] three data uh storytelling fellows that
[19:49] we have at data for the people. And this
[19:52] is kind of a work in progress project.
[19:54] He's doing a really big project, which
[19:57] I'm sure after we publish this, you're
[19:58] going to want to talk about it again
[19:59] because it's evaluating the changing
[20:01] cost benefit of a four-year college
[20:03] degree over time versus a trade career,
[20:05] which is very complex. But, um, as he's
[20:09] building the databases and getting to
[20:10] learn all these databases, he's coming
[20:13] up with these interactive tools that on
[20:15] their own are very, very useful. And so,
[20:17] this wage ledger is, I thought, was
[20:20] fantastic that he came up with. You can
[20:22] basically go through 830 different jobs
[20:24] that are shown. Sort them from high to
[20:26] low on the annual median. What will come
[20:29] up is the number one paying in the in
[20:31] the country. By the way, this is only W2
[20:33] employees. So, you know, you're not
[20:34] going to find Elon Musk on here, any
[20:36] people that own businesses. Um,
[20:38] pediatric surgeons make a median salary
[20:40] of $559,000.
[20:42] There are 1,190 of them. But then what
[20:45] you can actually do is that sort that by
[20:47] employment. Boom. What comes to the top?
[20:50] home health and personal care aids
[20:52] 4,35,810
[20:55] making an hourly median of $1721
[20:58] $35,800
[21:00] a year. The paid range, you can even
[21:03] hover over that pay range, you can see
[21:05] that it is very tight. the 90th
[21:07] percentile makes $45,000 a year. Which,
[21:10] by the way, if you go to another one of
[21:11] our data visualizations, you will find
[21:14] in some of the higher cost areas that
[21:16] still doesn't cover the cost of poverty
[21:18] for to to raise a family of four. So, we
[21:20] are building basically all of our job
[21:23] growth and betting it all on people that
[21:27] are largely women, largely immigrants,
[21:29] largely living at or below the poverty
[21:32] line to support a family of four. And
[21:34] this is where we come back to the Fed to
[21:36] make it full circle. The Fed is report.
[21:39] They're not telling us about any of
[21:40] this. So, do they know it? Probably. But
[21:44] this is a political game, right? Why are
[21:46] they not telling us that the quality of
[21:48] the job growth is coming all from home,
[21:50] healthcare, and personal care aids that
[21:52] make $35,000 a year? Like, these aren't
[21:55] jobs that are creating tremendous
[21:56] disposable income for average Americans.
[22:01] That is an important data point. I would
[22:03] think we would want to have if we are
[22:04] claiming it is a strong or robust job
[22:07] market, but we're not getting any of
[22:08] that information. And shame on, sorry,
[22:11] I'm gonna say it. Shame on the people
[22:13] that are interviewing them and
[22:15] interviewing the whatever the guy's name
[22:16] at the chair of the Fed, this new dude.
[22:18] Shame on them for not asking these
[22:20] questions. I mean, I I I really can't
[22:22] believe that the people like that are
[22:24] invited to the room don't have access to
[22:27] any of this data. the people at
[22:29] Bloomberg, the people at Barrens,
[22:30] wherever they are, whoever's coming
[22:32] there. They don't have data analysts
[22:33] that can do this. I just had a high
[22:35] schooler do this. So, don't tell me you
[22:37] don't have the the chops to do this. All
[22:39] right? I would love to be in that room
[22:41] and ask some questions. By the way, I
[22:43] would love to see what the answers are
[22:44] because then we'd actually get to figure
[22:46] out, does he really know this or does he
[22:48] not even know what we're seeing here?
[22:50] Because this is the level of detail that
[22:51] I think investors really need to know.
[22:53] But right now, it's just a game of like
[22:57] your investors that are listening to
[22:58] this are going to say, "Oh, wow. Now I
[23:00] know this." But like, you know, Ben Hunt
[23:04] says, if this is knowledge that only
[23:06] investors on on I'm sorry, that that on
[23:09] uh on this podcast have, but they know
[23:11] that not everyone else knows this, then
[23:13] then the game of investing is to really
[23:15] figure out, well, what does the
[23:16] consensus know? And if the consensus
[23:18] doesn't know about this, does it even
[23:20] make sense for me to act on it? because
[23:23] the real economy is going to suffer. We
[23:24] we know this from the data, right? All
[23:27] the data says that you can triangulate
[23:29] any which way. But if no one ever
[23:31] figures it out or it takes two years,
[23:33] what are your clients going to say? Like
[23:35] you're going to sit on the sidelines
[23:36] waiting for that. It's it's a very hard
[23:37] job this job that you guys have. Thank
[23:39] thankfully I don't have to do it
[23:40] anymore. I just have to diagnose all
[23:42] this and you figure out what to do with
[23:43] it.
[23:44] >> You you found a good you found a good
[23:46] place and if I get war on speed dial uh
[23:48] you're going to be one of the first ones
[23:49] I get to know. I want to take us to
[23:51] inflation yet next I want to go to the
[23:53] cost side and the reason I want to go
[23:56] there is because this is another data
[23:58] series that's enormous enormously clunky
[24:01] enormously
[24:04] funny in the way that we even talk about
[24:06] it or measure it. So I'll ask the same
[24:08] question that I did about labor to lead
[24:10] off with inflation as we understand it
[24:13] at the top top level
[24:15] up down sideways where is inflation
[24:18] moving right now up for sure.
[24:21] >> That one's an easy one to tell you. Like
[24:22] you don't even have to do all the work
[24:25] that you're doing on the job side to be
[24:27] like well wait a second it's this the
[24:29] not in labor force the participation
[24:31] rate like all these things that people
[24:32] don't talk about. You got to drill a
[24:34] little bit for that. inflation is just
[24:35] like just look at the data. I mean like
[24:37] we know that it's up but we h we
[24:40] published about two years ago a data
[24:42] visualization on Breek banrete.com it's
[24:45] free it's the first one we ever
[24:46] published on CPI we followed up with a
[24:48] PCE one and all it does is it takes the
[24:52] underlying kind of items about 180
[24:55] mutually exclusive items and it will
[24:57] size them and show you like this is the
[24:59] the impact that this is having on
[25:01] inflation
[25:03] >> just like you did with CES and CPS just
[25:05] take a second and talk about CPI, PCE,
[25:09] how you guys broke that down to show it
[25:11] because this is people need this
[25:13] reminder.
[25:14] >> Yeah. Okay. So, so um CPI is you know
[25:19] surveyed measured by the BLS. It is
[25:21] supposed to be the consumer's experience
[25:24] of inflation and so the weights are
[25:27] different from PCE because that is like
[25:29] the broader economy's experience of
[25:30] inflation. So um you know each of them
[25:34] are have different weights. They have
[25:36] different ways that they measure things.
[25:38] So when you drill into PCE several of
[25:42] the items will actually be taken from
[25:44] CPI and they'll be the same and then
[25:46] others will not. They'll be taken from
[25:48] PPI you know and so it's this mishmash
[25:52] of them. But the the best example I can
[25:55] give you with PCE and given that it is
[25:58] like the holistic view of the economy's
[26:01] experience of inflation is it has like a
[26:03] much higher weight for health care
[26:06] because you have employers you have the
[26:09] federal government Medicaid like you
[26:11] have a lot of um non-consumer payers
[26:15] mostly non-consumer payers within
[26:16] healthcare and so you'll see a much
[26:18] larger weight there and then you see a
[26:20] much smaller weight on shelter Um so you
[26:25] know PCE is the Fed says it's what they
[26:28] look at over CPI. Um the Fed also says
[26:32] they look at core right. I have been on
[26:35] record and written multiple times about
[26:37] how core is part of my French
[26:41] because core was defined and you can do
[26:43] the research on your own by um coming
[26:46] out of the 1973 oil shock or whatever
[26:49] and then it was having impacts on food
[26:51] prices and the the current Fed chair at
[26:53] that time was like well this is noisy
[26:54] and so let's strip it out and so they
[26:56] stripped it out and like we haven't
[26:57] revisited that ever since and I wrote a
[27:00] piece um
[27:02] I can't remember exactly where this But
[27:04] trust me, I wrote a piece that um
[27:06] actually looked at the volatility of
[27:08] these categories and it's like, okay,
[27:10] gasoline is really volatile. Makes sense
[27:12] to strip that out if you are really
[27:14] looking to smooth this out. Still a
[27:16] really important, you know, variable for
[27:19] the consumer. So, we probably do care
[27:21] about that a lot. But food is not
[27:23] variable. Like, it's not nearly as
[27:25] volatile as healthcare. And so, it's
[27:29] pretty arbitrary the way that core is
[27:30] measured right now. If you were just
[27:32] doing it based on volatility, you would
[27:34] strip out all of healthare and you would
[27:35] include all the groceries. And then if
[27:37] you were really building a benchmark
[27:39] that you wanted to measure the pain and
[27:41] the suffering of the average American,
[27:44] you would measure gasoline and and and
[27:46] groceries first and foremost because
[27:48] that's that's what we feel and that's
[27:50] what we experience, you know. Um the
[27:53] surveys in it themselves have all sorts
[27:56] of assumptions baked in. Um CPI is
[28:00] heavily influenced by shelter and the
[28:04] the number one item by weight is
[28:07] something called OEER owner's equivalent
[28:09] rent of residences. It itself is a
[28:12] proxy. It's a fabricated surveyed number
[28:15] that is trying to come up with kind of
[28:17] an estimate of what rent would be and
[28:20] the changes in rental from month to
[28:21] month for people that own their homes.
[28:23] So they literally just place a call to
[28:26] you. I don't know if anyone who's
[28:27] listening has ever got this call. I
[28:28] haven't. They place a call and they're
[28:30] like, "Hey, what would you rent your
[28:31] house for right now if you could?"
[28:33] Theoretically, hypothetically, what
[28:35] would you do? I just go to Zillow and be
[28:36] like, "I don't know. I mean, like, what
[28:37] does Zillow say?" And so, like then
[28:39] that's what they I'm assuming that's
[28:40] what people do. And then that is 30%.
[28:42] That's about 26 to 27% of all of CPI is
[28:46] just on that. And so, why did CPI go up
[28:49] so much in 2022? It's just because
[28:52] shelter was going up so much. This one
[28:53] this one item was. And why is it like
[28:56] staying muted now? Because shelter is
[28:58] staying muted now. But when you look
[29:00] underneath that, and we published a
[29:01] report on Bank Creek, I think something
[29:03] like 42 to 45% of all items out of the
[29:08] 180 have breached one standard deviation
[29:11] over their historical mean. So they've
[29:13] moved into this is anomalous, you know,
[29:16] and you also have like a huge amount
[29:18] that are above two standard deviations.
[29:19] And so you can see this real easily on
[29:21] that tool. just hover over them and you
[29:23] can just all of a sudden see a bunch of
[29:24] stuff like spiking gardening, lawn care
[29:27] services, beef, coffee, like random
[29:29] stuff like hair care, I don't know, like
[29:32] it's weird stuff that that is just kind
[29:35] of all going kind of parabolic and
[29:37] you're we did that report on Ban Creek
[29:39] and I thought that was a really good one
[29:40] just because it's like no one's talking
[29:43] about any of this stuff. the weights are
[29:44] so small that you really don't care
[29:46] about your laundry care services that
[29:48] are spiking, but it's like all of a
[29:50] sudden you put all of them together and
[29:52] you're like, none of these things
[29:53] actually are related and yet they're all
[29:56] spiking. That doesn't feel so good. And
[29:59] that's free. You can see that very
[30:01] easily in our tool.
[30:03] So, one of the places that you've been
[30:05] drilling in that I think is the most
[30:07] valuable and certainly this came up when
[30:09] we were recording that last call a week
[30:10] or so ago was looking at oil and you've
[30:14] got some charts on the petroleum
[30:16] inventory seasonality that I think are
[30:18] fascinating especially where we are with
[30:19] the straight of horror moves and our on
[30:21] again offagain war and the 321 crack
[30:23] spreads. I think these are really really
[30:26] useful to understand right now even for
[30:28] the people who aren't oil investors or
[30:29] aren't tied to that market. Everyone
[30:32] investor now
[30:33] >> it flows through to everything.
[30:35] >> Everyone needs to become an oil investor
[30:37] to be an equity investor. That's what I
[30:40] think. So let's start now.
[30:42] >> All right, let's start now. Petroleum
[30:43] inventory seasonality. What's going on
[30:45] there? This comes straight out of your
[30:46] background. We should call this out,
[30:48] too. This is
[30:48] >> This does. And let me give you like um a
[30:51] bit of context and background. So I have
[30:54] for years I'm I'm a chemical engineer. I
[30:57] worked at at Exxon Mobile. I modeled
[30:59] refineries. I know this right?
[31:03] Well, I I tried to forget it. I can't.
[31:05] It's been tattooed in my brain how how
[31:07] crude oil gets processed through a
[31:09] refinery. Um, I have been trying to come
[31:12] up with a way I I like speaking in terms
[31:14] of analogies, metaphors, whatever to
[31:16] explain
[31:17] oil to people that they'll understand.
[31:20] Like I don't know like at at the level
[31:23] of my 11-year-old where he gets it right
[31:25] because I think people think that oil is
[31:28] one thing. Crude oil. Oh, we have lots
[31:31] of crude oil in this country. We're
[31:32] producing record crude oil. We'd have no
[31:35] problem.
[31:36] People who will go unnamed are saying
[31:38] that and people probably are just
[31:41] believing that. Yet, let's look at the
[31:44] evidence. We're exporting records
[31:47] amounts of oil, still importing a lot of
[31:49] oil, and you're like, and then we're
[31:52] drawing down our strategic petroleum
[31:54] reserves to the lowest level in like 45
[31:56] years, like almost on record. We're
[31:58] getting close to that. Um, you know, the
[32:00] oil inventories when we look at those
[32:02] charts, which we'll talk about, are just
[32:04] all crashing. And you're like, why would
[32:07] you export your oil
[32:10] if we're out of oil? [laughter]
[32:13] One would think that like if we had any
[32:15] strategy whatsoever and rather than the
[32:18] marketer is us basically just selling us
[32:19] to the highest bidder which that could
[32:21] be it is like nobody nobody's at the
[32:23] wheel right now and so of course like if
[32:26] I have oil and I'm a company and I own
[32:28] it and I can get a higher price by
[32:31] selling it on the market and I'm not
[32:33] forced to send it to a refinery in you
[32:37] know Pennsylvania
[32:39] to basically say like well we want to
[32:41] bring gas prices down in the us, then
[32:43] that's what I'm going to do. Like, if no
[32:44] one told me to do it. And so, that's one
[32:46] part of it. But the other part of it is
[32:48] that oil is not oil.
[32:52] And I and I actually have um by the time
[32:54] this come out, hopefully it's out, but
[32:55] but I should have an op-ed coming out um
[32:57] in a major national publication. So,
[33:01] that will be posted on Data for the
[33:02] People.
[33:03] >> And as soon as it's out, we'll get a
[33:05] link to it. Look in the description. If
[33:06] it's out when this is out, it's in the
[33:08] description. So, go ahead. Keep going.
[33:09] So, so I have I have an analogy in there
[33:11] that I finally think can work. And so we
[33:14] need to tell everybody about this
[33:16] analogy. Oil, think of oil as fruit or
[33:20] even better, a fruit salad. So everybody
[33:23] knows that if you order a fruit salad,
[33:25] it's going to have cantaloupe and it's
[33:26] going to have honeydew and it's gonna
[33:27] have blueberries, it's have
[33:28] strawberries, it's have apples, it's
[33:30] have a mix of all the different types of
[33:31] fruit. Oil is not blueberries. Oil is
[33:35] not one type of fruit. It is a blend of
[33:39] all of the different fright types of
[33:41] fruits which are really hydrocarbons.
[33:44] So there's some fruit which creates
[33:46] propane and there's some fruit which
[33:48] creates gasoline, the ones with six
[33:50] hydrocarbons or the with six carbons or
[33:53] eight carbons or something like that.
[33:55] There's some fruit that creates diesel,
[33:58] some fruit that creates jet fuel,
[33:59] asphalt, petrochemicals, all that kind
[34:02] of stuff. And so every type of crude oil
[34:06] is different. The type that you drill in
[34:09] the Middle East is that's where most of
[34:12] the oil has come from over the history
[34:14] of our world. And so most of the
[34:17] refineries which we haven't built a new
[34:18] refinery here in like probably my
[34:20] lifetime. Most of the refineries were
[34:22] designed to produce that kind of stuff
[34:23] which is heavier. It has more of the
[34:25] diesel in it. It is more of the jet fuel
[34:27] in it. It is more of like the the he the
[34:29] heating oil. More of the heavy stuff. So
[34:32] refineries develop technology called
[34:34] fluid catalytic crackers and cokers to
[34:36] take the heavy crap in the oil billions
[34:39] of dollars of technology and crack that
[34:42] and morph it chemically and physically
[34:44] into gasoline. Now, the stuff that we're
[34:47] drilling here, which is very recent,
[34:50] right? This happened in like the 20 the
[34:52] 2005, 2006, the fracking revolution, all
[34:55] that kind of stuff, the shale oil, all
[34:57] that. This is very light oil, lots of
[35:00] the gasoline molecules in it, not a lot
[35:03] of the other stuff in it, right? Well,
[35:05] now if you take that and you put it into
[35:07] a refiner, there are actual physical
[35:09] limitations of like what that refinery
[35:11] can do. In the entire refinery, the
[35:14] economics are managed to like maximize
[35:16] the economics, right? You so you want to
[35:19] maximize the yields. There are specs on
[35:21] every product. I mean, it's very very
[35:23] complicated. And I built refiner I
[35:25] refinery models to to optimize all of
[35:27] this based on what type of crude. And I
[35:29] can tell you that a refinery on the Gulf
[35:31] Coast, you would never send you'd never
[35:34] be like, "Oh, I'm going to take all the
[35:35] per the oil from the Peran basin, which
[35:37] is literally right there, and send it
[35:38] all here." because all of a sudden the
[35:40] yields of crap that comes out the other
[35:42] end, it's all broken. It's not it's not
[35:44] what the refiner wants to maximize their
[35:46] profitability. And so what happens when
[35:49] you have the wrong type of oil matched
[35:50] to the wrong refinery? The crack spreads
[35:53] rise. And so the crack spreads is the
[35:57] market telling you this is three barrels
[35:59] of it's a proxy for refining margins. So
[36:02] it's three barrels of oil equals two
[36:04] barrels of gasoline and one barrel of
[36:06] diesel. All three of them are separately
[36:08] traded products on the market. They all
[36:10] are just like stocks, right? You know,
[36:12] nobody is fixing these prices. Nobody's
[36:14] controlling this. The refiners get get
[36:17] what they get from these prices. And
[36:19] what's happening is when oil gets
[36:21] mismatched to the refineries, the
[36:23] economics of the refineries are bad.
[36:25] Now, if you have what's called a
[36:27] hydrokming refinery, which is like
[36:30] actually one of the cheapest type of
[36:31] refineries that wants to process like
[36:33] light sweet crude that we produce, man,
[36:35] you're you're a cash machine right now.
[36:37] You could just run that thing flat out,
[36:40] make tons of money, $60 a barrel in in
[36:43] crackspread, which is f four to five
[36:45] times your historical profit margin.
[36:47] You're making four to 500% profit.
[36:49] That's why refining stocks are probably
[36:50] up. I don't I don't check them, but my
[36:52] guess is they are. But if you're like
[36:54] that Gulf Coast refinery, the big, the
[36:57] bad refineries, the Exxon refineries,
[36:58] the BP, the Shell, that's not the kind
[37:01] of oil you want. And so what I wrote in
[37:06] this oped is we close the straight, we
[37:10] open the straight. When you close the
[37:12] straight, all the flows across the
[37:16] country, the world get disrupted. The
[37:18] wrong oil goes to the wrong place and
[37:21] all the economics are screwed up. This
[37:23] is COVID. When we closed the straight,
[37:26] we created COVID for oil markets, right?
[37:29] When we had COVID, remember what it did
[37:31] to all the supply chains for like two,
[37:33] three, four years, but we were back like
[37:36] wearing masks in public. I mean, there
[37:38] wasn't any immediate near-term threat
[37:41] after we realized we needed to max mask
[37:42] and we had vaccines, but it still took
[37:45] years for supply chains to recover.
[37:48] that like you don't even need to know
[37:49] about refineries. You just need to know
[37:52] that we just shut down the bottleneck of
[37:55] the the key choke point. We shut down
[37:57] Atlanta Hartsfield if you think about
[38:00] this from like the the air traffic
[38:02] network for like two months. I mean,
[38:05] don't tell me that not every single
[38:07] flight around this country will be
[38:09] affected eventually. Maybe not on day
[38:11] one, but it takes a long time and the
[38:14] air traffic network is underelling it.
[38:15] That's actually a lot easier to reset
[38:18] because you just don't fly overnight.
[38:20] Whereas, I mean, think about all the
[38:21] ships that are sailing around the Cape
[38:23] the sailing all these like extended
[38:25] voyages to not pass through the straight
[38:27] and everything. It'll take months for
[38:29] those to actually get back to where they
[38:30] need to be and then we just keep
[38:32] shutting it down and then opening and
[38:34] shutting it down and the insurance
[38:35] premiums are high. Like arguably this
[38:38] may never go back to where it is. Um
[38:41] especially if Iran is able to formalize
[38:43] the PGSC, they start charging, you know,
[38:45] fees on this, the the capacity is like
[38:48] permanently lower because we clearly
[38:51] don't want that to happen. All bets are
[38:53] off. Like we just created COVID for the
[38:56] oil markets from a supply chain
[38:58] standpoint. We're seeing it in the
[39:00] inventory visualization that I put
[39:02] together, which by the way, this is yet
[39:04] another example of the government not
[39:06] giving you the data that you really
[39:07] should have. They tell you what was the
[39:10] percent change versus the last 5 years.
[39:13] And then you're like, "Oh, diesel
[39:15] inventories are down 10% versus the last
[39:16] 5 years." You're like, "10% isn't the
[39:18] scariest number ever." [laughter]
[39:20] And then you're like, "Well, wait a
[39:21] second. What in 2022 we had the Russia
[39:23] Ukraine thing and then like everything
[39:25] was going crazy back then. Oil was like
[39:27] at 100 plus. You know, gasoline prices
[39:29] were at $6 average. That's one of the
[39:32] five years I'm comparing it against the
[39:33] worst year on record. Why wouldn't we
[39:36] compare this against all 40 plus years
[39:38] of history? I don't it doesn't make any
[39:40] sense to me and that's why I did it. So,
[39:41] so you can actually go and look at the
[39:43] diesel inventory chart, the gasoline,
[39:45] the strategic petroleum reserve, crude
[39:47] oil, and you can look at against all
[39:49] history and you can click on and off of
[39:51] different decades. So, what if you don't
[39:53] want to compare it to the 90s or the
[39:54] 2000s? Just click those off and then it
[39:56] will take those off the charts and then
[39:58] you can actually see how bad things
[40:00] really are. And it's scary. It's scary
[40:02] bad. Like if inventories matter at all,
[40:06] this is COVID happening in real time and
[40:10] the investing public couldn't care less.
[40:13] Like it's it's like COVID without the
[40:15] transmissibility until it hits and then
[40:18] like my worst case which we're heading
[40:20] towards. And I think a lot of oil
[40:22] analysts are talking about this is like
[40:23] one day you'll show up at the gas
[40:24] station, you just won't be there. Or
[40:27] what happens when you know El Nino hits?
[40:30] What happens when hurricane season comes
[40:32] through and one of them happens to take
[40:34] out a refinery in Louisiana? I mean,
[40:36] like, we're basically just like
[40:38] sacrificing all of our risk mitigation
[40:42] for the sake of whatever. I mean,
[40:44] short-term profiteering from the
[40:46] administration, from the government,
[40:48] from investors, like we're pulling
[40:49] forward all of the gains. So, go party
[40:53] while you can. But like I mean like I
[40:55] look at this and as as a knowledgeable
[40:58] not investor but like concerned citizen
[41:01] that happens to know how this all works
[41:02] and I'm like I I better prepare, you
[41:05] know, I better prepare my family for
[41:07] this. I I better just get prepared for
[41:09] times to get very difficult. Maybe we
[41:12] end up threading that needle somehow. I
[41:14] don't know. I can't tell you what's
[41:16] going to happen. I can just give you a
[41:18] probabilistic assessment of it. And it
[41:21] is not pretty right now. tie,
[41:23] >> don't take my word for it. Look at the
[41:25] charts.
[41:26] >> Tie that back to CPI
[41:29] to PC. The way that most people are
[41:32] looking at this because I think what
[41:33] you're highlighting is that's especially
[41:36] important is the tail risk this
[41:37] represents if there's overlapping
[41:39] events. So, this helps put
[41:42] applied pressure that's not going away
[41:45] onto the inflation numbers across the
[41:46] board.
[41:47] >> Yeah. On top of that though, how much is
[41:50] this showing up in CPI and PCE now
[41:53] versus in that tail scenario? How much
[41:55] more does it move those numbers where
[41:57] the Fed actually looks at this and says
[41:58] we have an inflation problem?
[42:00] >> Yeah. So,
[42:02] oh man, how do I say this kind of like
[42:05] somewhat politely? Um, so let me be
[42:08] honest with you. Like I haven't really
[42:10] looked at PC in a while. So, um, but PC
[42:14] is the same as CPI just with different
[42:16] weights. You know, go look at it
[42:17] yourself. Ask Claude, they'll they'll
[42:19] give you all the weights, you know. So,
[42:21] like one weights will be higher, one
[42:22] weight will be lower. It doesn't matter.
[42:24] But CPI, I can tell you I did a study
[42:27] with this at Ban Creek. I can predict
[42:30] almost exactly to with like 99%
[42:33] certainty when the AAA retail gasoline
[42:36] price gets finalized at the end of every
[42:38] month, which if you have a Bloomberg
[42:39] license, you have access to AAA data.
[42:43] Um, if you don't, it's very hard to
[42:45] actually find that series. It should be
[42:47] in the public domain, but it's tough to
[42:48] get. So, if you have that, average the
[42:50] entire month, compare it versus the p
[42:53] past month or compare it those those
[42:55] retail gasoline prices versus the last
[42:57] year. And then the gasoline component of
[42:59] CPI will come in almost spot on on that
[43:02] every single month. That's all they use.
[43:04] And so, I've done the correlation. It's
[43:06] like a 0.99% R or 0.99 R squared. It
[43:10] that that's just what it is. So, I can
[43:12] tell you the gasoline component, we know
[43:14] that. So, I mean, honestly, it's July
[43:18] 10th right now, so we know exactly what
[43:20] the gasoline component is going to be. I
[43:21] haven't looked at it yet. I should have
[43:22] gone going into this podcast, but um
[43:25] maybe I'll send it to you and you can
[43:26] kind of post in the show notes. Um we
[43:28] know exactly what that's going to be
[43:30] going into next week's CPI release.
[43:34] Everything else
[43:36] is just based on the methodology and the
[43:38] surveys and the error and the models and
[43:40] everything of the BLS. And so I couldn't
[43:44] tell you that like laundry services or
[43:46] gardening services were going to be
[43:47] spiking, but yet they are like I mean I
[43:49] think
[43:50] >> but that means that this is the this is
[43:51] the the moving data point that basically
[43:55] drags it doesn't drag the others with
[43:56] it. But if something is the most
[43:58] volatile component
[43:59] >> and it's this
[44:01] >> then this is where you want to
[44:02] understand where that surprise risk
[44:03] comes from in the whole data series.
[44:06] >> Well and I can tell you that that's not
[44:07] the part. So gasoline is is the you know
[44:09] that that individually is the large the
[44:12] single largest mover because it's so
[44:13] volatile and it's a large weight but
[44:16] diesel is more important because that
[44:18] feeds into almost all the other ones. So
[44:20] think about gardening and lawn care
[44:22] services diesel. [laughter]
[44:25] Think about um you know all of your
[44:27] grocery store food diesel. Why is that
[44:30] the case? I mean I also happen to work
[44:31] at a railroad and so fuel search charge
[44:33] is a really big thing for the trucking
[44:35] industry. all runs on diesel for the
[44:37] railroad industry. All runs on diesel.
[44:39] The fuel searchcharge gets passed
[44:41] through to the consumers. Now, I'm not
[44:44] an expert on this, but I'm sure people
[44:46] are on this call. I find it very
[44:48] interesting that you're hearing the
[44:50] Targets and the Walmarts of the world
[44:52] talking about reducing their prices in
[44:54] the face of clearly what could be
[44:57] dramatically rising costs for them
[44:58] because of like they're having to eat
[45:00] fuel search charge as it, you know,
[45:02] migrates through. And this only gets
[45:05] worse and worse and worse if we have
[45:06] this on again offagain thing and if the
[45:08] diesel inventories keep dropping. I mean
[45:10] you saw like on the day where um this is
[45:14] telling on the day where like we went
[45:16] back to war last week
[45:19] um and everyone started bombing again.
[45:22] That same day, the EIA inventories were
[45:24] released and crude oil, commercial crude
[45:28] oil inventories actually went up because
[45:30] the refinery utilization dropped down,
[45:32] but gasoline dropped by like 2 million
[45:33] barrels and diesel dropped by like 3
[45:35] million barrels. Diesel prices were up
[45:37] 13% that day. Like this is the main
[45:39] choke point. People are most worried
[45:41] about diesel right now. And that's a
[45:44] that's very very unsettling for CPI
[45:46] because that could be like permanent
[45:48] long- ter not permanent but it could be
[45:50] long-term inflation that works itself
[45:52] into CPI because all that kind of stuff
[45:54] has to get kind of passed through um
[45:56] over time unless Walmart and Target and
[46:00] Costco and all of them are willing to
[46:01] basically step in front of this bus or
[46:03] this train pun intended and say we're
[46:07] willing
[46:08] >> yeah we're willing to kill our margins
[46:10] to to basically protect the consumer.
[46:13] Which to me, if they're willing to do
[46:15] that, that means not like the top 1%,
[46:18] they're immune largely until the
[46:21] really hits the fan. But that means the
[46:23] rest of us are really, really suffering.
[46:26] Cuz I mean, why would you, as you know,
[46:30] someone that cared about quarterly
[46:31] reports, as one of these large
[46:33] retailers, you're looking at rising
[46:35] costs pretty obviously as fuel search
[46:37] charge passes through. Why would you
[46:39] ever cut cost right now unless you were
[46:41] really really really concerned about
[46:42] volume at the lowcost retailers? So
[46:45] that's a concerning data point. Don't
[46:48] take my word for it because I don't read
[46:49] these these transcripts. I just saw, you
[46:52] know, news in passing. So go out
[46:54] validate that for yourself. If they
[46:55] really are cutting that, that is
[46:57] something that that I would really want
[46:58] to understand. But my own like I shop at
[47:01] Walmart every week. Again, we're a
[47:04] nonprofit or [laughter] so I have to
[47:06] shop at Walmart. Um, and I can tell like
[47:09] they they are cutting prices. Like at
[47:10] least in my like anecdotally, I'm I'm
[47:12] shocked. I'm really shocked that they're
[47:14] doing it given the inflationary
[47:16] pressures that they're probably just
[47:19] subsidizing at this point in time. It's
[47:20] interesting. Really, really interesting
[47:22] what's going on.
[47:23] >> It's fascinating, especially when we get
[47:24] into corporate earnings or we get into
[47:27] this and this is a broader question that
[47:28] keeps coming up on excess returns is
[47:30] this idea of how corporations are
[47:32] thinking of it. If you're spending on
[47:33] capex and AI and other places, you're
[47:35] cutting somewhere else. Different
[47:37] companies are reallocating right now. I
[47:39] want to land us here because this is now
[47:41] the combination of all this data, at
[47:44] least in my mind.
[47:45] >> And this is with financial planning hat
[47:47] on. This is when I go through yet
[47:49] another review of taxes and spending and
[47:52] budgeting in an exercise and we go,
[47:54] here's another person whose grocery and
[47:56] basic income expenses, whatever. It
[47:59] didn't go up 3% or 5% this year.
[48:01] >> Mhm. It went up 50 or 60%.
[48:04] >> Yeah.
[48:04] >> Seen it across the board. Luckily, a lot
[48:07] of the people we care about are at the
[48:09] upper arm of the K, not the lower leg of
[48:11] the K. Part of why bridging this makes
[48:14] so much sense. I want to talk about the
[48:16] single income stress test.
[48:18] >> The procarity line. Shout out Adam
[48:19] Butler, Mike Green, the people have done
[48:21] work on this, you as well. Let's talk
[48:23] about the single income stress test
[48:25] because I think
[48:26] >> if this economy is running on
[48:27] consumption, this is why this important
[48:30] this data is so important in
[48:31] understanding what the knock-on effects
[48:33] to everything else are.
[48:35] >> Yeah.
[48:35] >> And this also goes back to the home
[48:37] healthcare aid thing. You know, it's
[48:39] what I was really interested in. And I
[48:41] took that same OEWS database and this is
[48:43] one of the first visualizations I put
[48:44] together and published on data for the
[48:46] people is I was really interested in
[48:48] connecting um the wage that the median
[48:54] wage for one worker. So we're not
[48:56] talking like now there's other data in
[48:58] the visualization we first started
[49:00] talking about where you can look at um
[49:02] people that have two jobs and that's at
[49:05] an all-time high which this
[49:07] visualization you just asked me about
[49:08] will explain why. So, if you want to
[49:13] just work one job, like this, this to me
[49:15] is where like this whole like
[49:18] America's greatness kind of went
[49:20] sideways and how it was kind of like
[49:22] weaponized. Like I I think back to like
[49:25] the unions and like I wasn't alive
[49:27] during this period of time, but like
[49:30] my understanding of that this period of
[49:32] time was like you could actually have an
[49:36] middle class to upper middle class
[49:37] lifestyle, buy your own home, put your
[49:40] kids through college on one income.
[49:44] And it didn't have to be like I'm the
[49:46] president of an investment bank income.
[49:48] It could be like, you know, I'm I'm like
[49:50] a senior person working at a factory and
[49:53] I can do that. You know, that is a great
[49:56] thing. If you can do that, it's great. I
[49:58] mean, look, maybe your wife or maybe
[50:00] it's the wife that works and but I mean,
[50:03] I can tell you I've been in that
[50:04] situation where like my wife only worked
[50:07] when I was not bringing an income when
[50:08] I'm starting dating for the people and I
[50:10] my kids benefit a lot from that. like
[50:13] having a parent home, having a parent
[50:15] present for them to take care of them
[50:17] rather than just putting them in daycare
[50:19] like you know putting them in front of a
[50:21] tablet like there are real
[50:24] um call it you know qualitative benefits
[50:28] that that um you get from that. So, I
[50:31] look back and I'm like, "All right,
[50:32] well, what if you wanted to do that now?
[50:36] What if you wanted to earn a median
[50:37] income in the city in which you live,
[50:40] Dayton, Ohio, let's say, or I don't
[50:43] know, say Philadelphia is close to you.
[50:45] I don't know. [laughter]
[50:46] So, you want to it's an upgrade.
[50:47] >> You want to Yeah. You want to own or you
[50:49] want to earn a single income. How far
[50:52] above the poverty line to raise a family
[50:55] of four are you?" It's a model, right?
[50:57] Again, all models are wrong. Some are
[51:00] useful. I find this one really useful
[51:02] because it's simulation. It's not saying
[51:04] this is the number of people because
[51:07] most families have two earners now,
[51:09] right? But what if you didn't want that?
[51:12] Like you wanted those old days of where
[51:14] you did. So the answer if you actually
[51:16] look through all of them. One, it shows
[51:19] you the gradient. So the more green you
[51:22] are, the higher above the um poverty
[51:25] line you are. And then I also give you a
[51:27] little kind of um it's called a
[51:30] parameter entry box. So you can actually
[51:32] say, "Whoops, I have $5,000 of surprise
[51:34] expense. Whoops, I have $10,000. I had a
[51:37] health care bill. I had this." Like, you
[51:39] can just plug that in and say, "Well,
[51:42] take the the the poverty line and add
[51:44] that amount of money to it. Now, how far
[51:46] above?" So, like, how much breathing
[51:48] room do I have? And what you find is if
[51:50] you put $15,000 in there, the whole
[51:54] country turns red.
[51:56] So it doesn't matter where you live. The
[51:59] the whole country the median income in
[52:03] those cities using the 2024 data which
[52:05] is what I was using at that time they
[52:07] only have $15,000 of breathing room and
[52:09] that's pre-tax too. So it's probably
[52:11] even less than that before they are
[52:13] living under the poverty line to support
[52:15] a family of four. And so that's why they
[52:17] have to work two jobs. We can start
[52:19] understanding more about the lived
[52:20] experience of people in the median. Now
[52:24] go and switch that from median to 25th
[52:26] percentile or even to 10th percentile
[52:28] everything is blood red. I mean to
[52:32] actually like this is the thing that's
[52:34] beautiful about data for the people is
[52:35] like when I did that like
[52:38] I mean I I felt it like when I switched
[52:41] it and I'm like wait a second 10% of all
[52:43] the people 10% this isn't like a small
[52:46] percentage of all the people living in
[52:48] this city make under like $16,000 a
[52:51] year. 17,000 20,000.
[52:55] It's It's just a It's like a hole in my
[52:58] heart almost that it's like, well, what
[53:01] if that were me? Like I mean, I can't
[53:03] even envision like I mean like my wife
[53:06] works a good government job and like we
[53:08] really were struggling like to kind of
[53:10] over the months of not having no income
[53:12] until I got this fellowship um
[53:15] gratefully to Oshanasy Ventures. um we
[53:18] were really really you know budgeting
[53:20] aggressively and cutting back on things
[53:22] and just to make things meet on her very
[53:24] good salary. Um and yet there are people
[53:27] that are making $20,000 a year, $30,000
[53:30] a year. Like I can't even like fathom
[53:33] how that must feel. But I can start to I
[53:36] can start to when I look at this data
[53:37] and I really try to get myself out of my
[53:39] own, you know, privilege problems and
[53:42] start to see through the lens of other
[53:44] people. And that that's what I'm really
[53:47] look there's a lot of investing
[53:48] takeaways. So many if you still believe
[53:52] that the economy has anything to do with
[53:53] the market. Big qualifier big asterisk
[53:56] there. Um but I mean
[53:59] >> take us take us here because I think
[54:01] this is a great place for us to put the
[54:03] bow in this conversation.
[54:04] >> Yeah.
[54:05] >> The work with data for the people.
[54:07] >> Yeah.
[54:08] >> About to be officially a nonprofit.
[54:10] Congratulations on making that move.
[54:12] Another reason check out the site. you
[54:14] can support work like this because there
[54:16] are direct market implications of
[54:19] understanding these data sets but I also
[54:22] know there's a deep personal connection
[54:23] that you feel I feel this too where you
[54:26] think about you think about your kids
[54:27] you think about your kids' kids and you
[54:29] say this is not a sustainable framework
[54:31] to build the next several generations on
[54:34] because we're not using the data that's
[54:36] at our disposal.
[54:38] >> Yeah. Yeah.
[54:39] >> Talk to me about the mission for the for
[54:40] the company going forward.
[54:43] >> Yeah. So, um, yeah, thanks for the shout
[54:46] out. We I literally am just submitting
[54:48] the right now simply because it cost I
[54:52] was in an LLC structure with a DBA doing
[54:55] business as for Data for the People. Um,
[54:58] I now, you know, I'm getting I'm filing
[55:01] for an Ohio nonprofit corporation. I'm
[55:04] hoping that will be done next week. um
[55:06] transferring the name over or giving
[55:09] rights to to use the name and then um
[55:12] yeah, then we'll be going through the
[55:14] form 1023 process, you know, getting the
[55:16] five the 501c3 status and and um yeah,
[55:20] and I I will keep people updated on how
[55:22] that goes because this is not a Substack
[55:25] model. There is no payw wall. There
[55:27] never will be a payw wall in our work. I
[55:29] want everybody to have access to this
[55:32] and I don't want to have to keep
[55:33] pestering you about, you know, paying
[55:35] money for this. I refuse to do that. But
[55:38] ultimately, our work will be supported
[55:40] by those that that see value in it and
[55:42] can afford to do it. Like if you can
[55:44] afford $10 a month, it's totally up to
[55:47] you. I don't want to know your
[55:48] financials, but like that goes a long
[55:50] way to us. you know, if I even if I had
[55:53] like a hundred people that could afford
[55:54] $10 a month, I mean, it's a meaningful
[55:56] amount of money for for us and and I
[55:59] understand that it's prohibitive right
[56:00] now because I'm not a 51c3, but I will
[56:02] be. So, right now, if you look at the
[56:05] website, um, we're publishing at a at a
[56:09] frenetic pace. [laughter] Thanks.
[56:12] >> It's a good word for it.
[56:14] >> The magic of AI. Um, you know, I have
[56:18] figured out how to play nice with AI and
[56:21] how to use it to do things that I never
[56:23] could have envisioned doing. Like the
[56:25] the data visualization that we talked
[56:27] about to start, impossible to do without
[56:31] AI. Not with my skill set. I'm not smart
[56:33] enough to do it. Um, and that's because
[56:36] when you actually go into the raw
[56:38] database that lives underneath the
[56:39] unemployment data, there are at least 30
[56:42] different dimensions with intersections
[56:44] of every single dimension. And many of
[56:47] those are blank. And so when I get the
[56:49] intersection of sex and age there, that
[56:52] will be populated. But then if I try to
[56:54] intersect that again with another
[56:56] dimension, say race, oop, all of a
[56:58] sudden it's blank. I spent days and days
[57:02] trying to wrap my head around it until
[57:03] like, you know, my head was spinning and
[57:06] I gave up. And so I I I focused a lot on
[57:08] nativity because I think there's amazing
[57:10] stories about immigrants versus native
[57:12] born. Look at the data visualization
[57:14] I've written about this at length. But
[57:16] that's about all the scraping I was able
[57:18] to do on my own. And then I, you know,
[57:20] we have all this wonderful access to
[57:22] anthropics fable for another couple
[57:24] weeks or another week. And I basically
[57:26] just went to Fable and I'm like, do this
[57:29] all for me. And it did, you know, and of
[57:32] course it takes tremendous amount of
[57:34] editorial oversight to make sure it's
[57:36] doing right, doing it right, and testing
[57:37] the code and everything, which
[57:39] fortunately I'm skilled to and I know
[57:41] how to do this. Um, but my gosh, the
[57:45] amount of crank turning that it did and
[57:47] the amount of like testing and
[57:49] connections and then even specifying
[57:51] that I only want you to present these
[57:54] dimensions when they're available and
[57:56] like come be smart enough to know to
[57:58] default to the age group of 16 plus when
[58:01] you're looking at the combination of
[58:02] race and sex. And it it does it just
[58:04] figured it all out. And um so that kind
[58:08] of stuff like has allowed me to take
[58:11] what would have taken me about two weeks
[58:12] and do it in two hours now. Um that's
[58:15] why I'm able to publish every single day
[58:16] a new original data research study. um
[58:20] yesterday or this morning's piece like I
[58:22] actually for the first time went down
[58:24] into the census's micro data which if
[58:27] you have heard about that don't go
[58:28] anywhere near it until unless you're
[58:30] using AI because it is you know it
[58:34] you'll just um be committed to a looney
[58:38] bin [laughter]
[58:39] um impossible to decipher what's going
[58:41] on but if you want the intersection of
[58:43] every single dimension micro data that's
[58:46] where you get it and I was able to
[58:47] unearth some amazing ing findings that
[58:50] nobody had ever looked at that America
[58:52] is far older than we thought. You know,
[58:55] there was a latest um there was a a
[58:58] change in the way that the models were
[58:59] measuring the age of people and we lost
[59:02] about two and a half million prime age
[59:04] workers.
[59:05] So, that's a big deal, you know, it's a
[59:08] big deal for social security for all
[59:09] these things. I was able to figure that
[59:10] using the app. So, long story short,
[59:13] like we're doing a ton of data
[59:15] journalism right now, but I archive
[59:17] everything I do, every chat I have, and
[59:20] everything that we're doing is being
[59:23] used to train an LLM
[59:26] on, and it's not just me. There are
[59:27] other people that are doing this.
[59:29] There's Jonathan, there's other data
[59:30] fellows. like all of our interactions is
[59:32] being used to train a special
[59:34] purposebuilt
[59:36] LLM to understand
[59:40] how to triage problem solving within
[59:43] data storytelling and data analysis and
[59:45] data visualization. So how do how do you
[59:48] basically create a digital twin of us?
[59:50] Then on the other side, shout out to Am
[59:53] Amanda Cinton who is my founding data um
[59:57] data architect. She is brilliant and
[60:00] she's building the entire architecture
[60:02] for how do we rescue data sources? How
[60:04] do we publish them on GitHub in a way
[60:06] that everybody can use for free? And
[60:08] then how do we integrate that into an AI
[60:11] intake agent that anyone can go to? And
[60:16] there are many reasons why AI I call it
[60:18] the um the everything store AI which is
[60:21] what all like Claude is and Gemini and
[60:23] everything. Many reasons why it can't do
[60:25] this. But for people that and I really
[60:27] think local journalists, community
[60:28] advocates, just interested people that
[60:31] have problems that they want to solve.
[60:32] It could be investors too. Um, if you
[60:36] really want a research assistant that is
[60:39] trained on the art of working with data
[60:42] and helping you kind of problem solve on
[60:44] how to get to the scope of something
[60:46] that actually is achievable to solve and
[60:49] then can it create charts and data
[60:50] visualizations and a story and and all
[60:53] the narrative for then you to edit. Like
[60:55] I don't think this should be an AI only
[60:57] tool. There always needs to be the human
[60:59] editorial oversight because we are the
[61:01] source of creativity and storytelling,
[61:03] right? But I think we can get to doing
[61:06] 80 to 90% of the work for you with an AI
[61:08] bot. Um, and so that is all being built
[61:12] out. So right now we have Amanda working
[61:15] on one side building the infrastructure
[61:17] for this platform and me feverishly
[61:21] creating as much content as I possibly
[61:23] can do solving every question or
[61:26] answering every question that I've ever
[61:28] had by using AI in this responsible way
[61:31] and then taking myself out of being the
[61:33] crank turner to being the call it the
[61:37] idea generator. I'm always generating
[61:38] the idea. I'm almost always creating the
[61:42] stream of consciousness
[61:44] piece, the the writing on it. Like I do
[61:46] the data work with with Claude with AI.
[61:49] I'm like, here's the story that I see.
[61:52] And then I am spending the vast majority
[61:54] of my time in an editorial role
[61:56] oversight. Claude is really bad at
[61:59] sometimes it wants to go too far with
[62:01] the claims, sometimes it doesn't go far
[62:03] enough. Like sometimes it will make like
[62:05] one little statement that you're like
[62:06] you're going to torpedo the entire
[62:08] credibility of the entire piece based on
[62:10] that statement. So you have to be very
[62:12] careful on an editorial basis which is
[62:14] the stuff that like I'm really learning
[62:16] looking to build that into the LLM. So
[62:19] it doesn't go anywhere near that which
[62:21] if you just go create something right
[62:23] now it will do that
[62:25] >> and so real.
[62:27] >> Yeah. So like we're we're just learning
[62:28] we're learning a lot about what it's
[62:30] really good at and where it is good. Oh
[62:33] my gosh, it is like it is like universe
[62:36] changing good and then where it's not it
[62:39] can basically destroy all the work that
[62:41] it's good at. Like so so it's like how
[62:43] do you build that infrastructure that
[62:45] takes the best of it and then really
[62:48] filters it. So if like if you go and you
[62:50] ask a question that is like clearly
[62:52] profit seeeking, we're going to direct
[62:55] you to go to Gemini. Like we're not
[62:57] going to that's not what we're for. The
[63:00] problem ultimately, and I'm not saying
[63:01] it's not for investors, but it's for
[63:03] people that care about building as
[63:06] robust and as strong of an America as
[63:09] possible for all of us. Um, investing
[63:12] can overlap with that.
[63:14] Sometimes it doesn't. And so, we'll know
[63:17] how to fair it out the questions and
[63:19] which way you're going with it. And
[63:21] then, you know, we'll either choose to
[63:23] help you or we'll be like, you know
[63:25] what, this is not what our free service
[63:28] is for.
[63:28] >> [laughter]
[63:28] >> So that's what we're looking to build.
[63:32] >> Eric, insightful as always. One more
[63:34] time, just tell the people where to find
[63:35] it. Tell them where they can bug you on
[63:36] the internet.
[63:38] >> Yeah. So the best place to find me on my
[63:42] website, data forthepeople.com,
[63:45] number four, not FO. Um, we're moving up
[63:49] in all the search rankings, so you could
[63:50] just search for data for the people.
[63:52] We'll come up. We should be, you know,
[63:53] number one on that list. So you could do
[63:55] that if you forget. Um, email me. It's
[63:59] ericdatforthepeople.com.
[64:02] Um, and u, sign up for the distribution
[64:05] list. I'd love to hear feedback. I'm
[64:07] getting a lot more engagement,
[64:09] especially from um, this crowd. I love
[64:12] it. You know, when people tell me good
[64:14] or bad, you know, be critical with what
[64:16] I'm writing. I love that. Um, I want to
[64:18] get engaged on the debates that are
[64:20] coming out of this data. I put a lot of
[64:22] my own bias into my interpretation of
[64:25] what I'm seeing. I will not allow any of
[64:27] my bias into how the data is worked. All
[64:31] the methodology is free. You're free to
[64:32] recreate your tools and you're free to
[64:34] come up with completely different
[64:35] conclusions than me. I believe I mean
[64:38] our vision ultimately is to create a
[64:40] shared basis of reality for America and
[64:44] for the world, you know, and data can do
[64:46] that if we choose to use it for good.
[64:49] But that's not to say that we can't have
[64:50] polar opposite viewpoints. We are
[64:52] allowed to have that. That's what makes
[64:55] America beautiful. But we can't have our
[64:58] own sets of data. We just can't get by
[65:01] with that because then we actually can
[65:03] never see each other's perspectives. So
[65:06] if we can be any part of building that
[65:07] foundation and if you can be any part
[65:09] with supporting us, especially once
[65:11] we're a 501c3, just following our work,
[65:14] telling people about it, right? I'm not
[65:17] on social media that much, although
[65:18] we're trying to automate the entire
[65:20] process to shove out a whole bunch of
[65:21] things. So, you'll see more posts coming
[65:22] from Data for the People. But, um,
[65:25] please, if you value our work, let
[65:27] people know. Um, you know, spread the
[65:30] word. It's all organic. It's all word of
[65:32] mouth. I'm really relying on you to do
[65:34] that.
[65:35] >> Spread the word. Data forthepeople.com.
[65:37] Eric, thanks so much for joining me
[65:39] today.
[65:40] >> Yeah, thanks, Matt.
[65:41] >> Excess returns in all the places. You
[65:44] know what to do. Like, comment,
[65:45] subscribe, send Eric an email, all the
[65:47] things below, and we're out.
[65:48] >> Thank you for tuning in to this episode.
[65:50] If you found this discussion interesting
[65:52] and valuable, please subscribe on your
[65:54] favorite audio platform or on YouTube.
[65:56] You can also follow all the podcasts in
[65:58] the Excess Returns Network at excess
[66:00] returnspod.com. [music]
[66:01] If you have any feedback or questions,
[66:03] you can contact us at excess
[66:05] returnspod@gmail.com.
[66:07] No information [music] on this podcast
[66:09] should be construed as investment
[66:10] advice. Securities discussed in the
[66:13] podcast [music] may be holdings of the
[66:14] firms of the hosts or their clients.