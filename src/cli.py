"""
Template CLI Interface

This module provides the command line interface for the template.
"""

import argparse
import sys
from pathlib import Path
import pandas as pd
import json
from typing import Optional

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


class TemplateCLI:
    def __init__(self):
        self.settings = Settings()
        self.error_handler = ErrorHandler()
        self.setup_parser()
        
    def setup_parser(self):
        """Sets up the argument parser."""
        self.parser = argparse.ArgumentParser(
            description="Template CLI - Data Analysis and Machine Learning Tool"
        )
        
        # Main commands
        subparsers = self.parser.add_subparsers(dest="command", help="Commands")
        
        # Data loading command
        load_parser = subparsers.add_parser("load", help="Load data")
        load_parser.add_argument("--file", help="Data file path")
        load_parser.add_argument("--api", help="API URL")
        load_parser.add_argument("--sample", action="store_true", help="Use sample data")
        load_parser.add_argument("--output", help="Output file path")
        
        # Data analysis command
        analyze_parser = subparsers.add_parser("analyze", help="Analyze data")
        analyze_parser.add_argument("--input", required=True, help="Input file path")
        analyze_parser.add_argument("--type", choices=["stats", "corr", "trend", "anomaly"], required=True, help="Analysis type")
        analyze_parser.add_argument("--output", help="Output file path")
        
        # Model training command
        train_parser = subparsers.add_parser("train", help="Train model")
        train_parser.add_argument("--input", required=True, help="Input file path")
        train_parser.add_argument("--type", choices=["regression", "classification", "clustering"], required=True, help="Model type")
        train_parser.add_argument("--model", required=True, help="Model name")
        train_parser.add_argument("--output", help="Model save path")
        
        # Insight generation command
        insight_parser = subparsers.add_parser("insight", help="Generate insights")
        insight_parser.add_argument("--input", required=True, help="Input file path")
        insight_parser.add_argument("--type", choices=["pca", "tsne", "feature"], required=True, help="Insight type")
        insight_parser.add_argument("--output", help="Output file path")
        
        # Report generation command
        report_parser = subparsers.add_parser("report", help="Generate report")
        report_parser.add_argument("--input", required=True, help="Input file path")
        report_parser.add_argument("--type", choices=["pdf", "html", "csv"], required=True, help="Report type")
        report_parser.add_argument("--output", help="Output file path")
        
    def load_data(self, args) -> Optional[pd.DataFrame]:
        """Performs data loading operation."""
        data_loader = DataLoader()
        
        if args.file:
            return data_loader.load_from_file(args.file)
        elif args.api:
            return data_loader.load_from_api(args.api)
        elif args.sample:
            return data_loader.load_sample_data()
            
        return None
        
    def analyze_data(self, data: pd.DataFrame, analysis_type: str) -> dict:
        """Performs data analysis operation."""
        analyzer = DataAnalyzer()
        
        if analysis_type == "stats":
            return analyzer.show_basic_statistics(data)
        elif analysis_type == "corr":
            return analyzer.show_correlation(data)
        elif analysis_type == "trend":
            return analyzer.show_trend_analysis(data)
        elif analysis_type == "anomaly":
            return analyzer.show_anomaly_detection(data)
            
        return {}
        
    def train_model(self, data: pd.DataFrame, model_type: str, model_name: str) -> dict:
        """Performs model training."""
        model = MLModel()
        return model.train(data, model_type, model_name)
        
    def generate_insights(self, data: pd.DataFrame, insight_type: str) -> dict:
        """Generates insights."""
        ai_processor = AIProcessor()
        return ai_processor.generate_insights(data, insight_type)
        
    def generate_report(self, data: pd.DataFrame, report_type: str) -> bytes:
        """Generates report."""
        report_generator = ReportGenerator()
        return report_generator.generate(data, report_type)
        
    def save_output(self, data: any, output_path: str, output_type: str):
        """Saves the output."""
        if output_type == "json":
            with open(output_path, "w") as f:
                json.dump(data, f, indent=4)
        elif output_type == "csv":
            data.to_csv(output_path, index=False)
        elif output_type == "pdf":
            with open(output_path, "wb") as f:
                f.write(data)
                
    def run(self):
        """Runs the CLI."""
        args = self.parser.parse_args()
        
        try:
            if args.command == "load":
                data = self.load_data(args)
                if data is not None and args.output:
                    self.save_output(data, args.output, "csv")
                    
            elif args.command == "analyze":
                data = pd.read_csv(args.input)
                results = self.analyze_data(data, args.type)
                if args.output:
                    self.save_output(results, args.output, "json")
                    
            elif args.command == "train":
                data = pd.read_csv(args.input)
                model = self.train_model(data, args.type, args.model)
                if args.output:
                    self.save_output(model, args.output, "json")
                    
            elif args.command == "insight":
                data = pd.read_csv(args.input)
                insights = self.generate_insights(data, args.type)
                if args.output:
                    self.save_output(insights, args.output, "json")
                    
            elif args.command == "report":
                data = pd.read_csv(args.input)
                report = self.generate_report(data, args.type)
                if args.output:
                    self.save_output(report, args.output, args.type)
                    
            else:
                self.parser.print_help()
                
        except Exception as e:
            self.error_handler.handle_error(e)


if __name__ == "__main__":
    cli = TemplateCLI()
    cli.run()