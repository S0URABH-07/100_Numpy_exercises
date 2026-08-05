# Measure of Spread  (Range, IQR, Outliers, Five Number Summary)
import numpy as np

sales = [100,110,120,115,118,117,119,121,500]

q1 = np.percentile(sales,25)
q3 = np.percentile(sales,75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print("Lower Limit:", lower)
print("Upper Limit:", upper)

outliers = []

for value in sales:
    if value < lower or value > upper:
        outliers.append(value)

print("Outliers:", outliers)