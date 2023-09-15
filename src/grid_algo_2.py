import random
from itertools import combinations
from collections import Counter


from grid_algo import unique_combo_of_teams

def find_a_grid_combo():
    solved = False
    while solved == False:
        # step 1: chose a combo at random
        random_combo_index = random.choice(range(len(unique_combo_of_teams)))
        random_combo = unique_combo_of_teams[random_combo_index]
        team_a = random_combo[0]
        print(team_a)
        unique_combo_of_teams.pop(random_combo_index)
        print(len(unique_combo_of_teams))

        #step 2: chose x,y,z
        team_list_that_matches_team_a = []
        for combo in unique_combo_of_teams:
            if combo[0] == team_a:
                team_list_that_matches_team_a.append(combo[1])
            if combo[1] == team_a:
                team_list_that_matches_team_a.append(combo[0])
        print(len(team_list_that_matches_team_a))
        # step 3: get possible b and c
        x_y_z_combinations = list(combinations(team_list_that_matches_team_a, 3))
        # print(x_y_z_combinations)
        for x_y_z_combo in x_y_z_combinations: # [x, y, z]
            x_y_z_combo = list(x_y_z_combo)
            # print(x_y_z_combo)
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
            # print(potential_b_or_c_matching_comobo)
            print(len(potential_b_or_c_matching_comobo))
            # Get all teams not x,y,z in list:
            for match_combo in potential_b_or_c_matching_comobo:
                #[chels, bright]
                for team in match_combo:
                    if team != team_x and team != team_y and team != team_z and team != team_a:
                        potential_b_or_c_team.append(team)
            # print(potential_b_or_c_team)
            print(f'Number of potential b or c teams: {len(potential_b_or_c_team)}')
            if len(potential_b_or_c_team) < 3:
                pass
            else:
                #If a team appears 3 times it is match for a,b,c
                counter_dict = Counter(potential_b_or_c_team)
                print(counter_dict)
                for team,count in counter_dict.items():
                    if count == 3:
                        #It therefore has all matches
                        valid_b_or_c_team.append(team)
                    if len(valid_b_or_c_team) == 2:
                        team_b = valid_b_or_c_team[0]
                        team_c = valid_b_or_c_team[1] 
                        correct_dict = {
                            'Team A': team_a,
                            'Team B': team_b,
                            'Team C': team_c,
                            'Team X': team_x,
                            'Team Y': team_y,
                            'Team Z': team_z
                            }
                        solved = True
                        print('6 potential teams were found!')
                        return correct_dict 
        return 'No matches found, please restart...'


grid_combo = find_a_grid_combo()
print(grid_combo)


            
            
    
    



