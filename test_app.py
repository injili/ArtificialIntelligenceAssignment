"""
    Test_app.py - tests for the app functions
    To run the pytest - ...
""" 
import pytest
from app import app
from app import get_completion


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_404_page(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'<!DOCTYPE html>' in response.data

if __name__ == "__main__":
    pytest.main()