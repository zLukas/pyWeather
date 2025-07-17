# from telnetlib import BM
# from flask import Flask
# from flask import redirect
# from flask import jsonify
# from .config import Config
# from sensor import SensorHat

# app = Flask("station")
# app.config.from_object(Config)
# #separate api and sensor, objects
# hat = SensorHat()


# def set_sensor_callback(callback):
#     global sensor_callback
#     sensor_callback = callback

# @app.route("/", methods=["GET"])
# def redirect_to_measurements():
#     return redirect("/measurements")

# @app.route("/measurements", methods=["GET"])
# def get_measurements():
#     return hat.getData()


# @app.route("/status", methods=["GET"])
# def heartbeat():
#     return {"status": "I'm Alive"}



from flask import Flask, render_template, jsonify
from flask import redirect
from flask import Response
from threading import Thread
import time
from .config import Config
from sensor import SensorHat

app = Flask("station")
app.config.from_object(Config)
hat = SensorHat()

latest_data = {}

def sensor_reader():
    global latest_data
    while True:
        latest_data = hat.getData()
        time.sleep(60)

# Start background thread to read sensor data every minute
Thread(target=sensor_reader, daemon=True).start()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", data=latest_data)

@app.route("/api/v1/raw", methods=["GET"])
def get_measurements():
    return jsonify(latest_data)

@app.route("/api/v1/status", methods=["GET"])
def heartbeat():
    return {"status": "I'm Alive"}
