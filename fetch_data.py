import requests
import json
import os

api_key = os.environ.get('API_FOOTBALL_KEY')

# Usaremos este endpoint y headers estándar
url = "https://v3.football.api-sports.io/fixtures?live=all"
headers = {
    'x-apisports-key': api_key
}

try:
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Datos guardados con éxito.")
    else:
        print(f"Error en la respuesta: {response.text}")
except Exception as e:
    print(f"Error de conexión: {e}")
