import pandas as pd
import numpy as np

from utils.classes import Player
from data.data_db_functions import get_all_team_from_db

##########################################################################################################
### HELPER FUNCTIONS FOR THE FOOTBALL DATA ###
##########################################################################################################
'''
These functions carry out data manipulation
They do not use the Flaks API
They do not interact with the DB directly
'''

def join_team_name_with_id(player_df,team_name_dict):
    temp_dict = dict((v,k) for k,v in team_name_dict.items())
    player_df['team_id'] = player_df['team_name'].apply(lambda team_name :temp_dict.get(team_name))
    player_df['team_id'].astype(np.int64)
    return player_df

def create_player_objects(player_df: pd.DataFrame) -> list[Player]:
    '''
    Creates a list of player class objects from a dataframe
    '''
    players_list = []
    for i in player_df.index:
        player_to_add = Player(full_name=player_df['full_name'][i], 
                                team_id =int(player_df['team_id'][i]),
                                team_name = player_df['team_name'][i],
                                first_season=int(player_df['first_season'][i]),
                                last_season=int(player_df['last_season'][i])
                                )
        players_list.append(player_to_add)
    return players_list 

def add_cols_to_df(df: pd.DataFrame) -> pd.DataFrame:
    df['full_name'] = df['first_name'].map(str)+' '+df['last_name'].map(str)
    df['identifier'] = df['first_name'].map(str)+'-'+df['last_name'].map(str)+'-'+df['team_name'].map(str) 
    return df

def list_of_unique_player_teams(df: pd.DataFrame) -> list:
    '''
    Creates a list of unique players from all players df
    '''
    unique_player_teams: list = df['identifier'].unique()
    return unique_player_teams

def create_cleaned_player_df(player_df: pd.DataFrame, unique_player_teams: list) -> pd.DataFrame:
    '''
    Inputs: 
    1. Raw player df
    2. List of unique player teams (e.g. [Harry-Kane-Tottenham, ...])
    Outputs: Alphabetically sorted df with full name, team_name, first_season, last_season
    Note: No team_id at this stage
    '''
    cleaned_df = pd.DataFrame(columns=['full_name', 'team_name', 'first_season', 'last_season'])

    for player_team in unique_player_teams:
        split_player = player_team.split('-')
        team = split_player[-1]
        name = f'{split_player[0]} {split_player[1]}'
        temp_df = player_df[player_df['identifier'] == player_team]
        first_season = temp_df['season'].min()
        last_season = temp_df['season'].max()
        new_row = [name, team, first_season, last_season]
        cleaned_df.loc[len(cleaned_df)] = new_row

    sorted_df = cleaned_df.sort_values(['full_name'])
    return sorted_df

def add_team_id_to_df(player_df_without_team_id: pd.DataFrame)-> pd.DataFrame:
    '''
    Input: Player df without team_id (only team_name and seasons)
    Output: A new df with players and corresponding team ID
    '''
    all_teams_in_db_df: pd.DataFrame = get_all_team_from_db()
    team_dict = all_teams_dict_from_df(all_teams_in_db_df)
    team_df = pd.DataFrame.from_dict(team_dict,orient='index').reset_index()#, columns=['team_id','team'])
    team_df.columns = ['team_id','team_name']
    print(team_df.dtypes)
    player_df_with_team_id = player_df_without_team_id.merge(team_df, on = 'team_name', how='left')
    return player_df_with_team_id

def convert_players_list_to_df(player_list: list[dict]) -> pd.DataFrame:
    '''
    Input: player list from API 
    Output: Cleaned dataframe with players (no duplicates) with max and min seasons
    '''
    df = pd.DataFrame(player_list)
    # Adds full name and identifier column:
    player_df: pd.DataFrame = add_cols_to_df(df)
    # List of unique players
    unique_player_teams: list[str] = list_of_unique_player_teams(df)
    # Single entry with a max and min season per player
    cleaned_df = create_cleaned_player_df(player_df, unique_player_teams)
    print(cleaned_df)
    # Adds corresponding team ID to df from PG db
    cleaned_df_with_team_id = add_team_id_to_df(cleaned_df)
    print(cleaned_df_with_team_id)
    return cleaned_df_with_team_id 

def all_teams_dict_from_df(all_teams_df: pd.DataFrame) -> dict:
    '''
    Input: All teams from db as a df
    Output: Dictionay in this format {team_id: team_name}
    '''
    all_teams_df_name_id_only = all_teams_df[['team_name','team_id']]
    team_name_dict= all_teams_df_name_id_only.set_index('team_id')['team_name'].to_dict()
    return team_name_dict