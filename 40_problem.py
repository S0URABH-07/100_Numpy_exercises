# How to sum a small array faster than np.sum?

import numpy as np
arr = np.arange(10)
print("Faster for small array: ",sum(arr))
print("Slower for small array: ",np.sum(arr))