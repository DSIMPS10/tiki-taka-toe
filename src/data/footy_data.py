import http.client
import json
import os 
from dotenv import load_dotenv
import time

from utils.app_objects import Player

load_dotenv()
api_key = os.getenv("FOOTBALL_API_KEY")
conn = http.client.HTTPSConnection("v3.football.api-sports.io")
headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': api_key
    }

# conn.request("GET", "/players/squads?team=33", headers=headers)

def get_list_of_seasons(start_date=1993, end_date=2023):
    season_list = [x for x in range(start_date, end_date+1)]
    return season_list
        

def response_to_json(request):
    res = conn.getresponse()
    data = res.read()
    decoded = data.decode("utf-8")
    data_json = json.loads(decoded)

def player_data(player_id):
   
    conn.request("GET", f"/players/squads?player={player_id}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    decoded = data.decode("utf-8")
    print(type(decoded))
    # test = decoded['response']
    player_json = json.loads(decoded)
    print(player_json)
    player_response = player_json['response']
    print(player_response)
    player_team = player_response[0]['team']
    print(type(player_response))
    print(player_team)
    
    return player_team

def player_for_a_season(player_id, season):
    conn.request("GET", f"/players?id={player_id}&season={season}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    decoded = data.decode("utf-8")
    player_json = json.loads(decoded)
    player_response = player_json['response']
    try: 
        player_info = player_response[0]
        player_stats = player_info['statistics']
        player_team = player_stats[0]['team']['name']
    except IndexError as e:
        player_team = "No value"
    print(player_team)
    
def get_all_teams_of_player(player_id: int, seasons:list) -> dict:
    player_teams: dict = {}
    for season in seasons:
        conn.request("GET", f"/players?id={player_id}&season={season}", headers=headers)
        res = conn.getresponse()
        data = res.read()
        decoded = data.decode("utf-8")
        player_json = json.loads(decoded)
        player_response = player_json['response']
        try: 
            player_info = player_response[0]
            player_stats = player_info['statistics']
            player_team = player_stats[0]['team']['name']
            player_teams[season] = player_team
        except IndexError as e:
            continue
        
    return player_teams

def get_number_of_pages(league_id,season):
    '''
    Get number of pages for players
    '''
    conn.request("GET", f"/players?league={league_id}&season={season}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    decoded = data.decode("utf-8")
    season_json = json.loads(decoded)
    paging = season_json['paging']
    total_pages = paging['total']
    return total_pages

def get_all_players_for_season_per_page(league_id, season, page):
    conn.request("GET", f"/players?league={league_id}&season={season}&page={page}", headers=headers)
    # conn.request("GET", f"/players?league={league_id}&season={season}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    decoded = data.decode("utf-8")
    season_json = json.loads(decoded)
    season_response = season_json['response']
    list_of_players = []
    for player in season_response:
        player_dict = {}
        player_info = player['player']
        team_info = player['statistics'][0]
        player_dict['first_name'] = player_info['firstname']
        player_dict['last_name'] = player_info['lastname']
        player_dict['team'] = team_info['team']['name']
        player_dict['season'] = season
        list_of_players.append(player_dict)   
    return list_of_players

def get_all_players_for_a_season(season, league):
    total_list = []
    total_pages = get_number_of_pages(league,season)
    for i in range(total_pages):
        single_list = get_all_players_for_season_per_page(league, season, i+1)
        time.sleep(10)
        total_list += single_list
    return total_list

def get_all_players_for_seasons(list_of_seasons, league):
    all_players = []
    for season in list_of_seasons:
        season__players = get_all_players_for_a_season(season,league)
        all_players += season__players
    return all_players

def convert_player_list_to_obj(player_list):
    players = []
    for player in player_list:
        #TODO - get team Id and add in season column
        team_id = 1
        start_season = 2020
        end_season = 2022
        players.append(Player(first_name=player['first_name'], 
                              last_name=player['last_name'], 
                              team_id=team_id,
                              start_season=start_season,
                              end_season=end_season))
    return players

#TODO: only have start and end seasons for each player and club
def season_for_player():
    pass
        
    
def main():
    season_list = get_list_of_seasons(2016, 2022)
    print(season_list)
    prem_league = 39
    all_players = get_all_players_for_seasons(season_list, league=prem_league)
    return all_players
    
if __name__ == "__main__":
    main()

