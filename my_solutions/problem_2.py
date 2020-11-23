# Problem 2 (Medium)
# Visit this URL and find Michael Thomas's receiving yards for 2019. Input each weeks receiving yards in to a ordered list, and find the average of the list using Python's built in functions len and sum. Both of these functions can be found in the Python docs.

# Print out MT's average receiving yards for 2019 using the print function.

rec_yds = [123, 89, 54, 95, 182, 89, 131, 112, 152, 114, 101, 48, 134, 128, 136, 37]

total_rec_yds = sum(rec_yds)
avg_rec_yds = total_rec_yds / len(rec_yds)
print("Michael Thomas\' average receiving yards in 2019 per game was", avg_rec_yds)