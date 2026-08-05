# Measure of Central Tendency (Mean, Median, Mode)
import statistics

ages = [22,25,28,30,35,35,40,45,50,28,30,30]

mean = statistics.mean(ages)
median = statistics.median(ages)
modes = statistics.multimode(ages)

count = sum(age > mean for age in ages)

print("Mean:", mean)
print("Median:", median)
print("Modes:", modes)
print("Older than mean:", count)