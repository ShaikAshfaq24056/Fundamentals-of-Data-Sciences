import pandas as pd
sales_data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'Name': ['Customer1', 'Customer2', 'Customer3', 'Customer4', 'Customer5'],
    'Age': [25, 30, 28, 35, 40],
    'PurchaseAmount': [100, 150, 120, 200, 180]
})
age_frequency = sales_data['Age'].value_counts().sort_index()
print("Frequency distribution of customer ages:")
print(age_frequency)
