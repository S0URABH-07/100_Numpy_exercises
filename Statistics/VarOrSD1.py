# Variance & Standard Deviation
import statistics

sales = [20, 25, 30, 28, 35, 40, 22]

mean = statistics.mean(sales)
variance = statistics.variance(sales)
std = statistics.stdev(sales)

print("Mean:", mean)
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(std, 2))