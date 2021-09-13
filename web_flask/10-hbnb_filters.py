#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def index():
    """list all states"""
    states = storage.all(State)
    cities = storage.all(City)
    ameni = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, cities=cities,ameni=ameni)



@app.teardown_appcontext
def teardown_appcontext(exception):
    """close the conection with db"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
