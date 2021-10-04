"""
    Extract regular expression value from the current utterance.
    The output will be a data structure containing:
        [Start position,
         Content length,
         Current type]
"""

from util.query_tool import retStr_filter
import unittest

"""
您好，我的支付订单号是2019053000006095，我对此订单有疑问，疑问是：支付宝显示的订单号
我的電話155 -9353 - 2412
我的遊戲帳號是10149747
"""


class TestSlotDecoderTool(unittest.TestCase):

    """Test Util Tool"""
    @classmethod
    def setUp(self) -> None:
        self.sample1 = {
                "intents": [
                    {
                        "confidence": 0.9998619077977099,
                        "value": "h_問_回_大類"
                    },{
                        "confidence": 0.9998619077977099,
                        "value": "h_問_回_QQ未回"
                    }
                ]
            }
        self.sample2 = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_大類"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_QQ未回"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_代理未回"
                }
            ]
        }
        self.sample3 = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_催促"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_QQ未回"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_代理未回"
                }
            ]
        }
        self.sample4 = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                },
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_QQ未回"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_代理未回"
                }
            ]
        }
        self.sample5 = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                },
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_QQ未回"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_代理未回"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_快點快點"
                }
            ]
        }
        self.sample6 = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_大類"
                },
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_QQ未回"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_問_回_代理未回"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_快點快點"
                }
            ]
        }
    def test_common_filter(self):
        result = retStr_filter(self.sample6)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_問_回_大類'},
                     {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'},
                     {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'},
                     {'confidence': 0.9998619077977099, 'value': 'h_快點快點'}],
         'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_問_回_大類'},
                          {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'},
                          {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'},
                          {'confidence': 0.9998619077977099, 'value': 'h_快點快點'}],
         'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_快點快點'},
                             {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'},
                             {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}]}


        print(result)
        self.assertEqual(result,ans)

    def test_common_1(self):
        result = retStr_filter(self.sample1)
        #print(result)
        ans ={
             'intents': [{'confidence': 0.9998619077977099, 'value': 'h_問_回_大類'},
                         {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'}],
             'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_問_回_大類'},
                              {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'}],
             'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'}]
        }

        self.assertEqual(result, ans)

    def test_common_2(self):
        result = retStr_filter(self.sample3, token_id='pass')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促'},
                     {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'},
                     {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}],
         'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促'},
                          {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'},
                          {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}],
         'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促'},
                             {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'},
                             {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}]}

        self.assertEqual(result, ans)
    def test_common_contain(self):
        result = retStr_filter(self.sample4, token_id='pass')
        print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'},
                     {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'},
                     {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}],
         'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'},
                          {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'},
                          {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}],
         'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'},
                             {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'},
                             {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}]}

        self.assertEqual(result, ans)
    def test_common_fit_two_filter(self):
        result = retStr_filter(self.sample5, token_id='pass')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}, {'confidence': 0.9998619077977099, 'value': 'h_快點快點'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}, {'confidence': 0.9998619077977099, 'value': 'h_快點快點'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}, {'confidence': 0.9998619077977099, 'value': 'h_快點快點'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}]}


        self.assertEqual(result, ans)
    def test_combine(self):
        result = retStr_filter(self.sample2, token_id='pass')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_問_回_大類'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_問_回_大類'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_問_回_QQ未回'}, {'confidence': 0.9998619077977099, 'value': 'h_問_回_代理未回'}]}

        self.assertEqual(result,ans)

    def test_example_dadd031d4af39d04_money_error(self):
        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_提供未到帳資訊"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}],
         'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}],
         'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}]}
        self.assertEqual(result,ans)

        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}]}

        self.assertEqual(result, ans)

        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_充值"
                }
            ]
        }
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_充值未到帳'}]}

        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)

        self.assertEqual(result, ans)


        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_提供未到帳資訊"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_充值"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_充值未到帳'}]}

        self.assertEqual(result, ans)
        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_兌換"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_未到帳'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_兌換未到帳'}]}

        self.assertEqual(result, ans)


        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_提供未到帳資訊"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_兌換"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_兌換未到帳'}]}

        self.assertEqual(result, ans)

    def test_example_dadd031d4af39d04_timeout(self):
        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_等待時間已過"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}]}


        self.assertEqual(result, ans)


        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_催促或等候太久"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_提供未到帳資訊"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_充值"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans =  {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促充值未到帳'}]}

        self.assertEqual(result, ans)


        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_催促或等候太久"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_充值"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促充值未到帳'}]}

        self.assertEqual(result, ans)



        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_等待時間已過"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_提供未到帳資訊"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_充值"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促充值未到帳'}]}

        self.assertEqual(result, ans)


        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_等待時間已過"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_充值"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_充值'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促充值未到帳'}]}
        self.assertEqual(result, ans)

        ##h_兌換
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_催促或等候太久"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_提供未到帳資訊"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_兌換"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促兌換未到帳'}]}

        self.assertEqual(result, ans)


        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_催促或等候太久"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_兌換"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促兌換未到帳'}]}

        self.assertEqual(result, ans)



        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_等待時間已過"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_提供未到帳資訊"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_兌換"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促兌換未到帳'}]}

        self.assertEqual(result, ans)


        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_等待時間已過"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_兌換"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_兌換'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促兌換未到帳'}]}

        self.assertEqual(result, ans)

        ## h_催促未到帳
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_催促或等候太久"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_提供未到帳資訊"
                },
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促未到帳'}]}

        self.assertEqual(result, ans)


        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_催促或等候太久"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促未到帳'}]}

        self.assertEqual(result, ans)



        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_等待時間已過"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_提供未到帳資訊"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_提供未到帳資訊'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促未到帳'}]}

        self.assertEqual(result, ans)


        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_等待時間已過"
                },{
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        #print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'}], 'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促未到帳'}]}

        self.assertEqual(result, ans)

    def test_example_dadd031d4af39d04_timeout_2(self):
        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_等待時間已過"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_未到帳"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_測試"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        print(result)
        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'}, {'confidence': 0.9998619077977099, 'value': 'h_未到帳'},
                           {'confidence': 0.9998619077977099, 'value': 'h_測試'}],
               'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'},
                                {'confidence': 0.9998619077977099, 'value': 'h_未到帳'},
                                {'confidence': 0.9998619077977099, 'value': 'h_測試'}],
               'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_測試'},
                                   {'confidence': 0.9998619077977099, 'value': 'h_催促未到帳'}]}




        self.assertEqual(result, ans)

        ##
        sample = {
            "intents": [
                {
                    "confidence": 0.9998619077977099,
                    "value": "h_等待時間已過"
                }, {
                    "confidence": 0.9998619077977099,
                    "value": "h_催促或等候太久"
                }
            ]
        }
        result = retStr_filter(sample, token_id='dadd031d4af39d04')
        print(result)

        ans = {'intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'},
                           {'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}],
               'orig intents': [{'confidence': 0.9998619077977099, 'value': 'h_等待時間已過'},
                                {'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}],
               'combine_intents': [{'confidence': 0.9998619077977099, 'value': 'h_催促或等候太久'}]}


        self.assertEqual(result, ans)