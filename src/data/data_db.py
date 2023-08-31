import pandas as pd
import numpy as np
import json

from utils.app_objects import Team, Player # pylint: disable=import-error
from flask_pkg.project.routes import get_request, post_request, BASE # pylint: disable=import-error

def post_teams_to_db(teams: list[Team]):
    # Convert activities to json
    teams_array = [vars(team) for team in teams]       
    activitity_json_str = json.dumps(teams_array)
        
    # Post request
    teams_posted = post_request(BASE,"post_teams",activitity_json_str)
    print(f"New teams posted: {teams_posted}")
    return teams_posted

def post_players_to_db(players: list[Player]):
    # Convert activities to json
    players_array = [vars(player) for player in players]       
    activitity_json__players_str = json.dumps(players_array)
        
    # Post request
    players_posted = post_request(BASE,"post_players",activitity_json__players_str)
    print(f"New players posted: {players_posted}")
    return players_posted


def get_teams_from_db(limit):
    teams = get_request(BASE, f'get_football_teams/{limit}')
    df = pd.DataFrame.from_dict(teams)
    return df

def post_some_demo_teams():
    chelsea = Team(team_name='Chelsea', league='Premiership', country='England')
    tottenham = Team(team_name='Tottenham', league='Premiership', country='England')
    arsenal = Team(team_name='Arsenal', league='Premiership', country='England')
    teams_to_be_posted: Team = [chelsea, tottenham, arsenal]
    teams_posted = post_teams_to_db(teams_to_be_posted)

def post_some_demo_players():
    sterling = Player(first_name='Raheem', last_name='Sterling', team_id='7')
    kane = Player(first_name='Harry', last_name='Kane', team_id='18')
    players_to_be_posted: Player = [sterling, kane]
    players_posted = post_players_to_db(players_to_be_posted)


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

def team_dict_from_db():
    teams = get_request(BASE, 'get_all_football_teams')
    df = pd.DataFrame.from_dict(teams)
    df['id'] = df.index +1
    df = df[['team_name','id']]
    team_name_dict= df.set_index('id')['team_name'].to_dict()
    return team_name_dict

def clean_players_data(player_df):
    player_df = player_df[['name','team']].drop_duplicates().replace({
    "Bournemouth": "Bournemouth AFC",
    "Brentford": "Brentford",
    "Brighton": 'Brighton & Hove Albion',
    # "Leeds":"Leeds United",
    "Leicester":"Leicester City",
    "Man City": "Manchester City",
    "Man Utd": "Manchester United",
    "Newcastle": "Newcastle United",
    "Nott'm Forest": "Nottingham Forest",
    "Spurs": "Tottenham Hotspur",
    "West Ham": "West Ham United",
    "Wolves": "Wolverhampton Wanderers"
    })
    player_df[['first_name','last_name']] = player_df["name"].str.split(" ", n = 1, expand = True)
    player_df = player_df.drop(columns = ['name'])
    return player_df

def join_team_name_with_id(player_df,team_name_dict):
    temp_dict = dict((v,k) for k,v in team_name_dict.items())
    player_df['team_id'] = player_df['team'].apply(lambda team_name :temp_dict.get(team_name))
    player_df['team_id'].astype(np.int64)
    return player_df

def create_player_objects(player_df):
    players_list = []
    for i in player_df.index:
        players_list.append(Player(first_name=player_df['first_name'][i], last_name=player_df['last_name'][i], team_id =int(player_df['team_id'][i])))
    return players_list  

def total_player_process():
    prem_22_data = pd.read_csv("C:\\Users\\domsi\\OneDrive\\Documents\\fantasy-football\\season_22.csv")
    team_name_dict = team_dict_from_db()
    player_df = clean_players_data(prem_22_data)
    #print(player_df.head())
    player_df = join_team_name_with_id(player_df,team_name_dict).reset_index(drop=True)
    #print(player_df.head())
    players_22_23 = create_player_objects(player_df)
    post_players_to_db(players_22_23)

def main():
    pass
    
if __name__ == "__main__":
    main()