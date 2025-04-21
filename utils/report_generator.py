"""
Report Generation Module

This module generates analysis results as PDF reports.
"""

import streamlit as st
import pandas as pd
import numpy as np
from typing import Optional, Dict, Any
from fpdf import FPDF
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from datetime import datetime


class ReportGenerator:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        
    def generate(
        self,
        data: pd.DataFrame,
        analysis_results: Dict[str, Any],
        model_results: Dict[str, Any],
        insights: Dict[str, Any],
    ) -> Optional[bytes]:
        """
        Generates PDF report.
        
        Args:
            data: Analyzed data
            analysis_results: Analysis results
            model_results: Model results
            insights: AI insights
            
        Returns:
            Optional[bytes]: PDF report
        """
        try:
            # Report title
            self._add_title("Data Analysis Report")
            
            # Date and time
            self._add_text(f"Creation Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Data summary
            self._add_section("Data Summary")
            self._add_data_summary(data)
            
            # Analysis results
            self._add_section("Analysis Results")
            self._add_analysis_results(analysis_results)
            
            # Model results
            self._add_section("Model Results")
            self._add_model_results(model_results)
            
            # AI insights
            self._add_section("AI Insights")
            self._add_insights(insights)
            
            # Save report
            return self.pdf.output(dest="S").encode("latin1")
            
        except Exception as e:
            st.error(f"Error occurred while generating report: {str(e)}")
            return None
            
    def _add_title(self, title: str):
        """Adds report title."""
        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, title, ln=True, align="C")
        self.pdf.ln(10)
        
    def _add_section(self, section_title: str):
        """Adds section title."""
        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(0, 10, section_title, ln=True)
        self.pdf.ln(5)
        
    def _add_text(self, text: str):
        """Adds text."""
        self.pdf.set_font("Arial", "", 10)
        self.pdf.multi_cell(0, 5, text)
        self.pdf.ln(5)
        
    def _add_data_summary(self, data: pd.DataFrame):
        """Adds data summary."""
        # Data size
        self._add_text(f"Data Size: {data.shape[0]} rows, {data.shape[1]} columns")
        
        # Column types
        self._add_text("Column Types:")
        for col, dtype in data.dtypes.items():
            self._add_text(f"- {col}: {dtype}")
            
        # Missing values
        missing_values = data.isnull().sum()
        self._add_text("Missing Values:")
        for col, count in missing_values.items():
            if count > 0:
                self._add_text(f"- {col}: {count} missing values")
                
    def _add_analysis_results(self, analysis_results: Dict[str, Any]):
        """Adds analysis results."""
        for analysis_type, results in analysis_results.items():
            self._add_text(f"{analysis_type} Results:")
            
            if isinstance(results, dict):
                for key, value in results.items():
                    self._add_text(f"- {key}: {value}")
            else:
                self._add_text(str(results))
                
    def _add_model_results(self, model_results: Dict[str, Any]):
        """Adds model results."""
        if "metrics" in model_results:
            self._add_text("Model Metrics:")
            for metric, value in model_results["metrics"].items():
                self._add_text(f"- {metric}: {value:.4f}")
                
        if "feature_importance" in model_results:
            self._add_text("Feature Importance:")
            for feature, importance in model_results["feature_importance"].items():
                self._add_text(f"- {feature}: {importance:.4f}")
                
    def _add_insights(self, insights: Dict[str, Any]):
        """Adds AI insights."""
        for insight_type, results in insights.items():
            self._add_text(f"{insight_type} Insights:")
            
            if isinstance(results, dict):
                for key, value in results.items():
                    self._add_text(f"- {key}: {value}")
            else:
                self._add_text(str(results))
                
    def _add_plot(self, fig: plt.Figure):
        """Adds plot."""
        # Save plot to temporary file
        buffer = BytesIO()
        fig.savefig(buffer, format="png")
        buffer.seek(0)
        
        # Add plot to PDF
        self.pdf.image(buffer, x=10, w=190)
        self.pdf.ln(10)
        
    def _add_table(self, df: pd.DataFrame):
        """Adds table."""
        # Table headers
        self.pdf.set_font("Arial", "B", 10)
        for col in df.columns:
            self.pdf.cell(40, 10, str(col), border=1)
        self.pdf.ln()
        
        # Table data
        self.pdf.set_font("Arial", "", 10)
        for _, row in df.iterrows():
            for col in df.columns:
                self.pdf.cell(40, 10, str(row[col]), border=1)
            self.pdf.ln()
            
        self.pdf.ln(10) 