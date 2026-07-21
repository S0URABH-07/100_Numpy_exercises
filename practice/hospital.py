import numpy as np
patients = np.array([
    [120,15],
    [150,20],
    [170,18],
    [130,25],
    [180,12]
])
ratio = patients[:,0] / patients[:,1]

print(ratio)

print(np.argmax(ratio))

print(np.mean(ratio))

print(np.where(ratio > 10)[0])