from flask_pkg.project.routes import BASE, get_request
from data.data_db_functions import update_guesses_count_in_db, get_guess_from_db, post_guess_to_db
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
    print(total_list)
    correct_players = find_duplicate_names(total_list)
    return correct_players


def all_correct_answers(team_a, team_b) -> list:
    team_a_dict = get_request(BASE, f'team_from_name/{team_a}')
    team_b_dict = get_request(BASE, f'team_from_name/{team_b}')
    team_id_a = team_a_dict['team_id']
    team_id_b = team_b_dict['team_id']
    team_a_players = get_all_players_for_team_id(team_id_a)
    team_b_players = get_all_players_for_team_id(team_id_b)
    correct_players = get_players_for_two_teams(team_a_players,team_b_players)
    return correct_players

#TODO: Get total number of guesses for each players
def total_number_of_guess(all_possible_players) -> dict:
    # Get guesses list of players from DB guesses table


    # Ouput from GET request
    player_guess_dict = {'player_a': 1,
                        'player_b': 2,
                        'player_c': 3}
    
    return player_guess_dict

#TODO: Get the relative score of chosen player
def score_for_selected_player(player, player_guess_dict):
    player_score = 0
    # Code to get the percentage score of each player based on number of guesses

    return player_score


def update_guesses_table(player_full_name: str,two_team_combo: list[str]):
    two_team_combo = sorted(two_team_combo)
    #Step 1: Create identifier
    single_player_identifier= player_full_name+'~'+two_team_combo[0]+'~'+two_team_combo[1]
    # Step 1: See if combo exists already
    if get_guess_from_db(single_player_identifier):
        update_guesses_count_in_db(single_player_identifier)
    else:
        new_guess = [Guess(full_name=player_full_name, team_1=two_team_combo[0], team_2=two_team_combo[1])]
        post_guess_to_db(new_guess)
    


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

    update_guesses_table('Tom-Diamond',['Chelsea','Tottenham'])


if __name__ == "__main__":
    main()

    