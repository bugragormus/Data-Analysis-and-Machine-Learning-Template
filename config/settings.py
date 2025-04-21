"""
Settings Module

This module contains settings used throughout the application.
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        # Load .env file
        load_dotenv()
        
        # Application settings
        self.app_settings = {
            "APP_NAME": "Template Application",
            "APP_VERSION": "1.0.0",
            "APP_DESCRIPTION": "Data analysis, machine learning and AI application",
            "APP_AUTHOR": "Your Name",
            "APP_EMAIL": "your.email@example.com",
        }
        
        # Data settings
        self.data_settings = {
            "DEFAULT_DATA_PATH": "data",
            "SUPPORTED_FILE_TYPES": [".csv", ".xlsx", ".json"],
            "MAX_FILE_SIZE": 100 * 1024 * 1024,  # 100 MB
            "DEFAULT_ENCODING": "utf-8",
        }
        
        # Model settings
        self.model_settings = {
            "DEFAULT_MODEL_PATH": "models",
            "SUPPORTED_MODEL_TYPES": ["Regression", "Classification", "Clustering"],
            "DEFAULT_TEST_SIZE": 0.2,
            "DEFAULT_RANDOM_STATE": 42,
        }
        
        # Analysis settings
        self.analysis_settings = {
            "SUPPORTED_ANALYSIS_TYPES": [
                "Basic Statistics",
                "Correlation",
                "Trend Analysis",
                "Anomaly Detection",
            ],
            "DEFAULT_CONFIDENCE_LEVEL": 0.95,
            "DEFAULT_SIGNIFICANCE_LEVEL": 0.05,
        }
        
        # Visualization settings
        self.visualization_settings = {
            "DEFAULT_THEME": "plotly",
            "DEFAULT_COLOR_SCHEME": "viridis",
            "DEFAULT_FIGURE_SIZE": (800, 600),
            "DEFAULT_FONT_SIZE": 12,
        }
        
        # Report settings
        self.report_settings = {
            "DEFAULT_REPORT_PATH": "reports",
            "REPORT_TEMPLATE": "default_template.html",
            "DEFAULT_REPORT_FORMAT": "pdf",
            "SUPPORTED_REPORT_FORMATS": ["pdf", "html", "csv"],
        }
        
        # API settings
        self.api_settings = {
            "DEFAULT_API_TIMEOUT": 30,  # seconds
            "DEFAULT_API_RETRIES": 3,
            "DEFAULT_API_BACKOFF": 1,  # seconds
        }
        
        # Logging settings
        self.logging_settings = {
            "LOG_LEVEL": "ERROR",
            "LOG_FORMAT": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "LOG_FILE": "app_errors.log",
            "MAX_LOG_SIZE": 10 * 1024 * 1024,  # 10 MB
            "BACKUP_COUNT": 5,
        }
        
    def get_setting(self, category: str, key: str) -> Any:
        """
        Returns the specified setting.
        
        Args:
            category: Settings category
            key: Setting key
            
        Returns:
            Any: Setting value
        """
        settings_dict = getattr(self, f"{category}_settings", None)
        if settings_dict is None:
            raise ValueError(f"Invalid settings category: {category}")
            
        return settings_dict.get(key)
        
    def update_setting(self, category: str, key: str, value: Any):
        """
        Updates the specified setting.
        
        Args:
            category: Settings category
            key: Setting key
            value: New setting value
        """
        settings_dict = getattr(self, f"{category}_settings", None)
        if settings_dict is None:
            raise ValueError(f"Invalid settings category: {category}")
            
        settings_dict[key] = value
        
    def get_all_settings(self) -> Dict[str, Dict[str, Any]]:
        """
        Returns all settings.
        
        Returns:
            Dict[str, Dict[str, Any]]: All settings
        """
        return {
            "app": self.app_settings,
            "data": self.data_settings,
            "model": self.model_settings,
            "analysis": self.analysis_settings,
            "visualization": self.visualization_settings,
            "report": self.report_settings,
            "api": self.api_settings,
            "logging": self.logging_settings,
        }
        
    def load_environment_variables(self):
        """Loads environment variables."""
        for category in self.get_all_settings().keys():
            settings_dict = getattr(self, f"{category}_settings")
            for key in settings_dict.keys():
                env_value = os.getenv(f"{category.upper()}_{key}")
                if env_value is not None:
                    # Preserve value type
                    if isinstance(settings_dict[key], bool):
                        settings_dict[key] = env_value.lower() == "true"
                    elif isinstance(settings_dict[key], int):
                        settings_dict[key] = int(env_value)
                    elif isinstance(settings_dict[key], float):
                        settings_dict[key] = float(env_value)
                    else:
                        settings_dict[key] = env_value 