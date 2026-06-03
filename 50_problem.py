# How to find the closest max value (to a given scalar) in a vector?

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
value = 33

closest_max = arr[arr >= value].min()
print(closest_max)