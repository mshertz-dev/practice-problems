# Problem 1 (Easy)
# Tyler Lockett had the following stat line for 2019.

# 69 receptions, 82 targets, 1057 receiving yards, 8 receiving touchdowns

# Using Python, print Lockett's catch rate and fantasy points scored for 2019.

receptions = 69
targets = 82
rec_yds = 1057
rec_tds = 8

catch_rate = receptions / targets
print('Tyler Lockett\'s catch rate is', catch_rate)

fantasy_pts = receptions + rec_yds * .1 + rec_tds * 6
print('Tyler Lockett\'s overall fantasy points =', fantasy_pts)