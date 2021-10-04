import unittest
import requests as rq
import json


class TestHandlerApiQueryTestHandler(unittest.TestCase):#
    """Test Util Tool"""

    @classmethod
    def setUp(self) -> None:
        pass

    @classmethod
    def tearDown(self) -> None:
        pass

    def test_get(self):
        get_method_reponds = rq.get("http://127.0.0.1:8088/api/config")
        re = str(get_method_reponds.content)[2:-1]
        re = json.loads(re)
        self.assertEqual('config' in re, True)
        return re['config']

        del get_method_reponds, re

    def test_delete(self):
        now_config = self.test_get()
        if 'New_service' not in now_config: self.test_post()
        data = {"config_name": "New_service"}
        del_method_reponds = rq.delete("http://127.0.0.1:8088/api/config", data=data)
        re_delete = json.loads(str(del_method_reponds.content)[2:-1])
        self.assertEqual('Old config' in re_delete, True)
        self.assertEqual('New config' in re_delete, True)
        self.assertEqual(len(re_delete['New config'])+1, len(re_delete['Old config']))

        del data, del_method_reponds, re_delete

    def test_put(self):
        now_config = self.test_get()
        if 'New_service' not in now_config: self.test_post()
        data = {"config":"{ \"token_id\": \"New_service\", \"model_ver\": \"put_test\", \"servers\":[ {\"server_name\":\"nlumdl1\", \"ip\": \"xxx.xxx.xxx.xxx\", \"workers\": [ { \"worker_name\":\"nlumdl1-eryuij345236sfdagete-wk1\", \"MQip\":\"127.0.0.1\", \"MQport\": 6379 } ]} ] }"}
        put_method_reponds = rq.put("http://127.0.0.1:8088/api/config", data=data)
        re_put = json.loads(str(put_method_reponds.content)[2:-1])
        self.assertEqual('Old config' in re_put, True)
        self.assertEqual('New config' in re_put, True)
        self.assertEqual('put_test', re_put['New config']['New_service']['servers']['model_ver'])

        del data, put_method_reponds, re_put

    def test_post(self):
        now_config = self.test_get()
        if 'New_service' in now_config: self.test_delete()
        data = {"config":"{ \"token_id\": \"New_service\", \"model_ver\": \"silkBERTJoinV1\", \"servers\":[ {\"server_name\":\"nlumdl1\", \"ip\": \"xxx.xxx.xxx.xxx\", \"workers\": [ { \"worker_name\":\"nlumdl1-eryuij345236sfdagete-wk1\", \"MQip\":\"127.0.0.1\", \"MQport\": 6379 } ]} ] }"}
        post_method_reponds = rq.post("http://127.0.0.1:8088/api/config", data=data)
        re_post = json.loads(str(post_method_reponds.content)[2:-1])
        self.assertEqual('Old config' in re_post, True)
        self.assertEqual('New config' in re_post, True)
        self.assertEqual(len(re_post['New config'])-1, len(re_post['Old config']))

        del data, post_method_reponds, re_post
