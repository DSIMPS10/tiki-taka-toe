import pytest
from pandas import DataFrame

from src.app import (
    get_six_random_indices,
    get_teams_from_indices,
    get_teams_for_selected_player_from_db, 
    get_teams_from_grid_index,
    compare_player,
    create_six_team_df_for_grid,
    convert_print_grid_as_df,
    create_footy_team_board
)
from src.utils.classes import Grid

####################################################################################################################
### INPUTS ###
####################################################################################################################

@pytest.fixture
def team_df() -> DataFrame:
    team_data = {"pos_1":["Tottenham","Chelsea"],
           "pos_2":["West Ham","Liverpool"],
           "pos_3": ["Man City","Bayern Munich"]}

    team_df = DataFrame(team_data)
    return team_df

@pytest.fixture
def players_df() -> DataFrame:
    player_data = {
    "Name": ['Raheem Sterling', 'Kai Havertz', 'Harry Kane'],
    "Team": [['Chelsea', 'Man City', 'Liverpool'], ['Chelsea','Arsenal'], ['Tottenham', 'Bayern Munich']]
        }

    players_df = DataFrame(player_data)
    return players_df

@pytest.fixture
def grid() -> Grid:
    return Grid()

####################################################################################################################
### TESTS ###
####################################################################################################################

def test_get_six_random_indices():
    test_list = get_six_random_indices()
    assert len(test_list) == 6
    assert type(test_list[0]) is int

def test_get_teams_for_selected_player_from_db(players_df):
    player_name = 'Raheem Sterling'
    team_list = get_teams_for_selected_player_from_db(players_df,player_name)
    assert len(team_list) == 3
    assert team_list[0] == 'Chelsea'
    assert 'Tottenham' not in team_list

def test_get_teams_from_grid_index(grid, team_df):
    pos_number = 2
    selected_teams = get_teams_from_grid_index(team_df, grid, pos_number)
    team_a = selected_teams[0]
    team_b = selected_teams[1]
    assert team_a == 'West Ham'
    assert team_b == 'Bayern Munich'
    assert len(selected_teams) == 2

def test_compare_player(players_df):
    correct_name = 'Harry Kane'
    incorrect_name = 'Kai Havertz'
    selected_teams = ['Tottenham', 'Bayern Munich']
    assert compare_player(players_df, correct_name, selected_teams) == True
    assert compare_player(players_df, incorrect_name, selected_teams) == False
    
# def test_compare_player_invalid_input(players_df):
#     invalid_guess = ''
#     selected_teams = ['Tottenham', 'Bayern Munich']
#     with pytest.raises(ValueError) as excinfo:  
#         compare_player(players_df, invalid_guess, selected_teams)  
#     assert str(excinfo.value) == 'Please input a players name as a guess.'
    
def test_get_teams_from_indices():
    indices_list = [0,1]
    test_list = get_teams_from_indices(indices_list)
    assert test_list[0] == 'Arsenal'
    assert test_list[1] == 'Aston Villa'
    assert len(test_list) == 2
    assert type(test_list) is list
    
def test_create_six_team_df_for_grid():
    test_list = ["Tottenham","Chelsea","West Ham","Liverpool","Man City","Bayern Munich"]
    test_df = create_six_team_df_for_grid(test_list)
    assert test_df.columns.to_list() == ['pos_1', 'pos_2', 'pos_3']
    assert test_df['pos_1'].count() == 2
    assert len(test_df['pos_2'].values.tolist()) == 2
    assert type(test_df['pos_3'][0]) is str

def test_print_grid_as_df():
    test_list = ["Tottenham","Chelsea","West Ham","Liverpool","Man City","Bayern Munich"]
    test_df = convert_print_grid_as_df(test_list)
    assert type(test_df) is DataFrame

def test_create_footy_team_board():
    test_df = create_footy_team_board()
    assert type(test_df) is DataFrame
