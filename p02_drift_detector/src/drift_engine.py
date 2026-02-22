import numpy as np
import pandas as pd
from scipy.stats import ks_2samp
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def detect_drift(baseline_data, current_batch, threshold=0.05):
    """
    Uses the Kolmogorov-Smirnov test to detect distribution drift.
    If p-value < threshold, drift is detected.
    """
    drift_report = {}
    
    for column in baseline_data.columns:
        stat, p_value = ks_2samp(baseline_data[column], current_batch[column])
        is_drifting = p_value < threshold
        drift_report[column] = {"p_value": round(p_value, 4), "drift": is_drifting}
        
        if is_drifting:
            logging.warning(f"⚠️ DRIFT DETECTED in feature: {column} (p={round(p_value, 4)})")
        else:
            logging.info(f"✅ Feature {column} is stable.")
            
    return drift_report

if __name__ == "__main__":
    # Simulate Baseline (Normal CPU/RAM usage)
    baseline = pd.DataFrame({
        'cpu_usage': np.random.normal(40, 5, 1000),
        'ram_usage': np.random.normal(60, 10, 1000)
    })
    
    # Simulate Drifting Data (Sudden spike in resource behavior)
    current = pd.DataFrame({
        'cpu_usage': np.random.normal(85, 2, 1000), # Drifted!
        'ram_usage': np.random.normal(62, 9, 1000)   # Stable
    })
    
    detect_drift(baseline, current)