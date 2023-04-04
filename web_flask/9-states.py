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


@app.route('/states', strict_slashes=False)
def states():
    """ Displays a HTML page with a list of all states """
    states = storage.all(State)
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """ Displays a HTML page of a State and their cities """
    for state in storage.all('State'):
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', not_found=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
