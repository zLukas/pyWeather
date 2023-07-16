from telnetlib import BM
from flask import Flask
from flask import redirect
from .config import Config
from sensor import Bme

bme = Bme()
app = Flask("station")
app.config.from_object(Config)

def set_sensor_callback(callback):
    global sensor_callback
    sensor_callback = callback

@app.route("/", methods=["GET"])
def redirect_to_measurements():
    return redirect("/measurements")

@app.route("/measurements", methods=["GET"])
def get_measurements():
    return bme.read_formated()
