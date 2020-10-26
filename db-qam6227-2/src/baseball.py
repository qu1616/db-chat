from src.swen344_db_utils import *


def build_tables():
    exec_sql_file('Baseball-AL-East-2015.sql')


def find_team():
    team_sql = """
        SELECT name, title, team FROM Coach 
            WHERE title= 'Manager'
    """
    team = exec_get_all(team_sql)
    print("Managers")
    print("---------------------------------")
    for row in team:
        print(row[0] + "   " + row[1] + "   " + row[2])


def find_player_name():
    play_name_sql = """
        SELECT Player.name, Coach.name, Coach.team
        FROM Player
        INNER JOIN Coach ON Player.team = Coach.team
        WHERE player.position = 1
        AND Coach.title = 'Pitching Coach'
        AND player.age > 30
    """
    print("\nPitchers over age of 30 and their coach")
    print("---------------------------------")
    player = exec_get_all(play_name_sql)
    for row in player:
        print(row[0], row[1], row[2])


def find_infielders():
    find_sql = """
    SELECT Player.name, Player.number, Player.age, Team.ballpark
        FROM Player
        INNER JOIN Team ON Player.team = Team.name
        WHERE player.position BETWEEN 3 AND 6 
        AND Team.ballpark = 'Camden Yards'
    """
    print("\nInfielders")
    print("---------------------------------")
    infield = exec_get_all(find_sql)
    for row in infield:
        print(row[0], row[1], row[2])


def find_rays():
    rays_sql = """
        SELECT name, number FROM Player
            WHERE team = 'Rays'
            ORDER BY name
    """
    rays = exec_get_all(rays_sql)
    print("\nRays Players")
    print("---------------------------------")
    for row in rays:
        print(row[0], row[1])


def find_num_infielders():
    num_sql = """
        SELECT COUNT(position) FROM Player 
            WHERE position BETWEEN 3 AND 6
    """

    print("\nnum of infielders")
    print("---------------------------------")
    num = exec_get_all(num_sql)
    print(num[0])


def find_avg_pitcher_age():
    find_sql = """
        SELECT ROUND(AVG(age),2) FROM Player      
            WHERE position = 1
            
    """
    print("\nAverage pitcher age")
    print("---------------------------------")
    age = exec_get_all(find_sql)
    print(age[0])


def find_num():
    find_sql = """
        SELECT COUNT(position), team from Player 
            WHERE position BETWEEN 3 AND 6
            GROUP BY team
    """
    print("\ninfielders grouped by team")
    print("---------------------------------")
    infield = exec_get_all(find_sql)
    for row in infield:
        print(row[0])


def main():
    build_tables()
    find_team()
    find_player_name()
    find_infielders()
    find_rays()
    find_num_infielders()
    find_avg_pitcher_age()
    find_num()


main()
