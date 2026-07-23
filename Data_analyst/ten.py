import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
income = data[:,18].astype(float)

normalized = (income-np.min(income))/(np.max(income)-np.min(income))

print(normalized)