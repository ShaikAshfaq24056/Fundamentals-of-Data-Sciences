import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample data (replace with your actual data)
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'total_amount': [100, 250, 300, 50, 120, 350, 80, 110, 400, 200],
    'frequency': [2, 3, 1, 1, 4, 5, 2, 1, 3, 2]
}

df = pd.DataFrame(data)

# Feature scaling (optional, but recommended for KMeans)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['total_amount', 'frequency']])

# Define number of clusters (k)
k = 3  # Experiment with different values

# Create KMeans model
kmeans = KMeans(n_clusters=k, random_state=42)

# Fit the model to the data
kmeans.fit(scaled_data)

# Get cluster labels
cluster_labels = kmeans.labels_

# Add cluster labels to the DataFrame
df['cluster'] = cluster_labels

# Print the DataFrame with cluster labels
print(df)
