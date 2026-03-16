import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Generate High-Dimensional Synthetic Data (10 features)
np.random.seed(42)
# Creating 100 samples with 10 features each
data = np.random.rand(100, 10) 
# Adding some structure so PCA has something to find
data[:, 0] = data[:, 1] * 2 + np.random.normal(0, 0.1, 100)
data[:, 2] = data[:, 0] - data[:, 1]

# 2. Standardize the data (Crucial for PCA)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# 3. Apply PCA to reduce from 10D to 2D
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

# 4. Visualization
plt.figure(figsize=(8, 6))
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c='teal', edgecolor='k', alpha=0.7)
plt.title('PCA: 10D Network Data Compressed to 2D')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)
plt.savefig('pca_plot.png')
plt.show()

print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
print(f"Total variance captured: {sum(pca.explained_variance_ratio_)*100:.2f}%")