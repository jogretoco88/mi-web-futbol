import requests
import json
import os

# Obtenemos la clave desde los secretos
api_key = os.environ.get('API_FOOTBALL_KEY')

# Cambiamos live=all por la fecha de hoy
url = "https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2026-05-25"

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'api-football-v1.p.rapidapi.com'
}

try:
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        # Si funciona, guardamos el resultado
        with open('data.json', 'w') as f:
            json.dump(response.json(), f, indent=4)
    else:
        # Si falla, guardamos el error para verlo en la web
        with open('data.json', 'w') as f:
            json.dump({"error": "Fallo en conexión", "code": response.status_code, "msg": response.text}, f, indent=4)
except Exception as e:
    print(f"Error crítico: {e}")
