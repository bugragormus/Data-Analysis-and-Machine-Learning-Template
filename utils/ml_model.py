"""
Machine learning model module.

This module performs machine learning model training and evaluation operations.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_squared_error,
    r2_score,
    silhouette_score,
)
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.cluster import KMeans
import plotly.express as px
import plotly.graph_objects as go
from typing import Optional, Dict, Any


class MLModel:
    def __init__(self):
        self.models = {
            "Regression": {
                "Linear Regression": LinearRegression(),
                "Random Forest": RandomForestRegressor(random_state=42),
            },
            "Classification": {
                "Logistic Regression": LogisticRegression(random_state=42),
                "Random Forest": RandomForestClassifier(random_state=42),
            },
            "Clustering": {
                "K-Means": KMeans(n_clusters=3, random_state=42),
            },
        }
        
    def train(self, data: pd.DataFrame, model_type: str) -> Optional[Dict[str, Any]]:
        """
        Performs model training.
        
        Args:
            data: Training data
            model_type: Model type
            
        Returns:
            Optional[Dict[str, Any]]: Trained model and metrics
        """
        try:
            if model_type not in self.models:
                raise ValueError(f"Unsupported model type: {model_type}")
                
            # Model selection
            model_name = st.selectbox(
                "Select Model",
                list(self.models[model_type].keys())
            )
            model = self.models[model_type][model_name]
            
            # Data preparation
            if model_type in ["Regression", "Classification"]:
                if "target" not in data.columns:
                    st.error("Target variable not found!")
                    return None
                    
                X = data.drop("target", axis=1)
                y = data["target"]
                
                # Data splitting
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.2, random_state=42
                )
                
                # Model training
                model.fit(X_train, y_train)
                
                # Prediction
                y_pred = model.predict(X_test)
                
                # Metrics
                metrics = self._calculate_metrics(y_test, y_pred, model_type)
                
                # Show results
                self._show_results(model, metrics, X_test, y_test, y_pred, model_type)
                
                return {
                    "model": model,
                    "metrics": metrics,
                    "X_test": X_test,
                    "y_test": y_test,
                    "y_pred": y_pred,
                }
                
            elif model_type == "Clustering":
                # Data preparation for clustering
                X = data.select_dtypes(include=[np.number])
                
                # Model training
                model.fit(X)
                
                # Prediction
                clusters = model.predict(X)
                
                # Metrics
                silhouette = silhouette_score(X, clusters)
                
                # Show results
                self._show_clustering_results(model, X, clusters, silhouette)
                
                return {
                    "model": model,
                    "clusters": clusters,
                    "silhouette_score": silhouette,
                }
                
        except Exception as e:
            st.error(f"Error occurred during model training: {str(e)}")
            return None
            
    def _calculate_metrics(
        self, y_true: np.ndarray, y_pred: np.ndarray, model_type: str
    ) -> Dict[str, float]:
        """Calculates model metrics."""
        metrics = {}
        
        if model_type == "Regression":
            metrics["MSE"] = mean_squared_error(y_true, y_pred)
            metrics["R2"] = r2_score(y_true, y_pred)
            
        elif model_type == "Classification":
            metrics["Accuracy"] = accuracy_score(y_true, y_pred)
            metrics["Precision"] = precision_score(y_true, y_pred, average="weighted")
            metrics["Recall"] = recall_score(y_true, y_pred, average="weighted")
            metrics["F1"] = f1_score(y_true, y_pred, average="weighted")
            
        return metrics
        
    def _show_results(
        self,
        model: Any,
        metrics: Dict[str, float],
        X_test: pd.DataFrame,
        y_test: np.ndarray,
        y_pred: np.ndarray,
        model_type: str,
    ):
        """Shows model results."""
        st.subheader("📊 Model Results")
        
        # Show metrics
        st.write("Model Metrics:")
        for metric_name, value in metrics.items():
            st.write(f"{metric_name}: {value:.4f}")
            
        # Actual vs Prediction graph
        if model_type == "Regression":
            fig = px.scatter(
                x=y_test,
                y=y_pred,
                labels={"x": "Actual Values", "y": "Predictions"},
                title="Actual vs Prediction",
            )
            fig.add_trace(
                go.Scatter(
                    x=[min(y_test), max(y_test)],
                    y=[min(y_test), max(y_test)],
                    mode="lines",
                    name="Ideal",
                )
            )
            st.plotly_chart(fig)
            
        elif model_type == "Classification":
            # Confusion matrix
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(y_test, y_pred)
            
            fig = px.imshow(
                cm,
                labels=dict(x="Prediction", y="Actual"),
                title="Confusion Matrix",
            )
            st.plotly_chart(fig)
            
    def _show_clustering_results(
        self, model: Any, X: pd.DataFrame, clusters: np.ndarray, silhouette: float
    ):
        """Shows clustering results."""
        st.subheader("📊 Clustering Results")
        
        # Silhouette score
        st.write(f"Silhouette Score: {silhouette:.4f}")
        
        # Visualize clusters
        if X.shape[1] >= 2:
            fig = px.scatter(
                X,
                x=X.columns[0],
                y=X.columns[1],
                color=clusters,
                title="Clustering Results",
            )
            st.plotly_chart(fig)
            
        # Show cluster centers
        if hasattr(model, "cluster_centers_"):
            st.write("Cluster Centers:")
            centers = pd.DataFrame(
                model.cluster_centers_,
                columns=X.columns[: model.cluster_centers_.shape[1]],
            )
            st.write(centers) 