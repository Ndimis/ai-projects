import pytest
import numpy as np
from time_engine import TimeSeriesPredictor

@pytest.fixture
def predictor():
    # Initialize with a window size of 3 for simple math verification
    return TimeSeriesPredictor(window_size=3)

def test_sequence_creation(predictor):
    """
    Verify that a flat list is correctly converted into 
    sliding window sequences (X) and targets (y).
    """
    data = [10, 20, 30, 40, 50]
    X, y = predictor.create_sequences(data)
    
    # With window=3 and data=5, we expect 2 sequences:
    # 1: [10, 20, 30] -> target 40
    # 2: [20, 30, 40] -> target 50
    assert X.shape == (2, 3)
    assert y.shape == (2,)
    assert np.array_equal(X[0], [10, 20, 30])
    assert y[0] == 40

def test_forecast_trend(predictor):
    """
    Verify that the forecast reflects an upward trend.
    """
    history = [10, 12, 11, 13, 15, 17, 19]
    predictor.train_lite(history)
    
    last_window = [20, 22, 24] # Clearly increasing
    prediction = predictor.forecast(last_window)
    
    # Because it's a weighted average of an increasing window, 
    # the prediction should be significantly higher than the first element (20).
    assert prediction > 20
    assert prediction <= 24 # Weighted average won't exceed the max unless extrapolated

def test_temporal_weighting(predictor):
    """
    Ensure recent data has more weight than older data.
    """
    predictor.train_lite([1, 2, 3, 4, 5, 6, 7])
    
    # Case A: Spike in the recent past [10, 10, 50]
    # Case B: Spike in the distant past [50, 10, 10]
    # Recent spikes should yield a higher forecast.
    forecast_recent = predictor.forecast([10, 10, 50])
    forecast_distant = predictor.forecast([50, 10, 10])
    
    assert forecast_recent > forecast_distant