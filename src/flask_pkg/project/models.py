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
            'id': self.id,
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
    team_combo = db.Column(ARRAY(db.String))
    correct_guesses = db.Column(db.Integer)
    
    def __init__(self, player, team_combo,correct_guesses):
        self.player = player
        self.team_combo = team_combo
        self.correct_guesses = correct_guesses
        
    def as_dict(self):
        return {
            'id': self.id,
            'player':self.player,
            'teams':self.team_combo,
            'correct_guesses':self.correct_guesses
            }
    
    def __repr__(self):
        return f'<{self.player}: [{self.team_combo}]>'
    
class Grids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pos_a = db.Column(db.String(100))
    pos_b = db.Column(db.String(100))
    pos_c = db.Column(db.String(100))
    pos_x = db.Column(db.String(100))
    pos_y = db.Column(db.String(100))
    pos_z = db.Column(db.String(100))
    total_score = db.Column(db.Integer) #sum off player matches across all 9 combos
    min_matches = db.Column(db.Integer) #the minimum number of player matches out of the 9 combos
    max_matches = db.Column(db.Integer) #the max number of player matches out of the 9 combos
    #av_matches = db.Column(db.Decimal(8,2)) # 
    mode_matches = db.Column(db.Integer)
    median_matches = db.Column(db.Integer)
    percentage_completion = db.Column(db.Numeric(8,2)) #Percentage of completed games, either won or draw (9 combos)

    def __init__(self, pos_a, pos_b, pos_c, pos_x, pos_y, pos_z, total_score, max_matches, min_matches, mode_matches,median_matches, percentage_completion):
        self.pos_a = pos_a,
        self.pos_b = pos_b
        self.pos_c = pos_c
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.total_score = total_score
        self.max_matches = max_matches
        self.min_matches = min_matches
        # self.av_matches = av_matches
        self.mode_matches = mode_matches
        self.median_matches = median_matches
        self.percentage_completion = percentage_completion
    def as_dict(self):
        return {
            'id': self.id,
            'pos_a':self.pos_a,
            'pos_b':self.pos_b,
            'pos_c':self.pos_c,
            'pos_x':self.pos_x,
            'pos_y':self.pos_y,
            'pos_z':self.pos_z,
            'total_score':self.total_score,
            'min_matches':self.min_matches,
            'max_matches':self.max_matches,
            # 'av_matches':self.av_matches,
            'mode_matches':self.mode_matches,
            'meadian_matches':self.median_matches,
            'percentage_completion':self.percentage_completion
            }
    def __repr__(self):
        return f'<Grid {self.id} (score: {self.total_score})>'

if __name__ == "__main__":
    db.create_all()