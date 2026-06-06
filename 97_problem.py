# Insert a Space Between Characters

import numpy as np
arr = np.array(['hello', 'numpy'])
result = [' '.join(word) for word in arr]
print(result)