import time
import requests
import pandas as pd
from api import obter_dados
from database import get_existing_ids


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

    venues = venues.dropna(subset=["id"])
    venues = venues.drop_duplicates()

    return venues


# Criar o dataframe dos jogadores
def criar_players(teams):

    existing_team_ids = get_existing_ids(
        "dim_players",
        "teamId"
    )

    teams_to_request = teams[
        ~teams["id"].isin(existing_team_ids)
    ]

    print(
        f"Times para consultar jogadores: "
        f"{len(teams_to_request)}"
    )

    data = []

    for team in teams_to_request["id"]:

        try:
            response = obter_dados(
                f"/squads?team={team}"
            )
            data.extend(response)
        except requests.exceptions.HTTPError as erro:
            if erro.response is not None and erro.response.status_code == 429:
                print("Limite de requisições da API atingido (429). Interrompendo consultas de jogadores.")
                break
            print(f"Falha ao consultar jogadores do time {team}: {erro}")
        except Exception as erro:
            print(f"Falha ao consultar jogadores do time {team}: {erro}")

        time.sleep(1)

    if not data:
        return pd.DataFrame(
            columns=[
                "id",
                "name",
                "teamId",
                "position"
            ]
        )

    df_squad = pd.json_normalize(data)

    players = df_squad[
        [
            "playerId",
            "player.name",
            "teamId",
            "position"
        ]
    ]

    players.columns = [
        "id",
        "name",
        "teamId",
        "position"
    ]

    players = players.drop_duplicates()

    return players


# Criar o dataframe das estatísticas das partidas
def criar_stats(fixtures):

    existing_fixture_ids = get_existing_ids(
        "fact_stats",
        "fixtureId"
    )

    fixtures_to_request = fixtures[
        ~fixtures["id"].isin(existing_fixture_ids)
    ]

    print(
        f"Fixtures para consultar estatísticas: "
        f"{len(fixtures_to_request)}"
    )

    data = []

    for fixture in fixtures_to_request["id"][:25]:

        try:
            response = obter_dados(
                f"/fixtures/{fixture}/statistics"
            )
            data.extend(response)
        except requests.exceptions.HTTPError as erro:
            if erro.response is not None and erro.response.status_code == 429:
                print("Limite de requisições da API atingido (429). Interrompendo consultas de estatísticas.")
                break
            print(f"Falha ao consultar estatísticas da fixture {fixture}: {erro}")
        except Exception as erro:
            print(f"Falha ao consultar estatísticas da fixture {fixture}: {erro}")

        time.sleep(1)

    if not data:
        return pd.DataFrame(
            columns=[
                "id",
                "fixtureId",
                "teamId",
                "type",
                "value"
            ]
        )

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

    existing_fixture_ids = get_existing_ids(
        "fact_events",
        "fixtureId"
    )

    fixtures_to_request = fixtures[
        ~fixtures["id"].isin(existing_fixture_ids)
    ]

    print(
        f"Fixtures para consultar eventos: "
        f"{len(fixtures_to_request)}"
    )

    data = []

    for fixture in fixtures_to_request["id"][:25]:

        try:
            response = obter_dados(
                f"/fixtures/{fixture}/events"
            )
            data.extend(response)
        except requests.exceptions.HTTPError as erro:
            if erro.response is not None and erro.response.status_code == 429:
                print("Limite de requisições da API atingido (429). Interrompendo consultas de eventos.")
                break
            print(f"Falha ao consultar eventos da fixture {fixture}: {erro}")
        except Exception as erro:
            print(f"Falha ao consultar eventos da fixture {fixture}: {erro}")

        time.sleep(1)

    if not data:
        return pd.DataFrame(
            columns=[
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
        )

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
def criar_seasons(df_leagues):

    df_seasons = pd.json_normalize(df_leagues['seasons'].explode())

    seasons = df_seasons[
        [
            "leagueId",
            "year",
            "start",
            "end"
        ]
    ]
    
    seasons = seasons.drop_duplicates()
    
    return seasons