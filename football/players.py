class Player:
    '''Dosctring
    '''
    def __init__(self, name=None, yards=120, touchdowns=5, safety=1,
                 interceptions=0, field_goals=3):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

#    def set_stats(self, yards=120, touchdowns=5, safety=1, interceptions=0):
#        self.stats = {'yards': yards, 'td': touchdowns, 'fg': field_goals,
#        'interceptions':interceptions}
#        return self

    def get_points(self):
        td_points = 6 * self.stats['td']
        safety_points = 2 * self.stats['safety']
        total_points = td_points + safety_points
        return total_points


class Quarterback(Player):
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes

#    def set_stats(self, yards=130, touchdowns=5, completed_passes=20,
#    interceptions=4):
#    self.stats = {'yards': yards, 'td': touchdowns, 'pass_completions':
#    completed_passes, 'interceptions':interceptions}
#    return self

    def passing_score(self):
        score = self.completed_passes - (2 * self.interceptions)
        return score
