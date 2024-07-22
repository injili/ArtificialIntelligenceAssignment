"""
App.py - The main file of the entire application
importations:
    flask modules
"""


from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def get_ai_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and ai_choice == 'scissors') or \
         (user_choice == 'scissors' and ai_choice == 'paper') or \
         (user_choice == 'paper' and ai_choice == 'rock'):
        return "You win!"
    else:
        return "AI wins!"

@app.route('/')
def home():
    """
        The default function
    """
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    ai_choice = get_ai_choice()
    result = determine_winner(user_choice, ai_choice)
    return jsonify({
        'user_choice': user_choice,
        'ai_choice': ai_choice,
        'result': result
    })

@app.errorhandler(404)
def page_not_found(e):
    """"
        The 404 error page
    """
    return "Page not found"
    # return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(port=1111, debug=True)