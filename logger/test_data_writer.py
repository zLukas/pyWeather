import pytest
from data_writer import is_file_valid
from data_writer import write_data_to_file
from datetime import datetime
from datetime import timedelta
from os import remove

date=str(datetime.now().date()).replace("-","_")
TEST_FILE_NAME=date+"_py_weather_logs.csv"


def test_is_file_valid_file_no_file():
    assert False == is_file_valid("dummy_name.csv")

def test_is_file_valid_proper_file_exist():
    # Arrange
    test_file = open(TEST_FILE_NAME, 'w')

    # Act
    test_result = is_file_valid(TEST_FILE_NAME)

    # Teardown
    remove(TEST_FILE_NAME)

    # Assert
    assert True==test_result

def test_is_file_valid_old_file_exist():
    # Arrange
    old_date=datetime.now().date() - timedelta(days=1)
    OLD_TEST_FILE_NAME=str(old_date).replace("-","_")+"_py_weather_logs.csv"

    test_file = open(OLD_TEST_FILE_NAME, 'w')

    # Act 
    test_result = is_file_valid(OLD_TEST_FILE_NAME)

    # Teardown
    remove(OLD_TEST_FILE_NAME)

    # Assert
    assert False == test_result


def test_log_data_no_file_proper_input_data():
    # Arrange
    header="col1,col2,col3"

    # Act 
    log_data(TEST_FILE_NAME, header)
    file_lines=[]
    file_lines_num=0
    with open(TEST_FILE_NAME) as f:
        for line in f.readlines():
            file_lines.append(line)
    
    file_header=str(file_lines[0]).replace("\n","")
    file_len = len(file_lines)
    # Teardown
    remove(TEST_FILE_NAME)

    # Assert
    assert 1 == file_len 
    assert header == file_header 

def test_log_data_add_record_to_existing_file():
    # Arrange
    header="col1,col2,col3"
    with open(TEST_FILE_NAME, 'w') as t:
        t.write(header)
        t.write("\n")
    
    test_record_to_write="1, 2, 3, 4"
    # Act
    log_data(TEST_FILE_NAME, test_record_to_write)
    file_lines=[]
    file_lines_num=0
    with open(TEST_FILE_NAME) as f:
        for line in f.readlines():
            file_lines.append(line)
    
    file_header=str(file_lines[0]).replace("\n","")
    file_record=str(file_lines[1]).replace("\n","")
    file_len = len(file_lines)
    # Teardown
    remove(TEST_FILE_NAME)

    # Assert
    assert 2 == file_len 
    assert header == file_header 
    assert test_record_to_write == file_record


def test_write_data_to_file_add_several_records_new_file():
    # Arrange
    header="col1, col2, col3"
    test_record_to_write1="1, 2, 3, 4"
    test_record_to_write2="5, 6, 7, 8"
    test_record_to_write3="9, 10, 11, 12"
    # Act
    write_data_to_file(TEST_FILE_NAME, header)
    write_data_to_file(TEST_FILE_NAME, test_record_to_write1)
    write_data_to_file(TEST_FILE_NAME, test_record_to_write2)
    write_data_to_file(TEST_FILE_NAME, test_record_to_write3)
    file_lines=[]
    file_lines_num=0
    with open(TEST_FILE_NAME) as f:
        for line in f.readlines():
            file_lines.append(line)
    
    file_header=str(file_lines[0]).replace("\n","")
    file_record1=str(file_lines[1]).replace("\n","")
    file_record2=str(file_lines[2]).replace("\n","")
    file_record3=str(file_lines[3]).replace("\n","")
    file_len = len(file_lines)
    # Teardown
    remove(TEST_FILE_NAME)

    # Assert
    assert 4 == file_len 
    assert header == file_header 
    assert test_record_to_write1 == file_record1
    assert test_record_to_write2 == file_record2
    assert test_record_to_write3 == file_record3

def test_lwrite_data_to_file_add_several_records_existing_file():
    # Arrange
    header="col1, col2, col3"
    with open(TEST_FILE_NAME, 'w') as t:
        t.write(header)
        t.write("\n")
    test_record_to_write1="1, 2, 3, 4"
    test_record_to_write2="5, 6, 7, 8"
    test_record_to_write3="9, 10, 11, 12"
    # Act
    write_data_to_file(TEST_FILE_NAME, test_record_to_write1)
    write_data_to_file(TEST_FILE_NAME, test_record_to_write2)
    write_data_to_file(TEST_FILE_NAME, test_record_to_write3)
    file_lines=[]
    file_lines_num=0
    with open(TEST_FILE_NAME) as f:
        for line in f.readlines():
            file_lines.append(line)
    
    file_header=str(file_lines[0]).replace("\n","")
    file_record1=str(file_lines[1]).replace("\n","")
    file_record2=str(file_lines[2]).replace("\n","")
    file_record3=str(file_lines[3]).replace("\n","")
    file_len = len(file_lines)
    # Teardown
    remove(TEST_FILE_NAME)

    # Assert
    assert 4 == file_len 
    assert header == file_header 
    assert test_record_to_write1 == file_record1
    assert test_record_to_write2 == file_record2
    assert test_record_to_write3 == file_record3
