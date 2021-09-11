#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text=None):
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
