# Create a 3x3x3 array with random values

import numpy as np
# This randint create random value between given series as  integer
arr = np.random.randint(0,10, (3,3,3))
print(arr)

#This random create random value between 0 to 1 as float
arr1 = np.random.random((3,3,3))
print(arr1)