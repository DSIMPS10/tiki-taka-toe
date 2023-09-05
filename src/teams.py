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
    Step 3: Create team list
    Step 4: Post list to db
    '''
    #1. Get team data from footbal api
    season = 2019
    prem_league = 39
    team_names_for_season: list[str] = get_all_team_names_for_season(prem_league, season)
    
    #2. Check which teams aren't already in the db
    all_teams_already_in_db: pd.DataFrame = get_all_team_from_db()
    all_teams_dict: dict = all_teams_dict_from_df(all_teams_already_in_db)  # Dict format: {id: Team_name}
    team_names_in_db: list[str] = list(all_teams_dict.values())
    # Get all the team names that aren't in the db
    new_teams_to_post = list(set(team_names_for_season).difference(team_names_in_db))
    
    #3. Create list of teams to be posted
    teams_to_post = [Team(team_name=team_name, 
                          league='Premiership', 
                          country='England') for team_name in new_teams_to_post]
    
    #4. Post teams
    teams_posted = post_teams_to_db(teams_to_post)
    return teams_posted

def get_teams_from_db_process(team_names=None, team_ids=None, league_name=None):
    '''
    Full process to get player data from db
    By either team, league, id
    '''
    all_teams_in_db: pd.DataFrame = get_all_team_from_db()
    if team_names != None:
        pass

def main():
    all_teams_already_in_db: pd.DataFrame = get_all_team_from_db()
    all_teams_dict: dict = all_teams_dict_from_df(all_teams_already_in_db)
    team_names_in_db = list(all_teams_dict.values())
    # print(team_names_in_db)
    team_names_for_season = ['Test 1', 'Test 2', 'Chelsea', 'Test 3', 'Tottenham']
    new_teams = list(set(team_names_for_season).difference(team_names_in_db))
    print(new_teams)



if __name__ == "__main__":
    main()
