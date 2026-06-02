# Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area

import numpy as np
arr = np.zeros((5, 5), dtype=[('x', int), ('y', int)])

arr['x'], arr['y'] = np.meshgrid(np.linspace(0, 100, 5),np.linspace(0, 100, 5))
print(arr)
# meshgrid()--> creates all these possible coordinate points 