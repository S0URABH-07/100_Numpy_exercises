import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
age = data[:,0].astype(int)
income = data[:,18].astype(int)

condition = (age < 30) & (income > 15000)

print(np.sum(condition))