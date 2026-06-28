import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('KICK_OFF_API_KEY')

HEADERS = {
    'x-api-key': API_KEY
    }

URL = 'https://app.kickoffapi.com/api/v1/fixtures'

PARAMS = {
    'league': 1, 
    'season': 2026
    }

response = requests.get(
    URL, 
    headers=HEADERS,
    params=PARAMS,
    timeout=30)

response.raise_for_status()

data = response.json()

print(data.keys())
print(data['response'][0])

df_fixtures = pd.DataFrame(data)

print(df_fixtures)