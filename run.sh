#!/bin/bash
# Script to run the Alchemist API

# Check for Python installation
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3 and try again."
    exit 1
fi

# Check for virtual environment or create one
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install or upgrade dependencies
echo "Installing dependencies..."
pip install --upgrade -r requirements.txt

# Set development environment variables
export LOGLEVEL=INFO

# Run the application
echo "Starting Alchemist API server..."
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Deactivate virtual environment on exit
deactivate
