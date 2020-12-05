import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
owm_api_key = os.environ.get("OWM_API_KEY")
lat = 45.649490
long = 25.606550

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

params = {
    "lat": lat,
    "lon": long,
    "exclude": "current,minutely,daily",
    "appid": owm_api_key,
}

res = requests.get(url=OWM_ENDPOINT, params=params)
res.raise_for_status()
weather_data = res.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔️",
            from_="+14156349707",
            to="+40732513832"
        )

    print(message.status)
