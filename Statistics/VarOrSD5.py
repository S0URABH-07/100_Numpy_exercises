# Variance & Standard Deviation
import numpy as np

salary = [25000,27000,29000,30000,32000,34000,35000,36000,38000,100000]

mean = np.mean(salary)
median = np.median(salary)
variance = np.var(salary)
std = np.std(salary)
range_value = np.max(salary) - np.min(salary)

print("Mean:", round(mean,2))
print("Median:", median)
print("Variance:", round(variance,2))
print("Standard Deviation:", round(std,2))
print("Range:", range_value)

if std > 10000:
    print("High variability in salaries.")
else:
    print("Low variability in salaries.")