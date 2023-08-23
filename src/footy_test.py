import pytest
import footy as footy

def test_check_grid_works():

    answer = footy.main(3)
    assert answer == True

def test_check_grid_works_two():

    answer = footy.main(2)
    assert answer == False

def test_check_grid_works_three():

    answer = footy.main(2)
    assert answer == True