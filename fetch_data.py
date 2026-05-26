import requests
import json
import os

# Esto busca el secreto que acabamos de crear en GitHub
api_key = os.environ.get('API_FOOTBALL_KEY')

url = "https://v3.football.api-sports.io/fixtures?live=all"
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'api-football-v1.p.rapidapi.com'
}

response = requests.get(url, headers=headers)
data = response.json()

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
