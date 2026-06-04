# How to get the n largest values of an array

import numpy as np
arr = np.array([10, 5, 8, 20, 15])
n = 3
print(arr)
largest = np.sort(arr)[-n:]
print(largest)