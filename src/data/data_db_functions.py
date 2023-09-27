import pandas as pd
import json

from utils.classes import Team, Player , Guess, FootyGrid
from flask_pkg.project.routes import get_request, post_request,put_request, BASE 


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

#### TEAMS ####

def post_teams_to_db(teams: list[Team]):
    # Convert activities to json
    teams_array = [vars(team) for team in teams]       
    teams_json_str = json.dumps(teams_array)
        
    # Post request
    teams_posted = post_request(BASE,"post_teams",teams_json_str)
    print(f"New teams posted: {teams_posted}")
    return teams_posted

#### PLAYERS ####

def post_players_to_db(players: list[Player]):
    # Convert players to json
    players_array = [vars(player) for player in players] 
    players_json_str = json.dumps(players_array)  
    # Post request
    players_posted = post_request(BASE,"post_players",players_json_str)
    print(f"New players posted: {players_posted}")
    return players_posted

def post_valid_player_combos(valid_player_combos: list[Guesses]):
    # Convert valid players to json
    valid_player_combos_array = [vars(player_combo) for player_combo in valid_player_combos] 
    player_json_str = json.dumps(valid_player_combos_array)  
    # Post request
    valid_player_combos_posted = post_request(BASE,"post_valid_player_combos",player_json_str)
    print(f"New player combos posted: {valid_player_combos_posted}")
    return valid_player_combos_posted

#### GRIDS ####

def post_valid_grids(valid_grids: list[FootyGrid]):
    # Convert valid players to json
    valid_grids_array = [vars(grid) for grid in valid_grids]
    grids_json_str = json.dumps(valid_grids_array)  
    # Post request
    valid_grid_posted = post_request(BASE,"post_grids",grids_json_str)
    print(f"New Grid posted: {valid_grid_posted}")
    return valid_grid_posted

#### GUESSES ####

def post_guess_to_db(guesses: list[Guess]):
    # Convert guess to json
    guess_array = [vars(guess) for guess in guesses] 
    guess_json_str = json.dumps(guess_array)  
    # Post request
    guess_posted = post_request(BASE,"post_new_guess",guess_json_str)
    print(f"New guess posted: {guess_posted}")
    return guess_posted


##########################################################################################################
### GET DATA FROM DB ###
##########################################################################################################

#### TEAMS ####

def get_teams_from_db(limit: int) -> pd.DataFrame:
    teams = get_request(BASE, f'get_football_teams/{limit}')
    df = pd.DataFrame.from_dict(teams)
    return df

def get_all_team_from_db() -> pd.DataFrame:
    all_teams = get_request(BASE, f'get_all_football_teams')
    df = pd.DataFrame.from_dict(all_teams)
    return df

#### GUESSES ####

def get_all_guesses_from_db() -> pd.DataFrame:
    all_guesses = get_request(BASE, f'get_players_from_guesses_table')
    all_guesses_df = pd.DataFrame.from_dict(all_guesses)
    return all_guesses_df


def get_valid_guesses_from_db()->list[str]:
    all_valid_guesses = get_request(BASE, f'get_all_valid_player_guesses')
    return all_valid_guesses

#### PLAYERS ####

def get_all_players_from_db() -> pd.DataFrame:
    all_players = get_request(BASE, f'get_all_players')
    players_df = pd.DataFrame.from_dict(all_players)
    return players_df

def get_player_info_from_name_db(full_name: str):
    player_info = get_request(BASE, f'get_player_info_from_name/{full_name}')
    players_df = pd.DataFrame.from_dict(player_info)
    return players_df

#### GRID ####

def check_team_combo_has_matching_player(team_a: str, team_b: str) -> list[str]:
    list_of_valid_players = get_request(BASE, f'check_team_combo_is_valid/{team_a}/{team_b}')
    return list_of_valid_players

def get_all_grids_from_db() -> pd.DataFrame:
    all_grids = get_request(BASE, f'get_all_grids')
    grids_df = pd.DataFrame.from_dict(all_grids)
    return grids_df

    

##########################################################################################################
### UPDATE DATA FROM DB ###
##########################################################################################################

def update_player_first_season_in_db(single_player_identifier:str,first_season:int)->dict:
    single_player_identifier = single_player_identifier.replace(" ", "-")
    updated_player = put_request(BASE,f'update_player_first_season/{single_player_identifier}/{first_season}')
    return updated_player

def update_guesses_count_in_db(single_player_identifier:str)->dict:
    single_player_identifier = single_player_identifier.replace(" ", "-")
    updated_guess_count = put_request(BASE,f'update_guess_count/{single_player_identifier}')
    return updated_guess_count

def main():
    pass
    
if __name__ == "__main__":
    main()