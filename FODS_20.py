import numpy as np
response_times = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
percentiles_25th = np.percentile(response_times, 25)
percentiles_50th = np.percentile(response_times, 50)
percentiles_75th = np.percentile(response_times, 75)
print("25th Percentile:", percentiles_25th)
print("50th Percentile (Median):", percentiles_50th)
print("75th Percentile:", percentiles_75th)
