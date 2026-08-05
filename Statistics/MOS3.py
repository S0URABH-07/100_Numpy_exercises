# Measure of Spread  (Range, IQR, Outliers, Five Number Summary)
import numpy as np

ages = [18,20,21,22,24,25,27,28,30,31,32,35,38]

q1 = np.percentile(ages,25)
q3 = np.percentile(ages,75)

iqr = q3 - q1

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)