import pandas as pd
import numpy as np

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
        players_list.append(Player(full_name=player_df['full_name'][i], 
                                   first_season=player_df['first_season'][i],
                                   last_season=player_df['last_season'][i],
                                   team_name = player_df['team_name'][i],
                                   team_id =int(player_df['team_id'][i])))
    return players_list 