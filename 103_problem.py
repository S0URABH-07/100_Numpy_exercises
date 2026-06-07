# Check if Two Same-Shaped String Arrays Match Element-Wise

import numpy as np
a = np.array(['A', 'B', 'C'])
b = np.array(['A', 'X', 'C'])
print(np.char.equal(a, b))