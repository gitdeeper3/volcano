# Deployment Guide

This document covers deployment options for the Volcano Monitoring Framework.

## 🚀 Quick Deployment Options

### Option 1: Python Virtual Environment (Development)
```bash
# Clone repository
git clone https://gitlab.com/gitdeeper3/volcano.git
cd volcano

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run system
python run_volcano.py --volcano "Etna" --demo --report
```

Option 2: Docker (Production)

```bash
# Build Docker image
docker build -t volcano-monitoring:latest .

# Run container
docker run -d \
  --name volcano-monitoring \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/results:/app/results \
  -p 8050:8050 \
  volcano-monitoring:latest
```

Option 3: Docker Compose (Multi-service)

```bash
docker-compose up -d
```

📦 Deployment Architectures

1. Single Node Deployment

```
┌─────────────────────────────────┐
│         Application Node         │
├─────────────────────────────────┤
│  Volcano Monitoring Framework   │
│  • Data Processing              │
│  • Parameter Calculation        │
│  • Alert System                 │
│  • Report Generation            │
└─────────────────────────────────┘
```

2. Distributed Deployment

```
┌─────────┐    ┌─────────┐    ┌─────────┐
│ Sensor  │    │  Edge   │    │  Cloud  │
│  Node   │───▶│ Processor│───▶│ Storage │
└─────────┘    └─────────┘    └─────────┘
      │              │              │
  [Seismic,      [Parameter    [Long-term
   GPS, Gas]      Calculation]   Analysis]
```

🔧 Configuration

Environment Variables

```bash
# Core Settings
export VOLCANO_LOG_LEVEL="INFO"
export VOLCANO_UPDATE_RATE="3600"
export VOLCANO_DATA_PATH="./data"

# Database Settings
export DATABASE_URL="sqlite:///volcano.db"
export REDIS_URL="redis://localhost:6379/0"

# Alert Settings
export ALERT_EMAIL_ENABLED="false"
export ALERT_SMS_ENABLED="false"
```

Configuration Files

1. config/default_config.yaml - Main system configuration
2. config/volcano_list.yaml - Volcano metadata
3. config/parameter_weights.yaml - Parameter weighting
4. config/thresholds.yaml - Alert thresholds

🐳 Docker Deployment

Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install -e .
CMD ["python", "run_volcano.py", "--volcano", "Etna", "--demo", "--monitor"]
```

Docker Compose

```yaml
version: '3.8'
services:
  volcano:
    build: .
    ports:
      - "8050:8050"
    volumes:
      - ./data:/app/data
      - ./results:/app/results
    environment:
      - LOG_LEVEL=INFO
      - UPDATE_RATE=3600
```

📱 Mobile Deployment (Termux)

Android/Termux Setup

```bash
# Update packages
pkg update && pkg upgrade

# Install Python
pkg install python

# Install dependencies
pip install numpy pandas matplotlib scipy

# Run Volcano Monitoring
python run_volcano.py --volcano "Etna" --demo --report --simple
```

🖥️ System Requirements

Minimum Requirements

· CPU: 1 GHz processor
· RAM: 512 MB
· Storage: 100 MB
· OS: Linux, macOS, Windows, or Android (Termux)

Recommended Requirements

· CPU: 2+ GHz multi-core
· RAM: 2 GB
· Storage: 1 GB SSD
· Python: 3.11+

🔐 Security Considerations

1. Network Security

```yaml
firewall:
  - Allow: 22 (SSH)
  - Allow: 8050 (Web Dashboard)
  - Deny: All other ports
```

2. Data Protection

· Encrypt sensitive configuration files
· Use secure protocols for data transmission
· Regular backup of critical data

3. Access Control

· Implement role-based access control
· Use API keys for external access
· Regular audit of access logs

📊 Monitoring & Logging

Log Files

```bash
# View logs
tail -f logs/volcano_monitoring.log

# Log rotation configuration
logs/
├── volcano.log      # Current log
├── volcano.log.1    # Previous day
└── volcano.log.2    # Two days ago
```

Health Checks

```bash
# System health check
curl http://localhost:8050/health 2>/dev/null || echo "Dashboard not running"

# Check database connection
python -c "import sqlite3; conn = sqlite3.connect('volcano.db'); print('Database OK')"
```

🔄 Update Procedures

Rolling Update

```bash
# 1. Pull latest changes
git pull origin main

# 2. Update dependencies
pip install -r requirements.txt --upgrade

# 3. Restart service
pkill -f "python run_volcano.py"
python run_volcano.py --volcano "Etna" --demo --monitor &
```

Docker Update

```bash
# Pull new image
docker pull gitdeeper3/volcano-monitoring:latest

# Update container
docker-compose down
docker-compose pull
docker-compose up -d
```

🚨 Troubleshooting

Common Issues

Issue: Import errors

```bash
# Solution: Set Python path
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"
```

Issue: Permission denied

```bash
# Solution: Fix permissions
chmod +x run_volcano.py publish.sh
chmod 755 data/ results/ logs/
```

Issue: Missing dependencies

```bash
# Solution: Install requirements
pip install -r requirements.txt --upgrade
```

Debug Mode

```bash
# Run with debug logging
export VOLCANO_LOG_LEVEL="DEBUG"
python run_volcano.py --volcano "Test" --demo --report --verbose
```

📈 Scaling Considerations

Vertical Scaling

· Increase CPU/RAM resources
· Optimize database performance
· Use faster storage (SSD)

Horizontal Scaling

· Add more monitoring nodes
· Implement load balancing
· Use distributed processing

Database Scaling

· SQLite → PostgreSQL for production
· Redis for caching
· TimescaleDB for time-series data

🎯 Production Checklist

· Security audit completed
· Backup system in place
· Monitoring configured
· Load testing performed
· Documentation updated
· Team trained on procedures
· Disaster recovery plan tested
· Performance benchmarks established

📞 Support

For deployment assistance:

· Email: gitdeeper@gmail.com
· GitLab Issues: https://gitlab.com/gitdeeper3/volcano/-/issues
· Documentation: docs/ directory
· Repository: https://gitlab.com/gitdeeper3/volcano

GitLab Repository Information

· URL: https://gitlab.com/gitdeeper3/volcano
· Username: gitdeeper3
· Access: Public repository
· CI/CD: Enabled (see .gitlab-ci.yml)

---

Deployment Examples by Use Case

1. Research Installation

```bash
# For academic/research use
git clone https://gitlab.com/gitdeeper3/volcano.git
cd volcano
pip install -e .
python notebooks/01_data_exploration.ipynb
```

2. Observatory Deployment

```bash
# For volcano observatory use
docker-compose -f docker-compose-observatory.yml up -d
# Includes: PostgreSQL, Redis, Dashboard, API
```

3. Cloud Deployment

```bash
# For AWS/GCP/Azure
git clone https://gitlab.com/gitdeeper3/volcano.git
cd volcano
./deploy/cloud-deploy.sh --provider aws --region us-east-1
```

Version Information

· Current Version: 1.0.0
· Python Version: 3.8+
· License: MIT
· Repository: https://gitlab.com/gitdeeper3/volcano

---

Last Updated: 2026-02-05
