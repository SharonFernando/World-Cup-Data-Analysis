import os
from dotenv import load_dotenv

# Leitura do arquivo .env
load_dotenv()

API_KEY = os.getenv('KICK_OFF_API_KEY')

# Dicionário com as variáveis do arquivo .env
HEADERS = {
    "x-api-key": API_KEY
    }

# Dicionário com os parâmetros de requisição da API
PARAMS = {
    'teams' : {
        'league': 1,
        'season': 2026
    },
    'fixtures': {
        'league': 1,
        'season': 2026
    }
}

# Dicionário com os endpoints da API
ENDPOINTS = {
    'countries': 'https://app.kickoffapi.com/api/v1/countries',
    'leagues': 'https://app.kickoffapi.com/api/v1/leagues',
    'teams': 'https://app.kickoffapi.com/api/v1/teams',
    'team_logos': 'https://app.kickoffapi.com/api/v1/teams/logos',
    'fixtures': 'https://app.kickoffapi.com/api/v1/fixtures',
    'fixtures_events': 'https://app.kickoffapi.com/api/v1/fixtures/:id/events',
    'fixtures_lineups': 'https://app.kickoffapi.com/api/v1/fixtures/:id/lineups',
    'fixtures_statistics': 'https://app.kickoffapi.com/api/v1/fixtures/:id/statistics',
    'fixtures_players': 'https://app.kickoffapi.com/api/v1/fixtures/:id/players',
    'standings': 'https://app.kickoffapi.com/api/v1/standings',
    'players': 'https://app.kickoffapi.com/api/v1/players',
    'odds': 'https://app.kickoffapi.com/api/v1/odds',
    'odds_live': 'https://app.kickoffapi.com/api/v1/odds/live',
    'predictions': 'https://app.kickoffapi.com/api/v1/predictions',
    'injuries': 'https://app.kickoffapi.com/api/v1/injuries',
    'transfers': 'https://app.kickoffapi.com/api/v1/transfers',
    'trophies': 'https://app.kickoffapi.com/api/v1/trophies',
    'coachs': 'https://app.kickoffapi.com/api/v1/coaches',
    'venues': 'https://app.kickoffapi.com/api/v1/venues',
    'bookmakers': 'https://app.kickoffapi.com/api/v1/bookmakers',
    'bet_types': 'https://app.kickoffapi.com/api/v1/bet-types',
    'team_statistics': 'https://app.kickoffapi.com/api/v1/team-statistics',
    'status': 'https://app.kickoffapi.com/api/v1/account/status'
    }