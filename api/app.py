from flask import Flask
from flask import redirect
from .config import Config


app = Flask("station")
app.config.from_object(Config)

sensor_callback = None

def set_sensor_callback(callback):
    global sensor_callback
    sensor_callback = callback

@app.route("/", methods=["GET"])
def redirect_to_measurements():
    return redirect("/measurements")

@app.route("/measurements", methods=["GET"])
def get_measurements():
    response = {}
    if sensor_callback is not None:
        if sensor_callback.return_type is not None:
            response = sensor_callback.function()
        else:
            response = {"error": "calback function returns None type"}
    else:
        response = {"error": "calback function is not defined"}
    return response
