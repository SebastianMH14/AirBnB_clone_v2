#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_states():
    """cities_by_states"""
    states = storage.all(State)
    cities = storage.all(City)
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """close the conection with db"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
