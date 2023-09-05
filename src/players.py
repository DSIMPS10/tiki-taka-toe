import pandas as pd

from utils.classes import Player
from data.data_db_functions import ( post_players_to_db)
from data.data_helper_functions import(convert_players_list_to_df,
                                    create_player_objects,
                                    all_teams_dict_from_df)
from data.footy_api_functions import (get_all_players_for_a_season)

##########################################################################################################
### PLAYERS ###
##########################################################################################################

def add_players_to_db_process():
    '''
    Full process to add a list of players to the database
    Step 1: Get data
    Step 2: Clean data
    Step 3: Create player list
    Step 4: Post list to db
    '''

    #1. Get list of players from football API 
    season = 2023
    prem_league = 39
    all_players_for_single_season: list = get_all_players_for_a_season(season, prem_league)

    #2. Create a cleaned player df from list 
    player_df: pd.DataFrame = convert_players_list_to_df(all_players_for_single_season)
    print(player_df)
    
    #3. Create Player object list
    players_to_post: list[Player] = create_player_objects(player_df)
    print(players_to_post)

    #4. Post players to db
    players_posted = post_players_to_db(players_to_post)
    print(players_posted)
    return players_posted

def get_players_from_db_process():
    '''
    Full process to get player data from db
    By either team, league, id, name
    '''
    pass

def main():
    add_players_to_db_process()

if __name__ == "__main__":
    main()
