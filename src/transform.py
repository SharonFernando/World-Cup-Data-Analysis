import pandas as pd
from api import obter_dados


# Obter as informações de um endpoint
def carregar_endpoint(endpoint):

    response = obter_dados(f"{endpoint}")
    
    return pd.json_normalize(response)


# Criar o dataframe das partidas
def criar_fixtures(df_fixtures):

    fixtures = df_fixtures[
        [
            "id",
            "date",
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

    return fixtures


# Criar o dataframe dos times
def criar_teams(df_fixtures):

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

    return teams


# Criar o dataframe dos estádios
def criar_venues(df_fixtures):
    
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

    return venues


# Criar o dataframe dos jogadores
def criar_players(df_players):

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

    return players


# Criar o dataframe das estatísticas das partidas
def criar_stats(fixtures):
    
    data = []

    for fixture in fixtures["id"][:2]:

        response = obter_dados(f"/fixtures/{fixture}/statistics")
        data.extend(response)

    df_stats = pd.json_normalize(data)

    stats = df_stats[
        [
            "id",
            "fixtureId",
            "teamId",
            "type",
            "value"
        ]
    ]

    stats = stats.drop_duplicates()

    return stats


# Criar o dataframe dos eventos das partidas
def criar_events(fixtures):

    data = []

    for fixture in fixtures["id"][:2]: #limitação de quantidade de execuções para teste | API tem limite de 100 requisições ao dia

        response = obter_dados(f"/fixtures/{fixture}/events")
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

    return events

# Criar dataframe das ligas/copas
def criar_leagues(df_leagues):

    leagues = df_leagues[
        [
            "id",
            "name",
            "type",
            "logo",
            "countryName"
        ]
    ]
    
    leagues = leagues.drop_duplicates()

    return leagues


# Criar o dataframe das temporadas
def criar_seasons(df_leagues)

    df_seasons = pd.json_normalize(df_leagues['seasons'].explode())

    seasons = df_seasons[
        [
            "leagueId",
            "year",
            "start",
            "end",
            "current"
        ]
    ]
    
    seasons = seasons.drop_duplicates()
    
    return seasons
