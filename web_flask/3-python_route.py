#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, escape

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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """python is text"""
    python = text.replace('_', ' ')
    return 'Python ' + escape(python)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
