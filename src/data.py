import pandas as pd
import numpy as np
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



def team_dict_from_db():
    teams = get_request(BASE, 'get_all_football_teams')
    df = pd.DataFrame.from_dict(teams)
    df['id'] = df.index
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
    player_df.to_csv("C:\\Users\\domsi\\OneDrive\\Documents\\fantasy-football\\test_csv")
    player_df['team_id'].astype(np.int64)
    return player_df

def create_player_objects(player_df):
    players_list = []
    for i in player_df.index:
        players_list.append(Player(first_name=player_df['first_name'][i], last_name=player_df['last_name'][i], team_id =player_df['team_id'][i]))
    return players_list  

def main():
    prem_22_data = pd.read_csv("C:\\Users\\domsi\\OneDrive\\Documents\\fantasy-football\\season_22.csv")
    team_name_dict = team_dict_from_db()
    player_df = clean_players_data(prem_22_data)
    #print(player_df.head())
    player_df = join_team_name_with_id(player_df,team_name_dict).reset_index(drop=True)
    #print(player_df.head())
    players_22_23 = create_player_objects(player_df)
    print(players_22_23)
    print(type(players_22_23[0]))
    
if __name__ == "__main__":
    main()