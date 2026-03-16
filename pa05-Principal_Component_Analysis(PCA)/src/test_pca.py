import pytest
import numpy as np
from sklearn.decomposition import PCA

def test_dimensionality_reduction():
    """Ensure the output has exactly 2 dimensions."""
    test_data = np.random.rand(10, 5) # 5 features
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(test_data)
    assert reduced.shape == (10, 2)

def test_variance_order():
    """Principal Component 1 must explain more variance than Component 2."""
    test_data = np.random.rand(50, 10)
    pca = PCA(n_components=2)
    pca.fit(test_data)
    assert pca.explained_variance_ratio_[0] >= pca.explained_variance_ratio_[1]

def test_reconstruction_error():
    """PCA should be able to transform back to original shape (with some loss)."""
    test_data = np.random.rand(10, 5)
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(test_data)
    recovered = pca.inverse_transform(reduced)
    assert recovered.shape == (10, 5)