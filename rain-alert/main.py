import requests
from twilio.rest import Client

account_sid = __SID__
auth_token = __TOKEN__

# Hometown
MY_LAT, MY_LONG = 16.073309, 120.442097

api_key = __KEY__

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 4,  # read API documentation # getting data every 3 hours for the next 12 hours = 4
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = [index for index in range(4) if weather_data["list"][index]["weather"][0]["id"] < 700]

if len(will_rain) > 0:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="RAIN ALERT: 🌧️\nHi there, it's going to rain today. Remember to bring an umbrella ☔",
        to="whatsapp:+639063416021"
    )

    print(message.status)

# TODO: Use environmental variables!
