# Filter Out Integers from Float NumPy Array

import numpy as np
arr = np.array([1.0, 1.5, 2.0, 2.7, 3.0])
result = arr[arr == arr.astype(int)]
print(result)