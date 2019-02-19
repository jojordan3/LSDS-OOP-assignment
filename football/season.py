'''Tracks the season perfomance of different teams
'''
from .teams import team_names


class Season:


    def __init__(self, week, year, records):
    # make sure the keys in recors (team names) are in team_names
