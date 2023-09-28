import math

from flask_pkg.project.routes import BASE, get_request
from data.data_db_functions import (update_guesses_count_in_db, 
                                    get_guess_from_db, 
                                    post_guess_to_db, 
                                    check_team_combo_has_matching_player,
                                    get_all_valid_guesses)
from utils.classes import Guess

##########################################################################################################
### SCORING ###
##########################################################################################################

def get_all_players_for_team_id(team_id):
    team_players_dict = get_request(BASE, f'get_players_for_team_id/{team_id}')
    return team_players_dict


def find_duplicate_names(list_of_players):
    # If a player is duplicated they have played for both teams
    seen = set()
    duplicates = []   
    for name in list_of_players:
        if name in seen:
            duplicates.append(name)
        else:
            seen.add(name)
    return duplicates


def get_players_for_two_teams(team_players_dict_a, team_players_dict_b):
    total_list = []
    for player in team_players_dict_a:
        total_list.append(player['full_name'])
    for player in team_players_dict_b:
        total_list.append(player['full_name'])
    #print(total_list)
    correct_players = find_duplicate_names(total_list)
    return correct_players


def update_guesses_table(player_full_name: str,two_team_combo: list[str]):
    '''
    Function to update the guesses table with correct guess count based on a player and team combo
    '''
    
    # Sort the team alphabetically
    two_team_combo = sorted(two_team_combo)
    # Create custome player team identifier
    single_player_identifier= player_full_name+'~'+two_team_combo[0]+'~'+two_team_combo[1]
    # Post new guess if it hasn't been already guessed, or update if it has 
    if get_guess_from_db(single_player_identifier):
        update_guesses_count_in_db(single_player_identifier)
    else:
        new_guess = [Guess(full_name=player_full_name, team_1=two_team_combo[0], team_2=two_team_combo[1])]
        post_guess_to_db(new_guess)


def get_guess_score(player_full_name: str,two_team_combo: list[str]) -> dict:
    '''
    Get the score of a correctly guess player for a two team combo
    Outputs: dict with the score for player
    '''
    
    # Step 1: get all valid players from players table
    list_of_all_valid_players = check_team_combo_has_matching_player(two_team_combo[0], two_team_combo[1])
    total_valid_count: int = len(list_of_all_valid_players)
    #print(f'The total number of valid players that could have been selected: {total_valid_count}')
    
    # Step 2: get all existing guesses for two team combo
    all_valid_guesses = get_all_valid_guesses(two_team_combo)
    # print(all_valid_guesses)
    guesses_only_df = all_valid_guesses[['full_name', 'correct_guesses']]
    guesses_only_df = guesses_only_df.set_index('full_name')
    # print(guesses_only_df)
    scoring_dict = guesses_only_df.to_dict(orient='dict')['correct_guesses']
    # print(scoring_dict)
    
    # Step 3: Assign a score
    total_number_of_players_never_guessed = total_valid_count - len(guesses_only_df) # i.e. 0 correct guesses so far
    #print(f'The total number of players never guessed for this combo: {total_number_of_players_never_guessed}')
    sum_of_all_guesses_for_team_combo = guesses_only_df['correct_guesses'].sum()
    #print(f'The total sum of all guesses for this combo: {sum_of_all_guesses_for_team_combo}')
    # Step 4: get number of guesses for selected player
    selected_player_guess_count = scoring_dict[player_full_name]
    #print(f'The total number of guesses for selected player: {selected_player_guess_count}')
    list_of_all_guesses = [*scoring_dict.values()]
    if total_number_of_players_never_guessed > 0:
        for i in range(total_number_of_players_never_guessed):
            list_of_all_guesses.append(0)
            i +=1
    list_of_all_guesses = sorted(list_of_all_guesses)
    # print(list_of_all_guesses)
    # percentage_guess = round(selected_player_guess_count/sum_of_all_guesses_for_team_combo,2)
    # print(percentage_guess)
    score = score_allocation(list_of_all_guesses, selected_player_guess_count)
    if score > 10: score = 10
    print(f'Score for {player_full_name} is: {score}')
    return {'Selected player': player_full_name, 'Score': score}
    
def score_allocation(list_of_scores: list[int], selected_score: int):
    '''
    Get score based on total list of all guess counts by index
    '''
    index_of_score = list_of_scores.index(selected_score)
    score = len(list_of_scores)-index_of_score
    return score
    
    
def set_score_allocation(list_of_scores: list[int], selected_score: int):
    '''
    Get a score based on the unique number of guess counts by index
    '''
    unique_score = set(list_of_scores)
    index_of_score = list(unique_score).index(selected_score)
    score = len(unique_score)-index_of_score
    return score


def scoring_process():
    '''
    Assumptions: A correct guess in an already formed grid
    Inputs:two teams and a string player guess
    '''
    #Step 1: Update the Guesses DB
    # sorted_team_combo = sorted(two_team_combo)
    # update_guesses_table(player_full_name: str, sorted_team_combo: list)
    pass


def main():
    # update_guesses_table('Tom-Diamond',['Chelsea','Tottenham'])
    manually_update_guesses = False
    if manually_update_guesses: 
        player_names = ['Fabio Borini', 'Raul José Trindade Meireles', 'Mohamed Salah Hamed Mahrous Ghaly', 'Daniel Andre Sturridge', 'Yossi Shai Benayoun', 'Raheem Shaquille Sterling', 'Victor Moses', 'Fernando José Torres Sanz', 'Joe Cole', 'Dominic Ayodele Solanke']
        round_2_names = ['Mohamed Salah Hamed Mahrous Ghaly', 'Daniel Andre Sturridge', 'Yossi Shai Benayoun', 'Raheem Shaquille Sterling', 'Victor Moses', 'Fernando José Torres Sanz', 'Joe Cole']
        round_3_names = ['Mohamed Salah Hamed Mahrous Ghaly', 'Daniel Andre Sturridge', 'Raheem Shaquille Sterling', 'Joe Cole']
        round_4_names = ['Raheem Shaquille Sterling', 'Joe Cole']

        two_team_combo = ['Chelsea', 'Liverpool']
        for player in round_4_names:
            update_guesses_table(player, two_team_combo)
            
    two_team_combo = ['Chelsea', 'Liverpool']
    low_score_player_name = 'Raheem Shaquille Sterling'
    med_score_player_name = 'Victor Moses'
    high_score_player_name = 'Fabio Borini'
    get_guess_score(low_score_player_name, two_team_combo)
    get_guess_score(med_score_player_name, two_team_combo)
    get_guess_score(high_score_player_name, two_team_combo)



if __name__ == "__main__":
    main()

    