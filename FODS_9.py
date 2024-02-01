import pandas as pd

property_data = pd.DataFrame({
    'property_ID': [1, 2, 3, 4],
    'location': ['A', 'B', 'A', 'B'],
    'noofbedrooms': [5, 4, 6, 4],
    'areasqft': [1200, 1000, 1300, 1400],
    'listingprice': [50000, 35000, 55000, 40000]
})

# 1. Average listing price of properties in each location
avg_listing_price_per_location = property_data.groupby('location')['listingprice'].mean()
print("Average listing price of properties in each location:")
print(avg_listing_price_per_location)

# 2. Number of properties with more than four bedrooms
num_properties_more_than_four_bedrooms = property_data[property_data['noofbedrooms'] > 4].shape[0]
print("\nNumber of properties with more than four bedrooms:", num_properties_more_than_four_bedrooms)

# 3. Property with the largest area
property_with_largest_area = property_data.loc[property_data['areasqft'].idxmax()]
print("\nProperty with the largest area:")
print(property_with_largest_area)
