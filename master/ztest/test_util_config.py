import random
import unittest
import json
from util.config import *


class TestUtilConfig(unittest.TestCase):
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        self.obj = {
            "token_id": "eryuij345236sfdagete",
            "model_ver": "silkRuleBasedV1",
            "servers":[
                    {"server_name":"nlumdl1",
                    "ip": "xxx.xxx.xxx.xxx",
                    "workers": [
                        {
                          "worker_name":"nlumdl1-eryuij345236sfdagete-wk1",
                          "MQip":"localhost",
                          "MQport": 6379
                        },
                        {
                          "worker_name":"nlumdl1-eryuij345236sfdagete-wk1",
                          "MQip":"localhost",
                          "MQport": 6379
                        }]
                    }]
            }
        self.user_service = UserConfig(self.obj)



    @classmethod
    def tearDown(self) -> None:
        del self.user_service
        del self.obj

    def test_total_size(self):
        self.assertEqual(1, len(self.user_service.servers))

    def test_get_worker(self):
        self.assertEqual("nlumdl1-eryuij345236sfdagete-wk1", self.user_service.servers[0].workers[0].worker_name)
        self.assertEqual("localhost", self.user_service.servers[0].workers[0].MQip)
        self.assertEqual(6379, self.user_service.servers[0].workers[0].MQport)

    def test_update_config(self):
        temp_arr = []
        for i in range(1, 4):
            temp_txt = {}
            for k, v in self.obj.items():
                temp_txt[k] = v

            temp_txt["token_id"] = "_" + str(i)
            temp_arr.append(UserConfig(temp_txt).config)
        self.assertEqual(3, len(update_config(temp_arr)))

    def test_print_config(self):
        print(str(self.user_service))

