import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Additional libraries for visualization (optional)
import matplotlib.pyplot as plt
# Replace with your actual data
data = {'customer_id': [1, 2, 3, 4, 5],
        'age': [25, 32, 40, 28, 55],
        'gender': ['M', 'F', 'M', 'F', 'M'],
        'income': [50000, 70000, 80000, 65000, 40000],
        'purchase_frequency': [2, 4, 1, 3, 5],
        'average_order_value': [100, 150, 200, 120, 80],
        'product_categories': ['Electronics', 'Fashion', 'Electronics, Home', 'Fashion, Home', 'Home']}

df = pd.DataFrame(data)
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[['age', 'income', 'purchase_frequency', 'average_order_value']]))
# Elbow method
inertia = []
for k in range(2, 8):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(2, 8), inertia, '-o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# Silhouette score
silhouette_scores = []
for k in range(2, 8):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(df_scaled)
    silhouette_scores.append(silhouette_score(df_scaled, kmeans.labels_))

plt.plot(range(2, 8), silhouette_scores, '-o')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette score')
plt.show()
kmeans = KMeans(n_clusters=3)
kmeans.fit(df_scaled)
df['cluster'] = kmeans.labels_
print(df)
