from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MeasurementForm(FlaskForm):
    temperatureBox=StringField('temperature', validators=[DataRequired()])
    humidityBox=StringField('humidity', validators=[DataRequired()])
    pressureBox=StringField('pressure', validators=[DataRequired()])