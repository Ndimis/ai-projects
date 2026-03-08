import pytest
import numpy as np
from segmentation_engine import kmeans, scaler

def test_cluster_count():
    """Verify the model identifies exactly 3 clusters as defined."""
    assert len(kmeans.cluster_centers_) == 3, "Model should identify 3 distinct groups"

def test_prediction_consistency():
    """Ensure similar inputs end up in the same cluster."""
    # Two similar 'IoT-like' devices
    dev_a = scaler.transform([[12, 52]])
    dev_b = scaler.transform([[11, 49]])
    
    assert kmeans.predict(dev_a) == kmeans.predict(dev_b), "Similar behaviors should cluster together"

def test_scaling_effect():
    """Ensure the scaler is working to keep data normalized."""
    test_input = np.array([[2000, 100]])
    scaled_val = scaler.transform(test_input)
    # Scaled values should be near 0 (mean) and within 1-3 standard deviations
    assert -5 < scaled_val[0][0] < 5