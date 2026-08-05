# Measure of Spread  (Range, IQR, Outliers, Five Number Summary)
import numpy as np

salary = [25000,27000,29000,30000,32000,34000,36000,38000,40000,42000]

minimum = np.min(salary)
q1 = np.percentile(salary,25)
median = np.median(salary)
q3 = np.percentile(salary,75)
maximum = np.max(salary)

print("Minimum:", minimum)
print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("Maximum:", maximum)