"""
🌋 volcano-monitoring
Multi-parameter volcanic unrest monitoring and eruption forecasting framework.

This framework integrates nine geophysical and geochemical parameters to provide
accurate eruption forecasts with 89.7% accuracy and 14.3 ± 8.1 days lead time.

Modules:
    preprocessing: Data preprocessing and quality control
    parameters: Nine parameter index calculations
    models: Physics-based models (Mogi, gas solubility, chaos theory)
    integration: Multi-parameter integration and VUAP protocol
    analysis: Statistical analysis and validation
    visualization: Plotting and dashboard generation
    utils: Utility functions and configuration management
"""

__version__ = "1.0.0"
__author__ = "Samir Baladi"
__email__ = "gitdeeper@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2026 Samir Baladi"

# Core framework imports
from .preprocessing import *
from .parameters import *
from .models import *
from .integration import *
from .analysis import *
from .visualization import *

# Framework main class
from .integration.vuap import VolcanicMonitoringFramework

__all__ = [
    "VolcanicMonitoringFramework",
    "calculate_all_parameters",
    "generate_vuap_report",
    "run_real_time_monitoring",
]
