class Grid():
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

class Team():
    def __init__(self, team_name, league, country):
        self.team_name = team_name
        self.league = league
        self.country = country
    
    def __repr__(self):
        return f'{self.team_name} (League: {self.league}, {self.country})'
    
    def __str__(self):
        return f'{self.team_name} (League: {self.league}, {self.country})'

class Player():
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
