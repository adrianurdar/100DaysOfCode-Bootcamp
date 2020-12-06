# Stock Trading News Alert Project
## Day 36 - Intermediate+ - \#100DaysOfCode

**To do:**
* Create a stock trading news alert

**Acceptance criteria:**
* Use https://www.alphavantage.co
* When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
* Use https://newsapi.org
* Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
* STEP 3: Use https://www.twilio.com
* Send a separate message with the percentage change and each article's title and description to your phone number. 
* Format the SMS message like this: 
    * ```
        TSLA: 🔺2%
        Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
        Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are 
        required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 
        31st, near the height of the coronavirus market crash.
        ``` 
    * ```
        "TSLA: 🔻5%
        Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
        Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are 
        required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 
        31st, near the height of the coronavirus market crash.
        ```
