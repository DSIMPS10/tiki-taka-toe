import pandas as pd
import json
import random

# import tic_tac_toe as ttt
from utils.app_objects import Team
from flask_pkg.project.routes import BASE, get_request, post_request
from data import CURRENT_PREM_TEAMS

def post_teams_to_db(teams: list[Team]):
    # Convert activities to json
    teams_array = [vars(team) for team in teams]
    # for team in teams:
    #     teams_array.append(vars(team))
        
    activitity_json_str = json.dumps(teams_array)
        
    # Post request
    teams_posted = post_request(BASE,"post_teams",activitity_json_str)
    print(f"New teams posted: {teams_posted}")
    return teams_posted


def get_teams_from_db(limit):
    teams = get_request(BASE, f'get_football_teams/{limit}')
    df = pd.DataFrame.from_dict(teams)
    return df

def post_some_demo_teams():
    chelsea = Team(team_name='Chelsea', league='Premiership', country='England')
    tottenham = Team(team_name='Tottenham', league='Premiership', country='England')
    arsenal = Team(team_name='Arsenal', league='Premiership', country='England')
    teams_to_be_posted: Team = [chelsea, tottenham, arsenal]
    teams_posted = post_teams_to_db(teams_to_be_posted)

# TODO: get 6 random indexes to select teams by (will need to get max index of DB and use the random lib)
# Output: list[] of 6 integers
def get_six_random_indices()->list:
    team_count_dict = get_request(BASE,"count_all_football_teams")
    print(team_count_dict)
    team_count = team_count_dict["team_count"]
    print(team_count)
    six_indices = random.sample(range(1,team_count+1),6)
    return six_indices

# TODO: use the list of 6 indexes to get the teams from the db
# Output: list[] of 6 team objects
# Later on will be able to add filter by country or league
def get_teams_from_indices(six_indices:list)-> list:
    team_names_list = []
    for i in six_indices:
        
        team_name_dict = get_request(BASE,f"team_name_from_id/{i}")
        print(team_name_dict)
        
        team_names_list.append(team_name_dict["team_name"])
        print(team_names_list)
    return team_names_list
        
def get_teams_for_selected_player_from_db(player_df, player_name):
    teams: list = player_df.loc[player_df['Name'] == player_name]['Team'].values[0]  
    return teams


def get_teams_from_grid_index(team_df, grid: Grid, pos_number):
    pos_list = grid.number_to_index(pos_number)
    row_a = pos_list[0]-1
    row_b = pos_list[1]-1
    teams_x = team_df.iloc[0].values
    teams_y = team_df.iloc[1].values
    selected_teams = [teams_x[row_a],teams_y[row_b]]
    return selected_teams

    
def compare_player(players_df, player_name, selected_teams) -> bool: 
    '''
    This function will return true if the player has played for both teams
    '''
    teams_of_player = get_teams_for_selected_player_from_db(players_df, player_name)

    if selected_teams[0] in teams_of_player and selected_teams[1] in teams_of_player:
        return True
    
    return False

def create_six_team_info(team_names_list)-> pd.DataFrame:
    team_data = {"pos_1":[team_names_list[0:1]],
                 "pos_2":[team_names_list[2:3]],
                 "pos_3":[team_names_list[4:5]]}
    
    team_df = pd.DataFrame(team_data)
    
    return team_df

def run_footy():
    ### INPUTS ###
    create_six_team_info

    players_data = {
    "Name": ['Raheem Sterling', 'Kai Havertz', 'Harry Kane'],
    "Team": [['Chelsea', 'Man City', 'Liverpool'], ['Chelsea','Arsenal'], ['Tottenham', 'Bayern Munich']]
        }

    players_df = pd.DataFrame(players_data)
    players_df['Name'] = players_df['Name'].apply(str.lower)

    grid = Grid()

    pos_guess = int(input("Choose a grid number: "))
    selected_teams = get_teams_from_grid_index(team_df, grid, pos_guess)

    print(f"Selected teams are: {selected_teams}")

    player_guess = input("Guess a player that played for both teams: ").lower()
    answer = compare_player(players_df, player_guess, selected_teams)

    if answer: 
        print("Correct! That player did play for both teams.")
    else:
        print("Incorrect, that player didn't play for both teams.")


def main():
    #teams = get_teams_from_db(3)
    #print(teams)
    #print(CURRENT_PREM_TEAMS)
    # test = post_some_demo_teams()
    # print(test)
    # test = CURRENT_PREM_TEAMS
    # posted_teams = post_teams_to_db(CURRENT_PREM_TEAMS)
    # print(posted_teams)
    six_indices = get_six_random_indices()
    testing_list= get_teams_from_indices(six_indices)
    print(testing_list)

if __name__ == "__main__":
    main()
