import http.client
import json
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("FOOTBALL_API_KEY")
conn = http.client.HTTPSConnection("v3.football.api-sports.io")



# conn.request("GET", "/players/squads?team=33", headers=headers)

def player_data(player_id):
   
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': api_key
        }
    
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

def main():
    #harry mag
    # player_id = 2935

    #wan bas
    player_id = 18846
    player_data(player_id)

if __name__ == "__main__":
    main()
