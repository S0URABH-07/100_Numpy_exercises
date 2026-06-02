# Given two arrays, X and Y, construct the Cauchy matrix C ( Cij = 1 / (xi - yj) )

import numpy as np
X = np.array([1, 2, 3, 4])
Y = np.array([5, 6, 7])

C = 1.0 / (X[:, None] - Y)
print(C)

# X[:, None] --> (:) Take all elements || (None)--> Add a new dimension
# [1,2,3,4] size(4,0) --> to --> [[1] [2] [3] [4]] size(4,1)