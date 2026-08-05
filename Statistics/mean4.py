# Measure of Central Tendency (Mean, Median, Mode)
import statistics

visitors = [1200,1500,1600,1700,1800,2000,2200,2100,1900,1800,1750,1650]

mean = statistics.mean(visitors)
median = statistics.median(visitors)

difference = abs(mean - median)

print("Mean:", mean)
print("Median:", median)
print("Difference:", difference)

if difference < 100:
    print("Data is approximately symmetric.")
else:
    print("Data may be skewed.")