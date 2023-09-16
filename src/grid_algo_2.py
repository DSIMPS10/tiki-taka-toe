import random
from itertools import combinations
from collections import Counter

from data.data_db_functions import check_team_combo_has_matching_player
from grid_algo import unique_combo_of_teams

def find_a_grid_combo(unique_combo_of_teams: list):
    # Shuffle unique team combos
    random.shuffle(unique_combo_of_teams)
    solved = False
    iteration = 1
    while solved == False:
        print(f'Iteration: {iteration}')
        # step 1: chose a combo at random
        random_combo_index = random.choice(range(len(unique_combo_of_teams)))
        random_combo = unique_combo_of_teams[random_combo_index]
        team_a = random_combo[0]
        print(f'Team A: {team_a}')
        unique_combo_of_teams.pop(random_combo_index)
        print(f'Number of unique team combos: {len(unique_combo_of_teams)}')

        #step 2: chose x,y,z
        team_list_that_matches_team_a = []
        for combo in unique_combo_of_teams:
            if combo[0] == team_a:
                team_list_that_matches_team_a.append(combo[1])
            if combo[1] == team_a:
                team_list_that_matches_team_a.append(combo[0])
        print(f'Number of teams that have a player match with team a: {len(team_list_that_matches_team_a)}')
        # step 3: get possible b and c
        x_y_z_combinations = list(combinations(team_list_that_matches_team_a, 3))
        for x_y_z_combo in x_y_z_combinations: # [x, y, z]
            x_y_z_combo = list(x_y_z_combo)
            team_x = x_y_z_combo[0] #liv
            team_y = x_y_z_combo[1] #chels
            team_z = x_y_z_combo[2] #tot
            potential_b_or_c_team = []
            potential_b_or_c_matching_comobo = []
            valid_b_or_c_team = []

            # Get all combos that contain liv, chels, tot
            for combo in unique_combo_of_teams:
                if team_x in combo or team_y in combo or team_z in combo:
                    potential_b_or_c_matching_comobo.append(combo)
            print(f'Number of potential combos with b or c teams : {len(potential_b_or_c_matching_comobo)}')
            # Get all teams not x,y,z in list:
            for match_combo in potential_b_or_c_matching_comobo:
                for team in match_combo:
                    if team != team_x and team != team_y and team != team_z and team != team_a:
                        potential_b_or_c_team.append(team)
            print(f'Number of potential b or c teams: {len(potential_b_or_c_team)}')
            # Get unique teams by removing duplicates
            unique_b_c_teams = list(set(potential_b_or_c_team))
            print(f'Number of unique teams (out of 40): {len(unique_b_c_teams)}')
            if len(potential_b_or_c_team) < 3:
                pass
            else:
                #If a team appears 3 times it is match for a,b,c
                counter_dict = Counter(potential_b_or_c_team)
                # print(counter_dict)
                for team,count in counter_dict.items():
                    if count == 3:
                        #It therefore has all matches with x, y & z teams
                        valid_b_or_c_team.append(team)
                print(f'Number of valid b and c teams (i.e. matching x, y & z teams): {len(valid_b_or_c_team)}')
                if len(valid_b_or_c_team) < 2:
                    print('Failed! Not enough matching teams. Restarting combo finder...')
                else:
                    team_b = random.choice(valid_b_or_c_team)
                    valid_b_or_c_team.remove(team_b)
                    team_c = random.choice(valid_b_or_c_team)
                    correct_dict = {
                        'team_a': team_a,
                        'team_b': team_b,
                        'team_c': team_c,
                        'team_x': team_x,
                        'team_y': team_y,
                        'team_z': team_z
                        }
                    solved = True
                    print('6 potential teams were found!')
                    return correct_dict 
        print('Runing another iteration...')
        iteration += 1
        
def check_a_combo(team_a: str, team_b: str) -> bool:
    combo_exists = False
    list_of_valid_players = check_team_combo_has_matching_player(team_a, team_b)
    if len(list_of_valid_players) > 0:
        combo_exists = True
    return combo_exists

def check_all_combos(grid_dict: dict):
    combos = [[grid_dict['team_a'], grid_dict['team_x']], [grid_dict['team_a'], grid_dict['team_y']], [grid_dict['team_a'], grid_dict['team_z']],
              [grid_dict['team_b'], grid_dict['team_x']], [grid_dict['team_b'], grid_dict['team_y']], [grid_dict['team_b'], grid_dict['team_z']],
              [grid_dict['team_c'], grid_dict['team_x']], [grid_dict['team_c'], grid_dict['team_y']], [grid_dict['team_c'], grid_dict['team_z']]]
    for combo in combos:
        valid = check_a_combo(combo[0], combo[1])
        if valid == False: 
            print(f'ERROR: {combo[0]} and {combo[1]} do not have matching player.')
            return False
    print('All teams have matching players. This grid is valid!')
    return True

def main():
    solved = False
    while solved == False:
        # Step 1: Find a valid grid
        grid_combo: dict = find_a_grid_combo(unique_combo_of_teams)
        print(grid_combo)
        # Step 2: Check if grid is valid (i.e. all team combos have a player that has played for both.)
        is_grid_valid: bool = check_all_combos(grid_combo)
        if is_grid_valid:
            solved = True
    return grid_combo
        
if __name__ == "__main__":
    grid_combo = main()
    print(grid_combo)

            
            
    
    



