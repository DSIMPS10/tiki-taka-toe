import pytest
import pandas as pd

from src.app import get_teams_for_selected_player_from_db
# from utils.classes import Grid

####################################################################################################################
### INPUTS ###
####################################################################################################################

@pytest.fixture
def team_df() -> pd.DataFrame:
    team_data = {"pos_1":["Tottenham","Chelsea"],
           "pos_2":["West Ham","Liverpool"],
           "pos_3": ["Man City","Bayern Munich"]}

    team_df = pd.DataFrame(team_data)
    return team_df

@pytest.fixture
def players_df() -> pd.DataFrame:
    player_data = {
    "Name": ['Raheem Sterling', 'Kai Havertz', 'Harry Kane'],
    "Team": [['Chelsea', 'Man City', 'Liverpool'], ['Chelsea','Arsenal'], ['Tottenham', 'Bayern Munich']]
        }

    players_df = pd.DataFrame(player_data)
    return players_df

# @pytest.fixture
# def grid() -> Grid:
#     return Grid()

def test_get_teams_for_selected_player_from_db(players_df):
    player_name = 'Raheem Sterling'
    team_list = get_teams_for_selected_player_from_db(players_df,player_name)
    assert len(team_list) == 3


####################################################################################################################
### TESTS ###
####################################################################################################################

def test_get_one_team_for_selected_player_from_db(players_df):
    player_name = 'Raheem Sterling'
    team_list = app.get_teams_for_selected_player_from_db(players_df,player_name)
    assert team_list[0] == 'Chelsea'

def test_get_teams_from_grid_index(grid, team_df):
    pos_number = 2
    selected_teams = app.get_teams_from_grid_index(team_df, grid, pos_number)
    team_a = selected_teams[0]
    assert team_a == 'Tottenham'

def test_get_teams_from_grid_index_length(grid, team_df):
    pos_number = 2
    selected_teams = app.get_teams_from_grid_index(team_df, grid, pos_number)
    assert len(selected_teams) == 2

def test_compare_player_correct(players_df):
    player_name = 'Harry Kane'
    selected_teams = ['Tottenham', 'Bayern Munich']
    answer = app.compare_player(players_df, player_name, selected_teams)
    assert answer == True

def test_compare_player_incorrect(players_df):
    player_name = 'Kai Havertz'
    selected_teams = ['Tottenham', 'Bayern Munich']
    answer = app.compare_player(players_df, player_name, selected_teams)
    assert answer == False
    
def test_get_teams_from_indices():
    indices_list = [0,1]
    test_list = app.get_teams_from_indices(indices_list)
    assert test_list[0] == 'Arsenal'