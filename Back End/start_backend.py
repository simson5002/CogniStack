#!/usr/bin/env python3
"""
Startup script for the Personality Assessment Backend
This script will train models if they don't exist and start the API server
"""

import os
import sys
import subprocess
import time
from pathlib import Path

# Add current directory to Python path for local imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def check_requirements():
    """Check if all required packages are installed"""
    required_packages = [
        ("fastapi", "fastapi"),
        ("uvicorn", "uvicorn"),
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("sklearn", "scikit-learn"),
        ("kaggle", "kaggle"),
        ("joblib", "joblib"),
        ("python-dotenv", "python-dotenv")
    ]
    
    missing_packages = []
    
    for import_name, package_name in required_packages:
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(package_name)
    
    if missing_packages:
        print(f"✗ Missing packages: {', '.join(missing_packages)}")
        print("Please install requirements: pip install -r requirements.txt")
        return False
    else:
        print("✓ All required packages are installed")
        return True

def train_models_if_needed():
    """Train models if they don't exist"""
    models_dir = Path("models")
    mbti_model = models_dir / "mbti_model.pkl"
    ocean_model = models_dir / "ocean_model.pkl"
    
    if not mbti_model.exists() or not ocean_model.exists():
        print("Models not found. Training models...")
        try:
            subprocess.run([sys.executable, "train_models.py"], check=True)
            print("✓ Models trained successfully")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error training models: {e}")
            return False
    else:
        print("✓ Models already exist")
    
    return True

def start_api_server():
    """Start the FastAPI server"""
    print("Starting API server...")
    print("API will be available at: http://localhost:8000")
    print("API documentation at: http://localhost:8000/docs")
    print("Press Ctrl+C to stop the server")
    
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "api:app", 
            "--host", "0.0.0.0", 
            "--port", "8000", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")

def main():
    print("=== Personality Assessment Backend Startup ===")
    
    # Ensure we're in the Back End directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if we're in the right directory
    if not os.path.exists("api.py"):
        print("✗ Please run this script from the Back End directory")
        print(f"Current directory: {os.getcwd()}")
        print(f"Script location: {script_dir}")
        sys.exit(1)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Train models if needed
    if not train_models_if_needed():
        sys.exit(1)
    
    # Start the API server
    start_api_server()

if __name__ == "__main__":
    main()
