from flask import render_template
from app import app
from flask import render_template
from flask import redirect
from app.forms import MeasurementForm
from sensor import bme

@app.route("/", methods=["GET"])
def go_to_measurements():
    return redirect("/measurements")

@app.route("/measurements", methods=["GET"])
def measurements():
        data=bme.read_measurements()
        form = MeasurementForm()
        form.humidityBox.data=f"{data.humidity:.1f} %"
        form.pressureBox.data= f"{data.pressure:.1f} hPa"
        form.temperatureBox.data = f"{data.temperature:.1f} C"
        return render_template('measurements.html', form=form)


# TODO: get measurenments by name via command line