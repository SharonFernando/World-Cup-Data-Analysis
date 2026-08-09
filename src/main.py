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

# partidas
df_fixtures = carregar_endpoint("fixtures")
fixtures = criar_fixtures(df_fixtures)

# ligas
df_leagues = carregar_endpoint("leagues")
leagues = criar_leagues(df_leagues)

# temporadas
seasons = criar_seasons(df_leagues)

# times
teams = criar_teams(df_fixtures)

# estádios
venues = criar_venues(df_fixtures)

# jogadores
players = criar_players(teams)

# eventos
events = criar_events(df_fixtures)

# estatísticas das partidas
fixtures_stats = criar_stats(df_fixtures)

# inserir informações no banco de dados
load_dataframe(leagues,DB_TABLES['leagues'])
load_dataframe(seasons,DB_TABLES['seasons'])
load_dataframe(teams,DB_TABLES['teams'])
load_dataframe(venues,DB_TABLES['venues'])
load_dataframe(players,DB_TABLES['players'])
load_dataframe(fixtures,DB_TABLES['fixtures'])
load_dataframe(events,DB_TABLES['events'])
load_dataframe(fixtures_stats,DB_TABLES['fixtures_stats'])

print("Todas as operações foram concluídas")