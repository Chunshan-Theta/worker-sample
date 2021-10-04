import unittest
from tornado.testing import AsyncTestCase, gen_test
import random
import uuid

from util.aredis_queue import *

class TestUtilqueue(AsyncTestCase):
    """Test Util nlu_queue_asyn"""

    @gen_test(timeout=5)
    def test_push_pop(self):

        self.nlu_queue = nlu_queue_asyn('test')
        # test push pop
        tmpStr = 'mytest' + str(random.randint(0,100))
        yield self.nlu_queue.enqueue(tmpStr)
        retmsg = yield self.nlu_queue.dequeue_nowait()
        self.assertEqual(tmpStr, retmsg)

        del self.nlu_queue

    @gen_test(timeout=5)
    def test_direct_set_get(self):
        self.nlu_queue = nlu_queue_asyn('test')

        # test direct test get
        tmpStr = 'mytest' + str(random.randint(0, 100))
        channel_id = str(uuid.uuid4())

        yield self.nlu_queue.set_msg_by_direct_id_ex(channel_id, 10, tmpStr)
        retmsg = yield self.nlu_queue.get_msg_by_direct_id(channel_id)

        self.assertEqual(tmpStr, retmsg)
        del self.nlu_queue