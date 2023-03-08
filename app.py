from flask import Flask, send_from_directory
import random

from mqtt_client import *

app = Flask(__name__)


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('tm4csite/dist', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('tm4csite/dist', path)


# Return the current temperature reading
@app.route("/temp")
def get_temp():
    return str(random.randint(0, 100))


# Return the current motion reading
@app.route("/motion")
def get_motion():
    num = (random.randint(0, 1))
    if num == 0:
        return "None Detected"
    else:
        return "Motion has been detected!"


# Return the current temperature reading
@app.route("/humidity")
def get_humidity():
    return str(random.randint(0, 100))


if __name__ == "__main__":


    initialize()
