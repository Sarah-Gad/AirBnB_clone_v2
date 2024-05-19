#!/usr/bin/python3
"""This script will start the falsk web application for my HBNB project"""
from flask import Flask, render_template
from models import storage
my_airnbn_app = Flask(__name__)


@my_airnbn_app.route("/cities_by_states", strict_slashes=False)
def listing_cities():
    """This function will be called when the
    user access this url /states_list"""
    allstates = storage.all("State").values()
    return render_template("8-cities_by_states.html", passed_states=allstates)


@my_airnbn_app.teardown_appcontext
def closingst(excep):
    """This function will be called at the end of each request"""
    storage.close()


if __name__ == '__main__':
    my_airnbn_app.run(host='0.0.0.0', port=5000)
