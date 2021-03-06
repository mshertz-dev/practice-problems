# Problem 5 (Easy)
# Write a program that calculates yards per carry for 3 three top running backs. Store the player data in a list of dictionaries, where each dictionary corresponds to a separate player. Iterate over each dictionary using a for loop.

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