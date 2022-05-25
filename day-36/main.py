import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "319TWXQHDGPV1ESC"
NEWS_API_KEY = "7e2c856c85434800ad187b03d6313733"

TWILIO_SID = "AC25ff4e67c2b9ddb4595eee0da2b24153"  # your account SID
TWILIO_TOLKEN = "e8a8be5db649a854df11c776091d3e20"  # your auth tolken

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference / yesterday_closing_price) * 100

#if diff_percent > 5: print("Get News")

if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    for article in three_articles:
        client = Client(TWILIO_SID, TWILIO_TOLKEN)
        message = client.messages \
            .create(
            body=article,
            from_='+13193463515',
            to='+5583981214614'
        )

