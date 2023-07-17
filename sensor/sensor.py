import smbus2
import bme280
from time import sleep
from datetime import datetime as dt


class Bme():
    def __init__(self):
        self.__port = 1
        self.__i2c_address = 0x76
        self.__bus = smbus2.SMBus(self.__port)
        sleep(1)
        self.__calibration_params = bme280.load_calibration_params(
            self.__bus, self.__i2c_address)

    def read_raw(self):
        return bme280.sample(self.__bus, self.__i2c_address, self.__calibration_params)

    def read_formated(self):
        data = self.read_raw()
        return {"datetime": dt.now().strftime("%m/%d/%Y-%H:%M:%S"),
                "temperature": f"{round(data.temperature,2)}",
                "humidity": f"{round(data.humidity,2)}",
                "pressure": f"{round(data.pressure,2)}"
                }
