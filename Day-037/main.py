import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USER_TOKEN = "YOUR_USER_TOKEN"
USERNAME = "YOUR_USERNAME"
GRAPH_ID = "YOUR_GRAPH_ID"

user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": USER_TOKEN
}

graph_config = {
    "id": GRAPH_ID,
    "name": "YOUR_GRAPH_CODE",
    "unit": "Hours",
    "type": "int",
    "color": "kuro"
}

# response = requests.post(f"{pixela_endpoint}/{USERNAME}/graphs", json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

post_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did u code today? ")

}

response = requests.post(
    f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json=post_pixel, headers=headers)
print(response.text)

# new_pixel_data = {
#     "quantity": "5"
# }

# response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}",
#                         json=new_pixel_data,
#                         headers=headers
#                         )
# print(response.text)

# response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}",
#                            headers=headers
#                            )
# print(response.text)
