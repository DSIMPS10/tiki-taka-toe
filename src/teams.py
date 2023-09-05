import pandas as pd

from data.data_db_functions import (post_teams_to_db,
                                    get_all_team_from_db)
from data.data_helper_functions import (all_teams_dict_from_df)
from data.footy_api_functions import (get_all_team_names_for_season)
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
    season = 2019
    prem_league = 39
    team_names_for_season: list[str] = get_all_team_names_for_season(prem_league, season)
    
    #2. Check if team is already in the db
    all_teams_already_in_db: pd.DataFrame = get_all_team_from_db()
    all_teams_dict: dict = all_teams_dict_from_df(all_teams_already_in_db)
    print(all_teams_dict)
    
    #3. Create list of teams to be posted
    teams_to_post = [Team(team_name=team_name, 
                          league='Premiership', 
                          country='England') for team_name in team_names_for_season]
    
    #4. Post teams
    teams_posted = post_teams_to_db(teams_to_post)
    return teams_posted

def get_teams_from_db_process():
    '''
    Full process to get player data from db
    By either team, league, id, name
    '''
    pass


def main():
    all_teams_already_in_db: pd.DataFrame = get_all_team_from_db()
    all_teams_dict: dict = all_teams_dict_from_df(all_teams_already_in_db)
    print(all_teams_dict)

if __name__ == "__main__":
    main()
