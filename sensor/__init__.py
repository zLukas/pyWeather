from  datetime import datetime as dt
from .bme280 import BME280
from .ltr390 import LTR390
from .tsl2591 import TSL2591
from .spg40 import SGP40



class SensorHat():
    def __init__(self):
        self.bme280 = BME280()
        self.ltr390 = LTR390()
        self.tsl2591 = TSL2591()
        self.spg40  = SGP40()

    def getData(self):

        createRecord = lambda value, unit: {"value": value, "unit": unit}

        temperature, humidity, pressure = self.bme280.read_formated()
        voc, nox = self.spg40.getVocNoxIndex(temperature, humidity)
        uv = self.ltr390.UVI()
        lux = self.tsl2591.Lux()

        return {"time": dt.now().strftime("%m/%d/%Y-%H:%M:%S"),
                "temperature": createRecord(temperature, "C"),
                "humidity": createRecord(humidity, "%%"),
                "pressure": createRecord(pressure, "hPa"),
                "uv": createRecord(int(uv), "UVI"),
                "lux": createRecord(int(lux), "lx"),
                "voc": createRecord(int(voc), "ppb"),
                "nox": createRecord(int(nox), "ppb")}
