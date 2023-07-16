from ast import Call
from threading import Thread
from sensor import Bme
from api import app
from api import set_sensor_callback
from api.callback import Callback

bme = Bme()
set_sensor_callback(Callback(bme.read_formated, dict))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
