import requests
from config import HEADERS, PARAMS

# Função para realizar as requisições HTTP
def get_data(endpoint, params=None):
    response = requests.get(
        endpoint,
        headers=HEADERS,
        params=PARAMS,
        timeout=30
    )

    response.raise_for_status()

    return response.json()