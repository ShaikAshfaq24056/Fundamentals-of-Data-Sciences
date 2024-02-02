import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the data (replace with your actual data path)
data = pd.read_csv("house_data.csv")

# Select the target variable and feature
target_variable = "price"
feature = "size"  # Replace with your chosen feature

# Perform bivariate analysis (scatter plot)
data.plot.scatter(x=feature, y=target_variable)

# Prepare data for modeling
X = data[[feature]]
y = data[target_variable]

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Evaluate model performance
mse = mean_squared_error(y, predictions)
r2 = r2_score(y, predictions)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Print the model equation
print(f"Model equation: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}")

# Example prediction for a specific house size
house_size = 2000  # Example value
predicted_price = model.predict([[house_size]])[0]
print(f"Predicted price for a house size of {house_size}: ${predicted_price:.2f}")
