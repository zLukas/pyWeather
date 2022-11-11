from flask import render_template
from app import app
from flask import render_template
from flask import redirect
from app.forms import MeasurementForm


sensor_data = None

@app.route("/", methods=["GET"])
def go_to_measurements():
    return redirect("/measurements")

@app.route("/measurements", methods=["GET"])
def measurements():
        global sensor_data
        form = MeasurementForm()
        form.humidityBox.data=f"{sensor_data.humidity:.1f} %"
        form.pressureBox.data= f"{sensor_data.pressure:.1f} hPa"
        form.temperatureBox.data = f"{sensor_data.temperature:.1f} C"
        return render_template('measurements.html', form=form)
