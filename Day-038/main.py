import requests
from datetime import datetime

APP_ID = "YOUR_APP_ID"
API_KEY = "YOUR_API_KEY"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Tell me which exercises your did: "),
    "gender": "YOUR_GENDER",
    "weight_kg": YOUR_WEIGHT,
    "height_cm": YOUR_HEIGHT,
    "age": YOUR_AGE
}

response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
data = response.json()['exercises']

today = datetime.now()

for exercise in data:
    sheety_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }

    sheety_response = requests.post(url="YOUR_API",
                                    json=sheety_params,
                                    auth=("YOUR_USERNAME", "YOUR_PASSWORD")
                                    )
    print(sheety_response.text)
    print(sheety_response.json())
