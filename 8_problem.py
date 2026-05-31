#Find indices of non-zero elements from [1,2,0,0,4,0]

import numpy as np
arr3 = np.array([1, 2, 0, 0, 4, 0])
indices = np.nonzero(arr3)
print(indices)