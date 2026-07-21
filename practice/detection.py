import numpy as np
transactions = np.array([
    500,
    700,
    450,
    100000,
    650,
    900,
    250000,
    800
])
fraud = transactions > 50000

print(transactions[fraud])

print("Count:", np.sum(fraud))

print("Percentage:",
      np.sum(fraud)/len(transactions)*100)

print(np.max(transactions))
print(np.min(transactions))

clean = transactions[~fraud]
print(clean)