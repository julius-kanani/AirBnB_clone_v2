#!/usr/bin/python3
"""
6-number_odd_or_even module that starts a simple flask web application.
"""


from flask import Flask
from flask import render_template


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
    return f"Python {txt.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ Display "n is a number" only if n is an integer. """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    """ Display a HTML page only if n is an integer. """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_route(n):
    """ Display a HTML page only if n is an integer. """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
