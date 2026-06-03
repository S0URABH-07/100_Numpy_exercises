# Considering a four dimensions array, how to get sum over the last two axis at once?

import numpy as np
arr = np.ones((2, 3, 4, 5))
result = arr.sum(axis=(-2, -1))

print(result)