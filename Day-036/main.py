import os
import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

now = dt.datetime.now()

if now.day < 12:
    yesterday = f"{now.year}-{now.month}-0{now.day - 2}"
    day_before = f"{now.year}-{now.month}-0{now.day - 3}"
else:
    yesterday = f"{now.year}-{now.month}-{now.day - 2}"
    day_before = f"{now.year}-{now.month}-{now.day - 3}"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_api = os.environ.get("ALPHA_API")
alpha_endpoint = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_api,
}

res = requests.get(url=alpha_endpoint, params=params)
res.raise_for_status()
stock = res.json()

stock_yesterday = float(stock["Time Series (Daily)"][yesterday]["4. close"])
stock_day_before = float(stock["Time Series (Daily)"][day_before]["4. close"])

stock_change = round(stock_day_before / stock_yesterday * 100 - 100, 2)
if stock_change < 0:
    stock_move = f"{STOCK}: 🔻{stock_change * -1}%"
elif stock_change > 0:
    stock_move = f"{STOCK}: 🔺{stock_change}%"
else:
    stock_move = f"{STOCK}: {stock_change}%"

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_api = os.environ.get("NEWS_API")
news_endpoint = "http://newsapi.org/v2/top-headlines"
params = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "apiKey": news_api,
}

res = requests.get(url=news_endpoint, params=params)
res.raise_for_status()
news_data = res.json()
top_three = news_data["articles"][:3]

news = [f'{stock_move}\nHeadline: {news["title"]}\nBrief: {news["description"]}' for news in top_three]

for item in news:
    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    # Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
    file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
    of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
    file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
    of the coronavirus market crash.
    """
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    receiver = os.environ.get("RECEIVER")
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
            body=f"{item}",
            from_="+14156349707",
            to=receiver,
        )

    print(message.status)
