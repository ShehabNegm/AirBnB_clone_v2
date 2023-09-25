#!/usr/bin/python3
"""using Flask to list states using Jinja2 templates"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def list_all():
    """list states. citieies, aminities from storage"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states, amenities = amenities)


@app.teardown_appcontext
def close(exception):
    """teardown mmethod"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
