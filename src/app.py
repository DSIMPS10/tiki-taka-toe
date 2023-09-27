import pandas as pd
import random
import numpy as np
import logging

from utils.classes import Team, Player, FootyGrid
from flask_pkg.project.routes import BASE, get_request, post_request
from data.data_db_functions import get_all_players_from_db, get_all_team_from_db, get_all_grids_from_db
from scoring import update_guesses_table    
##########################################################################################################
### THE TIC TAC TOE APP WITH THE FOOTBALL DATA ###
##########################################################################################################


def select_grid_for_game(level: str)-> pd.DataFrame:
    '''Updates existing logic of choosing 6 random teams for the game. Instead, this gets all grids from the DB and selects as random grid option based on
    the input level, easy, medium, hard. These levels are chosen by filtering the DF imported by get_all_grids_from_db. 
    '''
    all_grids_df: pd.DataFrame = get_all_grids_from_db()
    if level =='easy':
        easy_grids_df = all_grids_df.loc[all_grids_df['total_score'] >= 50]
        easy_grid = easy_grids_df.sample(n=1)
        return easy_grid
    if level =='medium':
        medium_grids_df = all_grids_df.loc[(all_grids_df['total_score'] < 50) & (all_grids_df['total_score'] >= 20)]
        medium_grid = medium_grids_df.sample(n=1)
        return medium_grid
    if level =='hard':
        hard_grids_df = all_grids_df.loc[all_grids_df['total_score'] < 20]
        hard_grid = hard_grids_df.sample(n=1)
        return hard_grid

def grid_to_footygrid(grid_df: pd.DataFrame)-> FootyGrid:
    grid_df = grid_df.drop(columns = ['id'])
    selected_grid_dict = grid_df.to_dict(orient='records')[0]
    print(selected_grid_dict)
    selected_grid = FootyGrid(**selected_grid_dict)
    print(selected_grid)
    return selected_grid


#TODO: Change this to get teams from grid
# def get_six_random_indices()->list:
#     """
#     Input: No input
#     Output: List of 6 random indicies
#     """
#     team_count_dict = get_request(BASE,'count_all_football_teams')
#     team_count = team_count_dict["team_count"]
#     six_indices = random.sample(range(team_count),6)
#     return six_indices

# def get_teams_from_indices(six_indices:list[int])-> list[str]:
#     """
#     Input: List of 6 integers
#     Output: List of corresponding team names from the indices
#     """
#     team_names_list = []
#     all_teams_in_db: pd.DataFrame = get_all_team_from_db()
#     all_team_ids = all_teams_in_db['team_id'].to_list()
#     for i in six_indices:
#         team_id = all_team_ids[i]
#         team_name_dict = get_request(BASE,f"team_from_id/{team_id}")
#         team_names_list.append(team_name_dict["team_name"])
#     return team_names_list
        
def get_teams_for_selected_player_from_db(players_df: pd.DataFrame, player_name: str) -> list[str]:
    '''
    Input: DataFrame of player info, and players full name
    Output: List of all teams the player has played for
    '''
    try:
        teams: list[str] = players_df.loc[players_df['full_name'] == player_name]['team_name'].values.tolist()  
    except IndexError as e:
        print('Player not found in DB')
        teams = []
    except Exception as e:
        print('Error when searching for player.')
        logging.exception(e)
    return teams


def get_teams_from_grid_index(team_grid_obj: FootyGrid, pos_number)-> list[str]:
    '''
    Outp
    '''
    if pos_number == 1:
        return [team_grid_obj.team_a,team_grid_obj.team_z]
    elif pos_number == 2:
        return [team_grid_obj.team_b,team_grid_obj.team_z]
    elif pos_number == 3:
        return [team_grid_obj.team_c,team_grid_obj.team_z]
    elif pos_number == 4:
        return [team_grid_obj.team_a,team_grid_obj.team_y]
    elif pos_number == 5:
        return [team_grid_obj.team_b,team_grid_obj.team_y]
    elif pos_number == 6:
        return [team_grid_obj.team_c,team_grid_obj.team_y]
    elif pos_number == 7:
        return [team_grid_obj.team_a,team_grid_obj.team_x]
    elif pos_number == 8:
        return [team_grid_obj.team_b,team_grid_obj.team_x]
    elif pos_number == 9:
        return [team_grid_obj.team_c,team_grid_obj.team_x]
    



    
def compare_player(players_df: pd.DataFrame, player_name: str, selected_teams: list[str]) -> bool: 
    '''
    This function will return true if the player has played for both teams
    '''
    try:
        valid_guess = str(player_name)
    except ValueError:
        if not valid_guess:
            raise ValueError('empty input')
    else:
        teams_of_player = get_teams_for_selected_player_from_db(players_df, valid_guess)
        if len(teams_of_player) == 0:
            return False
        else:
            if selected_teams[0] in teams_of_player and selected_teams[1] in teams_of_player:
                return True    
        return False

# def create_six_team_df_for_grid(team_names_list: list[str])-> pd.DataFrame:
#     team_data = {"pos_1":team_names_list[0:2],
#                  "pos_2":team_names_list[2:4],
#                  "pos_3":team_names_list[4:6]}
    
#     team_df = pd.DataFrame(team_data)
#     return team_df

def convert_print_grid_as_df(team_names_list: list[str]) -> pd.DataFrame:
    grid_df = pd.DataFrame(columns=['Y\X', team_names_list[0], team_names_list[2], team_names_list[4]])
    print(grid_df)
    grid_df['Y\X']  = [team_names_list[1],team_names_list[3],team_names_list[5]]
    grid_df[team_names_list[0]]  = [{'3,1': np.nan},{'3,2': np.nan},{'3,3': np.nan}]
    grid_df[team_names_list[2]]  = [{'2,1': np.nan},{'2,2': np.nan},{'2,3': np.nan}]
    grid_df[team_names_list[4]]  = [{'1,1': np.nan},{'1,2': np.nan},{'1,3': np.nan}]
    return grid_df

def create_footy_team_board(level:str) -> FootyGrid:
    team_df: pd.DataFrame = select_grid_for_game(level)
    grid_obj: FootyGrid = grid_to_footygrid(team_df)
    return grid_obj

def run_footy(move: int, footy_team_obj: FootyGrid) -> bool:
    ### INPUTS ###
    # players_df: pd.DataFrame = get_all_players_from_db()
    guesses_df: pd.DataFrame = get_all_players_from_db()

    # pos_guess = int(input("Choose a grid number: "))
    selected_teams = get_teams_from_grid_index(footy_team_obj,move)

    print(f"Selected teams are: {selected_teams}")

    player_guess = input("Guess a player that played for both teams: ")
    answer: bool = compare_player(guesses_df, player_guess, selected_teams)

    if answer: 
        update_guesses_table(player_guess,selected_teams)
        print("Correct! That player did play for both teams.")
    else:
        print("Incorrect, that player didn't play for both teams.")
    
    return answer

def main(): #move: int, team_df: pd.DataFrame
    # run_footy(move, team_df)
    a = select_grid_for_game('easy')
    
    print(a)

    b = grid_to_dict(a)
    
    print(type(b))
    print(b)

if __name__ == "__main__":
    # move = int(input('Chose a grid position to place a marker: '))
    # team_df = pd.DataFrame()
    main() #move, team_df
