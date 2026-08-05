# Measure of Spread  (Range, IQR, Outliers, Five Number Summary)
import numpy as np

delivery = [20,22,25,28,30,31,32,35,38,40,42,45,120]

minimum = np.min(delivery)
maximum = np.max(delivery)

range_value = maximum - minimum

q1 = np.percentile(delivery,25)
median = np.median(delivery)
q3 = np.percentile(delivery,75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = []

for value in delivery:
    if value < lower or value > upper:
        outliers.append(value)

print("Range:", range_value)
print("Minimum:", minimum)
print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("Maximum:", maximum)
print("IQR:", iqr)
print("Outliers:", outliers)