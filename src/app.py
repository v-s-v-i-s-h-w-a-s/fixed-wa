"""
Flask Weather Analytics Application

This module provides a simple Flask web application for weather analytics
with basic routes for home and dashboard pages.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """
    Home route handler.

    Returns:
        str: Welcome message
    """
    return "Hello, World! from Flask"


@app.route("/dashboard")
def dashboard() -> str:
    """
    Dashboard route handler.

    Returns:
        str: HTML content for dashboard page
    """
    return "<h1>Dashboard</h1><p>This is a simple dashboard page.</p>"


if __name__ == "__main__":
    app.run(debug=True)
