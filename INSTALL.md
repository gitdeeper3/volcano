# Quick Installation Guide

## 1. Clone Repository
```bash
git clone https://gitlab.com/gitdeeper3/volcano.git
cd volcano
```

## 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## 3. Test Installation
```bash
python run_volcano.py --volcano "Test" --demo --report --simple
```

## 4. Run Real Monitoring
```bash
python run_volcano.py --volcano "Etna" --demo --monitor --interval 3600
```

## 5. For Production
```bash
# Docker
docker build -t volcano-monitoring .
docker run -d -p 8050:8050 volcano-monitoring

# Or use pip
pip install volcano-monitoring
```

## Troubleshooting
If you get import errors:
```bash
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"
```

## Need Help?
- Email: gitdeeper@gmail.com
- GitLab: https://gitlab.com/gitdeeper3/volcano/issues
- Docs: Check docs/ directory
