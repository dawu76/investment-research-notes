### Real estate price estimation

[tw.forumosa.com](https://tw.forumosa.com/t/guide-how-to-estimate-the-price-of-a-property-in-taiwan/237990): How to Estimate the Price of a Property in Taiwan

**The Slow (but best) Way**
- Go to the Ministry of Interior’s [land database website](https://lvr.land.moi.gov.tw/) and type in the road or street that the property is located on, but not the exact address. You should select only the “房地” checkbox, and enter the most recent 1 year for the “交易期間” range dates. You should also open up the side filter and type in which floor the property is located on. Now do a search, and hopefully you will have lots of results for properties recently sold that are similar to the property you are assessing.
- If there are very few results, or no results at all, then you may need to do the search again with a few nearby roads/streets names and include all the data in your later calculations.
- Highlight and copy all the data (there may be multiple pages) and paste into a Google Sheets or Microsoft Excel spreadsheet. When highlighting, start from the bottom right cell and drag up to the top left cell.
- Once all the data is in your spreadsheet, identify the column called “單價 (萬元/坪)”, which is the average price per ping and write a formula that calculates the average price per ping. Bear in mind that the data in this column is in 10,000 units, so to find the actual price per ping we will later need to multiply it by 10,000.
- Example: In this case, the result was 34.44 and so by multiplying by 10,000, we come to the number $344,400 per ping. Now, finally we can multiple the per ping value by how many pings the property we are assessing has. For this example, let’s say 30 ping. 30 * $344,400 = $10,332,000 -> So the final estimate for this example property is $10.3 million.

**The Fast (but worse) Way**
- If you don’t have time to use the previous method, you can use House Plus’ [立即估價 page](https://www.houseplus.com.tw/estimation). By typing in an exact address, you can estimate the price of a property. However, you must register for an account and you only get 5 free searches.
- For this example, let’s pick a roughly 30 ping 2nd floor property on Xingfu Road so we can compare our previous manual estimation with House Plus’ estimation. This estimate has the per ping price at $339,400, just $5,000 less than what we calculated manually.
- I’m not saying that House Plus’ estimate is inaccurate, it seems to me that it’s highly accurate, but I recommend the slow manual method because you know where your data is coming from and can fine tune it to be even more relevant to the property you are assessing, for example by entering the age of the property. House Plus, as far as I can tell, doesn’t give you much data about how they come to their estimation.

Notes
- The 單價 can include or exclude parking space. Some agents are sneaky and try to show it one way to make it seem the price is lower than competitors, when the competitor pricing is shown using the other method. Also they can record it down in the government site in different ways to inflate or deflate the price per ping. It’s best to use your own formula and derive at a price that includes and excludes the parking space. If you only check this box it should exclude properties with a parking space.
