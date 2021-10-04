"""
    Extract regular expression value from the current utterance.
    The output will be a data structure containing:
        [Start position,
         Content length,
         Current type]
"""

from util.regular_expression_extract import REExtract
import unittest
import requests
import json

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

    def test_pre_process(self):
        with open("./test_sample/前處理範例.txt","r") as f:
            rows = f.readlines()

        for idx,row in enumerate(rows):
            print('+'*20)
            label_txt, label, content = row.split(",")

            headers = {
                "token": "a303f9ee2386e876"
            }

            contents = requests.get("http://127.0.0.1:80/api/query?debug=1&q={}".format(content), headers=headers)

            print(idx, content, json.loads(contents.text)['retStr']['pre entities'],label_txt)
            obj = json.loads(contents.text)['retStr']['pre entities']
            if label_txt != "UNKNOWN":
                self.assertTrue(self.in_entities(obj, label_txt, label))
            else:
                self.assertTrue((obj == {} or label not in obj))

    def in_entities(self, obj, label_txt, label):
        print(obj)

        if label not in obj:
            return False
        for a in obj[label]:
            if label_txt in a:
                return True

        return False

    def test_pre_process_all(self):
        with open("./test_sample/全部句子.txt","r") as f:
            rows = f.readlines()

        with open("./test_sample/temp.txt", "w") as f:
            for idx,row in enumerate(rows):
                #print('+'*20)
                content = row

                headers = {
                    "token": "a303f9ee2386e876"
                }

                contents = requests.get("http://127.0.0.1:80/api/query?debug=1&q={}".format(content), headers=headers)

                #print(idx, content, json.loads(contents.text)['retStr']['pre entities'])
                obj = json.loads(contents.text)['retStr']['pre entities']
                print(idx,content, obj)
                temp_str = []
                for label_key,val in obj.items():
                    for label_value,sub_val in val.items():
                        temp_str.append("('原始內容'={sample_text},轉換後內容={converted_text}, => {label}:{value})".format(sample_text=sub_val['原始內容'],converted_text=sub_val['轉換後內容'],label=label_key, value=label_value))
                if len(temp_str) == 0:
                    temp_str = "()"
                elif len(temp_str)!=0:
                    print(temp_str)
                    temp_str = sorted(temp_str)
                    print(temp_str)
                    temp_str = "".join(temp_str)
                f.write(temp_str)
                f.write('\n')
