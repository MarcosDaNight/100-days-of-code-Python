import requests
from twilio.rest import Client

OWM_EndPoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "7bf5efa44bc739f3a32824ccc5e04d0d"  # your API key
account_sid = "AC25ff4e67c2b9ddb4595eee0da2b24153"  # your account SID
auth_tolken = "e8a8be5db649a854df11c776091d3e20"  # your auth tolken
message = "It's going to rain today in Malta City, PB. Remember to bring an ☂"

rain_lat = 51.626640
rain_lon = 15.761730

parameters = {
    "lat": -6.907790,
    "lon": -37.521290,
    "exclude": "current,minutely,daily",
    "appid": api_key
}


def get_weather():
    response = requests.get(url=OWM_EndPoint, params=parameters)
    response.raise_for_status()
    return response.json()


def verify_rain(data_weather):
    weather_status = data_weather['hourly'][0]['weather'][0]['id']
    return weather_status < 700


data = get_weather()
weather_slice = data['hourly'][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
print(will_rain)
if will_rain:
    client = Client(account_sid, auth_tolken)
    message = client.messages \
        .create(
        body=message,
        from_='+13193463515',
        to='+5583981214614'
    )

    print(message.status)
