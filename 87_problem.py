# Different Ways to Convert a Dictionary to a NumPy Array

import numpy as np
d = {'a': 10, 'b': 20, 'c': 30}
arr = np.array(list(d.values()))
print(arr)