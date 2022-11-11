from datetime import date
from os.path import exists

class LogWriter():
    def __init__(self, header="Timestamp, Temperature, Humidity, Pressure"):
        self.current_date = None
        self.header = header
        self.__create_file_with_header()

    def __set_filename(self):
        date=str(date.today()).replace("-","_")
        self.filename = date+"py_weather_logs.csv"

    def __validate_file(self):
        current_date = date.today()
        filename_date=str(self.filename).replace("_py_weather_logs.csv","").replace("_","-")
        if  current_date != filename_date:
            self._set_filename()
            self._create_file_with_header()


    def __write_file(self, data_to_write, file_mode):
        with open(self.filename, file_mode) as f:
            if type(data_to_write) is str:
                f.write(data_to_write)
                f.write("\n")
            else:
                print("cannot write data to file, wrong format")
                print(f"dataformat provided: {type(data_to_write)}")
    

    def __create_file_with_header(self):
        self.write_file(self.header, 'w')


    def __log_a_record(self, record):
        self.write_file(record, 'a')


    def _write_data_to_file(self, data):
        self._validate_file()
        self._log_a_record(data)
