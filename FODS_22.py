import numpy as np
daily_temperatures = np.array([25.5, 26.0, 24.8, 25.2, 25.7, 26.5, 27.0, 28.5, 25.0, 25.5, 26.8, 29.5, 24.0, 26.5, 27.8])
variance_temperatures = np.var(daily_temperatures)
print("Variance of Daily Temperatures:", variance_temperatures)
z_scores = (daily_temperatures - np.mean(daily_temperatures)) / np.std(daily_temperatures)
z_score_threshold = 2
potential_outliers = np.abs(z_scores) > z_score_threshold
print("\nPotential Outliers:")
print(daily_temperatures[potential_outliers])
