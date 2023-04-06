#!/usr/bin/python3
"""
Script that starts a Flask web application and display
a HTML page with list of states sorted by name
"""
from flask import Flask, render_template
from models import storage
from models.state import *


app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """ Closes the database after a request has been processed """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states(id=None):
    """ Displays a HTML page with a list of all states and aminities """
    print(f"Storage: {storage}")
    states = storage.all(State)
    aminities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, aminities=aminities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
