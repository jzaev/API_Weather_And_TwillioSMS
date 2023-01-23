import requests
from twilio.rest import Client

account_sid = "AC68959a76a5bdb1731ca82b30eddc78fb"
auth_token = "dc4ef6f7b866dc13a99cd5e1dd5c453e"

API_KEY = "54d6071c2db35b7439edb2da68572a1d"
LAT = 38  # 38.664398
LNG = 34  # 21.116257

parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": API_KEY,
    "exclude": "daily,current,minutely",
}
respond = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
weather_data_hourly_12 = respond.json()["hourly"][0:12]
my_rain_list = [x["weather"][0]["id"] for x in weather_data_hourly_12]

if min(my_rain_list) < 700:
    msg = "Take the umbrella"
else:
    msg = "Don't worry. Sky is clear"

client = Client(account_sid, auth_token)
message = client.messages.create(body=msg, from_='+18125944733', to='+972532857801')

print(message.status)
