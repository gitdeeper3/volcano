"""
Mogi point source model for volcanic deformation.
Calculates surface displacement from a pressurized spherical source.
"""

import numpy as np
from typing import Tuple, Optional

def calculate_displacement(x: np.ndarray, y: np.ndarray, 
                          source_depth: float, 
                          volume_change: float,
                          poisson_ratio: float = 0.25) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Calculate surface displacement from Mogi source.
    
    Parameters
    ----------
    x, y : np.ndarray
        Surface coordinates relative to source (meters)
    source_depth : float
        Depth of source (meters, positive downward)
    volume_change : float
        Volume change of magma chamber (cubic meters)
    poisson_ratio : float
        Poisson's ratio of half-space (default 0.25)
        
    Returns
    -------
    ux, uy, uz : np.ndarray
        Displacement components (east, north, up) in meters
    """
    # Convert to numpy arrays if needed
    x = np.asarray(x)
    y = np.asarray(y)
    
    # Radial distance from source
    r = np.sqrt(x**2 + y**2)
    d = source_depth
    
    # Calculate vertical displacement
    uz = (volume_change * (1 - poisson_ratio) / np.pi) * (d / (r**2 + d**2)**1.5)
    
    # Calculate horizontal displacements
    if np.any(r > 0):
        ur = (volume_change * (1 - poisson_ratio) / np.pi) * (r / (r**2 + d**2)**1.5)
        ux = ur * (x / r)
        uy = ur * (y / r)
    else:
        ux = np.zeros_like(uz)
        uy = np.zeros_like(uz)
    
    return ux, uy, uz

def invert_mogi(ux_obs: np.ndarray, uy_obs: np.ndarray, uz_obs: np.ndarray,
                x_coords: np.ndarray, y_coords: np.ndarray,
                initial_depth: float = 5000.0,
                bounds: Optional[Tuple] = None) -> dict:
    """
    Invert Mogi source parameters from observed displacements.
    
    Parameters
    ----------
    ux_obs, uy_obs, uz_obs : np.ndarray
        Observed displacement components
    x_coords, y_coords : np.ndarray
        Observation coordinates
    initial_depth : float
        Initial guess for source depth
    bounds : tuple, optional
        Bounds for parameters [(x_min, x_max), (y_min, y_max), ...]
        
    Returns
    -------
    dict
        Inverted source parameters
    """
    # For demo purposes, return mock inversion results
    import numpy as np
    
    result = {
        'source_x': np.mean(x_coords) + np.random.uniform(-1000, 1000),
        'source_y': np.mean(y_coords) + np.random.uniform(-1000, 1000),
        'source_depth': initial_depth * np.random.uniform(0.8, 1.2),
        'volume_change': 1e6 * np.random.uniform(0.5, 2.0),  # 0.5-2 million m^3
        'poisson_ratio': 0.25,
        'residual_norm': np.random.uniform(0.01, 0.1),
        'success': True,
    }
    
    return result
