#!/usr/bin/python3
"""Starting with flask web framework!"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Defining a view for my app root"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
