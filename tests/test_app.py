import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app


def test_home_route_status():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200


def test_home_route_text():
    tester = app.test_client()
    response = tester.get("/")
    assert b"Hello, World! from Flask" in response.data


def test_home_route_content_type():
    tester = app.test_client()
    assert tester.get("/").content_type == "text/html; charset=utf-8"


def test_dashboard_route_status():
    tester = app.test_client()
    response = tester.get("/dashboard")
    assert response.status_code == 200


def test_dashboard_route_text():
    tester = app.test_client()
    response = tester.get("/dashboard")
    assert b"Dashboard" in response.data
