# Create a 5×5 matrix with the values 1, 2, 3, and 4 on the first diagonal above the main
# diagonal (superdiagonal) using NumPy.

import numpy as np
arr = np.diag([1,2,3,4] , k=1)
print(arr)

# O/P

# [[0 1 0 0 0]
#  [0 0 2 0 0]
#  [0 0 0 3 0]
#  [0 0 0 0 4]
#  [0 0 0 0 0]]

# k=0	Main diagonal
# k=1	First diagonal above the main diagonal
# k=2	Second diagonal above the main diagonal
# k=-1	First diagonal below the main diagonal
# k=-2	Second diagonal below the main diagonal