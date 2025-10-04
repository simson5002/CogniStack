#!/usr/bin/env python3
"""
Script to train MBTI and OCEAN personality models
Run this script to download datasets and train the models
"""

import os
import sys
from data_loader import DatasetLoader
from models import MBTIModel, OCEANModel
from config import MODEL_SAVE_PATH

def main():
    print("Starting model training process...")
    
    # Create necessary directories
    os.makedirs(MODEL_SAVE_PATH, exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    # Initialize data loader
    loader = DatasetLoader()
    
    try:
        # Download and preprocess MBTI data
        print("\n=== Processing MBTI Dataset ===")
        mbti_X, mbti_y, mbti_features = loader.download_mbti_dataset()
        print(f"MBTI dataset shape: {mbti_X.shape}")
        print(f"MBTI features: {len(mbti_features)}")
        print(f"MBTI types: {len(set(mbti_y))}")
        
        # Train MBTI model
        print("\n=== Training MBTI Model ===")
        mbti_model = MBTIModel()
        mbti_accuracy = mbti_model.train(mbti_X, mbti_y)
        mbti_model.save(os.path.join(MODEL_SAVE_PATH, "mbti_model.pkl"))
        print(f"MBTI model saved with accuracy: {mbti_accuracy:.3f}")
        
        # Download and preprocess OCEAN data
        print("\n=== Processing OCEAN Dataset ===")
        ocean_X, ocean_y, ocean_features, ocean_cols = loader.download_ocean_dataset()
        print(f"OCEAN dataset shape: {ocean_X.shape}")
        print(f"OCEAN features: {len(ocean_features)}")
        print(f"OCEAN dimensions: {ocean_cols}")
        
        # Train OCEAN model
        print("\n=== Training OCEAN Model ===")
        ocean_model = OCEANModel()
        ocean_mse = ocean_model.train(ocean_X, ocean_y)
        ocean_model.save(os.path.join(MODEL_SAVE_PATH, "ocean_model.pkl"))
        print(f"OCEAN model saved with MSE scores: {ocean_mse}")
        
        print("\n=== Training Complete ===")
        print("Models are ready to use!")
        print(f"MBTI model accuracy: {mbti_accuracy:.3f}")
        print(f"OCEAN model MSE: {ocean_mse}")
        
    except Exception as e:
        print(f"Error during training: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
