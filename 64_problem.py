#  How to swap two rows of an array?

import numpy as np
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Normal arr: \n",arr)
arr[[0, 2]] = arr[[2, 0]]
print("Swaped Arr: \n",arr)