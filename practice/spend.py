import numpy as np
spending = np.array([1200,2500,900,5000,7000,1500,3500,4500])
print(np.mean(spending))

print(spending[spending > 4000])

print(spending[spending < 1500])

print(np.sum(spending))

print(np.median(spending))

print(np.percentile(spending,25))

print(np.percentile(spending,75))