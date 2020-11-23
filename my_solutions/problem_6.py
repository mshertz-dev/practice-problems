# Problem 6 (Very Hard)
# For each player in the program you created above, write a program that finds the player with the max rushing yards. You should still store player data in a list of dictionaries.

# You should leverage for and if here. I'll offer an alternative solution in the problem_6.py file as there are multiple ways to go about this problem.

players = [
    {
        'name': 'Derrick Henry',
        'rushing_yds': 1540,
        'rushing_att': 303
    },
    {
        'name': 'Aaron Jones',
        'rushing_yds': 1084,
        'rushing_att': 236,
    },
    {
        'name': 'Christian McCaffrey',
        'rushing_yds': 1387,
        'rushing_att': 287
    }
]

max_rusher = 'Bob'
max_rush_yds = 0

for player in players:
  if player['rushing_yds'] > max_rush_yds:
    max_rush_yds = player['rushing_yds']
    max_rusher = player['name']
  ypc = round(player['rushing_yds'] / player['rushing_att'], 1)
  print(player['name'], "currently has", ypc, "yards per carry")

print(max_rusher, 'has the most rushing yards with', max_rush_yds)