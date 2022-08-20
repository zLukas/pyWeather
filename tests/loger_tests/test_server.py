from unittest.mock import Mock
import sys
sys.modules['pyDrive.googleApi'] = Mock()

def init_server_connection_failed():
    pass

def init_server_connection_passed():
    pass

def is_local_file_ready_to_send_yesterday_file():
    pass

def is_local_file_ready_to_send_no_file():
    pass

def is_local_file_ready_to_send_current_file():
    pass

def send_file_to_server_passed():
    pass

def send_file_to_server_auth_error():
    pass

def send_file_to_server_connection_broken():
    pass

def send_file_to_serves_no_remote_folder():
    pass

def send_file_to_server_no_file():
    pass

def send_file_to_server_file_already_exist():
    pass