from ast import Call
from threading import Thread
from sensor import Bme
from api import app


if __name__ == "__main__":
    app.run(host='0.0.0.0')
