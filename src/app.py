import pandas as pd
import json

# import tic_tac_toe as ttt
from utils.app_objects import Team
from flask_pkg.project.routes import BASE, get_request, post_request

def post_teams_to_db(teams: list[Team]):
    # Convert activities to json
    teams_array = [vars(team) for team in teams]
    # for team in teams:
    #     teams_array.append(vars(team))
        
    activitity_json_str = json.dumps(teams_array)
        
    # Post request
    teams_posted = post_request(BASE, 'post_teams', activitity_json_str)
    print(f"New teams posted: {teams_posted}")
    return teams_posted


def get_teams_from_db(limit):
    teams = get_request(BASE, f'get_football_teams/{limit}')
    df = pd.DataFrame.from_dict(teams)
    return df

def post_some_demo_teams():
    chelsea = Team(team_name='Chelsea', league='Premiership', country='England')
    tottenham = Team(team_name='Tottenham', league='Premiership', country='England')
    arsenal = Team(team_name='Arsenal', league='Premiership', country='England')
    teams_to_be_posted: Team = [chelsea, tottenham, arsenal]
    teams_posted = post_teams_to_db(teams_to_be_posted)

# TODO: get 6 random indexes to select teams by (will need to get max index of DB and use the random lib)
# Output: list[] of 6 integers
def get_six_random_indexes():
    pass

# TODO: use the list of 6 indexes to get the teams from the db
# Output: list[] of 6 team objects
# Later on will be able to add filter by country or league
def get_teams_from_indexes():
    pass

def main():
    teams = get_teams_from_db(3)
    print(teams)


if __name__ == "__main__":
    main()
