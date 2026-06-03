# Create a structured array representing a position (x,y) and a color (r,g,b)
# Nested Structure

import numpy as np
arr = np.zeros(1, dtype=[
    ('position', [('x', int), ('y', int)]),
    ('color', [('r', float), ('g', float), ('b', float)])
])

print("Original: ",arr)
arr['position']['x'] = 10
arr['position']['y'] = 20
arr['color']['r'] = 100
arr['color']['g'] = 200
arr['color']['b'] = 300
print("With Data: ",arr)