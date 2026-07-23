import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
income = data[:,18].astype(int)

index = np.argsort(income)[::-1]

print(data[index[:10]])