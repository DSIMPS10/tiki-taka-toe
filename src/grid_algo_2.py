import random
from itertools import combinations
from collections import Counter
from pandas import DataFrame

from data.data_db_functions import check_team_combo_has_matching_player
from grid_algo import unique_combo_of_teams

def find_a_grid_combo(unique_combo_of_teams: list, level: str):
    # Shuffle unique team combos
    random.shuffle(unique_combo_of_teams)
    solved = False
    major_iteration = 1
    minor_iteration = 1

    while solved == False:
        # Step 1: chose a combo at random
        random_combo_index = random.choice(range(len(unique_combo_of_teams)))
        random_combo = unique_combo_of_teams[random_combo_index]
        team_a = random_combo[0]
        print(f'Team A: {team_a}')
        unique_combo_of_teams.pop(random_combo_index)
        print(f'Number of unique team combos: {len(unique_combo_of_teams)}')

        # Step 2: chose x,y,z that have a match with team a
        team_list_that_matches_team_a = []
        for combo in unique_combo_of_teams:
            if combo[0] == team_a:
                team_list_that_matches_team_a.append(combo[1])
            if combo[1] == team_a:
                team_list_that_matches_team_a.append(combo[0])
        print(f'Number of teams that have a player match with team a: {len(team_list_that_matches_team_a)}')
        # Step 3: get possible b and c teams that all have a match with x,y & z
        random.shuffle(team_list_that_matches_team_a)
        x_y_z_combinations = list(combinations(team_list_that_matches_team_a, 3))
        for x_y_z_combo in x_y_z_combinations: # [x, y, z]
            print(f'Iteration: {major_iteration}.{minor_iteration}')
            x_y_z_combo = list(x_y_z_combo)
            team_x = x_y_z_combo[0] # team name x
            team_y = x_y_z_combo[1] # team name y
            team_z = x_y_z_combo[2] # team name z
            potential_b_or_c_team = []
            potential_b_or_c_matching_comobo = []
            valid_b_or_c_team = []

            # Step 4: Get all combos that contain x, y and z teams
            for combo in unique_combo_of_teams:
                if team_x in combo or team_y in combo or team_z in combo:
                    potential_b_or_c_matching_comobo.append(combo)
            print(f'Number of potential combos with b or c teams : {len(potential_b_or_c_matching_comobo)}')
            # Step 5: Get all teams from combos that aren't x,y,z in list:
            for match_combo in potential_b_or_c_matching_comobo:
                for team in match_combo:
                    if team != team_x and team != team_y and team != team_z and team != team_a:
                        potential_b_or_c_team.append(team)
            print(f'Number of potential b or c teams: {len(potential_b_or_c_team)}')
            # Extra: Get unique teams by removing duplicates
            unique_b_c_teams = list(set(potential_b_or_c_team))
            print(f'Number of unique teams (out of 40): {len(unique_b_c_teams)}')
            if len(potential_b_or_c_team) < 3:
                pass
            else:
                # Step 6: If a team appears 3 times it is match for a,b,c
                counter_dict = Counter(potential_b_or_c_team)
                for team,count in counter_dict.items():
                    if count == 3:
                        #It therefore has all matches with x, y & z teams
                        valid_b_or_c_team.append(team)
                print(f'Number of valid b and c teams (i.e. matching x, y & z teams): {len(valid_b_or_c_team)}')
                if len(valid_b_or_c_team) < 2:
                    print('Failed! Not enough matching teams. Restarting combo finder...')
                else:
                    # Step 7: Get dict of valid teams for grid
                    random.shuffle(valid_b_or_c_team)
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
                    check_combos_and_level = check_all_combos(correct_dict, level)
                    if check_combos_and_level[0] == True:
                        solved = True
                        combo_count_dict = check_combos_and_level[1] 
                        print('6 potential teams at the right level were found!')
                        return True, correct_dict, combo_count_dict 
                    else: 
                        print('Runing another iteration...')
                        # iteration += 1
            print('Running new x y z combo iteration...')
            minor_iteration += 1
        print('Running new iteration from start team...')
        major_iteration += 1
       
def check_a_combo(team_a: str, team_b: str) -> [bool, int]:
    combo_exists = False
    list_of_valid_players = check_team_combo_has_matching_player(team_a, team_b)
    number_of_matching_players = len(list_of_valid_players)
    if len(list_of_valid_players) > 0:
        combo_exists = True
    return combo_exists, number_of_matching_players

def check_all_combos(grid_dict: dict, level: str) -> bool:
    combo_dict = {}
    combos = [[grid_dict['team_a'], grid_dict['team_x']], [grid_dict['team_a'], grid_dict['team_y']], [grid_dict['team_a'], grid_dict['team_z']],
              [grid_dict['team_b'], grid_dict['team_x']], [grid_dict['team_b'], grid_dict['team_y']], [grid_dict['team_b'], grid_dict['team_z']],
              [grid_dict['team_c'], grid_dict['team_x']], [grid_dict['team_c'], grid_dict['team_y']], [grid_dict['team_c'], grid_dict['team_z']]]
    for combo in combos:
        valid = check_a_combo(combo[0], combo[1])[0]
        number_of_matching_players = check_a_combo(combo[0], combo[1])[1]
        if valid == False: 
            print(f'ERROR: {combo[0]} and {combo[1]} do not have matching player.')
            return False, None
        combo_dict[f'{combo[0]}, {combo[1]}'] = number_of_matching_players
    print('All teams have matching players. This grid is valid!')
    correct_level = check_level(level, combo_dict)
    if correct_level == False: 
        return False, None
    else:
        return True, combo_dict

def convert_grid_dict_to_pos_df(grid_dict: dict) -> DataFrame:
    data = {
        'pos_1': [grid_dict['team_a'],grid_dict['team_x']],
        'pos_2': [grid_dict['team_b'],grid_dict['team_y']],
        'pos_3': [grid_dict['team_c'],grid_dict['team_z']]
    }
    grid_df = DataFrame(data)
    return grid_df

def check_level(level: str, combo_dict: dict):
    level_dict = {
        'easy': 3,
        'medium': 2,
        'hard': 1,
        'random': 1
        }
    min_number: int = level_dict[level]
    for combo, count in combo_dict.items():
        if count < min_number:
            return False
    return True
        

def main(level: str) -> DataFrame:
    solved = False
    # iteration = 1
    # while solved == False:
    #     print(f'Iteration: {iteration}')
        # Step 1: Find a valid grid
    grid_combo_tuple: dict = find_a_grid_combo(unique_combo_of_teams, level)
    grid_combo = grid_combo_tuple[1]
    combo_count = grid_combo_tuple[2]
    if grid_combo_tuple[0] == True:
        print(grid_combo)
        print(combo_count)
        solved = True
    # else: 
    #     print('Runing another iteration...')
    #     iteration += 1
            
        # # Step 2: Check if grid is valid (i.e. all team combos have a player that has played for both.)
        # is_grid_valid: bool = check_all_combos(grid_combo)
        # # Check level
        # if is_grid_valid[0] and redo == False:
        #     solved = True
        #     valid_grid_with_count = is_grid_valid[1]
        #     print(f'Valid grid with number of correct matches for each combo: {valid_grid_with_count}')
        
    # print(grid_combo)
    team_df = convert_grid_dict_to_pos_df(grid_combo)
    return team_df
        
if __name__ == "__main__":
    level = 'medium'
    grid_df = main(level)
    print(grid_df)

            
            
    
    



