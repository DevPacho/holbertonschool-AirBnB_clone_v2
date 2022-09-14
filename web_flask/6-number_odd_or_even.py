#!/usr/bin/python3
"""Starting with flask web framework!"""

from flask import Flask, render_template

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
    """Displays 'n' is a number only if 'n' is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def integer_template(n):
    """Displays a HTML page only if 'n' is an integer"""
    return render_template("5-number.html", data=n)


@app.route("/number_odd_or_even/<int:n>")
def even_or_odd_integer_template(n):
    """Displays a HTML page that validates if a given number
    is even or odd"""
    return render_template("6-number_odd_or_even.html", data=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
