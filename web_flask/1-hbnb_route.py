#!/usr/bin/python3
"""
1-hbnb_route module that starts a simple flask web application.
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ Display "Hello HBNB!. """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ Route to display "HBNB. """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
