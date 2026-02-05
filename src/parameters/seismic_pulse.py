"""
Seismic Pulse Index (S(t)) calculation.
Measures seismic activity including earthquake rate, tremor, b-value, and depth.
"""

import numpy as np
import pandas as pd
from typing import Optional, Dict, Any

def calculate_seismic_pulse(seismic_data: pd.DataFrame, 
                           config: Optional[Dict] = None) -> float:
    """
    Calculate Seismic Pulse Index S(t).
    
    Parameters
    ----------
    seismic_data : pd.DataFrame
        Seismic data with columns: time, magnitude, depth, latitude, longitude
    config : dict, optional
        Configuration parameters
        
    Returns
    -------
    float
        Seismic Pulse Index normalized to [0, 1]
    """
    if seismic_data.empty:
        return 0.0
    
    if config is None:
        config = {
            'weight_rate': 0.4,
            'weight_magnitude': 0.3,
            'weight_depth': 0.2,
            'weight_tremor': 0.1,
        }
    
    # Calculate earthquake rate (events per day)
    if 'time' in seismic_data.columns:
        seismic_data['time'] = pd.to_datetime(seismic_data['time'])
        time_range = (seismic_data['time'].max() - seismic_data['time'].min()).total_seconds()
        if time_range > 0:
            rate = len(seismic_data) / (time_range / 86400)  # events per day
            rate_norm = min(rate / 100, 1.0)  # Normalize (100 events/day = 1.0)
        else:
            rate_norm = 0.0
    else:
        rate_norm = 0.0
    
    # Calculate magnitude factor
    if 'magnitude' in seismic_data.columns:
        avg_magnitude = seismic_data['magnitude'].mean()
        mag_factor = min(avg_magnitude / 4.0, 1.0)  # M4 = 1.0
    else:
        mag_factor = 0.0
    
    # Calculate depth factor (shallow earthquakes weighted higher)
    if 'depth' in seismic_data.columns:
        avg_depth = seismic_data['depth'].mean()
        depth_factor = max(0, 1.0 - (avg_depth / 20.0))  # 0km = 1.0, 20km = 0.0
    else:
        depth_factor = 0.0
    
    # For demo, add some random tremor simulation
    tremor_factor = np.random.uniform(0.1, 0.5)
    
    # Calculate weighted index
    s_index = (
        config['weight_rate'] * rate_norm +
        config['weight_magnitude'] * mag_factor +
        config['weight_depth'] * depth_factor +
        config['weight_tremor'] * tremor_factor
    )
    
    # Ensure value is in [0, 1]
    s_index = max(0.0, min(1.0, s_index))
    
    return float(s_index)

def calculate_b_value(seismic_data: pd.DataFrame, mc: float = 1.0) -> float:
    """
    Calculate b-value from magnitude-frequency distribution.
    
    Parameters
    ----------
    seismic_data : pd.DataFrame
        Seismic data with magnitude column
    mc : float
        Magnitude of completeness
        
    Returns
    -------
    float
        b-value
    """
    if 'magnitude' not in seismic_data.columns or len(seismic_data) < 10:
        return 1.0  # Default value
    
    mags = seismic_data[seismic_data['magnitude'] >= mc]['magnitude'].values
    
    if len(mags) < 5:
        return 1.0
    
    # Maximum likelihood estimation of b-value
    avg_mag = np.mean(mags)
    b_value = np.log10(np.e) / (avg_mag - mc + 0.05)
    
    return float(b_value)
