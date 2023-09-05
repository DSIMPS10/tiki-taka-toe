import pandas as pd
from sqlalchemy.dialects.postgresql import ARRAY


# from utils.app_objects import Team, Player
from .extensions import db


### DATABASE MODELS ###
class Football_teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), unique=True)
    league = db.Column(db.String(100))
    country = db.Column(db.String(100))
    
    def __init__(self, id, team_name, league, country):
        self.id = id
        self.team_name = team_name
        self.league = league
        self.country = country
        
    def as_dict(self):
        return {
            'team_id':self.id,
            'team_name':self.team_name,
            'league':self.league,
            'country':self.country,
            }
    
    # def as_obj(self):
    #     team_obj = Team(
    #         team_name=self.team_name,
    #         league=self.league,
    #         country=self.country,
    #     )
    #     return team_obj

    def __repr__(self):
        return f'<Team: {self.team_name} ({self.league})>'
    
class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150))
    team_id = db.Column(db.Integer)
    team_name = db.Column(db.String(100))
    first_season = db.Column(db.Integer)
    last_season = db.Column(db.Integer)

    def __init__(self, full_name, team_id, team_name, first_season, last_season):
        self.full_name = full_name
        self.team_id = team_id
        self.team_name = team_name
        self.first_season = first_season
        self.last_season = last_season
    
        
    def as_dict(self):
        return {
            'full_name':self.full_name,
            'team_id':self.team_id,
            'team_name':self.team_name,
            'first_season':self.first_season,
            'last_season': self.last_season
            }
    
    # def as_obj(self):
    #     player_obj = Player(
    #         first_name=self.first_name,
    #         last_name=self.last_name,
    #         team_id=self.team_id,
    #     )
    #     return player_obj

    def __repr__(self):
        return f'<Players: {self.full_name}>'

if __name__ == "__main__":
    db.create_all()

class Guesses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(100))
    teams = db.Column(ARRAY(db.String))
    
    def __init__(self, player, teams):
        self.player = player
        self.teams = teams
        
    def as_dict(self):
        return {
            'player':self.player,
            'teams':self.teams,
            }
    
    def __repr__(self):
        return f'<{self.player}: [{self.teams}]>'

if __name__ == "__main__":
    db.create_all()