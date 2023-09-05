import pandas as pd

from data.data_db_functions import (post_teams_to_db)
from utils.classes import Team
##########################################################################################################
### TEAMS ###
##########################################################################################################


def add_teams_to_db_process():
    '''
    Full process to add a list of players to the database
    Step 1: Get data
    Step 2: Clean data
    Step 3: Create player list
    Step 4: Post list to db
    '''
    #1. Get team data from footbal api
    
    #2. Clean team data
    
    
    #3. Create list of teams to be posted
    teams_to_post: list[Team] = []
    
    #4. Post teams
    teams_posted = post_teams_to_db(teams_to_post)
    return teams_posted

def get_players_from_db_process():
    '''
    Full process to get player data from db
    By either team, league, id, name
    '''
    pass


def main():
    pass

if __name__ == "__main__":
    main()
