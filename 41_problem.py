# Consider two random arrays A and B, check if they are equal
import numpy as np

A = np.random.randint(0, 10, 5)
B = np.random.randint(0, 10, 5)

equal = np.array_equal(A, B)
# array_equal() --> return the value (True and False)

print("A =", A)
print("B =", B)
print("Are they equal?", equal)