from flask_wtf import FlaskForm
from wtforms import StringField

class MeasurementForm(FlaskForm):
    temperatureBox=StringField('temperature')
    humidityBox=StringField('humidity')
    pressureBox=StringField('pressure')