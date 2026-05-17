# Taiwan & US Property Tax Research Plan: Inherited Property Sale

## Project Background
- **Property Location:** New Taipei City, Taiwan
- **Inheritance Date:** May 2022 (Mother deceased)
- **Target Sale Date:** Summer 2026
- **Objective:** Determine the applicable tax regimes, cost basis, tax brackets, and total liability for both Taiwan and the US.

---

## Risk Register
*These unknowns gate other calculations — resolve before proceeding to Phase 2.*

| Risk | Consequence | Mitigation |
|---|---|---|
| Original purchase date: approximate month **April 2012**, exact day TBD | Pre-Jan 2016 confirmed → Old System (LVIT + building income) applies. Exact day needed for precise LVIT calculation and combined holding period verification. | Confirm exact day via title deed search (地政事務所) |
| No 2022 FMV appraisal exists | IRS may challenge stepped-up basis | Commission retroactive qualified appraisal now |
| 戶籍 not registered at subject property | Self-use HSTT exemption (NT$4M deduction, 10% rate) unavailable — **affects property sales tax only** | Likely a closed issue: even with active 戶籍, it must be registered at *this property* for 6+ years of combined holding period; physical residency requirement also unmet |
| Taiwan tax non-resident (<183 days/year in TW) | Buyer withholds tax at closing; flat withholding rate applies to building gain if Old System — **affects income tax and withholding mechanism** | Treat as confirmed given US-based living; plan for withholding at closing |
| NIIT applies | Extra 3.8% on US side — not offset by Foreign Tax Credit | Model this scenario regardless |
| Old System applies + high US income year | Taiwan building gain stacked on top of all other income, taxed at 40%+ | Model both regimes with your expected 2026 income |
| Registration date later than date of death | Holding period clock starts later than expected | Confirm actual 登記日 from title records |

**Key Terms for Online Research:**

| Chinese | Pinyin | English |
|---|---|---|
| 地政事務所 | Dìzhèng Shìwùsuǒ | Land Administration Office |
| 戶籍 | Hùjí | Household Registration |
| 登記日 | Dēngjì Rì | Date of Ownership Transfer Registration |

---

## Phase 1: Data Gathering & Document Verification
*Goal: Establish the legal and financial foundation for tax calculations.*

- [ ] **Confirm Original Acquisition Date:**
    - Verify when the property was first purchased by the decedent (mother).
    - **Threshold:** Pre-Jan 1, 2016 vs. Post-Jan 1, 2016 determines which tax regime applies.
    - Source: title deed search at the local 地政事務所 (Land Administration Office).
    - **Legal sources:**
        - [Department of Land Administration (地政司), MOI](https://www.land.moi.gov.tw/enhtml/index) — central authority governing Taiwan's land registration system; explains how to access title records
        - [Regulations of the Land Registration](https://www.land.moi.gov.tw/enhtml/enlawdet/29?elid=113) — the formal MOI regulation governing registration procedures, required documents, and timelines
        - [New Taipei City Land Administration Department](https://eng.land.ntpc.gov.tw/) — the local office for New Taipei City property records (English interface)
    - **中文法源：**
        - [全國地政電子謄本系統（內政部地政司）](https://ep.land.nat.gov.tw/) — 線上申請全國土地及建物所有權狀謄本，可查詢原始登記資料（含所有權移轉日期及取得原因）
        - [我的E政府——各類地籍謄本申請及資料閱覽](https://www.gov.tw/News3_Content.aspx?n=2&s=381320) — 政府入口網說明地籍謄本申請流程及各類謄本差異
        - [內政部地政司——土地登記](https://www.land.moi.gov.tw/chhtml/content/64?mcid=3490) — 地政司土地登記總覽，涵蓋繼承登記相關規定及申辦說明

- [ ] **Confirm Actual Registration Date (登記日):**
    - The HSTT holding period clock starts at the date of ownership transfer *registration*, not the date of death.
    - If registration was delayed past May 2022, your holding period is shorter than expected — confirm the exact 登記日 from title records.
    - **Legal sources:**
        - [MOF — Heirs Can Now Register Inherited Property Under Collective Joint-Ownership](https://www.mof.gov.tw/eng/singlehtml/f48d641f159a4866b1d31c0916fbcc71?cntId=27ddb5dd2413423b895ffd3a3341dfb4) — MOF notice confirming that the inheritance transfer registration date governs holding period and that the 完稅證明書 is required before registration
        - [National Taxation Bureau of Kaohsiung — Holding Period Starts at Completion of Registration](https://www.ntbk.gov.tw/eng/singlehtml/c19e2cba4e6f4d43ba7b15040c8dbe50?cntId=e478e2564ad74cd697a9289141c2e8f5) — bureau guidance explicitly stating "The acquisition date of house and land for individuals shall be the completion date of the ownership transfer registration"
        - [Regulations of the Land Registration](https://www.land.moi.gov.tw/enhtml/enlawdet/29?elid=113) — legal basis for registration timing rules
    - **中文法源：**
        - [財政部——出售因繼承取得之房地，應依新制申報房地合一稅嗎？](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=6d27fbf173364c3aa0d3e9f0d25e57ca) — 財政部確認：以**被繼承人取得日**判斷適用新/舊制；取得日以**完成所有權移轉登記之日**為準
        - [財政部稅務入口網——房屋、土地取得日之認定（問答2911）](https://www.etax.nat.gov.tw/etwmain/tax-info/understanding/tax-q-and-a/national/profit-seeking-enterprise-income-tax/house-tax-and-land-tax-consolidation/nDRr1Gm) — 明確說明取得日原則以「所有權移轉登記完竣日」計算
        - [財政部臺北國稅局——個人交易連續繼承房地之稅制判斷及持有期間計算](https://www.ntbt.gov.tw/singlehtml/41ae3594197f4f69b47753ce08188516?cntId=cdeb372790044547ad6a8749ae975e4a) — 詳細說明繼承「接計持有期間」（tack-on rule）計算方式
        - [桃園市政府地政局——繼承登記](https://land.tycg.gov.tw/News_Content.aspx?n=3946&s=688348) — 繼承登記申辦流程及應備文件

- [ ] **Verify 戶籍 (Household Registration) Status — affects HSTT self-use exemption (property sales tax only):**
    - Having a Taiwan national ID card does *not* automatically mean active 戶籍 — the ID is issued at registration but the registration itself can be cancelled later. However, if you never formally emigrated or deregistered, your 戶籍 likely still exists at its last recorded address.
    - To confirm: request a 戶籍謄本 (household registration extract) from any 戶政事務所 or via the Taiwan e-government portal.
    - **Practical conclusion for this sale:** Even if your 戶籍 is active, the self-use exemption requires it to be registered *at this specific property* for at least 6 of the combined holding years — with no rental or business use and evidence of actual physical occupancy. Given that you have lived in the US for most of the year, this requirement is almost certainly unmet. The self-use exemption can be treated as **unavailable** for planning purposes.
    - 戶籍 status does **not** affect the standard HSTT tax rates (15%/20%/35%/45%) — those apply regardless.
    - **Legal sources:**
        - [Department of Household Registration (戶政司), MOI](https://www.ris.gov.tw/app/en) — central government authority for 戶籍 status, 戶籍謄本 applications, and registration/deregistration procedures
        - [Household Registration Act (戶籍法)](https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=D0030006) — the statute governing registration, cancellation (廢止登記), and address changes
        - [Taiwan Government Portal — Residency & Household Registration Services](https://www.taiwan.gov.tw/content5.php?p=33&c=55) — English-language guide to household registration services, including how to request extracts
        - [NTBT — 房地合一 (HSTT) English Overview](https://www.ntbt.gov.tw/english/multiplehtml/cd61d91304fc4fb194571fea1d82ba35) — official NTBT English page covering HSTT rules including the self-use exemption eligibility criteria
    - **中文法源：**
        - [內政部戶政司——現戶全戶紙本戶籍謄本申請](https://www.ris.gov.tw/app/portal/481) — 戶政司官方說明紙本戶籍謄本申請方式、應備文件及各戶政事務所受理流程
        - [內政部戶政司——現戶全戶電子戶籍謄本申辦作業](https://www.ris.gov.tw/app/portal/16) — 免費線上申請電子戶籍謄本，24小時均可申辦（需自然人憑證）
        - [內政部戶政司——電子戶籍謄本申請及驗證程序說明](https://www.ris.gov.tw/app/portal/288) — 說明電子謄本之法律效力及驗證方式
        - [我的E政府——電子戶籍謄本申辦及驗證](https://www.gov.tw/News_Content_2_371532) — 政府入口網整合說明
    - **⚠ Partially unsourced:** The assertion that "having a Taiwan national ID card does not automatically mean active 戶籍" is a practical interpretation of how cancellation (廢止登記) works under the Household Registration Act — it does not appear verbatim on any government page. Confirm this framing directly with the local 戶政事務所 or a Taiwan CPA before acting on it.

- [ ] **Determine Taiwan Tax Residency Status — affects income tax rates and withholding mechanism:**
    - Taiwan tax residency is determined separately from 戶籍, based solely on physical presence: **≥183 days in Taiwan in the calendar year = resident; <183 days = non-resident.**
    - Given that you live in the US for most of the year, you are almost certainly a **Taiwan tax non-resident** in the year of sale. Treat this as confirmed unless you expect an unusually extended Taiwan stay in 2026.
    - Consequence for **property sales tax (HSTT, New System):** The HSTT rate schedule (15%/20%/35%/45%) is the same for residents and non-residents. However, non-residents are subject to **withholding at the source by the buyer** at closing rather than self-filing. See Phase 4.
    - Consequence for **income tax (Old System only):** If the Old System applies, non-residents are taxed on building gain at a **flat 20% withholding rate** rather than progressive rates — which may actually be favorable compared to stacking the gain on top of other income.
    - **Legal sources:**
        - [MOF — Aliens Staying Over 183 Days Can File Taxes Online (183-day rule)](https://www.mof.gov.tw/eng/singlehtml/f48d641f159a4866b1d31c0916fbcc71?cntId=b8ae2181a22146fdaccfe0aaff391b39) — MOF confirmation of the resident/non-resident 183-day threshold
        - [NTBT — Resident Status (≥183 days)](https://www.ntbt.gov.tw/English/htmlList/bfc158abe6fe4e43b301e491263e7fee) — National Taxation Bureau of Taipei page on resident tax treatment
        - [NTBT — Computing Period of Stay](https://www.ntbt.gov.tw/English/multiplehtml/06922971ae7e48d18d2902dfa6ebfcea) — explains how accumulated days of physical presence are counted (including multiple entries/exits)
        - [NTBT — Non-Resident Status (90–183 days)](https://www.ntbt.gov.tw/English/htmlList/d8fa239122dc4d14989884c1ded43df8) — non-resident income tax treatment
    - **中文法源：**
        - [財政部稅務入口網——「非中華民國境內居住之個人」扣繳率規定（十七）](https://www.etax.nat.gov.tw/etwmain/alien-tax-service/alien-individual-income-tax/vV8Z3o9) — 財政部列明非居住者各類所得扣繳率；佣金、利息、租金、執行業務報酬均為20%（薪資18%，為例外）
        - [財政部稅務入口網——非居住者扣繳率規定（問答）](https://www.etax.nat.gov.tw/etwmain/alien-tax-service/alien-tax-faq/KK9Y76o) — 問答形式補充說明各所得類別扣繳規定
        - [財政部稅務入口網——外僑所得稅與居留期間的關係](https://www.etax.nat.gov.tw/etwmain/alien-tax-service/alien-individual-income-tax/15r2N1n) — 183天計算基準及居住者/非居住者稅務差異說明
        - [財政部臺北國稅局——居住者（居留天數≧183天）中文版](https://www.ntbt.gov.tw/htmlList/00c79f3c83c249f6a0c280f638c868c0) — 居住者申報及適用稅率說明
        - [財政部臺北國稅局——非居住者適用稅率（90天＜居留天數＜183天）](https://www.ntbt.gov.tw/multiplehtml/df93772580dd46189977c6f37ffd66de) — 非居住者各所得項目適用稅率彙整
    - **⚠ Partially unsourced:** The specific claim that non-residents pay a **flat 20% withholding rate on building gain** under the Old System requires further verification. The Chinese-language sources above confirm 20% withholding for non-residents on commissions, interest, rent, and professional fees — but real property building gain falls under **財產交易所得** (property transaction income), a distinct income category not explicitly listed in those pages. The applicable rate for 財產交易所得 paid to a non-resident requires direct verification in the Income Tax Act (所得稅法 §88 and the accompanying withholding rate schedule) or with a Taiwan CPA before relying on the 20% figure.

- [ ] **Retrieve Inheritance Tax Records:**
    - Confirm whether Taiwan inheritance tax (遺產稅) was filed and paid in 2022.
    - The inheritance tax clearance certificate (遺產稅免稅證明書 or 完稅證明書) is typically required before property transfer can be registered.
    - The government-assessed values used in that filing are the same values establishing your Taiwan cost basis — obtain a copy.
    - **Legal sources:**
        - [MOF — E-tax Document Service Portal: Online Reissue of Estate Tax Certificates](https://www.mof.gov.tw/Eng/Detail/Index?nodeid=319&pid=80678) — the MOF portal for electronically re-issuing 完稅證明書 and 免稅證明書; legally equivalent to paper certificates under the Electronic Signatures Act
        - [MOF — Estate Tax Law Content](https://law-out.mof.gov.tw/EngLawContent.aspx?lan=E&id=20472&KW=Estate+Tax) — legal text of Taiwan's Estate and Gift Tax Act
        - [eTax Portal, Ministry of Finance](https://www.etax.nat.gov.tw/etwmain/en) — central e-filing and tax document portal for all MOF tax types
    - **中文法源：**
        - [財政部稅務入口網——3705 如何申領遺產稅證明書？](https://www.etax.nat.gov.tw/etwmain/tax-info/understanding/tax-q-and-a/national/estate-tax/certification/QN716Kb) — 詳細說明完稅證明書及免稅證明書之申請流程、所需文件及核發時限
        - [財政部中區國稅局——遺產繼承流程（步驟三：申報遺產稅）](https://www.ntbca.gov.tw/singlehtml/73956170c8c84f6caf14e77161f938ab?cntId=30e3cea4885c4f89a8f33a9d3b0ad44f) — 完整遺產稅申報流程說明，含使用政府評定現值之規定
        - [財政部中區國稅局——遺產繼承流程（步驟四：取得遺產稅證明）](https://www.ntbca.gov.tw/singlehtml/73956170c8c84f6caf14e77161f938ab?cntId=e0e1f999b51b4d67be1a5e7be204aa5d) — 完稅/免稅證明書核發程序；確認此證明書為辦理產權移轉登記之先決條件
        - [財政部——申報遺產稅所需文件](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=fbb7eecfd3c74135b11b14b0310a1aa5) — 財政部說明申報遺產稅應備及得免附之文件
    - **⚠ Partially resolved:** A Chinese-language MOF page (see Bullet 8 中文法源第一筆) directly confirms that HSTT cost basis for inherited property = 繼承時房屋評定現值及公告土地現值（CPI調整後）— the same government-published values used in the 遺產稅 filing. The linkage holds because both filings draw from identical publicly available government data tables. However, the mechanism is that the national tax authority sources those values from 公告現值 records (not from the 遺產稅 filing documents themselves); confirm with your Taiwan CPA which documents are accepted as proof of cost basis when filing HSTT.

- [ ] **Retrieve 2022 Government-Assessed Values:**
    - Obtain the "Assessed Current Land Value" (公告現值) and "House Value" (房屋評定現值) from May 2022.
    - These serve as the **Taiwan cost basis** under the New System.
    - **Legal sources:**
        - [MOI Land Administration — 公告現值 / 公告地價 National Online Lookup](https://www.land.moi.gov.tw/chhtml/landvalue/42) — national system for querying historical assessed land values by parcel; supports historical year lookups
        - [Land Price Inquiry Network (地政資訊網路服務e點通)](https://pqt.ttt.nat.gov.tw/landprice.jsp) — a second national-level query system covering 公告現值 and 公告地價 by administrative district, section, and parcel number
        - [New Taipei City Land Administration Bureau — Land Price Section](https://www.land.ntpc.gov.tw/cl.aspx?n=20) — New Taipei City-specific land price records and historical data
    - **中文法源：**
        - [全國公告土地現值查詢系統（內政部地政司）](https://www.land.moi.gov.tw/chhtml/landvalue/42) — 地政司官方歷年公告土地現值查詢，可依縣市/鄉鎮市區/地段地號查詢特定年度現值
        - [公告地價歷年調整表（內政部地政司）](https://www.land.moi.gov.tw/chhtml/content/65?mcid=2942&qitem=1) — 全國各年度公告地價調整統計資料
        - [新北不動產愛連網——公告地價與現值查詢](https://i.land.ntpc.gov.tw/iland/index.php/2019-01-11-09-49-36/article-category-blog) — 新北市政府整合不動產資訊平台，含公告現值及歷史交易資料
        - [新北市政府稅捐稽徵處——如何查詢房屋現值？](https://www.tax.ntpc.gov.tw/cp-2158-1225-7f578-1.html) — **直接解答房屋評定現值查詢方式**：明確說明房屋現值屬稅務保密資料（稅捐稽徵法§33），須向稅捐稽徵處申請「房屋稅籍證明書」以取得；可線上、郵寄或臨櫃申辦
        - [新北市政府稅捐稽徵處——線上申辦服務入口](https://www.tax.ntpc.gov.tw/np-7-1.html) — 包含房屋稅籍證明書線上申辦管道
    - **⚠ Resolved (房屋評定現值):** The New Taipei City 稅捐稽徵處 FAQ (中文法源第四筆) directly confirms that 房屋現值 is confidential tax data under the Tax Collection Law and must be obtained by requesting a **房屋稅籍證明書** — available online, by mail, or in person. There is no public online self-service lookup for this value.

- [ ] **Obtain 2022 Fair Market Value (FMV):**
    - Source a professional appraisal or historical market data for the property's FMV in May 2022.
    - This serves as the **US cost basis** (stepped-up basis under IRC §1014).
    - **Risk:** If no appraisal was done at the time of inheritance, establishing defensible FMV retroactively is harder and may require a qualified appraisal — the IRS can challenge an undocumented step-up. Address this sooner rather than later.
    - **Legal sources (US only — no Taiwan government source applies to this bullet):**
        - [IRS Publication 551 — Basis of Assets](https://www.irs.gov/publications/p551) — the authoritative IRS publication on the stepped-up basis rule; the "Inherited Property" section confirms FMV at date of death as the basis for property received from a decedent
        - [IRS FAQ — Gifts & Inheritances](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances) — IRS confirmation that the basis of inherited property is the FMV on the date of the decedent's death
        - [IRS Publication 561 — Determining the Value of Donated Property](https://www.irs.gov/publications/p561) — IRS guidance on qualified appraisal standards; while primarily for charitable donations, it contains the IRS's qualified appraiser requirements and FMV methodology that applies to establishing inherited property values
    - **中文法源：** 「公平市場價值（Fair Market Value / FMV）」與「qualified appraisal」係純美國稅法概念（IRC §1014），台灣政府並無直接對應之法規。惟台灣政府之**實價登錄**資料庫（內政部不動產交易實價查詢服務網）為查詢同棟或同區域歷史成交行情之重要資料來源，可作為推估2022年5月公平市場價值之比較基礎（參見下方「建立公平市場價值：有效方法」）。
    - **⚠ Note on §1014(f) and Form 706:** The stepped-up basis concept and FMV documentation requirement are entirely US tax law constructs (IRC §1014). The §1014(f) basis-consistency rules do not apply here: the decedent was a US citizen whose estate was almost certainly below the 2022 federal estate tax exclusion threshold (~$12,060,000), so no Form 706 was required to be filed. The stepped-up basis is FMV at date of death, documented by whatever evidence is available — there is no IRS form requirement specific to this scenario beyond maintaining defensible documentation.

### Establishing May 2022 FMV: Valid Methods

Because no formal appraisal was commissioned at the time of inheritance, FMV must be established retroactively. The IRS accepts any methodology that a qualified appraiser would accept, provided it is documented, internally consistent, and grounded in objective data. Four methods are available, listed in order of IRS defensibility:

---

**Method 1 — Comparable Sales Analysis (實價登錄 / Actual Price Registration)**

Taiwan's Ministry of the Interior (MOI) operates the **實価登錄** (Actual Price Registration) database, which records every real estate transaction in Taiwan at the actual contract price, unit, and floor level. The 2.0 version (launched July 2021) includes building-specific data (unit number, floor, area, price per ping, and transaction date).

- **How to use it:** Search for transactions in the same building or the immediate neighborhood (within 500 meters, same building age and type) from **March–August 2022** (±3 months from date of death). Calculate a price-per-ping (坪) range from those comparables and apply it to the subject property's area to derive an estimated FMV.
- **IRS mapping:** This method corresponds to the **Sales Comparison Approach** described in IRS Publication 561 and IRS Internal Revenue Manual (IRM) 4.48.6 (Real Property Valuation Guidelines). The IRS uses this approach as its primary method for residential real property.
- **Strength:** Objective, government-recorded, publicly accessible data — extremely difficult for the IRS to dispute if comparables are close in time, location, and property type.
- **Limitation:** Comparable transactions may be sparse for the specific building during a narrow time window; if <3 comparables exist, supplement with Method 2 or 4.
- **Sources:**
    - [MOI 實價登錄 Query Portal (lvr.land.moi.gov.tw)](https://lvr.land.moi.gov.tw/) — the official government database for actual transaction prices; supports searches by district, building address, and time period
    - [IRS Publication 561 — Determining the Value of Donated Property](https://www.irs.gov/publications/p561) — IRS qualified appraisal standards and FMV methodology; Sales Comparison Approach is explicitly described
    - [IRS IRM 4.48.6 — Real Property Valuation Guidelines](https://www.irs.gov/irm/part4/irm_04-048-006) — IRS examiner guidance on how real property FMV is assessed; the three approaches (Sales Comparison, Income, Cost) are described; Sales Comparison is the primary residential method

---

**Method 2 — Retroactive Qualified Appraisal (不動産估価師)**

A **不動産估価師** (licensed real estate appraiser, Ministry of Interior) can produce a retroactive appraisal using historical market data as of May 2022. This is the strongest FMV documentation available because it satisfies the IRS "qualified appraisal" standard under IRC §170(f)(11) and Treasury Regulation §1.170A-17.

- **How to use it:** Engage a licensed 不動産估価師 now (before the sale, ideally). Provide the property details and specify the **effective date of valuation: May [date], 2022**. The appraiser will use 実価登録 data, government-assessed values, and their professional judgment to produce a formal report with an as-of-date opinion of value.
- **IRS mapping:** A qualified appraisal completed by a qualified appraiser and attached (in summary form) to the return is the highest tier of documentation under IRS Pub 561 and IRM 4.48.6.
- **Strength:** A signed appraisal report by a licensed professional with an explicit effective date shifts the burden of proof significantly toward the taxpayer in any IRS examination.
- **Limitation:** Costs NT$15,000–NT$50,000+ depending on complexity; turnaround 2–6 weeks. Retroactive appraisals are accepted but may receive more IRS scrutiny than a contemporaneous appraisal (i.e., one done at the time of death).
- **Sources:**
    - [不動産估価師公會全國聯合會 (Taiwan Association of Real Estate Appraisers)](https://www.twarea.org.tw/) — the national association of licensed real estate appraisers; maintains a searchable directory of licensed 不動産估価師
    - [不動産估価師法 (Real Estate Appraiser Act)](https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=D0060049) — MOI statute governing licensing, professional standards, and scope of work for 不動産估価師
    - [IRS Publication 561](https://www.irs.gov/publications/p561) — defines "qualified appraisal" and "qualified appraiser" for IRS purposes; a Taiwan-licensed appraiser generally meets the qualification standard if their credentials are described in the appraisal report

---

**Method 3 — Government-Assessed Values as a Conservative Floor**

The **公告現值** (Assessed Current Land Value) and **房屋評定現值** (House Assessed Value) for May 2022 are government-published figures that establish a documentable minimum basis. These are the same values used for Taiwan inheritance tax (遺產稅) purposes.

- **How to use it:** Retrieve the May 2022 公告現值 (from the MOI online system) and the 房屋評定現值 (from the 稅捐稽徵處 via a 房屋稅籍證明書). Convert both to USD at the May 2022 TWD/USD spot rate. Use as a conservative floor estimate if no market data is available.
- **IRS mapping:** Government-assessed values are relevant supporting data but are not equivalent to FMV under US tax law. The IRS will accept them as one data point, but the agent or examiner will typically expect market-based corroboration. Using assessed values alone without comparables is the weakest FMV documentation.
- **Strength:** Entirely objective government data; essentially zero cost to obtain; useful as a sanity check and minimum bound.
- **Limitation:** As discussed in Phase 2, 房屋評定現值 can be **70–90% below market value** due to Taiwan's depreciation formula. Using assessed values as FMV will likely **understate** the US basis — resulting in higher US capital gains tax than necessary. Use this method only if market data is unavailable.
- **Sources:**
    - [MOI 全國公告土地現值查詢系統](https://www.land.moi.gov.tw/chhtml/landvalue/42) — national system for querying historical 公告現值 by parcel and year
    - [新北市政府稅捐稽徵處——房屋稅籍證明書](https://www.tax.ntpc.gov.tw/cp-2158-1225-7f578-1.html) — how to obtain the 房屋評定現值 via a 房屋稅籍證明書

---

**Method 4 — Broker Opinion of Value (經紀人市場行情意見書)**

A licensed Taiwan real estate broker or agent can provide a written **市場行情意見書** (market opinion letter or broker price opinion) estimating the property's value as of May 2022, based on their knowledge of local market conditions and transaction history.

- **How to use it:** Contact an established broker in the New Taipei City area (particularly the district where the property is located). Request a written opinion dated to May 2022, referencing specific comparables they are aware of. This is often obtainable at low cost or as part of a listing agreement.
- **IRS mapping:** A broker opinion is not a "qualified appraisal" under IRC §170(f)(11) because brokers are not "qualified appraisers" in the IRS sense. However, it is accepted as supporting documentation in an audit context and is useful as corroborating evidence alongside Method 1 or Method 2.
- **Strength:** Low cost, easily obtained, provides market-based context; particularly useful if the broker has specific knowledge of transactions in the same building.
- **Limitation:** Not a qualified appraisal; treated as secondary documentation only. A sophisticated IRS examiner will discount it if no comparables are cited.

---

**Comparison Table**

| Method | IRS Strength | Cost | Time | Taiwan Government Source? |
|---|---|---|---|---|
| 1. 実価登録 Comparables | High (Sales Comparison Approach) | Free | 1–2 hours | Yes (MOI database) |
| 2. 不動産估価師 Appraisal | Highest (Qualified Appraisal) | NT$15K–50K+ | 2–6 weeks | Yes (MOI-licensed) |
| 3. Government Assessed Values | Low (floor only, understates FMV) | Free | 1–2 weeks | Yes (官方數據) |
| 4. Broker Opinion | Low-Medium (supporting only) | Free–Low | 1 week | No |

---

**Practical Recommendation**

Use **Method 1 + Method 2 together** for the strongest documentation package:
1. Pull 実価登録 comparables for March–August 2022 for the same building and surrounding area.
2. Commission a retroactive 不動産估価師 appraisal with an effective date of May 2022, referencing those same comparables.
3. The appraiser's report anchored to government-recorded transaction data gives you both a qualified appraisal (highest IRS tier) and objective data support (hard to dispute).

If time or cost is a constraint, Method 1 alone (with a well-documented spreadsheet of comparables including registration numbers from 実価登録) is likely sufficient for an estate of this size. Retain screenshots/exports from the MOI database as part of your permanent tax file.

**Sources for this sub-section:**
- [IRS Publication 561 — Determining the Value of Donated Property](https://www.irs.gov/publications/p561)
- [IRS IRM 4.48.6 — Real Property Valuation Guidelines](https://www.irs.gov/irm/part4/irm_04-048-006)
- [IRS Publication 551 — Basis of Assets (Inherited Property section)](https://www.irs.gov/publications/p551)
- [MOI 實価登錄 Query Portal](https://lvr.land.moi.gov.tw/)
- [不動産估価師公會全國聯合會](https://www.twarea.org.tw/)

---

- [ ] **Confirm Property Use History (Personal Use vs. Rental):**
    - Determine whether the property was rented out — either by the decedent before May 2022 or by the heir after inheritance.
    - **Taiwan side:** Rental income received by a non-resident is subject to 20% withholding; if rental income went unreported, there may be outstanding Taiwan tax liability. Confirm with Taiwan CPA that all prior filings are current before closing — unresolved obligations can delay the title transfer.
    - **US side:** If the heir received rental income after May 2022, the property is investment/rental property for US tax purposes. In that case: (a) depreciation deductions should have been claimed on the US return since 2022 (reducing the current basis below the stepped-up FMV), and (b) §1250 unrecaptured depreciation is taxed at 25% rather than the preferential long-term rate on any gain. If the property has been entirely personal-use since inheritance with no rental income, neither of these applies — confirm this with your US CPA and note it in your permanent tax file.

- [ ] **Gather Deductible Expense Records:**
    - Taiwan-deductible: original acquisition cost (government-assessed value at inheritance), deed tax (契稅), stamp duty, notary fees, agent commissions (both buy and sell side), and major capital improvement receipts (post-inheritance renovations).
    - US-deductible: selling expenses (commissions, legal fees) reduce the capital gain.
    - **Legal sources:**
        - [NTBT — 房地合一 (HSTT) English Overview](https://www.ntbt.gov.tw/english/multiplehtml/cd61d91304fc4fb194571fea1d82ba35) — official English HSTT page from the National Taxation Bureau of Taipei; covers eligible deduction categories including deed tax, stamp duty, notary fees, brokerage commissions, and qualifying capital improvement costs
        - [NTBT — Filing 房地合一所得稅 (HSTT Return)](https://www.ntbt.gov.tw/english/htmlList/88c7365da64c421c8455d20116172462) — NTBT filing guidance with detail on what documentation is required to support each deduction claim
        - [Taxation Administration, MOF — Land Value Increment Tax (LVIT)](https://www.dot.gov.tw/Eng/singlehtml/en_143) — reference for LVIT under the Old System; relevant if the pre-2016 regime applies
        - [Taxation Administration, MOF — Stamp Tax](https://www.dot.gov.tw/Eng/singlehtml/en_140) — stamp duty reference for deductible expense documentation
    - **中文法源：**
        - [財政部——個人出售繼承取得之房地，房地成本以繼承時房屋評定現值及公告土地現值按消費者物價指數調整計算](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=4f67457f68ee4c5ea98bad28127d4584) — **核心法源**：財政部直接說明繼承取得房地之HSTT成本計算規則；成本 = 繼承時房屋評定現值及公告土地現值，**需按交易日所屬年月最新消費者物價指數（CPI）調整後認定**（此CPI調整為常見漏算項目，漏計將導致成本少計、溢繳稅款）
        - [財政部稅務入口網——捌、房地合一課徵個人所得稅相關問題](https://www.etax.nat.gov.tw/etwmain/web/ETW118W/CON/904/5887006684254281366) — 財政部房地合一問答總覽，涵蓋可減除費用認定標準
        - [財政部稅務入口網——申報房地合一稅應如何申報及檢附文件](https://www.etax.nat.gov.tw/etwmain/alien-tax-service/alien-tax-faq/05KVgzL) — 申報所需文件清單，包含費用扣除憑證要求
        - [財政部臺北國稅局——房地合一稅2.0修法重點](https://www.ntbt.gov.tw/singlehtml/cd61d91304fc4fb194571fea1d82ba35?cntId=fa38f9d9fdae496b82ee5ce5061d2041) — 中文版房地合一2.0說明，含費用扣除相關修法重點
        - [財政部北區國稅局——房地合一專區](https://www.ntbna.gov.tw/multiplehtml/cae51830571d48b0a3b01c01ad336483) — 北區國稅局房地合一整合資訊
        - [財政部中區國稅局——房地合一專區](https://www.ntbca.gov.tw/multiplehtml/9d087e8054ea4ea1a7dae372c99ce934) — 中區國稅局房地合一整合資訊
    - **⚠ New finding — CPI adjustment required:** The MOF page (中文法源第一筆) reveals that the 繼承時房屋評定現值及公告土地現值 must be **adjusted by the Consumer Price Index (CPI) as of the month of sale** before use as the HSTT cost basis. This adjustment is not mentioned in the main memo text and is a documented common error — taxpayers who omit it under-claim their cost basis and overpay tax. Ensure your Taiwan CPA applies this CPI adjustment when calculating HSTT liability.

**Key Terms for Online Research:**

| Chinese | Pinyin | English |
|---|---|---|
| 地政事務所 | Dìzhèng Shìwùsuǒ | Land Administration Office |
| 登記日 | Dēngjì Rì | Date of Ownership Transfer Registration |
| 戶籍 | Hùjí | Household Registration |
| 戶籍謄本 | Hùjí Téngběn | Household Registration Extract |
| 戶政事務所 | Hùzhèng Shìwùsuǒ | Household Registration Office |
| 居住者 / 非居住者 | Jūzhùzhě / Fēi Jūzhùzhě | Resident / Non-Resident (Taiwan Tax Status) |
| 遺產稅 | Yíchǎn Shuì | Inheritance Tax |
| 遺產稅免稅證明書 | Yíchǎn Shuì Miǎnshuì Zhèngmíngshū | Inheritance Tax Exemption Certificate |
| 完稅證明書 | Wánshuì Zhèngmíngshū | Tax Payment Completion Certificate |
| 公告現值 | Gōnggào Xiànzhí | Assessed Current Land Value |
| 房屋評定現值 | Fángwū Píngdìng Xiànzhí | House Assessed Value |
| 契稅 | Qìshuì | Deed Tax |

---

## Phase 2: Taiwan Tax Analysis (Local Liability)
*Goal: Calculate the net tax owed to the Taiwan Ministry of Finance.*

- [ ] **Determine the Tax Regime (Old System / HSTT 1.0 / HSTT 2.0):**
    - **Old System (original purchase before Jan 1, 2016):** Building gain only is taxed as ordinary income (separate from land); land gain is subject to Land Value Increment Tax (LVIT / 土地增值稅), administered by local government — these are two separate taxes filed with separate authorities.
    - **HSTT 1.0 (original purchase Jan 1, 2016 – Jun 30, 2021):** Unified tax on combined house+land gain. Rate schedule differs from HSTT 2.0: ≤1yr 45%; >1–2yr 35%; **>2yr combined hold = flat 20%** — no 15% bracket exists. A combined hold of 14+ years still applies at 20%. On the NT$9.45M illustrative gain, this equals ~NT$1.89M (~$61K) vs. NT$1.42M (~$46K) under HSTT 2.0 — a NT$470K (~$15K) difference.
    - **HSTT 2.0 (original purchase Jul 1, 2021 or later):** Unified tax at the 45%/35%/20%/15% schedule below. A single filing with the national tax authority within 30 days of transfer.
    - **For this property:** Original purchase confirmed as **April 2012** (exact day TBD, pre-Jan 2016) → Old System applies. Confirm exact day via title deed search for precise LVIT and combined holding period calculations.

- [ ] **Map the Full HSTT Rate Schedule (New System):**
    - ≤2 years combined holding: **45%**
    - >2 and ≤5 years: **35%**
    - >5 and ≤10 years: **20%**
    - >10 years: **15%**
    - Self-use exemption pathway: **10% flat** after NT$4 million deduction (residency requirements apply — see below)

- [ ] **Calculate Combined Holding Period (Tack-On Rule):**
    - Apply the "inheritance bridge": [Mother's holding years from purchase date] + [Your holding years: 登記日 through sale date in 2026].
    - This is the single most consequential calculation — model it with the exact 登記日 and the confirmed purchase date.
    - With confirmed April 2012 purchase and sale registered August 2026, combined hold ≈ 14 years → **15% bracket**.

- [ ] **Evaluate Self-Use Exemption (戶籍 Residency Requirement) — affects property sales tax (HSTT) only:**
    - Requires 戶籍 registered *at this property specifically* for at least 6 of the combined holding years, with no rental or business use and evidence of physical occupancy.
    - **Assessment: likely unavailable.** Even if your 戶籍 is still active, it is probably not registered at this property, and the physical residency requirement is unmet given your US-based living situation. Confirm with Taiwan CPA, but do not plan on this exemption applying.
    - If somehow eligible: 10% flat rate on gain above NT$4 million; gain below NT$4M is exempt.
    - Note: this exemption is a function of 戶籍 and occupancy — **not** of Taiwan tax residency (the 183-day rule). A Taiwan tax non-resident cannot claim the self-use exemption regardless.

- [ ] **Old System — Building Gain Income Tax Modeling:**
    - If Old System applies and you are a **Taiwan tax resident** (≥183 days in 2026 — treat as inapplicable given US-based living): the building gain is added to all other income and taxed at progressive Taiwan rates (up to ~40%); the interaction with US-source income matters.
    - As a **Taiwan tax non-resident** (<183 days — confirmed scenario): the building gain is instead subject to a flat withholding rate (~20% — see Phase 1 ⚠ flag for CPA confirmation on 財產交易所得). This is the scenario to model and is more favorable than progressive rates.

- [ ] **Old System — LVIT Estimation:**
    - Calculate the Land Value Increment Tax on the land portion based on the change in government-assessed land value (公告地價) from the inheritance date (2022) to the 2026 sale date.
    - Self-use LVIT rate is 10% flat; general rates are tiered (20%–40%). Administered by local government, not national tax authority.
    - **Self-use LVIT rate is unavailable here** — it requires 戶籍 registered at this specific property with evidence of physical occupancy, the same conditions that make the HSTT self-use exemption unavailable (see Phase 1 and Phase 2 above). Plan on **general tiered rates (20%–40%)**.

---

### Regime Comparison: Which System Yields Higher Tax?

*Context: ~$450K USD (~NT$14.5M) New Taipei City property, US-based non-resident seller, combined holding period likely >10 years.*

**Note on the Phase 2 building gain bullet above:** That bullet describes progressive Taiwan resident rates (up to ~40%). For a confirmed non-resident (<183 days/year), the building gain is instead subject to a **flat withholding rate** (likely ~20% — see Phase 1 ⚠ flag). This non-resident treatment is actually *more favorable* than resident progressive rates and is a key input to the comparison below.

#### The Core Structural Difference

The two systems tax fundamentally different things:

| | New System (HSTT) | Old System |
|---|---|---|
| **What is taxed** | Actual market gain: sale price minus government-assessed cost basis at inheritance | Government-assessed changes only: building gain (small) + land 公告地價 increment (moderate) |
| **Why the base differs** | Land 公告現值 is only ~8–15% below market land value nationally (MOI 2019: 91.64% avg). The large gap is in building 房屋評定現值, which can be 70–90% below building market value due to Taiwan's assessed-value depreciation formula. For older properties, total assessed value is far below total market — HSTT taxes the full gap. | Building values *depreciate* in assessed terms; LVIT is measured in 公告地價 units (which closely track market land value) rather than actual sale price |
| **Rate(s)** | 15% flat for >10yr combined holding | Building income: ~20% flat (non-resident); LVIT: 20–40% tiered |
| **# of tax authorities** | One (national, MOF) | Two (national for building, local government for LVIT) |
| **Filing deadline** | 30 days from transfer registration | Building: annual income tax return (May 2027); LVIT: at time of sale |

**Sources for table above:** [HSTT rate schedule & 30-day deadline (NTBT English)](https://www.ntbt.gov.tw/english/multiplehtml/cd61d91304fc4fb194571fea1d82ba35); [Land Tax Act — LVIT rate tiers (English, law.moj.gov.tw)](https://law.moj.gov.tw/ENG/LawClass/LawAll.aspx?pcode=G0340096); [LVIT rate tiers 貳 (財政部稅務入口網)](https://www.etax.nat.gov.tw/etwmain/tax-info/understanding/tax-saving-manual/local/land-value-increment-tax/noaGA0q); [Old System building gain added to annual income return (財政部)](https://www.mof.gov.tw/singlehtml/384fb3077bb349ea973e7fc6f13b6974?cntId=684c43657d2f44779b94ee3fe0838529); [LVIT must be filed at time of sale — 我的E政府](https://www.gov.tw/News_Content_2_378930); [Building/land split uses time-of-sale assessed values Q1142 (財政部稅務入口網)](https://www.etax.nat.gov.tw/etwmain/tax-info/understanding/tax-q-and-a/national/individual-income-tax/taxation-scope/which-income/r8q3EDv)

#### Why Assessed Values Are the Critical Lever

For a NT$14.5M (~$450K) property in New Taipei City, the government-assessed values at inheritance are a small fraction of market:
- **Land 公告現值:** NT$3–4.5M is a reasonable range. Land 公告現值 nationally averages ~91.64% of market land value (MOI 2019 press release), so the land assessed/market gap is only ~8–15%. The large understatement is in the building value below.
- **Building 房屋評定現值:** NT$500K–800K (buildings depreciate heavily under Taiwan's assessed-value formula: 房屋現值 = 核定單價 × 面積 × (1 − 折舊率 × 年數) × 地段等級率; a 15–20 year old unit may retain only 10–30% of its original assessed cost basis, making the building assessed value a small fraction of market)
- **Total assessed at 2022 inheritance:** NT$3.5–5.3M range, vs. market value of NT$14.5M — the gap is dominated by building depreciation, not land undervaluation
- **After CPI adjustment (+~12% for 2022→2026):** ~NT$4–6M

This means the **HSTT taxable gain is NT$8–10M on a NT$14.5M sale** — the full market-vs.-assessed gap becomes the tax base, even at the low 15% rate.

Under the Old System, the tax bases are far smaller because both the building gain and LVIT are measured in government-assessed terms, not market terms.

**Sources:** [MOI 2019 press release — 公告現值 national avg = 91.64% of market](https://www.land.moi.gov.tw/chhtml/content/10?mcid=3834); [宜蘭地政事務所 FAQ Q5 — 公告現值為何低於市價](https://ilanland.e-land.gov.tw/chaspx/Faq_Detail.aspx?web=178&id=1462); [台南市地政局 FAQ — 公告現值為何比市價低](https://land.tainan.gov.tw/11/QADetailC115400.aspx?Cond=117e0a12-202e-44b8-a7a6-4e9e0a02d403); [財政部 — 房屋現值如何核定（折舊公式）](https://www.etax.nat.gov.tw/etwmain/announcement/news/Pq5xPN9)

#### Illustrative Side-by-Side (~NT$14.5M sale)

*Assumptions: assessed values at inheritance = NT$4.2M (NT$3.5M land + NT$700K building); CPI-adjusted basis = NT$4.7M; deductible expenses = NT$350K (seller-side agent commission ~1.5% + stamp duty + 代書 + notary; buyer's commission is paid by the buyer); non-resident flat rate ~20% for building gain (pending CPA confirmation).*

**New System (HSTT):**
| Item | Amount |
|---|---|
| Sale price | NT$14.5M |
| Less: CPI-adjusted cost basis | (NT$4.7M) |
| Less: deductible expenses | (NT$350K) |
| **Taxable gain** | **NT$9.45M** |
| Rate (>10yr combined hold) | 15% |
| **HSTT due** | **~NT$1.42M (~$46K USD at NT$31/USD; ~$48K at NT$29.5/USD)** |

**Old System — Building Income Tax:**

*Correction applied: Taiwan law (所得稅法施行細則) requires the building/land split to use assessed values at the time of SALE ("按出售時之房屋評定現值占公告土地現值及房屋評定現值總額之比例"), not at inheritance. By 2026 the building is ~4 years further depreciated; land 公告現值 may also have been reassessed upward. Sources: [財政部稅務入口網 Q1142](https://www.etax.nat.gov.tw/etwmain/tax-info/understanding/tax-q-and-a/national/individual-income-tax/taxation-scope/which-income/r8q3EDv); [NTBT Old System Q&A](https://www.ntbt.gov.tw/singlehtml/9de2c2c966cb4fb48aca9dddf1fcae9c?cntId=fb1eaa593cfc4072954312284580cc3b)*

| Item | Amount |
|---|---|
| 2026 building 房屋評定現值 (est., further depreciated from NT$700K) | ~NT$650K |
| 2026 land 公告現值 (est., slightly increased from NT$3.5M) | ~NT$3.6M |
| Building % of 2026 assessed (NT$650K / NT$4.25M) | ~15% |
| Building allocation of sale price (NT$14.5M × 15%) | NT$2.175M |
| Less: adjusted building cost basis (NT$700K × 1.12 CPI) | (NT$784K) |
| Less: building-apportioned deductibles (~15% × NT$350K) | (NT$53K) |
| **Building taxable gain** | **~NT$1.338M** |
| Rate (non-resident flat, ~20%) | ~20% |
| **Building income tax** | **~NT$268K (~$9K USD at NT$31/USD)** |

**Old System — LVIT (the swing factor):**

LVIT depends heavily on how much 公告地價 has risen since the *original purchase* — making the original purchase date the single most important variable in the old system calculation.

| Assumed purchase year | Combined hold | Original 公告地價 (est.) | 2026 公告地價 (est.) | LVIT base | Approx. LVIT (after tiering) |
|---|---|---|---|---|---|
| 2014 | ~12yr | NT$2.0M | NT$3.5M | NT$1.5M | ~NT$300K (~$9K USD) |
| 2010 | ~16yr | NT$1.2M | NT$3.5M | NT$2.3M | ~NT$570K (~$18K USD) |
| 2005 | ~21yr | NT$700K | NT$3.5M | NT$2.8M | ~NT$840K (~$26K USD) |
| 2000 | ~26yr | NT$400K | NT$3.5M | NT$3.1M | ~NT$1.02M (~$31K USD) |

*LVIT tiering: 20% on the first 100% of the original 公告地價, 30% on the next 100%, 40% above 200%. **No long-hold discount applies for combined holdings under 20 years.** Discount triggers only at >20yr (20% reduction on excess above the 20% floor rate), >30yr (30% reduction), >40yr (40% reduction) — using: discounted_rate = original_rate − [(original_rate − 20%) × reduction%]. The 2005 vintage (~21yr) benefits from the >20yr discount in Tiers 2 and 3; the 2000 vintage (~26yr) also qualifies. Sources: [LVIT rate tiers — 貳 (財政部稅務入口網)](https://www.etax.nat.gov.tw/etwmain/tax-info/understanding/tax-saving-manual/local/land-value-increment-tax/noaGA0q); [Long-hold discount formula — 參 (財政部稅務入口網)](https://www.etax.nat.gov.tw/etwmain/tax-info/understanding/tax-saving-manual/local/land-value-increment-tax/VGE8YNL); [LVIT overview — Invest Taiwan (English)](https://investtaiwan.nat.gov.tw/showPage?lang=eng&search=68); [New Taipei City LVIT (English)](https://www.tax.ntpc.gov.tw/cp-131-3180-19226-2.html)*

**Summary comparison:**

| Scenario | Building tax | LVIT | **Old System total** | **HSTT (New System)** | **Difference** |
|---|---|---|---|---|---|
| Purchased 2014 | ~$9K | ~$10K | **~$19K** | **~$46K** | Old saves ~$27K |
| Purchased 2010 | ~$9K | ~$18K | **~$27K** | **~$46K** | Old saves ~$19K |
| Purchased 2005 | ~$9K | ~$27K | **~$36K** | **~$46K** | Old saves ~$10K |
| Purchased 2000 | ~$9K | ~$33K | **~$42K** | **~$46K** | Old saves ~$4K |

#### Rules of Thumb

1. **Old System is likely $4–27K cheaper** for this property profile, depending entirely on how long ago the mother originally purchased. The advantage shrinks the further back the original purchase date, because LVIT accumulates on a larger 公告地價 increment. The 2014 vintage shows the largest Old System advantage (~$27K savings); the 2000 vintage almost closes the gap (~$4K savings). *(All USD conversions at NT$31/USD; deductible expenses = NT$350K seller-side only.)*

2. **LVIT is the swing factor.** Building income tax (~$8K) is relatively stable regardless of original purchase date. What varies is LVIT — which scales with 公告地價 appreciation since the *original* (pre-2016) purchase. If the mother purchased in 2014 vs. 2000, the LVIT difference alone is ~$22K. Sources for LVIT rate tiers: [財政部稅務入口網 — 貳](https://www.etax.nat.gov.tw/etwmain/tax-info/understanding/tax-saving-manual/local/land-value-increment-tax/noaGA0q); [LVIT trial calculation tool](https://www.etax.nat.gov.tw/etwmain/etw158w/51)

3. **Old System becomes more expensive than New System** only if original purchase was very early AND 公告地價 has risen very sharply — roughly: pre-1995 vintage + heavy urban appreciation. For a 2000s purchase, Old System still saves meaningfully at this price point.

4. **Non-resident status is an Old System advantage.** Building gain for a non-resident is taxed at ~20% flat rather than the progressive resident rate (up to ~40%). At the same building gain amount, a US-resident-in-Taiwan would pay roughly double the building income tax. This makes the Old System comparatively more attractive for US-based owners than it would be for Taiwan residents. (Source: [財政部 — 非居住者扣繳率](https://www.etax.nat.gov.tw/etwmain/alien-tax-service/alien-individual-income-tax/vV8Z3o9) — confirms 20% flat withholding for most non-resident income categories; see Phase 1 ⚠ flag re: 財產交易所得 confirmation with CPA)

5. **HSTT has a "big base, low rate" problem.** Even at 15%, taxing NT$9.45M (the market/assessed gap) produces NT$1.42M (~$46K at NT$31/USD) in tax. The Old System avoids this by never putting market value appreciation into the tax base directly.

6. **For New System (HSTT), the holding period bracket matters enormously.** If the combined holding period somehow fell into the 5–10yr bracket (20% rate), the HSTT would be ~NT$1.82M (~$56K) — a large jump. At 35% (2–5yr), it would be ~NT$3.19M (~$98K). Confirming a combined hold >10 years is essential before planning around the 15% rate. ([HSTT rate schedule — NTBT English](https://www.ntbt.gov.tw/english/multiplehtml/cd61d91304fc4fb194571fea1d82ba35); [NTBT — 繼承接計持有期間](https://www.ntbt.gov.tw/singlehtml/41ae3594197f4f69b47753ce08188516?cntId=cdeb372790044547ad6a8749ae975e4a))

7. **US tax is largely symmetric across both Taiwan regimes.** Because the US stepped-up basis resets to FMV at May 2022 (not the original purchase date), US capital gain = price appreciation since 2022 only. The Taiwan regime choice does not change the US gain calculation; it only affects the Foreign Tax Credit available to offset US tax. Higher Taiwan tax → larger FTC → lower net US tax (up to the FTC limitation). NIIT (3.8%) applies regardless and is not offset by FTC. ([IRS Pub 551 — Inherited Property stepped-up basis](https://www.irs.gov/publications/p551); [IRS — About Form 1116, Foreign Tax Credit](https://www.irs.gov/forms-pubs/about-form-1116))

#### What to Do With This

- **If title search confirms pre-2016 purchase → budget ~$19–42K USD in Taiwan tax** (Old System at NT$31/USD; 2014 purchase = ~$19K, 2010 = ~$27K, 2005 = ~$36K, 2000 = ~$42K)
- **If title search confirms post-2016 purchase → budget ~$46–48K USD in Taiwan tax** (HSTT 2.0 at 15% if original purchase was Jul 2021+; NT$31–29.5/USD), assuming >10yr combined hold still applies via tack-on rule. **If original purchase was Jan 2016–Jun 2021 (HSTT 1.0), budget ~$61K instead** — the 15% bracket does not exist under HSTT 1.0, and a combined hold of any length >2yr applies at 20% flat
- **In either case:** engage a Taiwan CPA to (a) confirm the non-resident 20% flat rate for building gain, (b) apply the CPI adjustment to cost basis, and (c) calculate actual 公告地價 at original purchase year for LVIT estimation

**Key Terms for Online Research:**

| Chinese | Pinyin | English |
|---|---|---|
| 房地合一稅 | Fángdì Héyī Shuì | House and Land Unified Transaction Tax (HSTT) |
| 土地增值稅 | Tǔdì Zēngzhí Shuì | Land Value Increment Tax (LVIT) |
| 持有期間 | Chíyǒu Qījiān | Holding Period |
| 繼承取得 | Jìchéng Qǔdé | Acquisition by Inheritance (Tack-On Rule) |
| 公告地價 | Gōnggào Dìjià | Government-Assessed Land Price |
| 自住 | Zìzhù | Self-Use / Owner-Occupancy |
| 自住優惠稅率 | Zìzhù Yōuhuì Shuìlǜ | Self-Use Preferential Tax Rate |
| 財政部 | Cáizhèng Bù | Ministry of Finance |
| 國稅局 | Guóshuì Jú | National Taxation Bureau |

---

## Phase 3: US Tax Analysis (Worldwide Liability)
*Goal: Calculate IRS liability and identify double-taxation relief.*

- [ ] **Confirm Stepped-Up Basis Eligibility (IRC §1014):**
    - US citizens and residents inheriting foreign real estate are entitled to a stepped-up basis to FMV at the date of death.
    - Basis = FMV as of the date of death (May 2022), not the original purchase price.
    - Documentation risk: ensure a defensible appraisal exists (see Phase 1).
    - **Note on §1014(f):** The basis-consistency rules (which require the heir to use the same value reported on Form 706) do not apply here. For a US citizen dying in 2022, Form 706 was only required if the gross estate exceeded $12,060,000 — far above the value of this property alone. If the mother's total estate was below that threshold, no Form 706 was filed and §1014(f) imposes no constraint. ⚠ If she had other significant assets that pushed her total estate above ~$12M, confirm with a US CPA whether Form 706 was required.
    - **Legal source:** [IRS — Estate Tax FAQ (filing threshold)](https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes) — confirms Form 706 is required only when the gross estate exceeds the applicable exclusion amount for the year of death
    - **Legal sources:**
        - [IRS Publication 551 — Basis of Assets (Rev. December 2025)](https://www.irs.gov/publications/p551) — authoritative IRS publication on stepped-up basis; the "Inherited Property" section confirms FMV at date of death as basis for property received from a decedent
        - [IRS FAQ — Gifts & Inheritances](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances) — IRS FAQ directly confirming FMV-at-death as the cost basis for inherited property
        - [IRS Topic 703 — Basis of Assets](https://www.irs.gov/taxtopics/tc703) — IRS topic page summarizing the basis rules for inherited, gifted, and purchased property

- [ ] **Calculate US Capital Gain:**
    - `[2026 Sale Price] - [2022 FMV (stepped-up basis)] - [Selling Expenses]`
    - Gain since 2022 only — not since mother's original purchase date.
    - Report the sale on Form 8949 (enter "INHERITED" in column (b)) and carry to Schedule D.
    - **Currency conversion required:** All amounts must be reported in USD. Use the TWD/USD spot exchange rate on the date of each transaction: (a) for the stepped-up basis, use the rate as of the date of death (May 2022); (b) for the sale price and selling expenses, use the rate on the closing date (2026). The IRS has no official exchange rate and accepts any consistently-used posted rate (e.g., Federal Reserve, OANDA, XE). USD/TWD exchange rate fluctuation between 2022 and 2026 is therefore a separate variable in the gain calculation, independent of the property's local-currency price change.
    - **Legal sources:**
        - [IRS Publication 544 — Sales and Other Dispositions of Assets (2025)](https://www.irs.gov/publications/p544) — covers how to compute gain or loss on disposition of property, including foreign real estate; confirms selling expenses reduce the amount realized
        - [IRS — About Form 8949, Sales and Other Dispositions of Capital Assets](https://www.irs.gov/forms-pubs/about-form-8949) — the form on which the gain is reported; "INHERITED" entered in column (b) designates it as inherited property receiving automatic long-term treatment
        - [IRS Instructions for Schedule D (Form 1040) (2025)](https://www.irs.gov/instructions/i1040sd) — Schedule D is where the net capital gain from Form 8949 is carried and the applicable rate is computed
        - [IRS — Foreign Currency and Currency Exchange Rates](https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates) — IRS guidance on converting foreign currency amounts to USD; confirms use of spot rate on date of transaction and acceptance of any consistently-used posted rate
        - [IRS — Yearly Average Currency Exchange Rates](https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates) — IRS published annual average rates (acceptable for income received evenly throughout the year, though spot rate on transaction date is preferred for a single sale event)

- [ ] **Apply Long-Term Capital Gains Rate:**
    - Long-term rates apply (0% / 15% / 20% depending on taxable income).
    - **Correction from original note:** For inherited property, IRC §1223(11) provides that the holding period is *automatically* treated as long-term, regardless of how long you actually held the property — even if you sold the day after registration. You do not need to confirm that the hold exceeds 12 months. Report the gain in Part II (long-term) of Form 8949 with "INHERITED" in column (b).
    - For 2026 income thresholds (inflation-adjusted annually): consult the IRS's current-year tax rate schedules. As a reference point, for 2025 the 0% bracket applies below ~$48,350 (single) / ~$96,700 (MFJ); 20% applies above ~$533,400 (single) / ~$600,050 (MFJ); 15% applies in between.
    - **Legal sources:**
        - [IRS Topic no. 409 — Capital Gains and Losses](https://www.irs.gov/taxtopics/tc409) — IRS topic page on capital gains rates and the >1-year holding period requirement; notes that inherited property is automatically long-term
        - [IRS Instructions for Schedule D (Form 1040) (2025)](https://www.irs.gov/instructions/i1040sd) — confirms that property acquired by inheritance goes in Part II (long-term), citing IRC §1223(11)
        - [IRS — Federal Income Tax Rates and Brackets](https://www.irs.gov/filing/federal-income-tax-rates-and-brackets) — current IRS page with official income brackets including capital gains rate thresholds
        - [IRS — IRS Releases Tax Inflation Adjustments for Tax Year 2026](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill) — official 2026 inflation-adjusted figures

- [ ] **Check Net Investment Income Tax (NIIT):**
    - If your MAGI exceeds $200K (single) or $250K (MFJ), an additional **3.8% NIIT** applies to the lesser of (a) net investment income or (b) the MAGI excess above the threshold.
    - **This is not offset by the Foreign Tax Credit** — the FTC is only allowed against Chapter 1 income tax; NIIT is a separate Chapter 2A tax. IRS explicitly confirms: "foreign income tax credits may not be used to reduce NIIT liability." Model this separately.
    - The MAGI thresholds ($200K/$250K) are **not inflation-adjusted** — they are fixed by statute and have not changed since NIIT was enacted in 2013.
    - Gain from the sale of investment real estate is unambiguously subject to NIIT.
    - **Legal sources:**
        - [IRS Topic no. 559 — Net Investment Income Tax](https://www.irs.gov/taxtopics/tc559) — IRS topic page summarizing NIIT, the 3.8% rate, MAGI thresholds, and what counts as net investment income
        - [IRS — Questions and Answers on the Net Investment Income Tax](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax) — IRS Q&A explicitly confirming (a) gain from investment real estate is subject to NIIT and (b) FTC cannot be used to reduce NIIT
        - [IRS — About Form 8960, Net Investment Income Tax](https://www.irs.gov/forms-pubs/about-form-8960) — the form used to compute NIIT; attach to Form 1040

- [ ] **Apply Foreign Tax Credit (Form 1116):**
    - Taiwan HSTT or building income tax paid may be applied as a credit against US income tax liability (not NIIT — see above).
    - Key limitation: FTC is subject to income basket rules. Capital gains from foreign real estate generally fall into the **passive category** basket on Form 1116. Unused credits in one basket cannot offset tax in another basket.
    - Additionally: because the Taiwan gain is taxed in the US at a preferential long-term rate (15% or 20%), the Form 1116 instructions require a **rate-differential adjustment** — you must reduce the foreign-source income reported on Line 1a by multiplying by 0.4054 (15% rate group) or 0.5405 (20% rate group). This adjustment reduces the FTC limitation and may leave residual US tax even when Taiwan tax nominally exceeds US tax on the same gain.
    - FTC coverage is unlikely to be 1:1 for this transaction. Model residual US tax after FTC application and rate-differential adjustment.
    - **⚠ LVIT creditability question:** The FTC requires the foreign tax to be an income tax (or excess profits tax). Taiwan HSTT — a tax on capital gain income — clearly qualifies. However, **LVIT (土地增值稅)** is administered by local government and measured on land value increments, which the IRS could potentially characterize as a property transfer tax rather than an income tax. Confirm LVIT creditability with your US CPA before claiming it as FTC.
    - **Legal sources:**
        - [IRS Publication 514 — Foreign Tax Credit for Individuals (2025)](https://www.irs.gov/publications/p514) — comprehensive guidance on FTC eligibility, basket categories, the limitation computation, and rate-differential adjustments for capital gains
        - [IRS Instructions for Form 1116 (2025)](https://www.irs.gov/instructions/i1116) — covers basket categories; confirms rate-differential adjustment for foreign capital gains taxed at reduced US rates (multiply by 0.4054 or 0.5405 per rate group)
        - [IRS Topic no. 856 — Foreign Tax Credit](https://www.irs.gov/taxtopics/tc856) — introductory IRS topic page on FTC eligibility and Form 1116 overview
        - [IRS — Foreign Tax Credit (eligibility overview)](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit) — IRS summary page explaining the creditability requirements (compulsory, imposed by foreign government, tax on income)

- [ ] **Identify Informational Filing Requirements:**
    - **Form 3520:** **Not applicable in this situation.** Form 3520 Part IV is triggered only by bequests from a *nonresident alien individual* or a *foreign estate* (IRC §6039F; Form 3520 instructions). The decedent was a US citizen — US citizenship is permanent regardless of physical residence, so living in Taiwan does not make a US citizen a "nonresident alien." Her estate is also not a "foreign estate": under IRC §7701(a)(31), a foreign estate is one whose foreign-source income is *not* subject to US income tax; a US citizen's estate is taxable on worldwide income and therefore does not qualify. No Form 3520 obligation arose from this inheritance. Confirm with your US CPA that no Taiwan trust structure was involved in the estate administration that could alter this analysis.
    - **FBAR (FinCEN 114):** Required if the aggregate value of all foreign financial accounts exceeds $10,000 at **any point** during the calendar year — including momentarily while sale proceeds sit in a Taiwan bank account. Filed with FinCEN (not IRS), due April 15 (auto-extended to October 15).
    - **FATCA (Form 8938):** Required if total specified foreign financial assets exceed the applicable threshold. For a US-resident individual filing single: $50,000 at year-end or $75,000 at any point during the year; for MFJ: $100,000 / $150,000. **Note:** The IRS explicitly states that foreign real property held directly is **not** a specified foreign financial asset — "a personal residence or a rental property does not have to be reported" on Form 8938. However, a Taiwan bank account holding the sale proceeds **would** be a specified foreign financial asset and would trigger Form 8938 once it exceeds the threshold (in addition to FBAR). If the property was held through any foreign entity (trust, company), that entity interest would be reportable.
    - **Legal sources:**
        - [IRS — About Form 3520 (foreign inheritance/gifts)](https://www.irs.gov/forms-pubs/about-form-3520) — confirms Form 3520 is required for bequests from foreign estates >$100,000; also links to current instructions
        - [IRS Instructions for Form 3520 (Rev. December 2025)](https://www.irs.gov/instructions/i3520) — full filing instructions including threshold, due date, penalties, and filing address
        - [FinCEN — Report Foreign Bank and Financial Accounts (FBAR)](https://www.fincen.gov/report-foreign-bank-and-financial-accounts) — official FinCEN page for FBAR (FinCEN Form 114); confirms $10,000 aggregate threshold and April 15 due date
        - [IRS — Report of Foreign Bank and Financial Accounts (FBAR)](https://www.irs.gov/businesses/small-businesses-self-employed/report-of-foreign-bank-and-financial-accounts-fbar) — IRS companion page for FBAR, including penalty framework and link to BSA e-filing system
        - [IRS — About Form 8938, Statement of Specified Foreign Financial Assets](https://www.irs.gov/forms-pubs/about-form-8938) — official Form 8938 page with thresholds, definition of "specified foreign financial assets," and key differences from FBAR
        - [IRS — Basic Questions and Answers on Form 8938](https://www.irs.gov/businesses/corporations/basic-questions-and-answers-on-form-8938) — IRS FAQ explicitly confirming that foreign real property held directly is **not** a specified foreign financial asset and does not need to be reported on Form 8938
        - [IRS — Comparison of Form 8938 and FBAR Requirements](https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements) — IRS side-by-side comparison clarifying when each form is required and what assets each covers
    - **Note — Form 3520 inapplicable here:** The ⚠ timing flag previously noted in this section has been removed. Form 3520 does not apply because the decedent was a US citizen (not a nonresident alien) and her estate is not a "foreign estate" under IRC §7701(a)(31). No late filing obligation exists.

- [ ] **Check State Income Tax:**
    - Depending on your state of residence, the capital gain may be taxable at the state level.
    - Some states (e.g., California) tax all capital gains as ordinary income with no preferential long-term rate and no state-level foreign tax credit — meaning the full gain is stacked on top of other income and taxed at up to 13.3% (California's top marginal rate, including the 1% Mental Health Services Tax on income over $1M; most taxpayers will be in the 9.3%–12.3% range) with no credit for Taiwan taxes paid.
    - Other states have no income tax (TX, FL, NV, WA, etc.) or provide a state-level FTC (varies by state).
    - Confirm your state's treatment before projecting total tax.
    - **⚠ No universal government source applies here** — state income tax treatment of foreign capital gains varies by state and must be researched state-by-state. For California specifically:
        - [California FTB — Capital Gains and Losses](https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html) — FTB page directly stating California does not have a lower rate for capital gains; all capital gains are taxed as ordinary income
        - [California FTB — 2025 Tax Rate Schedules](https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf) — official California income tax rate schedule confirming rates from 1% to 13.3%; capital gains are taxed at these same rates with no reduction
    - For all other states: consult your state tax authority's website or a state-tax-experienced CPA.
    - **⚠ California foreign tax credit:** California's credits are limited to taxes paid to other US states; no credit is available for foreign taxes paid to Taiwan. No standalone IRS source covers this (it is a California-specific rule); confirm directly with the FTB or a California CPA.

---

### Gain Calculation Methodology (Federal IRS & California FTB)

*Both the Internal Revenue Service (IRS) and the California Franchise Tax Board (FTB) start from the same capital gain figure — the same basis, the same amount realized, the same dollar gain. They diverge only in the tax rate applied and the relief available for Taiwan taxes paid.*

#### Step 1 — Establish the US Dollar (USD) Cost Basis

Under Internal Revenue Code (IRC) §1014, the basis of inherited property is its fair market value (FMV) at the date of death. California conforms to this rule.

```
Basis (USD) = Property FMV in New Taiwan Dollars (TWD) as of May 2022
              ÷ TWD/USD spot exchange rate on the date of death
```

- The FMV must be documented by a qualified appraisal or defensible comparable-sales data as of May 2022 (see Phase 1 bullet on FMV appraisal).
- The IRS has no official exchange rate. Any consistently-used posted rate is acceptable (e.g., Federal Reserve, OANDA, XE).
- **No depreciation is deducted from basis** — the property was held as personal (non-rental, non-business) real estate.

**Sources:** [IRS Publication 551 — Basis of Assets](https://www.irs.gov/publications/p551); [IRS FAQ — Gifts & Inheritances](https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances); [California FTB — Schedule D (540) Instructions 2025](https://www.ftb.ca.gov/forms/2025/2025-540-d-instructions.html) (California conforms to IRC §1014)

#### Step 2 — Establish Amount Realized

```
Amount Realized (USD) = [Gross sale price in TWD ÷ TWD/USD spot rate on closing date]
                        − Seller-paid selling expenses converted at the same closing-date rate
```

Seller-paid selling expenses that reduce the amount realized include: real estate agent commissions (both sides if paid by seller), legal/notary fees, deed tax (契稅), and stamp duty (印花稅) paid by seller. These are deducted here.

**Taiwan HSTT (House and Land Transaction Tax / 房地合一稅) and LVIT (Land Value Increment Tax / 土地增值稅) are NOT deducted from the amount realized.** These are income taxes handled separately — either as a Foreign Tax Credit (FTC) on the federal return, or potentially as a foreign tax deduction. Subtracting them here would be double-counting.

**Sources:** [IRS Publication 544 — Sales and Other Dispositions of Assets](https://www.irs.gov/publications/p544); [IRS — Foreign Currency and Currency Exchange Rates](https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates); [IRS Topic 503 — Deductible Taxes](https://www.irs.gov/taxtopics/tc503) (confirms foreign income taxes are not deducted as selling expenses; the FTC or deduction election applies instead)

#### Step 3 — Compute Capital Gain

```
Capital Gain (USD) = Amount Realized (USD) − Basis (USD)
```

This figure is the **same on both your federal return and your California return.** It is automatically long-term — inherited property is treated as held longer than one year regardless of actual holding period under IRC §1223(11), so there is no holding-period test to satisfy.

Report on Form 8949 (enter "INHERITED" in column (b)) and carry to Schedule D.

**Source:** [IRS Instructions for Schedule D (Form 1040)](https://www.irs.gov/instructions/i1040sd)

#### Step 4 — Currency Effect: A Separate Variable

Because the basis is converted at the **2022 exchange rate** and the sale price at the **2026 rate**, TWD/USD fluctuation is an independent variable in the gain calculation — separate from whether the property appreciated in local-currency terms.

If TWD weakens against USD between 2022 and 2026 (e.g., NT$29/USD → NT$32/USD), the USD gain will be **smaller** than the NT$ gain — potentially significantly so. Conversely, if TWD strengthens, the USD gain is larger. This effect can make a material difference in whether you owe federal/California tax at all, independent of Taiwan's tax outcome.

**Source:** [IRS — Yearly Average Currency Exchange Rates](https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates)

#### Step 5 — Federal Tax on the Gain

| Layer | Rate | Applied to |
|---|---|---|
| Long-term capital gains | 0% / 15% / 20% | Gain amount; rate bracket based on total taxable income |
| Net Investment Income Tax (NIIT) | 3.8% | Gain amount, if Modified Adjusted Gross Income (MAGI) > $200K (single) / $250K (married filing jointly / MFJ) |
| **Less: Foreign Tax Credit (FTC)** | Reduces income tax dollar-for-dollar | Taiwan HSTT paid (creditable); LVIT creditability uncertain — confirm with CPA |

Key FTC constraint: the credit is computed on Form 1116 with a **rate-differential adjustment** — foreign-source income in the 15% long-term rate group is multiplied by 0.4054, and in the 20% group by 0.5405, before computing the FTC limitation. This adjustment reduces the allowable credit below the face amount of Taiwan tax paid, and may leave residual US income tax even when Taiwan tax exceeds the nominal US rate. The FTC does **not** offset NIIT.

**Sources:** [IRS Publication 514 — Foreign Tax Credit for Individuals](https://www.irs.gov/publications/p514); [IRS Instructions for Form 1116](https://www.irs.gov/instructions/i1116); [IRS — Questions and Answers on the Net Investment Income Tax](https://www.irs.gov/newsroom/questions-and-answers-on-the-net-investment-income-tax) (confirms FTC cannot offset NIIT); [IRS — Foreign Tax Credit: Choosing Credit or Deduction](https://www.irs.gov/individuals/international-taxpayers/foreign-tax-credit-choosing-to-take-credit-or-deduction)

#### Step 6 — California FTB Tax on the Same Gain

California uses the **identical gain figure** from Step 3 but applies different rules:

| Item | California treatment |
|---|---|
| Tax rate | Ordinary income rates — 1% to 13.3% (no preferential long-term rate) |
| NIIT | Not applicable — California has no equivalent |
| Foreign Tax Credit | **Not available** — California provides no credit for taxes paid to foreign countries |
| Foreign tax as itemized deduction | **Likely unavailable** — California does not conform to the federal Schedule A deduction for foreign income taxes; confirm with a California CPA |

**Net result:** California taxes the full gain at ordinary income rates with zero relief for Taiwan taxes paid. This is the layer of double taxation that neither the FTC nor any other federal mechanism can offset.

**Sources:** [California FTB — Capital Gains and Losses](https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html); [California FTB — 2025 Tax Rate Schedules](https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf); [California FTB — 2025 Instructions for Schedule CA (540)](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html)

#### Illustrative Example

*Assumptions: FMV at death May 2022 = NT$13M; TWD/USD rate May 2022 = NT$29.5/USD → basis = $440,678 USD. Sale price 2026 = NT$14.5M; TWD/USD rate closing 2026 = NT$31/USD → gross proceeds = $467,742 USD. Seller-paid selling expenses = NT$450K → $14,516 USD. Amount realized = $453,226 USD.*

```
Capital Gain = $453,226 − $440,678 = $12,548 USD
```

*At 15% federal long-term rate: ~$1,882 federal income tax. Taiwan HSTT paid ≈ $42K USD (far exceeds federal income tax) → FTC eliminates the $1,882 federal income tax entirely (excess FTC is not refundable but may carry forward). NIIT at 3.8% ≈ $477 (not offset by FTC). California at ~10% ordinary rate ≈ $1,255 with no relief.*

*Note: The small USD gain (~$12.5K) on a NT$1.5M TWD gain is entirely due to TWD depreciation from NT$29.5 to NT$31 between 2022 and 2026. Had the TWD held at NT$29.5, the USD gain would have been ~$50K — materially larger federal and California tax.*

#### What You Need to Complete This Calculation

- [ ] Documented FMV appraisal (or comparable sales evidence) for the property as of May 2022
- [ ] Confirmed TWD/USD spot rate on date of death (May 2022) — from Federal Reserve H.10 release or similar
- [ ] Confirmed TWD/USD spot rate on closing date (2026)
- [ ] Itemized seller-paid closing costs in TWD (from the closing statement)
- [ ] Total Taiwan HSTT or Old System taxes paid in TWD (for FTC conversion to USD)

**Sources:** [IRS — Foreign Currency and Currency Exchange Rates](https://www.irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates); [Federal Reserve — Foreign Exchange Rates (H.10)](https://www.federalreserve.gov/releases/h10/)

---

**Key Terms for Online Research:**

| Chinese | Pinyin | English |
|---|---|---|
| 外國稅額抵免 | Wàiguó Shuì'é Dǐmiǎn | Foreign Tax Credit (FTC) — Taiwan-side term for the credit mechanism |
| — | IRC §1014 | Stepped-Up Basis Rule (Inherited Property) |
| — | Form 1116 | US Foreign Tax Credit Claim |
| — | Form 3520 | Annual Return to Report Foreign Inheritance / Trust Transactions — **not applicable here** (decedent was a US citizen, not a nonresident alien) |
| — | FBAR / FinCEN 114 | Foreign Bank Account Report |
| — | Form 8938 / FATCA | Statement of Specified Foreign Financial Assets |
| — | NIIT | Net Investment Income Tax (3.8%) |
| — | MAGI | Modified Adjusted Gross Income |

---

## Phase 4: Logistics, Deadlines & Payment
*Goal: Ensure compliance with filing timelines and manage cash flow.*

- [ ] **Taiwan Filing Deadlines:**
    - **New System (HSTT 2.0):** File and pay within **30 days** of transfer registration. This is a hard deadline — missing it triggers penalties.
    - **Old System:** Building gain is added to your annual income tax return, filed in May of the following year (May 2027 for a 2026 sale). LVIT is filed separately with the local government at time of sale.

- [ ] **Designate a Taiwan-based authorized representative (代理人) before closing:**
    - As a non-resident, you will almost certainly not be physically present in Taiwan during the 30-day HSTT filing window after closing. The deadline runs regardless of your location.
    - Engage your Taiwan CPA or the handling 代書 (title transfer notary) as your designated 代理人 to: (a) receive the buyer's withholding certificate, (b) file the HSTT return within 30 days of transfer registration, (c) remit any balance due or file for a refund if withholding exceeded actual tax owed.
    - Confirm the 代理人 designation in writing before the sale closes. Without a local representative, the hard 30-day deadline creates a practical compliance risk that cannot be resolved remotely after the fact.

- [ ] **Non-Resident Withholding at Closing — triggered by tax residency (183-day rule), not 戶籍:**
    - Because you are a Taiwan tax non-resident (<183 days/year in Taiwan), the buyer is typically required to withhold a portion of the purchase price at closing and remit it directly to the tax authority on your behalf.
    - This is a cash flow issue, not an additional tax — the withheld amount is credited against your final HSTT liability. However, if withholding exceeds actual tax owed, you must file for a refund, which takes time.
    - Confirm the exact withholding rate and mechanics with your Taiwan CPA or the handling notary before closing.

- [ ] **Payment from Sale Proceeds:**
    - Confirm with the handling attorney or notary whether HSTT and LVIT can be paid directly from escrow/proceeds at time of closing.
    - In practice this is common, but confirm the mechanics with the local agent.

- [ ] **Wire Transfer & Currency Reporting:**
    - Wiring large proceeds from Taiwan to the US: amounts over $10,000 trigger Bank Secrecy Act reporting at the receiving US bank.
    - Taiwan banks may require documentation of the source of funds (sale contract, tax clearance) before releasing an international wire.
    - Factor in wire timing when planning cash flow around US filing deadlines.

- [ ] **US Filing Deadline:**
    - The sale will be reported on your 2026 US federal return, due April 2027 (or October 2027 with extension).
    - Form 3520 is not required (decedent was a US citizen — see Phase 3 notes).

**Key Terms for Online Research:**

| Chinese | Pinyin | English |
|---|---|---|
| 申報 | Shēnbào | Tax Declaration / Filing |
| 扣繳 | Kòujiǎo | Tax Withholding at Source |
| 代扣稅款 | Dài Kòu Shuìkuǎn | Withholding Tax Remitted by Buyer |
| 結匯 | Jiéhuì | Foreign Exchange Settlement (Wire Transfer of Proceeds) |
| 外匯申報 | Wàihuì Shēnbào | Foreign Exchange Declaration |
| 國稅局 | Guóshuì Jú | National Taxation Bureau |
| 財政部電子申報 | Cáizhèng Bù Diànzǐ Shēnbào | Ministry of Finance e-Filing Portal |

---

## Professional Resources to Engage

- [ ] **Taiwan CPA or tax attorney** with HSTT expertise — to confirm regime, calculate LVIT if applicable, and advise on non-resident withholding.
- [ ] **US CPA or tax attorney** with foreign real estate experience — specifically: IRC §1014 stepped-up basis for foreign inherited property, Form 1116 basket analysis, Form 3520, FBAR/FATCA.

---

## Summary of Key Findings
1. **The "Tack-on" Rule:** You can add your mother's holding years to yours for HSTT bracket purposes. If mother purchased pre-2016 but the New System still applies (edge case to confirm), a combined hold exceeding 10 years puts you in the 15% bracket.
2. **The "Step-up" Basis:** For US purposes, you are taxed only on gain since May 2022, not since mother's original purchase — but you need a documented FMV appraisal to defend this.
3. **Double Tax Protection:** The US Foreign Tax Credit should substantially offset double taxation, but is not a perfect shield — the NIIT (3.8%) applies regardless of FTC, and basket limitations may leave residual US liability.
4. **Two Distinct Residency Concepts — Different Tax Consequences:**
    - **戶籍 (household registration)** → affects *property sales tax* (HSTT self-use exemption eligibility only). The self-use exemption is almost certainly unavailable: even with active 戶籍, it must be registered at *this property* for 6+ years with physical occupancy. Close this out and plan on the standard HSTT rate schedule.
    - **Taiwan tax residency (183-day rule)** → affects *income tax treatment* (flat 20% withholding vs. progressive rates under the Old System) and the *withholding mechanism at closing* (buyer withholds on behalf of non-resident sellers). Treat non-resident status as confirmed given US-based living.
