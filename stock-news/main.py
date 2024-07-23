import requests
from twilio.rest import Client
from math import floor

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key = __API_KEY__
api_key_news = __NEWS__KEY__

account_sid = __SID__
auth_token = __TOKEN__

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": api_key,
}

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": api_key_news,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()

# # temporary workaround, try and except to store data in stock_data.py:
# from stock_data import stock_data
# stock_data = stock_data
# transform dict to list
dates_list = [f"{dates}" for dates in stock_data["Time Series (Daily)"]]

# yesterday
most_recent_0 = stock_data["Time Series (Daily)"][dates_list[0]]["4. close"]
# the other day
most_recent_1 = stock_data["Time Series (Daily)"][dates_list[1]]["4. close"]

close_diff_actual = float(most_recent_0) - float(most_recent_1)
up_or_down = ""
if close_diff_actual < 0:
    up_or_down = "🔻"
else:
    up_or_down = "🔺"
    
close_diff = abs(float(most_recent_0) - float(most_recent_1))

percentage_diff = close_diff/((float(most_recent_0)+float(most_recent_1))/2)
percentage_diff *= 100

if percentage_diff > 5:
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data["articles"][:3]
    for _ in range(3):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=f"{STOCK_NAME}: {up_or_down} {floor(percentage_diff)}%\n"
                 f"Headline: {articles[_]['title']}\n"
                 f"Brief: {articles[_]["description"]}",
            to="whatsapp:+639063416021"
        )

# TODO: Deploy in cloud (Python Anywhere)
# TODO: Use environmental variables!
