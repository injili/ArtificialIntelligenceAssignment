"""
App.py - The main file of the entire application
importations:
    flask modules
"""


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    """
        The default function
    """
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    """"
        The 404 error page
    """
    return "Page not found"
    # return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(port=1111, debug=True)