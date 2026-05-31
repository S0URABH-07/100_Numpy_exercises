# How to add a border (filled with 0's) around an existing array?

import numpy as np
arr = np.array([[1,3,5,6,8],[9,6,3,4,7],[5,4,1,7,8],[1,2,3,4,5],[9,8,7,6,5]])
arr[0, :] =0
arr[-1, :] =0
arr[: ,0] =0
arr[: ,-1] =0

print(arr)