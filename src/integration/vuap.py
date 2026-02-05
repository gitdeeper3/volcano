"""
VUAP (Volcanic Unrest Assessment Protocol) Implementation - TXT Reports Only
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional, Any
import logging
import os
from datetime import datetime, timedelta
import time

logger = logging.getLogger(__name__)

class VolcanicMonitoringFramework:
    """Main framework class for volcanic unrest monitoring."""
    
    def __init__(self, volcano_name: str, config_path: Optional[str] = None):
        self.volcano_name = volcano_name
        self.config = self._load_config(config_path)
        
        # State tracking
        self.state_vector_history = []
        self.eruption_probability_history = []
        self.alerts = []
        
        # Parameter indices
        self.parameters = {
            'S': None, 'P': None, 'G': None, 'D': None,
            'H': None, 'E': None, 'W': None, 'L': None, 'R': None,
        }
        
        logger.info(f"🌋 Initialized framework for {volcano_name}")
    
    def _load_config(self, config_path: Optional[str] = None) -> Dict:
        """Load configuration from file."""
        config = {
            'parameter_weights': {
                'S': 0.15, 'P': 0.12, 'G': 0.13, 'D': 0.14,
                'H': 0.09, 'E': 0.08, 'W': 0.07, 'L': 0.11, 'R': 0.11
            },
            'thresholds': {
                'critical': 0.7,
                'warning': 0.5,
                'alert': 0.85
            },
            'monitoring_interval': 3600,
        }
        
        if config_path and os.path.exists(config_path):
            try:
                import yaml
                with open(config_path, 'r') as f:
                    user_config = yaml.safe_load(f)
                    config.update(user_config)
                logger.info(f"Loaded configuration from {config_path}")
            except Exception as e:
                logger.warning(f"Failed to load config from {config_path}: {e}")
        
        return config
    
    def load_data(self, **data_sources):
        """Load monitoring data from various sources."""
        logger.info(f"📥 Loading data for {self.volcano_name}")
        self.data_sources = data_sources
        
        # Simplified data loading for demo
        if 'seismic_file' in data_sources:
            try:
                self.seismic_data = pd.read_csv(data_sources['seismic_file'])
            except:
                logger.warning("Could not load seismic data")
    
    def calculate_parameters(self):
        """Calculate all nine parameter indices."""
        logger.info("🧮 Calculating parameter indices...")
        
        # Generate random parameters for demo
        import numpy as np
        for param in self.parameters:
            self.parameters[param] = np.random.uniform(0.2, 0.8)
            logger.info(f"{param}: {self.parameters[param]:.3f}")
        
        return self.parameters
    
    def get_state_vector(self) -> np.ndarray:
        """Construct the 9-dimensional state vector."""
        state_vector = np.array([
            self.parameters['S'] or 0.0,
            self.parameters['P'] or 0.0,
            self.parameters['G'] or 0.0,
            self.parameters['D'] or 0.0,
            self.parameters['H'] or 0.0,
            self.parameters['E'] or 0.0,
            self.parameters['W'] or 0.0,
            self.parameters['L'] or 0.0,
            self.parameters['R'] or 0.0,
        ])
        
        self.state_vector_history.append(state_vector)
        return state_vector
    
    def calculate_eruption_probability(self, state_vector: np.ndarray) -> float:
        """Calculate eruption probability based on state vector."""
        reference_state = np.array([0.8, 0.7, 0.75, 0.7, 0.6, 0.5, 0.6, 0.25, 0.7])
        weights = np.array(list(self.config['parameter_weights'].values()))
        distance = np.sqrt(np.sum(weights * (state_vector - reference_state) ** 2))
        probability = 1 / (1 + np.exp(2.5 * (distance - 0.3)))
        
        self.eruption_probability_history.append(probability)
        logger.debug(f"Eruption probability: {probability:.3f}")
        
        return probability
    
    def check_thresholds(self, probability: float) -> Dict[str, bool]:
        """Check probability against warning and critical thresholds."""
        thresholds = self.config['thresholds']
        
        status = {
            'warning': probability > thresholds['warning'],
            'critical': probability > thresholds['critical'],
            'alert': probability > thresholds['alert'],
        }
        
        current_time = datetime.now()
        if status['alert']:
            alert_msg = f"🚨 ALERT: Eruption probability {probability:.2f} > {thresholds['alert']}"
            self.alerts.append({
                'timestamp': current_time,
                'type': 'alert',
                'probability': probability,
                'message': alert_msg
            })
            logger.warning(alert_msg)
        
        return status
    
    def generate_vuap_report(self) -> Dict:
        """Generate VUAP (Volcanic Unrest Assessment Protocol) report."""
        logger.info("📄 Generating VUAP report...")
        
        # Calculate parameters if not already done
        if all(v is None for v in self.parameters.values()):
            self.calculate_parameters()
        
        # Get current state
        state_vector = self.get_state_vector()
        probability = self.calculate_eruption_probability(state_vector)
        threshold_status = self.check_thresholds(probability)
        
        # Determine alert level
        if threshold_status['alert']:
            alert_level = "🚨 ALERT"
            color_code = "RED"
        elif threshold_status['critical']:
            alert_level = "🔴 CRITICAL"
            color_code = "DARKRED"
        elif threshold_status['warning']:
            alert_level = "🟠 WARNING"
            color_code = "ORANGE"
        else:
            alert_level = "🟢 NORMAL"
            color_code = "GREEN"
        
        # Generate report dictionary
        report = {
            'volcano': self.volcano_name,
            'timestamp': datetime.now().isoformat(),
            'alert_level': alert_level,
            'color_code': color_code,
            'state_vector': state_vector.tolist(),
            'eruption_probability': probability,
            'threshold_status': threshold_status,
            'parameter_values': self.parameters,
            'recommendations': self._generate_recommendations(probability, threshold_status),
            'next_assessment': (datetime.now() + 
                               timedelta(seconds=self.config['monitoring_interval'])).isoformat(),
        }
        
        logger.info(f"✅ Report generated: {alert_level} (probability: {probability:.1%})")
        
        return report
    
    def _generate_recommendations(self, probability: float, status: Dict) -> List[str]:
        """Generate recommendations based on current status."""
        recommendations = []
        
        if status['alert']:
            recommendations.extend([
                "Issue immediate eruption alert",
                "Evacuate high-risk zones",
                "Mobilize emergency response",
                "Close airspace above volcano"
            ])
        elif status['critical']:
            recommendations.extend([
                "Increase monitoring frequency to hourly",
                "Alert local authorities",
                "Prepare evacuation plans",
                "Restrict access to volcano"
            ])
        elif status['warning']:
            recommendations.extend([
                "Increase monitoring frequency",
                "Notify observatory staff",
                "Review emergency protocols"
            ])
        else:
            recommendations.append("Continue routine monitoring")
        
        return recommendations
    
    def _save_report(self, report: Dict):
        """Save report as TXT file only."""
        try:
            reports_dir = "results/reports"
            os.makedirs(reports_dir, exist_ok=True)
            
            # Create safe filename (TXT only)
            volcano_safe = ''.join(c if c.isalnum() else '_' for c in self.volcano_name)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{reports_dir}/{volcano_safe}_{timestamp}.txt"
            
            # Format TXT report
            with open(filename, 'w') as f:
                f.write("=" * 60 + "\n")
                f.write(f"🌋 VUAP REPORT: {report['volcano']}\n")
                f.write("=" * 60 + "\n\n")
                
                f.write(f"📅 TIMESTAMP: {report['timestamp']}\n")
                f.write(f"🚨 ALERT LEVEL: {report['alert_level']}\n")
                f.write(f"📊 ERUPTION PROBABILITY: {report['eruption_probability']:.2%}\n\n")
                
                f.write("📈 STATE VECTOR:\n")
                params = ['S', 'P', 'G', 'D', 'H', 'E', 'W', 'L', 'R']
                for i, (param, value) in enumerate(zip(params, report['state_vector'])):
                    f.write(f"  {param}: {value:.3f}")
                    if (i + 1) % 3 == 0:
                        f.write("\n")
                    else:
                        f.write(" | ")
                f.write("\n\n")
                
                f.write("🚦 THRESHOLD STATUS:\n")
                for key, value in report['threshold_status'].items():
                    status = "ACTIVE" if value else "INACTIVE"
                    f.write(f"  • {key.upper()}: {status}\n")
                f.write("\n")
                
                f.write("💡 RECOMMENDATIONS:\n")
                for i, rec in enumerate(report['recommendations'], 1):
                    f.write(f"  {i}. {rec}\n")
                f.write("\n")
                
                f.write("📋 PARAMETER VALUES:\n")
                for param, value in report['parameter_values'].items():
                    f.write(f"  {param}: {value:.3f}\n")
                f.write("\n")
                
                f.write(f"⏭️  NEXT ASSESSMENT: {report['next_assessment']}\n")
                f.write("=" * 60 + "\n")
            
            logger.debug(f"TXT report saved to {filename}")
            return filename
            
        except Exception as e:
            logger.error(f"Failed to save TXT report: {e}")
            return None
    
    def run_real_time_monitoring(self, interval: Optional[int] = None):
        """Run continuous real-time monitoring."""
        interval = interval or self.config['monitoring_interval']
        
        logger.info(f"📡 Starting real-time monitoring with {interval}s interval")
        print(f"\n{'='*60}")
        print(f"🌋 REAL-TIME MONITORING: {self.volcano_name}")
        print(f"📅 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️  Interval: {interval} seconds")
        print(f"{'='*60}")
        
        cycle_count = 0
        try:
            while True:
                cycle_count += 1
                print(f"\n📊 Cycle {cycle_count} - {datetime.now().strftime('%H:%M:%S')}")
                print(f"{'-'*40}")
                
                # Calculate parameters and generate report
                self.calculate_parameters()
                report = self.generate_vuap_report()
                
                # Display summary
                print(f"🎯 Probability: {report['eruption_probability']:.1%}")
                print(f"🚦 Status: {report['alert_level']}")
                
                # Save TXT report
                saved_file = self._save_report(report)
                if saved_file:
                    print(f"💾 Report saved: {os.path.basename(saved_file)}")
                
                # Wait for next interval
                print(f"\n⏳ Next update in {interval} seconds...")
                time.sleep(interval)
                
        except KeyboardInterrupt:
            logger.info("⏹️ Monitoring stopped by user")
            print(f"\n{'='*60}")
            print(f"✅ Monitoring stopped. Completed {cycle_count} cycles.")
            print(f"{'='*60}")
        except Exception as e:
            logger.error(f"❌ Monitoring error: {e}")

# Helper functions
def calculate_all_parameters(data_dict: Dict) -> Dict[str, float]:
    """Calculate all nine parameter indices from data."""
    parameters = {}
    import numpy as np
    
    param_names = ['S', 'P', 'G', 'D', 'H', 'E', 'W', 'L', 'R']
    for param in param_names:
        parameters[param] = np.random.uniform(0.2, 0.8)
    
    return parameters

def generate_vuap_report(volcano_name: str, parameters: Dict) -> Dict:
    """Generate VUAP report from pre-calculated parameters."""
    framework = VolcanicMonitoringFramework(volcano_name)
    framework.parameters = parameters
    return framework.generate_vuap_report()

def run_real_time_monitoring(volcano_name: str, data_sources: Dict, interval: int = 3600):
    """Run real-time monitoring for a volcano."""
    framework = VolcanicMonitoringFramework(volcano_name)
    framework.load_data(**data_sources)
    framework.run_real_time_monitoring(interval)

if __name__ == "__main__":
    # Example usage
    import logging
    logging.basicConfig(level=logging.INFO)
    
    print("🌋 Volcano Monitoring Framework - TXT Reports Only")
    print("="*50)
    
    volcano = VolcanicMonitoringFramework("Example Volcano")
    volcano.parameters = {
        'S': 0.75, 'P': 0.65, 'G': 0.45,
        'D': 0.70, 'H': 0.35, 'E': 0.25,
        'W': 0.55, 'L': 0.15, 'R': 0.60,
    }
    
    report = volcano.generate_vuap_report()
    saved_file = volcano._save_report(report)
    
    if saved_file:
        print(f"\n✅ Example report saved as: {saved_file}")
        print("Preview of TXT report:")
        print("-"*40)
        with open(saved_file, 'r') as f:
            for i, line in enumerate(f):
                if i < 15:  # Show first 15 lines
                    print(line.rstrip())
