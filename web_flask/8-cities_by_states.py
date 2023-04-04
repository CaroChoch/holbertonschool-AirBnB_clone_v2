#!/usr/bin/python3
"""
Script that starts a Flask web application and display
a HTML page with list of states sorted by name
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(self):
    """ Closes the database after a request has been processed """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """ Displays a HTML page with a list of cities by states """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
