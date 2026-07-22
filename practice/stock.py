import numpy as np
prices = np.array([
    120,123,125,122,130,135,132,140
])
change = np.diff(prices)

print(change)

print(np.max(change))

print(np.min(change))

print(np.mean(change))

growth = ((prices[-1]-prices[0])/prices[0])*100

print(growth)