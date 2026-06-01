# Given a 1D array, negate all elements which are between 3 and 8, in place.

import numpy as np
arr = np.array([1, 3, 5, 7, 9, 2, 8, 6, 4])

arr[(arr >= 3) & (arr <= 8)] *= (-1)
print(arr)