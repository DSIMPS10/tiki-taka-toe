import pandas as pd
import ssl
import os

from utils.classes import Player
from data.data_db_functions import (post_players_to_db,
                                    update_player_first_season_in_db,
                                    update_player_last_season_in_db,
                                    get_all_players_from_db)
from data.data_helper_functions import(convert_players_list_to_df,
                                    create_player_objects,
                                    all_teams_dict_from_df)
from data.footy_api_functions import (get_all_players_for_a_season)
from data.transfermrkt_api_functions import (get_squad_from_team_id, get_teams_from_season_year)
from utils.cert_helpers import (fixing_SSL_error)
#from data.season_data.season_2021 import PLAYERS_21

##########################################################################################################
### PLAYERS ###
##########################################################################################################

def get_all_players_for_season(season: int, league_id) -> list[dict]:
    teams = get_teams_from_season_year(season, league_id)
    all_players_for_season = []
    for team_name,team_id in teams.items():
       all_players_for_season += get_squad_from_team_id(team_name,team_id,season)
    all_players_for_season = split_nationality_and_team(all_players_for_season)
    return all_players_for_season


def split_nationality_and_team(players_for_season:list[dict]) -> list[dict]:
    all_players: list[dict] = []

    
    #{'full_name': 'Thiago Silva', 'team_name': 'Brazil', 'season': 2022}
    for player in players_for_season:
        individual_player_club_dict = {}
        individual_player_club_dict['full_name'] = player['full_name']
        individual_player_club_dict['team_name'] = player['team_name']
        individual_player_club_dict['season'] = player['season']

        individual_player_nationality_dict = {}
        individual_player_nationality_dict['full_name'] = player['full_name']
        individual_player_nationality_dict['team_name'] = player['nationality']
        individual_player_nationality_dict['season'] = player['season']

        all_players.append(individual_player_club_dict)
        all_players.append(individual_player_nationality_dict)

    return all_players
        

def add_players_to_db_process(season: int, league_id: str):
    '''
    Full process to add a list of players to the database
    Step 1: Get data
    Step 2: Clean data
    Step 3: Check if player needs to be added
    Step 4: Create player list
    Step 5: Post list to db
    '''

    #1. Get list of players from football API 
    all_players_for_single_season: list = get_all_players_for_season(season, league_id)
    season_df = pd.DataFrame(all_players_for_single_season) 
    try:
        season_df.to_csv(f".\src\data\season_data\season_{season}.csv")
    except Exception as e:
        print("Couldn't save csv, likely a path error")
    finally:
        pass

    #2. Create a cleaned players df from list 
    players_df: pd.DataFrame = convert_players_list_to_df(all_players_for_single_season) #
    # print(f'Players of the {season} season to be checked:{players_df}')
    
    #3. Get a dataframe of all players already in db and loop through each new player
    all_players_in_db_df = get_all_players_from_db()
    all_players_in_db_df['identifier'] = all_players_in_db_df['full_name'].map(str)+'~'+all_players_in_db_df['team_name'].map(str)
    players_to_upload_to_db_df = pd.DataFrame(columns=['full_name', 'team_name', 'first_season', 'last_season', 'team_id'])

    for i in range(len(players_df)): 
        # Create a df for each row of the new season players
        single_player_df = players_df.iloc[[i]]
        # Create an identifier for each player for new season
        single_player_identifier = single_player_df['full_name'].map(str)+'~'+single_player_df['team_name'].map(str)
        single_player_identifier = single_player_identifier.values[-1]
        # First check for player and team combo
        combo_match_df = all_players_in_db_df.loc[all_players_in_db_df['identifier'].isin([single_player_identifier])]
        # combo_match_df = all_players_in_db_df.loc[all_players_in_db_df['identifier']==single_player_identifier]
        print(f"Match df: {combo_match_df}")
        # If combo_match_df is empty then the player team combo doesn't exist and the player needs to be added
        if combo_match_df.empty:
            print(f"This player to be added: {single_player_df}")
            # Add player to list of players to be added
            players_to_upload_to_db_df: pd.DataFrame = pd.concat([players_to_upload_to_db_df,single_player_df]).reset_index(drop=True)
            print(players_to_upload_to_db_df)
        elif len(combo_match_df)  == 1:
            # The season needs to be updated
            new_season_data = update_player_last_season_in_db(single_player_identifier,season)
            print(f'Season info to be updated: {new_season_data}')
        elif len(combo_match_df)  > 1:
            # There is a duplicate ERROR
            print(f"Investigate duplicate error for {single_player_identifier} & {season}")

    #4. Create Player object list
    players_to_post: list[Player] = create_player_objects(players_to_upload_to_db_df)
    print(f'players to be posted: {players_to_post}')

    #6. Post players to db
    players_posted = post_players_to_db(players_to_post)
    print(f'Players posted: {players_posted}')
    return players_posted


def main():
    add_players_to_db_process(2007,'GB1')


if __name__ == "__main__":
    main()
