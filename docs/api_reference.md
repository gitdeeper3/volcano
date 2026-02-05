# API Reference

## Core Framework
### `VolcanicMonitoringFramework`
Main class for volcanic monitoring.

#### Methods:
- `load_data(**kwargs)`: Load monitoring data
- `calculate_parameters()`: Calculate 9 parameter indices
- `get_state_vector()`: Construct 9D state vector
- `calculate_eruption_probability()`: Get eruption probability
- `generate_vuap_report()`: Generate assessment report
- `run_real_time_monitoring()`: Continuous monitoring

## Parameter Modules
### Seismic Pulse
```python
calculate_seismic_pulse(seismic_data, config)
```

Pressure

```python
calculate_pressure(pressure_data, config)
```

Gas Flux

```python
calculate_gas_flux(gas_data, config)
```

Deformation

```python
calculate_deformation(gps_data, config)
```

Heat

```python
calculate_heat(thermal_data, config)
```

Electrokinetic

```python
calculate_electrokinetic(sp_data, config)
```

Water Flow

```python
calculate_water_flow(hydro_data, config)
```

Lyapunov

```python
calculate_lyapunov(time_series, config)
```

Resistivity

```python
calculate_resistivity(resistivity_data, config)
```

Physics Models

Mogi Model

```python
calculate_displacement(x, y, source_depth, volume_change)
```

Gas Solubility

```python
calculate_solubility(temperature, pressure, composition)
```

Utility Functions

Configuration

```python
load_config(config_path)
```

Data I/O

```python
load_data_file(filepath, format)
```

Helper Functions

```python
calculate_all_parameters(data_dict)
generate_vuap_report(volcano_name, parameters)
run_real_time_monitoring(volcano_name, data_sources, interval)
```

