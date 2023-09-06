import pandas as pd
import ssl
import os

from utils.classes import Player
from data.data_db_functions import ( post_players_to_db)
from data.data_helper_functions import(convert_players_list_to_df,
                                    create_player_objects,
                                    all_teams_dict_from_df)
from data.footy_api_functions import (get_all_players_for_a_season)
from utils.cert_helpers import (fixing_SSL_error)

##########################################################################################################
### PLAYERS ###
##########################################################################################################

def add_players_to_db_process():
    '''
    Full process to add a list of players to the database
    Step 1: Get data
    Step 2: Clean data
    Step 3: Check if player needs to be added
    Step 4: Create player list
    Step 5: Post list to db
    '''

    #1. Get list of players from football API 
    season = 2023
    prem_league = 39
    all_players_for_single_season: list = get_all_players_for_a_season(season, prem_league)

    #2. Create a cleaned players df from list 
    players_df: pd.DataFrame = convert_players_list_to_df(all_players_for_single_season)
    print(players_df)
    
    #3. Get a dataframe of all players already in db and loop through each new player
    all_players_in_db_df = pd.DataFrame()
    all_players_in_db_df['identifier'] = all_players_in_db_df['name'].map(str)+' '+all_players_in_db_df['team_name'].map(str)
    
    for i in range(len(players_df)): 
        # Create a df for each row of the new season players
        single_player_df = players_df.iloc[[i]]
        # Create an identifier for each player for new season
        single_player_identifier = single_player_df['name'].map(str)+' '+single_player_df['team_name'].map(str)
        # First check for player and team combo
        combo_match_df = all_players_in_db_df[all_players_in_db_df['identifier'] == single_player_identifier]
        # If combo_match_df is empty then the player team combo doesn't exist and the player needs to be added
        if combo_match_df.empty:
            # Add player to list of players to be added
            continue
        elif len(combo_match_df)  == 1:
            # The season needs to be updated
            continue
        elif len(combo_match_df)  > 1:
            # There is a duplicate ERROR
            print()
        else:
            # See if the player already exists for different team
            player_match_df = all_players_in_db_df[all_players_in_db_df['name'] == single_player_df['name']]
        
        # Second check if player exists for different team
    
    #4. Check if player is already in DB, if yes update season info, if not add
    # Will return true if player needs to be added and false if players has been updated
    checked_player = check_if_player_is_in_db(all_players_in_db_df)
    
    #5. Create Player object list
    players_to_post: list[Player] = create_player_objects(player_df)
    print(players_to_post)

    #6. Post players to db
    players_posted = post_players_to_db(players_to_post)
    print(players_posted)
    return players_posted

def get_players_from_db_process():
    '''
    Full process to get player data from db
    By either team, league, id, name
    '''
    pass


def check_if_player_is_in_db(all_players_in_db_df: pd.DataFrame, new_player_df: pd.DataFrame):
    pass


def main():
    add_players_to_db_process()

if __name__ == "__main__":
    main()
