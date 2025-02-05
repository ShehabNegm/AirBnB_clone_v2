#!/usr/bin/python3
""" starting flask web server"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """function to print hello message"""
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """function to print hello message"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """function to print variable in the url"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text=None):
    """function to print variable in the url"""
    if not text:
        return "Python is cool"
    else:
        return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
