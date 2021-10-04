import random
import unittest

from util.tools import *


class TestUtilTool(unittest.TestCase):
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        self.CapHist = CappedHistogram(50)

        for i in range(0, 50):
            self.CapHist[str(i)] = 0

        for i in range(0, 100):
            self.CapHist[str(random.randint(0, 49))] += 1

    @classmethod
    def tearDown(self) -> None:
        del self.CapHist

    def test_total_size(self):
        """Test """
        self.assertEqual(50, self.CapHist.total_size())
