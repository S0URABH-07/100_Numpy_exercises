import numpy as np
sales = np.array([
    [120,140,160],
    [200,180,170],
    [300,250,280]
])
print(np.sum(sales ,axis=0))
print(np.sum(sales , axis=1))