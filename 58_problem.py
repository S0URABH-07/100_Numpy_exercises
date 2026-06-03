# How to accumulate elements of a vector (X) to an array (F) based on an index list (I)?

import numpy as np

X = np.array([1, 2, 3, 4])
I = np.array([0, 1, 1, 2])

F = np.zeros(3)

np.add.at(F, I, X)
print(F)
# np.add.at()--> is specifically designed to handle repeated indices safely.