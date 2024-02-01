import numpy as np
import pandas as pd  
house_data = np.array([
    [4, 2000, 350000],
    [3, 1800, 300000],
    [5, 2200, 400000],
    [4, 2400, 380000],
    [6, 2800, 450000]
])
bedroom_column = 0
sale_price_column = -1
houses_more_than_four_bedrooms = house_data[house_data[:, bedroom_column] > 4, sale_price_column]
average_sale_price = np.mean(houses_more_than_four_bedrooms)
print("Average sale price of houses with more than four bedrooms:", average_sale_price)
