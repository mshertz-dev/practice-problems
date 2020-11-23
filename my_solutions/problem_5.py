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

for player in players:
  ypc = round(player['rushing_yds'] / player['rushing_att'], 1)
  print(player['name'], "currently has", ypc, "yards per carry")