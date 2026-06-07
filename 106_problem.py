# Get Boolean Array When Values End with a Particular Character

import numpy as np
arr = np.array(['apple','orange','banana','grape'])
print(np.char.endswith(arr, 'e'))