import requests
from sqlalchemy import desc
import json

from flask import request, jsonify, render_template, redirect, url_for, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

from .extensions import db
from .models import Football_teams, Players

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

#############################################################################################################################################################
### ROUTES ###
#############################################################################################################################################################


@main.get("/")
def home():
    return 'Tiki Taka Toe app'

@main.get("/api/get_football_teams/<int:limit>")
def get_teams(limit): 
    teams = Football_teams.query.order_by(Football_teams.team_name).limit(limit).all()
    teams_array = [team.as_dict() for team in teams]
    return jsonify(teams_array)

@main.post("/api/post_teams")
def post_teams():
    team_jsons = request.get_json()
    team_dicts = json.loads(team_jsons)  
    teams_to_add = [Football_teams(**row) for row in team_dicts]
    db.session.add_all(teams_to_add)
    db.session.commit()
    return team_jsons