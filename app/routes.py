from flask import render_template
from app import app

@app.route("/")
def measurements():
    #TODO: dopisac pomiary z BME, i zrenderowac tempalate
    # Template powinien sie odswiezac co 1 min
    pass

@app.route("/api/v1/measurements/<name>"):
def get_measurement(name):
    # TODO: get measurenments by name via command line
    pass