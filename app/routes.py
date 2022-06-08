from flask import render_template
from app import app
from flask import render_template
from flask import redirect
from app.forms import MeasurementForm



@app.route("/", methods=["GET"])
def go_to_measurements():
    return redirect("/measurements")

@app.route("/measurements", methods=["GET"])
def measurements():
    form = MeasurementForm()
    form.humidityBox.data="50%"
    form.pressureBox.data="1010 hpa"
    form.temperatureBox.data="20.0 C"
    return render_template('measurements.html', form=form)



# TODO: get measurenments by name via command line