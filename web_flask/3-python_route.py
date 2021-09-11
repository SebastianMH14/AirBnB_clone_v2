#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """Hello HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """c is cool"""
    return 'C ' + text.replace('_', ' ')

@app.route('/python/<text>', strict_slashes=False)
def python(text=None):
    """python is text"""
    return 'Python ' + text.replace('_', ' ')

@app.route('/python/', strict_slashes=False)
def python2(text="is cool"):
    """python is cool"""
    return 'Python ' + text


if __name__ == '__main__':
    app.run(debug=True, port=5000)
