#!/usr/bin/python3
"""Starts a Flask web application!"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """Displays HTML page with the States content"""
    data = storage.all(State).values()
    return render_template("7-states_list.html", data=data)


@app.teardown_appcontext
def close(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
