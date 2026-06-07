# Subtract Row Means from a Matrix

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
row_mean = arr.mean(axis=1, keepdims=True)
result = arr - row_mean
print(result)