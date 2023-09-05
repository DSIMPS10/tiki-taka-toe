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
    # all_players_for_single_season: list = get_all_players_for_a_season()
    players_list = [{'first_name': 'Patson', 'last_name': 'Daka', 'team_name': 'Leicester', 'season': 2021}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team_name': 'Arsenal', 'season': 2021}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team_name': 'Wolves', 'season': 2021}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team_name': 'Everton', 'season': 1999},
        {'first_name': 'Patson', 'last_name': 'Daka', 'team_name': 'Leicester', 'season': 2020}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team_name': 'Arsenal', 'season': 2015}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team_name': 'Everton', 'season': 2004}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team_name': 'Everton', 'season': 1996},
        {'first_name': 'Patson', 'last_name': 'Daka', 'team_name': 'Leicester', 'season': 2019}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team_name': 'Tottenham', 'season': 2010}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team_name': 'Everton', 'season': 2003}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team_name': 'Liverpool', 'season': 1995},
        {'first_name': 'Patson', 'last_name': 'Daka', 'team_name': 'Chelsea', 'season': 1995}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team_name': 'Tottenham', 'season': 2005}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team_name': 'Everton', 'season': 2003}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team_name': 'Liverpool', 'season': 1993}]

    #2. Create a cleaned player df from list 
    # team_name_dict = all_teams_dict_from_df()
    player_df: pd.DataFrame = convert_players_list_to_df(players_list)
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
