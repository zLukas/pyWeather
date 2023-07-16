from flask import Flask
from .config import Config


app = Flask("station")
app.config.from_object(Config)

bme_callback = None

@app.route("/", methods=["GET"])
def redirect_to_measurements():
    return redirect("/measurements")

@app.route("/measurements", methods=["GET"])
def get_measurements():
    global bme_callback
    response = None
    if bme_callback is not None \
        and bme_callback.return_type is not None:
        response = bme_callback.function()
    return response