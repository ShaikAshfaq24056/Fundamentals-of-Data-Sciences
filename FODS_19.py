import numpy as np
monthly_expenses = np.array([
    [50000, 55000, 60000, 52000, 58000],
    [40000, 42000, 38000, 41000, 45000],
    [30000, 32000, 31000, 30000, 33000]
])
variance_expenses = np.var(monthly_expenses, axis=1)
print("Variance of Monthly Expenses for Each Department:")
print(variance_expenses)
covariance_matrix_expenses = np.cov(monthly_expenses)
print("\nCovariance Matrix of Monthly Expenses:")
print(covariance_matrix_expenses)
