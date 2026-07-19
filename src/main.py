import pandas as pd
from api import get_data
from config import BASE_URL, ENDPOINTS, PARAMS

# Criação do Dataframe dos fatos
df_fixtures = pd.json_normalize(get_data(f"{BASE_URL}/fixtures")["response"])
fixtures = df_fixtures[
    [
        "id",
        "date",
        "leagueId",
        "venueId",
        "homeTeamId",
        "awayTeamId",
        "goalsHome",
        "goalsAway",
        "scoreHalfHome",
        "scoreHalfAway",
        "scoreFullHome",
        "scoreFullAway",
        "seasonYear",
        "statusLong"
    ]
]

# Criação do Dataframe da dimesão dos times/seleções
home = df_fixtures[
    [
        "homeTeam.id",
        "homeTeam.name",
        "homeTeam.logo"
    ]
]

home.columns = [
    "id",
    "name",
    "logo"
]

away = df_fixtures[
    [
        "awayTeam.id",
        "awayTeam.name",
        "awayTeam.logo"
    ]
]

away.columns = [
    "id",
    "name",
    "logo"
]

teams = pd.concat([home, away]).drop_duplicates()

# Criação do Dataframe da dimesão dos estádios
venues = df_fixtures[
    [
        "venue.id",
        "venue.name",
        "venue.city",
    ]
]

venues.columns = [
    "id",
    "name",
    "city"
]

venues = venues.drop_duplicates()

# Criação do Dataframe da dimesão dos jogadores
df_players = pd.json_normalize(get_data(f"{BASE_URL}/players")["response"])

players = df_players[
    [
        "id",
        "name",
        "age",
        "nationality",
        "height",
        "weight"
    ]
]

players = players.drop_duplicates()

# Criação do Dataframe da dimensão das estatísticas dos jogos

data = []

for fixture in fixtures["id"][:2]:
  response = get_data(f"{BASE_URL}/fixtures/{fixture}/statistics")["response"]
  data.extend(response)

df_fixtures_stats = pd.json_normalize(data)

fixtures_stats = df_fixtures_stats[
    [
        "id",
        "fixtureId",
        "teamId",
        "type",
        "value"
    ]
]

fixtures_stats = fixtures_stats.drop_duplicates()

# Criação do Dataframe da dimensão dos eventos dos jogos
data = []

for fixture in fixtures["id"][:2]: #limitação de quantidade de execuções para teste | API tem limite de 100 requisições ao dia
  response = get_data(f"{BASE_URL}/fixtures/{fixture}/events")["response"]
  data.extend(response) #.extend ao invés de .append | "extend" percorre os itens do dicionário/lista

df_events = pd.json_normalize(data)

events = df_events[
    [
        "id",
        "fixtureId",
        "time",
        "playerId",
        "assistId",
        "teamId",
        "type",
        "detail",
        "comments"
    ]
]

events = events.drop_duplicates()