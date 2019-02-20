'''Tracks the season perfomance of different teams
'''
from teams import team_names
from game import Game
from random import randint, uniform, sample


def generate_rand_games(n=15):
    games = []
    for _ in list(range(n)):
        game = Game(teams=sample(team_names, k=2))

        for i in list(range(randint(0, 4))):
            game.field_goal(game.teams[0])

        for j in list(range(randint(0, 4))):
            game.field_goal(game.teams[1])

        for k in list(range(randint(0, 4))):
            game.touchdown(game.teams[0])

        for l in list(range(randint(0, 4))):
            game.touchdown(game.teams[1])

        games.append(game)
    return games


def season_report(games):
    teams = set()
    winning_teams = []
    losing_teams = []
    winning_team_total_points = 0
    losing_team_total_points = 0
    for game in games:
        teams.add(game.teams[0])
        teams.add(game.teams[1])

        winning_team, losing_team = game.get_winning_team()
        winning_teams.append(winning_team)
        losing_teams.append(losing_team)

        winning_team_total_points += game.score[winning_team]
        losing_team_total_points += game.score[losing_team]

    winning_team_average = (winning_team_total_points /
                            len(winning_team))
    losing_team_average = (losing_team_total_points /
                           len(losing_team))

    team_records = {}

    for team in list(teams):
        team_records[team] = [0, 0]

    for team in winning_teams:
        team_records[team][0] += 1

    for team in losing_teams:
        team_records[team][1] += 1

    print('\n\n--------Football Season Report--------\n')
    print('Team Records')
    print('---------------------------------')
    for team, record in team_records.items():
        print(f'{team}: {record[0]} W, {record[1]} L')
    print('---------------------------------')
    print(f'Average Score of Winning Team: {winning_team_average: .1f}')
    print(f'Average Score of Losing Team: {losing_team_average:.1f}\n')


if __name__ == '__main__':
    season_report(generate_rand_games())
