import pandas as pd
import numpy as np
import json

from utils.classes import Team, Player # pylint: disable=import-error
from flask_pkg.project.routes import get_request, post_request, BASE # pylint: disable=import-error

##########################################################################################################
### FUNCTION TO INTERACT WITH PG DATABASE ###
##########################################################################################################
'''
These functions all use the Flask API to interact with the PG database
They are main POST and GET requestios
'''

##########################################################################################################
### POST DATA ###
##########################################################################################################

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

def post_some_demo_teams():
    chelsea = Team(team_name='Chelsea', league='Premiership', country='England')
    tottenham = Team(team_name='Tottenham', league='Premiership', country='England')
    arsenal = Team(team_name='Arsenal', league='Premiership', country='England')
    teams_to_be_posted: Team = [chelsea, tottenham, arsenal]
    teams_posted = post_teams_to_db(teams_to_be_posted)

# def post_some_demo_players():
#     sterling = Player(first_name='Raheem', last_name='Sterling', team_id='7')
#     kane = Player(first_name='Harry', last_name='Kane', team_id='18')
#     players_to_be_posted: Player = [sterling, kane]
#     players_posted = post_players_to_db(players_to_be_posted)
    
##########################################################################################################
### GET DATA FROM DB ###
##########################################################################################################

def get_teams_from_db(limit):
    teams = get_request(BASE, f'get_football_teams/{limit}')
    df = pd.DataFrame.from_dict(teams)
    return df

def team_dict_from_db():
    teams = get_request(BASE, 'get_all_football_teams')
    df = pd.DataFrame.from_dict(teams)
    df['id'] = df.index +1
    df = df[['team_name','id']]
    team_name_dict= df.set_index('id')['team_name'].to_dict()
    return team_name_dict


 

def add_cols_to_df(df: pd.DataFrame) -> pd.DataFrame:
    df['full_name'] = df['first_name'].map(str)+' '+df['last_name'].map(str)
    df['identifier'] = df['first_name'].map(str)+'-'+df['last_name'].map(str)+'-'+df['team_name'].map(str) 
    return df

def list_of_unique_player_teams(df: pd.DataFrame) -> list:
    unique_player_teams: list = df['identifier'].unique()
    return unique_player_teams

def create_cleaned_player_df(df: pd.DataFrame, unique_player_teams: list) -> pd.DataFrame:
    cleaned_df = pd.DataFrame(columns=['full_name', 'team_name', 'first_season', 'last_season'])

    for player_team in unique_player_teams:
        split_player = player_team.split('-')
        team = split_player[-1]
        name = f'{split_player[0]} {split_player[1]}'
        temp_df = df[df['identifier'] == player_team]
        first_season = temp_df['season'].min()
        last_season = temp_df['season'].max()
        new_row = [name, team, first_season, last_season]
        cleaned_df.loc[len(cleaned_df)] = new_row

    sorted_df = cleaned_df.sort_values(['full_name'])
    return sorted_df

def add_team_id_to_df(df: pd.DataFrame)-> pd.DataFrame:
    team_dict = team_dict_from_db()
    team_df = pd.DataFrame.from_dict(team_dict,orient='index').reset_index()#, columns=['team_id','team'])
    team_df.columns = ['team_id','team_name']
    print(team_df.dtypes)
    print(df.dtypes)
    df = df.merge(team_df, on = 'team_name', how='left')
    return df

def run_player_cleaning_process(player_list: list) -> pd.DataFrame:

    df = pd.DataFrame(player_list)
    player_df = add_cols_to_df(df)
    unique_player_teams = list_of_unique_player_teams(df)
    cleaned_df = create_cleaned_player_df(player_df, unique_player_teams)
    cleaned_df = add_team_id_to_df(cleaned_df)
    return cleaned_df

def main():
    pass
    
if __name__ == "__main__":
    main()