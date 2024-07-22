import pytest
from app import app, get_ai_choice, determine_winner

# Set up a fixture for the Flask test client
@pytest.fixture
def client():
    # Enable testing mode
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test the get_ai_choice function
def test_get_ai_choice():
    choices = ['rock', 'paper', 'scissors']
    ai_choice = get_ai_choice()
    assert ai_choice in choices

# Test the determine_winner function
def test_determine_winner():
    # Test all winning scenarios for the user
    assert determine_winner('rock', 'scissors') == "You win!"
    assert determine_winner('scissors', 'paper') == "You win!"
    assert determine_winner('paper', 'rock') == "You win!"
    # Test all tie scenarios
    assert determine_winner('rock', 'rock') == "It's a tie!"
    assert determine_winner('scissors', 'scissors') == "It's a tie!"
    assert determine_winner('paper', 'paper') == "It's a tie!"
    # Test all winning scenarios for the AI
    assert determine_winner('rock', 'paper') == "AI wins!"
    assert determine_winner('scissors', 'rock') == "AI wins!"
    assert determine_winner('paper', 'scissors') == "AI wins!"

# Test the home route
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data

# Test the play route
def test_play(client):
    choices = ['rock', 'paper', 'scissors']
    for choice in choices:
        rv = client.post('/play', data={'choice': choice})
        json_data = rv.get_json()
        assert rv.status_code == 200
        assert json_data['user_choice'] == choice
        assert json_data['ai_choice'] in choices
        assert json_data['result'] in ["You win!", "AI wins!", "It's a tie!"]

# Test a non-existent route (404 error)
def test_404_page(client):
    response = client.get('/nonexistent')
    assert response.status_code == 200
    assert b'Page not found' in response.data


# To run the pytest:
# $ pip install pytest pytest-flask
# $ pytest