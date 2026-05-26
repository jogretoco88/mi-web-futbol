import requests
import json
import os

api_key = os.environ.get('API_FOOTBALL_KEY')

url = "https://v3.football.api-sports.io/fixtures?live=all"

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.get(url, headers=headers)
data = response.json()

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
