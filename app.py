from flask import Flask, send_from_directory
import random

app = Flask(__name__)


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('tm4csite/dist', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('tm4csite/dist', path)


@app.route("/temp")
def get_temp():
    return str(random.randint(0, 100))


@app.route("/motion")
def get_motion():
    num = (random.randint(0, 1))
    if num is 0:
        return "None Detected"
    else:
        return "Motion has been detected!"


@app.route("/humidity")
def get_humidity():
    return str(random.randint(0, 100))


if __name__ == "__main__":
    app.run(debug=True)
