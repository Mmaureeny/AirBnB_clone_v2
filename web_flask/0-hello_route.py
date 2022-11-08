#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/airbnb-onepage', strict_slashes=False)
def index():
    """Returns a string at the root route"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
