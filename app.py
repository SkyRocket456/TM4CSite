import json
import random
import threading
from flask import Flask, send_from_directory, request
import paho.mqtt.client as mqtt

app = Flask(__name__)

motion = None
light = None
moisture = None


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('tm4csite/dist', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('tm4csite/dist', path)


# Return the current temperature reading
@app.route("/motion")
def get_motion():
    if motion is None:
        return "Motion reading not available"
    return str(random.randint(0, 1))


# Return the current motion reading
@app.route("/light")
def get_light():
    if light is None:
        return "Light reading not available"
    return str(random.randint(0, 4096))


# Return the current temperature reading
@app.route("/moisture")
def get_moisture():
    if moisture is None:
        return "Moisture reading not available"
    return str(random.randint(0, 4096))


@app.route("/pin_control", methods=['POST'])
def pin_control():
    if request.method == 'POST':
        # Process the data here...
        info = request.data.decode()

        # convert to dict
        json_object = json.loads(info)

        pin_type = json_object["pin_type"]
        pin_number = json_object["pin_number"]
        signal = json_object["signal"]
        io = json_object["io"]

        print(json_object)

    return "1"


def flask():
    app.run()


# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("sensor/motion")
    client.subscribe("sensor/light")
    client.subscribe("sensor/moisture")


def on_message(client, obj, msg):
    if msg.topic == "sensor/motion":
        global motion
        if int(msg.payload.decode()) == 0:
            motion = "No motion"
        else:
            motion = "Motion"
    if msg.topic == "sensor/light":
        global light
        light = str(int(msg.payload.decode()) / 40.96)
    if msg.topic == "sensor/moisture":
        global moisture
        moisture = str(int(msg.payload.decode()) / 40.96)

    print("Incoming message from " + msg.topic + " with QoS " + str(msg.qos) + ": " + str(msg.payload))


def on_publish(client, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(client, obj, level, string):
    print(string)


def mqtt_client():
    mqttc = mqtt.Client(transport="websockets")
    mqttc.tls_set()
    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe

    # Uncomment to enable debug messages
    # mqttc.on_log = on_log

    mqttc.username_pw_set("pljcjeom", "pCWWNWHzPsBk")
    # Connect
    mqttc.connect("driver.cloudmqtt.com", 38893)

    # Continue the network loop, exit when an error occurs

    mqttc.loop_start()

    while True:
        pass


if __name__ == "__main__":
    flask_app = threading.Thread(target=flask)
    mqtt_app = threading.Thread(target=mqtt_client)

    flask_app.start()
    mqtt_app.start()
