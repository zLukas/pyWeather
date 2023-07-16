from ast import Call
from threading import Thread
from sensor import Bme
from api import app
from api.routes import RestApi
from api.callback import Callback

bme = Bme()
api = RestApi(Callback(bme.read_formated, dict))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
