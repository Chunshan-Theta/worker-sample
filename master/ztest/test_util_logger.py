import unittest
from util.logger import log_Object
import logging
import os

class TestLogTool(unittest.TestCase):
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        self.log_file_name = "./just_for_test.delete.me"
        self.logger = log_Object().init_logger(log_file_prefix=self.log_file_name)

    @classmethod
    def tearDown(self) -> None:
        try:
            os.remove(self.log_file_name)
        except Exception:
            pass

        del self.logger
        del self.log_file_name

    def test_log_Handler_num(self) -> None:
        """Test """
        self.assertEqual(2, len(self.logger.handlers))



