from database import load_dataframe, get_existing_ids, get_existing_pairs
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
    existing_league_ids = get_existing_ids(DB_TABLES['leagues'], "id")
    leagues = leagues[~leagues["id"].isin(existing_league_ids)]
    load_dataframe(leagues, DB_TABLES['leagues'])

    # temporadas
    seasons = criar_seasons(df_leagues)
    existing_seasons = get_existing_pairs(DB_TABLES['seasons'], "leagueId", "year")
    seasons = seasons[
        ~seasons.apply(lambda row: (row["leagueId"], row["year"]) in existing_seasons, axis=1)
    ]
    load_dataframe(seasons, DB_TABLES['seasons'])

    # times
    teams = criar_teams(df_fixtures)
    existing_team_ids = get_existing_ids(DB_TABLES['teams'], "id")
    teams_to_load = teams[~teams["id"].isin(existing_team_ids)]
    load_dataframe(teams_to_load, DB_TABLES['teams'])

    # estádios
    venues = criar_venues(df_fixtures)
    existing_venue_ids = get_existing_ids(DB_TABLES['venues'], "id")
    venues = venues[~venues["id"].isin(existing_venue_ids)]
    load_dataframe(venues, DB_TABLES['venues'])

    # jogadores
    players = criar_players(teams)
    load_dataframe(players, DB_TABLES['players'])

    # partidas
    fixtures = criar_fixtures(df_fixtures)
    existing_fixture_ids = get_existing_ids(DB_TABLES['fixtures'], "id")
    fixtures_to_load = fixtures[~fixtures["id"].isin(existing_fixture_ids)]
    load_dataframe(fixtures_to_load, DB_TABLES['fixtures'])

    # eventos
    events = criar_events(fixtures)
    load_dataframe(events, DB_TABLES['events'])

    # estatísticas das partidas
    fixtures_stats = criar_stats(fixtures)
    load_dataframe(fixtures_stats, DB_TABLES['fixtures_stats'])

    print("Todas as operações foram concluídas")


if __name__ == "__main__":
    main()