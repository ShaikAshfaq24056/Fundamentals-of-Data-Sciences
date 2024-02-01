import matplotlib.pyplot as plt
import pandas as pd
weather_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [10, 12, 15, 18, 22, 25, 27, 26, 23, 20, 15, 12],
    'Rainfall': [50, 40, 30, 20, 10, 5, 8, 12, 15, 25, 35, 45]
})
plt.plot(weather_data['Month'], weather_data['Temperature'], marker='o', color='b', label='Temperature')
plt.title('Monthly Temperature Data - Line Plot')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.show()
plt.scatter(weather_data['Month'], weather_data['Rainfall'], color='r', label='Rainfall')
plt.title('Monthly Rainfall Data - Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.show()
