import numpy as np
employees = np.array([
    [85,90,88],
    [70,65,72],
    [95,92,96],
    [60,68,65],
    [80,85,82]
])
average = np.mean(employees, axis=1)

print("Average:", average)

print("Best Employee:", np.argmax(average))

print("Needs Improvement:", np.where(average < 70)[0])

print("Company Average:", np.mean(employees))

ranking = np.argsort(average)[::-1]
print("Ranking:", ranking)

print("Top 3:", ranking[:3])