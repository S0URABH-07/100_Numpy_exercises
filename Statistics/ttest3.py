import numpy as np
from scipy import stats
group_A = [85,88,90,92,87,85,89,91,86,88]
group_B = [82,84,80,83,81,79,78,85,84,83]
t_stats , p_value = stats.ttest_ind(group_A,group_B,equal_var=False)
print(t_stats)