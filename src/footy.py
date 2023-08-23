import pandas as pd
from app_objects import Grid

def get_teams_for_selected_player_from_db(df, player_name):
    teams: list = df.loc[df['Name'] == player_name]['Team'].values[0]  
    return teams


def get_teams_from_grid_index(team_df, grid: Grid, pos_number):
    pos_list = grid.number_to_index(pos_number)
    row_a = pos_list[0]-1
    row_b = pos_list[1]-1
    teams_x = team_df.iloc[0].values
    teams_y = team_df.iloc[1].values
    selected_teams = [teams_x[row_a],teams_y[row_b]]
    return selected_teams

    
def compare_player(df, player_name, selected_teams) -> bool: 
    '''
    This function will return true if the player has played for both teams
    '''
    teams_of_player = get_teams_for_selected_player_from_db(df, player_name)

    if selected_teams[0] in teams_of_player and selected_teams[1] in teams_of_player:
        return True
    
    return False

def main(pos_number):
    ### INPUTS ###
    team_data = {"pos_1":["Tottenham","Chelsea"],
           "pos_2":["West Ham","Liverpool"],
           "pos_3": ["Man City","Bayern Munich"]}

    team_df = pd.DataFrame(team_data)

    data_nosql = {
    "Name": ['Raheem Sterling', 'Kai Havertz', 'Harry Kane'],
    "Team": [['Chelsea', 'Man City', 'Liverpool'], ['Chelsea','Arsenal'], ['Tottenham', 'Bayern Munich']]
        }

    players_df = pd.DataFrame(data_nosql)

    grid = Grid()

    ### FUNCTIONS ###
    player_name = "Harry Kane"
    selected_teams = get_teams_from_grid_index(team_df, grid, pos_number)
    answer = compare_player(players_df, player_name, selected_teams)
    return answer 

if __name__ == "__main__":
    pos_guess = int(input("Choose a grid number"))
    answer = main(pos_guess)
    print(answer)



