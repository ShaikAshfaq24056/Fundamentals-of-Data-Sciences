import pandas as pd
order_data = pd.DataFrame({
    'CustomerID': [1, 2, 1, 3, 2],
    'OrderDate': ['2022-01-01', '2022-01-02', '2022-01-01', '2022-01-03', '2022-01-02'],
    'ProductName': ['ProductA', 'ProductB', 'ProductA', 'ProductC', 'ProductB'],
    'OrderQuantity': [3, 5, 2, 1, 4]
})
total=order_data.groupby('CustomerID')['OrderDate'].count()
avg=order_data.groupby('ProductName')['OrderQuantity'].mean()
earliest=order_data['OrderDate'].min()
latest=order_data['OrderDate'].max()
print(total)
print(avg)
print(earliest)
print(latest)
