import pandas as pd
from flask_pkg.project.routes import get_request, post_request,put_request, BASE 
from data.data_db_functions import get_valid_guesses_from_db, get_player_info_from_name_db, post_valid_player_combos
from utils.classes import Guesses

def get_player_info_from_name(list_of_full_names: list[str])-> pd.DataFrame:
    combined_player_df = pd.DataFrame(columns = ['id', 'full_name', 'team_id', 'team_name', 'first_season', 'last_season'])
    for player in list_of_full_names:
        player_info_df = get_player_info_from_name_db(player)
        combined_player_df = pd.concat([combined_player_df,player_info_df])
    combined_player_df.reset_index(inplace=True)
    return combined_player_df

def melt_guesses_to_dict(valid_players_df: pd.DataFrame) -> dict:
    player_dict ={}
    for i in range(len(valid_players_df)):
        player_name = valid_players_df.loc[i, "full_name"]
        if player_name in player_dict:
            player_dict[player_name].append(valid_players_df.loc[i, "team_name"])
        else:
            player_dict[player_name] = [valid_players_df.loc[i, "team_name"]]
    return player_dict

def convert_guess_dict_to_obj(player_dict: dict) -> list[Guesses]:
    player_list = []
    for player_name, player_teams in player_dict.items():
        player = Guesses(player=player_name, team_combo=player_teams,correct_guesses=0)
        player_list.append(player)
    return player_list

def run_process():
    test_list = ['James Oliver Charles Tomkins', 'Jean Philippe', 'Fábio Pereira da Silva', 'Darren Edward Andrew Randolph', 'Ademola Lookman Olajade Alade Aylola Lookman', 'Robert Huth', 'Kai Lukas Havertz', 'Kurt Happy Zouma', 'Ayoze Pérez Gutiérrez', 'Lazar Marković', 'Jeffrey Schlupp', 'Nathan Michael Collins', 'Hélder Wander Sousa de Azevedo e Costa', 'Sonny Tufail Perkins', 'Saido Berahino', 'Jesse Ellis Lingard']
    #Step 1: Get valid players from db
    valid_players: list[str] = get_valid_guesses_from_db()
    #Step 2: Convert valid players name list to player df
    valid_players_df: pd.DataFrame = get_player_info_from_name(test_list)
    #Step 3: Convert player df to guess df (melt?)
    melted_dict: dict = melt_guesses_to_dict(valid_players_df)
    #Step 4: Convert dict to guess objects
    guess_list: list[Guesses] = convert_guess_dict_to_obj(melted_dict)
    print(guess_list)
    #Step 5: Post guess list to guesses table
    posted_combos = post_valid_player_combos(guess_list)
    print(posted_combos)

def main():
    run_process()

if __name__ == "__main__":
    main()

