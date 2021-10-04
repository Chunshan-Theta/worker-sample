import unittest
import random

from util.status import *


class TestUtilStatus_PreviousRequest_100(unittest.TestCase):
    """Test Util Status Class"""

    @classmethod
    def setUp(self) -> None:
        self.status_obj = PreviousRequest_100()

    @classmethod
    def tearDown(self) -> None:
        del self.status_obj

    def test_add_records(self):
        """Test """
        for _ in range(10):
            self.status_obj.add_record("test-label", {"exe-time": random.uniform(0.0001, 0.09)})

        self.assertEqual(10, len(self.status_obj.records))

    def test_update_average_time(self):
        """Test """
        for _ in range(15):
            self.status_obj.add_record("test-label", {"exe-time": 0.01})

        self.assertEqual(0.01, self.status_obj.average_time)

    def test_get_record(self):
        """Test """
        self.status_obj.add_record("test-label", {"exe-time": 0.01})
        self.assertEqual(1, len(self.status_obj.get_record()))


class TestUtilStatus_PreviousRequest(unittest.TestCase):
    """Test Util Status Class"""

    @classmethod
    def setUp(self) -> None:
        self.status_obj = PreviousRequest()

    @classmethod
    def tearDown(self) -> None:
        del self.status_obj

    def test_add_records(self):
        """Test """
        for _ in range(10):
            self.status_obj.add_record("test-label", {"exe-time": random.uniform(0.0001, 0.09)})

        self.assertEqual(type(self.status_obj.records), str)

    def test_get_record(self):
        """Test """
        self.status_obj.add_record("test-label", {"exe-time": 0.01})
        self.assertEqual(str, type(self.status_obj.get_record()))
