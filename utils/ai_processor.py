"""
AI Processing Module

This module performs data analysis and insight generation using artificial intelligence.
"""

import streamlit as st
import pandas as pd
import numpy as np
from typing import Optional, Dict, Any
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import DBSCAN
from sklearn.ensemble import IsolationForest
import plotly.express as px
import plotly.graph_objects as go


class AIProcessor:
    def __init__(self):
        self.pca = PCA(n_components=2)
        self.tsne = TSNE(n_components=2, random_state=42)
        self.dbscan = DBSCAN(eps=0.5, min_samples=5)
        self.isolation_forest = IsolationForest(contamination=0.1, random_state=42)
        
    def generate_insights(self, data: pd.DataFrame, model: Any) -> Optional[Dict[str, Any]]:
        """
        Generates insights using artificial intelligence.
        
        Args:
            data: Data to analyze
            model: Trained model
            
        Returns:
            Optional[Dict[str, Any]]: Generated insights
        """
        try:
            insights = {}
            
            # Dimensionality reduction
            insights["pca"] = self._apply_pca(data)
            insights["tsne"] = self._apply_tsne(data)
            
            # Clustering
            insights["clusters"] = self._apply_clustering(data)
            
            # Anomaly detection
            insights["anomalies"] = self._detect_anomalies(data)
            
            # Feature importance
            if hasattr(model, "feature_importances_"):
                insights["feature_importance"] = self._analyze_feature_importance(
                    data, model
                )
                
            # Show insights
            self._show_insights(insights, data)
            
            return insights
            
        except Exception as e:
            st.error(f"Error occurred while generating insights: {str(e)}")
            return None
            
    def _apply_pca(self, data: pd.DataFrame) -> np.ndarray:
        """Performs dimensionality reduction using PCA."""
        numeric_data = data.select_dtypes(include=[np.number])
        return self.pca.fit_transform(numeric_data)
        
    def _apply_tsne(self, data: pd.DataFrame) -> np.ndarray:
        """Performs dimensionality reduction using t-SNE."""
        numeric_data = data.select_dtypes(include=[np.number])
        return self.tsne.fit_transform(numeric_data)
        
    def _apply_clustering(self, data: pd.DataFrame) -> np.ndarray:
        """Performs clustering using DBSCAN."""
        numeric_data = data.select_dtypes(include=[np.number])
        return self.dbscan.fit_predict(numeric_data)
        
    def _detect_anomalies(self, data: pd.DataFrame) -> np.ndarray:
        """Performs anomaly detection using Isolation Forest."""
        numeric_data = data.select_dtypes(include=[np.number])
        return self.isolation_forest.fit_predict(numeric_data)
        
    def _analyze_feature_importance(
        self, data: pd.DataFrame, model: Any
    ) -> Dict[str, float]:
        """Analyzes feature importance."""
        feature_importance = dict(
            zip(data.columns, model.feature_importances_)
        )
        return dict(
            sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)
        )
        
    def _show_insights(self, insights: Dict[str, Any], data: pd.DataFrame):
        """Visualizes insights."""
        st.subheader("🤖 AI Insights")
        
        # PCA results
        if "pca" in insights:
            st.write("PCA Results:")
            pca_df = pd.DataFrame(
                insights["pca"],
                columns=["PC1", "PC2"],
            )
            fig = px.scatter(
                pca_df,
                x="PC1",
                y="PC2",
                title="PCA Results",
            )
            st.plotly_chart(fig)
            
        # t-SNE results
        if "tsne" in insights:
            st.write("t-SNE Results:")
            tsne_df = pd.DataFrame(
                insights["tsne"],
                columns=["t-SNE1", "t-SNE2"],
            )
            fig = px.scatter(
                tsne_df,
                x="t-SNE1",
                y="t-SNE2",
                title="t-SNE Results",
            )
            st.plotly_chart(fig)
            
        # Clustering results
        if "clusters" in insights:
            st.write("Clustering Results:")
            clusters = insights["clusters"]
            fig = px.scatter(
                data,
                x=data.columns[0],
                y=data.columns[1],
                color=clusters,
                title="DBSCAN Clustering",
            )
            st.plotly_chart(fig)
            
        # Anomaly results
        if "anomalies" in insights:
            st.write("Anomaly Detection:")
            anomalies = insights["anomalies"]
            fig = px.scatter(
                data,
                x=data.columns[0],
                y=data.columns[1],
                color=anomalies,
                title="Anomaly Detection",
            )
            st.plotly_chart(fig)
            
        # Feature importance
        if "feature_importance" in insights:
            st.write("Feature Importance:")
            importance = insights["feature_importance"]
            fig = px.bar(
                x=list(importance.keys()),
                y=list(importance.values()),
                title="Feature Importance",
            )
            st.plotly_chart(fig) 