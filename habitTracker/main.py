import requests
from datetime import datetime

USERNAME = "<username_you_create>"
TOKEN = "<token you create>"
GRAPH_ID = "<name of graph>"

pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"


user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response)

graph_config = {
    'id': GRAPH_ID,
    'name': 'cycling graph',
    'unit': 'km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '9.8'
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)