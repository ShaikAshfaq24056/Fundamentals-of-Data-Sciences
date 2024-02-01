import matplotlib.pyplot as plt
import pandas as pd
sales_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [10000, 12000, 8000, 15000, 13000, 16000]
})
plt.plot(sales_data['Month'], sales_data['Sales'], marker='o', color='b', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
plt.bar(sales_data['Month'], sales_data['Sales'], color='c', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
