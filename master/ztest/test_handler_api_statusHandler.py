import unittest
import requests
import json


class TestHandlerApiQueryTestHandler(unittest.TestCase):#
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        self.source_text = "hello server"
        self.reponds = requests.get('http://127.0.0.1:8088/api/status')
        self.source_text = self.source_text

    @classmethod
    def tearDown(self) -> None:
        del self.reponds
        del self.source_text

    def test_Equal_text(self):
        re = json.loads(str(self.reponds.content)[2:-1])
        self.assertEqual('PreviousRequest_str' in re, True)
        self.assertEqual('average_time' in re, True)

