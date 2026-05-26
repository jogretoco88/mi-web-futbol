import requests
import json
import os

# Tu API Key está guardada en los "Secrets" de GitHub
api_key = os.environ['API_FOOTBALL_KEY']

url = "https://v3.football.api-sports.io/fixtures?live=all"
headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "v3.football.api-sports.io"
}

response = requests.get(url, headers=headers)
data = response.json()

# Guardamos los resultados en un archivo data.json
with open('data.json', 'w') as f:
    json.dump(data, f)
  
