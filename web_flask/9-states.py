#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """list all states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_cities(id=None):
    """list all cities"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_appcontext(exception):
    """close the conection with db"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
