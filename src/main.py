from database import load_dataframe
from config import DB_TABLES
from transform import (
    carregar_endpoint, 
    criar_fixtures, 
    criar_teams, 
    criar_venues, 
    criar_players, 
    criar_events, 
    criar_stats, 
    criar_leagues, 
    criar_seasons
)


def main():

    try:
        df_fixtures = carregar_endpoint("fixtures")
        df_leagues = carregar_endpoint("leagues")
    except Exception as erro:
        print(f"Falha ao consultar dados iniciais da API: {erro}")
        return

    # ligas
    leagues = criar_leagues(df_leagues)
    load_dataframe(leagues, DB_TABLES['leagues'])

    # temporadas
    seasons = criar_seasons(df_leagues)
    load_dataframe(seasons, DB_TABLES['seasons'])

    # times
    teams = criar_teams(df_fixtures)
    load_dataframe(teams, DB_TABLES['teams'])

    # estádios
    venues = criar_venues(df_fixtures)
    load_dataframe(venues, DB_TABLES['venues'])

    # jogadores
    players = criar_players(teams)
    load_dataframe(players, DB_TABLES['players'])

    # partidas
    fixtures = criar_fixtures(df_fixtures)
    load_dataframe(fixtures, DB_TABLES['fixtures'])

    # eventos
    events = criar_events(fixtures)
    load_dataframe(events, DB_TABLES['events'])

    # estatísticas das partidas
    fixtures_stats = criar_stats(fixtures)
    load_dataframe(fixtures_stats, DB_TABLES['fixtures_stats'])

    print("Todas as operações foram concluídas")


if __name__ == "__main__":
    main()