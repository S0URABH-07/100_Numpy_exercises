# Different Ways to Convert a Dictionary to a NumPy Array || Convert Key-Value Pairs
import numpy as np

d = {'a': 10, 'b': 20, 'c': 30}
arr = np.array(list(d.items()))

print(arr)