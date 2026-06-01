# How to ignore all numpy warnings (not recommended)?
import numpy as np
np.seterr(all='ignore') 

a = np.array([1, 0])

print(1 / a)

# np.seterr()--> controls how NumPy handles floating-point errors.
# all = 'ignore' -->tells NumPy to ignore all floating-point warnings, including:  Division by zero, Overflow, Underflow, Invalid operations