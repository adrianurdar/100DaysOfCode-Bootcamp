import requests

params = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

res = requests.get(url="https://opentdb.com/api.php", params=params)
res.raise_for_status()
data = res.json()

question_data = data["results"]
