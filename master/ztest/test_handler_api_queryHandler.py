import unittest
import requests
import json
'''
run `python3 ../util/simpleServer.py` to on worker before run this testcase.
'''

class TestHandlerApiQueryqueryHandler(unittest.TestCase):#
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        self.reponds = None
        self.source_text = None
        self.re = None
        self.mock_retStr = {
            "orig entities": {},
            "intents": [
                {
                    "confidence": 0.9990760946916271,
                    "value": "h_問_登_大類"
                },
                {
                    "confidence": 0.99934014824977,
                    "value": "h_問_登_進不去"
                }
            ],
            "entities": {}
        }
        self.mock_retStr_ans = {'orig entities': {}, 'intents': [{'confidence': 0.99934014824977, 'value': 'h_問_登_進不去'}], 'entities': {}, 'orig intents': [{'confidence': 0.9990760946916271, 'value': 'h_問_登_大類'}, {'confidence': 0.99934014824977, 'value': 'h_問_登_進不去'}]}
        self.mock_retStr_ans2 = {'orig entities': {}, 'intents': [{'confidence': 0.9990760946916271, 'value': 'h_問_登_大類'}, {'confidence': 0.9990760946916271, 'value': 'h_問_兌_手續費'}, {'confidence': 0.9990760946916271, 'value': 'h_問_兌_最低金額'}, {'confidence': 0.9990760946916271, 'value': 'h_問_註_多重註冊'}, {'confidence': 0.9990760946916271, 'value': 'h_問_註_註銷帳號'}], 'entities': {}, 'orig intents': [{'confidence': 0.9990760946916271, 'value': 'h_問_登_大類'}, {'confidence': 0.9990760946916271, 'value': 'h_問_兌_手續費'}, {'confidence': 0.9990760946916271, 'value': 'h_問_兌_大類'}, {'confidence': 0.9990760946916271, 'value': 'h_問_兌_最低金額'}, {'confidence': 0.9990760946916271, 'value': 'h_問_註_多重註冊'}, {'confidence': 0.9990760946916271, 'value': 'h_問_註_大類'}, {'confidence': 0.9990760946916271, 'value': 'h_問_註_註銷帳號'}]}
        self.mock_retStr2 = {
            "orig entities": {},
            "intents": [
                {
                    "confidence": 0.9990760946916271,
                    "value": "h_問_登_大類"
                },{
                    "confidence": 0.9990760946916271,
                    "value": "h_問_兌_手續費"
                },{
                    "confidence": 0.9990760946916271,
                    "value": "h_問_兌_大類"
                },{
                    "confidence": 0.9990760946916271,
                    "value": "h_問_兌_最低金額"
                },{
                    "confidence": 0.9990760946916271,
                    "value": "h_問_註_多重註冊"
                },{
                    "confidence": 0.9990760946916271,
                    "value": "h_問_註_大類"
                },{
                    "confidence": 0.9990760946916271,
                    "value": "h_問_註_註銷帳號"
                },
            ],
            "entities": {}
        }

    @classmethod
    def tearDown(self) -> None:
        del self.reponds
        del self.source_text
        del self.re
        del self.mock_retStr
        del self.mock_retStr_ans

    def test_Equal_text(self):
        pass
        self.source_text = "hello server"
        self.reponds = requests.get('http://127.0.0.1:8088/api/query?msgid=test&q=' + self.source_text,
                                    headers={'token': 'a303f9ee2386e876'})
        print(str(self.reponds.content))

        self.re = json.loads(str(self.reponds.content)[2:-1])
        self.assertEqual(self.re['msgid'], "test")
        self.assertEqual(self.re['retCheck'], True)

