import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
customer_data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'total_spent': [100, 50, 200, 80, 30, 150, 120, 70, 250, 90],
    'num_items': [2, 1, 4, 3, 1, 5, 3, 2, 6, 2]
}

df = pd.DataFrame(customer_data)

# Data preparation (assuming no missing values or outliers)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['total_spent', 'num_items']])

# K-Means clustering (using elbow method for k selection)
k_range = range(2, 8)
sse = []
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(k_range, sse, marker='o', linestyle='-', color='blue')
plt.xlabel('Number of clusters')
plt.ylabel('Sum of squared errors (SSE)')
plt.title('Elbow method for K-Means clustering')
plt.show()

# Based on the elbow plot, choose k=3
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(scaled_data)

# Customer segmentation and visualization
df['cluster'] = kmeans.labels_

plt.figure(figsize=(8, 6))
plt.scatter(df['total_spent'], df['num_items'], c=df['cluster'], cmap='viridis')
plt.xlabel('Total amount spent')
plt.ylabel('Number of items purchased')
plt.title('Customer segmentation using K-Means clustering')
plt.show()

# Analyze cluster characteristics
cluster_centers = kmeans.cluster_centers_
print("Cluster centers:")
for i, center in enumerate(cluster_centers):
    print(f"Cluster {i+1}:", center)

# Assign labels to clusters based on characteristics
df['segment'] = ['High-spending Frequent Buyers' if c == 0 else
                 'Moderate Spenders' if c == 1 else
                 'Budget-conscious Infrequent Buyers' for c in df['cluster']]

print("Customer segments:")
print(df.groupby('segment').describe())

# Further analysis and action based on customer segments
# ... (replace with your specific actions)
