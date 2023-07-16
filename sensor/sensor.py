import smbus2
import bme280
from time import sleep


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
                "sensor_id": "1",
                "temperature": f" {data.temperature} C",
                "humididty": f" {data.humidity} %",
                "pressure": f"{data.pressure} hPa"
                }
