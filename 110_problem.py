# Normalize Each Column Separately

import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
col_min = arr.min(axis=0)
col_max = arr.max(axis=0)
normalized = (arr - col_min) / (col_max - col_min)
print(normalized)