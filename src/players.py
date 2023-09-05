import pandas as pd

from utils.classes import Player
from data.data_db_functions import (team_dict_from_db, 
                                    run_player_cleaning_process,
                                    create_player_objects,
                                    post_players_to_db
)

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
    players_list = [{'first_name': 'Patson', 'last_name': 'Daka', 'team_name': 'Leicester', 'season': 2021}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team_name': 'Arsenal', 'season': 2021}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team_name': 'Wolves', 'season': 2021}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team_name': 'Everton', 'season': 1999},
        {'first_name': 'Patson', 'last_name': 'Daka', 'team_name': 'Leicester', 'season': 2020}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team_name': 'Arsenal', 'season': 2015}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team_name': 'Everton', 'season': 2004}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team_name': 'Everton', 'season': 1996},
        {'first_name': 'Patson', 'last_name': 'Daka', 'team_name': 'Leicester', 'season': 2019}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team_name': 'Tottenham', 'season': 2010}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team_name': 'Everton', 'season': 2003}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team_name': 'Liverpool', 'season': 1995},
        {'first_name': 'Patson', 'last_name': 'Daka', 'team_name': 'Chelsea', 'season': 1995}, {'first_name': 'Emile', 'last_name': 'Smith Rowe', 'team_name': 'Tottenham', 'season': 2005}, {'first_name': 'Daniel', 'last_name': 'Castelo Podence', 'team_name': 'Everton', 'season': 2003}, {'first_name': 'José Salomón', 'last_name': 'Rondón Giménez', 'team_name': 'Liverpool', 'season': 1993}]

    #2. Create a cleaned player df from list 
    team_name_dict = team_dict_from_db()
    player_df: pd.DataFrame = run_player_cleaning_process(players_list)
    
    #3. Create Player object list
    players_to_post: list[Player] = create_player_objects(player_df)
    print(players_to_post)

    #4. Post players to db
    players_posted = post_players_to_db(players_to_post)
    return players_posted

def get_players_from_db_process():
    '''
    Full process to get player data from db
    By either team, league, id, name
    '''
    pass

def main():
    pass

if __name__ == "__main__":
    main()
