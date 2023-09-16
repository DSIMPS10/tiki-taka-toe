import random
unique_combo_of_teams = [['Birmingham', 'Manchester United'], ['Aston Villa', 'Luton'], ['Arsenal', 'Crystal Palace'], ['Bolton', 'Cardiff'], ['Liverpool', 'Norwich'], ['Cardiff', 'Manchester United'], ['QPR', 'Reading'], ['Bournemouth', 'Watford'], ['Brighton', 'Middlesbrough'], ['Chelsea', 'Luton'], ['Aston Villa', 'Swansea'], ['Hull City', 'Newcastle'], ['Huddersfield', 'Hull City'], ['Chelsea', 'Swansea'], ['Liverpool', 'West Ham'], ['Manchester City', 'Swansea'], ['Arsenal', 'Southampton'], ['Hull City', 'West Brom'], ['Blackburn', 'West Brom'], ['Fulham', 'Reading'], ['Bolton', 'Fulham'], ['Hull City', 'Liverpool'], ['Middlesbrough', 'Norwich'], ['Crystal Palace', 'Watford'], ['QPR', 'Wolves'], ['Crystal Palace', 'QPR'], ['Liverpool', 'Manchester City'], ['Leeds', 'Wigan'], ['Hull City', 'Manchester United'], ['Aston Villa', 'Blackpool'], ['Leicester', 'Wolves'], ['Newcastle', 'Tottenham'], ['Blackburn', 'Sunderland'], ['Blackburn', 'Chelsea'], ['Brighton', 'Newcastle'], ['Southampton', 'West Ham'], ['Middlesbrough', 'West Ham'], ['Aston Villa', 'Cardiff'], ['Birmingham', 'Cardiff'], ['Everton', 'Wigan'], ['Burnley', 'Fulham'], ['Swansea', 'Wigan'], ['Sunderland', 'Watford'], ['Brighton', 'West Brom'], ['Bournemouth', 'Wolves'], ['Newcastle', 'QPR'], ['Arsenal', 'Luton'], ['Tottenham', 'West Ham'], ['Liverpool', 'Tottenham'], ['Brighton', 'Manchester United'], ['Leicester', 'Southampton'], ['Brentford', 'Burnley'], ['Bournemouth', 'Crystal Palace'], ['Arsenal', 'Swansea'], ['Aston Villa', 'Fulham'], ['Fulham', 'Stoke City'], ['Chelsea', 'Fulham'], ['Crystal Palace', 'Wolves'], ['Southampton', 'Tottenham'], ['Bournemouth', 'Southampton'], ['Newcastle', 'Stoke City'], ['Chelsea', 'Norwich'], ['Nottingham Forest', 'West Brom'], ['Manchester City', 'Norwich'], ['Blackburn', 'West Ham'], ['Everton', 'Watford'], ['Everton', 'QPR'], ['Swansea', 'Watford'], ['Nottingham Forest', 'Sunderland'], ['Sunderland', 'Wolves'], ['QPR', 'Swansea'], ['Hull City', 'Wigan'], ['Blackburn', 'Wigan'], ['Norwich', 'QPR'], ['Leicester', 'Swansea'], ['Liverpool', 'Stoke City'], ['Crystal Palace', 'Southampton'], ['Huddersfield', 'West Ham'], ['Bournemouth', 'Manchester United'], ['Chelsea', 'Manchester City'], ['Burnley', 'Leicester'], ['Arsenal', 'Aston Villa'], ['Arsenal', 'Fulham'], ['Brentford', 'Huddersfield'], ['Bournemouth', 'Swansea'], ['Leeds', 'Wolves'], ['Middlesbrough', 'Stoke City'], ['Birmingham', 'Burnley'], ['Blackpool', 'Stoke City'], ['Crystal Palace', 'Manchester United'], ['Aston Villa', 'Leicester'], ['Aston Villa', 'Reading'], ['Fulham', 'West Brom'], ['Birmingham', 'Leicester'], ['Crystal Palace', 'Luton'], ['Blackpool', 'Huddersfield'], ['Fulham', 'Nottingham Forest'], ['Manchester City', 'Tottenham'], ['Everton', 'Wolves'], ['Fulham', 'Liverpool'], ['Huddersfield', 'Tottenham'], ['Nottingham Forest', 'Sheffield Utd'], ['Cardiff', 'Leicester'], ['Stoke City', 'West Ham'], ['Bolton', 'Bournemouth'], ['Crystal Palace', 'Swansea'], ['Manchester City', 'Reading'], ['Fulham', 'Sunderland'], ['Blackburn', 'QPR'], ['Norwich', 'Wolves'], ['Newcastle', 'West Brom'], ['Bournemouth', 'Cardiff'], ['Manchester United', 'Norwich'], ['Arsenal', 'Manchester City'], ['Birmingham', 'Wolves'], ['Sunderland', 'Swansea'], ['Cardiff', 'Wolves'], ['Hull City', 'Leicester'], ['Everton', 'Southampton'], ['Everton', 'Leeds'], ['Luton', 'Norwich'], ['Manchester United', 'West Ham'], ['Liverpool', 'West Brom'], ['Liverpool', 'Nottingham Forest'], ['Brighton', 'Watford'], ['Norwich', 'Southampton'], ['Stoke City', 'Tottenham'], ['Burnley', 'Everton'], ['Bournemouth', 'Fulham'], ['Liverpool', 'Sunderland'], ['Aston Villa', 'Bournemouth'], ['QPR', 'West Ham'], ['Leeds', 'Manchester United'], ['Chelsea', 'Stoke City'], ['Aston Villa', 'Huddersfield'], ['Manchester City', 'Stoke City'], ['Brighton', 'Burnley'], ['Huddersfield', 'Stoke City'], ['Birmingham', 'Southampton'], ['Southampton', 'West Brom'], ['Hull City', 'Wolves'], ['Leeds', 'Swansea'], ['Brighton', 'Leicester'], ['Leicester', 'Manchester City'], ['Everton', 'Manchester United'], ['Aston Villa', 'Everton'], ['Blackpool', 'West Brom'], ['Everton', 'Luton'], ['Blackpool', 'Liverpool'], ['Fulham', 'West Ham'], ['Chelsea', 'Everton'], ['Crystal Palace', 'Fulham'], ['Blackburn', 'Crystal Palace'], ['Burnley', 'Hull City'], ['Middlesbrough', 'Sunderland'], ['Manchester United', 'Tottenham'], ['Blackpool', 'Sunderland'], ['Everton', 'Swansea'], ['Nottingham Forest', 'Watford'], ['Fulham', 'Wigan'], ['Bolton', 'Sunderland'], ['Norwich', 'Swansea'], ['QPR', 'Tottenham'], ['Bolton', 'Chelsea'], ['Hull City', 'Southampton'], ['Hull City', 'Leeds'], ['Aston Villa', 'Hull City'], ['Birmingham', 'Hull City'], ['Newcastle', 'Wigan'], ['Liverpool', 'Sheffield Utd'], ['Cardiff', 'Hull City'], ['Brighton', 'Crystal Palace'], ['Blackburn', 'Newcastle'], ['Arsenal', 'Bournemouth'], ['Cardiff', 'Swansea'], ['Fulham', 'Tottenham'], ['Burnley', 'Chelsea'], ['Bournemouth', 'Reading'], ['Liverpool', 'Wigan'], ['Arsenal', 'Everton'], ['Sheffield Utd', 'West Ham'], ['Brighton', 'Southampton'], ['Blackburn', 'Manchester United'], ['Chelsea', 'West Brom'], ['Blackpool', 'Sheffield Utd'], ['Chelsea', 'Nottingham Forest'], ['Manchester United', 'Stoke City'], ['Manchester City', 'West Brom'], ['Chelsea', 'Liverpool'], ['Nottingham Forest', 'Wolves'], ['Huddersfield', 'West Brom'], ['Bolton', 'Norwich'], ['Fulham', 'QPR'], ['Huddersfield', 'Nottingham Forest'], ['Bolton', 'Sheffield Utd'], ['Aston Villa', 'Chelsea'], ['Huddersfield', 'Liverpool'], ['Hull City', 'Swansea'], ['Chelsea', 'Sunderland'], ['Everton', 'Fulham'], ['Manchester City', 'Sunderland'], ['Arsenal', 'Brighton'], ['Crystal Palace', 'Leicester'], ['Crystal Palace', 'Reading'], ['Middlesbrough', 'Wigan'], ['Bolton', 'West Ham'], ['Newcastle', 'Watford'], ['Burnley', 'Norwich'], ['Manchester United', 'Middlesbrough'], ['Burnley', 'Sheffield Utd'], ['Brentford', 'Tottenham'], ['Brighton', 'Luton'], ['Bolton', 'Manchester City'], ['Aston Villa', 'Blackburn'], ['Cardiff', 'Fulham'], ['Stoke City', 'West Brom'], ['Burnley', 'West Ham'], ['Liverpool', 'Watford'], ['Birmingham', 'Blackburn'], ['Blackburn', 'Cardiff'], ['Liverpool', 'QPR'], ['Blackpool', 'Bolton'], ['Aston Villa', 'Norwich'], ['Arsenal', 'West Brom'], ['Bournemouth', 'Huddersfield'], ['Birmingham', 'Norwich'], ['Aston Villa', 'Sheffield Utd'], ['Arsenal', 'Nottingham Forest'], ['Arsenal', 'Liverpool'], ['Cardiff', 'Norwich'], ['Stoke City', 'Sunderland'], ['Burnley', 'Manchester City'], ['Chelsea', 'Sheffield Utd'], ['Watford', 'Wolves'], ['Arsenal', 'Sunderland'], ['Manchester City', 'Sheffield Utd'], ['Fulham', 'Middlesbrough'], ['Aston Villa', 'West Ham'], ['Manchester United', 'Newcastle'], ['Arsenal', 'Chelsea'], ['Middlesbrough', 'QPR'], ['Middlesbrough', 'Watford'], ['Chelsea', 'West Ham'], ['Newcastle', 'Wolves'], ['Blackpool', 'QPR'], ['Crystal Palace', 'Huddersfield'], ['Manchester City', 'West Ham'], ['Manchester United', 'West Brom'], ['Aston Villa', 'Manchester City'], ['Nottingham Forest', 'Swansea'], ['Birmingham', 'Manchester City'], ['Manchester United', 'Nottingham Forest'], ['Chelsea', 'Wigan'], ['Burnley', 'Tottenham'], ['Cardiff', 'Manchester City'], ['Tottenham', 'Watford'], ['Manchester City', 'Wigan'], ['Everton', 'Leicester'], ['Everton', 'Reading'], ['Manchester United', 'Sunderland'], ['QPR', 'West Brom'], ['Aston Villa', 'Birmingham'], ['Fulham', 'Leeds'], ['Aston Villa', 'Bolton'], ['Fulham', 'Newcastle'], ['QPR', 'Sunderland'], ['Liverpool', 'Middlesbrough'], ['Newcastle', 'Southampton'], ['Aston Villa', 'Tottenham'], ['Brighton', 'Fulham'], ['Arsenal', 'Norwich'], ['Reading', 'Tottenham'], ['Brentford', 'Everton'], ['West Ham', 'Wigan'], ['Birmingham', 'Tottenham'], ['Arsenal', 'Sheffield Utd'], ['Bolton', 'Stoke City'], ['Crystal Palace', 'Hull City'], ['Cardiff', 'Reading'], ['Fulham', 'Manchester United'], ['Southampton', 'Wolves'], ['Arsenal', 'West Ham'], ['Middlesbrough', 'Wolves'], ['West Brom', 'West Ham'], ['Brentford', 'Brighton'], ['Liverpool', 'Southampton'], ['Stoke City', 'Wigan'], ['Blackpool', 'Middlesbrough'], ['Chelsea', 'QPR'], ['Tottenham', 'Wolves'], ['Manchester United', 'Sheffield Utd'], ['Burnley', 'Stoke City'], ['Manchester City', 'QPR'], ['Liverpool', 'Newcastle'], ['Huddersfield', 'QPR'], ['Bolton', 'Middlesbrough'], ['Blackburn', 'Burnley'], ['Manchester City', 'Watford'], ['Everton', 'Huddersfield'], ['Blackburn', 'Leicester'], ['Newcastle', 'Swansea'], ['Leicester', 'Norwich'], ['Leicester', 'Sheffield Utd'], ['Luton', 'Sheffield Utd'], ['Middlesbrough', 'Southampton'], ['Arsenal', 'Bolton'], ['Aston Villa', 'Stoke City'], ['Reading', 'Stoke City'], ['Birmingham', 'Stoke City'], ['Manchester United', 'Wigan'], ['Arsenal', 'Tottenham'], ['Sheffield Utd', 'West Brom'], ['Sunderland', 'West Brom'], ['Burnley', 'Middlesbrough'], ['Brentford', 'Liverpool'], ['Cardiff', 'Stoke City'], ['Luton', 'West Ham'], ['Leicester', 'West Ham'], ['Bournemouth', 'Norwich'], ['Liverpool', 'Swansea'], ['Bournemouth', 'Sheffield Utd'], ['Sheffield Utd', 'Sunderland'], ['Stoke City', 'Watford'], ['Birmingham', 'Everton'], ['Aston Villa', 'Middlesbrough'], ['Arsenal', 'QPR'], ['Everton', 'Hull City'], ['Cardiff', 'Everton'], ['Bournemouth', 'West Ham'], ['Bolton', 'West Brom'], ['Chelsea', 'Middlesbrough'], ['Huddersfield', 'Wolves'], ['Bolton', 'Liverpool'], ['Chelsea', 'Crystal Palace'], ['Manchester City', 'Middlesbrough'], ['Southampton', 'Swansea'], ['Crystal Palace', 'Norwich'], ['Aston Villa', 'Brighton'], ['Middlesbrough', 'Swansea'], ['Bournemouth', 'Manchester City'], ['Burnley', 'Newcastle'], ['Leicester', 'Tottenham'], ['West Ham', 'Wolves'], ['Burnley', 'West Brom'], ['Manchester United', 'QPR'], ['Manchester United', 'Watford'], ['Crystal Palace', 'West Ham'], ['Burnley', 'Nottingham Forest'], ['Chelsea', 'Leeds'], ['Burnley', 'Liverpool'], ['Aston Villa', 'Newcastle'], ['Huddersfield', 'Southampton'], ['Burnley', 'Sunderland'], ['QPR', 'Watford'], ['Crystal Palace', 'Manchester City'], ['Bournemouth', 'Tottenham'], ['Chelsea', 'Newcastle'], ['Luton', 'Watford'], ['Aston Villa', 'West Brom'], ['Manchester City', 'Newcastle'], ['Reading', 'West Brom'], ['Birmingham', 'West Brom'], ['Brighton', 'Huddersfield'], ['Sunderland', 'West Ham'], ['Aston Villa', 'Liverpool'], ['Cardiff', 'West Brom'], ['Arsenal', 'Middlesbrough'], ['Cardiff', 'Nottingham Forest'], ['Aston Villa', 'Sunderland'], ['Cardiff', 'Liverpool'], ['Birmingham', 'Sunderland'], ['Brighton', 'Everton'], ['Sunderland', 'Wigan'], ['Chelsea', 'Manchester United'], ['Fulham', 'Watford'], ['Leeds', 'Norwich'], ['Blackburn', 'Swansea'], ['Cardiff', 'Sunderland'], ['Manchester City', 'Manchester United'], ['Crystal Palace', 'Tottenham'], ['Leicester', 'Stoke City'], ['Blackpool', 'Wigan'], ['Everton', 'Norwich'], ['Leeds', 'West Ham'], ['Fulham', 'Leicester'], ['Everton', 'Sheffield Utd'], ['Bolton', 'Wigan'], ['Brighton', 'Hull City'], ['Sunderland', 'Tottenham'], ['Arsenal', 'Newcastle'], ['Leeds', 'Manchester City'], ['Bournemouth', 'Stoke City'], ['Hull City', 'Sunderland'], ['Everton', 'West Ham'], ['Leicester', 'Middlesbrough'], ['Newcastle', 'Reading'], ['Swansea', 'West Ham'], ['Norwich', 'West Ham'], ['Manchester United', 'Southampton'], ['Everton', 'Manchester City'], ['Burnley', 'Wigan'], ['Arsenal', 'Manchester United'], ['Fulham', 'Wolves'], ['Cardiff', 'Sheffield Utd'], ['Bournemouth', 'Everton'], ['Brighton', 'Liverpool'], ['Bournemouth', 'Middlesbrough'], ['Crystal Palace', 'Stoke City'], ['QPR', 'Southampton'], ['Stoke City', 'Swansea'], ['Birmingham', 'West Ham'], ['Brighton', 'Sunderland'], ['Cardiff', 'West Ham'], ['Blackpool', 'Watford'], ['Aston Villa', 'Wigan'], ['Brighton', 'Chelsea'], ['Birmingham', 'Wigan'], ['Bournemouth', 'Brighton'], ['Leicester', 'Newcastle'], ['Luton', 'Newcastle'], ['Everton', 'Tottenham'], ['Bolton', 'QPR'], ['Blackburn', 'Norwich'], ['Hull City', 'Norwich'], ['Swansea', 'Tottenham'], ['Crystal Palace', 'Everton'], ['Fulham', 'Huddersfield'], ['Fulham', 'Southampton'], ['Blackpool', 'Burnley'], ['Norwich', 'Tottenham'], ['Leicester', 'West Brom'], ['Crystal Palace', 'Middlesbrough'], ['Leicester', 'Nottingham Forest'], ['Blackpool', 'Leicester'], ['Leicester', 'Liverpool'], ['Liverpool', 'Wolves'], ['Bolton', 'Burnley'], ['Manchester United', 'Swansea'], ['Leicester', 'Manchester United'], ['Luton', 'Manchester United'], ['Hull City', 'West Ham'], ['Bournemouth', 'Newcastle'], ['Burnley', 'Watford'], ['Burnley', 'QPR'], ['Sheffield Utd', 'Wolves'], ['Cardiff', 'Tottenham'], ['Bournemouth', 'West Brom'], ['Blackburn', 'Manchester City'], ['Brighton', 'Norwich'], ['Bournemouth', 'Nottingham Forest'], ['Bournemouth', 'Liverpool'], ['Bournemouth', 'Sunderland'], ['Fulham', 'Luton'], ['Fulham', 'Hull City'], ['Aston Villa', 'QPR'], ['Aston Villa', 'Watford'], ['Reading', 'Watford'], ['Crystal Palace', 'Newcastle'], ['Birmingham', 'Watford'], ['Bournemouth', 'Chelsea'], ['Brighton', 'West Ham'], ['Arsenal', 'Wigan'], ['Fulham', 'Swansea'], ['Chelsea', 'Watford'], ['Cardiff', 'QPR'], ['West Brom', 'Wigan'], ['Everton', 'Stoke City'], ['Blackpool', 'Crystal Palace'], ['Sheffield Utd', 'Southampton'], ['Crystal Palace', 'West Brom'], ['Hull City', 'Tottenham'], ['Blackburn', 'Tottenham'], ['Aston Villa', 'Burnley'], ['Norwich', 'Stoke City'], ['Crystal Palace', 'Nottingham Forest'], ['Bolton', 'Crystal Palace'], ['Crystal Palace', 'Liverpool'], ['Leeds', 'Middlesbrough'], ['Blackburn', 'Reading'], ['Brentford', 'Newcastle'], ['Crystal Palace', 'Sunderland'], ['Watford', 'West Brom'], ['Blackpool', 'Southampton'], ['Chelsea', 'Leicester'], ['Burnley', 'Wolves'], ['Everton', 'Middlesbrough'], ['Huddersfield', 'Leicester'], ['Bolton', 'Leeds'], ['Burnley', 'Crystal Palace'], ['Brentford', 'Manchester United'], ['Newcastle', 'Nottingham Forest'], ['Nottingham Forest', 'West Ham'], ['Brighton', 'Tottenham'], ['Newcastle', 'Sunderland'], ['Aston Villa', 'Wolves'], ['Sheffield Utd', 'Swansea'], ['Arsenal', 'Watford'], ['Chelsea', 'Wolves'], ['Burnley', 'Southampton'], ['Aston Villa', 'Crystal Palace'], ['Manchester City', 'Wolves'], ['Birmingham', 'Crystal Palace'], ['Cardiff', 'Middlesbrough'], ['Arsenal', 'Brentford'], ['Leeds', 'West Brom'], ['Hull City', 'Stoke City'], ['Blackburn', 'Stoke City'], ['Cardiff', 'Crystal Palace'], ['Bolton', 'Manchester United'], ['Everton', 'Newcastle'], ['Fulham', 'Norwich'], ['Aston Villa', 'Southampton'], ['Everton', 'West Brom'], ['Reading', 'Southampton'], ['Bolton', 'Swansea'], ['Nottingham Forest', 'Tottenham'], ['Swansea', 'West Brom'], ['Chelsea', 'Huddersfield'], ['Everton', 'Liverpool'], ['Chelsea', 'Southampton'], ['Blackburn', 'Everton'], ['Norwich', 'West Brom'], ['Manchester City', 'Southampton'], ['Burnley', 'Manchester United'], ['Hull City', 'Middlesbrough'], ['Everton', 'Sunderland'], ['Norwich', 'Nottingham Forest'], ['Newcastle', 'Norwich'], ['Crystal Palace', 'Wigan'], ['Brighton', 'Stoke City'], ['Newcastle', 'Sheffield Utd'], ['Watford', 'West Ham'], ['Tottenham', 'West Brom'], ['Norwich', 'Sunderland'], ['Stoke City', 'Wolves'], ['Burnley', 'Swansea'], ['West Brom', 'Wolves'], ['Fulham', 'Manchester City'], ['Wigan', 'Wolves'], ['Watford', 'Wigan'], ['Newcastle', 'West Ham'], ['Aston Villa', 'Manchester United']]

list_of_teams = ["Chelsea",
"Middlesbrough",
"Bournemouth",
"Burnley",
"Everton",
"West Ham",
"Hull City",
"Leeds",
"Birmingham",
"West Brom",
"Huddersfield",
"Manchester City",
"Blackpool",
"Reading",
"Fulham",
"Brentford",
"Blackburn",
"Sunderland",
"Brighton",
"Manchester United",
"Newcastle",
"QPR",
"Sheffield Utd",
"Wolves",
"Tottenham",
"Aston Villa",
"Leicester",
"Stoke City",
"Swansea",
"Cardiff",
"Norwich",
"Liverpool",
"Wigan",
"Crystal Palace",
"Arsenal",
"Nottingham Forest",
"Luton",
"Watford",
"Southampton",
"Bolton"]


def count_frequency_of_club(list_of_teams,unique_combo_of_teams):
    #This tells us the frequency of of clubs appearing in the combos. I.e.
    count_dict = {}
    for team in list_of_teams:
        counter = 0
        for combo in unique_combo_of_teams:
            if team in combo:
                counter += 1
        count_dict[team] = counter
    count_of_team_list = sorted(count_dict.items(), key = lambda x:x[1], reverse=True)
    return count_of_team_list
'''
This is the returned count_of_team_list. For teams a and x we should choose teams over 30. If we have brentford as team a for exmaple we will be screwed.

[('Everton', 36), ('West Ham', 36), ('West Brom', 36), ('Aston Villa', 36), ('Crystal Palace', 36), ('Fulham', 34), ('Manchester United', 34), ('Liverpool', 33), ('Chelsea', 32), ('Burnley', 32), ('Manchester City', 32), ('Sunderland', 32), ('Newcastle', 32), ('Norwich', 32), ('Tottenham', 31), ('Stoke City', 31), ('Swansea', 31), ('Wolves', 29), ('Middlesbrough', 28), ('Bournemouth', 28), ('Leicester', 28), ('Watford', 28), ('Southampton', 28), ('QPR', 27), ('Arsenal', 27), ('Cardiff', 26), ('Hull City', 25), ('Brighton', 25), ('Wigan', 25), ('Bolton', 23), ('Sheffield Utd', 22), ('Blackburn', 21), ('Nottingham Forest', 21), ('Birmingham', 20), ('Huddersfield', 20), ('Blackpool', 16), ('Reading', 15), ('Leeds', 14), ('Luton', 13), ('Brentford', 9)]
'''

def return_all_combo_for_team_name(unique_combo_of_teams, team_name_to_check,team_name_to_remove):
    matching_team_combos = []
    for combo in unique_combo_of_teams:
        if team_name_to_check in combo:
            matching_team_combos.append(combo)
    #Dom edit 15.09 - Removed the combo of team_a and team_x as a selection
    for combo in matching_team_combos:
        if [team_name_to_check,team_name_to_remove] in matching_team_combos:
           matching_team_combos.remove([team_name_to_check,team_name_to_remove])
        elif [team_name_to_remove, team_name_to_check] in matching_team_combos:
            matching_team_combos.remove([team_name_to_remove, team_name_to_check])
    return matching_team_combos

def return_all_combo_for_two_team_names(unique_combo_of_teams, team_name_1, team_name_2):
    print(f'Team name 1: is {team_name_1}')
    print(f'Team name 2: is {team_name_2}')
    
    matching_team_combos_1 = []
    matching_team_combos_2 = []
    for combo in unique_combo_of_teams:
        # Get all possible matching combos [x,y] that have team_1 in it
        if team_name_1 in combo:
            matching_team_combos_1.append(combo)
        # Get all possible matching combos [x,y] that have team_2 in it
        if team_name_2 in combo:
            matching_team_combos_2.append(combo)
    print(f'{team_name_1} matching list is: {matching_team_combos_1}')
    print(f'{team_name_2} matching list is: {matching_team_combos_2}')
    matching_combo = [combo for combo in matching_team_combos_2 if combo in matching_team_combos_1]
    print(f'Combo for both {team_name_1} and {team_name_2} is: {matching_combo}')
    list_without_team_original_combo = [combo for combo in matching_combo if combo != [team_name_1, team_name_2] and combo != [team_name_2, team_name_1]]
    if len(list_without_team_original_combo) < 1:
        return 'No match found'
    else: 
        return list_without_team_original_combo

def return_all_combo_for_three_team_names(unique_combo_of_teams, team_name_1, team_name_2, team_name_3):
    matching_team_combos_1 = []
    matching_team_combos_2 = []#
    matching_team_combos_3 = []

    for combo in unique_combo_of_teams:
        if team_name_1 in combo:
            matching_team_combos_1.append(combo)
        if team_name_2 in combo:
            matching_team_combos_2.append(combo)
        if team_name_3 in combo:
            matching_team_combos_3.append(combo)
    matching_combo_1_2 = [combo for combo in matching_team_combos_2 if combo in matching_team_combos_1]
    matching_combo_1_2_3 = [combo for combo in matching_combo_1_2 if combo in matching_team_combos_3]

    if len(matching_combo_1_2_3) < 1:
        return 'No match found'
    else: 
        return matching_combo_1_2_3

def main():
    
    #Step 1: Chose random team combo
    #TODO make random_combo a selection of the top 10 teams. We should also randomise the ordering of x,y,z and a,b,c to switch it up.
    random_combo = random.choice(unique_combo_of_teams)
    print(random_combo)
    #Step 2: Do first match
    team_a = random_combo[0]
    team_x = random_combo[1]

    possible_team_a_matches = return_all_combo_for_team_name(unique_combo_of_teams,team_a,team_x)
    possible_team_x_matches = return_all_combo_for_team_name(unique_combo_of_teams,team_x,team_a)
    #Step 3: next match
    #TODO: When selecting team y there is no check to see if there is a match with team b.
    possible_team_y_combo = random.choice(possible_team_a_matches)
    team_y = [team_name for team_name in possible_team_y_combo if team_name != team_a][0]
    possible_team_b_combo = random.choice(possible_team_x_matches)
    team_b = [team_name for team_name in possible_team_b_combo if team_name != team_x][0]

    team_y_and_x_matches: list = return_all_combo_for_two_team_names(unique_combo_of_teams,team_x,team_y)
    team_a_and_b_matches: list = return_all_combo_for_two_team_names(unique_combo_of_teams,team_a,team_b)

    #Step 4: 
    team_z = random.choice(team_a_and_b_matches)
    team_c = random.choice(team_y_and_x_matches)
    team_x_y_z_matches: list = return_all_combo_for_three_team_names(unique_combo_of_teams,team_x,team_y,team_z)
    team_a_b_c_matches: list = return_all_combo_for_three_team_names(unique_combo_of_teams,team_a,team_b, team_c)

    


    
    # matching_team_combo = return_all_combo_for_team_name(unique_combo_of_teams,'Tottenham')
    # print(matching_team_combo)
    
if __name__ == "__main__":
    main()