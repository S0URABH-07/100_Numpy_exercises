# Create Histogram Using NumPy

import numpy as np
data = np.random.randn(1000)
hist, bins = np.histogram(data, bins=10)
print("Histogram:", hist)
print("Bins:", bins)