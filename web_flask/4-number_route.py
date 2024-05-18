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
def cpage(text):
    """This function will be called when the used access this url /c/<text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@my_airbnb_app.route("/python", strict_slashes=False)
@my_airbnb_app.route("/python/<text>", strict_slashes=False)
def pythonpage(text="is cool"):
    """This function will be called when user access the url /pythin/<text>"""
    converted_txt = text.replace("_", " ")
    return "Python {}".format(converted_txt)


@my_airbnb_app.route("/number/<n>", strict_slashes=False)
def numberpage(n):
    """This function will be called when user access the url /number/<n>"""
    if n.isdigit():
        return "{} is a number".format(n)

if __name__ == "__main__":
    my_airbnb_app.run(host='0.0.0.0', port=5000)
