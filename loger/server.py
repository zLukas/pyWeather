from pyDrive.googleApi import DriveLogin
from pyDrive.googleApi import DriveFiles

class Server():
    def __init__(self, token):
        self.instance=DriveLogin()
        self.api_service = self.instance.api_login()
        

    def init_server_connection(self):
        if self.api_service is None:
            self.api_service = self.instance.api_login()
        else:
            pass


    def send_file_to_server(filename, remote_dir_name):
        # send old file to server
        # remove old file
        pass



s
