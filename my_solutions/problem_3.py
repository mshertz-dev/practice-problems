# Problem 3 (Very Hard)
# Using the list above, find the standard deviation of Michael Thomas's receiving yards. This is how you calculate the standard deviation: For each element in the list, subtract away the mean of the list, and square the difference for each of these intermediary calculations. Set these numbers to the side. Once you are finish iterating this operation, sum up all of the results, and divide by the length of the list (the number of observations). Find out more information about standard deviation here.

# Finally, take the square root of that number (that number is actually the variance). This is your standard deviation.


import math

rec_yds = [123, 89, 54, 95, 182, 89, 131, 112, 152, 114, 101, 48, 134, 128, 136, 37]

total_rec_yds = sum(rec_yds)

avg_rec_yds = total_rec_yds / len(rec_yds)

print("Michael Thomas\' average receiving yards in 2019 per game was", avg_rec_yds)

variances = []

for game in rec_yds:
  variances.append((game - avg_rec_yds) ** 2)

print(variances)

standard_deviation = math.sqrt(sum(variances) / len(variances))

print("The standard deviation of receiving yards is",standard_deviation)