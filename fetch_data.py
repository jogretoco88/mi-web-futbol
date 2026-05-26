import requests
import json
import os

# Usamos os.environ.get para acceder al secreto
api_key = os.environ.get('API_FOOTBALL_KEY')

if not api_key:
    print("¡ERROR! La variable API_FOOTBALL_KEY no se encontró.")
    exit(1)

url = "https://v3.football.api-sports.io/fixtures?live=all"
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.get(url, headers=headers)
print(f"Código de respuesta: {response.status_code}")
data = response.json()

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
