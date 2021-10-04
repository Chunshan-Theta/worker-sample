import requests


def test_sample(server_ip, token, q="华夏总代理充值17.01时间14:39"):
    url = f"http://{server_ip}/api/query?debug=0&q={q}"

    payload = {}
    headers = {
      'token': token
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    return response.text.encode('utf8')



import unittest
from util.config import *


class TestUtilConfig(unittest.TestCase):
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        pass

    @classmethod
    def tearDown(self) -> None:
        pass

    def test_compare_loacl_and_server1(self):

        for q in SAMPLE_TEXT:
            source = json.loads(test_sample("127.0.0.1:8088", token='thor_0319',q=q))
            target = json.loads(test_sample("10.205.50.23", token='thor_0319',q=q))

            source.pop('msgid')
            target.pop('msgid')
            del target["retStr"]["all_intents"]
            print(source)
            print(target)
            self.assertEqual(source, target)

    def test_compare_loacl_and_server2(self):

        for q in SAMPLE_TEXT:
            source = json.loads(test_sample("127.0.0.1:8088", token='369f26f3d7704705a132d21a8cf67c3a',q=q))
            target = json.loads(test_sample("10.205.50.2", token='369f26f3d7704705a132d21a8cf67c3a',q=q))

            source.pop('msgid')
            target.pop('msgid')
            print(source)
            print(target)
            self.assertEqual(source, target)



SAMPLE_TEXT=[
"我要看屍速列車",
"玩命關頭 早場",
"全面攻佔，12/7下午有場次嗎？",
"12/6的怪胎",
"翻供12/10午夜場",
"天能早場",
"九月十號的葉問",
"9/20早場",
"john@gmail.com",
"john1@gmail.com",
"john2@gmail.com",
"john4@gmail.com",
"john6@gmail.com",
"台北市內湖區民權東路",
"台北市忠孝東路",
"新竹市阿哩不搭路",
"台東知本鄉",
"新北市汐止區忠孝東路",
"這是我的 john123@gmail.com",
"john1@gmail.com 拉",
"john1@gmail.com 喔",
"信箱 john1@gmail.com",
"電子信箱john1@gmail.com 拉",
"寄信到 john1@gmail.com",
"我家地址 台北市內湖區民權東路",
"地址 台北市內湖區民權東路",
"我住在 台北市內湖區民權東路",
"可以來 台北市內湖區民權東路",
"來 地址 台北市內湖區民權東路 我家",
"陳先生 0912-323-302",
"陳小姐0919292932",
"0965432228彭于晏",
"我叫林志玲0922337799",
"0912302232 王一二",
"一張軍警一張學生",
"三張學生票",
"敬老票一張",
"我要兩張全票",
"四張學生票 兩張全票",
]