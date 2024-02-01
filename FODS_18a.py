import numpy as np
daily_sales = np.array([100, 120, 90, 110, 130, 95, 105, 115, 125, 100, 110, 120, 130, 95, 105])
mean_sales = np.mean(daily_sales)
variance_sales = np.var(daily_sales)
print("Variance of Daily Sales:", variance_sales)
