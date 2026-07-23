import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
income = data[:,18].astype(int)

limit = np.mean(income) + 2*np.std(income)

print(income[income > limit])