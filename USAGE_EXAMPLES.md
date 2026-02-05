# 🌋 Usage Examples - Volcanic Monitoring Framework

## Quick Installation
```bash
# Install requirements
pip install -r requirements.txt

# Or use pip if available
# pip install volcano-monitoring
```

Running Examples

1. Quick Report with Demo Data

```bash
# Simple report
python run_volcano.py --volcano "Mount Etna" --demo --report --simple

# Detailed report
python run_volcano.py --volcano "Stromboli" --demo --report --verbose
```

2. Live Monitoring (Demo Data)

```bash
# Monitor every 5 minutes (300 seconds)
python run_volcano.py --volcano "Merapi" --demo --monitor --interval 300

# Monitor every hour with details
python run_volcano.py --volcano "Kilauea" --demo --monitor --interval 3600 --verbose
```

3. Using Real Data (If Available)

```bash
python run_volcano.py --volcano "Etna" \
  --seismic "data/raw/seismic/etna_2026.csv" \
  --gps "data/raw/gps/etna_gps.csv" \
  --report
```

Python API Examples

Example 1: Basic Usage

```python
from src.integration.vuap import VolcanicMonitoringFramework

# Create monitoring framework
volcano = VolcanicMonitoringFramework("Etna")

# Set parameters (demo data)
import numpy as np
volcano.parameters = {
    'S': 0.75,  # Seismic activity
    'P': 0.65,  # Pressure
    'G': 0.45,  # Gas emissions
    'D': 0.70,  # Deformation
    'H': 0.35,  # Heat
    'E': 0.25,  # Electrokinetic
    'W': 0.55,  # Water flow
    'L': 0.15,  # Lyapunov
    'R': 0.60,  # Resistivity
}

# Generate report
report = volcano.generate_vuap_report()
print(f"Eruption probability: {report['eruption_probability']:.1%}")
print(f"Alert level: {report['alert_level']}")
```

Example 2: Parameter Calculation from Data

```python
from src.parameters.seismic_pulse import calculate_seismic_pulse
from src.parameters.deformation import calculate_deformation
import pandas as pd
import numpy as np

# Demo seismic data
seismic_data = pd.DataFrame({
    'time': pd.date_range('2026-01-01', periods=100, freq='h'),
    'magnitude': np.random.uniform(1.0, 3.0, 100),
    'depth': np.random.uniform(1.0, 15.0, 100),
})

# Demo deformation data
gps_data = pd.DataFrame({
    'time': pd.date_range('2026-01-01', periods=50, freq='h'),
    'easting': np.cumsum(np.random.normal(0, 5, 50)),
    'northing': np.cumsum(np.random.normal(0, 5, 50)),
    'vertical': np.cumsum(np.random.normal(0, 2, 50)),
})

# Calculate indices
s_index = calculate_seismic_pulse(seismic_data)
d_index = calculate_deformation(gps_data)

print(f"Seismic Pulse Index: {s_index:.3f}")
print(f"Deformation Index: {d_index:.3f}")
```

Example 3: Mogi Model for Deformation

```python
from src.models.mogi import calculate_displacement
import numpy as np

# Surface coordinates
x = np.linspace(-5000, 5000, 100)
y = np.linspace(-5000, 5000, 100)
X, Y = np.meshgrid(x, y)

# Calculate displacement from Mogi source
ux, uy, uz = calculate_displacement(
    x=X.flatten(), y=Y.flatten(),
    source_depth=3000,      # Depth 3 km
    volume_change=1e6,      # Volume change 1 million m³
    poisson_ratio=0.25
)

print(f"Maximum surface uplift: {uz.max():.3f} m")
```

Configuration Files

Custom Configuration

```yaml
# my_config.yaml
parameter_weights:
  seismic_pulse: 0.20    # Higher weight for seismic activity
  deformation: 0.18      # Deformation weight
  gas_flux: 0.16         # Gas emission weight
  pressure: 0.12
  heat: 0.08
  electrokinetic: 0.07
  water_flow: 0.06
  lyapunov: 0.08
  resistivity: 0.05

thresholds:
  warning: 0.6          # Warning at 60%
  critical: 0.8         # Critical at 80%
  alert: 0.9            # Alert at 90%

monitoring:
  interval: 1800        # Every 30 minutes
```

Using Custom Configuration

```bash
python run_volcano.py --volcano "Etna" --config my_config.yaml --demo --report
```

Alert Levels

Level Symbol Probability Recommended Action
Normal 🟢 < 30% Routine monitoring
Unrest 🟡 30-50% Increased monitoring
Warning 🟠 50-70% Prepare emergency plans
Critical 🔴 70-85% Restrict access
Alert 🚨 85% Immediate evacuation

Saving Results

Reports are automatically saved to:

```
results/reports/
├── Etna_20260205_143022.json
├── Stromboli_20260205_150115.json
└── ...
```

Troubleshooting

Error: "Invalid frequency: H"

```bash
# Fixed! Use the corrected version
python run_volcano.py --volcano "Test" --demo --report
```

Import Error

```bash
# Ensure src/ directory exists
# Install requirements
pip install -r requirements.txt
```

Debug Mode

```bash
python run_volcano.py --volcano "Test" --demo --report --verbose
```

Additional Help

```bash
# Show command-line help
python run_volcano.py --help

# Read documentation
cat README.md
cat QUICKSTART.md
```

Contact

· Email: gitdeeper@gmail.com
· GitLab: https://gitlab.com/gitdeeper3/volcano
· Documentation: docs/ directory

---

Updated: 2026-02-05
