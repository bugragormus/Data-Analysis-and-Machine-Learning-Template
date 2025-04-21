"""
Template Application

This template provides a basic structure for data analysis, machine learning,
and artificial intelligence applications.

Modules:
    - data_loader: Data loading and validation
    - data_processor: Data processing and transformation
    - data_analyzer: Data analysis and visualization
    - ml_model: Machine learning model
    - ai_processor: Artificial intelligence processing
    - report_generator: Report generation
    - error_handler: Error management

Usage:
    streamlit run src/main.py
"""

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from utils.data_loader import DataLoader
from utils.data_processor import DataProcessor
from utils.data_analyzer import DataAnalyzer
from utils.ml_model import MLModel
from utils.ai_processor import AIProcessor
from utils.report_generator import ReportGenerator
from utils.error_handler import ErrorHandler
from config.settings import Settings


class TemplateApp:
    def __init__(self):
        self.settings = Settings()
        self.error_handler = ErrorHandler()
        self.setup_page()
        
    def setup_page(self):
        """Configures page settings."""
        st.set_page_config(
            layout="wide",
            page_title="Template Application",
            page_icon="📊",
            initial_sidebar_state="expanded"
        )
        
    def setup_sidebar(self):
        """Configures sidebar settings."""
        with st.sidebar:
            st.header("🔧 Settings")
            
            # Data loading options
            data_source = st.radio(
                "Data Source",
                ["File Upload", "Sample Data", "API"]
            )
            
            # Model settings
            model_type = st.selectbox(
                "Model Type",
                ["Regression", "Classification", "Clustering"]
            )
            
            # Analysis settings
            analysis_type = st.multiselect(
                "Analysis Types",
                ["Basic Statistics", "Correlation", "Trend Analysis", "Anomaly Detection"]
            )
            
        return {
            "data_source": data_source,
            "model_type": model_type,
            "analysis_type": analysis_type
        }
        
    def load_data(self, data_source):
        """Performs data loading operations."""
        data_loader = DataLoader()
        
        if data_source == "File Upload":
            uploaded_file = st.file_uploader(
                "Upload data file",
                type=["csv", "xlsx", "json"]
            )
            if uploaded_file:
                return data_loader.load_from_file(uploaded_file)
                
        elif data_source == "Sample Data":
            return data_loader.load_sample_data()
            
        elif data_source == "API":
            api_url = st.text_input("API URL")
            if api_url:
                return data_loader.load_from_api(api_url)
                
        return None
        
    def process_data(self, data):
        """Performs data processing operations."""
        if data is None:
            return None
            
        processor = DataProcessor()
        return processor.process(data)
        
    def analyze_data(self, data, analysis_types):
        """Performs data analysis operations."""
        if data is None:
            return
            
        analyzer = DataAnalyzer()
        
        for analysis_type in analysis_types:
            if analysis_type == "Basic Statistics":
                analyzer.show_basic_statistics(data)
            elif analysis_type == "Correlation":
                analyzer.show_correlation(data)
            elif analysis_type == "Trend Analysis":
                analyzer.show_trend_analysis(data)
            elif analysis_type == "Anomaly Detection":
                analyzer.show_anomaly_detection(data)
                
    def train_model(self, data, model_type):
        """Performs model training."""
        if data is None:
            return None
            
        model = MLModel()
        return model.train(data, model_type)
        
    def generate_insights(self, data, model):
        """Generates insights using artificial intelligence."""
        if data is None or model is None:
            return
            
        ai_processor = AIProcessor()
        return ai_processor.generate_insights(data, model)
        
    def generate_report(self, data, analysis_results, model_results, insights):
        """Generates report."""
        if data is None:
            return
            
        report_generator = ReportGenerator()
        return report_generator.generate(
            data=data,
            analysis_results=analysis_results,
            model_results=model_results,
            insights=insights
        )
        
    def run(self):
        """Runs the application."""
        try:
            st.title("📊 Template Application")
            
            # Get sidebar settings
            settings = self.setup_sidebar()
            
            # Load data
            data = self.load_data(settings["data_source"])
            
            if data is not None:
                # Process data
                processed_data = self.process_data(data)
                
                # Analyze data
                self.analyze_data(processed_data, settings["analysis_type"])
                
                # Train model
                model = self.train_model(processed_data, settings["model_type"])
                
                # Generate insights
                insights = self.generate_insights(processed_data, model)
                
                # Generate report
                report = self.generate_report(
                    processed_data,
                    settings["analysis_type"],
                    model,
                    insights
                )
                
        except Exception as e:
            self.error_handler.handle_error(e)


if __name__ == "__main__":
    app = TemplateApp()
    app.run() 