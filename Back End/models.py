import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import os
from config import MODEL_SAVE_PATH

class MBTIModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def train(self, X, y):
        """Train the MBTI model"""
        print("Training MBTI model...")
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale the features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train the model
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"MBTI Model Accuracy: {accuracy:.3f}")
        
        self.is_trained = True
        return accuracy
    
    def predict(self, X):
        """Predict MBTI type"""
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)
    
    def predict_proba(self, X):
        """Predict MBTI type probabilities"""
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        X_scaled = self.scaler.transform(X)
        return self.model.predict_proba(X_scaled)
    
    def save(self, filepath):
        """Save the model"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump({
            'model': self.model,
            'scaler': self.scaler,
            'is_trained': self.is_trained
        }, filepath)
    
    def load(self, filepath):
        """Load the model"""
        data = joblib.load(filepath)
        self.model = data['model']
        self.scaler = data['scaler']
        self.is_trained = data['is_trained']

class OCEANModel:
    def __init__(self):
        self.models = {
            'O': RandomForestRegressor(n_estimators=100, random_state=42),
            'C': RandomForestRegressor(n_estimators=100, random_state=42),
            'E': RandomForestRegressor(n_estimators=100, random_state=42),
            'A': RandomForestRegressor(n_estimators=100, random_state=42),
            'N': RandomForestRegressor(n_estimators=100, random_state=42)
        }
        self.scaler = StandardScaler()
        self.is_trained = False
        
    def train(self, X, y):
        """Train the OCEAN model"""
        print("Training OCEAN model...")
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale the features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train each OCEAN dimension separately
        mse_scores = {}
        for i, trait in enumerate(['O', 'C', 'E', 'A', 'N']):
            self.models[trait].fit(X_train_scaled, y_train[:, i])
            y_pred = self.models[trait].predict(X_test_scaled)
            mse = mean_squared_error(y_test[:, i], y_pred)
            mse_scores[trait] = mse
            print(f"{trait} MSE: {mse:.3f}")
        
        self.is_trained = True
        return mse_scores
    
    def predict(self, X):
        """Predict OCEAN scores"""
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        X_scaled = self.scaler.transform(X)
        predictions = {}
        for trait in ['O', 'C', 'E', 'A', 'N']:
            predictions[trait] = self.models[trait].predict(X_scaled)
        
        return predictions
    
    def save(self, filepath):
        """Save the model"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump({
            'models': self.models,
            'scaler': self.scaler,
            'is_trained': self.is_trained
        }, filepath)
    
    def load(self, filepath):
        """Load the model"""
        data = joblib.load(filepath)
        self.models = data['models']
        self.scaler = data['scaler']
        self.is_trained = data['is_trained']
