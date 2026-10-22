---
title: "Apple WebKit Blocks Identity Resolution (iOS 27): Impact on Public Adtech"
created: 2026-10-20
updated: 2026-10-20
type: concept
tags: [risk, catalyst, ecommerce, comparison, speculation]
sources: ["AdExchanger: Apple Publishes Its Plan To Wipe Out Web Tracking (October 2026), quoting the WebKit blog post 'Blocking Identity Resolution Infrastructure' by John Wilander, Charlie Wolfe and Matthew Finkel"]
confidence: medium
contested: false
---

# Apple WebKit Blocks Identity Resolution (iOS 27): Impact on Public Adtech

**Source:** an AdExchanger article (October 2026) on Apple's WebKit post "Blocking Identity Resolution Infrastructure" by engineers John Wilander, Charlie Wolfe and Matthew Finkel. The company assessments below are this page's analysis. Current share prices, revenue mix by device and Apple's actual blocklist were not checked.

## What Apple announced

* **Scope:** Starting with iOS 27, WebKit blocks third-party **identity-resolution** vendors at the domain level. Data such as email addresses is blocked from reaching their servers. Apple: "The blocking is done on the domain level, meaning they can't just change the structure of the network request to work around the protection."
* **First-party scoping doesn't exempt vendors.** Apple says identity graphs limited to a single company's data still count: "the central identity resolver is a third party and it holds cross-site, cross-device and cross-party data about the user and can perform matching and targeting functions in the capacity of a clearinghouse." Vendors that are not themselves first-party data owners (login providers, newsletter services) fall under the block.
* **Rationale:** blocking cross-site cookies (Safari, 2020) is "not enough... because the tracking industry has not stopped trying to track users on the web." "Users deserve to not be tracked, not across websites and not covertly through fingerprinting, unless they explicitly opt in to it."
* **Named early targets** (per AdExchanger): The Trade Desk, LiveRamp, Experian's Audigent, ID5, Permutive. Some spun up new domains not yet on the blocklist. The Trade Desk created `TTDCDN.org` as a backup to its core `adsrvr.org` domain. A source familiar with Permutive's strategy called this a temporary Band-Aid.

## Why it matters

This goes further than the 2020 cookie block or App Tracking Transparency (ATT, the 2021 iOS app-tracking opt-in). It targets the industry's main post-cookie strategy: email-based IDs, publisher login-data networks and identity graphs, including the move to graphs limited to one client's data.

The main limit: Apple controls only what the device sends. **Data moving server-to-server, outside the browser, is not affected.** The hit therefore lands on businesses whose identity products need code running on iOS web pages.

## Exposure by company (this page's ranking)

| Company | Exposure | Why | Mitigation |
|---|---|---|---|
| **LiveRamp (RAMP)** | Highest | The article's central example: RampID, its publisher login-data network (Authenticated Traffic Solution, ATS), and its graphs limited to one client's data are all within Apple's stated target | Offline CRM matching and server-side clean rooms are unaffected; the loss is the browser-side identity layer meant to replace cookies |
| **The Trade Desk (TTD)** | High | Named target; its email-based identity standard (UID2) on iOS web and the `adsrvr.org` domain (tracking pixels, conversions, attribution) at risk; backup domains are a temporary fix | Connected TV (outside WebKit), retail data, server-side signals; lost iOS-web spend may move to CTV within TTD rather than leave |
| **Criteo (CRTO)** | High | Retargeting already weak on Safari; email-based IDs and code on retailer sites exposed | Retail-media data handled server-side; commerce-media partnerships |
| **Zeta Global (ZETA)** | High (inference; not named) | Its model is the email-based identity graph Apple describes | Email, CRM and server-side data assets |
| **PubMatic (PUBM)** | Medium-high | Ad sellers lose value when Safari users can't be identified; its CTV business is small | Building CTV and app supply |
| **Magnite (MGNI)** | Medium | Same web exposure as PubMatic | Larger CTV business cushions it |
| **DoubleVerify / Integral Ad Science (DV / IAS)** | Medium, uncertain | Verification code runs on third-party domains; unclear whether Apple treats measurement as tracking | Demand for independent measurement as attribution weakens |
| **AppLovin (APP)** | Low-medium | In-app ads not affected, but the website tracking pixel behind its e-commerce push could lose measurement on iOS Safari; see [[app-2-equity-report]] | Server-side conversion data |
| **Experian, Viant, Unity, Digital Turbine** | Low | Audigent is immaterial to Experian; the others are mostly app or CTV inventory | n/a |

## Relative winners

* **Retail media (Amazon, Walmart):** first-party purchase data matched server-side. Budgets shift toward closed systems.
* **Meta and Alphabet:** mostly beneficiaries on their own apps and logged-in properties. Their web tags that send hashed emails are the kind of identity matching Apple describes, so expect some iOS-web measurement loss, cushioned by server-side conversion APIs (Meta's Conversions API, Google's enhanced conversions).
* **Apple:** strengthens its privacy positioning and its own ads and attribution tools.
* **Chrome and Android audiences:** Chrome kept third-party cookies, so the price gap between Safari and Chrome users widens and spend shifts toward Chrome, Android and walled gardens.

## Size and timing

1. **Coverage:** every iOS browser runs on WebKit, so Chrome on iPhone is likely covered, except in the EU where other browser engines are allowed. A macOS Safari rollout would add exposure.
2. **Ramp:** the impact grows with iOS 27 adoption, historically a majority of active iPhones within a few months of release.
3. **Precedent:** ATT cost Meta roughly $10B in 2022, and adtech multiples compressed for about two years before modeling recovered part of the signal. This time the open-web identity vendors with the least first-party data (LiveRamp, Criteo, Zeta) bear more of it.
4. **Regulatory pushback:** Apple blocking rival ad infrastructure while running its own ads invites antitrust complaints. EU authorities have previously challenged ATT, which could slow enforcement there. Apple has generally held its position in the U.S.

## Watch list

* iOS-specific reach and match-rate commentary in TTD, RAMP, CRTO and PUBM earnings calls.
* Progress moving identity matching server-side, and whether backup domains survive Apple's blocklist updates.
* Whether Apple extends the block to measurement and verification domains, or to macOS Safari.
* Any EU antitrust action against the policy.

## Bottom line

LiveRamp, The Trade Desk, Criteo and Zeta carry the most risk, then PubMatic. Retail media and the walled gardens gain share. How much each company loses depends on how much of its identity matching it can move off the device.

**Related:** [[app-2-equity-report]] (AppLovin's web-pixel exposure), [[shop-2-equity-report]] (merchant first-party data and commerce media), [[saaspocalypse-dispersion-2026-04-09]] (software multiple dispersion when a business model is threatened).
