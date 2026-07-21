import numpy as np

sales = np.array([
    [12000,15000,18000,22000],
    [10000,12000,17000,21000],
    [14000,18000,19000,25000],
    [16000,17000,21000,26000],
    [18000,22000,24000,30000]
])

city_total = np.sum(sales, axis=1)
print("City Total:", city_total)

quarter_total = np.sum(sales, axis=0)
print("Quarter Total:", quarter_total)

best_city = np.argmax(city_total)
print("Best City Index:", best_city)

best_quarter = np.argmax(quarter_total)
print("Best Quarter:", best_quarter + 1)

print("Average City Sales:", np.mean(sales, axis=1))

print("Company Revenue:", np.sum(sales))

print("Cities above 80000:", np.where(city_total > 80000)[0])

growth = sales[:,3] - sales[:,0]
print("Growth:", growth)