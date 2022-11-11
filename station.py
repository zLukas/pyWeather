from app import app
from time import sleep
from sys import path
from sensor import bme
from threading import Lock
from threading import Thread
from loger import LogWriter
from datetime import datetime as dt
from app import sensor_data

log_writer = LogWriter()
lock = Lock()
def bme_read_thread(lock=lock):
    global sensor_data
    with lock:
        sensor_data = bme.read_measurements()
    now = dt.now()
    ts = dt.timestamp(now)
    record_str= ','.join([str(ts),
                          sensor_data.temperature,
                          sensor_data.humidity,
                          sensor_data.pressure])
    log_writer.write_data_to_file(record_str)
    sleep(5)

if __name__ == "__main__":
     inf_thread = Thread(target=bme_read_thread, daemon=True)
     app.run(host='0.0.0.0', threaded=True)