import pandas as pd
from utils.app_objects import Team, Player
from flask_pkg.project.routes import get_request, BASE

team_names = ['Arsenal',
                'Aston Villa',
                'Bournemouth',
                'Brentford',
                'Brighton & Hove Albion',
                'Chelsea',
                'Crystal Palace',
                'Everton',
                'Fulham',
                'Leeds',
                'Leicester City'
                'Liverpool',
                'Manchester City',
                'Manchester United',
                'Newcastle United',
                'Nottingham Forest',
                'Southampton',
                'Tottenham Hotspur',
                'West Ham United',
                'Wolverhampton Wanderers']

CURRENT_PREM_TEAMS =[Team(team_name=team, league='Premiership', country='England') for team in team_names]

#print(CURRENT_PREM_TEAMS)

#create a function that calls draws the teams from db's with unique ids. create db from the json get request with the ids.

prem_22_data = pd.read_csv("C:\\Users\\domsi\\OneDrive\\Documents\\fantasy-football\\season_22.csv")
prem_22_data = prem_22_data[['name','team']].drop_duplicates()

def team_dict_from_db():
    teams = get_request(BASE, 'get_all_football_teams')
    df = pd.DataFrame.from_dict(teams)
    df = df[['team_name','id']]
    team_name_dict = df.to_dict()
    return team_name_dict

def clean_players_data(df):
    df = prem_22_data[['name','team']].drop_duplicates()
    df = df.replace({
    "Bournemouth", "Bournemouth AFC",
    "Brentford", "Brentford",
    "Brighton": 'Brighton & Hove Albion',
    "Leeds":"Leeds United",
    "Leicester":"Leicester City",
    "Man City": "Manchester City",
    "Man Utd": "Manchester United",
    "Newcastle": "Newcastle United",
    "Nott'm Forest": "Nottingham Forest",
    "Spurs": "Tottenham Hotspur",
    "West Ham": "West Ham United",
    "Wolves": "Wolverhampton Wanderers"
})

