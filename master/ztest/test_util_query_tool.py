import unittest
import requests
import json
from util.query_tool import in_entities,in_sentence
'''
run `python3 ../util/simpleServer.py` to on worker before run this testcase.
'''

class TestHandlerApiQueryqueryHandler(unittest.TestCase):#
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        pass
    def test_in_entities(self):

        entities_dict ={
            "時間": [
                "18:25"
            ]
        }

        entities_str = 18
        self.assertTrue(in_entities(entities_dict, entities_str))

    def test_in_entities2(self):

        entities_dict ={'金額': ['300.0'], '日期': ['2019-05-03']}

        entities_str = '3000000.0'
        self.assertTrue(in_entities(entities_dict, entities_str))

    def test_in_sentence(self):

        entities_dict =[[3000000.0,300.0],[3000000.0,"300w"]]

        self.assertTrue(in_sentence(entities_dict))


