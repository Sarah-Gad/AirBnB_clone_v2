#!/usr/bin/python3
"""This script will start flask web application"""
from models import storage
from flask import Flask, render_template

my_aribnb_app= Flask(__name__)


@my_aribnb_app.route("/hbnb_filters", strict_slashes=False)
def list_filter():
    """this function will be called when the user accesss the url /hbnb_filters"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@my_aribnb_app.teardown_appcontext
def teardown(excep):
    """This function will be called at the end of each request"""
    storage.close()


if __name__ == "__main__":
    my_aribnb_app.run(host="0.0.0.0")
