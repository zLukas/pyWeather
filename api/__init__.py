from flask import Flask
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)
from api import routes
from .routes  import sensor_data