from datetime import datetime
from os.path import exists

def is_file_valid(filename):
    file = exists(filename)
    file_is_valid=False
    if file is not None:
        current_date=str(datetime.now().date())
        filename_date=str(filename).replace("_py_weather_logs.csv","").replace("_","-")
        if current_date == filename_date:
            file_is_valid=True
        else:
            pass
    else:
        pass
    return file_is_valid


def write_file(filename, data_to_write, file_mode):
    with open(filename, file_mode) as f:
        if type(data_to_write) is str:
            f.write(data_to_write)
            f.write("\n")
        else:
            print("cannot write data to file, wrong format")
            print(f"dataformat provided: {type(data_to_write)}")
    

def create_file_header(filename, header):
    write_file(filename, header, 'w')


def log_a_record(filename, record):
    write_file(filename, record, 'a')


def log_data(filename,data):
    #date=str(datetime.now().date()).replace("-","_")
    #filename = date+"_py_weather_logs.csv"
    if is_file_valid(filename):
        log_a_record(filename, data)
    else:
        create_file_header(filename, data)
    