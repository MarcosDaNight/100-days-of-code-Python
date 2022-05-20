import requests

OWM_EndPoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "7bf5efa44bc739f3a32824ccc5e04d0d"  # your API key

parameters = {
    "lat": -6.907790,
    "lon": -37.521290,
    "exclude": "hourly",
    "appid": api_key
}


def get_weather():
    response = requests.get(url=OWM_EndPoint, params=parameters)
    response.raise_for_status()
    print(response.status_code)
    print(response)
    data = response.json()
    return data


print(get_weather())
