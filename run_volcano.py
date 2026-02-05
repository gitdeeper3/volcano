#!/usr/bin/env python3
"""
🌋 Volcano Monitoring Framework - Command Line Interface
Fixed version with proper TXT file saving.
"""

import argparse
import logging
import sys
import os
from pathlib import Path

# Add src to path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir / 'src'))

try:
    from src.integration.vuap import VolcanicMonitoringFramework
    IMPORT_SUCCESS = True
except ImportError as e:
    print(f"⚠️  Import error: {e}")
    IMPORT_SUCCESS = False

def setup_logging(level=logging.INFO):
    """Configure logging."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

def save_txt_report(report: dict, output_dir: str = "results/reports"):
    """
    Save report as TXT file.
    
    Args:
        report: Report dictionary from generate_vuap_report()
        output_dir: Directory to save the report
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create safe filename
        volcano_safe = ''.join(c if c.isalnum() else '_' for c in report['volcano'])
        timestamp = report['timestamp'].replace(':', '').replace('-', '').replace('T', '_').split('.')[0]
        filename = f"{output_dir}/{volcano_safe}_{timestamp}.txt"
        
        # Format TXT report
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write(f"🌋 VUAP REPORT: {report['volcano']}\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"📅 TIMESTAMP: {report['timestamp']}\n")
            f.write(f"🚨 ALERT LEVEL: {report['alert_level']}\n")
            f.write(f"📊 ERUPTION PROBABILITY: {report['eruption_probability']:.2%}\n\n")
            
            f.write("📈 STATE VECTOR:\n")
            params = ['S', 'P', 'G', 'D', 'H', 'E', 'W', 'L', 'R']
            vector = report['state_vector']
            for i, (param, value) in enumerate(zip(params, vector)):
                f.write(f"  {param}: {float(value):.3f}")
                if (i + 1) % 3 == 0:
                    f.write("\n")
                else:
                    f.write(" | ")
            f.write("\n\n")
            
            f.write("🚦 THRESHOLD STATUS:\n")
            for key, value in report['threshold_status'].items():
                status = "✅ ACTIVE" if value else "☑️ INACTIVE"
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
        
        print(f"💾 TXT report saved: {filename}")
        return filename
        
    except Exception as e:
        print(f"❌ Failed to save TXT report: {e}")
        return None

def main():
    """Main CLI entry point."""
    if not IMPORT_SUCCESS:
        print("❌ Failed to import modules")
        return 1
    
    parser = argparse.ArgumentParser(
        description='🌋 Multi-parameter volcanic unrest monitoring framework',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--volcano', required=True, help='Name of volcano to monitor')
    parser.add_argument('--demo', action='store_true', help='Run with demo data')
    parser.add_argument('--report', action='store_true', help='Generate single report')
    parser.add_argument('--monitor', action='store_true', help='Run real-time monitoring')
    parser.add_argument('--interval', type=int, default=3600, help='Monitoring interval in seconds')
    parser.add_argument('--output', default='results/reports', help='Output directory for reports')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--simple', action='store_true', help='Simple output format')
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(log_level)
    
    logger = logging.getLogger(__name__)
    logger.info(f"🌋 Starting volcano monitoring for {args.volcano}")
    
    # Initialize framework
    try:
        framework = VolcanicMonitoringFramework(args.volcano)
    except Exception as e:
        logger.error(f"Failed to initialize: {e}")
        return 1
    
    # Use demo data if requested
    if args.demo:
        logger.info("📊 Using demo data mode")
        import numpy as np
        
        # Set demo parameters
        framework.parameters = {
            'S': np.random.uniform(0.6, 0.9),
            'P': np.random.uniform(0.5, 0.8),
            'G': np.random.uniform(0.4, 0.7),
            'D': np.random.uniform(0.5, 0.8),
            'H': np.random.uniform(0.3, 0.6),
            'E': np.random.uniform(0.2, 0.5),
            'W': np.random.uniform(0.4, 0.7),
            'L': np.random.uniform(0.1, 0.3),
            'R': np.random.uniform(0.5, 0.8),
        }
    
    # Run selected mode
    try:
        if args.monitor:
            logger.info(f"📡 Starting real-time monitoring")
            framework.run_real_time_monitoring(args.interval)
        
        elif args.report or not args.monitor:
            # Generate report
            report = framework.generate_vuap_report()
            
            # Save TXT report
            saved_file = save_txt_report(report, args.output)
            
            # Display summary
            if args.simple:
                print(f"\n🌋 {report['volcano']}")
                print(f"📊 Probability: {report['eruption_probability']:.1%}")
                print(f"🚨 Status: {report['alert_level']}")
                if saved_file:
                    print(f"💾 Saved: {saved_file}")
            else:
                print(f"\n{'='*60}")
                print(f"🌋 VUAP REPORT: {report['volcano']}")
                print(f"{'='*60}")
                print(f"📅 Timestamp: {report['timestamp']}")
                print(f"📊 Eruption Probability: {report['eruption_probability']:.2%}")
                print(f"🚨 Alert Level: {report['alert_level']}")
                print(f"\n📈 State Vector: {[f'{float(v):.2f}' for v in report['state_vector']]}")
                
                print(f"\n💾 TXT Report: {saved_file or 'Not saved'}")
                print(f"{'='*60}")
        
        return 0
        
    except KeyboardInterrupt:
        logger.info("⏹️ Stopped by user")
        return 0
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
