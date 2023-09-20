class Grid:
    def __init__(self):
        self.one = [2,0] # bottom row, left
        self.two =[2,1] # bottom row, middle
        self.three =[2,2] # bottom row, right
        self.four =[1,0] # middle row, left
        self.five =[1,1] # middle row, middle
        self.six =[1,2] # middle row, right
        self.seven = [0,0] # top row, left
        self.eight =[0,1] # top row, middle
        self.nine =[0,2] # top row, right

    def grid_to_list(self):
        grid_list = [self.one ,self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine]
        return grid_list

    def number_to_index(self,number):
        grid_list = self.grid_to_list()
        index = number - 1
        return grid_list[index]

class Team:
    def __init__(self, team_name, league, country):
        self.team_name = team_name
        self.league = league
        self.country = country
    
    def __repr__(self):
        return f'{self.team_name} (League: {self.league}, {self.country})'
    
    def __str__(self):
        return f'{self.team_name} (League: {self.league}, {self.country})'

class Player:
    def __init__(self, full_name, team_id, team_name, first_season, last_season):
        self.full_name = full_name
        self.team_id = team_id
        self.team_name = team_name
        self.first_season = first_season
        self.last_season = last_season
    
    def __repr__(self):
        return f'<Player: {self.full_name}>'
    
    def __str__(self):
        return f'<Player: {self.full_name}>'

class Guesses:
    def __init__(self, player, team_combo,correct_guesses):
        self.player = player
        self.team_combo = team_combo
        self.correct_guesses = correct_guesses
        
    def as_dict(self):
        return {
            'player':self.player,
            'teams':self.team_combo,
            'correct_guesses':self.correct_guesses
            }
    
    def __repr__(self):
        return f'<{self.player}: {self.team_combo}>'
    
    def __str__(self):
        return f'<{self.player}: {self.team_combo}>'
    
class FootyGrid:
    def __init__(self, team_a, team_b, team_c, team_x, team_y, team_z, total_score, max_matches, min_matches, mode_matches,median_matches, percentage_completion):
        self.team_a = team_a,
        self.team_b = team_b
        self.team_c = team_c
        self.team_x = team_x
        self.team_y = team_y
        self.team_z = team_z
        self.total_score = total_score
        self.max_matches = max_matches
        self.min_matches = min_matches
        # self.av_matches = av_matches
        self.mode_matches = mode_matches
        self.median_matches = median_matches
        self.percentage_completion = percentage_completion
        
    def as_dict(self):
        return {
            'team_a':self.team_a,
            'team_b':self.team_b,
            'team_c':self.team_c,
            'team_x':self.team_x,
            'team_y':self.team_y,
            'team_z':self.team_z,
            'total_score':self.total_score,
            'min_matches':self.min_matches,
            'max_matches':self.max_matches,
            # 'av_matches':self.av_matches,
            'mode_matches':self.mode_matches,
            'meadian_matches':self.median_matches,
            'percentage_completion':self.percentage_completion
            }
        
    def calculate_grid_average(self):
        return round(self.total_score/9, 1)
        
    def __repr__(self):
        return f'<Grid score: {self.total_score})>'
    
    def __str__(self):
        return f'<Grid score: {self.total_score})>'