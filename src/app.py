import pandas as pd
import json
import random
import numpy as np
import logging

from utils.classes import Team, Grid, Player
from flask_pkg.project.routes import BASE, get_request, post_request

##########################################################################################################
### THE TIC TAC TOE APP WITH THE FOOTBALL DATA ###
##########################################################################################################

def get_six_random_indices()->list:
    team_count_dict = get_request(BASE,"count_all_football_teams")
    print(team_count_dict)
    team_count = team_count_dict["team_count"]
    print(team_count)
    six_indices = random.sample(range(1,team_count+1),6)
    return six_indices

def get_teams_from_indices(six_indices:list)-> list:
    team_names_list = []
    for i in six_indices:
        
        team_name_dict = get_request(BASE,f"team_name_from_id/{i}")
        print(team_name_dict)
        
        team_names_list.append(team_name_dict["team_name"])
        print(team_names_list)
    return team_names_list
        
def get_teams_for_selected_player_from_db(player_df, player_name):
    try:
        teams: list = player_df.loc[player_df['Name'] == player_name]['Team'].values[0]  
    except IndexError as e:
        print('Player not found in DB')
        teams = []
    except Exception as e:
        print('Error when searching for player.')
        logging.exception(e)
    return teams


def get_teams_from_grid_index(team_df, grid: Grid, pos_number):
    pos_list = grid.number_to_index(pos_number)
    row_a = pos_list[0]-1
    row_b = pos_list[1]-1
    teams_x = team_df.iloc[0].values
    teams_y = team_df.iloc[1].values
    selected_teams = [teams_x[row_a],teams_y[row_b]]
    selected_teams.sort()
    return selected_teams

    
def compare_player(players_df, player_name, selected_teams) -> bool: 
    '''
    This function will return true if the player has played for both teams
    '''
    teams_of_player = get_teams_for_selected_player_from_db(players_df, player_name)
    if len(teams_of_player) == 0:
        return False
    else:
        if selected_teams[0] in teams_of_player and selected_teams[1] in teams_of_player:
            return True
    
    return False

def create_six_team_info(team_names_list)-> pd.DataFrame:
    team_data = {"pos_1":[team_names_list[0:1]],
                 "pos_2":[team_names_list[2:3]],
                 "pos_3":[team_names_list[4:5]]}
    
    team_df = pd.DataFrame(team_data)
    
    return team_df

def print_grid_as_df(team_names_list: list) -> pd.DataFrame:
    grid_df = pd.DataFrame(columns=['Y\X', team_names_list[0], team_names_list[2], team_names_list[4]])
    print(grid_df)
    grid_df['Y\X']  = [team_names_list[1],team_names_list[3],team_names_list[5]]
    grid_df[team_names_list[0]]  = [{'1,1': np.nan},{'1,2': np.nan},{'1,3': np.nan}]
    grid_df[team_names_list[2]]  = [{'2,1': np.nan},{'2,2': np.nan},{'2,3': np.nan}]
    grid_df[team_names_list[4]]  = [{'3,1': np.nan},{'3,2': np.nan},{'3,3': np.nan}]
    return grid_df

def run_footy(move: int):
    ### INPUTS ###
    # six_indices = get_six_random_indices()
    # team_names_list = get_teams_from_indices(six_indices)
    # team_df = create_six_team_info(team_names_list)

    team_data = {"pos_1":["Tottenham","Chelsea"],
            "pos_2":["West Ham","Liverpool"],
            "pos_3": ["Man City","Bayern Munich"]}
    team_df = pd.DataFrame(team_data)
    players_data = {
    "Name": ['Raheem Sterling', 'Kai Havertz', 'Harry Kane'],
    "Team": [['Chelsea', 'Man City', 'Liverpool'], ['Chelsea','Arsenal'], ['Tottenham', 'Bayern Munich']]
        }

    players_df = pd.DataFrame(players_data)
    players_df['Name'] = players_df['Name'].apply(str.lower)

    grid = Grid()

    # pos_guess = int(input("Choose a grid number: "))
    selected_teams = get_teams_from_grid_index(team_df, grid, move)

    print(f"Selected teams are: {selected_teams}")

    player_guess = input("Guess a player that played for both teams: ").lower()
    answer: bool = compare_player(players_df, player_guess, selected_teams)

    if answer: 
        print("Correct! That player did play for both teams.")
    else:
        print("Incorrect, that player didn't play for both teams.")
    
    return answer

def main(move: int):
    run_footy(move)

if __name__ == "__main__":
    move = int(input('Chose a grid position to place a marker: '))
    main(move)
