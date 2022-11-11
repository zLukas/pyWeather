from unittest import TestCase
from unittest.mock import patch
from loger import RemoteDrive


class Test_Remotedrive(TestCase):

    def test_init_class(self):
        test_drive = RemoteDrive()
        self.assertIsNotNone(test_drive)

    def test_init_class_no_submodule():
        test_drive = RemoteDrive()


    def test_init_class_no_creds_file():
        pass

    def test_init_class_creds_file_exist():
        pass

    def test_push_file_file_exist():
        pass

    def test_push_file_not_exist();
        pass




