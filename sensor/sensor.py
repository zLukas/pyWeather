import smbus2
import bme280
from time import sleep

port = 1
address = 0x76

bus = smbus2.SMBus(port)
sleep(1)


while True:

	calibration_params = bme280.load_calibration_params(bus, address)

	data = bme280.sample( bus, address, calibration_params)


	print(f"timestamp: {data.timestamp} ")
	print(f"temperature {data.temperature:.1f} C")
	print(f"pressure: {data.pressure:.1f} hPa" )
	print(f"humidity: {data.humidity:.1f} %")
	print("\n\n")
	sleep(5)
