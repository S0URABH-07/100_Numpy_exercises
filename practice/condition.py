import numpy as np
price = np.array([500,700,1200,3000,1500])
discount = np.where(price > 1000,price * 0.80,price)

print(discount)