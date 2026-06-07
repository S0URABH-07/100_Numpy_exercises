# Divide Every Row by Its Maximum Value

import numpy as np

arr = np.array([[1,2,3],[4,8,2],[5,10,15]])
row_max = arr.max(axis=1, keepdims=True)
result = arr / row_max
print(result)