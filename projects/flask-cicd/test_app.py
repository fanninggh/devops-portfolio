import pytest
from app import app

def test_hello_route():
    """Test the main route"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'DevOps Portfolio' in response.data

def test_health_route():
    """Test health check"""
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert b'Healthy' in response.data
