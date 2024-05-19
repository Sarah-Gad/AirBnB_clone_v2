#!/usr/bin/python3
"""This script will start the falsk web application for my HBNB project"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def listing_states():
    """This function will be called when the
    user access this url /states_list"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(excep):
    """This function will be called at the end of each request"""
    storage.close()


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
