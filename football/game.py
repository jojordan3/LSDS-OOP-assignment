'''Game class to model a football game
'''
from .teams import team_names

class Game:
    '''Models a football game. 

    Parameters
    -----------------------------
    teams : list
        list of length 2, strings of team names
    location : str
        city
    score : dict
        key - team name
        value - score for the team
    week : int
        week number during the season
    
    Attributes
    -----------------------------
    winning_team_ : str
        team name
    '''
    
    
    def __init__(self, teams, location=None, score=None, week=None):
        self.teams = teams # validate to make sure this is a list of 2 strings both in team_names
        self.location = location # validate this is a string or None
        self.score = score # validate this is a dict w/ keys == teams and int values or None
        self.week = week

    def touchdown(self, team, extra_point=1):
        '''record td for a team
        Parameters
        -----------------------------
        team : str
            team that scored
        extra_point : int
            extra points earned in extra point play
        '''
        if team not in self.teams:
            raise ValueError('team parameter must be in self.teams')
        else:
            self.score[team] += (6 + extra_point)

    def field_goal(self, team):
        '''record td for a team
        Parameters
        -----------------------------
        team : str
            team that scored
        '''
        if team not in self.teams:
            raise ValueError('team parameter must be in self.teams')
        else:
            self.score[team] += 3
        
    def safety(self, TODO):
        return TODO

    def get_winning_team(self):
        self.winning_team_ #= TODO
        return self.winning_team_
