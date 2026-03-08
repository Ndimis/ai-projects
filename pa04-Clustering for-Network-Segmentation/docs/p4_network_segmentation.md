# Concept Explainer: K-Means Clustering for Network Segmentation

### 🧠 The Core Concept

**K-Means Clustering** is an unsupervised learning algorithm that groups data points into $K$ number of clusters. In a network context, we use this to identify different "profiles" of devices (e.g., IoT sensors, workstations, servers) based on their behavior rather than their IP address or MAC vendor.

The algorithm works through an iterative process:
1.  **Initialization:** Placing $K$ "centroids" (center points) randomly in the data space.
2.  **Assignment:** Every data point is assigned to the nearest centroid based on Euclidean distance.
3.  **Update:** Centroids move to the average center of their assigned points.
4.  **Convergence:** Step 2 and 3 repeat until the centroids no longer move significantly.



### 🛠️ Lessons Learned

1.  **The "Elbow" Method:** Choosing $K$ is the hardest part. Since we don't have labels, we use the "Inertia" metric (sum of squared distances to the nearest cluster center) to find the point where adding more clusters provides diminishing returns.
2.  **Feature Scaling:** K-Means relies entirely on distance. If "Bytes Transferred" is in the millions and "Connection Duration" is in seconds, the model will ignore the duration. We must use **Standardization** (scaling data to have a mean of 0 and variance of 1).
3.  **Unsupervised Nature:** Unlike our Linear Regression model, K-Means doesn't know what a "Printer" is; it just knows that 50 devices are behaving identically and differently from the rest of the network.

### 📈 Future Application

This is the mathematical foundation for **Zero Trust Micro-segmentation**. Once we cluster devices by behavior, we can automatically generate firewall rules or dynamic VLAN assignments. For example, if a device moves from the "IoT Cluster" to the "Database Admin Cluster" behaviorally, it can be flagged for a security review immediately.

# Concept Explainer: K-Means Clustering for Network Segmentation

### 🧠 The Core Concept

**K-Means Clustering** is an unsupervised learning algorithm that groups data points into $K$ number of clusters. In a network context, we use this to identify different "profiles" of devices (e.g., IoT sensors, workstations, servers) based on their behavior rather than their IP address or MAC vendor.

The algorithm works through an iterative process:
1.  **Initialization:** Placing $K$ "centroids" (center points) randomly in the data space.
2.  **Assignment:** Every data point is assigned to the nearest centroid based on Euclidean distance.
3.  **Update:** Centroids move to the average center of their assigned points.
4.  **Convergence:** Step 2 and 3 repeat until the centroids no longer move significantly.



### 🛠️ Lessons Learned

1.  **The "Elbow" Method:** Choosing $K$ is the hardest part. Since we don't have labels, we use the "Inertia" metric (sum of squared distances to the nearest cluster center) to find the point where adding more clusters provides diminishing returns.
2.  **Feature Scaling:** K-Means relies entirely on distance. If "Bytes Transferred" is in the millions and "Connection Duration" is in seconds, the model will ignore the duration. We must use **Standardization** (scaling data to have a mean of 0 and variance of 1).
3.  **Unsupervised Nature:** Unlike our Linear Regression model, K-Means doesn't know what a "Printer" is; it just knows that 50 devices are behaving identically and differently from the rest of the network.

### 📝 Key Takeaway
> **Unsupervised learning doesn't predict the future; it reveals the present.** By grouping devices based on raw behavior (traffic volume vs. connection frequency), we can detect "Shadow IT" or misconfigured devices that don't fit into established corporate profiles.

### 🚀 How to Run

1. **Install Dependencies**:
   Ensure you are in the project root and run:
   ```bash
   pip install -r requirements.txt