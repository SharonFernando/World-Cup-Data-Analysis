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

# Dados banco de dados
HOST=os.getenv('DB_HOST')
PORT=os.getenv('DB_PORT')
NAME=os.getenv('DB_NAME')
USER=os.getenv('DB_USER')
PASSWORD=os.getenv('DB_PASSWORD')