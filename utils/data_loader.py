"""
Data Loading Module

This module performs data loading operations from different sources.
"""

import pandas as pd
import numpy as np
from typing import Union, Optional
import requests
from io import BytesIO
import json


class DataLoader:
    def __init__(self):
        self.supported_formats = {
            "csv": self._load_csv,
            "xlsx": self._load_excel,
            "json": self._load_json
        }
        
    def load_from_file(self, file) -> Optional[pd.DataFrame]:
        """
        Loads data from a file.
        
        Args:
            file: File to load
            
        Returns:
            Optional[pd.DataFrame]: Loaded data frame
        """
        try:
            file_extension = file.name.split(".")[-1].lower()
            
            if file_extension in self.supported_formats:
                return self.supported_formats[file_extension](file)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
                
        except Exception as e:
            print(f"Data loading error: {str(e)}")
            return None
            
    def load_from_api(self, url: str) -> Optional[pd.DataFrame]:
        """
        Loads data from an API.
        
        Args:
            url: API URL
            
        Returns:
            Optional[pd.DataFrame]: Loaded data frame
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            data = response.json()
            return pd.DataFrame(data)
            
        except Exception as e:
            print(f"API data loading error: {str(e)}")
            return None
            
    def load_sample_data(self) -> pd.DataFrame:
        """
        Loads sample data.
        
        Returns:
            pd.DataFrame: Sample data frame
        """
        # Create sample data
        np.random.seed(42)
        n_samples = 1000
        
        data = {
            "feature1": np.random.normal(0, 1, n_samples),
            "feature2": np.random.normal(5, 2, n_samples),
            "feature3": np.random.randint(0, 10, n_samples),
            "target": np.random.choice([0, 1], n_samples)
        }
        
        return pd.DataFrame(data)
        
    def _load_csv(self, file) -> pd.DataFrame:
        """Loads data from CSV file."""
        return pd.read_csv(file)
        
    def _load_excel(self, file) -> pd.DataFrame:
        """Loads data from Excel file."""
        return pd.read_excel(file)
        
    def _load_json(self, file) -> pd.DataFrame:
        """Loads data from JSON file."""
        return pd.read_json(file) 