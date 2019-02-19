class Player:
    def __init__(self, name, stats=None):
        self.name = name
        self.stats = stats

    def set_stats(self, yards=120, touchdowns=5, safety=1, interceptions=0):
        self.stats = {'yards': yards, 'td': touchdowns, 'fg': field_goals, 'interceptions':interceptions}
        return self

    def get_points(self):
        td_points = 6 * self.stats['td']
        safety_points = 2 * self.stats['safety']
        total_points = td_points + safety_points
        return total_points


class Quarterback(Player):
    def __init__(self, name, stats=None):
        super().init(name, stats)

    def set_stats(self, yards=130, touchdowns=5, completed_passes=20, interceptions=4):
        self.stats = {'yards': yards, 'td': touchdowns, 'pass_completions': completed_passes, 'interceptions':interceptions}
        return self

    def passing_score(self):
        self.stats['pass_completions'] - (2 * self.stats['interceptions'])
