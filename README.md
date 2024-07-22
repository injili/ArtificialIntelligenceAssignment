# Rock, Paper, Scissors Game with Flask

## Overview

This project implements a simple Rock, Paper, Scissors game using Flask for the backend and a basic HTML frontend. The AI opponent uses a random choice strategy. The application provides an interface for the user to play the game, keeps track of the scores, and displays the result of each round.

## Deployment

https://artificialintelligenceassignment.onrender.com/

## Features

- User can select rock, paper, or scissors.
- AI opponent makes a random choice.
- Game determines the winner based on user and AI choices.
- Scores are displayed after each round.
- Simple and intuitive web interface.

## Usage

- Select "Rock", "Paper", or "Scissors" from the dropdown menu.
- Click the "Play" button to play a round against the AI.
- The result of the round, including the choices and the winner, will be displayed.
- The scores will be updated after each round.
- To play another round, select a new choice and click "Play" again.

## Requirements

- Python 3
- Flask
- node

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/injili/ArtificialIntelligenceAssignment
   cd flask_rock_paper_scissors
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask application:**
   ```bash
   python app.py
   ```
2. **Open your browser and navigate to:**
   ```arduino
   http://127.0.0.1:1111/
   ```

## Testing

1. **Install pytest and pytest-flask:**
   ```bash
   pip install pytest pytest-flask
   ```
2. **Run the tests:**
   ```bash
   pytest
   ```

## Collaborators

- Gladys Pasha
- Carla Lagat
- Nyareki Gospel

## License

License
This project is licensed under the MIT License.

## Acknowledgements

- Flask documentation: https://flask.palletsprojects.com/
- pytest documentation: https://docs.pytest.org/
- Tailwind documentation: https://tailwindcss.com/docs/installation

Feel free to contribute to this project by opening issues or submitting pull requests. Happy coding!
