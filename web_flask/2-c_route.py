#!/usr/bin/python3
from flask import Flask, escape


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """
    Route that displays 'Hello HBNB!'

    Returns:
        str: The greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """
    Route that displays 'HBNB'

    Returns:
        str: The message.
    """
    return 'HBNB'


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def display_text(text):
    """
    Route that displays 'C ' followed by the value of the text variable.

    Args:
        text (str): The text provided in the route.

    Returns:
        str: The formatted message.
    """
    formatted_text = escape(text.replace('_', ' '))
    return f'C {formatted_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
