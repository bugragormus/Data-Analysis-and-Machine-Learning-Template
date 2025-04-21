"""
Data Processing Module

This module performs data preprocessing and transformation operations.
"""

import pandas as pd
import numpy as np
from typing import Optional
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif


class DataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.imputer = SimpleImputer(strategy="mean")
        self.feature_selector = SelectKBest(score_func=f_classif, k=10)
        
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Performs data preprocessing operations.
        
        Args:
            data: Data frame to process
            
        Returns:
            pd.DataFrame: Processed data frame
        """
        try:
            # Create data copy
            processed_data = data.copy()
            
            # Handle missing values
            processed_data = self._handle_missing_values(processed_data)
            
            # Handle outliers
            processed_data = self._handle_outliers(processed_data)
            
            # Scale features
            processed_data = self._scale_features(processed_data)
            
            # Select features
            processed_data = self._select_features(processed_data)
            
            return processed_data
            
        except Exception as e:
            print(f"Data processing error: {str(e)}")
            return data
            
    def _handle_missing_values(self, data: pd.DataFrame) -> pd.DataFrame:
        """Handles missing values."""
        # Fill missing values for numeric columns
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        data[numeric_cols] = self.imputer.fit_transform(data[numeric_cols])
        
        # Fill missing values for categorical columns
        categorical_cols = data.select_dtypes(include=["object"]).columns
        data[categorical_cols] = data[categorical_cols].fillna("Unknown")
        
        return data
        
    def _handle_outliers(self, data: pd.DataFrame) -> pd.DataFrame:
        """Handles outliers."""
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            # Detect outliers using IQR method
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Replace outliers with bounds
            data[col] = np.where(
                data[col] < lower_bound,
                lower_bound,
                np.where(data[col] > upper_bound, upper_bound, data[col])
            )
            
        return data
        
    def _scale_features(self, data: pd.DataFrame) -> pd.DataFrame:
        """Scales features."""
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        
        # Separate target variable
        if "target" in data.columns:
            target = data["target"]
            data = data.drop("target", axis=1)
            
            # Scale numeric columns
            data[numeric_cols] = self.scaler.fit_transform(data[numeric_cols])
            
            # Add target variable back
            data["target"] = target
        else:
            data[numeric_cols] = self.scaler.fit_transform(data[numeric_cols])
            
        return data
        
    def _select_features(self, data: pd.DataFrame) -> pd.DataFrame:
        """Performs feature selection."""
        if "target" in data.columns:
            # Separate target variable
            target = data["target"]
            features = data.drop("target", axis=1)
            
            # Perform feature selection
            selected_features = self.feature_selector.fit_transform(features, target)
            selected_indices = self.feature_selector.get_support(indices=True)
            
            # Combine selected features and target variable
            selected_data = pd.DataFrame(
                selected_features,
                columns=features.columns[selected_indices]
            )
            selected_data["target"] = target
            
            return selected_data
            
        return data 