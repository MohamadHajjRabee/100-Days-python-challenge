import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_articles():
    news_api = "YOUR_NEWS_API"
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": news_api
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()["articles"][:3]

    message = ""
    for msj in news:
        message += f"\nHeadline: {msj['title']}\nBrief: {msj['description']}"
    return message


def send_sms(title):
    message = get_articles()
    account_sid = "YOUR_ACCOUNT_SID"
    auth_token = "YOUR_ACCOUNT_AUTH_TOKEN"
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=f"{title} {message}",
            from_='YOUR_TWILIO_PHONE_NUMBER',
            to='YOUR_VERIFIED_NUMBER'
        )

    print(message.sid)


alphavantage_api = "YOUR_ALPHAVANTAGE_API"
alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_api
}

alphavantage_response = requests.get(url="https://www.alphavantage.co/query", params=alphavantage_parameters)
alphavantage_response.raise_for_status()
stock_data = alphavantage_response.json()

yesterday_close = float(list(stock_data["Time Series (Daily)"].items())[0][1]["4. close"])
previous_day_close = float(list(stock_data["Time Series (Daily)"].items())[1][1]["4. close"])
percentage = (yesterday_close - previous_day_close) / previous_day_close * 100
percentage = round(percentage, 2)

if percentage > 2:
    message_title = f"{STOCK}: 🔺{percentage}%"
    send_sms(message_title)
elif percentage < -2:
    message_title = f"{STOCK}: 🔻{abs(percentage)}%"
    send_sms(message_title)
