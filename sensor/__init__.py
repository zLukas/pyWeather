import time
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

    def getBme280Data(self):
        return  self.bme280.read_formated()
    def getLtr390Data(self):
        return self.ltr390.UVS()
    def getTsl2591Data(self):
        return self.tsl2591.Lux()
    def getSgp40Data(self):
        temperature, humidity, _ = self.getBme280Data()
        return self.spg40.getVocNoxIndex(temperature, humidity)