# imports
import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()

# request auth
API_KEY = os.getenv('API_KEY')
HEADERS = {
  'x-api-key': API_KEY,
  'Content-Type': 'application/json',
}

# set your subscription
# can be paid or free
MY_PLAN = 'free'
# MY_PLAN = 'paid'

API_DOMAIN = 'https://www.crunchtimeodds.com/api'
API_ENDPOINT = f'{API_DOMAIN}/v1'

if MY_PLAN == 'paid':
  # privileged endpoints
  API_ENDPOINT += '/adv'

# api endpoints
HEALTH_ENDPOINT = f'{API_DOMAIN}/health'
SITES_ENDPOINT = f'{API_DOMAIN}/v1/sites'
TEAMS_ENDPOINT = f'{API_DOMAIN}/v1/teams'
GAMEIDS_ENDPOINT = f'{API_ENDPOINT}/games/ids'
ML_ENDPOINT = f'{API_ENDPOINT}/ml'
OU_ENDPOINT = f'{API_ENDPOINT}/ou'
PS_ENDPOINT = f'{API_ENDPOINT}/ps'

def pretty_print_odds(j, t):
  """ pretty print odds data """
  print(
    f"[{t.upper()} ODDS UPDATE {datetime.datetime.fromtimestamp(j['updated_at'])}] "+
    f"{j['league'].upper()} | "+
    f"{j['game_id']} | "+
    f"{j['site_id']} | "+
    f"{j['t1_id'].replace(j['league']+'-','')} {j['t1_odds']} | "+
    f"{j['t2_id'].replace(j['league']+'-','')} {j['t2_odds']}"
  )

def get_health():
  """ health check """
  resp = requests.get(HEALTH_ENDPOINT, headers=HEADERS)
  if (resp.status_code == 200):
    print(f"[HEALTH] {resp.json()}")

def get_teams():
  """ all teams """
  teams = []
  resp = requests.get(TEAMS_ENDPOINT, headers=HEADERS)
  if (resp.status_code == 200):
    teams = [d['team_id'] for d in resp.json()]
  print(f"[TEAMS] {len(teams)} teams found")
  return teams

def get_sites():
  """ all sites """
  sites = []
  resp = requests.get(SITES_ENDPOINT, headers=HEADERS)
  if (resp.status_code == 200):
    sites = [d['site_id'] for d in resp.json()]
  print(f"[SITES] {len(sites)} sites found")
  return sites

def get_game_ids(n_pages=2):
  """ game ids for page(s) """
  game_ids = []
  for page in range(0,n_pages):
    pg = page * 10
    resp = requests.get(
      f'{GAMEIDS_ENDPOINT}?page={pg}',
      headers=HEADERS
    )
    if (resp.status_code == 200):
      print(f"[GAME IDS] page = {page} | found {len(resp.json())} items")
      game_ids.extend([d['game_id'] for d in resp.json()])
  print(f"[GAME IDS] {len(game_ids)} game ids found in {n_pages} pages")
  return game_ids

def print_ml_data(n_pages=1):
  """ moneyline data for page(s) """
  for page in range(0,n_pages):
    pg = page * 10
    resp = requests.get(
      f'{ML_ENDPOINT}?page={pg}',
      headers=HEADERS
    )
    if (resp.status_code == 200):
      for d in resp.json():
        pretty_print_odds(d, 'ml')

def print_ou_data(n_pages=1):
  """ over under data for page(s) """
  for page in range(0,n_pages):
    pg = page * 10
    resp = requests.get(
      f'{OU_ENDPOINT}?page={pg}',
      headers=HEADERS
    )
    if (resp.status_code == 200):
      for d in resp.json():
        pretty_print_odds(d, 'ou')

def print_ps_data(n_pages=1):
  """ point spread data for page(s) """
  for page in range(0,n_pages):
    pg = page * 10
    resp = requests.get(
      f'{PS_ENDPOINT}?page={pg}',
      headers=HEADERS
    )
    if (resp.status_code == 200):
      for d in resp.json():
        pretty_print_odds(d, 'ps')

if __name__ == '__main__':
  get_health()
  teams = get_teams()
  sites = get_sites()
  game_ids = get_game_ids()
  print('-'*50)
  print_ml_data()
  print('-'*50)
  print_ou_data()
  print('-'*50)
  print_ps_data()
  print('-'*50)