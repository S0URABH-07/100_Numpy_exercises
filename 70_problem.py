# Consider a 16x16 array, how to get the block-sum (block size is 4x4)?

import numpy as np
arr = np.ones((16, 16))
result = arr.reshape(4, 4, 4, 4).sum(axis=(2, 3))
print(result)