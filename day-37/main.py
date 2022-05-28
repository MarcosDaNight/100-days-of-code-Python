from datetime import datetime

import requests

USERNAME = "marcosgdn"
TOKEN = "JAScnkqnnlsjcn2134SA"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "61",
}

# response = requests.post(url=pixel_creation_end_point, json=pixel_data, headers=headers)
# print(response.text)

date_update = datetime.now().strftime("%Y%m%d")  # chose a date

update_pixel_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_update}"

update_data = {
    "quantity": "42.5",
}

# response = requests.put(url=update_pixel_end_point, json=update_data, headers=headers)
# print(response.text)

data_delete = datetime.now().strftime("%Y%m%d")  # chose a date

delete_pixel_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{data_delete}"

response = requests.delete(url=delete_pixel_end_point, headers=headers)
print(response)