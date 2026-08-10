import numpy as np
import seaborn as sns
import pandas as pd
from scipy.stats import chi2_contingency

var = sns.load_dataset("titanic")
contingency_table = pd.crosstab(var["sex"],var["survived"])
print(contingency_table)

chi2 , p_value , dof , expected = chi2_contingency(contingency_table)
print(expected)
print(p_value)
print(chi2)

# alpha = significant value
alpha = 0.05
if p_value<alpha:
    print("I will reject the null hypothesis and there is a signifanct relationship between gender and survival")
else:
    print("there is no connection")