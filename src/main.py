from api import get_data
from config import ENDPOINTS, PARAMS

# Requisição HTTP
data = get_data(
    ENDPOINTS["teams"],
    PARAMS["teams"]
)

print(data)