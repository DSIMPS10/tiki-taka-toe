import pandas as pd
import json

from utils.classes import Team, Player , Guesses
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

def post_teams_to_db(teams: list[Team]):
    # Convert activities to json
    teams_array = [vars(team) for team in teams]       
    activitity_json_str = json.dumps(teams_array)
        
    # Post request
    teams_posted = post_request(BASE,"post_teams",activitity_json_str)
    print(f"New teams posted: {teams_posted}")
    return teams_posted

def post_players_to_db(players: list[Player]):
    # Convert players to json
    players_array = [vars(player) for player in players] 
    activitity_json_players_str = json.dumps(players_array)  
    # Post request
    players_posted = post_request(BASE,"post_players",activitity_json_players_str)
    print(f"New players posted: {players_posted}")
    return players_posted

def post_valid_player_combos(valid_player_combos: list[Guesses]):
    # Convert valid players to json
    valid_player_combos_array = [vars(player_combo) for player_combo in valid_player_combos] 
    activitity_json_players_str = json.dumps(valid_player_combos_array)  
    # Post request
    valid_player_combos_posted = post_request(BASE,"post_valid_player_combos",activitity_json_players_str)
    print(f"New player combos posted: {valid_player_combos_posted}")
    return valid_player_combos_posted
    
##########################################################################################################
### GET DATA FROM DB ###
##########################################################################################################

def get_teams_from_db(limit: int) -> pd.DataFrame:
    teams = get_request(BASE, f'get_football_teams/{limit}')
    df = pd.DataFrame.from_dict(teams)
    return df

def get_all_team_from_db() -> pd.DataFrame:
    all_teams = get_request(BASE, f'get_all_football_teams')
    df = pd.DataFrame.from_dict(all_teams)
    return df

def get_all_players_from_db() -> pd.DataFrame:
    all_players = get_request(BASE, f'get_all_players')
    players_df = pd.DataFrame.from_dict(all_players)
    return players_df

def get_valid_guesses_from_db()->list[str]:
    all_valid_guesses = get_request(BASE, f'get_all_valid_player_guesses')
    return all_valid_guesses

def get_player_info_from_name_db(full_name: str):
    player_info = get_request(BASE, f'get_player_info_from_name/{full_name}')
    players_df = pd.DataFrame.from_dict(player_info)
    return players_df

##########################################################################################################
### UPDATE DATA FROM DB ###
##########################################################################################################

def update_player_first_season_in_db(single_player_identifier:str,first_season:int)->dict:
    single_player_identifier = single_player_identifier.replace(" ", "-")
    print(single_player_identifier)
    updated_player = put_request(BASE,f'update_player_first_season/{single_player_identifier}/{first_season}')
    return updated_player

def main():
    pass
    
if __name__ == "__main__":
    main()