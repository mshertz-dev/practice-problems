# Problem 4 (Medium)
# Using if statements, find whether or not Rashaad Penny is in the interquartile range for rushing yards (between 25th and 75th percentile), in the bottom 25th percentile, or in the top 75th percentile.

# Rashaad Penny Rushing Yards: 370 yards
# 25th percentile (2019) for all RBs for Rushing Yards: 20 yards
# 75th percentile (2019) for all RBs for Rushing Yards: 465 yards


rashaad_rushing_yds = 370
percentile_25 = 20
percentile_75 = 465

if rashaad_rushing_yds <= percentile_25 :
  print("Rashaad Penny is in the bottom 25th percentile for rushing yards")
elif (rashaad_rushing_yds > percentile_25 and rashaad_rushing_yds <= percentile_75) :
  print("Rashaad Penny is in the interquartile range for rushing yards")
elif (rashaad_rushing_yds > percentile_75) :
  print("Rashaad Penny is in the top 25th percentile for rushing yards")