# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

import numpy as np
A = np.random.randint(1, 10, (5, 3))
B = np.random.randint(1, 10, (3, 2))

C = np.dot(A, B) # This performs matrix multiplication

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Result (A x B):\n", C)