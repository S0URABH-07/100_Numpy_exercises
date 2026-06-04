#Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C?

import numpy as np
C = np.array([1, 2, 3, 4])
print("Original arr: ",C)
L = len(C)
print("Length of arr: ",L)
Arrange = np.arange(L)
print("Arrange the length: ",Arrange)
A = np.repeat(Arrange, C)
print("Repeated arr: ",A)