class Grid():
    def __init__(self):
        self.one = [1,1]
        self.two =[1,2]
        self.three =[1,3]
        self.four =[2,1]
        self.five =[2,2]
        self.six =[2,3]
        self.seven = [3,1]
        self.eight =[3,2]
        self.nine =[3,3]

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
    def __init__(self, first_name, last_name, team_id, start_season, end_season):
        self.first_name = first_name
        self.last_name = last_name
        self.team_id = team_id
        self.start_season = start_season
        self.end_season = end_season
    
    def __repr__(self):
        return f'<Player: {self.first_name} {self.last_name}>'
    
    def __str__(self):
        return f'<Player: {self.first_name} {self.last_name}>'