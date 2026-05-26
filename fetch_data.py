import requests
import json
import os
from datetime import datetime

# Obtenemos la fecha de hoy automáticamente
hoy = datetime.now().strftime('%Y-%m-%d')
api_key = os.environ.get('API_FOOTBALL_KEY')

# La URL ahora usa la variable 'hoy'
url = f"https://api-football-v1.p.rapidapi.com/v3/fixtures?date={hoy}"

headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'api-football-v1.p.rapidapi.com'
}

response = requests.get(url, headers=headers)
# ... el resto de tu código para guardar en data.json
