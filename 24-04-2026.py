from scipy import stats
import numpy as np

data = [10, 20, 30, 40, 100]

# Mean
print(stats.tmean(data))

# Median
print(np.median(data))

# Skewness (measure of asymmetry)
print(stats.skew(data))