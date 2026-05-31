# Create a 10x10 array with random values and find the minimum and maximum values

import numpy as np
#This code print the min or max value between 1 to 100-1 (99)
arr = np.random.randint(1,100,(10,10))
print(arr)
print(np.max(arr))
print(np.min(arr))

# This code print the min or max value between 0 to 1
arr1 = np.random.random((10,10))
print(np.min(arr1))
print(np.max(arr1))