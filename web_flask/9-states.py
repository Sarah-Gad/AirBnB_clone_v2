#!/usr/bin/python3
"""This script will start the falsk web application for my HBNB project"""
from flask import Flask, render_template
from models import storage
my_airnbn_app = Flask(__name__)


@my_airnbn_app.route("/states", strict_slashes=False)
def listingstates():
    """This function will be called when
    the user access this url /states"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@my_airnbn_app.route("/states/<id>", strict_slashes=False)
def stateinfo(id):
    """This function will be callled when
    the user access this url /states/<id>"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@my_airnbn_app.teardown_appcontext
def closingst(excep):
    """This function will be called at the end of each request"""
    storage.close()


if __name__ == '__main__':
    my_airnbn_app.run(host='0.0.0.0', port=5000)
