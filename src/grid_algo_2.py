import random
from statistics import mode,median
from itertools import combinations
from collections import Counter
from pandas import DataFrame
from utils.classes import FootyGrid

from guesses import get_all_team_combos_process
from data.data_db_functions import check_team_combo_has_matching_player, post_valid_grids, get_all_grids_from_db
from grid_algo import unique_combo_of_teams

def find_a_grid_combo(unique_combo_of_teams:list, team_a: str): #, level: str
    valid_grids = []
    # Shuffle unique team combos
    random.shuffle(unique_combo_of_teams)
    major_iteration = 1
    minor_iteration = 1
    # Step 1: chose a combo at random
    # random_combo_index = random.choice(range(len(unique_combo_of_teams)))
    # random_combo = unique_combo_of_teams[random_combo_index]
    # team_a = random_combo[0]
    print(f'Team A: {team_a}')
    # unique_combo_of_teams.pop(random_combo_index)
    # print(f'Number of unique team combos: {len(unique_combo_of_teams)}')

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
                print(correct_dict)
                # grid_obj = get_single_grid_info(correct_dict)
                valid_grids.append(correct_dict)    
    return valid_grids

def get_single_grid_info(grid_dict: dict)->dict:
    combo_dict = {}
    combos = [[grid_dict['team_a'], grid_dict['team_x']], [grid_dict['team_a'], grid_dict['team_y']], [grid_dict['team_a'], grid_dict['team_z']],
              [grid_dict['team_b'], grid_dict['team_x']], [grid_dict['team_b'], grid_dict['team_y']], [grid_dict['team_b'], grid_dict['team_z']],
              [grid_dict['team_c'], grid_dict['team_x']], [grid_dict['team_c'], grid_dict['team_y']], [grid_dict['team_c'], grid_dict['team_z']]]
    for combo in combos:
        number_of_matching_players = check_a_combo(combo[0], combo[1])[1]
        combo_dict[f'{combo[0]}, {combo[1]}'] = number_of_matching_players
    total_count = 0
    min_count = 1000
    max_count = 0
    for team_combo, match_count in combo_dict.items():
        total_count+=match_count
        if match_count < min_count:
            min_count = match_count
        if match_count > max_count:
            max_count = match_count
    list_of_values = [*combo_dict.values()]
    list_of_values.sort()
    grid_median = median(list_of_values)
    grid_mode = mode(list_of_values)
    grid_dict['total_score'] = total_count
    grid_dict['max_matches'] = max_count
    grid_dict['min_matches'] = min_count
    grid_dict['mode_matches'] = grid_mode
    grid_dict['median_matches'] = grid_median
    grid_dict['percentage_completion'] = 0
    return grid_dict

def convert_to_grid_objects(grid_dict: dict)->FootyGrid:
    grid_details = FootyGrid(**grid_dict)
    return grid_details
    
        #             check_combos_and_level = check_all_combos(correct_dict, level)
        #             if check_combos_and_level[0] == True:
        #                 solved = True
        #                 combo_count_dict = check_combos_and_level[1] 
        #                 print('6 potential teams at the right level were found!')
        #                 return True, correct_dict, combo_count_dict 
        #     print(f'Running new x y z combo iteration... {minor_iteration+1} of {len(x_y_z_combinations)}')
        #     minor_iteration += 1
        # print(f'Running new iteration from start team... {major_iteration+1} of {len(unique_combo_of_teams)}')
        # major_iteration += 1
       
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
    level_count_dict = {
        'easy': 3,
        'medium': 2,
        'hard': 1,
        'random': 1
        }
    level_av_dict = {
        'very easy': 60,
        'easy': 40,
        'medium': 25,
        'hard': 9,
        'impossible': 1,
        'random': 9
        }
    # level_type = 'COUNT'
    level_type = 'AVE'
    if level_type == 'COUNT':
        # Get all combos to have over a certain number of matches
        min_number: int = level_count_dict[level]
        for combo, count in combo_dict.items():
            if count < min_number:
                return False
        return True

    if level_type == 'AVE':
        total = 0
        level_average: int = level_av_dict[level]
        for combo, count in combo_dict.items():
            total += count
        if total > level_average:
            print(f'Total matches: {total} (out of {level_av_dict[level]})')
            return True
        return False

#TODO: CHANGE FUNCTIONS TO EASY, MEDIUM, HARD 
def select_grid_for_game(level: str):
    '''Updates existing logic of choosing 6 random teams for the game. Instead, this gets all grids from the DB and selects as random grid option based on
    the input level, easy, medium, hard. These levels are chosen by filtering the DF imported by get_all_grids_from_db. 
    '''
    all_grids_df: DataFrame = get_all_grids_from_db()
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

def run_complete_grid_process(team_a): 
    # Step 1: Based on a defined team_a (already chosen) find every possible combination of grids 
    # Output: List of dictionaries of every possible grid combination
    unique_combo_of_teams = get_all_team_combos_process()
    grid_dicts: list[dict] = find_a_grid_combo(unique_combo_of_teams,team_a)
    # Step 2: Create a list of all grid combos with all grid info to turn it into a class obj
    grid_info_for_all_combo: list[dict] = [get_single_grid_info(grid_dict) for grid_dict in grid_dicts]
    # Step 3: Turn the lists into Grid class obj
    grids_obj: list[FootyGrid] = [convert_to_grid_objects(grid_info) for grid_info in grid_info_for_all_combo]
    #Step 4: Post to DB
    post_valid_grids(grids_obj)
    return print('All grids posted')


def main() -> DataFrame: #level: str

    # valid_grids = find_a_grid_combo(unique_combo_of_teams)    
    # solved = False
    # Step 1: Run through iterations to find a grip
    # grid_combo_tuple: dict = find_a_grid_combo(unique_combo_of_teams, level)
    # # Step 2: Use the valid grid
    # grid_combo = grid_combo_tuple[1]
    # combo_count = grid_combo_tuple[2]
    # if grid_combo_tuple[0] == True:
    #     print(grid_combo)
    #     print(combo_count)
    # team_a = 'Arsenal'
    # run_complete_grid_process(team_a)
    grid = select_grid_for_game('hard')
    print(grid)

    
    #team_df = convert_grid_dict_to_pos_df(grid_combo)
        
if __name__ == "__main__":
    level = 'impossible'
    grid_df = main() #level
    #print(grid_df)

            
            
    
    



