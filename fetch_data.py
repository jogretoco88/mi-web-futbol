import requests
import json
import os
from datetime import datetime

# Configuramos con la clave que ya activaste
api_key = os.environ.get('API_FOOTBALL_KEY')

# Usamos la URL y Host que aparecen en tu pantalla
url = "https://apifootball3.p.rapidapi.com/apifootball/api/apifootball3"
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'apifootball3.p.rapidapi.com'
}

# Consultamos los eventos del día
querystring = {
    "action": "get_events",
    "from": datetime.now().strftime('%Y-%m-%d'),
    "to": datetime.now().strftime('%Y-%m-%d')
}

response = requests.get(url, headers=headers, params=querystring)

# Guardamos el resultado
if response.status_code == 200:
    data = response.json()
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("¡Éxito! Datos descargados.")
else:
    print(f"Error {response.status_code}: {response.text}")
