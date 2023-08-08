import os
from twilio.rest import Client
import requests


api_key = "YOUR API KEY"
url = "http://api.weatherapi.com/v1/forecast.json"

account_sid = "YOUR TWILIO ACCT SID"
auth_token = "YOUR TWILIO AUTH TOKEN"

FROM = "YOUR TWILIO NUMBER"
TO = "YOUR RECEIVER NUMBER"

params = {
    "q": "ibadan",
    "aqi": "no",
    "key": api_key,
    "alerts": "no"
}

response = requests.get(url=url, params=params)
response.raise_for_status()
data = response.json()
# I want to get the data for 12 hours using slice.
sliced_data = data["forecast"]["forecastday"][0]["hour"][:12]
#print(sliced_data)

gon_rain = False

for each_hour in sliced_data:
    time = (each_hour["time"])
    code = (each_hour["condition"]["code"])
    print(code)
    text = (each_hour["condition"]["text"])
    an_hour = (time, code, text)

    if int(code) >= 1180:
        gon_rain = True

if gon_rain:
    print("bring an umbrella")

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"\nBro 😒 it's prolly gon rain!! 💦🌧️ Prepare 🥼☔🌧️.",
        from_= FROM,
        to= TO
    )

    print(message.status)


