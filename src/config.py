import os
from dotenv import load_dotenv

# Leitura do arquivo .env
load_dotenv()

# URL base dos endpoints
BASE_URL = "https://app.kickoffapi.com/api/v1"

# token da KickOff API
API_KEY = os.getenv('KICK_OFF_API_KEY')

# Dicionário com o cabeçalho da requisição da API
HEADERS = {
    "x-api-key": API_KEY
}

# Dicionário com os parâmetros de requisição da API
PARAMS = {
    'league': 1,
    'season': 2026
}

# Dicionário com os endpoints da API
ENDPOINTS = {
    "fixtures": f"{BASE_URL}/fixtures",
    "teams": f"{BASE_URL}/teams",
    "players": f"{BASE_URL}/players",
    "teams_statistics": f"{BASE_URL}/fixtures/{id}/statistics",
    "events": f"{BASE_URL}/fixtures{id}/events",
    "league": f"{BASE_URL}/leagues"
}