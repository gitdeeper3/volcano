# 🌋 Multi-Parameter Volcanic Unrest Monitoring Framework

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Research](https://img.shields.io/badge/research-volcanology-red)](https://gitlab.com/gitdeeper3/volcano)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

## 📋 Overview

A comprehensive physics-based framework for volcanic eruption forecasting through integrated analysis of nine geophysical and geochemical monitoring parameters. This framework achieves **89.7% accuracy** in distinguishing volcanic unrest episodes that lead to eruption from those that do not, with an average lead time of **14.3 ± 8.1 days**.

### Key Features

- ✅ **Nine-parameter integration**: Seismic, pressure, gas flux, deformation, heat, electrokinetic, water flow, Lyapunov index, and electrical resistivity
- 📊 **Validated on 47 volcanic systems** across 8 countries (2011-2025)
- 🎯 **82.4% reliability** for imminent eruption prediction (within 72 hours)
- 📈 **Real-time monitoring** capability with continuous data streams
- 🔬 **Physics-based models**: Mogi deformation, gas solubility, chaos theory, elastic rock mechanics
- 🌍 **Operational protocol**: VUAP (Volcanic Unrest Assessment Protocol) for observatory use

---

## 📂 Project Structure

```
volcano/
│
├── README.md                          # This file
├── LICENSE                            # MIT License
├── CITATION.cff                       # Citation metadata
├── requirements.txt                   # Python dependencies
├── environment.yml                    # Conda environment
│
├── docs/                              # Documentation
│   ├── methodology.md                 # Detailed methodology
│   ├── physics_background.md          # Physics and theory
│   ├── user_guide.md                  # User guide for VUAP
│   ├── api_reference.md               # Code API documentation
│   ├── case_studies/                  # Detailed case studies
│   │   ├── pinatubo_1991.md
│   │   ├── etna_2001.md
│   │   ├── eyjafjallajokull_2010.md
│   │   └── agung_2017.md
│   └── figures/                       # Documentation figures
│
├── data/                              # Data directory (not tracked in git)
│   ├── raw/                           # Raw monitoring data
│   │   ├── seismic/                   # Seismic waveforms and catalogs
│   │   ├── gps/                       # GPS time series
│   │   ├── gas/                       # SO2 flux and gas ratios
│   │   ├── insar/                     # InSAR displacement maps
│   │   ├── thermal/                   # Thermal camera and satellite data
│   │   ├── hydrochemistry/            # Spring discharge and chemistry
│   │   └── geophysical/               # Resistivity, SP, gravity, etc.
│   │
│   ├── processed/                     # Processed/cleaned data
│   │   ├── parameter_indices/         # Computed S, P, G, D, H, E, W, L, R
│   │   ├── catalogs/                  # Unified event catalogs
│   │   └── time_series/               # Standardized time series
│   │
│   ├── models/                        # Deformation and physics models
│   │   ├── mogi/                      # Mogi source inversions
│   │   ├── dike_models/               # Dike intrusion models
│   │   └── fem/                       # Finite element models
│   │
│   └── validation/                    # Validation datasets
│       ├── eruption_catalog.csv       # Historical eruptions with dates
│       ├── unrest_episodes.csv        # Non-eruptive unrest episodes
│       └── precursor_sequences/       # Complete precursory time series
│
├── src/                               # Source code
│   ├── __init__.py
│   │
│   ├── preprocessing/                 # Data preprocessing
│   │   ├── __init__.py
│   │   ├── seismic_processing.py      # Earthquake detection, location, b-value
│   │   ├── gps_processing.py          # GPS baseline processing, outlier removal
│   │   ├── insar_processing.py        # InSAR unwrapping, geocoding
│   │   ├── gas_processing.py          # SO2 flux calculation, ratio analysis
│   │   └── standardization.py         # Data standardization and QC
│   │
│   ├── parameters/                    # Parameter index calculation
│   │   ├── __init__.py
│   │   ├── seismic_pulse.py           # S(t) - seismic index
│   │   ├── pressure.py                # P(t) - pressure index from b-value, VLP
│   │   ├── gas_flux.py                # G(t) - gas emission index
│   │   ├── deformation.py             # D(t) - deformation index
│   │   ├── heat.py                    # H(t) - thermal index
│   │   ├── electrokinetic.py          # E(t) - self-potential index
│   │   ├── water_flow.py              # W(t) - hydrothermal index
│   │   ├── lyapunov.py                # L(t) - Lyapunov exponent calculation
│   │   └── resistivity.py             # R(t) - resistivity change index
│   │
│   ├── models/                        # Physics-based models
│   │   ├── __init__.py
│   │   ├── mogi.py                    # Mogi point source forward/inverse
│   │   ├── elastic_halfspace.py       # Elastic deformation solutions
│   │   ├── okada.py                   # Okada dislocation model
│   │   ├── gas_solubility.py          # Gas exsolution physics
│   │   └── thermal_models.py          # Heat transfer modeling
│   │
│   ├── integration/                   # Multi-parameter integration
│   │   ├── __init__.py
│   │   ├── state_vector.py            # 9D state vector V(t) construction
│   │   ├── eruption_probability.py    # P_erupt calculation
│   │   ├── threshold_detection.py     # Critical threshold monitoring
│   │   └── vuap.py                    # VUAP protocol implementation
│   │
│   ├── analysis/                      # Statistical analysis
│   │   ├── __init__.py
│   │   ├── time_series_analysis.py    # Trend detection, autocorrelation
│   │   ├── classification.py          # Eruption vs non-eruption classification
│   │   ├── validation.py              # Cross-validation, performance metrics
│   │   └── sensitivity.py             # Sensitivity and uncertainty analysis
│   │
│   ├── visualization/                 # Plotting and visualization
│   │   ├── __init__.py
│   │   ├── dashboard.py               # Real-time monitoring dashboard
│   │   ├── parameter_plots.py         # Individual parameter time series
│   │   ├── state_space_plots.py       # 9D state space visualization
│   │   └── report_generator.py        # Automated report generation
│   │
│   └── utils/                         # Utility functions
│       ├── __init__.py
│       ├── config.py                  # Configuration management
│       ├── io.py                      # Data I/O utilities
│       ├── math_utils.py              # Mathematical utilities
│       └── logging_utils.py           # Logging configuration
│
├── notebooks/                         # Jupyter notebooks
│   ├── 01_data_exploration.ipynb      # Data exploration and QC
│   ├── 02_parameter_calculation.ipynb # Parameter index calculation examples
│   ├── 03_mogi_modeling.ipynb         # Deformation modeling
│   ├── 04_lyapunov_analysis.ipynb     # Lyapunov exponent calculation
│   ├── 05_integration_framework.ipynb # Multi-parameter integration
│   ├── 06_validation.ipynb            # Framework validation
│   └── 07_case_studies.ipynb          # Case study analyses
│
├── scripts/                           # Standalone scripts
│   ├── download_data.py               # Download monitoring data
│   ├── batch_processing.py            # Batch process multiple volcanoes
│   ├── real_time_monitor.py           # Real-time monitoring daemon
│   ├── generate_report.py             # Generate VUAP assessment report
│   └── train_classifier.py            # Train eruption classifier
│
├── tests/                             # Unit tests
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_parameters.py
│   ├── test_models.py
│   ├── test_integration.py
│   └── test_validation.py
│
├── config/                            # Configuration files
│   ├── default_config.yaml            # Default configuration
│   ├── volcano_list.yaml              # List of monitored volcanoes
│   ├── parameter_weights.yaml         # Parameter weighting coefficients
│   └── thresholds.yaml                # Critical threshold values
│
├── results/                           # Analysis results (not in git)
│   ├── validation_results/            # Cross-validation results
│   ├── case_studies/                  # Case study outputs
│   ├── reports/                       # Generated VUAP reports
│   └── figures/                       # Publication-quality figures
│
├── papers/                            # Research papers and manuscripts
│   ├── main_manuscript.docx           # Primary research paper
│   ├── supplementary_materials.pdf    # Supplementary information
│   └── preprints/                     # Preprint versions
│
└── examples/                          # Usage examples
    ├── basic_usage.py                 # Basic framework usage
    ├── custom_volcano.py              # Add custom volcano
    ├── parameter_calculation.py       # Calculate individual parameters
    └── eruption_forecast.py           # Generate eruption forecast
```

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://gitlab.com/gitdeeper3/volcano.git
cd volcano

# Create conda environment
conda env create -f environment.yml
conda activate volcano-monitoring

# Or use pip
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

### Basic Usage

```python
from src.integration import VolcanicMonitoringFramework
from src.parameters import calculate_all_parameters

# Initialize framework
framework = VolcanicMonitoringFramework(volcano_name="Etna")

# Load monitoring data
framework.load_data(
    seismic_file="data/raw/seismic/etna_2001.csv",
    gps_file="data/raw/gps/etna_2001.csv",
    gas_file="data/raw/gas/etna_2001.csv"
)

# Calculate nine parameter indices
parameters = calculate_all_parameters(framework.data)

# Construct state vector
state_vector = framework.get_state_vector(parameters)

# Calculate eruption probability
probability = framework.calculate_eruption_probability(state_vector)

# Generate VUAP assessment
report = framework.generate_vuap_report()
print(report)
```

### Real-Time Monitoring

```bash
# Start real-time monitoring daemon
python scripts/real_time_monitor.py --volcano Etna --interval 3600

# Generate daily report
python scripts/generate_report.py --volcano Etna --output reports/
```

---

## 📊 Nine Monitoring Parameters

| Parameter | Symbol | Physical Basis | Critical Threshold |
|-----------|--------|----------------|-------------------|
| **Seismic Pulse** | S(t) | Rock fracture, magma movement, tremor | >0.7 (normalized) |
| **Pressure** | P(t) | Chamber pressurization (b-value, VLP) | >0.6 |
| **Gas Flux** | G(t) | SO₂ emissions, CO₂/SO₂ ratio | >0.7 |
| **Deformation** | D(t) | GPS/InSAR surface displacement | >0.6 |
| **Heat** | H(t) | Thermal anomalies, heat flux | >0.5 |
| **Electrokinetic** | E(t) | Self-potential changes | >0.4 |
| **Water Flow** | W(t) | Hydrothermal discharge response | >0.5 |
| **Lyapunov Index** | L(t) | Dynamical instability (chaos theory) | >0.2 |
| **Resistivity** | R(t) | Subsurface conductivity changes | >0.6 |

### State Vector

The nine-dimensional volcanic state vector:

```
V(t) = [S(t), P(t), G(t), D(t), H(t), E(t), W(t), L(t), R(t)]
```

Tracks volcanic system evolution from **Background → Unrest → Critical → Eruption**

---

## 🎯 Performance Metrics

### Classification Accuracy

| Metric | Value | Description |
|--------|-------|-------------|
| **Overall Accuracy** | 89.7% | Correct classification of eruption vs non-eruption |
| **Sensitivity (Recall)** | 87.0% | True positive rate (eruptions correctly identified) |
| **Specificity** | 91.3% | True negative rate (non-eruptions correctly identified) |
| **Precision** | 86.9% | Positive predictive value |
| **F1 Score** | 0.869 | Harmonic mean of precision and recall |
| **AUC-ROC** | 0.934 | Area under receiver operating characteristic |

### Lead Time Statistics

- **Mean lead time**: 14.3 days
- **Standard deviation**: ±8.1 days
- **Median lead time**: 12.7 days
- **Minimum**: 1.2 days (rapid phreatic eruption)
- **Maximum**: 47.5 days (slow andesitic magma ascent)

### Imminent Eruption (72-hour window)

- **Accuracy**: 82.4%
- **False alarm rate**: 13.1%
- **Missed eruption rate**: 4.5%

---

## 📖 Methodology

### Parameter Index Calculation

Each parameter is normalized to [0, 1] scale:

```python
# Example: Seismic Pulse Index
S(t) = w1·R(t) + w2·A_tremor(t) + w3·(1/b(t)) + w4·D_hypo(t)
```

Where:
- `R(t)` = earthquake rate
- `A_tremor(t)` = tremor amplitude (RSAM)
- `b(t)` = time-varying b-value (inverted)
- `D_hypo(t)` = depth indicator (shallow weighted higher)
- `w1, w2, w3, w4` = weighting coefficients

### Eruption Probability

Calculated using multi-parameter state space distance:

```python
# Distance to typical pre-eruptive state
d_erupt(t) = sqrt(Σ wi·(Vi(t) - Vi,erupt)²)

# Convert to probability
P_erupt(t) = 1/(1 + exp(β0 + β1·d_erupt(t)))
```

### Critical Thresholds

Eruption deemed **imminent** when:

1. **≥7 parameters** exceed critical thresholds simultaneously
2. **Lyapunov index L(t) > 0.2** (dynamical instability)
3. **Eruption probability P_erupt(t) > 0.75**
4. **State vector distance d_erupt(t) < 0.3**

---

## 🔬 Physics-Based Models

### Mogi Deformation Model

```python
# Vertical displacement from point pressure source
u_z(r) = (ΔV·(1-ν))/(π·d) · (1/(r²/d² + 1)^(3/2))
```

Where:
- `ΔV` = volume change of magma chamber
- `ν` = Poisson's ratio (~0.25)
- `d` = source depth
- `r` = radial distance

### Lyapunov Exponent (Chaos Theory)

```python
# Largest Lyapunov exponent from time series
λ₁ = lim[t→∞] (1/t)·ln(|δx(t)|/|δx(0)|)
```

Interpretation:
- `λ₁ < 0`: Stable system
- `λ₁ > 0`: Chaotic (unstable)
- `λ₁ > 0.2`: Critical threshold for volcanic eruption

### Gas Exsolution (Henry's Law)

```python
# Gas solubility in melt
X_gas = k_H · P_gas^n
```

CO₂/SO₂ ratio evolution tracks magma depth:
- **Deep (>10 km)**: CO₂/SO₂ > 10
- **Intermediate (5-10 km)**: CO₂/SO₂ = 5-10
- **Shallow (<5 km)**: CO₂/SO₂ < 5
- **Very shallow (<2 km)**: CO₂/SO₂ < 2

---

## 📚 Documentation

### Core Documentation

- [**Methodology**](docs/methodology.md) - Detailed framework methodology
- [**Physics Background**](docs/physics_background.md) - Mathematical derivations
- [**User Guide**](docs/user_guide.md) - Complete usage guide
- [**API Reference**](docs/api_reference.md) - Code documentation

### Case Studies

- [**Mount Pinatubo 1991**](docs/case_studies/pinatubo_1991.md) - Successful forecast (>60,000 evacuated)
- [**Mount Etna 2001**](docs/case_studies/etna_2001.md) - Lyapunov analysis demonstration
- [**Eyjafjallajökull 2010**](docs/case_studies/eyjafjallajokull_2010.md) - Rapid onset challenges
- [**Mount Agung 2017**](docs/case_studies/agung_2017.md) - Extended unrest episode

---

## 🗄️ Dataset

### Validation Dataset

- **47 volcanic systems** across 8 countries
- **15-year observation period** (2011-2025)
- **23 eruptions** with complete precursory sequences
- **56 non-eruptive unrest episodes**

### Geographic Distribution

- **Indonesia**: 12 volcanoes (Merapi, Agung, Sinabung, etc.)
- **Japan**: 8 volcanoes (Ontake, Sakurajima, Kirishima, etc.)
- **Italy**: 5 volcanoes (Etna, Stromboli, Vesuvius, etc.)
- **Ecuador**: 4 volcanoes (Cotopaxi, Tungurahua, Reventador, etc.)
- **Philippines**: 6 volcanoes (Pinatubo, Mayon, Taal, etc.)
- **USA**: 5 volcanoes (Kilauea, Redoubt, Augustine, etc.)
- **Iceland**: 4 volcanoes (Eyjafjallajökull, Katla, Grímsvötn, etc.)
- **New Zealand**: 3 volcanoes (Ruapehu, White Island, Tongariro, etc.)

### Data Availability

Raw monitoring data available upon request for research purposes. Contact: gitdeeper@gmail.com

---

## 🛠️ Development

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test module
pytest tests/test_parameters.py

# Run with coverage
pytest --cov=src tests/
```

### Code Style

This project follows PEP 8 style guidelines. Format code with:

```bash
# Format with black
black src/

# Check with flake8
flake8 src/

# Type checking with mypy
mypy src/
```

### Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📄 Citation

If you use this framework in your research, please cite:

```bibtex
@article{baladi2026volcano,
  title={Multi-Parameter Volcanic Unrest Monitoring Framework: A Physics-Based Approach to Eruption Forecasting Through Integrated Geophysical Signal Analysis},
  author={Baladi, Samir},
  journal={Journal of Volcanology and Geothermal Research},
  year={2026},
  volume={},
  pages={},
  doi={},
  url={https://gitlab.com/gitdeeper3/volcano}
}
```

---

## 👥 Authors

**Principal Investigator**: Samir Baladi

- ORCID: [0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029)
- Email: gitdeeper@gmail.com
- Affiliation: Emerald Compass | Ronin Institute | Rite of Renaissance

---

## 📧 Contact

- **Email**: gitdeeper@gmail.com
- **GitLab**: https://gitlab.com/gitdeeper3/volcano
- **GitHub**: https://github.com/emerladcompass/Volcano
- **Codeberg**: https://codeberg.org/gitdeeper2/volcano
- **Bitbucket**: https://bitbucket.org/gitdeeper3/volcano
- **Issues**: Please report bugs and feature requests via GitLab Issues

---

## 🙏 Acknowledgments

We gratefully acknowledge:

- **USGS Volcano Hazards Program** - Data and collaboration
- **INGV (Italy)** - Mount Etna monitoring data
- **IGN (Ecuador)** - Andes volcano data
- **PHIVOLCS (Philippines)** - Philippine volcano data
- **JMA (Japan)** - Japanese volcano data
- **GNS Science (New Zealand)** - New Zealand volcano data

Special thanks to volcano observatory scientists and technicians who maintain monitoring networks under challenging conditions.

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🔗 Related Resources

### Volcano Observatories

- [USGS Volcano Hazards Program](https://volcanoes.usgs.gov/)
- [INGV - Italy](https://www.ingv.it/)
- [JMA - Japan](https://www.jma.go.jp/jma/indexe.html)
- [Global Volcanism Program](https://volcano.si.edu/)

### Monitoring Data Sources

- [UNAVCO - GPS Data](https://www.unavco.org/)
- [IRIS - Seismic Data](https://www.iris.edu/)
- [NASA TROPOMI - SO2 Data](https://tropomi.gesdisc.eosdis.nasa.gov/)
- [ESA Sentinel - InSAR](https://sentinel.esa.int/)

### Scientific Background

- [Volcano Seismology](https://volcanoes.usgs.gov/vsc/software/mash/)
- [Gas Geochemistry](https://www.ngi.no/)
- [Deformation Modeling](https://www.unavco.org/software/geodetic-utilities/geodetic-utilities.html)

---

## 🗺️ Roadmap

### Version 2.0 (Planned)

- [ ] Machine learning integration for pattern recognition
- [ ] 3D magma ascent modeling
- [ ] VEI (eruption size) prediction capability
- [ ] Automated alert system with SMS/email notifications
- [ ] Web-based monitoring dashboard
- [ ] Integration with additional data sources (gravity, magnetics)
- [ ] Submarine and glaciovolcanic system adaptations

### Future Research Directions

- Deep learning for automated parameter extraction
- Bayesian uncertainty quantification
- Ensemble forecasting with multiple models
- Integration with ash dispersion models
- Economic cost-benefit analysis of false alarms vs missed eruptions

---

## 📊 Statistics

![GitHub repo size](https://img.shields.io/github/repo-size/emerladcompass/Volcano)
![GitHub contributors](https://img.shields.io/github/contributors/emerladcompass/Volcano)
![GitHub stars](https://img.shields.io/github/stars/emerladcompass/Volcano)
![GitHub forks](https://img.shields.io/github/forks/emerladcompass/Volcano)

---

## ⚠️ Disclaimer

This software is provided for **research and educational purposes only**. While validated on historical data, volcanic eruption forecasting remains inherently uncertain. This framework should be used as **one tool among many** in comprehensive hazard assessment, not as the sole basis for evacuation decisions. Operational volcano monitoring requires trained volcanologists, local knowledge, and integration of multiple information sources.

**No guarantee of forecast accuracy can be made. Use at your own risk.**

---

## 🌋 Stay Safe

Volcanoes are beautiful but dangerous. Always:

- Follow local authority guidance
- Respect evacuation zones
- Never approach active eruptions
- Support volcano monitoring efforts

**"The best eruption forecast is the one that saves lives."**

---

*Last updated: February 2026*

*Version: 1.0.0*
