#!/usr/bin/python3
""" Script that starts a Flask web application """


from flask import Flask
from flask import render_template

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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_is_cool(text="is cool"):
    """ Prints the message 'Python' when '/python/<text>' is called """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Prints the message 'n is a number' when '/number/<n>' is called only
    if n is an int
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays a HTML page only if n is an integer """
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
