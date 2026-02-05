FROM python:3.11-slim

LABEL maintainer="Samir Baladi <gitdeeper@gmail.com>"
LABEL version="1.0.0"
LABEL description="Multi-parameter volcanic unrest monitoring framework"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    gfortran \
    libgomp1 \
    libblas-dev \
    liblapack-dev \
    libhdf5-dev \
    libnetcdf-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Install the package
RUN pip install --no-cache-dir -e .

# Create necessary directories
RUN mkdir -p /app/data /app/results /app/reports /app/logs

# Expose dashboard port
EXPOSE 8050

# Default command (can be overridden)
CMD ["python", "src/integration/vuap.py"]
