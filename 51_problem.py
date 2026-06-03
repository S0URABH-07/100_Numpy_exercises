# Create a structured array representing a position (x,y) and a color (r,g,b)

import numpy as np

arr = np.zeros(1, dtype=[('x', int),('y', int),('r', float),('g', float),('b', float)])

print(arr)
print(arr['x'])
arr['x'] = 40
print(arr)