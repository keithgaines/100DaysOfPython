import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = 'YOUR APP ID'
API_KEY = 'YOUR API KEY'
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = YOUR SHEETY ENDPOINT

exercise_input = input("What exercise did you do today?: ")

nutritionix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': 'your user ID'
}

parameters = {
    'query': exercise_input,

}

bearer_headers = {
    'Authorization': 'Bearer YOUR TOKENß'
}

response = requests.post(url=EXERCISE_ENDPOINT, headers=nutritionix_headers, json=parameters)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)

    print(sheet_response.text)