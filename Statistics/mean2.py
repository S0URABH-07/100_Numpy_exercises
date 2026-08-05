# Measure of Central Tendency (Mean, Median, Mode)
import statistics

marks = [65,72,80,95,100,88,90,78,85,82,76,95]

mean = statistics.mean(marks)
median = statistics.median(marks)
mode = statistics.mode(marks)

print("Mean:", round(mean, 2))
print("Median:", median)
print("Mode:", mode)
print("Highest:", max(marks))
print("Lowest:", min(marks))