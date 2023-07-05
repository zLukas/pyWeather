import sqlite3
import os
class SqliteDataBase:

    def __init__(self):

        CREATE_QUERY = '''
                            CREATE TABLE measurements
                            (datetime    TEXT PRIMARY KEY NOT NULL,
                            sensor_id    TEXT             NOT NULL,
                            temperature  TEXT             NOT NULL,
                            humidity     TEXT             NOT NULL,
                            pressure     TEXT             NOT NULL);
                       '''
        self._dbName = "measurements.db"
        self._table_name = "measurements"
        self.status = ""
        self._sqlite3 = None
        try:
            self._sqlite3 = sqlite3.connect(self._dbName)
            self.status = f"connected"
            self._sqlite3.execute(CREATE_QUERY)
            self._sqlite3.close()
        except: 
            print(" cannot create database ")

    def PutItem(self, items: dict):
        self._sqlite3 = sqlite3.connect(self._dbName)
        if self._sqlite3 is not None:
            if type(items) == dict:
                putQuery = '''
                               INSERT INTO measurements
                               (datetime, sensor_id, temperature , humidity , pressure)
                               VALUES (?, ?, ?, ?, ?);
                           '''
                
                values = (items['datetime'], items['sensor_id'], items['temperature'], items['humidity'], items['pressure'])
                self._sqlite3.execute(putQuery, values)
                self._sqlite3.commit()
                self._sqlite3.close()

if __name__ == "__main__":
    if os.path.exists("measurements.db"):
        os.remove("measurements.db")

    db =  MeasurementDataBase()
    if db.status != "disconnected":
        d = {
            "datetime" : "1-mar-2020",
            "sensor_id": "1",
            "temperature": "25.0",
            "humidity" : "20.0",
            "pressure" : "100",
        }
        db.PutItem(d)
        d = {
            "datetime" : "2-mar-2020",
            "sensor_id": "1",
            "temperature": "20.0",
            "humidity" : "20.0",
            "pressure" : "100",
        }
        db.PutItem(d)
        d = {
            "datetime" : "3-mar-2020",
            "sensor_id": "1",
            "temperature": "27.0",
            "humidity" : "20.0",
            "pressure" : "100",           
        }
        db.PutItem(d)
    else:
        print("cannot connect to database")