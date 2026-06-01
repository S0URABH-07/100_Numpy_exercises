# How to compute ((A+B)*(-A/2)) in place (without copy)?

import numpy as np

A = np.ones(3) * 1
B = np.ones(3) * 2

np.add(A, B, out=B)      # B = A + B
np.divide(A, 2, out=A)   # A = A / 2
np.negative(A, out=A)    # A = -A
np.multiply(B, A, out=A) # A = (A + B) * (-A / 2)

print(A)