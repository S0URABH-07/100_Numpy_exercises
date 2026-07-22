import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
income = data[:,18].astype(int)

high_salary = income > 10000

print(income[high_salary])

print(np.sum(high_salary))