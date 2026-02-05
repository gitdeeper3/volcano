# Contributing to Volcano Monitoring Framework

Thank you for your interest in contributing to the Volcano Monitoring Framework! This document provides guidelines and instructions for contributing to the project.

## 🌟 First Time Contributors

If you're new to the project, we recommend:
1. Reading the [README.md](README.md) for project overview
2. Reviewing the [ARCHITECTURE.md](ARCHITECTURE.md) for system design
3. Looking at existing issues labeled "good first issue"

## 🏗️ Development Environment Setup

### Prerequisites
- Python 3.8 or higher
- Git
- pip (Python package manager)

### Installation
```bash
# Clone the repository
git clone https://gitlab.com/gitdeeper3/volcano.git
cd volcano

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

📁 Project Structure

```
volcano/
├── src/                    # Core source code
│   ├── integration/       # Multi-parameter integration
│   ├── parameters/        # Parameter calculations
│   ├── models/           # Physics-based models
│   ├── preprocessing/    # Data processing
│   ├── analysis/         # Statistical analysis
│   ├── visualization/    # Plotting and dashboards
│   └── utils/           # Utility functions
├── tests/                # Test suite
├── docs/                # Documentation
├── notebooks/           # Jupyter notebooks
├── scripts/            # Automation scripts
├── config/             # Configuration files
└── data/               # Data directory (structure only)
```

🔧 Development Workflow

1. Branch Strategy

· main: Production-ready code
· develop: Integration branch
· feature/*: New features
· bugfix/*: Bug fixes
· docs/*: Documentation updates

2. Creating a Feature

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes
# ...

# Commit changes
git add .
git commit -m "feat: description of changes"

# Push to remote
git push origin feature/your-feature-name
```

3. Commit Message Convention

We follow Conventional Commits:

· feat: New feature
· fix: Bug fix
· docs: Documentation
· style: Code style
· refactor: Code refactoring
· test: Tests
· chore: Maintenance

🧪 Testing

Run Tests

```bash
# Run all tests
pytest

# Run specific test module
pytest tests/test_parameters.py

# Run with coverage
pytest --cov=src tests/
```

Writing Tests

· Place tests in tests/ directory
· Test files should be named test_*.py
· Use descriptive test names
· Mock external dependencies

📝 Code Standards

Python Style Guide

We follow PEP 8 with Black formatter:

```bash
# Format code
black src/ tests/

# Check style
flake8 src/ tests/
```

Documentation

· All functions require docstrings
· Use NumPy docstring format
· Update relevant documentation when changing code

Type Hints

Use Python type hints for better code clarity:

```python
def process_sensor_data(data: List[float]) -> np.ndarray:
    """Process sensor data and return filtered results."""
    # Implementation
```

🐛 Issue Reporting

Before Reporting

1. Check existing issues
2. Search closed issues for solutions
3. Ensure you're using the latest version

Issue Template

```
## Description
[Clear description of the issue]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- OS: [e.g., Linux, Windows, macOS]
- Python Version: [e.g., 3.11.0]
- Volcano Monitoring Version: [e.g., 1.0.0]

## Additional Context
[Screenshots, logs, etc.]
```

🔄 Pull Request Process

PR Checklist

· Tests pass
· Code follows style guide
· Documentation updated
· Commit messages follow convention
· No breaking changes (or documented if necessary)

Review Process

1. Create draft PR for early feedback
2. Request review from maintainers
3. Address review comments
4. Wait for approval before merging

🎯 Areas for Contribution

High Priority

· New parameter algorithms
· Additional physics models
· Performance optimizations
· Data import/export modules

Medium Priority

· Additional test coverage
· Documentation improvements
· Example applications
· Visualization tools

Research Opportunities

· Advanced machine learning models
· Alternative forecasting algorithms
· Cross-validation improvements
· Field validation protocols

📞 Getting Help

· Documentation: Check the docs/ directory
· Issues: Use GitLab Issues
· Discussion: Project discussion boards
· Email: gitdeeper@gmail.com

📄 License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

---

GitLab Repository Information

· Repository: https://gitlab.com/gitdeeper3/volcano
· Username: gitdeeper3
· Maintainer: Samir Baladi
· Email: gitdeeper@gmail.com

Thank you for contributing to Volcano Monitoring Framework! 🎉
