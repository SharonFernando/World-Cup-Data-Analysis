import os
from dotenv import load_dotenv

# Leitura do arquivo .env
load_dotenv()

API_KEY = os.getenv('KICK_OFF_API_KEY')

# Dicionário com as variáveis do arquivo .env
HEADERS = {
    "x-api-key": API_KEY
    }

# Dicionário com os parâmetros de requisição da API
PARAMS = {
    'teams' : {
        'league': 1,
        'season': 2026
    },
    'fixtures': {
        'league': 1,
        'season': 2026
    }
}

# Dicionário com os endpoints da API
ENDPOINTS = {
    'fixtures': 'https://app.kickoffapi.com/api/v1/fixtures',
    'players': 'https://app.kickoffapi.com/api/v1/players',
    }