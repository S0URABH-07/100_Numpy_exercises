# Measure of Central Tendency (Mean, Median, Mode)
import statistics

sales = [120, 150, 180, 170, 160, 200, 190, 180, 170, 160]

mean = statistics.mean(sales)
median = statistics.median(sales)
mode = statistics.mode(sales)

print("Mean :", mean)
print("Median :", median)
print("Mode :", mode)