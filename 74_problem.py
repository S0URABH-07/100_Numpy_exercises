# Given a two dimensional array, how to extract unique rows? 

import numpy as np
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],
    [7, 8, 9],
    [4, 5, 6]
])
print("Original arr: \n",arr)
unique_rows = np.unique(arr, axis=0)
print("Unique arr: \n",unique_rows)