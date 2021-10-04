import unittest
import requests as rq
import json


class TestHandlerApiIntentTestHandler(unittest.TestCase):#
    """Test Util Tool"""

    def test_post(self):
        
        data = {"intent" : ["h_問_兌_手續費", "h_問_兌_大類", "h_問_充_不成功", "h_問_兌_到帳時間"]}
        expectedJson = {"response": [
        "报告老板，银行卡兑换收取兑换金币数1.5%的手续费，支付宝兑换收取兑换金币数2%的手续费，（小数点后一位往上取整），单笔兑换低于（包括）150的手续费收取3金币，收取的手续费将用于支付转账时所产生的费用，感谢您的支持。",
        "亲，如果微信和支付宝都充值不了，请选择尊享闪付充值。给您带来不便敬请谅解！",
        "老板，兑换一般5到10分钟到帐的呢，感谢您的支持。"
    ]}
        post_method_reponds = rq.post("http://127.0.0.1:8088/api/intent", json=data)
        
        self.assertEqual(post_method_reponds.json(), expectedJson)
        data = {"intent" : [""]}
        expectedJson = {"response": [
    ]}
        post_method_reponds = rq.post("http://127.0.0.1:8088/api/intent", json=data)
        
        self.assertEqual(post_method_reponds.json(), expectedJson)

if __name__ == '__main__':
    unittest.main()   