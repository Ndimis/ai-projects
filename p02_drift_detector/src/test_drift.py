import pytest
import pandas as pd
import numpy as np
from .drift_engine import detect_drift

@pytest.fixture
def baseline_data():
    np.random.seed(42)
    return pd.DataFrame({
        'network_latency': np.random.normal(20, 2, 500)
    })

def test_no_drift(baseline_data):
    """Verify that similar data does not trigger a drift alert."""
    # Data with almost identical distribution
    healthy_data = pd.DataFrame({
        'network_latency': np.random.normal(20.1, 1.9, 500)
    })
    report = detect_drift(baseline_data, healthy_data)
    assert report['network_latency']['drift'] is False

def test_significant_drift(baseline_data):
    """Verify that significantly different data triggers a drift alert."""
    # Sudden high latency (e.g., during a DDoS or network failure)
    malfunctioning_data = pd.DataFrame({
        'network_latency': np.random.normal(50, 10, 500)
    })
    report = detect_drift(baseline_data, malfunctioning_data)
    assert report['network_latency']['drift'] is True
    assert report['network_latency']['p_value'] < 0.05