import requests
import json
import os
# Usaremos una fecha fija que sabemos que tiene actividad hoy (2026-05-26)
hoy = "2026-05-26" 
api_key = os.environ.get('API_FOOTBALL_KEY')

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

# Sin filtros de liga, traerá TODO el fútbol del mundo para esta fecha
querystring = {"date": hoy}

headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Esto es para DEPURAR: Imprimiremos cuántos partidos encontró
print(f"Partidos encontrados: {len(data.get('response', []))}")

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
