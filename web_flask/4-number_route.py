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
def display_text_args_c(text):
    """Displays a text past as an argument"""
    return "C {}".format(text).replace("_", " ")


@app.route("/python/")
def display_text_args_python_text(text="is cool"):
    """Displays a default text"""
    return "Python {}".format(text).replace("_", " ")


@app.route("/python/<text>")
def display_text_args_python(text):
    """Displays another text past as an argument"""
    return "Python {}".format(text).replace("_", " ")


@app.route("/number/<int:n>")
def display_integer(n):
    """Display 'n' is a number only if 'n' is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
