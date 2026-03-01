import numpy as np
import pandas as pd
import logging
from sklearn.preprocessing import MinMaxScaler

logging.basicConfig(level=logging.INFO, format='%(message)s')

class TimeSeriesPredictor:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.model_coeff = None

    def create_sequences(self, data):
        """Converts a flat list into a sliding window sequence."""
        X, y = [], []
        for i in range(len(data) - self.window_size):
            X.append(data[i:(i + self.window_size)])
            y.append(data[i + self.window_size])
        return np.array(X), np.array(y)

    def train_lite(self, data):
        """Simulates a lightweight temporal learning model."""
        X, y = self.create_sequences(data)
        # Using a weighted average of the window to simulate temporal importance
        self.model_coeff = np.linspace(0.1, 1.0, self.window_size)
        self.model_coeff /= self.model_coeff.sum()
        logging.info("📈 Temporal model 'trained' on window sequences.")

    def forecast(self, current_window):
        """Predicts the next value based on the previous window."""
        prediction = np.dot(current_window, self.model_coeff)
        return round(prediction, 2)

if __name__ == "__main__":
    # Simulate 24 hours of CPU usage (with a trend)
    cpu_history = [20, 22, 21, 25, 28, 30, 35, 40, 42, 45, 50, 55, 60]
    
    predictor = TimeSeriesPredictor(window_size=5)
    predictor.train_lite(cpu_history)
    
    last_window = cpu_history[-5:]
    next_val = predictor.forecast(last_window)
    
    logging.info(f"Historical Window: {last_window}")
    logging.info(f"🔮 Predicted CPU for next hour: {next_val}%")