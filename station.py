from sensor import Bme
from sqlite import SqliteDataBase
from datetime import datetime as dt
import schedule

bme = Bme()
sqlite  = SqliteDataBase()

def read_and_save_measurements():
    data = bme.read_measurements()
    sqlite.PutItem({
        "datetime" : dt.now().strftime("%m/%d/%Y-%H:%M:%S"),
        "sensor_id" : "1",
        "temperature": data.temperature,
        "humididty": data.humidity,
        "pressure": data.pressure
    })
	
if __name__ == "__main__":
    schedule.every().hour.at(":00").do(read_and_save_measurements)