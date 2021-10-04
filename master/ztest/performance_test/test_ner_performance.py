import subprocess
import requests
from locust import HttpLocust, TaskSet, task
import json
IP = "http://127.0.0.1/api/ner"
class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        pass

    # @task(1)
    # def profile(self):
    #     test_data = {
    #         "docs": [
    #             {
    #                 "id": "1",
    #                 "text": "二十位陳家豪 銀行家"
    #             },
    #             {
    #                 "id": "2",
    #                 "text": "經過我們的試算，銀行願意貸款給您941.5萬，利率 百分之5，扣掉您自備款你仍需134.5萬元。謝謝您!請問還有其他問題嗎?"
    #             }
    #         ],
    #         "debug": 1
    #     }
    #     postresponse = self.client.post(IP, headers={"token": "ner_api"}, data=json.dumps(test_data), name="2")

    @task(100)
    def query(self):
        postresponse = self.client.get("http://127.0.0.1:8088/api/query?msgid=test&q=測試", headers= {"token" : "a303f9ee2386e876"})

    # @task(1)
    # def call_5_item(self):
    #     test_data = {
    #         "docs": [
    #             {
    #                 "id": "1",
    #                 "text": "二十位陳家豪 銀行家"
    #             },
    #             {
    #                 "id": "2",
    #                 "text": "經過我們的試算，銀行願意貸款給您941.5萬，利率 百分之5，扣掉您自備款你仍需134.5萬元。謝謝您!請問還有其他問題嗎?"
    #             },
    #             {
    #                 "id": "3",
    #                 "text": "二十位陳家豪 銀行家"
    #             },
    #             {
    #                 "id": "4",
    #                 "text": "經過我們的試算，銀行願意貸款給您941.5萬，利率 百分之5，扣掉您自備款你仍需134.5萬元。謝謝您!請問還有其他問題嗎?"
    #             },
    #             {
    #                 "id": "5",
    #                 "text": "二十位陳家豪 銀行家"
    #             }
    #         ],
    #         "debug": 1
    #     }
    #     postresponse = self.client.post(IP, headers={"token": "ner_api"},
    #                                     data=json.dumps(test_data), name="5")
    #
    # @task(1)
    # def call_10_item(self):
    #     test_data = {
    #         "docs": [
    #             {
    #                 "id": "1",
    #                 "text": "二十位陳家豪 銀行家"
    #             },
    #             {
    #                 "id": "2",
    #                 "text": "經過我們的試算，銀行願意貸款給您941.5萬，利率 百分之5，扣掉您自備款你仍需134.5萬元。謝謝您!請問還有其他問題嗎?"
    #             },
    #             {
    #                 "id": "3",
    #                 "text": "二十位陳家豪 銀行家"
    #             },
    #             {
    #                 "id": "4",
    #                 "text": "經過我們的試算，銀行願意貸款給您941.5萬，利率 百分之5，扣掉您自備款你仍需134.5萬元。謝謝您!請問還有其他問題嗎?"
    #             },
    #             {
    #                 "id": "5",
    #                 "text": "二十位陳家豪 銀行家"
    #             },
    #             {
    #                 "id": "6",
    #                 "text": "二十位陳家豪 銀行家"
    #             },
    #             {
    #                 "id": "7",
    #                 "text": "經過我們的試算，銀行願意貸款給您941.5萬，利率 百分之5，扣掉您自備款你仍需134.5萬元。謝謝您!請問還有其他問題嗎?"
    #             },
    #             {
    #                 "id": "8",
    #                 "text": "二十位陳家豪 銀行家"
    #             },
    #             {
    #                 "id": "9",
    #                 "text": "經過我們的試算，銀行願意貸款給您941.5萬，利率 百分之5，扣掉您自備款你仍需134.5萬元。謝謝您!請問還有其他問題嗎?"
    #             },
    #             {
    #                 "id": "10",
    #                 "text": "二十位陳家豪 銀行家"
    #             }
    #         ],
    #         "debug": 1
    #     }
    #     postresponse = self.client.post(IP, headers={"token": "ner_api"},
    #                                     data=json.dumps(test_data), name="10")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000