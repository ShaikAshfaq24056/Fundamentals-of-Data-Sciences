from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

# Load car dataset (using Boston housing dataset as an example)
boston = load_boston()
X = boston.data  # Features
y = boston.target  # Prices

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate a CART model
model = DecisionTreeRegressor(max_depth=5)  # Adjust max_depth for simpler/complexer tree

# Train the model
model.fit(X_train, y_train)

# Function to get user input for car features
def get_car_features():
    mileage = int(input("Enter mileage: "))
    age = int(input("Enter age (years): "))
    brand = input("Enter brand: ")
    engine_type = input("Enter engine type: ")
    return [[mileage, age, brand, engine_type]]  # Prepare input for prediction

# Get user input
new_car_features = get_car_features()

# Predict price and extract decision path
predicted_price = model.predict(new_car_features)[0]

# Create a dictionary to store features and decisions at each node
decision_path = {}
node = model.tree_.apply(new_car_features[0])
path_length = 0

while node != -1:
    feature_index = model.tree_.feature[node]
    feature_name = boston.feature_names[feature_index]
    threshold = model.tree_.threshold[node]
    decision = "<= " + str(threshold) if model.tree_.value[node][0] == 0 else "> " + str(threshold)
    decision_path[path_length] = {feature_name: decision}
    path_length += 1
    node = model.tree_.children_left[node]

# Print prediction and decision path
print("Predicted price:", predicted_price)
print("Decision path:")
for i, step in enumerate(decision_path):
    print(f"Step {i+1}:", decision_path[step])
