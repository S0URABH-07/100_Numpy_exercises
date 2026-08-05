# Variance & Standard Deviation
import numpy as np

temperature = [72, 74, 73, 75, 76, 72, 74, 73]

mean = np.mean(temperature)
variance = np.var(temperature)
std = np.std(temperature)

print("Mean:", mean)
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(std, 2))