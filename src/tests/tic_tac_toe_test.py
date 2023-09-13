import pytest
from pandas import DataFrame

import src.app as app
from src.tic_tac_toe import (
    print_board,
    check_winner,
    switch_turn,
    restart_game,
    check_move,
    game
)

####################################################################################################################
### INPUTS ###
####################################################################################################################

@pytest.fixture
def test_board() -> dict:
    the_board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
    return the_board

@pytest.fixture
def team_df() -> DataFrame:
    team_data = {"pos_1":["Tottenham","Chelsea"],
           "pos_2":["West Ham","Liverpool"],
           "pos_3": ["Man City","Bayern Munich"]}

    team_df = DataFrame(team_data)
    return team_df

####################################################################################################################
### TESTS ###
####################################################################################################################


def test_print_board(test_board, team_df):
    assert print_board(test_board, team_df) is None

def test_check_winner():    
    assert check_winner(1, 1, team_df) == False
    assert check_winner(9, 1, team_df) == True
    assert check_winner(1, 9, team_df) == False
    assert check_winner(3, 9, team_df) == False
    assert check_winner(9, 9, team_df) == True

def test_switch_turn():
    x_turn = 'X'
    o_turn = 'O'
    assert switch_turn(x_turn) == o_turn
    assert switch_turn(o_turn) == x_turn

# def test_restart_game():
#     yes = 'y'
#     YES = 'Y'
#     assert restart_game(yes) is game()
#     assert restart_game(YES) is game()

def test_check_move():
    assert check_move(1) == True
    assert check_move(9) == True
    assert check_move(0) == False
    assert check_move(10) == False

def test_check_move_exceptions():
    print(check_move('invalid input') )
    with pytest.raises(ValueError) as excinfo:  
        check_move('invalid input')  
    assert excinfo.value.message == 'Please chose an INTEGER value (between 1 and 9)'
    with pytest.raises(ValueError) as excinfo:  
        check_move(100)  
    assert excinfo.value.message == '100 is outside the range 1 to 9. Please chose a new position'

def test_game():
    pass

# Run tests: python -m pytest src/tests/tic_tac_toe_test.py