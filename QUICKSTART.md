# 🌋 Quick Start Guide - Volcano Monitoring Framework

## Installation

### Option 1: Using pip (after publication)
```bash
pip install volcano-monitoring
```

Option 2: From source

```bash
# Clone repository
git clone https://gitlab.com/gitdeeper3/volcano.git
cd volcano

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

Basic Usage

1. Generate a single report with demo data

```bash
python run_volcano.py --volcano "Etna" --demo --report
```

2. Real-time monitoring (demo mode)

```bash
python run_volcano.py --volcano "Stromboli" --demo --monitor --interval 300
```

3. Using custom configuration

```bash
python run_volcano.py --volcano "Merapi" --config config/my_config.yaml --report
```

Python API

Basic framework usage

```python
from src.integration.vuap import VolcanicMonitoringFramework

# Initialize framework
volcano = VolcanicMonitoringFramework("Etna")

# Load data (example with simulated data)
import numpy as np
volcano.parameters = {
    'S': 0.75,  # Seismic pulse
    'P': 0.65,  # Pressure
    'G': 0.70,  # Gas flux
    'D': 0.60,  # Deformation
    'H': 0.45,  # Heat
    'E': 0.35,  # Electrokinetic
    'W': 0.55,  # Water flow
    'L': 0.18,  # Lyapunov
    'R': 0.65,  # Resistivity
}

# Generate VUAP report
report = volcano.generate_vuap_report()
print(f"Eruption probability: {report['eruption_probability']:.2%}")
```

Calculate all parameters

```python
from src.integration.vuap import calculate_all_parameters

# Assuming you have data dictionaries
data = {
    'seismic': seismic_dataframe,
    'gps': gps_dataframe,
    'gas': gas_measurements,
}

parameters = calculate_all_parameters(data)
```

Project Structure

```
volcano/
├── run_volcano.py          # Main CLI interface
├── src/                    # Source code
│   ├── integration/       # Multi-parameter integration
│   ├── parameters/        # Parameter calculations
│   ├── models/           # Physics-based models
│   ├── preprocessing/    # Data processing
│   ├── analysis/         # Statistical analysis
│   ├── visualization/    # Plotting and dashboards
│   └── utils/           # Utility functions
├── config/               # Configuration files
├── notebooks/           # Jupyter notebooks for analysis
├── scripts/            # Automation scripts
├── tests/              # Unit tests
└── data/               # Data directory (structure only)
```

Configuration

Main configuration files:

· config/default_config.yaml - Default settings
· config/volcano_list.yaml - Volcano metadata
· config/parameter_weights.yaml - Weighting coefficients
· config/thresholds.yaml - Alert thresholds

Create custom configuration:

```yaml
# my_volcano_config.yaml
parameter_weights:
  seismic_pulse: 0.20
  deformation: 0.18
  gas_flux: 0.16
  # ... other parameters

thresholds:
  warning: 0.6
  critical: 0.8
```

Data Format

Expected data formats:

· Seismic data: CSV with columns [time, magnitude, depth, latitude, longitude]
· GPS data: CSV with columns [time, easting, northing, vertical]
· Gas data: CSV with columns [time, so2_flux, co2_so2_ratio]

Example data structure:

```bash
data/
├── raw/
│   ├── seismic/
│   ├── gps/
│   ├── gas/
│   ├── insar/
│   └── thermal/
├── processed/
│   ├── parameter_indices/
│   └── time_series/
└── validation/
```

Monitoring Modes

1. Single assessment

Generate one-time VUAP report for current state.

2. Periodic monitoring

Run assessments at regular intervals (e.g., hourly).

3. Real-time monitoring

Continuous monitoring with live alerts.

4. Historical analysis

Process historical data for validation.

Alert System

The framework provides four alert levels:

1. Background (Green): Normal volcanic activity
2. Unrest (Yellow): Elevated activity, increased monitoring
3. Warning (Orange): Significant unrest, prepare response
4. Critical (Red): Eruption likely, take protective actions
5. Imminent (Purple): Eruption expected within hours/days

Output

Report formats:

· JSON: Machine-readable format for integration
· TXT: Human-readable summary report
· YAML: Configuration-friendly format

Report location:

· Default: results/reports/
· Configurable via --output parameter

Examples

Check the examples/ directory for complete usage examples:

```bash
# Run example scripts
python examples/basic_usage.py
python examples/eruption_forecast.py
```

Troubleshooting

Common issues:

1. Import errors: Make sure src/ is in Python path
2. Missing dependencies: Run pip install -r requirements.txt
3. Configuration errors: Check YAML syntax in config files

Enable verbose logging:

```bash
python run_volcano.py --volcano "Etna" --demo --report --verbose
```

Getting Help

· Documentation: docs/ directory
· Issue tracker: GitLab Issues
· Email: gitdeeper@gmail.com

Citation

If you use this framework in research, please cite:

```bibtex
@software{baladi2026volcano,
  title = {Multi-Parameter Volcanic Unrest Monitoring Framework},
  author = {Baladi, Samir},
  year = {2026},
  url = {https://gitlab.com/gitdeeper3/volcano}
}
```

---

Last updated: $(date +%Y-%m-%d)
