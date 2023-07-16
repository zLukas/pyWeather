from flask import Flask
from .config import Config


app = Flask("station")
app.config.from_object(Config)