"""
Model Training Module

This module performs machine learning model training and evaluation operations.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, silhouette_score
import joblib
import os
from typing import Optional, Union


class ModelTrainer:
    def __init__(self):
        self.models = {
            "regression": {
                "linear_regression": LinearRegression(),
                "random_forest": RandomForestRegressor()
            },
            "classification": {
                "logistic_regression": LogisticRegression(),
                "random_forest": RandomForestClassifier()
            },
            "clustering": {
                "kmeans": KMeans()
            }
        }
        
    def train(self, data: pd.DataFrame, model_type: str, model_name: str, target_column: str, test_size: float = 0.2) -> dict:
        """Trains a machine learning model.
        
        Args:
            data: Input data
            model_type: Type of model (regression, classification, clustering)
            model_name: Name of the model
            target_column: Target column name
            test_size: Test set size ratio
            
        Returns:
            Dictionary containing model results
        """
        try:
            # Data preparation
            X = data.drop(columns=[target_column])
            y = data[target_column]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42
            )
            
            # Scale features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # Get model
            model = self.models[model_type][model_name]
            
            # Train model
            model.fit(X_train_scaled, y_train)
            
            # Make predictions
            y_pred = model.predict(X_test_scaled)
            
            # Calculate metrics
            metrics = self._calculate_metrics(y_test, y_pred, model_type)
            
            # Save model
            model_path = self._save_model(model, model_type, model_name)
            
            return {
                "model": model,
                "metrics": metrics,
                "model_path": model_path,
                "feature_importance": self._get_feature_importance(model, X.columns) if hasattr(model, "feature_importances_") else None
            }
            
        except Exception as e:
            st.error(f"Model training error: {str(e)}")
            return None
            
    def _calculate_metrics(self, y_true: np.ndarray, y_pred: np.ndarray, model_type: str) -> dict:
        """Calculates model evaluation metrics.
        
        Args:
            y_true: True values
            y_pred: Predicted values
            model_type: Type of model
            
        Returns:
            Dictionary containing metrics
        """
        metrics = {}
        
        if model_type == "regression":
            metrics["mse"] = mean_squared_error(y_true, y_pred)
            metrics["r2"] = r2_score(y_true, y_pred)
            
        elif model_type == "classification":
            metrics["accuracy"] = accuracy_score(y_true, y_pred)
            
        elif model_type == "clustering":
            metrics["silhouette"] = silhouette_score(y_true, y_pred)
            
        return metrics
        
    def _save_model(self, model: object, model_type: str, model_name: str) -> str:
        """Saves the trained model.
        
        Args:
            model: Trained model
            model_type: Type of model
            model_name: Name of the model
            
        Returns:
            Path to saved model
        """
        # Create models directory if it doesn't exist
        os.makedirs("models", exist_ok=True)
        
        # Save model
        model_path = f"models/{model_type}_{model_name}.pkl"
        joblib.dump(model, model_path)
        
        return model_path
        
    def _get_feature_importance(self, model: object, feature_names: list) -> pd.DataFrame:
        """Gets feature importance scores.
        
        Args:
            model: Trained model
            feature_names: List of feature names
            
        Returns:
            DataFrame containing feature importance scores
        """
        importance = model.feature_importances_
        return pd.DataFrame({
            "feature": feature_names,
            "importance": importance
        }).sort_values("importance", ascending=False) 