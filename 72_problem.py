# Convert a vector of ints into a matrix binary representation

import numpy as np
Z = np.array([0, 1, 2, 3, 4])
binary = ((Z[:, None] & (1 << np.arange(3)[::-1])) > 0).astype(int)
print(binary)