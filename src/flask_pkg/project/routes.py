import requests
from sqlalchemy import desc, func, text
import json

from flask import request, jsonify, render_template, redirect, url_for, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

from .extensions import db
from .models import Football_teams, Players, Guesses, Grids

BASE = "http://127.0.0.1:5000/api/"

main = Blueprint("main", __name__)

#############################################################################################################################################################
### GET / POST ###
#############################################################################################################################################################
   
def get_request(base, endpoint):
    response = requests.get(base + endpoint)
    json_response = response.json()
    return json_response

def post_request(base, endpoint, data):
    response = requests.post(base + endpoint, json=data)
    json_response = response.json()
    return json_response

def put_request(base, endpoint):
    response = requests.put(base + endpoint)
    json_response = response.json()
    return json_response

#############################################################################################################################################################
### ROUTES ###
#############################################################################################################################################################

@main.get("/")
def home():
    return 'Tiki Taka Toe app'

#############################################################################################################################################################
### GET ENDPOINTS ###
#############################################################################################################################################################

@main.get("/api/get_football_teams/<int:limit>")
def get_teams(limit): 
    teams = Football_teams.query.order_by(Football_teams.team_name).limit(limit).all()
    teams_array = [team.as_dict() for team in teams]
    return jsonify(teams_array)

@main.get("/api/get_all_football_teams")
def get_all_teams(): 
    teams = Football_teams.query.order_by(Football_teams.team_name).all()
    teams_array = [team.as_dict() for team in teams]
    return jsonify(teams_array)

@main.get("/api/count_all_football_teams")
def count_all_teams(): 
    teams_count = Football_teams.query.count()
    total_teams_dict = {'team_count': teams_count}
    return jsonify(total_teams_dict)

@main.get("/api/team_from_id/<int:team_id>")
def get_team_from_id(team_id): 
    team_info = Football_teams.query.filter(Football_teams.id == team_id).first()
    # teams_array = [team.as_dict() for team in team_info]
    team_info_dict = team_info.as_dict() 
    return jsonify(team_info_dict)

@main.get("/api/team_from_name/<string:team_name>")
def get_team_from_name(team_name): 
    team_info = Football_teams.query.filter(Football_teams.team_name == team_name).first()
    team_info_dict = team_info.as_dict() 
    return jsonify(team_info_dict)

@main.get("/api/get_players_for_team_id/<string:team_id>")
def get_players_for_team_id(team_id): 
    team_players = Players.query.filter(Players.team_id == team_id).all()
    team_players_dict = team_players.as_dict() 
    return jsonify(team_players_dict)

@main.get("/api/get_all_players")
def get_all_players(): 
    all_players = Players.query.all()
    all_players_array = [player.as_dict() for player in all_players]
    return jsonify(all_players_array)

@main.get("/api/get_player_info_from_name/<string:full_name>")
def get_player_info_from_name(full_name): 
    player_info = Players.query.filter(Players.full_name == full_name).all()
    player_info_array = [player.as_dict() for player in player_info]
    return jsonify(player_info_array)

@main.get("/api/get_all_valid_player_guesses")
def get_all_valid_player_guesses(): 
    sql = text('SELECT COUNT(full_name),full_name FROM Players GROUP BY full_name HAVING COUNT(full_name)>1')
    all_valid_players = db.session.execute(sql)
    all_valid_players_array = [player.full_name for player in all_valid_players]
    return jsonify(all_valid_players_array)

@main.get("/api/check_team_combo_is_valid/<string:team_a>/<string:team_b>")
def check_team_combo_is_valid(team_a, team_b): 
    sql = text(f"SELECT full_name, COUNT(full_name) FROM Players \
                    WHERE team_name = '{team_a}' OR team_name = '{team_b}' \
                    GROUP BY full_name \
                    HAVING COUNT(full_name) >1")
    check_combo_has_matching_player = db.session.execute(sql)
    all_valid_players_array = [player.full_name for player in check_combo_has_matching_player]
    return jsonify(all_valid_players_array)

@main.get("/api/get_players_from_guesses_table")
def get_players_from_guesses_table(): 
    all_guesses = Guesses.query.all()
    all_guesses_array = [player.as_dict() for player in all_guesses]
    return jsonify(all_guesses_array)

#############################################################################################################################################################
### POST ENDPOINTS ###
#############################################################################################################################################################

@main.post("/api/post_teams")
def post_teams():
    team_jsons = request.get_json()
    team_dicts = json.loads(team_jsons)  
    teams_to_add = [Football_teams(**row) for row in team_dicts]
    db.session.add_all(teams_to_add)
    db.session.commit()
    return team_jsons

@main.post("/api/post_players")
def post_players():
    player_jsons = request.get_json()
    player_dicts = json.loads(player_jsons)  
    players_to_add = [Players(**row) for row in player_dicts]
    db.session.add_all(players_to_add)
    db.session.commit()
    return player_jsons

@main.post("/api/post_valid_player_combos")
def post_valid_player_combos():
    valid_player_jsons = request.get_json()
    valid_player_dicts = json.loads(valid_player_jsons)  
    valid_players_to_add = [Guesses(**row) for row in valid_player_dicts]
    db.session.add_all(valid_players_to_add)
    db.session.commit()
    return valid_player_jsons

@main.post("/api/post_grids")
def post_grids():
    grid_jsons = request.get_json()
    grid_dicts = json.loads(grid_jsons)  
    grids_to_add = [Grids(**row) for row in grid_dicts]
    db.session.add_all(grids_to_add)
    db.session.commit()
    return grid_jsons

#############################################################################################################################################################
### UPDATE ENDPOINTS ###
#############################################################################################################################################################

@main.put("/api/update_player_first_season/<string:identifier>/<int:first_season>")
def update_player_season(identifier, first_season): #Identifier e.g. 'Raheem-Shaquille-Sterling~Chelsea'    
    player_name = identifier.split("~")[0].replace('-', ' ') #Raheem-Shaquille-Sterling
    player_team = identifier.split("~")[1].replace('-', ' ') #Manchester-City or Chelsea    
    updated_season_row = Players.query.filter_by(full_name=player_name, team_name=player_team).first()
    updated_season_row.first_season = first_season
    db.session.commit()
    player_info_dict = updated_season_row.as_dict() 
    return jsonify(player_info_dict)
     