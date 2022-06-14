import smbus2
import bme280
from time import sleep


class Bme():
	def __init__(self):
		self.__port = 1
		self.__i2c_address= 0x76
		self.__bus = smbus2.SMBus(self.__port)
		sleep(1)
		self.__calibration_params = bme280.load_calibration_params(self.__bus, self.__i2c_address)

	def read_measurements(self):
		data = bme280.sample( self.__bus, self.__i2c_address, self.__calibration_params)
		return data


bme=Bme()