# Multiply Each Row by a Different Value

import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
mult = np.array([1,2,3])
result = arr * mult[:, None]
print(result)