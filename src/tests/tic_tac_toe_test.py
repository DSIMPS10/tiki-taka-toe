import pytest
import pandas as pd

import src.app as app
import src.tic_tac_toe as ttt
from src.utils.app_objects import Grid

# def test_printBoard():
#     ttt.printBoard()

def test_game():
    ttt.game()