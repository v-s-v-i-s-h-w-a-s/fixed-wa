from src.app import app


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
