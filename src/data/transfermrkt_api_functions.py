import http.client
import json
import os 
import ssl
from dotenv import load_dotenv
import time
# import sys
# dir = os.getcwd()
# sys.path.append(dir)

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

##########################################################################################################
### FUNCTIONS TO INTERACT WITH 'API-FOOTBALL' API ###
##########################################################################################################

load_dotenv()
api_key = os.getenv("TOM_TRANSFERMRKT_API_KEY")


conn = http.client.HTTPSConnection("transfermarket.p.rapidapi.com")

headers = {
        'X-RapidAPI-Key': api_key,
        'X-RapidAPI-Host': "transfermarket.p.rapidapi.com"}

def get_teams_from_season_year(year: int, league_id)-> dict:

    conn.request("GET", f"/competitions/get-table?id={league_id}&seasonID={year}&domain=com", headers=headers)

    res = conn.getresponse()
    data = res.read()

    decoded = data.decode("utf-8")
    season_json= json.loads(decoded)
    clubs_info = {}
    for club in season_json['table']:
        print(club['clubName'])
        print(club['id'])
        clubs_info[club['clubName']] = club['id']
    return clubs_info

# conn.request("GET", "/players/squads?team=33", headers=headers)

##########################################################################################################
### PLAYER FUNCTIONS ###
##########################################################################################################

def get_squad_from_team_id(team_name:str ,team_id: int,season: int):

    conn.request("GET", f"/clubs/get-squad?id={team_id}&saison_id={season}&domain=com", headers=headers)

    res = conn.getresponse()
    data = res.read()

    decoded = data.decode("utf-8")
    squad_json= json.loads(decoded)
    list_of_players = []
    for player in squad_json['squad']:
        player_dict = {}
        player_dict['full_name'] = player['name']
        player_dict['team_name'] = team_name
        player_dict['season'] = season
        player_dict['nationality'] = player['nationalities'][0]['name']
        list_of_players.append(player_dict)   
    return list_of_players


def main():
    #season_2022 = {"share":{"title":"Premier League - Table","url":"https:\/\/www.transfermarkt.com\/premier-league\/tabelle\/wettbewerb\/GB1","description":"This page shows the detailed table of a competition."},"table":[{"id":"281","group":"N/A","rank":1,"oldRank":1,"clubName":"Man City","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/281.png?lm=1467356331","points":89,"goals":94,"goalsConceded":33,"goalDifference":61,"matches":38,"wins":28,"losses":5,"draw":5,"markID":"31","markClass":"meister","markColor":"#afd179","markDescription":"Champions & UEFA Champions League"},{"id":"11","group":"N/A","rank":2,"oldRank":2,"clubName":"Arsenal","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/11.png?lm=1489787850","points":84,"goals":88,"goalsConceded":43,"goalDifference":45,"matches":38,"wins":26,"losses":6,"draw":6,"markID":"78","markClass":"gruen","markColor":"#c3dc9a","markDescription":""},{"id":"985","group":"N/A","rank":3,"oldRank":3,"clubName":"Man Utd","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/985.png?lm=1457975903","points":75,"goals":58,"goalsConceded":43,"goalDifference":15,"matches":38,"wins":23,"losses":9,"draw":6,"markID":"78","markClass":"gruen","markColor":"#c3dc9a","markDescription":""},{"id":"762","group":"N/A","rank":4,"oldRank":4,"clubName":"Newcastle","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/762.png?lm=1472921161","points":71,"goals":68,"goalsConceded":33,"goalDifference":35,"matches":38,"wins":19,"losses":5,"draw":14,"markID":"78","markClass":"gruen","markColor":"#c3dc9a","markDescription":""},{"id":"31","group":"N/A","rank":5,"oldRank":5,"clubName":"Liverpool","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/31.png?lm=1456567819","points":67,"goals":75,"goalsConceded":47,"goalDifference":28,"matches":38,"wins":19,"losses":9,"draw":10,"markID":"4","markClass":"uefa","markColor":"#bdd9ef","markDescription":"UEFA Europa League"},{"id":"1237","group":"N/A","rank":6,"oldRank":6,"clubName":"Brighton","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/1237.png?lm=1492718902","points":62,"goals":72,"goalsConceded":53,"goalDifference":19,"matches":38,"wins":18,"losses":12,"draw":8,"markID":"4","markClass":"uefa","markColor":"#bdd9ef","markDescription":"UEFA Europa League"},{"id":"405","group":"N/A","rank":7,"oldRank":7,"clubName":"Aston Villa","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/405.png?lm=1469443765","points":61,"goals":51,"goalsConceded":46,"goalDifference":5,"matches":38,"wins":18,"losses":13,"draw":7,"markID":"110","markClass":"UEFA Europa Conference League Qualifikation","markColor":"#a5cce9","markDescription":"UEFA Europa Conference League Qualifikation"},{"id":"148","group":"N/A","rank":8,"oldRank":8,"clubName":"Tottenham","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/148.png?lm=1544345801","points":60,"goals":70,"goalsConceded":63,"goalDifference":7,"matches":38,"wins":18,"losses":14,"draw":6,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"1148","group":"N/A","rank":9,"oldRank":9,"clubName":"Brentford","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/1148.png?lm=1625150543","points":59,"goals":58,"goalsConceded":46,"goalDifference":12,"matches":38,"wins":15,"losses":9,"draw":14,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"931","group":"N/A","rank":10,"oldRank":10,"clubName":"Fulham","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/931.png?lm=1556831687","points":52,"goals":55,"goalsConceded":53,"goalDifference":2,"matches":38,"wins":15,"losses":16,"draw":7,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"873","group":"N/A","rank":11,"oldRank":11,"clubName":"Crystal Palace","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/873.png?lm=1457723287","points":45,"goals":40,"goalsConceded":49,"goalDifference":-9,"matches":38,"wins":11,"losses":15,"draw":12,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"631","group":"N/A","rank":12,"oldRank":12,"clubName":"Chelsea","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/631.png?lm=1682435911","points":44,"goals":38,"goalsConceded":47,"goalDifference":-9,"matches":38,"wins":11,"losses":16,"draw":11,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"543","group":"N/A","rank":13,"oldRank":13,"clubName":"Wolves","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/543.png?lm=1467496784","points":41,"goals":31,"goalsConceded":58,"goalDifference":-27,"matches":38,"wins":11,"losses":19,"draw":8,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"379","group":"N/A","rank":14,"oldRank":14,"clubName":"West Ham","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/379.png?lm=1464675260","points":40,"goals":42,"goalsConceded":55,"goalDifference":-13,"matches":38,"wins":11,"losses":20,"draw":7,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"989","group":"N/A","rank":15,"oldRank":15,"clubName":"Bournemouth","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/989.png?lm=1457991811","points":39,"goals":37,"goalsConceded":71,"goalDifference":-34,"matches":38,"wins":11,"losses":21,"draw":6,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"703","group":"N/A","rank":16,"oldRank":16,"clubName":"Nottm Forest","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/703.png?lm=1598890289","points":38,"goals":38,"goalsConceded":68,"goalDifference":-30,"matches":38,"wins":9,"losses":18,"draw":11,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"29","group":"N/A","rank":17,"oldRank":17,"clubName":"Everton","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/29.png?lm=1445949846","points":36,"goals":34,"goalsConceded":57,"goalDifference":-23,"matches":38,"wins":8,"losses":18,"draw":12,"markID":"0","markClass":"N/A","markColor":"N/A","markDescription":"N/A"},{"id":"1003","group":"N/A","rank":18,"oldRank":18,"clubName":"Leicester","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/1003.png?lm=1472229265","points":34,"goals":51,"goalsConceded":68,"goalDifference":-17,"matches":38,"wins":9,"losses":22,"draw":7,"markID":"6","markClass":"absteiger","markColor":"#f8a7a3","markDescription":"Relegated"},{"id":"399","group":"N/A","rank":19,"oldRank":19,"clubName":"Leeds","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/399.png?lm=1645652224","points":31,"goals":48,"goalsConceded":78,"goalDifference":-30,"matches":38,"wins":7,"losses":21,"draw":10,"markID":"6","markClass":"absteiger","markColor":"#f8a7a3","markDescription":"Relegated"},{"id":"180","group":"N/A","rank":20,"oldRank":20,"clubName":"Southampton","clubImage":"https:\/\/tmssl.akamaized.net\/images\/wappen\/medium\/180.png?lm=1444560086","points":25,"goals":36,"goalsConceded":73,"goalDifference":-37,"matches":38,"wins":6,"losses":25,"draw":7,"markID":"6","markClass":"absteiger","markColor":"#f8a7a3","markDescription":"Relegated"}],"legend":[{"id":"31","description":"Champions & UEFA Champions League","class":"meister","color":"#afd179"},{"id":"78","description":"","class":"gruen","color":"#c3dc9a"},{"id":"4","description":"UEFA Europa League","class":"uefa","color":"#bdd9ef"},{"id":"110","description":"UEFA Europa Conference League Qualifikation","class":"UEFA Europa Conference League Qualifikation","color":"#a5cce9"},{"id":"6","description":"Relegated","class":"absteiger","color":"#f8a7a3"}]}
    chels_2022 = get_squad_from_team_id('Chelsea',631,2022)
    print(chels_2022)
if __name__ == "__main__":
    main()

