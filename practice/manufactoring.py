import numpy as np
weights = np.array([
    98,100,102,105,97,96,104,99,101,95
])
defective = (weights < 97) | (weights > 103)

print(weights[defective])

print(np.sum(defective))

print(np.sum(defective)/len(weights)*100)

print(np.mean(weights))

print(np.std(weights))

print(np.max(np.abs(weights-100)))