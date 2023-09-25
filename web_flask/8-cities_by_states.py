#!/usr/bin/python3
"""using Flask to list states using Jinja2 templates"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def list_states():
    """list states from storage"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close(exception):
    """teardown mmethod"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
