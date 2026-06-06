"""Tests for Hello Flask application"""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestWelcomeEndpoint:
    """Tests for GET / endpoint."""

    def test_welcome_returns_200(self, client):
        """Given service is running, when requesting GET /, then return 200."""
        response = client.get("/")
        assert response.status_code == 200

    def test_welcome_returns_json(self, client):
        """Given requesting GET /, when parsing response, then it is JSON."""
        response = client.get("/")
        assert response.content_type == "application/json"

    def test_welcome_contains_message(self, client):
        """Given response is JSON, when parsing body, then it contains message field."""
        response = client.get("/")
        data = response.get_json()
        assert "message" in data
        assert data["message"] == "Welcome to Hello Flask!"


class TestHealthEndpoint:
    """Tests for GET /health endpoint."""

    def test_health_returns_200(self, client):
        """Given service is running, when requesting GET /health, then return 200."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_json(self, client):
        """Given requesting GET /health, when parsing response, then it is JSON."""
        response = client.get("/health")
        assert response.content_type == "application/json"

    def test_health_returns_status_ok(self, client):
        """Given response is JSON, when parsing body, then it contains status=ok."""
        response = client.get("/health")
        data = response.get_json()
        assert data == {"status": "ok"}
