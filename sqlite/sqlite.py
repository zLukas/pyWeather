import sqlite3
class SqliteDataBase:

    def __init__(self):

        CREATE_QUERY = '''
                            CREATE TABLE measurements
                            (datetime       TEXT PRIMARY KEY NOT NULL,
                            sensor_id       TEXT             NOT NULL,
                            temperature[C]  TEXT             NOT NULL,
                            humidity[%]     TEXT             NOT NULL,
                            pressure[hPa]   TEXT             NOT NULL);
                       '''
        self._dbName = "measurements.db"
        self._table_name = "measurements"
        self._sqlite3 = None
        self._sqlite3 = sqlite3.connect(self._dbName)
        try:
            self._sqlite3.execute(CREATE_QUERY)
            self._sqlite3.commit()
            self._sqlite3.close()
        except sqlite3.OperationalError: 
             pass

    def PutItem(self, items: dict):
        self._sqlite3 = sqlite3.connect(self._dbName)
        if self._sqlite3 is not None:
            if type(items) == dict:
                putQuery = '''
                               INSERT INTO measurements
                               (datetime, sensor_id, temperature , humidity , pressure)
                               VALUES (?, ?, ?, ?, ?);
                           '''

                values = (items['datetime'], 1,
                    items['temperature'], items['humidity'], items['pressure'])
                self._sqlite3.execute(putQuery, values)
                self._sqlite3.commit()
                self._sqlite3.close()
            else:
                print("data is not in dict, format")
