from src.flask_pkg.project.routes import BASE, get_request

def get_all_players_for_team_id(team_id):
    team_players_dict = get_request(BASE, f'get_players_for_team_id/{team_id}')
    return team_players_dict

def combine_names(player_dict):
    full_name = f'{player_dict["first_name"]} {player_dict["last_name"]}'
    team_id = player_dict['team_id']
    new_dict = {full_name: team_id}
    return new_dict

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
        new_dict = combine_names(player)
        total_list.append(new_dict.keys())
    for player in team_players_dict_b:
        new_dict = combine_names(player)
        total_list.append(new_dict.keys())
    correct_players = find_duplicate_names(total_list)
    return correct_players

#TODO: Get all available players which have played for both teams once a grid position has been picked
def all_correct_answers(team_a, team_b) -> list:
    team_a_dict = get_request(BASE, f'team_from_name/{team_a}')
    team_b_dict = get_request(BASE, f'team_from_name/{team_b}')
    team_id_a = team_a_dict['id']
    team_id_b = team_b_dict['id']
    taam_a_players = get_all_players_for_team_id(team_id_a)
    team_b_players = get_all_players_for_team_id(team_id_b)
    correct_players = get_players_for_two_teams(taam_a_players,team_b_players)
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

    