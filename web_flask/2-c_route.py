#!/usr/bin/python3
"""Starting with flask web framework!"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def display_hello():
    """Defining a view for my app root"""
    return "Hello HBNB!"


@app.route("/hbnb")
def display_hbnb():
    """Defining a view for '/hbnb' route"""
    return "HBNB"


@app.route("/c/<text>")
def display_text_args(text):
    """Displays a text past as an argument"""
    return "C {}".format(text).replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
