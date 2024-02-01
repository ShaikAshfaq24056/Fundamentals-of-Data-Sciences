import pandas as pd
sales_data = pd.DataFrame({
    'ProductID': [1, 2, 1, 3, 2, 3, 4, 5, 4, 5],
    'ProductName': ['ProductA', 'ProductB', 'ProductA', 'ProductC', 'ProductB', 'ProductC', 'ProductD', 'ProductE', 'ProductD', 'ProductE'],
    'QuantitySold': [10, 15, 8, 20, 12, 18, 5, 25, 6, 22]
})
product_Sales=sales_data.groupby('ProductName')['QuantitySold'].sum()
sorted_sales=product_Sales.sort_values(ascending=False)
five=sorted_sales.head(5)
print(five)
