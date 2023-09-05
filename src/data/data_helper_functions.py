import pandas as pd
import numpy as np

from utils.classes import Player
from data.data_db_functions import team_dict_from_db

##########################################################################################################
### HELPER FUNCTIONS FOR THE FOOTBALL DATA ###
##########################################################################################################
'''
These functions carry out data manipulation
They do not use the Flaks API
They do not interact with the DB directly
'''

def clean_team_names_data(player_df: pd.DataFrame) -> pd.DataFrame:
    player_df['team_name'] = player_df['team_name'].replace({
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
    return player_df

def join_team_name_with_id(player_df,team_name_dict):
    temp_dict = dict((v,k) for k,v in team_name_dict.items())
    player_df['team_id'] = player_df['team_name'].apply(lambda team_name :temp_dict.get(team_name))
    player_df['team_id'].astype(np.int64)
    return player_df

def create_player_objects(player_df) -> list(Player):
    players_list = []
    for i in player_df.index:
        player_to_add = Player(full_name=player_df['full_name'][i], 
                                team_id =int(player_df['team_id'][i]),
                                team_name = player_df['team_name'][i],
                                first_season=player_df['first_season'][i],
                                last_season=player_df['last_season'][i],
                                )
        players_list.append(player_to_add)
    return players_list 

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

def convert_player_list_to_obj(player_list):
    players = []
    for player in player_list:
        #TODO - get team Id and add in season column
        team_id = 1
        start_season = 2020
        end_season = 2022
        players.append(Player(first_name=player['first_name'], 
                              last_name=player['last_name'], 
                              team_id=team_id,
                              start_season=start_season,
                              end_season=end_season))
    return players