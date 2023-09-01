import http.client
import json
import os 
from dotenv import load_dotenv

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

def get_all_players_for_season(league_id, season, page):
    # conn.request("GET", f"/players?league={league_id}&season={season}&page={page}", headers=headers)
    conn.request("GET", f"/players?league={league_id}&season={season}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    decoded = data.decode("utf-8")
    season_json = json.loads(decoded)
    print(season_json)
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

def main():
    #harry mag
    # player_id = 2935

    #wan bas
    player_id = 18846
    
    # player_data(player_id)
    # player_for_a_season(player_id, season)
    # print(player_for_a_season)
    # season_list = get_list_of_seasons(2016, 2022)
    # print(season_list)
    # player_teams = get_all_teams_of_player(player_id, season_list)
    # print(player_teams)
    # test = get_all_players_for_season(39, 2021, 1)
    # print(test)
    total_list = []
    season = 2021
    prem_league = 39
    total_pages = get_number_of_pages(39,2021)
    for i in range(total_pages):
        single_list = get_all_players_for_season(prem_league, season, i)
        total_list += single_list
    print(total_list)
    
if __name__ == "__main__":
    main()
