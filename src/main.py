from transform import carregar_endpoint, criar_fixtures, criar_teams, criar_venues, criar_players, criar_events, criar_stats

# partidas
df_fixtures = carregar_endpoint("fixtures")
fixtures = criar_fixtures(df_fixtures)

# times
teams = criar_teams(df_fixtures)

# estádios
venues = criar_venues(df_fixtures)

# jogadores
df_players = carregar_endpoint("players")
players = criar_players(df_players)

# estatísticas
fixtures_stats = criar_stats(df_fixtures)

# eventos
events = criar_events(df_fixtures)

# leagues
df_leagues = carregar_endpoint("leagues")
leagues = criar_leagues(df_leagues)

# seasons
seasons = criar_seasons(df_leagues)
