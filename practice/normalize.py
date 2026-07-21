import numpy as np
data = np.array([100,120,150,200,300])
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

print(normalized)