import requests
from config import HEADERS, PARAMS, BASE_URL

# Função para realizar as requisições HTTP
def obter_dados(endpoint):
    response = requests.get(
        f"{BASE_URL}/{endpoint}",
        headers=HEADERS,
        params=PARAMS,
        timeout=30
    )

    response.raise_for_status()

    return response.json()["response"]