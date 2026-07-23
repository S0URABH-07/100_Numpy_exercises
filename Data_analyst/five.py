import pandas as pd
import numpy as np

var = pd.read_csv("HR_Analytics.csv")

data = var.to_numpy()
promotion = data[:,33].astype(int)

print(np.sum(promotion > 5))