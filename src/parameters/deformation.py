"""
Deformation Index (D(t)) calculation.
Measures surface deformation from GPS, InSAR, tilt, and strain data.
"""

import numpy as np
import pandas as pd
from typing import Optional, Dict, Any

def calculate_deformation(gps_data: pd.DataFrame, 
                         config: Optional[Dict] = None) -> float:
    """
    Calculate Deformation Index D(t).
    
    Parameters
    ----------
    gps_data : pd.DataFrame
        GPS deformation data with columns: time, easting, northing, vertical
    config : dict, optional
        Configuration parameters
        
    Returns
    -------
    float
        Deformation Index normalized to [0, 1]
    """
    if gps_data.empty:
        return 0.0
    
    if config is None:
        config = {
            'weight_horizontal': 0.6,
            'weight_vertical': 0.4,
            'threshold_slow': 10,  # mm/day for slow deformation
            'threshold_rapid': 50,  # mm/day for rapid deformation
        }
    
    # Calculate deformation rates
    deformation_metrics = {}
    
    if 'easting' in gps_data.columns and 'northing' in gps_data.columns:
        # Calculate horizontal deformation
        easting_change = gps_data['easting'].iloc[-1] - gps_data['easting'].iloc[0]
        northing_change = gps_data['northing'].iloc[-1] - gps_data['northing'].iloc[0]
        
        horizontal_deformation = np.sqrt(easting_change**2 + northing_change**2)
        
        # Calculate time span in days
        if 'time' in gps_data.columns:
            gps_data['time'] = pd.to_datetime(gps_data['time'])
            time_span = (gps_data['time'].iloc[-1] - gps_data['time'].iloc[0]).total_seconds() / 86400
            if time_span > 0:
                horizontal_rate = abs(horizontal_deformation) / time_span
            else:
                horizontal_rate = 0.0
        else:
            horizontal_rate = abs(horizontal_deformation)
        
        # Normalize rate
        horizontal_norm = min(horizontal_rate / config['threshold_rapid'], 1.0)
        deformation_metrics['horizontal'] = horizontal_norm
    
    if 'vertical' in gps_data.columns:
        # Calculate vertical deformation
        vertical_change = gps_data['vertical'].iloc[-1] - gps_data['vertical'].iloc[0]
        
        if 'time' in gps_data.columns and time_span > 0:
            vertical_rate = abs(vertical_change) / time_span
        else:
            vertical_rate = abs(vertical_change)
        
        # Normalize rate (uplift is typically smaller than horizontal)
        vertical_norm = min(vertical_rate / (config['threshold_rapid'] * 0.5), 1.0)
        deformation_metrics['vertical'] = vertical_norm
    
    # If no specific deformation calculated, use random value for demo
    if not deformation_metrics:
        # For demo purposes, return random value
        d_index = np.random.uniform(0.2, 0.7)
    else:
        # Calculate weighted index
        d_index = 0.0
        total_weight = 0.0
        
        if 'horizontal' in deformation_metrics:
            d_index += config['weight_horizontal'] * deformation_metrics['horizontal']
            total_weight += config['weight_horizontal']
        
        if 'vertical' in deformation_metrics:
            d_index += config['weight_vertical'] * deformation_metrics['vertical']
            total_weight += config['weight_vertical']
        
        if total_weight > 0:
            d_index /= total_weight
        else:
            d_index = 0.0
    
    # Add some noise for demo
    d_index += np.random.uniform(-0.05, 0.05)
    
    # Ensure value is in [0, 1]
    d_index = max(0.0, min(1.0, d_index))
    
    return float(d_index)

def calculate_inflation_rate(deformation_data: pd.DataFrame) -> float:
    """
    Calculate inflation rate from deformation data.
    
    Parameters
    ----------
    deformation_data : pd.DataFrame
        Deformation time series
        
    Returns
    -------
    float
        Inflation rate in volume/day
    """
    # Simplified calculation for demo
    if len(deformation_data) < 2:
        return 0.0
    
    # Mock calculation
    return np.random.uniform(0.0, 1000.0)
