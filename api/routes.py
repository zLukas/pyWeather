from api import callback
from flask import make_response
from api import app
from flask import redirect


class RestApi:
    def __init__(self, measurement_callback_obj: callback.Callback = None):
        self._measurement_callback = measurement_callback_obj

    @app.route("/", methods=["GET"])
    def redirect_to_measurements(self):
        return redirect("/measurements")

    @app.route("/measurements", methods=["GET"])
    def get_measurements(self):
        response = None
        if self._measurement_callback is not None \
           and self._measurement_callback.return_type is not None:
            response = self._measurement_callback.function()
        return response
