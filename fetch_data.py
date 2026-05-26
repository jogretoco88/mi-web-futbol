import requests
import json
import os
from datetime import datetime

# Configuramos la fecha de hoy automáticamente
hoy = datetime.now().strftime('%Y-%m-%d')
api_key = os.environ.get('API_FOOTBALL_KEY')

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

querystring = {
    "date": hoy,
    "league": "39", # Premier League (puedes cambiar este ID después)
    "season": "2025"
}

headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status() # Lanza error si el código no es 200
    
    data = response.json()
    
    # Guardamos el archivo data.json
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print("Éxito: Datos guardados en data.json")
    print(f"Status Code: {response.status_code}")

except Exception as e:
    print(f"Error al conectar con la API: {e}")
