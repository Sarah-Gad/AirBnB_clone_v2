#!/usr/bin/python3
"""This script will start a flask web application"""
from flask import Flask
my_airbnb_app = Flask(__name__)


@my_airbnb_app.route("/", strict_slashes=False)
def hellopage():
    """This fucntion will be called when the user access the root url /"""
    return "Hello HBNB!"


@my_airbnb_app.route("/hbnb", strict_slashes=False)
def hbnbpage():
    """This fucntion will be called when the user access this url /hbnb"""
    return "HBNB"


@my_airbnb_app.route("/c/<text>", strict_slashes=False)
def c_page(text):
    """This function will be called when the used access this url /c/<text>"""
    converted_txt = text.replace('_', ' ')
    return f"c {converted_txt}"


if __name__ == "__main__":
    my_airbnb_app.run(host='0.0.0.0', port=5000)
