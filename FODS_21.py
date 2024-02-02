import numpy as np
recovery_times = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
percentiles_10th = np.percentile(recovery_times, 10)
percentiles_50th = np.percentile(recovery_times, 50)
percentiles_90th = np.percentile(recovery_times, 90)
print("10th Percentile:", percentiles_10th)
print("50th Percentile (Median):", percentiles_50th)
print("90th Percentile:", percentiles_90th)
