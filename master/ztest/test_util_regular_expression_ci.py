"""
    Extract regular expression value from the current utterance.
    The output will be a data structure containing:
        [Start position,
         Content length,
         Current type]
"""

from util.regular_expression_extract import REExtract
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
        self.extract = REExtract()

    def test_Slot_game_account(self):
        re = self.extract.extract("我的遊戲帳號是10149747,10000499012019060100080082239209")
        ans = [{'start_pos': 6, 'utte_len': 10, 'sample_label': 'game-account-number:遊戲帳號:slot', 'sample_text': '是10149747,'}]
        #print(re)
        for a in ans:
            self.assertIn(a, re)
    def test_Slot_game_account_1(self):
        re = self.extract.extract("10149747")
        ans = [{'start_pos': 0, 'utte_len': 8, 'sample_label': 'game-account-number:遊戲帳號:slot', 'sample_text': '10149747'}]
        print(re)
        for a in ans:
            self.assertIn(a, re)

    def test_Slot_order_number(self):
        re = self.extract.extract("我的遊戲帳號是10149747,190530-640335217311098")
        ans = [{'start_pos': 16, 'utte_len': 22, 'sample_label': '訂單號:訂單號:slot', 'sample_text': '190530-640335217311098'}]
        for a in ans:
            self.assertIn(a, re)

    def test_intent_order_question(self):
        re = self.extract.extract("您好，我的支付订单号是2019053000006095，我对此订单有疑问，疑问是：支付宝显示的订单号是。。20190530200040011100500064452376已支付成功超过十分钟还没到账")
        ans = [{'start_pos': 11, 'utte_len': 16, 'sample_label': '訂單號:訂單號:slot', 'sample_text': '2019053000006095'}]
        #print(re)
        for a in ans:
            self.assertIn(a,re)

    def test_intent_phone_number(self):
        re = self.extract.extract("您好，我的支付订单号是2019053000006095, 我的電話155 - 9353 - 2412,支付寶 12w")
        ans = [{'start_pos': 32, 'utte_len': 19, 'sample_label': 'tel-number:電話號碼:slot', 'sample_text': '話155 - 9353 - 2412,'}]
        #print(re)
        for a in ans:
            self.assertIn(a, re)

    def test_intent_MON_w(self):
        re = self.extract.extract("充值12.37w")
        ans = [{'start_pos': 2, 'utte_len': 6, 'sample_label': '金額:金額_w萬:slot', 'sample_text': '12.37w'}]
        for a in ans:
            self.assertIn(a, re)

    def test_intent_today(self):
        re = self.extract.extract("今天")
        ans = [{'start_pos': 0, 'utte_len': 2, 'sample_label': '日期:今天:backup', 'sample_text': '今天'}]

        for a in ans:
            self.assertIn(a, re)

    def test_intent_cha1(self):
        re = self.extract.extract("支付寶")
        ans = [{'start_pos': 0, 'utte_len': 3, 'sample_label': '充值渠道:支付寶:backup', 'sample_text': '支付寶'}]
        for a in ans:
            self.assertIn(a, re)

    def test_intent_cha2(self):
        re = self.extract.extract("閃付")
        ans = [{'start_pos': 0, 'utte_len': 2, 'sample_label': '充值渠道:尊享閃付:backup', 'sample_text': '閃付'}]
        for a in ans:
            self.assertIn(a, re)

    def test_intent_cha3(self):
        re = self.extract.extract("云閃付")
        self.assertEqual(re,[])

    def test_intent_Mon_1(self):
        re = self.extract.extract("2019-05-3023:50300元")
        print(re)

    def test_intent_order(self):
        re = self.extract.extract("您好，我的支付订单号是2019053000006095，我对此订单有疑问，疑问是：支付宝显示的订单号")
        ans = [{'start_pos': 11, 'utte_len': 16, 'sample_label': '訂單號:訂單號:slot', 'sample_text': '2019053000006095'}]
        for a in ans:
            self.assertIn(a, re)

    def test_intent_Date1(self):
        re = self.extract.extract("11/3")
        assert  {'start_pos': 0, 'utte_len': 4, 'sample_label': '日期:標準日期:slot', 'sample_text': '11/3'} in re

    def test_intent_Date2(self):
        re = self.extract.extract("2019/10/29")
        print(re)
        assert {'start_pos': 0, 'utte_len': 10, 'sample_label': '日期:標準日期:slot', 'sample_text': '2019/10/29'} in re

    def test_intent_Date3(self):
        re = self.extract.extract("2018/10/23")
        print(re)
        assert {'start_pos': 0, 'utte_len': 10, 'sample_label': '日期:標準日期:slot', 'sample_text': '2018/10/23'} in re

    def test_intent_Date4(self):
        re = self.extract.extract("2018/02/17的这个订单我只有这一个支付凭证，我这笔订单到现在都没有进帐")
        print(re)
        assert {'start_pos': 0, 'utte_len': 11, 'sample_label': '日期:標準日期:slot', 'sample_text': '2018/02/17的'} in re
    def test_intent_Date5(self):
        re = self.extract.extract("的这个订单我只有这一个支付凭证，我这笔订单到现在都没有进帐2018/02/17")
        print(re)
        assert {'start_pos': 28, 'utte_len': 11, 'sample_label': '日期:標準日期:slot', 'sample_text': '帐2018/02/17'} in re

    def test_intent_Date6(self):
        re = self.extract.extract("安2018/10/23安")
        print(re)
        assert {'start_pos': 0, 'utte_len': 12, 'sample_label': '日期:標準日期:slot', 'sample_text': '安2018/10/23安'} in re

