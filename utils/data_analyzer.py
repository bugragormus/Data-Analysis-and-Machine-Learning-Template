"""
Data Analysis Module

This module performs data analysis and visualization operations.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import IsolationForest
from typing import Optional


class DataAnalyzer:
    def __init__(self):
        plt.style.use("seaborn")
        sns.set_palette("viridis")
        
    def show_basic_statistics(self, data: pd.DataFrame):
        """Shows basic statistics."""
        st.subheader("📊 Basic Statistics")
        
        # Statistics for numeric columns
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            st.write("Numeric Variables Statistics:")
            st.write(data[numeric_cols].describe())
            
        # Statistics for categorical columns
        categorical_cols = data.select_dtypes(include=["object"]).columns
        if len(categorical_cols) > 0:
            st.write("Categorical Variables Statistics:")
            for col in categorical_cols:
                st.write(f"{col} Value Counts:")
                st.write(data[col].value_counts())
                
    def show_correlation(self, data: pd.DataFrame):
        """Shows correlation analysis."""
        st.subheader("🔗 Correlation Analysis")
        
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 1:
            # Correlation matrix
            corr_matrix = data[numeric_cols].corr()
            
            # Heatmap
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
            
            # Correlation pairs
            st.write("Highest Correlation Pairs:")
            corr_pairs = corr_matrix.unstack().sort_values(ascending=False)
            corr_pairs = corr_pairs[corr_pairs < 1.0]  # Remove 1.0 values
            st.write(corr_pairs.head(10))
            
    def show_trend_analysis(self, data: pd.DataFrame):
        """Shows trend analysis."""
        st.subheader("📈 Trend Analysis")
        
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            # If time series data exists
            if "date" in data.columns or "timestamp" in data.columns:
                time_col = "date" if "date" in data.columns else "timestamp"
                
                for col in numeric_cols:
                    if col != time_col:
                        fig = px.line(
                            data,
                            x=time_col,
                            y=col,
                            title=f"{col} Trend"
                        )
                        st.plotly_chart(fig)
                        
            # If no time series
            else:
                for col in numeric_cols:
                    fig = px.histogram(
                        data,
                        x=col,
                        title=f"{col} Distribution"
                    )
                    st.plotly_chart(fig)
                    
    def show_anomaly_detection(self, data: pd.DataFrame):
        """Shows anomaly detection."""
        st.subheader("⚠️ Anomaly Detection")
        
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            # Anomaly detection using Isolation Forest
            clf = IsolationForest(contamination=0.1, random_state=42)
            anomalies = clf.fit_predict(data[numeric_cols])
            
            # Add anomaly results to data
            data["is_anomaly"] = anomalies
            
            # Show anomalies
            st.write("Detected Anomalies:")
            st.write(data[data["is_anomaly"] == -1])
            
            # Visualize anomaly distribution
            fig = px.scatter(
                data,
                x=numeric_cols[0],
                y=numeric_cols[1] if len(numeric_cols) > 1 else numeric_cols[0],
                color="is_anomaly",
                title="Anomaly Distribution"
            )
            st.plotly_chart(fig)
            
    def show_distribution(self, data: pd.DataFrame, column: str):
        """Shows variable distribution."""
        st.subheader(f"📊 {column} Distribution")
        
        if column in data.columns:
            if data[column].dtype in [np.int64, np.float64]:
                # Histogram for numeric variable
                fig = px.histogram(
                    data,
                    x=column,
                    title=f"{column} Distribution"
                )
                st.plotly_chart(fig)
                
            else:
                # Bar plot for categorical variable
                fig = px.bar(
                    data[column].value_counts(),
                    title=f"{column} Value Counts"
                )
                st.plotly_chart(fig)
                
    def show_pairplot(self, data: pd.DataFrame):
        """Shows relationships between variables."""
        st.subheader("🔗 Variable Relationships")
        
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 1:
            fig = px.scatter_matrix(
                data[numeric_cols],
                title="Variable Relationships"
            )
            st.plotly_chart(fig)
            
    def show_boxplot(self, data: pd.DataFrame, column: str):
        """Shows box plot."""
        st.subheader(f"📦 {column} Box Plot")
        
        if column in data.columns and data[column].dtype in [np.int64, np.float64]:
            fig = px.box(
                data,
                y=column,
                title=f"{column} Box Plot"
            )
            st.plotly_chart(fig) 