#!/usr/bin/python3
"""
3-python_route module that starts a simple flask web application.
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ Display "Hello HBNB!". """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ Display "HBNB". """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ Display "C" followed by text value of the text variable. """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False, defaults={"txt": "is cool"})
@app.route("/python/<txt>", strict_slashes=False)
def python_route(txt):
    """ Display "Python" followed by text value of the text variable. """
    return f"C {txt.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
