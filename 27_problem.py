# How to find common values between two arrays?

import numpy as np
a = np.array([1, 2, 2, 3, 4])
b = np.array([2, 2, 4, 5])

print(np.intersect1d(a, b))

# intersect1d() --> Returns unique and common value