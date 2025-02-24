#!/usr/bin/python3
"""A Script to start a Flask web application with a three view functions """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Returns HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ replace text with a variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
