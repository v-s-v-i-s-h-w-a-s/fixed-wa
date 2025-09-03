"""
Test suite for Flask Weather Analytics Application

This module contains comprehensive tests for the Flask application routes
and functionality to ensure proper behavior and coverage.
"""

import os
import sys

# Add src directory to Python path to import app module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from app import app  # noqa: E402


def test_home_route_status():
    """Test that home route returns HTTP 200 status code."""
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200


def test_home_route_text():
    """Test that home route returns expected welcome message."""
    tester = app.test_client()
    response = tester.get("/")
    assert b"Hello, World! from Flask" in response.data


def test_home_route_content_type():
    """Test that home route returns correct content type header."""
    tester = app.test_client()
    assert tester.get("/").content_type == "text/html; charset=utf-8"


def test_dashboard_route_status():
    """Test that dashboard route returns HTTP 200 status code."""
    tester = app.test_client()
    response = tester.get("/dashboard")
    assert response.status_code == 200


def test_dashboard_route_text():
    """Test that dashboard route returns expected content."""
    tester = app.test_client()
    response = tester.get("/dashboard")
    assert b"Dashboard" in response.data


def test_dashboard_route_contains_html():
    """Test that dashboard route returns HTML content."""
    tester = app.test_client()
    response = tester.get("/dashboard")
    assert b"<h1>" in response.data
    assert b"<p>" in response.data


def test_nonexistent_route():
    """Test that accessing non-existent route returns 404."""
    tester = app.test_client()
    response = tester.get("/nonexistent")
    assert response.status_code == 404


def test_app_instance():
    """Test that Flask app instance is properly configured."""
    assert app.name == "app"
    assert app.config.get("TESTING") is False


def test_multiple_requests():
    """Test that multiple requests to same route work correctly."""
    tester = app.test_client()
    for _ in range(3):
        response = tester.get("/")
        assert response.status_code == 200
        assert b"Hello, World! from Flask" in response.data
