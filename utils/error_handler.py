"""
Error handling module.

This module performs error handling operations throughout the application.
"""

import streamlit as st
import logging
from typing import Optional
from datetime import datetime
import traceback
import sys


class ErrorHandler:
    def __init__(self):
        # Logging configuration
        logging.basicConfig(
            filename="app_errors.log",
            level=logging.ERROR,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.logger = logging.getLogger(__name__)
        
    def handle_error(self, error: Exception, context: Optional[str] = None):
        """
        Performs error handling.
        
        Args:
            error: Caught error
            context: Error context
        """
        try:
            # Prepare error details
            error_details = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "error_type": type(error).__name__,
                "error_message": str(error),
                "context": context,
                "traceback": traceback.format_exc(),
            }
            
            # Log the error
            self._log_error(error_details)
            
            # Show error message to user
            self._display_error_message(error_details)
            
        except Exception as e:
            # Log errors that occur during error handling
            self.logger.error(f"Error occurred during error handling: {str(e)}")
            
    def _log_error(self, error_details: dict):
        """Logs the error."""
        log_message = (
            f"\nTimestamp: {error_details['timestamp']}\n"
            f"Error Type: {error_details['error_type']}\n"
            f"Error Message: {error_details['error_message']}\n"
            f"Context: {error_details['context']}\n"
            f"Traceback:\n{error_details['traceback']}\n"
            f"{'='*50}\n"
        )
        
        self.logger.error(log_message)
        
    def _display_error_message(self, error_details: dict):
        """Shows error message to user."""
        # Show error message
        st.error(
            f"An error occurred:\n\n"
            f"**Error Type:** {error_details['error_type']}\n"
            f"**Error Message:** {error_details['error_message']}\n"
            f"**Context:** {error_details['context']}\n\n"
            "Please try again later or contact the administrator."
        )
        
        # Show error details in expandable section
        with st.expander("Error Details"):
            st.code(error_details["traceback"])
            
    def handle_critical_error(self, error: Exception):
        """
        Handles critical errors.
        
        Args:
            error: Critical error
        """
        try:
            # Prepare critical error details
            error_details = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "error_type": type(error).__name__,
                "error_message": str(error),
                "traceback": traceback.format_exc(),
            }
            
            # Log the error
            self._log_error(error_details)
            
            # Show critical error message
            st.error(
                "A critical error occurred. The application is closing...\n\n"
                "Please contact the administrator."
            )
            
            # Close the application
            sys.exit(1)
            
        except Exception as e:
            # Log errors that occur during critical error handling
            self.logger.error(f"Error occurred during critical error handling: {str(e)}")
            sys.exit(1)
            
    def display_friendly_error(self, error_message: str, suggestion: str):
        """
        Shows user-friendly error message.
        
        Args:
            error_message: Error message
            suggestion: Suggestion
        """
        st.error(
            f"{error_message}\n\n"
            f"**Suggestion:** {suggestion}"
        )
        
    def log_warning(self, warning_message: str, context: Optional[str] = None):
        """
        Logs warning message.
        
        Args:
            warning_message: Warning message
            context: Context
        """
        log_message = (
            f"\nTimestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Warning Message: {warning_message}\n"
            f"Context: {context}\n"
            f"{'='*50}\n"
        )
        
        self.logger.warning(log_message)
        
    def display_warning(self, warning_message: str, suggestion: Optional[str] = None):
        """
        Shows user-friendly warning message.
        
        Args:
            warning_message: Warning message
            suggestion: Suggestion
        """
        if suggestion:
            st.warning(
                f"{warning_message}\n\n"
                f"**Suggestion:** {suggestion}"
            )
        else:
            st.warning(warning_message) 