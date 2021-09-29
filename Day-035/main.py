import requests
from twilio.rest import Client

api_key = "API_KEY"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"
my_lat = 0.123456
my_long = 0.123456

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"]
weather = weather_data[:12]

rain = False
for i in weather:
    weather_id = i["weather"][0]["id"]
    if weather_id < 700:
        rain = True
        break

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella ☂️",
            from_='+9876543210',
            to='+1234567890'
        )
    print(message.status)
