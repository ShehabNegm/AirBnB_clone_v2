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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
