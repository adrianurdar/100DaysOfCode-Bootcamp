import os
import requests
from datetime import datetime

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_API = os.environ.get("SHEETY_API")


# Get Exercise Stats with Natural Language Queries
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

params = {
    "query": input("Tell me which exercises you did: ")
}

res = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers)
res.raise_for_status()
exercises = res.json()["exercises"]

# Setup Current Date And Time
now = datetime.now()
date = now.date().strftime("%d/%m/%Y")
time = now.time().strftime("%H:%M:%S")

# Saving Data into Google Sheets
exercises_name = [exercise["name"] for exercise in exercises]
exercises_duration = [exercise["duration_min"] for exercise in exercises]
exercises_calories = [exercise["nf_calories"] for exercise in exercises]

for i in range(len(exercises_name)):
    headers = {
        "Authorization": os.environ.get("NUTRITIONIX_AUTH"),
    }

    params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercises_name[i].title(),
            "duration": exercises_duration[i],
            "calories": exercises_calories[i],
        }
    }

    res = requests.post(url=SHEETY_ENDPOINT, json=params, headers=headers)
    res.raise_for_status()
    print(res.text)
