import requests
import json
import os
from datetime import datetime

# URL correcta para la V3 basada en la documentación que abriste
url = "https://apiv3.apifootball.com/"

# Aquí combinamos todo en 'params' según lo que pide esa página
params = {
    "action": "get_events",       # 'get_events' es para resultados/partidos
    "from": datetime.now().strftime('%Y-%m-%d'),
    "to": datetime.now().strftime('%Y-%m-%d'),
    "APIkey": os.environ.get('API_FOOTBALL_KEY')
}

response = requests.get(url, params=params)
print(f"Status Code: {response.status_code}")
print(f"Respuesta: {response.text}")

if response.status_code == 200:
    with open('data.json', 'w') as f:
        json.dump(response.json(), f, indent=4)
