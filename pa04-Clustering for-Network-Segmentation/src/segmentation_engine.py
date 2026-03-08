import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Generate Synthetic Device Behavior (Throughput vs. Connection Count)
np.random.seed(42)
# Cluster 1: IoT Sensors (Low data, constant connections)
iot_devices = np.random.normal(loc=[10, 50], scale=2, size=(50, 2))
# Cluster 2: Workstations (Medium data, bursty connections)
workstations = np.random.normal(loc=[500, 20], scale=50, size=(50, 2))
# Cluster 3: Servers (High data, high connections)
servers = np.random.normal(loc=[2000, 100], scale=200, size=(50, 2))

X_raw = np.vstack([iot_devices, workstations, servers])

# 2. Scaling is mandatory for distance-based models
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)

# 3. Train K-Means (We look for 3 distinct groups)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# 4. Visualization
plt.figure(figsize=(10, 6))
plt.scatter(X_raw[:, 0], X_raw[:, 1], c=clusters, cmap='viridis', label='Devices')
plt.scatter(scaler.inverse_transform(kmeans.cluster_centers_)[:, 0], 
            scaler.inverse_transform(kmeans.cluster_centers_)[:, 1], 
            s=200, c='red', marker='X', label='Centroids')
plt.title('Unsupervised Network Device Segmentation')
plt.xlabel('Data Throughput (MB/day)')
plt.ylabel('Unique Connection Count')
plt.legend()
plt.grid(True)
plt.savefig('segmentation_plot.png')
plt.show()