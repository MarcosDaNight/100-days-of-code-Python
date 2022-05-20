import requests

OWM_EndPoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "7bf5efa44bc739f3a32824ccc5e04d0d"  # your API key

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

if will_rain:
    print("Take your umbrella!")

else:
    print("Right now, the time is ok!")