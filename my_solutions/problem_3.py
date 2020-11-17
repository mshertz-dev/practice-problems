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