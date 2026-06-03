# What is the equivalent of enumerate for numpy arrays? 

import numpy as np
arr = np.array([10, 20, 30])

for i, x in np.ndenumerate(arr):
    print(i, x)

# enumerate() --> work well on 1D array
# ndenumerate() --> work on Multi Dimension Array
# (index,) (value) return both the index tuple and the corresponding value.