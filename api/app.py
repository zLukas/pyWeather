from telnetlib import BM
from flask import Flask
from flask import redirect
from .config import Config
from sensor import SensorHat

app = Flask("station")
app.config.from_object(Config)
#separate api and sensor, objects
hat = SensorHat()


def set_sensor_callback(callback):
    global sensor_callback
    sensor_callback = callback

@app.route("/", methods=["GET"])
def redirect_to_measurements():
    return redirect("/measurements")

@app.route("/measurements", methods=["GET"])
def get_measurements():
    return hat.getData()


@app.route("/status", methods=["GET"])
def heartbeat():
    return {"status": "I'm Alive"}
