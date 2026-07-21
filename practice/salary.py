import numpy as np
salary = np.array([
25000,27000,29000,30000,28000,150000])
outliers = salary[salary > 50000]

print(outliers)