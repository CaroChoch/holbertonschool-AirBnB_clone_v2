#!/usr/bin/python3
""" Script that starts a Flask web application """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Prints the message 'Hello HBNB!' when '/' is called """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints the message 'HBNB' when '/hbnb' is called """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Prints the message 'C' when '/c/<text>' is called """
    return "C " + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
